import time
from src.agent.controller import LexAgentController
from src.utils.document_ingestor import LocalDocumentIngestor

def test_performance_caching():
    print("\n⚡ Starting LexAgent Cache & Performance Benchmark...")
    
    # 1. Benchmark ChromaDB Vector Persistent Storage Cache
    ingestor = LocalDocumentIngestor()
    t0 = time.perf_counter()
    res1 = ingestor.query("swimming pool RTI status", top_k=3)
    t1 = time.perf_counter()
    rag_time_1 = (t1 - t0) * 1000
    
    t2 = time.perf_counter()
    res2 = ingestor.query("swimming pool RTI status", top_k=3)
    t3 = time.perf_counter()
    rag_time_2 = (t3 - t2) * 1000
    
    print(f"  📂 ChromaDB Vector Search 1st Run: {rag_time_1:.2f} ms")
    print(f"  📂 ChromaDB Vector Search 2nd Run (Cached Index): {rag_time_2:.2f} ms")
    
    assert len(res1) > 0, "ChromaDB query 1 should return results"
    assert len(res2) > 0, "ChromaDB query 2 should return results"
    
    # 2. Benchmark Controller In-Memory LRU Strategy Cache
    controller = LexAgentController()
    query = "Builder failed to construct swimming pool"
    
    t4 = time.perf_counter()
    state1 = controller.process_query(query, wants_draft=False, client_name="Smt Sunita Verma")
    t5 = time.perf_counter()
    cold_time = (t5 - t4) * 1000
    
    t6 = time.perf_counter()
    state2 = controller.process_query(query, wants_draft=False, client_name="Smt Sunita Verma")
    t7 = time.perf_counter()
    warm_cache_time = (t7 - t6) * 1000
    
    print(f"  🧠 Controller Cold Trajectory Run: {cold_time:.2f} ms")
    print(f"  ⚡ Controller LRU Memory Cache Run: {warm_cache_time:.2f} ms")
    
    assert warm_cache_time < cold_time, "Cached query run should be significantly faster than cold run"
    assert warm_cache_time < 5.0, "Cached query latency should be < 5ms"
    print("✅ All Cache & Performance Checks PASSED successfully!")

if __name__ == "__main__":
    test_performance_caching()
