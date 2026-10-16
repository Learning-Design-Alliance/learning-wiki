---
type: claim
title: "The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)"
description: "The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)"
id: varia-ablation-null-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: ernesto-lee-2026
    resource: "https://doi.org/10.35542/osf.io/u6xef_v2"
    title: "Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2"
    author: Ernesto Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Removing the construct map from chain-of-thought raises the joint score from 0.876 to 0.877 while construct equivalence drops from 0.960 to 0.950, a shift that does not approach significance (p = 0.34); the few-shot wording contrast moves equivalence by two points with an essentially unchanged joint score. [→ Ernesto Lee 2026](#ernesto-lee-2026)

## Evidence

### Ernesto Lee 2026

Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2

`q2 · i?` · `causal · r1`

Descriptive contrasts from the single experimental trial, reported in the Results ablation subsection and confirmed as nulls by exact paired tests (construct-map equivalence shift p = 0.34; few-shot wording contrast p = 0.375 on equivalence, p = 0.87 on joint score).

> "Removing the construct map from chain-of-thought raises the joint score by a sliver ( 0.876 → 0.877 ) — the construct map step does not, in our pilot, materially improve the composite, and a modest drop in construct equivalence ( 0.960 → 0.950 ) is offset by tighter readability dispersion."

## Discussion


## Related Claims
- [Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot](few-shot-anchoring-three-way-tradeoff.md) — related
- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](varia-frontier-nonfrontier-tier-gap.md) — related
- Model performance is robust to minor prompt wording changes but sensitive to holistic rubric redesign — a broader claim this one bears on
- [Chain-of-Thought prompting improves KC planning for Qwen models but its effect varies by model and educational stage](cot-effect-varies-model-stage-kc-planning.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [Chain-of-thought and reasoning prompting significantly improve LLM proportional match with human-authored distractors over direct prompting on both math and science MCQs](reasoning-prompting-improves-llm-distractor-match.md) — related
