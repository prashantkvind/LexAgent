from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

class StepLog(BaseModel):
    step_num: int
    step_name: str
    description: str
    status: str = "completed"

class LexAgentState(BaseModel):
    """
    State object tracking the reasoning engine trajectory for LexAgent.
    """
    query: str
    wants_draft: bool = False
    client_name: str = "Shri Rajesh Sharma"
    opposite_party: str = "Royal Palms Infrastructure Pvt Ltd"
    
    # Internal Reasoning & Tools State
    step_logs: List[StepLog] = Field(default_factory=list)
    analysis: Optional[str] = None
    local_rag_output: Optional[Dict[str, Any]] = None
    online_search_output: Optional[Dict[str, Any]] = None
    synthesis_output: Optional[str] = None
    draft_output: Optional[Dict[str, Any]] = None
    
    final_advice: Optional[str] = None
    generated_file_path: Optional[str] = None
    generated_file_name: Optional[str] = None
    
    # Advanced Agentic & Hybrid RAG State
    fact_verification_score: float = 100.0  # Self-Correction Confidence Score (0 - 100%)
    discrepancy_matrix: List[Dict[str, str]] = Field(default_factory=list)
    verification_report: Optional[str] = None
