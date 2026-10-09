---
type: claim
title: Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement
description: Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement
id: moderate-cross-model-agreement-solvability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: croteau-2026
    resource: "https://osf.io/ct7bg/"
    title: "Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/"
    author: "Croteau, E., & Heffernan, N."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Pairwise Cohen's kappa on majority-correct solvability averages 0.54; the non-reasoning trio averages 0.64, the reasoning trio 0.56, and cross-family pairs 0.50. [→ Croteau 2026](#croteau-2026)

## Evidence

### Croteau 2026

Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/

`q2 · i?` · `causal · r2`

Cross-model agreement analysis on Required items with images using majority-correct (≥2/3 runs) item labels; pairwise Cohen's kappa computed for all model pairs. The section reports mean off-diagonal kappa of 0.54 and the family-level averages quoted here; no standardized effect size applies.

> "Within-family agreement exceeded cross-family: thenon-reasoning trio averagedκ= 0.64, the reasoning trioκ= 0.56, while cross-family pairs averagedκ= 0.50."

## Discussion


## Related Claims
- [Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency](family-permutation-tests-null-differences.md) — related
- [Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items](mllms-refuse-without-required-figures.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — a broader claim this one bears on
- [With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models](reasoning-mllms-higher-accuracy-image-required-math.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
