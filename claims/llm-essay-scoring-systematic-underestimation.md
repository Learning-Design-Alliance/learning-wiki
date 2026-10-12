---
type: claim
title: Systematic underestimation of human scores is the dominant bias trend across LLM essay scoring, with some models also compressing scores into a narrow range
description: Systematic underestimation of human scores is the dominant bias trend across LLM essay scoring, with some models also compressing scores into a narrow range
id: llm-essay-scoring-systematic-underestimation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: tongxi-liu-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100565"
    title: "Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565"
    author: Tongxi Liu, Luyao Ye, Wei Yan
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Systematic underestimation of human scores is the dominant bias trend across LLM essay scoring, with some models also compressing scores into a narrow range

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Most models systematically assigned lower scores than human raters, a consistent negative bias the article interprets as a calibration offset rather than random fluctuation. [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Bland-Altman bias analysis across five LLMs and four IELTS dimensions, reported in Results §4.3 with Fig. 4. The article describes the negative bias as a "general calibration offset rather than random fluctuation" with magnitude varying by model and criterion.

> "Specifically, underestimation emerged as the dominant trend, indi - cating that most models systematically assigned lower scores than human raters (Fig. 4)."

## Discussion


## Related Claims
- [In one reviewed study, GPT-4 automated essay scoring showed score inflation, with AI–human rating discrepancies exceeding 1.5 standard deviations in 38% of graduate-level bibliographies](gpt4-essay-score-inflation.md) — reports the opposite
- [Under the initial rubric with direct evaluation, machine raters systematically underestimate openness while relevance and clarity align near-perfectly](initial-rubric-openness-systematic-underestimation.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — reports the opposite
- [ML-based scoring approaches more often overestimated expert-assigned scores, whereas LLM-based approaches more often underestimated them](ml-overestimates-llm-underestimates-pattern.md) — possibly the same claim (merge candidate)
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
