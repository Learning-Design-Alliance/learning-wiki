---
type: claim
title: "Eco-mode selection in an LLM interface declines sharply as response latency increases, dropping from about 45% of interactions in eco mode 1 to below 5% in eco mode 5"
description: "Eco-mode selection in an LLM interface declines sharply as response latency increases, dropping from about 45% of interactions in eco mode 1 to below 5% in eco mode 5"
id: eco-mode-selection-declines-with-latency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hyeonwook-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2608.23968"
    title: "Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester. (2026). When LLMs Slow Down: How Environmental Impacts Mediate University Students' LLM Usage. https://arxiv.org/abs/2608.23968 [doi:10.48550/arxiv.2608.23968](https://doi.org/10.48550/arxiv.2608.23968)"
    author: Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Eco-mode selection in an LLM interface declines sharply as response latency increases, dropping from about 45% of interactions in eco mode 1 to below 5% in eco mode 5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Higher perceived latency strongly reduced the likelihood of choosing the eco mode over the default mode (OR = 0.192, p < .001). [→ Hyeonwook Kim 2026](#hyeonwook-kim-2026)
`q2 i?` The proportion of interactions in eco mode fell from approximately 45% in eco mode 1 to below 5% in eco mode 5. [→ Hyeonwook Kim 2026](#hyeonwook-kim-2026)

## Evidence

### Hyeonwook Kim 2026

Hyeonwook Kim, Xuesi Chen, Alex Cabral, Cindy Kaiying Lin, Udit Gupta, Josiah Hester. (2026). When LLMs Slow Down: How Environmental Impacts Mediate University Students' LLM Usage. https://arxiv.org/abs/2608.23968 [doi:10.48550/arxiv.2608.23968](https://doi.org/10.48550/arxiv.2608.23968)

`q2 · i3` · `design · r2`

Mixed-effects logistic regression (GLMM with participant-level random intercepts) of 89 undergraduates' mode choices in a live LLM system found "higher perceived latency was strongly associated with reduced eco mode preference (OR = 0.192,p < .001)". Descriptively, eco-mode selection dropped from about 45% (mode 1) to below 5% (mode 5).

> "higher perceived latency was strongly associated with reduced eco mode preference (OR = 0.192,p < .001). In contrast, recognition of carbon-saving impacts emerged as the strongest positive predictor of eco mode selection"

## Discussion


## Related Claims
- [Recognizing carbon-saving impacts increases the likelihood of selecting eco modes in LLM interactions](carbon-saving-recognition-increases-eco-mode-selection.md) — related
- [Stronger eco-mindedness raises initial eco-mode preference, but this advantage diminishes as response latency increases](eco-mindedness-raises-baseline-eco-preference-limited-by-latency.md) — related
- [User satisfaction with eco modes declines sharply from mode 1 (mean 3.64) to modes 4–5 (means 2.35 and 2.06)](eco-mode-satisfaction-declines-across-modes.md) — related
- [Interacting with an eco-feedback LLM interface surfaces gaps in students' understanding of digital sustainability and supports learning about the environmental impact of everyday LLM use](eco-feedback-interface-supports-sustainability-learning.md) — related
