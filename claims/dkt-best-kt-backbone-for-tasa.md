---
type: claim
title: Instantiating TASA with DKT as the knowledge tracing model yields the highest average learning gain among five KT variants
description: Instantiating TASA with DKT as the knowledge tracing model yields the highest average learning gain among five KT variants
id: dkt-best-kt-backbone-for-tasa
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: yang-wu-2025
    resource: "https://doi.org/10.48550/arXiv.2511.15163"
    title: "Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)"
    author: Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Instantiating TASA with DKT as the knowledge tracing model yields the highest average learning gain among five KT variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` TASA with DKT attains the highest average Δ-NLG (57.6), outperforming the history-based approach by 11.0% and other neural KT models by about 9% on average. [→ Yang Wu 2025](#yang-wu-2025)

## Evidence

### Yang Wu 2025

Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)

`q2 · i?` · `design · r2`

KT-backbone comparison (Table 3) on the Llama3.1-8B-Instruct backbone across the four benchmarks, contrasting History-based, AKT, SimKT, LPKT, and DKT instantiations. The article reports TASA-DKT is highest with a printed average of 57.6; no standardized effect size is given.

> "TASADKT attains the highest average∆-NLG, outperforming the simple history-based approach by 11.0% and other neural KT models by 9% on average."

## Discussion


## Related Claims
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks](tasa-outperforms-llm-tutor-baselines.md) — related
