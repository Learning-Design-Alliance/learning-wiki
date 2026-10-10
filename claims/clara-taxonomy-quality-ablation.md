---
type: claim
title: "Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation"
description: "Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation"
id: clara-taxonomy-quality-ablation
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
  - id: sijing-yin-2026-2
    resource: "https://arxiv.org/abs/2610.05783"
    title: "Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783"
    author: Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Taxonomy quality drives CLARA performance: degraded taxonomies reduce alignment, and removing SEL causes the largest degradation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Degraded taxonomy variants (random mapping, dimension-swapped, coarse) substantially reduce developmental alignment relative to the full taxonomy. [→ Sijing Yin 2026](#sijing-yin-2026)
`q2 i?` In dimension-level ablation, removing SEL leads to the largest performance degradation, with removing COG and LAN also hurting performance. [→ Sijing Yin 2026 (2)](#sijing-yin-2026-2)

## Evidence

### Sijing Yin 2026

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Taxonomy quality ablation (Table 6) comparing full taxonomy against random mapping, dimension-swapped, and coarse taxonomy variants on the benchmark. The article reports "degraded taxonomies sub- stantially reduce developmental alignment quality", indicating gains come from meaningful developmental organization rather than prompt structure alone.

> "As shown in Table 6, degraded taxonomies sub- stantially reduce developmental alignment quality, suggesting that CLARA benefits from meaning- ful developmental organization rather than prompt structure alone."

### Sijing Yin 2026 (2)

Sijing Yin, Zirui Wang, Qian Liu, Jiamou Liu. (2026). CLARA: Can AI Assess Developmental Appropriateness in Children's Stories?. https://arxiv.org/abs/2610.05783

`q2 · i?` · `design · r2`

Dimension-level ablation study (Table 10) removing one of COG, LAN, or SEL at a time. The article reports "removing SEL leads to the largest performance degradation", while removing COG and LAN also negatively affects performance, indicating the dimensions provide complementary developmental signals.

> "removing SEL leads to the largest performance degradation, suggesting that social-emotional development provides important signals beyond linguistic and cognitive complexity alone."

## Discussion


## Related Claims
- [CLARA's gains come from the interaction of structured representation, constrained annotation, and aggregation, not prompt engineering alone](clara-contribution-decomposition.md) — a broader claim this one bears on
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
