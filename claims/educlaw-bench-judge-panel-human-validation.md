---
type: claim
title: The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding
description: The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding
id: educlaw-bench-judge-panel-human-validation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: lee-2026
    resource: "https://arxiv.org/abs/2608.03206"
    title: "Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206"
    author: Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A three-family LLM judge panel agrees with two blind domain experts on every judged axis (permutation p < 0.05), reaching the expert ceiling on answer-holding and tracking Helpfulness and the curriculum axes as a positive but more modest proxy. [→ Lee 2026](#lee-2026)

## Evidence

### Lee 2026

Lee, U.; Lee, S.; Jeong, Y.; Lee, E.; Shin, M.; Kwon, H. (2026). EduClaw-Bench: A Long-Horizon Benchmark for Pedagogical LLM Agents with Simulated Learners. https://arxiv.org/abs/2608.03206

`q2 · i?` · `design · r2`

Human validation with two domain experts scoring about 40 judged days per axis, blind to the panel. Panel–expert Spearman ρ was 0.33 (Helpfulness), 0.43 (Gagné), 0.49 (Rosenshine), and 0.82 (answer-holding), against expert–expert ceilings of 0.91, 0.64, 0.90, and 0.85.

> "The panel agrees with the experts on every judged axis (permutation p <0.05), reaching the expert ceiling on answer-holding and tracking Helpfulness and the two curriculum axes as a positive but more modest proxy."

## Discussion


## Related Claims
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — reports the opposite
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — reports the opposite
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
