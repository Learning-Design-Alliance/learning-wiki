---
type: claim
title: "ToST achieves larger TreeAcc-R efficiency gains, up to 20% over SocraticLM on GSM8K and about 8% over the strongest general LLM on AIME25"
description: "ToST achieves larger TreeAcc-R efficiency gains, up to 20% over SocraticLM on GSM8K and about 8% over the strongest general LLM on AIME25"
id: tost-treeacc-r-efficiency-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: feng-ling-and-heng-yu-2026
    resource: "https://doi.org/10.48550/arXiv.2608.25775"
    title: "Feng Ling and Heng Yu. (2026). ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking. [doi:10.48550/arXiv.2608.25775](https://doi.org/10.48550/arXiv.2608.25775)"
    author: Feng Ling and Heng Yu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ToST achieves larger TreeAcc-R efficiency gains, up to 20% over SocraticLM on GSM8K and about 8% over the strongest general LLM on AIME25

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ToST's advantage is more pronounced under TreeAcc-R, with gains of up to 20% over SocraticLM on GSM8K and approximately 8% over the strongest general-purpose LLM baseline on AIME25. [→ Feng Ling and Heng Yu 2026](#feng-ling-and-heng-yu-2026)

## Evidence

### Feng Ling and Heng Yu 2026

Feng Ling and Heng Yu. (2026). ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking. [doi:10.48550/arXiv.2608.25775](https://doi.org/10.48550/arXiv.2608.25775)

`q2 · i?` · `design · r2`

Simulated benchmark results (Table 1) on the accuracy-per-round metric TreeAcc-R, defined as TreeAcc divided by average guidance rounds, showing "gains of up to 20% over the single-chain method SocraticLM on GSM8K".

> "The advantage of ToST is more pronounced under TreeAcc-R, with gains of up to 20% over the single-chain method SocraticLM on GSM8K, underscoring the effectiveness of multi-path reasoning."

## Discussion


## Related Claims
- [ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks](tost-improves-guidance-success-11-percent.md) — a broader claim this one bears on
- [SOLO stage-transition analysis shows ToST promotes upward cognitive transitions, e.g., 73.3% S3→S4, exceeding SocraticLM](tost-solo-stage-transitions.md) — related
