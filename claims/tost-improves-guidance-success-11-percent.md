---
type: claim
title: "ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks"
description: "ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks"
id: tost-improves-guidance-success-11-percent
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

# ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ToST surpasses representative single-chain tutoring methods on every dataset, achieving an average improvement of 11% in guidance success rate. [→ Feng Ling and Heng Yu 2026](#feng-ling-and-heng-yu-2026)

## Evidence

### Feng Ling and Heng Yu 2026

Feng Ling and Heng Yu. (2026). ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking. [doi:10.48550/arXiv.2608.25775](https://doi.org/10.48550/arXiv.2608.25775)

`q2 · i?` · `design · r2`

Simulated benchmark evaluation on MPSG-Bench protocol metrics (Table 1) comparing ToST, fine-tuned QWEN2.5-MATH-7B, against educational agents and general LLMs on GSM8K, MATH-500, AIME24, and AIME25, with "an average improve- ment of 11% in guidance success rate". Three random seeds per experiment.

> "ToST sur- passes representative single-chain tutoring methods on every dataset, achieving an average improve- ment of 11% in guidance success rate, while re- maining competitive with state-of-the-art general LLMs despite using a substantially smaller 7B teacher model."

## Discussion


## Related Claims
- [ToST achieves larger TreeAcc-R efficiency gains, up to 20% over SocraticLM on GSM8K and about 8% over the strongest general LLM on AIME25](tost-treeacc-r-efficiency-gains.md) — a narrower finding that bears on this claim
- [TASA outperforms state-of-the-art LLM tutoring baselines in normalized learning gain and response personalization across four mathematics benchmarks](tasa-outperforms-llm-tutor-baselines.md) — related
- [Ablations show Parallel Sowing drives exploration of more strategies while Multi-Path Adaptive Guidance maintains solution quality](tost-ablation-ps-mpag.md) — related
