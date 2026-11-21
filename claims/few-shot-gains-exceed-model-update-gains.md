---
type: claim
title: Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools
description: Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools
id: few-shot-gains-exceed-model-update-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: fox-2026
    resource: "https://doi.org/10.48550/arXiv.2605.30151"
    title: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)"
    author: "Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Gemini, few-shot prompting produced larger gains (+8 percentage points) than the model update alone (+/- 0); for Coteach, few-shot prompting recovered performance the update interval had degraded. [→ Fox 2026](#fox-2026)

## Evidence

### Fox 2026

Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)

`q2 · i?` · `causal · r1`

Cross-condition magnitude comparison within the same study, contrasting change from the model-update interval (Time 1 to Time 2a) with change from few-shot prompting (Time 2a to Time 2b). The article states "few-shot prompting produced larger gains (+8 percentage points) than the model update alone (+/- 0)" and concludes prompt optimization is viable against temporal drift.

> "For Gemini, few-shot prompting produced larger gains (+8 percentage points) than the model update alone (+/- 0)."

## Discussion


## Related Claims
- [AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%](ai-task-classification-temporal-instability-seven-weeks.md) — related
- [Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)](few-shot-prompting-improves-math-task-classification.md) — related
- [Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3](few-shot-prompting-gains-heterogeneous-llm.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
