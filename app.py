import os
import streamlit as st
from pathlib import Path
from src.agent.controller import LexAgentController
from config import GENERATED_DOCS_DIR, PRIVATE_DOCS_DIR

# Page Setup
st.set_page_config(
    page_title="LexAgent - Legal RERA/HC Advisor Agent",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Design & Visual Excellence
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 24px;
    }
    .badge-rag {
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .badge-web {
        background-color: #FEE2E2;
        color: #B91C1C;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.85rem;
    }
    .step-box {
        background-color: #F8FAFC;
        border-left: 4px solid #2563EB;
        padding: 12px 16px;
        margin-bottom: 8px;
        border-radius: 4px;
    }
    .stDownloadButton>button {
        background-color: #16A34A !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Controller in Session State
if "controller" not in st.session_state:
    st.session_state.controller = LexAgentController()

# Header
st.markdown("<h1 class='main-title'>⚖️ LexAgent: Legal RERA & High Court Advisor</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Tool-Augmented Legal Reasoning Agent combining <b>Local Private RAG</b>, <b>Online Case Precedents</b>, and <b>Automated Legal Notice Drafting</b>.</p>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/scales.png", width=80)
    st.header("⚙️ Agent Controls")
    
    client_name = st.text_input("Client Full Name", value="Shri Rajesh Sharma")
    opposite_party = st.text_input("Promoter / Builder Name", value="M/s Royal Palms Infrastructure Pvt Ltd")
    
    st.markdown("---")
    st.subheader("📚 Local Knowledge Base")
    private_files = [f for f in Path(PRIVATE_DOCS_DIR).rglob("*.*") if f.is_file()]
    if private_files:
        for f in private_files:
            rel_f = f.relative_to(PRIVATE_DOCS_DIR)
            st.caption(f"📄 `{rel_f}`")
    else:
        st.warning("No files in private_docs/")
        
    st.markdown("---")
    st.caption("Powered by LangChain • ChromaDB • Tavily • python-docx")

# Main Interface Layout
col_left, col_right = st.columns([1.2, 0.8])

with col_left:
    st.subheader("❓ Ask Legal Question")
    
    # One-click sample prompts
    sample_query = "The builder promised a swimming pool in brochure, but RTI response confirms OC was issued without it. What is the best 100% action plan?"
    
    if st.button("💡 Load Example Query"):
        st.session_state["user_query_input"] = sample_query

    query = st.text_area(
        "Enter query details (facts, RTI findings, or legal issue):",
        height=120,
        key="user_query_input",
        placeholder="e.g. Builder delayed possession by 18 months and omitted promised clubhouse..."
    )
    
    wants_draft = st.checkbox("📄 Generate downloadable Legal Notice (.docx)", value=True)
    
    run_btn = st.button("🚀 Analyze & Generate Advice", type="primary", use_container_width=True)

if run_btn and query:
    st.session_state.controller.legal_drafting_tool.output_dir = Path(GENERATED_DOCS_DIR)
    
    with st.spinner("LexAgent is analyzing request and executing tool sequence..."):
        state = st.session_state.controller.process_query(
            query=query,
            wants_draft=wants_draft,
            client_name=client_name
        )
        st.session_state["agent_result_state"] = state

# Display Results if state exists
if "agent_result_state" in st.session_state:
    state = st.session_state["agent_result_state"]
    
    st.markdown("---")
    
    # 1. Step Trajectory Log
    with st.expander("🧠 Agent Reasoning Trajectory & Tool Execution Log", expanded=True):
        for log in state.step_logs:
            st.markdown(f"<div class='step-box'><b>{log.step_name}</b><br>{log.description}</div>", unsafe_allow_html=True)

    # 2. Main Output Tabs
    tab_strategy, tab_rag, tab_search, tab_draft = st.tabs([
        "📜 Best Action Strategy", 
        "📄 Private RAG Sources (Tool 1)", 
        "🌐 Online Precedents (Tool 2)", 
        "📥 Document Download (Tool 3)"
    ])

    with tab_strategy:
        st.subheader("🎯 Synthesized Legal Strategy & 100% Action Plan")
        st.info("Source Attribution: Primary RAG (Local RTI Records) + General Legal LLM & HC Precedents")
        st.markdown(state.final_advice)

    with tab_rag:
        st.subheader("📄 Private Knowledge Base Findings")
        if state.local_rag_output and state.local_rag_output.get("sources"):
            for src in state.local_rag_output["sources"]:
                st.markdown(f"<span class='badge-rag'>File: {src['filename']}</span> (Chunk #{src['chunk']} | Match Similarity Distance: {src['distance']})", unsafe_allow_html=True)
            st.markdown("---")
            st.text_area("RAG Retrieved Context Snippets", value=state.local_rag_output.get("formatted_output", ""), height=250)
        else:
            st.warning("No matching private documents found in `private_docs/`.")

    with tab_search:
        st.subheader("🌐 Online Legal Search References & RERA Acts")
        if state.online_search_output and state.online_search_output.get("results"):
            st.caption(f"Search Provider: **{state.online_search_output.get('provider')}**")
            for item in state.online_search_output["results"]:
                st.markdown(f"🔹 **[{item['title']}]({item['url']})**")
                st.caption(item["snippet"])
                st.markdown("---")

    with tab_draft:
        st.subheader("📄 Download Formal Legal Notice (.docx)")
        if state.generated_file_path and os.path.exists(state.generated_file_path):
            st.success(f"Legal Notice document successfully created: **{state.generated_file_name}**")
            with open(state.generated_file_path, "rb") as file_data:
                st.download_button(
                    label="📥 Download Legal Notice (.docx)",
                    data=file_data,
                    file_name=state.generated_file_name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.info("Check 'Generate downloadable Legal Notice' checkbox before running query to create a .docx document.")
