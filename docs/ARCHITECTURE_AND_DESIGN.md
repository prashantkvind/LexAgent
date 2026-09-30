# 🏛️ LexAgent: System Architecture & Technical Design Specification

> **Project Name**: LexAgent (Legal RERA / High Court Advisor Agent)  
> **Architecture Pattern**: Tool-Augmented Agentic Controller (LangChain / ChromaDB / Local LLM)  
> **Target Execution**: Local Laptop (Zero Mandatory Cloud Dependencies)  

---

## 📐 1. Architectural Overview

LexAgent is built as a **Tool-Augmented Legal Reasoning Agent**. The system uses an **LLM Controller** as the central decision maker. Based on the user's legal query, the controller orchestrates a **5-step reasoning trajectory**, executing local document retrieval, online legal search, strategy synthesis, and automated legal notice generation in sequence.

```mermaid
graph TD
    User([👤 User / Advocate]) -->|Query & Parameters| UI[🖥️ Streamlit UI / CLI Launcher]
    UI -->|Pydantic Payload| Controller[🧠 LexAgent Controller]

    subgraph Step Reasoning Trajectory
        Controller -->|Step 1: Fact Analysis| Analysis[🔍 Query Analysis Engine]
        Analysis -->|Step 2: Private RAG| Tool1[📂 Tool 1: Local RAG Tool]
        Analysis -->|Step 3: Online Search| Tool2[🌐 Tool 2: Online Search Tool]
        Tool1 -->|Step 4: Strategy Synthesis| Strategy[📜 Legal Strategy Synthesizer]
        Tool2 --> Strategy
        Strategy -->|Step 5: Legal Drafting| Tool3[📄 Tool 3: Legal Drafting Tool]
    end

    subgraph Data Stores & Engines
        Tool1 -->|Recursive rglob| LocalFolder[📁 private_docs/ - Nested Subfolders]
        LocalFolder -->|Vector Embeddings| ChromaDB[(🗄️ ChromaDB Vector Store)]
        
        Tool2 -->|Tier 1: Tavily API| Tavily[Tavily Legal Search]
        Tool2 -->|Tier 2: DuckDuckGo| DDG[DuckDuckGo Search]
        Tool2 -->|Tier 3: Built-In Precedents| OfflineDB[(📚 Curated RERA & HC Database)]

        Tool3 -->|XML Formatting| PyDocx[python-docx Legal Notice Engine]
        PyDocx -->|Output File| WordDoc[📥 Generated Legal Notice .docx]
    end

    Strategy -->|Final Advice Payload| UI
    WordDoc -->|Downloadable File| UI
```

---

## 🔄 2. 5-Step Agentic Reasoning Trajectory

LexAgent processes legal queries through a strictly controlled 5-stage deterministic state pipeline defined in `LexAgentController`:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Controller as 🧠 LexAgentController
    participant RAG as 📂 LocalRAGTool (Tool 1)
    participant Search as 🌐 OnlineSearchTool (Tool 2)
    participant LLM as 🤖 LLM / Fallback Engine
    participant Drafter as 📄 LegalDraftingTool (Tool 3)

    User->>Controller: Submit Query + Client Name + Options
    Controller->>LLM: 1. Deconstruct query into Facts & Statutory Claims
    LLM-->>Controller: Extracted Fact Scope
    Controller->>RAG: 2. Search nested private_docs in ChromaDB
    RAG-->>Controller: Matching Chunks & Relative File Paths
    Controller->>Search: 3. Search RERA Acts & HC Rulings
    Search-->>Controller: Precedent Rulings & Statutory Links
    Controller->>LLM: 4. Synthesize Legal Advice & Action Plan
    LLM-->>Controller: 100% Success Action Strategy
    opt If Legal Notice Requested
        Controller->>Drafter: 5. Generate formatted .docx Legal Notice
        Drafter-->>Controller: Generated .docx File Path
    end
    Controller-->>User: Display Strategy, RAG Badges, Links & Download Button
```

---

## 🛠️ 3. Component & Tool Specifications

### 📂 Tool 1: Local RAG (Private Document Advisor)
* **Module**: `src/tools/local_rag_tool.py` & `src/utils/document_ingestor.py`
* **Purpose**: Retrieves confidential client facts, RTI responses, sanction plans, and sale deeds stored locally.
* **Key Features**:
  * **Nested Directory Support**: Uses `Path.rglob("*")` to recursively index files inside subfolders (e.g., `private_docs/case_files/2023/deed.txt`).
  * **Multi-Format Parsing**: Supports `.txt`, `.md`, `.pdf` (pypdf), and `.docx` (`python-docx`).
  * **Vector Engine**: Persistent ChromaDB vector store with `sentence-transformers/all-MiniLM-L6-v2` embeddings.
  * **Source Attribution**: Retains exact relative paths for auditability (`Source Path: case_files/2023/sample_deed.txt`).

```mermaid
flowchart LR
    Subfolders[📁 private_docs/ Subdirectories] -->|Recursive rglob| Parser[📄 Document Parser]
    Parser -->|Paragraph Chunker| Chunks[Text Chunks]
    Chunks -->|MiniLM Embeddings| VectorStore[(🗄️ ChromaDB Vector Collection)]
    Query[User RAG Query] -->|Similarity Search| VectorStore
    VectorStore -->|Distance Threshold < 0.75| TopKResults[Top-K Matching Chunks & Relative Paths]
