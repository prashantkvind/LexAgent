import logging
from typing import Dict, Any, Optional
from src.agent.state import LexAgentState, StepLog
from src.tools.local_rag_tool import LocalRAGTool
from src.tools.online_search_tool import OnlineSearchTool
from src.tools.legal_drafting_tool import LegalDraftingTool
from src.utils.llm_factory import get_llm

logger = logging.getLogger(__name__)

class LexAgentController:
    """
    Multi-Tool Legal Agent Controller following the 5-Step Reasoning Engine Workflow:
    Step 1: Analysis (Request breakdown into client facts, applicable law, target outcome)
    Step 2: Fact Retrieval (Local RAG over RTI/private docs)
    Step 3: Law Search (Online Legal Search for RERA Acts & High Court precedents)
    Step 4: Synthesis & Strategy (Formulating 100% success action plan)
    Step 5: Drafting (Generating downloadable .docx legal notice if requested)
    """

    def __init__(self):
        self.llm = get_llm()
        self.local_rag_tool = LocalRAGTool()
        self.online_search_tool = OnlineSearchTool()
        self.legal_drafting_tool = LegalDraftingTool()

    def process_query(self, query: str, wants_draft: bool = False, client_name: str = "Shri Rajesh Sharma") -> LexAgentState:
        """
        Executes the full 5-step agentic workflow for a given legal query.
        """
        state = LexAgentState(
            query=query,
            wants_draft=wants_draft,
            client_name=client_name
        )

        # ----------------------------------------------------
        # Step 1: Deconstruct & Analyze Legal Problem
        # ----------------------------------------------------
        state.step_logs.append(StepLog(
            step_num=1,
            step_name="Step 1: Query Analysis",
            description="Deconstructing query into Client Facts, Applicable Law, and Desired Legal Outcome..."
        ))
        
        prompt_analysis = f"Analyze the following legal query and extract key legal components:\nQuery: {query}"
        analysis_res = self.llm.invoke(prompt_analysis)
        state.analysis = str(analysis_res)

        # ----------------------------------------------------
        # Step 2: Fact Retrieval (Local RAG Tool)
        # ----------------------------------------------------
        state.step_logs.append(StepLog(
            step_num=2,
            step_name="Step 2: Private Fact Retrieval (Local RAG)",
            description="Executing Local RAG Tool to search private RTI replies and sanction documents in ChromaDB..."
        ))
        
        rag_output = self.local_rag_tool.run(query)
        state.local_rag_output = rag_output

        # ----------------------------------------------------
        # Step 3: Law & Precedent Search (Online Search Tool)
        # ----------------------------------------------------
        state.step_logs.append(StepLog(
            step_num=3,
            step_name="Step 3: Online Law & HC Precedent Search",
            description="Executing Online Legal Search Tool for RERA Act provisions and High Court rulings..."
        ))
        
        search_output = self.online_search_tool.run(query)
        state.online_search_output = search_output

        # ----------------------------------------------------
        # Step 4: Legal Synthesis & 100% Action Strategy Plan
        # ----------------------------------------------------
        state.step_logs.append(StepLog(
            step_num=4,
            step_name="Step 4: Strategy Synthesis & Action Plan",
            description="Synthesizing private facts and online precedents into a 100% success-oriented legal action plan..."
        ))
        
        prompt_synthesis = (
            f"User Legal Query: {query}\n\n"
            f"Retrieved Private Facts (Step 2):\n{rag_output.get('formatted_output', '')}\n\n"
            f"Online Legal Precedents (Step 3):\n{search_output.get('formatted_output', '')}\n\n"
            f"Synthesize a clear, actionable legal advice and step-by-step strategy."
        )
        
        synthesis_res = self.llm.invoke(prompt_synthesis)
        state.synthesis_output = str(synthesis_res)
        state.final_advice = str(synthesis_res)

        # ----------------------------------------------------
        # Step 5: Document Drafting (Optional / Requested)
        # ----------------------------------------------------
        if wants_draft or "draft" in query.lower() or "notice" in query.lower() or "generate" in query.lower():
            state.step_logs.append(StepLog(
                step_num=5,
                step_name="Step 5: Legal Document Drafting (.docx)",
                description="Executing Legal Drafting Tool to generate formal Legal Notice under python-docx..."
            ))
            
            facts_text = rag_output.get('formatted_output', 'Missing amenities confirmed via RTI inspection.')
            draft_res = self.legal_drafting_tool.run(
                doc_type="LEGAL NOTICE",
                client_name=client_name,
                opposite_party=state.opposite_party,
                facts=facts_text,
                statutes="Section 14 & Section 18 of the Real Estate (Regulation and Development) Act, 2016 (RERA)",
                demands="1. Construct and deliver promised swimming pool/common facilities within 30 days.\n2. Pay compensation interest at 10.75% p.a. under RERA Section 18."
            )
            
            state.draft_output = draft_res
            state.generated_file_path = draft_res.get("file_path")
            state.generated_file_name = draft_res.get("file_name")

        return state
