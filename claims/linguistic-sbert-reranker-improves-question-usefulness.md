---
type: claim
title: A re-ranker combining SBERT embeddings with linguistic features improves the usefulness of generated questions from 3.42 to 4.01
description: A re-ranker combining SBERT embeddings with linguistic features improves the usefulness of generated questions from 3.42 to 4.01
id: linguistic-sbert-reranker-improves-question-usefulness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: devang-kulshreshtha-2022
    resource: "https://doi.org/10.3233/faia220062"
    title: "Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar. (2022). Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring Systems. arXiv. [doi:10.3233/faia220062](https://doi.org/10.3233/faia220062)"
    author: Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# A re-ranker combining SBERT embeddings with linguistic features improves the usefulness of generated questions from 3.42 to 4.01

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Ling-SBERT re-ranker outperforms all other tested models on MSE, MAE, Pearson correlation, and usefulness metrics. [→ Devang Kulshreshtha 2022](#devang-kulshreshtha-2022)

## Evidence

### Devang Kulshreshtha 2022

Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar. (2022). Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring Systems. arXiv. [doi:10.3233/faia220062](https://doi.org/10.3233/faia220062)

`q1 · i?` · `design · r2`

Regression-based re-ranking experiment training an OLS model on 200 examples and testing on 40: Ling-SBERT reached usefulness 4.01 versus a 3.42 mean baseline (Table 5), with PCR of 0.40 versus the SBERT-only model's 0.38 and the Linguistic-only model's 0.33.

> "We find that Ling-SBERT outperforms all other models for all metrics. More importantly, it improves the usefulness rating from 3.42 to 4.01."

## Discussion


## Related Claims
- [QBERT-RR outperforms the E5 embedding model on question topic and equivalence tasks while E5 leads on answer retrieval](qbert-rr-vs-e5-task-dependent.md) — related
