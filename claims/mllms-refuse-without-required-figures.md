---
type: claim
title: Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items
description: Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items
id: mllms-refuse-without-required-figures
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

# Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` When figures are removed on image-Required items, refusals dominate across all six models (95.4%–98.9% of runs), with rare guess-wrong (0.3%–3.0%) and lucky-correct (0.9%–2.7%) answers. [→ Croteau 2026](#croteau-2026)

## Evidence

### Croteau 2026

Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/

`q2 · i?` · `causal · r2`

Without-image condition on the same 376 Required items, 1,128 runs per model, refusal defined as isSolvable=false. The results section reports "refusals dominate:1,076–1,115of1,128runs/model (95.4%–98.9%)"; item-level consistency spans 97.6%–99.7%. No effect size is printed.

> "Across all six models, refusals dominate:1,076–1,115of1,128runs/model (95.4%–98.9%)."

## Discussion


## Related Claims
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](moderate-cross-model-agreement-solvability.md) — related
- [With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models](reasoning-mllms-higher-accuracy-image-required-math.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
- [Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency](family-permutation-tests-null-differences.md) — related
