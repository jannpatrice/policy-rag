# Design and Evaluation

## 1. Design and Architecture Decisions

### Project Overview

This project implements a Retrieval-Augmented Generation (RAG) application that answers employee questions about company policies. The system retrieves relevant policy content from a vector database and uses a Large Language Model (LLM) to generate grounded responses supported by policy citations.

The objective was to create a lightweight, low-cost, and reproducible solution that minimizes hallucinations while providing accurate policy lookup capabilities.

---

## System Architecture

```text
Policy Documents (Markdown)
            ↓
Document Loading
            ↓
Chunking
            ↓
Embeddings (all-MiniLM-L6-v2)
            ↓
Chroma Vector Database
            ↓
Retriever (Top-K Similarity Search)
            ↓
Groq Llama 3.1
            ↓
Streamlit User Interface
```

---

## Technology Choices

### Policy Documents

The policy corpus was authored as Markdown documents because Markdown is lightweight, easy to maintain, human-readable, and well suited for version control.

The corpus consists of 12 policy documents covering:

* Employee Handbook
* Leave and Time Off
* Remote Work
* Information Security
* Acceptable Use
* Expense Reimbursement
* Business Travel
* Equipment and Asset
* Performance Management
* Recruitment and Hiring
* Learning and Development
* Code of Conduct

---

### LangChain

LangChain was used to orchestrate the RAG pipeline, including document processing, retrieval, embeddings, vector storage integration, and LLM interaction.

This reduced implementation complexity while maintaining flexibility for future enhancements.

---

### Embedding Model

Embedding model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

This model was selected because it:

* Is free and open source
* Provides strong semantic retrieval performance
* Runs efficiently on consumer hardware
* Integrates directly with LangChain and Chroma

The model converts document chunks into vector embeddings used for semantic search.

---

### Chunking Strategy

Documents were chunked using LangChain's RecursiveCharacterTextSplitter.

Configuration:

```text
Chunk Size: 500 characters
Chunk Overlap: 100 characters
```

This approach was selected to preserve context while reducing information loss at chunk boundaries.

The final corpus produced approximately 185 chunks.

---

### Vector Database

Vector store:

```text
ChromaDB
```

ChromaDB was selected because it:

* Is open source
* Requires minimal setup
* Supports local persistence
* Integrates seamlessly with LangChain

The vector database stores embeddings and enables semantic retrieval of policy content.

---

### Language Model

Model:

```text
Llama 3.1 8B Instant
```

Provider:

```text
Groq
```

Groq was selected because it:

* Provides a free developer tier
* Offers low-latency inference
* Requires no local GPU infrastructure
* Integrates easily with LangChain

The language model generates answers using retrieved policy content as context.

---

### Retrieval Strategy

The application uses similarity-based retrieval from ChromaDB.

Configuration:

```text
Top-K = 3
```

For each user query, the retriever returns the three most relevant document chunks.

During development, different Top-K values were tested. Lower values improved citation precision but occasionally missed relevant supporting information. Higher values increased the risk of introducing unrelated policy content into the context window. Top-K = 3 provided the best balance between retrieval recall and citation quality.

---

### Prompt Design

The prompt instructs the model to:

* Use only the provided policy context
* Avoid external knowledge
* Refuse unsupported questions
* Generate concise responses
* Reference supporting policy documents

This approach helps reduce hallucinations and improves answer groundedness.

---

### User Interface

The application uses Streamlit to provide a lightweight web interface.

Users can:

* Ask policy-related questions
* View generated answers
* Inspect supporting citations
* Review retrieved policy content

---

### CI/CD

A GitHub Actions workflow was implemented to support continuous integration.

The workflow automatically:

1. Installs project dependencies
2. Verifies successful application build execution
3. Runs validation checks on every push and pull request

This helps ensure repository consistency and reproducibility.

---

## 2. Evaluation

### Evaluation Methodology

The system was evaluated using a curated set of 30 policy-related questions.

The evaluation set covered:

* Leave and Time Off
* Remote Work
* Information Security
* Acceptable Use
* Expense Reimbursement
* Business Travel
* Learning and Development
* Performance Management

Generated answers were compared against expected answers and manually reviewed for factual correctness and citation quality.

---

### Groundedness

Groundedness measures whether generated answers are fully supported by the retrieved policy content and do not introduce unsupported information.

| Metric              | Result |
| ------------------- | ------ |
| Questions Evaluated | 30     |
| Grounded Answers    | 29     |
| Groundedness Score  | 96.7%  |

Most responses were directly supported by retrieved evidence. No significant hallucination behavior was observed.

One retrieval failure occurred when the system could not locate information regarding learning budget carryover despite the information existing in the corpus.

---

### Citation Accuracy

Citation Accuracy measures whether cited policy documents correctly support the generated answer.

| Metric              | Result |
| ------------------- | ------ |
| Questions Evaluated | 30     |
| Correct Citations   | 29     |
| Citation Accuracy   | 96.7%  |

Most responses cited the appropriate policy document and supporting evidence.

The same retrieval failure affecting groundedness also affected citation accuracy.

---

### Exact / Semantic Match

Generated answers were compared against expected answers contained in the evaluation dataset.

| Metric                                     | Result |
| ------------------------------------------ | ------ |
| Correct or Semantically Equivalent Answers | 29     |
| Incorrect Answers                          | 1      |
| Match Rate                                 | 96.7%  |

Many generated responses contained additional explanatory wording while remaining semantically equivalent to the expected answer.

---

### Latency

Latency was measured across the 30-question evaluation set.

| Metric      | Result        |
| ----------- | ------------- |
| p50 Latency | 2.478 seconds |
| p95 Latency | 5.069 seconds |

The measured response times were suitable for interactive policy lookup and employee self-service scenarios.

---

### Key Findings

The evaluation demonstrated that the system can reliably retrieve and generate policy-based answers with high accuracy and strong source attribution.

The primary failure mode observed was retrieval omission rather than hallucination. When retrieval failed, the model generally responded that it could not find the information rather than generating unsupported content.

---

### Future Improvements

Potential future enhancements include:

* Retrieval reranking to improve recall
* Hybrid search combining keyword and vector retrieval
* Additional policy documents and larger corpora
* Automated evaluation pipelines
* Public cloud deployment using Render or Railway
* User feedback collection and answer quality monitoring

---

## Summary

The final RAG application achieved:

* Groundedness: 96.7%
* Citation Accuracy: 96.7%
* Match Rate: 96.7%
* p50 Latency: 2.478 seconds
* p95 Latency: 5.069 seconds

These results indicate that the application successfully meets the project objective of providing accurate, grounded, and cited answers from a company policy corpus while maintaining acceptable response times for interactive use.
