from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# =========================
# LLM
# =========================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# =========================
# Embeddings
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# Vector Store
# =========================

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 1}
)


def ask_question(question: str):

    docs = retriever.invoke(question)

    context = ""

    for doc in docs:
        context += f"""
SOURCE: {doc.metadata["source"]}

{doc.page_content}

----------------------------------------
"""

    prompt = f"""
You are an HR Policy Assistant.

Answer the user's question using ONLY the information contained in the provided context.

Rules:
- Do not invent information.
- Do not use outside knowledge.
- If the answer cannot be found, respond:
  "I could not find that information in the policy documents."
- Provide a concise professional answer.
- Mention the policy source when appropriate.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content, docs