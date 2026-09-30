#!/usr/bin/env python3
import sys
import argparse
from src.agent.controller import LexAgentController

def main():
    parser = argparse.ArgumentParser(description="LexAgent - Legal RERA/HC Advisor CLI Agent")
    parser.add_argument("--query", "-q", type=str, help="Legal question to evaluate")
    parser.add_argument("--draft", "-d", action="store_true", help="Generate legal notice document (.docx)")
    parser.add_argument("--client", "-c", type=str, default="Shri Rajesh Sharma", help="Client full name")
    args = parser.parse_args()

    controller = LexAgentController()

    print("======================================================================")
    print(" ⚖️  LexAgent: Legal RERA & High Court Advisor (Tool-Augmented Agent)")
    print("======================================================================")
    print(" Stack: LangChain | ChromaDB Local RAG | Tavily/DDG Search | python-docx")
    print("----------------------------------------------------------------------\n")

    if args.query:
        run_agent(controller, args.query, args.draft, args.client)
    else:
        # Interactive loop
        while True:
            try:
                user_input = input("\n⚖️  Enter Legal Query (or 'exit' to quit): ").strip()
                if not user_input or user_input.lower() in ['exit', 'quit', 'q']:
                    print("Exiting LexAgent. Goodbye!")
                    break

                client_input = input("👤 Client Full Name [Default: Shri Rajesh Sharma]: ").strip()
                client_name = client_input if client_input else "Shri Rajesh Sharma"

                wants_draft_input = input("📄 Generate Legal Notice (.docx)? (y/N): ").strip().lower()
                wants_draft = wants_draft_input.startswith('y')

                run_agent(controller, user_input, wants_draft, client_name)
            except (KeyboardInterrupt, EOFError):
                print("\nExiting LexAgent.")
                break

def run_agent(controller: LexAgentController, query: str, wants_draft: bool, client_name: str = "Shri Rajesh Sharma"):
    print(f"\n[Processing Query]: {query}\n")
    state = controller.process_query(query, wants_draft=wants_draft, client_name=client_name)

    print("\n--- 🧠 AGENT REASONING TRAJECTORY LOG ---")
    for log in state.step_logs:
        print(f"  ✅ {log.step_name}: {log.description}")

    print("\n----------------------------------------------------------------------")
    print(" 📂 TOOL 1: PRIVATE RAG (LOCAL RTI & CASE FILE SOURCES)")
    print("----------------------------------------------------------------------")
    if state.local_rag_output and state.local_rag_output.get("sources"):
        for src in state.local_rag_output["sources"]:
            print(f"  📄 File: {src['filename']} | Chunk #{src['chunk']} | Match Distance: {src['distance']}")
        print("\nSnippet Preview:")
        print(state.local_rag_output.get("formatted_output", "")[:400] + "...\n")
    else:
        print("  (No private document matches found)\n")

    print("----------------------------------------------------------------------")
    print(" 🌐 TOOL 2: ONLINE LEGAL SEARCH (RERA ACTS & HC PRECEDENTS)")
    print("----------------------------------------------------------------------")
    if state.online_search_output and state.online_search_output.get("results"):
        print(f"  Provider: {state.online_search_output.get('provider', 'Web')}")
        for item in state.online_search_output["results"]:
            print(f"  🔗 [{item['title']}]({item['url']})")
    print()

    print("----------------------------------------------------------------------")
    print(" 📜 STRATEGY & ACTION PLAN (100% SUCCESS APPROACH)")
    print("----------------------------------------------------------------------")
    print(state.final_advice)
    print("----------------------------------------------------------------------\n")

    if state.generated_file_path:
        print("----------------------------------------------------------------------")
        print(" 📄 TOOL 3: GENERATED LEGAL DOCUMENT")
        print("----------------------------------------------------------------------")
        print(f"  File Generated: {state.generated_file_name}")
        print(f"  Full Path:      {state.generated_file_path}")
        print("----------------------------------------------------------------------\n")

if __name__ == "__main__":
    main()
