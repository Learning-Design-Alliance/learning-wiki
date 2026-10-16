---
type: claim
title: "LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it"
description: "LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it"
id: llm-upward-cognitive-shift-asymmetry
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yi-zhang-julia-rayz-2026
    resource: "https://doi.org/10.48550/arxiv.2607.08009"
    title: "Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009 [doi:10.48550/arxiv.2607.08009](https://doi.org/10.48550/arxiv.2607.08009)"
    author: "Yi Zhang & Julia Rayz"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Under both general difficulty prompts and targeted Bloom's levels, the evaluated models more easily add cognitively demanding operations than remove or replace them with lower-level operations. [→ Yi Zhang & Julia Rayz 2026](#yi-zhang-julia-rayz-2026)

## Evidence

### Yi Zhang & Julia Rayz 2026

Yi Zhang & Julia Rayz. (2026). From Execution to Education: A Bloom-Aligned Framework for Measuring Educational Control in LLMs. Preprint. https://arxiv.org/abs/2607.08009 [doi:10.48550/arxiv.2607.08009](https://doi.org/10.48550/arxiv.2607.08009)

`q2 · i?` · `causal · r2`

Behavioral evaluation of 2,520 programming tasks from three benchmarks, judged with an LLM-as-a-judge framework. Under the "Easier" prompt both models still produced positive OCS scores (0.715 and 0.194), and the general model achieved only a marginal negative shift of -0.134 under targeted "Lower" Bloom prompts.

> "OCS scores reveal that the models more easily add cognitively demanding operations than remove or replace them with lower-level operations, under both general difficulty prompts and targeted Bloom's levels."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can a language model write or rewrite questions at a targeted Bloom level?* This table gathers the studies behind this claim and the 5 narrower claims that bear on it: **2 distinct studies** (2 causal), `q2`, 0 of 2 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Yi Zhang & Julia Rayz 2026](https://doi.org/10.48550/arxiv.2607.08009) | q2 · causal · r2 | i? | this claim; [Both models target Higher Bloom levels far more accurately than Lower levels, with the gen](tza-higher-versus-lower-bloom-targets.md) (supports); [Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simpli](downward-shift-benchmark-dependence.md) (qualifies) |
| [abstraction-bias](https://doi.org/10.1145/3770854.3785686) | q2 · causal · r1 | i? | [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-tha](llm-abstraction-bias-higher-order-overproduction.md) (supports); [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fin](cogleap-dominant-fgp-suppresses-regression.md) (supports); [Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of](fgp-improves-catcons-knowcov.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Downward Bloom control is benchmark-dependent: repository-level tasks are easier to simplify than algorithmic puzzles](downward-shift-benchmark-dependence.md) — a narrower finding that bears on this claim
- [Both models target Higher Bloom levels far more accurately than Lower levels, with the general model outperforming the coder model upward](tza-higher-versus-lower-bloom-targets.md) — a narrower finding that bears on this claim
- [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression](cogleap-dominant-fgp-suppresses-regression.md) — related
- [A design-enactment gap in cognitive demand: 37.7% of conversations under-reached the teacher-targeted DOK level, and under-targeting increased with target ambition](dok-under-targeting-gap-ai-dialogue.md) — related
