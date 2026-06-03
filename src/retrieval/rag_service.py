from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Initialize once
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

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


def ask_question(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    sources = sorted(
        list(set(doc.metadata["source"] for doc in docs))
    )

    prompt = f"""
You are an HR Policy Assistant.

Answer the user's question using ONLY the information provided in the context.

Rules:
- Provide a complete and professional answer.
- Do not make up information.
- If the answer cannot be found in the context, respond with:
  "I could not find that information in the policy documents."

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content, sources