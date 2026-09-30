# ⚖️ LexAgent: Legal RERA & High Court Advisor Agent

**LexAgent** is a Tool-Augmented Agentic Legal Reasoning System built for RERA Act compliance, High Court precedent analysis, and automated legal notice drafting.

---

## ⚡ Quick Launch (1-Click Launchers)

Double-click to run on your laptop:
* **Windows**: [`Run_LexAgent.bat`](file:///config/.gemini/antigravity/scratch/LexAgent/Run_LexAgent.bat)
* **macOS / Linux**: [`Run_LexAgent.sh`](file:///config/.gemini/antigravity/scratch/LexAgent/Run_LexAgent.sh)

---

## 📚 Central Documentation Hub (`docs/`)

All documentation is consolidated in the [`docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/docs) folder:

* ⚡ **[Quick Start Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/QUICK_START_GUIDE.md)**: 2-minute quick start for UI and CLI execution.
* 💻 **[Local Installation Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/LOCAL_INSTALLATION_GUIDE.md)**: Environment setup, single-file `config.py` options, and nested document folder setup.
* 🏛️ **[System Architecture & Design Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ARCHITECTURE_AND_DESIGN.md)**: Mermaid system flowcharts, 5-step agent trajectory, and component mechanics.

---

## 🛠️ Stack Overview
* **Agent Framework**: LangChain + Custom Controller
* **Vector Database**: ChromaDB (Local Persistent Embeddings)
* **Search Engine**: Tavily API + DuckDuckGo + Offline Precedent Database
* **Document Drafter**: `python-docx`
* **User Interface**: Streamlit Web UI + Command Line CLI
