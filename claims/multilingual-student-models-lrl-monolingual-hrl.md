---
type: claim
title: Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages
description: Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages
id: multilingual-student-models-lrl-monolingual-hrl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The multilingual Aya-8B tends to be more effective for low-resource languages, while the monolingual Mistral-7B generally performs better on high-resource languages. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r1`

Analysis of Δ rows in Table 1 comparing Mistral-7B and Aya-8B gains under LLaMA-3.3-70B tutoring; the authors conclude that "multilingual LLMs tend to perform better for LRLs, while monolingual LLMs are better suited for HRLs."

> "Overall, as expected, multilingual LLMs tend to perform better for LRLs, while monolingual LLMs are better suited for HRLs."

## Discussion


## Related Claims
- [English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language](english-only-prompting-beats-multilingual-prompting-llm-tutoring.md) — related
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](hint-language-impacts-student-gains.md) — related
- [Multilingual mBERT embeddings uniformly outperform monolingual ELECTRA embeddings when parsing Old English with Modern English-trained models](mbert-beats-electra-on-oe-parsing.md) — related
