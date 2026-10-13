---
type: product
id: varia-benchmark-package-with-follow-up-harness
title: VARIA benchmark package with follow-up harness
description: "Ernesto Lee and colleagues' VARIA package provides assessment-variant blueprints, rubrics, canonical solutions, prompting strategies, evaluation metrics, and runnable follow-up analysis code for benchmarking LLM-generated construct-equivalent assessment variants."
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# VARIA benchmark package with follow-up harness

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Ernesto Lee and colleagues' VARIA package provides assessment-variant blueprints, rubrics, canonical solutions, prompting strategies, evaluation metrics, and runnable follow-up analysis code for benchmarking LLM-generated construct-equivalent assessment variants.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Released VARIA benchmark package with follow-up harness**: The authors release the VARIA benchmark as a code package containing the three pilot blueprints with rubrics and canonical solutions (blueprints.json), a held-out distant-discipline fourth blueprint (Constructing a Historical Argument from Primary Sources) pre-registered as a generalisation probe, four prompting strategies, five complementary metrics, and an evaluation harness. They "release VARIA together with a ready-to-run follow-up harness" implementing per-variant cross-family judging, the full rubric-stability protocol, and multi-run and larger-N regimes (run_followup.py), plus gap_analysis.py for the paired permutation tests. (Ernesto Lee (2026))

### Claims

- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](../claims/varia-frontier-nonfrontier-tier-gap.md) [+W]
- [Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells](../claims/threshold-gating-no-strategy-fully-passes.md) [+W]
- [Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot](../claims/few-shot-anchoring-three-way-tradeoff.md) [+W]
- [Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band](../claims/varia-model-by-prompt-interaction.md) [+W]

## Related Products and Programmes

- [Large-scale field study dataset and code release for AI-generated exam evaluation](large-scale-field-study-dataset-and-code-release-for-ai-generated-exam-evaluation.md)

## Key Sources
- Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://openrouter.ai
