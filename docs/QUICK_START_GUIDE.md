# ⚡ LexAgent: Quick Start Guide

Welcome to **LexAgent**, the Tool-Augmented Legal RERA & High Court Advisor Agent. This Quick Start Guide will get you up and running in **under 2 minutes** on any laptop (Windows, macOS, or Linux).

---

## 🚀 1. One-Click Quick Launch (Easiest Way)

No command line experience required! Simply double-click the launcher script for your operating system:

* **🪟 Windows**: Double-click [`Run_LexAgent.bat`](file:///config/.gemini/antigravity/scratch/LexAgent/Run_LexAgent.bat)
* **🍎 macOS / 🐧 Linux**: Double-click or run [`Run_LexAgent.sh`](file:///config/.gemini/antigravity/scratch/LexAgent/Run_LexAgent.sh)

*(The launcher automatically initializes the virtual environment, installs dependencies if needed, and opens the Streamlit Web Application in your default browser at `http://localhost:8501`).*

---

## 💻 2. Manual Command Line Launch

If you prefer using the terminal:

### Step 1: Open Terminal & Activate Environment
```bash
# macOS / Linux
cd /path/to/LexAgent
source env/bin/activate  # or source venv/bin/activate

# Windows (Command Prompt)
cd \path\to\LexAgent
env\Scripts\activate.bat
```

### Step 2: Run Web Interface or CLI

* **Interactive Streamlit Web UI**:
  ```bash
  streamlit run app.py
  ```

* **Interactive Command Line Mode**:
  ```bash
  python main.py
  ```

* **Single Command with Legal Notice (.docx) Generation**:
  ```bash
  python main.py --query "Builder failed to construct promised swimming pool in phase 1" --draft --client "Smt Sunita Verma"
  ```

---

## 📂 3. How to Use Private Local Documents (Local RAG)

1. Place your private RTI replies, sanction plans, sale deeds, or builder brochures (`.txt`, `.pdf`, `.docx`, `.md`) into the [`private_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/private_docs) folder.
2. You can organize files in **nested subfolders** (e.g., `private_docs/case_files/2023/sample_deed.txt`).
3. LexAgent automatically crawls, chunks, and indexes all nested files into an on-device ChromaDB vector database.
4. When you ask a query, LexAgent extracts relevant facts and displays exact source file paths (e.g. `Source Path: case_files/2023/sample_deed.txt`).

---

## ⚙️ 4. Quick Configuration (`config.py`)

All primary settings are located in a single file: [`config.py`](file:///config/.gemini/antigravity/scratch/LexAgent/config.py).

* **Change Local Folder Name**:
  ```python
  PRIVATE_DOCS_DIR_NAME = "private_docs"  # Change to any folder name
  ```
* **Change LLM Model**:
  ```python
  OLLAMA_MODEL = "mistral"  # Options: llama3, mistral, gemma2, etc.
  ```
* **Change Online Search Provider**:
  ```python
  SEARCH_MODEL_PROVIDER = "auto"  # Options: auto, tavily, duckduckgo, offline
  ```

---

## 📄 5. Finding Generated Legal Notices

All generated formal legal notices are saved into the [`generated_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/generated_docs) folder as Microsoft Word `.docx` files.
In the Streamlit Web UI, you can also download the `.docx` document directly using the **📥 Download Legal Notice (.docx)** button.

---

## 📚 6. Documentation Directory Index

All technical and operational documentation is stored inside the [`docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/docs) folder:

| Document | Description |
| :--- | :--- |
| ⚡ [docs/QUICK_START_GUIDE.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/QUICK_START_GUIDE.md) | This 2-minute quick start guide. |
| 💻 [docs/LOCAL_INSTALLATION_GUIDE.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/LOCAL_INSTALLATION_GUIDE.md) | Full installation, virtualenv, and troubleshooting guide. |
| 🏛️ [docs/ARCHITECTURE_AND_DESIGN.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ARCHITECTURE_AND_DESIGN.md) | System architecture, 6-step trajectory Mermaid diagrams, and tool specifications. |
| 💻 [docs/HARDWARE_REQUIREMENTS.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/HARDWARE_REQUIREMENTS.md) | Local laptop CPU/RAM specs and Ollama model tiers. |
| 🧠 [docs/TECHNICAL_LEARNINGS.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TECHNICAL_LEARNINGS.md) | Core AI concepts: RAG, Agentic Controller, and python-docx. |
| 🚀 [docs/ENHANCEMENTS.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ENHANCEMENTS.md) | System enhancements: What was changed, Why it was done, and Practical uses. |
| ⚡ [docs/PERFORMANCE_ENHANCEMENTS.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/PERFORMANCE_ENHANCEMENTS.md) | Performance & 2-Tier Caching Architecture (0.03ms query benchmark). |
| 🛠️ [docs/TOOL_IMPLEMENTATION_GUIDE.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TOOL_IMPLEMENTATION_GUIDE.md) | Deep dive into `LocalRAGTool`, `OnlineSearchTool`, and `LegalDraftingTool` implementation. |
| ☁️ [docs/CLOUD_DEPLOYMENT_GUIDE.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/CLOUD_DEPLOYMENT_GUIDE.md) | Step-by-step guide for migrating LexAgent to AWS, GCP, or Azure. |
| 🏛️ [docs/ProductionLiveGuideline.md](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ProductionLiveGuideline.md) | Requirements for live access, cost tiers ($5/mo), and cost control strategies. |
