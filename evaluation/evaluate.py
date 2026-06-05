import sys
import csv
import time
from pathlib import Path
from statistics import median

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.retrieval.rag_service import ask_question

INPUT_FILE = "evaluation/evaluation_questions.csv"
OUTPUT_FILE = "evaluation/evaluation_results.csv"

results = []
latencies = []

with open(INPUT_FILE, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        question = row["question"]

        print(f"Asking: {question}")

        start_time = time.perf_counter()

        answer, docs = ask_question(question)

        latency = time.perf_counter() - start_time

        latencies.append(latency)

        results.append({
            "question": question,
            "expected_answer": row["expected_answer"],
            "actual_answer": answer,
            "latency_seconds": round(latency, 3)
        })

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "question",
            "expected_answer",
            "actual_answer",
            "latency_seconds"
        ]
    )

    writer.writeheader()
    writer.writerows(results)

print(f"\nSaved results to {OUTPUT_FILE}")

# Calculate latency metrics

latencies.sort()

p50 = median(latencies)

p95_index = int(len(latencies) * 0.95)

if p95_index >= len(latencies):
    p95_index = len(latencies) - 1

p95 = latencies[p95_index]

print("\n=== Latency Metrics ===")
print(f"P50 Latency: {p50:.3f} seconds")
print(f"P95 Latency: {p95:.3f} seconds")