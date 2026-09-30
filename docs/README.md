# 📚 LexAgent Documentation Hub

Welcome to the central documentation hub for **LexAgent (Legal RERA & High Court Advisor Agent)**.

This directory contains all operational, setup, architectural, and user guides for LexAgent:

---

## 📄 Documentation Map

### 1. ⚡ [Quick Start Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/QUICK_START_GUIDE.md)
* **Target Audience**: Anyone wanting to run LexAgent in under 2 minutes.
* **Topics**: 1-click double-click launchers (`Run_LexAgent.sh` & `Run_LexAgent.bat`), web app launch, CLI usage, private document folder usage, and downloadable Word `.docx` notices.

### 2. 💻 [Local Laptop Installation & Configuration Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/LOCAL_INSTALLATION_GUIDE.md)
* **Target Audience**: Developers, IT admins, and legal tech engineers setting up local environments.
* **Topics**: Detailed Windows/macOS/Linux setup, Python virtualenv creation, `config.py` single-file configuration, nested directory ingestion, `.env` key options, and troubleshooting.

### 3. 🏛️ [System Architecture & Technical Design Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ARCHITECTURE_AND_DESIGN.md)
* **Target Audience**: Software architects, legal tech designers, and code contributors.
* **Topics**: Component topology, Mermaid architecture flowcharts, 5-step agentic controller trajectory, multi-tier search fallbacks, ChromaDB vector store mechanics, `python-docx` legal drafting engine, and Pydantic state schemas.

---

## 📁 Related Project Folders

* 📁 [`private_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/private_docs): Drop confidential client RTI replies, deeds, and brochures here (supports nested subfolders).
* 📥 [`generated_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/generated_docs): Output folder where created Microsoft Word `.docx` legal notices are saved.
* 🧪 [`tests/`](file:///config/.gemini/antigravity/scratch/LexAgent/tests): Automated Pytest test suite for RAG, Tavily/DuckDuckGo search, legal drafting, and controller.
