---
type: claim
title: With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models
description: With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models
id: reasoning-mllms-higher-accuracy-image-required-math
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

# With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` On 376 image-Required IM items with figures, reasoning models o4-mini (57.7%) and o3 (52.4%) achieve the highest majority-correct solved rates, while non-reasoning models range from mid-30s to low-40s percent. [→ Croteau 2026](#croteau-2026)

## Evidence

### Croteau 2026

Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/

`q2 · i?` · `causal · r2`

Evaluation of six MLLMs on 376 image-Required Illustrative Mathematics items, three runs per item with images, item-level majority-correct accuracy with bootstrap CIs. The takeaway reports "o4-mini 57.7%, o3 52.4%" versus mid-30s to low-40s for non-reasoning models; no standardized effect size is printed.

> "Reasoning models achieve the highestmajority-correct item-level solved rates(o4-mini 57.7%, o3 52.4%), while non-reasoning models range from mid-30s to low-40s."

## Discussion


## Related Claims
- [Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency](family-permutation-tests-null-differences.md) — related
- [Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items](mllms-refuse-without-required-figures.md) — related
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](moderate-cross-model-agreement-solvability.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
- [On the MathDial problem set with SymPy access, o3-mini(high) and Claude 3.5 Sonnet achieved the highest problem-solving accuracy at 90.00%](o3-mini-highest-mathdial-accuracy.md) — related
