---
type: claim
title: English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language
description: English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language
id: english-only-prompting-beats-multilingual-prompting-llm-tutoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: junior-cedric-tonga-2026
    resource: "https://doi.org/10.18653/2026.mathnlp-main.16"
    title: "Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)"
    author: Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across hint types, English-only student prompting consistently outperforms multilingual prompting, except in the L→L setting where native-language hints pair with native instructions. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r1`

Simulation study over the MGSM benchmark with two student models (Mistral-7B, Aya-8B) and LLaMA-3.3-70B as tutor, comparing multilingual versus English-only student prompts across four hint strategies; the authors report that "English-onlyprompting consistently outperforms multilingualprompting across all hint types, except for the L →L setting."

> "English-onlyprompting consistently outperforms multilingualprompting across all hint types, except for the L →L setting."

## Discussion


## Learner Variables
- [Reading and Language](../learner-variables/reading-and-language.md) — moderator: an instructional effect differs with it

## Related Claims
- [The EN→EN hint generation strategy yields the highest average student gains across setups](en-to-en-hint-strategy-highest-gains.md) — related
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](hint-language-impacts-student-gains.md) — related
- [Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages](multilingual-student-models-lrl-monolingual-hrl.md) — related
