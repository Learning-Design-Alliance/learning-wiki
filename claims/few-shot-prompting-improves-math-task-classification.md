---
type: claim
title: "Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)"
description: "Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)"
id: few-shot-prompting-improves-math-task-classification
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

# Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding eight exemplar tasks with correct classifications raised Gemini's accuracy from 58% to 67% and Coteach's from 50% to 75%, returning Coteach to baseline. [→ Fox 2026](#fox-2026)

## Evidence

### Fox 2026

Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)

`q2 · i?` · `causal · r1`

Within-model comparison at Time 2b, immediately after the Time 2a zero-shot retest, using two expert-coded exemplar tasks per TAG category presented in low-to-high demand order. The article reports the gains verbatim: "For Gemini, overall accuracy increased from 58% to 67% (8 of 12 tasks)."

> "For Gemini, overall accuracy increased from 58% to 67% (8 of 12 tasks). For Coteach, accuracy increased from 50% to 75% (9 of 12 tasks), representing a full return to baseline performance."

## Discussion


## Related Claims
- [AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%](ai-task-classification-temporal-instability-seven-weeks.md) — related
- [Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools](few-shot-gains-exceed-model-update-gains.md) — related
- [Few-shot prompting substantially improves Talk Move classification for some models (Claude 4.5 Opus κ 0.48→0.58; Gemini 2.5 Pro 0.38→0.57) but yields minimal gains for GPT-5 and o3](few-shot-prompting-gains-heterogeneous-llm.md) — related
- [Classification accuracy varied substantially by cognitive demand category: Procedures without Connections was most accurate (avg. 94%) and Doing Mathematics least (avg. 33%)](classification-accuracy-varies-by-cognitive-demand-category.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting score at or above zero-shot on every dataset tested, and above it in most comparisons](in-context-examples-improve-bloom-classification.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
