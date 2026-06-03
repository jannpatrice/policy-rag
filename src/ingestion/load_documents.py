from pathlib import Path

policy_folder = Path("data/policies")

files = list(policy_folder.glob("*.md"))

print(f"Loaded {len(files)} documents")

for file in files:
    print(file.name)