```

---

### 🌐 Tool 2: Online Search (RERA Acts & Precedent Provider)
* **Module**: `src/tools/online_search_tool.py`
* **Purpose**: Fetches applicable statutory provisions (RERA Sections 14, 18) and High Court / Supreme Court precedents.
* **Resilient Multi-Tier Fallback Architecture**:

```mermaid
graph TD
    Query[Legal Query] --> CheckKey{Is Tavily API Key present?}
    CheckKey -->|Yes| Tavily[1. Execute Tavily Legal Search API]
    CheckKey -->|No or Failed| DDGCheck{Is DuckDuckGo enabled?}
    Tavily -->|Success| ReturnResults[Return Precedents & Act Links]
    Tavily -->|API Failure| DDGCheck
    DDGCheck -->|Yes| DDG[2. Execute DuckDuckGo Legal Query]
    DDGCheck -->|No or Failed| Offline[3. Return Curated Offline RERA & HC Precedent DB]
    DDG -->|Success| ReturnResults
    DDG -->|Network Offline| Offline
    Offline --> ReturnResults
```

---

### 📄 Tool 3: Legal Drafting Tool
* **Module**: `src/tools/legal_drafting_tool.py`
* **Purpose**: Generates formal, court-ready legal notices saved as `.docx` files.
* **Features**:
  * Formal legal headers, Advocate notice structure, statutory citations, and formal demand directives.
  * Dynamic timestamped filenames (e.g., `Legal_Notice_Shri_Rajesh_Sharma_20260930_081416.docx`).

---

## ⚙️ 4. Central Configuration Architecture (`config.py`)

All system parameters are centralized in `config.py` for single-file maintainability:

| Configuration Variable | Default Value | Description |
| :--- | :--- | :--- |
| `PRIVATE_DOCS_DIR_NAME` | `"private_docs"` | Name of local document folder (supports nested subdirectories). |
| `OLLAMA_BASE_URL` | `"http://localhost:11434"` | Local Ollama API endpoint. |
| `OLLAMA_MODEL` | `"mistral"` | LLM model for legal synthesis (`mistral`, `llama3`, `gemma2`). |
| `SEARCH_MODEL_PROVIDER` | `"auto"` | Online search provider strategy (`auto`, `tavily`, `duckduckgo`, `offline`). |
| `EMBEDDING_MODEL_NAME` | `"sentence-transformers/all-MiniLM-L6-v2"` | Embedding model for vector indexing. |
| `CHROMA_COLLECTION_NAME` | `"lexagent_private_docs"` | ChromaDB vector collection identifier. |
| `RAG_TOP_K` | `3` | Number of chunks retrieved per query. |
| `RAG_DISTANCE_THRESHOLD` | `0.75` | Maximum similarity distance threshold. |

---

## 📦 5. State Management & Data Schema (`LexAgentState`)

LexAgent uses a unified Pydantic state model (`src/agent/state.py`) passed across all trajectory steps:

```python
class AgentStepLog(BaseModel):
    step_name: str
    description: str
    timestamp: str

class LexAgentState(BaseModel):
    query: str
    client_name: str
    wants_draft: bool
    step_logs: List[AgentStepLog]
    parsed_intent: Dict[str, Any]
    local_rag_output: Dict[str, Any]
    online_search_output: Dict[str, Any]
    final_advice: str
    generated_file_path: Optional[str]
    generated_file_name: Optional[str]
```

---

## 💻 6. User Interface & Launchers

1. **Streamlit Web Application (`app.py`)**:
   - Visual step reasoning logs.
   - Interactive source badges showing exact relative paths.
   - 1-click example query loader.
   - Downloadable `.docx` document button.

2. **Interactive Command-Line Interface (`main.py`)**:
   - Supports CLI flags (`--query`, `--draft`, `--client`).
   - Formatted console output with ASCII visual separators.

3. **1-Click Double-Click Laptop Launchers**:
   - **Windows**: `Run_LexAgent.bat`
   - **macOS / Linux**: `Run_LexAgent.sh`

---

## 🔒 7. Security, Privacy & Compliance Warranties

> [!IMPORTANT]
> **Data Privacy Guarantee**: All documents placed inside `private_docs/` are indexed locally into an on-device ChromaDB vector store. No private documents or confidential client files are ever uploaded to cloud servers.
