# 💻 LexAgent: Local Laptop Hardware Requirements

This document provides the hardware and system specifications required to run **LexAgent (Legal RERA & High Court Advisor Agent)** on a local laptop or workstation, specifically optimized for indexing and searching **100+ local legal documents** (RTI responses, sale deeds, sanction plans, brochures, PDFs, and `.docx` contracts).

---

## 📊 Hardware Requirements Summary

| Hardware Component | **Minimum Specs** *(Standard Laptop)* | **Recommended Specs** *(Optimal Speed & Local LLM)* |
| :--- | :--- | :--- |
| **Processor (CPU)** | Intel Core i5 (8th Gen+) or AMD Ryzen 5 | Intel Core i7 / Ryzen 7 or Apple M1/M2/M3/M4 |
| **System Memory (RAM)** | **8 GB RAM** | **16 GB RAM** |
| **Dedicated Graphics (GPU)** | Not required *(Runs smoothly on CPU)* | Integrated GPU / Apple Silicon Unified Memory / NVIDIA RTX |
| **Disk Storage (SSD)** | **2 GB Free SSD space** | **10 GB Free NVMe SSD space** *(If running Ollama Llama 3 / Mistral)* |
| **Operating System** | Windows 10/11, macOS 12+, or Linux | Windows 11, macOS Sonoma/Sequoia, or Ubuntu 22.04 |

---

## 🔍 Resource Performance Metrics for 100 Local Documents

For **100 local documents** (~500 to 2,000 paragraph chunks):

```
100 Documents (.pdf / .docx / .txt)
     │
     ├── 📁 Total File Size on Disk: ~50 MB to 200 MB
     ├── 🗄️ ChromaDB Vector Index Size: ~10 MB to 25 MB
     ├── ⚡ MiniLM Embedding RAM Usage: ~120 MB RAM
     └── ⏱️ Vector Search Retrieval Latency: < 15 milliseconds
```

---

## 💡 Operating Modes & System Memory Allocation

### Mode 1: Standard Mode (CPU Vector Search + Rule Synthesis + Web Search)
* **RAM Needed**: **4 GB to 8 GB RAM**
* **CPU Needed**: Any Dual-Core / Quad-Core CPU from 2018 or newer.
* **Architecture**: The local vector engine (`sentence-transformers/all-MiniLM-L6-v2`) requires only **~120 MB RAM** and computes vector similarity across 2,000 chunks in **< 15 milliseconds** on a standard CPU.

---

### Mode 2: Full Local LLM Mode (Running Llama 3 8B / Mistral 7B via Ollama)
* **RAM Needed**: **16 GB RAM** *(Allocates ~6 GB RAM to the quantized 7B/8B local LLM, leaving ~10 GB RAM for OS, ChromaDB, and Streamlit)*.
* **Processor / Acceleration**:
  * **Apple Mac**: Apple Silicon (M1/M2/M3/M4) with 16 GB Unified Memory generates 30–50 tokens/second.
  * **Windows/Linux Laptop**: Intel i7 / Ryzen 7 CPU or NVIDIA RTX 3050/3060/4060 GPU.

---

## ⚡ Performance Optimization Tips for 100+ Documents

1. **Use SSD Storage**: Keep your document folder (`private_docs/`) on an SSD rather than a mechanical hard drive for 10x faster document parsing during initial startup.
2. **Supported Formats**: LexAgent natively parses `.txt`, `.md`, `.pdf` (text-extractable), and `.docx` files.
3. **Persistent ChromaDB Vector Store**: Indexing only occurs once per file. On subsequent queries, searching 100+ documents completes in milliseconds.
