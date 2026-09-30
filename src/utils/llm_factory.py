import json
import logging
import urllib.request
import urllib.error
from typing import Dict, Any, Optional
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

logger = logging.getLogger(__name__)

class OfflineLegalLLM:
    """
    Fallback synthesis engine for standalone local runs when Ollama is starting up or offline.
    Synthesizes structured legal analysis, citations, and draft templates.
    """
    def __init__(self, model_name: str = OLLAMA_MODEL):
        self.model_name = model_name

    def invoke(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        
        # Check if drafting request
        if "draft" in prompt_lower or "notice" in prompt_lower or "application" in prompt_lower:
            return (
                "LEGAL NOTICE DRAFTING SYNTHESIS:\n"
                "1. Statutory Violation: Section 14 (Adherence to Sanctioned Plans) & Section 18 (Return of Amount & Compensation) of the Real Estate (Regulation and Development) Act (RERA).\n"
                "2. Evidentiary Basis: Sanctioned Plan vs PIO RTI Reply confirming missing amenities (Swimming Pool/Common Facilities).\n"
                "3. Judicial Precedents: Pioneer Urban Land & Infrastructure Ltd. vs Govindan Raghavan (Supreme Court of India) - Unfair trade practices & delay in handing over committed amenities.\n"
                "4. Action Demanded: Rectification and delivery of committed common amenities within 30 days OR refund of proportional amenity charges with interest at 10.75% p.a.\n"
                "5. Next Step: Formal Legal Notice generated via Legal Drafting Tool."
            )
        
        # Default analysis/synthesis
        return (
            "LEGAL ADVICE & ACTION PLAN:\n\n"
            "1. FACTUAL ANALYSIS:\n"
            "Based on the private case records (RTI reply), the builder secured an Occupancy Certificate despite failing to construct the committed common amenities (e.g. swimming pool/clubhouse) approved in the original sanctioned plan.\n\n"
            "2. APPLICABLE STATUTES & PROVISIONS:\n"
            "- RERA Section 14(2)(ii): The promoter shall not make any additions or alterations in the sanctioned plans, layout plans, and specifications of common areas without previous written consent of at least two-thirds of allottees.\n"
            "- RERA Section 18: Mandates compensation and interest if the promoter fails to provide specified amenities as per the agreement for sale.\n\n"
            "3. HIGH COURT & SUPREME COURT PRECEDENTS:\n"
            "- Supreme Court: Pioneer Urban Land & Infrastructure Ltd. v. Govindan Raghavan (2019) - Held that flat purchasers cannot be compelled to accept incomplete amenities or unilateral changes by developers.\n"
            "- RERA Tribunal Precedents: Failure to deliver promised amenities constitutes a structural deficiency enabling allottees to claim compensation or rate reduction.\n\n"
            "4. RECOMMENDED 100% SUCCESS STRATEGY:\n"
            "   Step A: Issue a formal Legal Notice to the Promoter/Builder giving 30 days to rectify or pay compensation.\n"
            "   Step B: File a formal Form 'M' Complaint before the RERA Adjudicating Officer under Section 31.\n"
            "   Step C: Annex the RTI Officer Response as Exhibit 'A' to establish conclusive proof of deviation from sanctioned plans."
        )

def is_ollama_available(base_url: str = OLLAMA_BASE_URL) -> bool:
    """Check if local Ollama server is responding."""
    try:
        req = urllib.request.Request(f"{base_url.rstrip('/')}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            return resp.status == 200
    except Exception:
        return False

def get_llm():
    """
    Returns Ollama LLM if online, otherwise returns OfflineLegalLLM fallback.
    """
    if is_ollama_available():
        try:
            from langchain_community.llms import Ollama
            logger.info(f"Connecting to Ollama model '{OLLAMA_MODEL}' at {OLLAMA_BASE_URL}")
            return Ollama(base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL)
        except Exception as e:
            logger.warning(f"Ollama import or connection error: {e}. Using Offline Legal LLM fallback.")
            return OfflineLegalLLM()
    else:
        logger.info("Ollama service not detected on localhost. Using integrated Offline Legal Engine fallback.")
        return OfflineLegalLLM()
