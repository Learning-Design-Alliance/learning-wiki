---
type: claim
title: BART outperforms T5 for few-shot question generation on cause-effect exercises, and MLQuestions pre-training further improves BLEU
description: BART outperforms T5 for few-shot question generation on cause-effect exercises, and MLQuestions pre-training further improves BLEU
id: bart-outperforms-t5-few-shot-question-generation
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

# BART outperforms T5 for few-shot question generation on cause-effect exercises, and MLQuestions pre-training further improves BLEU

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the 40-example test set, BART outperforms T5 by 4 BLEU1 points, and pre-training on MLQuestions increases BLEU1 by 1.5 absolute points. [→ Devang Kulshreshtha 2022](#devang-kulshreshtha-2022)

## Evidence

### Devang Kulshreshtha 2022

Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar. (2022). Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring Systems. arXiv. [doi:10.3233/faia220062](https://doi.org/10.3233/faia220062)

`q1 · i?` · `design · r2`

Evaluation of three question generation models (T5-QG, BART-QG, BART-ML-QG) with BLEU1-4 and ROUGE-L on the 40-example test set (Table 4): BART-ML-QG scores 36.1 BLEU1 versus 30.4 for T5-QG. Numerical evaluation result on a very small test set.

> "We find BART outperforms T5 by 4 BLEU1 points, showing that BART is better suited for conditional generation. Also pre-training on MLQuestions dataset [17] increases BLEU1 by 1.5 absolute points."

## Discussion


## Related Claims
- [Human evaluators judge BART-generated questions more useful than T5-generated questions](human-evaluation-bart-questions-preferred.md) — related
- [Hint-assisted generative question answering outperforms a vanilla QA model, and entailment consistency further boosts ROUGE](hint-assisted-qa-improves-rouge.md) — related
