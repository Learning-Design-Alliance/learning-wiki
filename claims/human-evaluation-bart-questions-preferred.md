---
type: claim
title: Human evaluators judge BART-generated questions more useful than T5-generated questions
description: Human evaluators judge BART-generated questions more useful than T5-generated questions
id: human-evaluation-bart-questions-preferred
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
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human evaluators judge BART-generated questions more useful than T5-generated questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In pairwise human comparison of questions for 80 randomly sampled reference solutions, BART is judged the more useful generator. [→ Devang Kulshreshtha 2022](#devang-kulshreshtha-2022)

## Evidence

### Devang Kulshreshtha 2022

Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar. (2022). Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring Systems. arXiv. [doi:10.3233/faia220062](https://doi.org/10.3233/faia220062)

`q2 · i?` · `design · r2`

Human evaluation where annotators compared T5-QG and BART-ML-QG questions on 80 randomly sampled reference solutions, choosing among T5, BART, BOTH, and NONE labels (Figure 3). The article reports BART as the clear winner, consistent with its BLEU results.

> "The results from Figure 3 indicate that BART model is the clear winner, which is also supported by the superior BLEU scores."

## Discussion


## Related Claims
- [BART outperforms T5 for few-shot question generation on cause-effect exercises, and MLQuestions pre-training further improves BLEU](bart-outperforms-t5-few-shot-question-generation.md) — related
