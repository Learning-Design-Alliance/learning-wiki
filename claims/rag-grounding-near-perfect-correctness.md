---
type: claim
title: Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline
description: Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline
id: rag-grounding-near-perfect-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: bhavishya-tarun-2025
    resource: "https://doi.org/10.1109/fie63693.2025.11328658"
    title: "Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)"
    author: Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The RAG pipeline scored 9.70 on Correctness while the untuned LLM baseline scored 7.89. [→ Bhavishya Tarun 2025](#bhavishya-tarun-2025)

## Evidence

### Bhavishya Tarun 2025

Bhavishya Tarun, Haoze Du, Dinesh Kannan, Edward F. Gehringer. (2025). Human-in-the-Loop Systems for Adaptive Learning Using Generative AI. [doi:10.1109/fie63693.2025.11328658](https://doi.org/10.1109/fie63693.2025.11328658)

`q2 · i?` · `design · r2`

GPT-based evaluation of pipeline responses on Object-Oriented Design questions. Retrieval grounding from textbook passages (cosine-similarity ≥ 0.8) yields "Correctness score of 9.70", versus 7.89 for the untuned LLM.

> "The RAG pipeline’s Correctness score of 9.70 nearly matches that of the static “Personalized” pipeline, whereas the untuned LLM baseline falls to 7.89."

## Discussion


## Related Claims
- [Targeted enhancements (retrieval-augmented inference, multimodal training) substantially raise open-source models' phonology mastery to near-ceiling levels](targeted-enhancements-raise-phonology-mastery.md) — related
- [NCERT-tailored RAG preprocessing and figure-aware indexing improve retrieval precision over a generic-chunking baseline, per the authors' assertion](ncert-tailored-rag-improves-retrieval-precision.md) — related
- [In one on-premise introductory computer-science QA system built on open educational resources, a local LLM without retrieval scored below a TF-IDF baseline on 300 test queries](retrieval-augmentation-essential-local-llm-below-tfidf.md) — related
- [Retrieval-augmented generation reduces but does not eliminate hallucinations in AI-assisted verification](rag-reduces-not-eliminates-hallucinations.md) — related
- [The RAG-enhanced assistant achieves context recall above 0.93 and answer relevance of 0.87 on an expert-built 52-question evaluation set](rag-assistant-high-recall-relevance.md) — related
- [Adding RAG context does not improve and appears to reduce MMLU biology accuracy, with the largest declines in the bigger model](rag-context-reduces-small-model-accuracy.md) — related
