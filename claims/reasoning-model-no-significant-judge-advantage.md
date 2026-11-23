---
type: claim
title: The reasoning model o3-mini/low wins most often among judge models but does not significantly outperform the non-reasoning GPT-4o models
description: The reasoning model o3-mini/low wins most often among judge models but does not significantly outperform the non-reasoning GPT-4o models
id: reasoning-model-no-significant-judge-advantage
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: tobias-geisler-and-gerd-kortemeyer-2026
    resource: "https://doi.org/10.1103/9hh9-vt4d"
    title: "Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)"
    author: Tobias Geisler and Gerd Kortemeyer
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# The reasoning model o3-mini/low wins most often among judge models but does not significantly outperform the non-reasoning GPT-4o models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Aggregating highest macro-F1 wins across metrics, o3-mini/low leads with 11 victories (44%), GPT-4o has 9 (36%), and GPT-4o-mini 5 (20%), and the reasoning model does not significantly outperform the non-reasoning one. [→ Tobias Geisler and Gerd Kortemeyer 2026](#tobias-geisler-and-gerd-kortemeyer-2026)

## Evidence

### Tobias Geisler and Gerd Kortemeyer 2026

Tobias Geisler and Gerd Kortemeyer. (2026). When AI Evaluates Its Own Work: Validating Learner-Initiated, AI-Generated Physics Practice Problems. arXiv. [doi:10.1103/9hh9-vt4d](https://doi.org/10.1103/9hh9-vt4d)

`q2 · i?` · `associational · r1`

Model-comparison aggregation across the metric benchmark in Results. The article reports the win counts and states the reasoning model "does not significantly outperform the non-reasoning one"; no effect size is printed.

> "the o3-mini/low variant leads with 11 victories (44 %), followed by GPT-4o with 9 wins (36 %) and GPT-4o-mini with 5 wins (20 %). Although o3-mini/low holds the top spot, more than half of the winning metrics still favor GPT-4o-based models — the reasoning model does not significantly outperform the non-reasoning one."

## Discussion


## Related Claims
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [On the MathDial problem set with SymPy access, o3-mini(high) and Claude 3.5 Sonnet achieved the highest problem-solving accuracy at 90.00%](o3-mini-highest-mathdial-accuracy.md) — related
- [On the LearnArena benchmark, GPT-4o achieves the best average win rate (0.77), and learning ability improves with model scale but with diminishing gains](learnarena-gpt4o-best-scale-diminishing-gains.md) — related
