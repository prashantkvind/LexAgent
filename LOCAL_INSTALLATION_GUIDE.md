# 💻 LexAgent: Local Laptop Installation & Configuration Guide

This guide provides complete, step-by-step instructions for installing, configuring, and running **LexAgent (Legal RERA & High Court Advisor Agent)** on a local laptop (Windows, macOS, or Linux).

---

## ⚙️ 1. Single-File Central Configuration (`config.py`)

All primary settings—including the **Local Document Folder Name**, **LLM Model Selection**, and **Online Search Providers**—are configured in a single file: `config.py`.

### 📂 A. Configuring the Local Document Folder
To change the local folder used for primary document search, simply update `PRIVATE_DOCS_DIR_NAME` in `config.py`:
```python
# config.py (Line 7)
PRIVATE_DOCS_DIR_NAME = "private_docs"  # Change to "my_legal_files", "case_documents", etc.
```

### 🧠 B. Configuring Models for Additional Search & Legal Synthesis
To configure which local LLM model or search provider LexAgent uses:
```python
# config.py (Lines 18-20)
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "mistral"  # Options: llama3, mistral, gemma2, legal-llama, etc.
SEARCH_MODEL_PROVIDER = "auto"  # Options: auto, tavily, duckduckgo, offline
```

---

## 📂 2. Nested Folder Support for Primary Local RAG Search

LexAgent automatically performs **recursive search (`rglob`)** across all nested subdirectories inside your document folder.

You can organize your private legal documents in nested subfolders:
```
private_docs/
├── rti_replies/
│   └── 2023_inspection_report.txt
├── case_files/
│   └── 2023/
│       └── sample_deed.txt
└── contracts/
    └── builder_brochure.pdf
```

*When a search is run, LexAgent searches all subfolders recursively and displays exact relative source paths (e.g., `Source Path: case_files/2023/sample_deed.txt`).*

---

## ⚡ 3. One-Click Double-Click Launchers

Non-technical users can double-click launcher scripts to run LexAgent:

* **Windows**: Double-click `Run_LexAgent.bat`
* **macOS / Linux**: Double-click or run `./Run_LexAgent.sh`

---

## 🛠️ 4. Manual Installation & Execution

### Step 1: Create & Activate Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat
```

### Step 2: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run LexAgent
```bash
# Web UI (Streamlit)
streamlit run app.py

# Interactive CLI
python main.py

# CLI with immediate Legal Notice (.docx) generation
python main.py --query "What amenities were promised in Clause 12?" --draft
```

---

## 🧪 5. Verification & Tests
To verify all tools (Nested Local RAG, Tavily/DuckDuckGo Search, and python-docx Legal Notice Generator):
```bash
pytest tests/ -v
```
