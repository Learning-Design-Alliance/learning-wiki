---
type: claim
title: Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases
description: Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases
id: hint-language-impacts-student-gains
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

# Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Hint language substantially affects student model gains; English hints yield the highest median improvements in most configurations, though native-language hints can be competitive or superior for HRLs with monolingual students. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r2`

Table 1 analysis of hint language effects with LLaMA-3.3-70B; the authors find that "hint language substantially impacts student model gains," with English hints giving the best LRL results (e.g., 38.19% for Mistral-7B in the English-only setup) and native hints winning some HRL cases.

> "Using the larger tutor model,LLaMA-3.3-70B, we find that hint language substantially impacts student model gains as shown in Table 1."

## Discussion


## Related Claims
- [The EN→EN hint generation strategy yields the highest average student gains across setups](en-to-en-hint-strategy-highest-gains.md) — related
- [English-only student prompting generally outperforms multilingual prompting for student gains, except when instructions and hints are both in the native language](english-only-prompting-beats-multilingual-prompting-llm-tutoring.md) — related
- [Gold answer leakage in generated hints is low for the main tutor model but higher for low-resource languages](gold-answer-leakage-low-lrl-higher.md) — related
- [A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages](larger-tutor-model-greater-student-gains.md) — related
- [Multilingual student models perform better for low-resource languages while monolingual models suit high-resource languages](multilingual-student-models-lrl-monolingual-hrl.md) — related
