from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

question = "How much is the monthly internet allowance?"

results = retriever.invoke(question)

print(f"\nQuestion: {question}\n")

for i, doc in enumerate(results, start=1):
    print(f"\n=== Result {i} ===")
    print(f"Source: {doc.metadata['source']}")
    print(doc.page_content[:500])