---
type: claim
title: TASA performance is stable for retrieval weight λ in the range 0.3–0.7, with optimal results at λ = 0.5
description: TASA performance is stable for retrieval weight λ in the range 0.3–0.7, with optimal results at λ = 0.5
id: retrieval-weight-lambda-stable-range
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
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

# TASA performance is stable for retrieval weight λ in the range 0.3–0.7, with optimal results at λ = 0.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The hybrid retrieval weighting between semantic similarity and concept-level alignment needs no delicate tuning: performance is stable within [0.3, 0.7] and best at λ = 0.5. [→ Yang Wu 2025](#yang-wu-2025)

## Evidence

### Yang Wu 2025

Yang Wu, Rujing Yao, Tong Zhang, Yufei Shi, Zhuoren Jiang, Zhushan Li, Xiaozhong Liu. (2025). Teaching According to Students’ Aptitude: Personalized Mathematics Tutoring via Persona-, Memory-, and Forgetting-Aware LLMs. arXiv. [doi:10.48550/arXiv.2511.15163](https://doi.org/10.48550/arXiv.2511.15163)

`q2 · i?` · `design · r2`

Numerical sensitivity analysis shown in Figure 3 (right) varying the retrieval weight λ that balances semantic and concept-level similarity. The article reports stable performance "within a broad range [0.3, 0.7]" and optimum at λ = 0.5; no effect size is printed.

> "TASA maintains stable performance within a broad range [0.3, 0.7] across all three backbones, with optimal results atλ= 0.5."

## Discussion


## Related Claims
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — a broader claim this one bears on
