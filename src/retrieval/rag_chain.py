from rag_service import ask_question

question = input("\nAsk a question: ")

answer, sources = ask_question(question)

print("\n=== Answer ===\n")
print(answer)

print("\n=== Sources ===\n")

for source in sources:
    print(f"- {source}")