import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import csv

from src.retrieval.rag_service import ask_question

INPUT_FILE = "evaluation/evaluation_questions.csv"
OUTPUT_FILE = "evaluation/evaluation_results.csv"

results = []

with open(INPUT_FILE, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        question = row["question"]

        print(f"Asking: {question}")

        answer, docs = ask_question(question)

        results.append({
            "question": question,
            "expected_answer": row["expected_answer"],
            "actual_answer": answer
        })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "question",
            "expected_answer",
            "actual_answer"
        ]
    )

    writer.writeheader()

    writer.writerows(results)

print(f"\nSaved results to {OUTPUT_FILE}")