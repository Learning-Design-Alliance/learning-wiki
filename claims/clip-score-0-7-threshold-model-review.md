---
type: claim
title: A CLIP score threshold of 0.7 flags suspicious 3D models for manual review
description: A CLIP score threshold of 0.7 flags suspicious 3D models for manual review
id: clip-score-0-7-threshold-model-review
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: wang-yibo-2024
    resource: "https://doi.org/10.48550/arXiv.2405.13701"
    title: "WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan. (2024). Metabook: A Mobile-to-Headset Pipeline for 3D Story Book Creation in Augmented Reality. [doi:10.48550/arXiv.2405.13701](https://doi.org/10.48550/arXiv.2405.13701)"
    author: WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A CLIP score threshold of 0.7 flags suspicious 3D models for manual review

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All models with CLIP score above 0.6 were at least 96% plausible, supporting a 0.7 review threshold. [→ WANG Yibo 2024](#wang-yibo-2024)

## Evidence

### WANG Yibo 2024

WANG Yibo, MAO Yuanyuan, Lik-Hang Lee, NI Shi-ting, WANG Zeyu, GU Xiaole, HUI Pan. (2024). Metabook: A Mobile-to-Headset Pipeline for 3D Story Book Creation in Augmented Reality. [doi:10.48550/arXiv.2405.13701](https://doi.org/10.48550/arXiv.2405.13701)

`q2 · i?` · `design · r2`

Workshop evaluation of 183 text-model pairs tagged by five illustrators and scored with CLIP; proportions of plausible models were 100% at thresholds 0.9–0.7 and 96% at 0.6, motivating the S<0.7 manual-review rule.

> "Based on the result, we decided that all models with S <0.7 need to be manually reviewed."

## Discussion


## Related Claims
- [No detection threshold simultaneously keeps original flag rates, light-edit capture, and AI-pool false negatives low](no-threshold-satisfies-all-three-error-rates.md) — related
