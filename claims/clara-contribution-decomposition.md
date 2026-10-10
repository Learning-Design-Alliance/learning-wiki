---
type: claim
title: "CLARA's gains come from the interaction of structured representation, constrained annotation, and aggregation, not prompt engineering alone"
description: "CLARA's gains come from the interaction of structured representation, constrained annotation, and aggregation, not prompt engineering alone"
id: clara-contribution-decomposition
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sijing-yin-2026
    resource: "https://arxiv.org/abs/2610.05783"
    title: "Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783"
    author: Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CLARA's gains come from the interaction of structured representation, constrained annotation, and aggregation, not prompt engineering alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Progressive addition of structured components (taxonomy labels, age mapping, aggregation) yields progressive improvement over free-form annotation with aggregation. [→ Sijing Yin 2026](#sijing-yin-2026)

## Evidence

### Sijing Yin 2026

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Contribution decomposition study (Table 5) comparing GPT-4o direct, free-form with aggregation, taxonomy labels, taxonomy plus mapping, and full CLARA. The article reports "progressive improvement as addi- tional structured components are introduced", with the taxonomy itself contributing substantially to developmental alignment.

> "Table 5 shows progressive improvement as addi- tional structured components are introduced. The taxonomy itself contributes substantially to devel- opmental alignment, while explicit developmen- tal age mapping and structured aggregation fur- ther improve performance."

## Discussion


## Related Claims
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
- [Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation](clara-taxonomy-quality-ablation.md) — a narrower finding that bears on this claim
- [In disagreement cases, blinded educators more frequently prefer CLARA developmental estimates over publisher recommendations](educators-prefer-clara-over-publisher-labels.md) — related
