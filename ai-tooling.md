# AI Tooling

## Overview

AI-assisted development was used throughout the project to accelerate implementation, troubleshooting, documentation, and evaluation activities. The final solution was assembled, tested, and validated by the author, while AI tools were used to assist with code generation, debugging, architectural decisions, and project documentation.

---

## AI Tools Used

### ChatGPT (Primary Tool)

ChatGPT was used extensively during development for:

* Project planning and architecture discussions
* RAG pipeline implementation guidance
* LangChain integration assistance
* ChromaDB setup and troubleshooting
* Streamlit application development
* Git and GitHub workflow support
* CI/CD configuration using GitHub Actions
* Evaluation framework creation
* Documentation drafting

ChatGPT was particularly useful when troubleshooting dependency issues, module import errors, retrieval quality problems, and integration of external services such as Groq.

---

### GitHub Copilot (Optional)

GitHub Copilot was occasionally used for code completion and boilerplate generation while working in the development environment.

Its primary value was accelerating repetitive coding tasks and reducing typing effort.

---

## How AI Was Used During Development

### Corpus Creation

AI assistance was used to help generate and refine a synthetic employee policy corpus suitable for the project requirements.

The generated policies were reviewed and modified before inclusion in the final corpus.

---

### RAG Development

AI assistance was used to:

* Design the ingestion pipeline
* Select chunking parameters
* Configure embeddings
* Implement ChromaDB storage
* Develop retrieval logic
* Design prompts and guardrails

Suggestions provided by AI were tested and validated manually before being adopted.

---

### Debugging and Troubleshooting

AI assistance was heavily used during troubleshooting activities including:

* Python virtual environment issues
* Package dependency conflicts
* LangChain version changes
* ChromaDB integration issues
* Groq API integration
* Git and GitHub configuration
* GitHub Actions CI failures

The ability to rapidly diagnose and explain error messages significantly reduced development time.

---

### Evaluation and Documentation

AI assistance was used to:

* Create the evaluation dataset structure
* Design latency measurement scripts
* Analyze evaluation results
* Draft design documentation
* Draft evaluation reports
* Review project completeness against the assignment rubric

All evaluation metrics reported in the project documentation were generated from actual project execution and not synthesized by AI.

---

## What Worked Well

The most valuable use cases were:

* Explaining unfamiliar technologies
* Troubleshooting implementation errors
* Generating boilerplate code
* Producing documentation drafts
* Reviewing architecture decisions
* Providing implementation examples for LangChain and Streamlit

AI significantly accelerated development while allowing the author to focus on system design and validation.

---

## What Did Not Work Well

AI-generated code occasionally:

* Used outdated library APIs
* Assumed incorrect package versions
* Produced code requiring manual adjustment
* Suggested retrieval configurations that required empirical testing

Several generated solutions required debugging and adaptation before they functioned correctly within the project environment.

Additionally, retrieval quality and evaluation metrics could not be reliably determined by AI alone and required manual testing and verification.

---

## Lessons Learned

AI-assisted development can substantially accelerate software engineering tasks, particularly for learning unfamiliar technologies and producing initial implementations. However, generated code must still be tested, validated, and reviewed carefully.

The project demonstrated that AI is most effective as a development assistant rather than a replacement for engineering judgment, experimentation, and validation.
