from typing import Dict, Any, List
from src.utils.document_ingestor import LocalDocumentIngestor
from config import RAG_TOP_K

class LocalRAGTool:
    """
    Tool 1: Local RAG (Private RTI / Sale Deed File Advisor)
    Accesses private documents (RTI replies, sanction plans, sale deeds) stored in private_docs.
    """
    name = "local_rag_tool"
    description = "Searches private client documents, RTI replies, and sale deeds stored in ChromaDB."

    def __init__(self):
        self.ingestor = LocalDocumentIngestor()

    def run(self, query: str) -> Dict[str, Any]:
        """Runs vector search over private_docs."""
        results = self.ingestor.query(query_text=query, top_k=RAG_TOP_K)
        
        if not results:
            return {
                "status": "empty",
                "summary": "No matching private case records found in private_docs directory.",
                "sources": [],
                "formatted_output": "No private RTI or document matches found."
            }

        sources = []
        formatted_chunks = []
        
        for res in results:
            filename = res["metadata"].get("filename", "unknown_file")
            rel_path = res["metadata"].get("relative_path", filename)
            chunk_idx = res["metadata"].get("chunk_index", 0)
            distance = round(res.get("distance", 0.0), 4)
            content = res["content"]
            
            sources.append({
                "filename": filename,
                "relative_path": rel_path,
                "chunk": chunk_idx,
                "distance": distance
            })
            
            formatted_chunks.append(
                f"[Source Path: {rel_path} (Chunk #{chunk_idx}, Dist: {distance})]\n{content}"
            )

        formatted_output = "\n\n---\n\n".join(formatted_chunks)

        return {
            "status": "success",
            "summary": f"Retrieved {len(results)} relevant facts from private document store.",
            "sources": sources,
            "raw_results": results,
            "formatted_output": formatted_output
        }
