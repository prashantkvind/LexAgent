import pytest
from src.agent.controller import LexAgentController

def test_agent_controller_flow():
    controller = LexAgentController()
    query = "The builder promised a swimming pool in the brochure but RTI confirms OC was issued without it."
    
    state = controller.process_query(query, wants_draft=True)
    
    assert len(state.step_logs) >= 5
    assert state.analysis is not None
    assert state.local_rag_output is not None
    assert state.online_search_output is not None
    assert state.synthesis_output is not None
    assert state.generated_file_path is not None
