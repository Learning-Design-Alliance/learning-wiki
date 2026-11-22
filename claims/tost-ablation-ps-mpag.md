---
type: claim
title: Ablations show Parallel Sowing drives exploration of more strategies while Multi-Path Adaptive Guidance maintains solution quality
description: Ablations show Parallel Sowing drives exploration of more strategies while Multi-Path Adaptive Guidance maintains solution quality
id: tost-ablation-ps-mpag
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: feng-ling-and-heng-yu-2026
    resource: "https://doi.org/10.48550/arXiv.2608.25775"
    title: "Feng Ling and Heng Yu. (2026). ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking. [doi:10.48550/arXiv.2608.25775](https://doi.org/10.48550/arXiv.2608.25775)"
    author: Feng Ling and Heng Yu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Ablations show Parallel Sowing drives exploration of more strategies while Multi-Path Adaptive Guidance maintains solution quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Removing Parallel Sowing reduces explored strategies (2.12 to 1.53 on MATH-500), removing MPAG degrades solution quality, and PS alone improves raw students by 3.71% but is insufficient. [→ Feng Ling and Heng Yu 2026](#feng-ling-and-heng-yu-2026)

## Evidence

### Feng Ling and Heng Yu 2026

Feng Ling and Heng Yu. (2026). ToST: A Tree-of-Thought Socratic Teaching Framework for Multi-Path Guidance and Parallel Thinking. [doi:10.48550/arXiv.2608.25775](https://doi.org/10.48550/arXiv.2608.25775)

`q2 · i?` · `causal · r2`

Ablation study within the simulated benchmark evaluation (Table 1), removing Parallel Sowing via single-chain prompting or disabling MPAG by removing explicit path selection, each with three random seeds.

> "Ablations show that removing PS reduces explored strategies (e.g., 2.12 → 1.53 on MATH-500), while removing MPAG de- grades solution quality; PS alone improves raw stu- dents by 3.71% but is insufficient."

## Discussion


## Related Claims
- [In a simulated tutoring agent, removing the behavioral-safety constraint (C3) appears to cause collapse to near-single-action policies, which the authors read as C3 being the most influential safeguard, though its ablation does not differ significantly from removing C1 in RHSI](c3-ablation-policy-collapse.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — a broader claim this one bears on
- [ToST improves guidance success rates by an average of 11% over educational LLM baselines across four math benchmarks](tost-improves-guidance-success-11-percent.md) — related
