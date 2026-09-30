import os
import pytest
from pathlib import Path
from src.tools.legal_drafting_tool import LegalDraftingTool

def test_legal_drafting_tool(tmp_path):
    tool = LegalDraftingTool(output_dir=tmp_path)
    res = tool.run(
        doc_type="LEGAL NOTICE",
        client_name="Test Client",
        opposite_party="Test Builder",
        facts="Test RTI fact statement",
        statutes="Section 14 & 18 RERA",
        demands="1. Deliver amenity\n2. Pay interest"
    )
    assert res["status"] == "success"
    assert os.path.exists(res["file_path"])
    assert res["file_name"].endswith(".docx")
