from pathlib import Path

policy_folder = Path("data/policies")

documents = []

for file in policy_folder.glob("*.md"):
    content = file.read_text(encoding="utf-8")

    documents.append(
        {
            "source": file.name,
            "content": content,
        }
    )

print(f"Loaded {len(documents)} documents")

print("\nFirst document:")
print(documents[0]["source"])

print("\nPreview:")
print(documents[0]["content"][:500])