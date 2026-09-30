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
* 💻 **[Local Laptop Hardware Requirements](file:///config/.gemini/antigravity/scratch/LexAgent/docs/HARDWARE_REQUIREMENTS.md)**: CPU, RAM, SSD specs and performance metrics for 100+ documents.
* 🧠 **[Key Technical Learnings](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TECHNICAL_LEARNINGS.md)**: Agentic controller design, local ChromaDB RAG, multi-tier fallbacks, and python-docx legal drafting.
* 🚀 **[System Enhancements Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ENHANCEMENTS.md)**: What was added, why it was done, and practical uses of Self-Correction, Discrepancy Matrix, and Hybrid RAG.
* ⚡ **[Performance & Caching Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/PERFORMANCE_ENHANCEMENTS.md)**: 2-Tier Caching Architecture, step-by-step optimizations, and 0.03ms (28,600x) benchmark metrics.
* 🛠️ **[Tool Implementation Architecture Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TOOL_IMPLEMENTATION_GUIDE.md)**: Deep dive into `LocalRAGTool`, `OnlineSearchTool`, and `LegalDraftingTool` with code snippets, advantages, and Mermaid flow diagrams.
* ☁️ **[Production Cloud Deployment Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/CLOUD_DEPLOYMENT_GUIDE.md)**: Step-by-step technical guide for deploying LexAgent to AWS, GCP, or Azure using Docker, S3/GCS, and GitHub Actions CI/CD.
* 🏛️ **[Production Live Guidelines & Cost Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ProductionLiveGuideline.md)**: Live access requirements, monthly cost breakdown tiers ($5/mo, $45/mo, $210/mo), and 6 cost-minimization strategies.

---

## 🛠️ Stack Overview
* **Agent Framework**: LangChain + Custom Controller
* **Vector Database**: ChromaDB (Local Persistent Embeddings)
* **Search Engine**: Tavily API + DuckDuckGo + Offline Precedent Database
* **Document Drafter**: `python-docx`
* **User Interface**: Streamlit Web UI + Command Line CLI
