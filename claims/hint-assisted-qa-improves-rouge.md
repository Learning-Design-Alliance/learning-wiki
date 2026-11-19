---
type: claim
title: Hint-assisted generative question answering outperforms a vanilla QA model, and entailment consistency further boosts ROUGE
description: Hint-assisted generative question answering outperforms a vanilla QA model, and entailment consistency further boosts ROUGE
id: hint-assisted-qa-improves-rouge
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

# Hint-assisted generative question answering outperforms a vanilla QA model, and entailment consistency further boosts ROUGE

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Korbit QA dataset split (400 train, 50 validation, 100 test), Hint-assisted QA is superior to Vanilla-QA by 1 ROUGE point, and enforcing hint-answer entailment boosts ROUGE by up to 1.5 points. [→ Devang Kulshreshtha 2022](#devang-kulshreshtha-2022)

## Evidence

### Devang Kulshreshtha 2022

Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Vlad Serban, Ekaterina Kochmar. (2022). Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring Systems. arXiv. [doi:10.3233/faia220062](https://doi.org/10.3233/faia220062)

`q1 · i?` · `design · r2`

Simulation experiment training BART-based QA, hint-generator, and hint-assisted QA models on the Korbit dataset of 550 exercises (Table 7): ROUGE-L rises from 29.68 (Vanilla-QA) to 30.63 (Hint-assisted) to 31.35 (Hint+Entailment). The authors call the improvements marginal given limited training data.

> "Hint-assisted QA sys-tem is superior to Vanilla-QA model by 1 ROUGE point, and enforcing hint-answer entailment further boosts ROUGE by up to 1.5 points."

## Discussion


## Related Claims
- [BART outperforms T5 for few-shot question generation on cause-effect exercises, and MLQuestions pre-training further improves BLEU](bart-outperforms-t5-few-shot-question-generation.md) — related
