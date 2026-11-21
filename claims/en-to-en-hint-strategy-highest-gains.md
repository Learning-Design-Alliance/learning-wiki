---
type: claim
title: The EN→EN hint generation strategy yields the highest average student gains across setups
description: The EN→EN hint generation strategy yields the highest average student gains across setups
id: en-to-en-hint-strategy-highest-gains
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
    rigour: 2
---

# The EN→EN hint generation strategy yields the highest average student gains across setups

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` English-to-English hint prompting outperforms the other three hint strategies on average in both multilingual and English-only setups. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r2`

Comparative analysis of four hint generation strategies (EN→EN, EN→EN→L, EN→L, L→L) using LLaMA-3.3-70B as tutor across 11 MGSM languages; the authors state the EN→EN strategy "yields the highest average improvement across both setups, outperforming other hint prompting strategies."

> "yields the highest average improvement across both setups, outperforming other hint prompting strategies. This indicates that models are highly responsive to English prompts."

## Discussion


## Related Claims
- [English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language](english-only-prompting-beats-multilingual-prompting-llm-tutoring.md) — related
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](hint-language-impacts-student-gains.md) — related
- [English prompts generally yield better LLM accuracy than language-matched prompts, but top models perform comparably with language-matched prompts](english-prompt-advantage-top-models-comparable.md) — a broader claim this one bears on
