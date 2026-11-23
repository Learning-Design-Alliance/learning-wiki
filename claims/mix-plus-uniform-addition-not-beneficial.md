---
type: claim
title: Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning
description: Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning
id: mix-plus-uniform-addition-not-beneficial
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: hanyu-zhao-2025
    resource: "https://doi.org/10.1609/aaai.v39i24.34798"
    title: "Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)"
    author: Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Uniformly adding more preliminary-category instructions (Mix+) does not necessarily improve performance, unlike sequenced curriculum learning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Hanyu Zhao 2024: the intervention came bundled with another change (read from the study by two models, 2026-11-23)

## Subclaims
`q2 i?` Comparing DT-CSFT with the Mix+ baseline shows that incorporating more instructions without sequencing them does not necessarily bring benefits to model performance. [→ Hanyu Zhao 2025](#hanyu-zhao-2025)

## Evidence

### Hanyu Zhao 2025

Hanyu Zhao, Li Du, Yiming Ju, Chengwei Wu, Tengfei Pan. (2025). Beyond IID: Optimizing Instruction Learning from the Perspective of Instruction Interaction and Dependency. Originally published 2024. [doi:10.1609/aaai.v39i24.34798](https://doi.org/10.1609/aaai.v39i24.34798)

`q2 · i?` · `causal · r2`

Baseline comparison within the curriculum fine-tuning experiment, where Mix+ uniformly mixes 2|D| additional preliminary category instructions within each epoch instead of sequencing them. The authors conclude that "the importance of sequentially arranging the training samples in curriculum learning" matters; no effect size is printed.

> "Comparing DT-CSFT with Mix+ shows that incorpo- rating more instructions would not necessarily bring ben- efits to model performance."

## Discussion


## Related Claims
- [DT-CSFT curriculum learning, which front-loads preliminary instruction categories, improves SFT performance over DEITA](dt-csft-curriculum-improves-sft.md) — related
- [EE-CPO improves LLM performance over the DEITA baseline by optimizing instruction category proportion alone](ee-cpo-improves-over-deita.md) — related
