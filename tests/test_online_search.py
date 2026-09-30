import pytest
from src.tools.online_search_tool import OnlineSearchTool

def test_online_search_tool():
    tool = OnlineSearchTool()
    res = tool.run("RERA Section 18 builder delay amenity pool")
    assert res["status"] == "success"
    assert "results" in res
    assert len(res["results"]) > 0
    assert "url" in res["results"][0]
    assert "title" in res["results"][0]
