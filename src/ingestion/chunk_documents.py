from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = []

for file in Path("data/policies").glob("*.md"):
    content = file.read_text(encoding="utf-8")

    documents.append(
        {
            "source": file.name,
            "content": content,
        }
    )

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

chunks = []

for doc in documents:
    split_docs = splitter.create_documents(
        [doc["content"]],
        metadatas=[{"source": doc["source"]}],
    )

    chunks.extend(split_docs)

print(f"Created {len(chunks)} chunks")

print("\nExample Chunk:")
print(chunks[0].page_content[:500])
print(chunks[0].metadata)