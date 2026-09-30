import os
from pathlib import Path
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from config import PRIVATE_DOCS_DIR, CHROMA_DB_DIR, CHROMA_COLLECTION_NAME

def read_file_content(file_path: Path) -> str:
    """Reads content from txt, md, pdf or docx file."""
    ext = file_path.suffix.lower()
    if ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    elif ext == '.docx':
        try:
            import docx
            doc = docx.Document(file_path)
            return "\n".join([p.text for p in doc.paragraphs if p.text])
        except Exception as e:
            return f"[Error reading docx {file_path.name}: {e}]"
    elif ext == '.pdf':
        try:
            import pypdf
            reader = pypdf.PdfReader(file_path)
            pages = [page.extract_text() for page in reader.pages if page.extract_text()]
            return "\n".join(pages)
        except Exception:
            return f"[PDF parsing fallback for {file_path.name}]"
    return ""

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Splits text into chunks preserving section paragraphs where possible."""
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if len(current_chunk) + len(p) <= chunk_size:
            current_chunk += ("\n\n" if current_chunk else "") + p
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = p

    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks

class LocalDocumentIngestor:
    """
    Ingests documents from private_docs into ChromaDB vector store.
    """
    def __init__(self, docs_dir: Path = PRIVATE_DOCS_DIR, db_dir: Path = CHROMA_DB_DIR):
        self.docs_dir = Path(docs_dir)
        self.db_dir = Path(db_dir)
        self.client = chromadb.PersistentClient(path=str(self.db_dir))
        self.collection = self.client.get_or_create_collection(name=CHROMA_COLLECTION_NAME)

    def ingest_all(self) -> int:
        """Reads all supported files from docs_dir (including nested subdirectories) and indexes into ChromaDB."""
        total_chunks = 0
        if not self.docs_dir.exists():
            return 0

        documents = []
        metadatas = []
        ids = []

        # Recursively search through all nested folders and subfolders
        for file_path in self.docs_dir.rglob("*"):
            if file_path.is_file() and file_path.suffix.lower() in ['.txt', '.md', '.docx', '.pdf']:
                content = read_file_content(file_path)
                if not content.strip():
                    continue
                
                # Compute path relative to docs_dir for clear nested folder source attribution
                try:
                    rel_path = str(file_path.relative_to(self.docs_dir))
                except ValueError:
                    rel_path = file_path.name

                chunks = chunk_text(content)
                for idx, chunk in enumerate(chunks):
                    # Sanitize doc_id for unique nested identification
                    sanitized_rel_path = rel_path.replace("/", "_").replace("\\", "_")
                    doc_id = f"{sanitized_rel_path}_chunk_{idx}"
                    documents.append(chunk)
                    metadatas.append({
                        "filename": file_path.name,
                        "relative_path": rel_path,
                        "chunk_index": idx,
                        "total_chunks": len(chunks)
                    })
                    ids.append(doc_id)
                    total_chunks += 1

        if documents:
            # Upsert into ChromaDB
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )

        return total_chunks

    def query(self, query_text: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Queries ChromaDB collection for matching document chunks."""
        count = self.collection.count()
        if count == 0:
            # Re-ingest if empty
            self.ingest_all()

        if self.collection.count() == 0:
            return []

        results = self.collection.query(
            query_texts=[query_text],
            n_results=min(top_k, self.collection.count())
        )

        formatted_results = []
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if "metadatas" in results else [{}] * len(docs)
            distances = results["distances"][0] if "distances" in results and results["distances"] else [0.0] * len(docs)
            
            for doc, meta, dist in zip(docs, metas, distances):
                formatted_results.append({
                    "content": doc,
                    "metadata": meta,
                    "distance": dist
                })

        return formatted_results
