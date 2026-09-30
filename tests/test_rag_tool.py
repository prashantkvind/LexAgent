import pytest
from pathlib import Path
from src.tools.local_rag_tool import LocalRAGTool

def test_local_rag_tool():
    tool = LocalRAGTool()
    # Ingest private sample document
    ingest_count = tool.ingestor.ingest_all()
    assert ingest_count >= 0

    res = tool.run("swimming pool RTI completion certificate")
    assert res["status"] in ["success", "empty"]
    if res["status"] == "success":
        assert len(res["sources"]) > 0
        assert "filename" in res["sources"][0]
