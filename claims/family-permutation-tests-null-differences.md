---
type: claim
title: Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency
description: Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency
id: family-permutation-tests-null-differences
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
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

# Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Permutation tests shuffling model-to-family assignment did not detect reliable differences in majority-correct solved rate (+12.77pp, p=0.197), with-image refusal (+8.63pp, p=0.298), or item-level consistency (−2.30pp, p=0.400). [→ Croteau 2026](#croteau-2026)

## Evidence

### Croteau 2026

Croteau, E., & Heffernan, N. (2026). Seeing Is Solving: MLLMs, Reasoning, and Refusal in Visual Math. https://osf.io/ct7bg/

`q2 · i?` · `causal · r2`

Family-level uncertainty analysis using item-level permutation tests (3-vs-3 model split, items as unit, two-sided p-values) reported in the Results uncertainty subsection. Only test statistics and p-values are printed, so no effect size is coded; non-detection is not equivalence.

> "these did not detectreliable differences in majority-correct solved rate (Reasoning−Non:+12.77pp,p= 0.197), with-image refusal (+8.63pp,p= 0.298), or item-level consistency (−2.30pp,p= 0.400)."

## Discussion


## Related Claims
- [With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models](reasoning-mllms-higher-accuracy-image-required-math.md) — related
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](moderate-cross-model-agreement-solvability.md) — related
- [In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve](visual-misread-dominant-non-reasoning-failure.md) — related
- [Without required figures, multimodal LLMs overwhelmingly refuse rather than guess on image-Required math items](mllms-refuse-without-required-figures.md) — related
