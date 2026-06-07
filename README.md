# Policy Assistant RAG

A Retrieval-Augmented Generation (RAG) application that answers employee policy questions using a corpus of company policy documents.

The application retrieves relevant policy content from a vector database and uses a Large Language Model (LLM) to generate grounded responses with supporting citations.

---

## Features

* Policy question answering using RAG
* Semantic search using embeddings
* ChromaDB vector database
* Source citations and supporting evidence
* Streamlit web interface
* Evaluation dataset and metrics
* GitHub Actions CI pipeline

---

## Technology Stack

| Component       | Technology                  |
| --------------- | --------------------------- |
| Application     | Python                      |
| UI              | Streamlit                   |
| LLM             | Groq (Llama 3.1 8B Instant) |
| Framework       | LangChain                   |
| Embeddings      | all-MiniLM-L6-v2            |
| Vector Database | ChromaDB                    |
| CI/CD           | GitHub Actions              |

---

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── data/
│   └── policies/
├── chroma_db/
├── evaluation/
│   ├── evaluation_questions.csv
│   ├── evaluation_results.csv
│   └── evaluate.py
├── src/
│   ├── ingestion/
│   └── retrieval/
├── .github/
│   └── workflows/
├── design-and-evaluation.md
├── ai-tooling.md
└── README.md
```

---

## Setup

### 1. Clone Repository

```bash
git clone <repository-url>
cd policy-rag
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

A free API key can be obtained from Groq.

---

## Build the Vector Database

If running the project for the first time:

### Chunk Documents

```bash
python src/ingestion/chunk_documents.py
```

### Create Vector Store

```bash
python src/retrieval/build_vectorstore.py
```

---

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## Example Questions

```text
How many Vacation Leave days do employees receive?

How much is the monthly internet allowance?

Can employees work outside the Philippines?

How long is the probationary period?

How many Study Leave days are available?
```

---

## Evaluation

The application was evaluated using a set of 30 policy-related questions covering:

* Leave and Time Off
* Remote Work
* Information Security
* Expense Reimbursement
* Business Travel
* Learning and Development
* Performance Management

### Results

| Metric            | Result        |
| ----------------- | ------------- |
| Groundedness      | 96.7%         |
| Citation Accuracy | 96.7%         |
| Match Rate        | 96.7%         |
| p50 Latency       | 2.478 seconds |
| p95 Latency       | 5.069 seconds |

Additional details are available in:

```text
design-and-evaluation.md
```

---

## CI/CD

GitHub Actions is configured to run on every push and pull request.

The workflow:

1. Installs project dependencies
2. Performs automated validation checks
3. Verifies successful application build execution

Workflow definition:

```text
.github/workflows/ci.yml
```

---

## Documentation

Additional project documentation:

* `design-and-evaluation.md` – Design decisions and evaluation results
* `ai-tooling.md` – AI tooling usage and lessons learned

---

## Future Improvements

* Hybrid keyword + vector retrieval
* Retrieval reranking
* Public deployment
* Larger policy corpus
* User feedback collection
* Automated evaluation pipelines

```
```
