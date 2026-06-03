from pathlib import Path

docs = []

for file in Path("data/policies").glob("*.md"):
    content = file.read_text(encoding="utf-8")

    docs.append({
        "source": file.name,
        "content": content
    })

print(f"Loaded {len(docs)} documents")