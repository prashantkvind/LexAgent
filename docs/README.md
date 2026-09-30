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

### 4. 💻 [Local Laptop Hardware Requirements](file:///config/.gemini/antigravity/scratch/LexAgent/docs/HARDWARE_REQUIREMENTS.md)
* **Target Audience**: Users and system administrators assessing hardware specs for searching 100+ documents.
* **Topics**: CPU, RAM, SSD, and GPU requirements, resource benchmarks for 100 documents, and local LLM vs lightweight mode.

### 5. 🧠 [Key Technical Learnings](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TECHNICAL_LEARNINGS.md)
* **Target Audience**: Developers, AI engineers, and legal tech architects studying agent design patterns.
* **Topics**: Tool-augmented agentic controller, local RAG with ChromaDB, 3-tier fallback architecture, python-docx legal notice generation, and zero-cloud privacy.

### 6. 🚀 [System Enhancements Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/ENHANCEMENTS.md)
* **Target Audience**: Developers, legal tech users, and architects reviewing recent agentic AI upgrades.
* **Topics**: Detailed breakdown of What changes were made, Why they were done, and What is the practical use of Self-Correction, Discrepancy Matrix, and Hybrid RAG.

### 7. ⚡ [Performance & Caching Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/PERFORMANCE_ENHANCEMENTS.md)
* **Target Audience**: Performance engineers, developers, and system architects.
* **Topics**: 2-Tier Caching Architecture (ChromaDB Disk Persistence + LRU Memory Cache) achieving 0.03ms (28,600x) query speedups.

### 8. 🛠️ [Tool Implementation Guide](file:///config/.gemini/antigravity/scratch/LexAgent/docs/TOOL_IMPLEMENTATION_GUIDE.md)
* **Target Audience**: AI developers, tool designers, and software engineers.
* **Topics**: In-depth implementation details, code snippets, advantages, and Mermaid integration diagrams for `LocalRAGTool`, `OnlineSearchTool`, and `LegalDraftingTool`.

### 9. ☁️ [Production Cloud Deployment Specification](file:///config/.gemini/antigravity/scratch/LexAgent/docs/CLOUD_DEPLOYMENT_GUIDE.md)
* **Target Audience**: DevOps engineers, cloud architects, and enterprise deployment leads.
* **Topics**: Step-by-step guide for migrating LexAgent to AWS, GCP, or Azure using Docker, Kubernetes/Cloud Run, S3/GCS Storage, and GitHub Actions CI/CD.

---

## 📁 Related Project Folders

* 📁 [`private_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/private_docs): Drop confidential client RTI replies, deeds, and brochures here (supports nested subfolders).
* 📥 [`generated_docs/`](file:///config/.gemini/antigravity/scratch/LexAgent/generated_docs): Output folder where created Microsoft Word `.docx` legal notices are saved.
* 🧪 [`tests/`](file:///config/.gemini/antigravity/scratch/LexAgent/tests): Automated Pytest test suite for RAG, Tavily/DuckDuckGo search, legal drafting, and controller.
