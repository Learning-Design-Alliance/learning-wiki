---
type: claim
title: "AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%"
description: "AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%"
id: ai-task-classification-temporal-instability-seven-weeks
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

# AI classification accuracy on math cognitive-demand tasks is temporally unstable over a seven-week interval, with Gemini stable at 58% and Coteach declining from 75% to 50%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Over seven weeks, Gemini's overall accuracy remained 58% while Coteach's overall accuracy declined 25 percentage points from 75% to 50%. [→ Fox 2026](#fox-2026)

## Evidence

### Fox 2026

Fox, D. S., Robles, B. L., DiPietro Brovey, E., & Schunn, C. D. (2026). Temporal Stability and Few-Shot Prompting in Math Task Assessment. [doi:10.48550/arXiv.2605.30151](https://doi.org/10.48550/arXiv.2605.30151)

`q2 · i?` · `causal · r1`

Longitudinal retesting of two AI tools classifying twelve expert-coded math tasks at baseline (October 30, 2025) and seven weeks later, after Gemini's update from 2.5 Flash to 3 Flash. The article reports "Gemini's overall accuracy was the same at both time points (58%, 7 of 12 tasks)" and a 25-percentage-point decline for Coteach (75% to 50%).

> "Gemini's overall accuracy was the same at both time points (58%, 7 of 12 tasks)."

## Discussion


## Related Claims
- [Few-shot prompting with two exemplars per cognitive-demand category improved both AI tools' classification accuracy (Gemini 58% to 67%; Coteach 50% to 75%)](few-shot-prompting-improves-math-task-classification.md) — related
- [Gemini showed task-level redistribution of correct classifications despite unchanged overall accuracy, a pattern the authors call consistent with prompt drift](gemini-task-level-redistribution-prompt-drift.md) — related
- [Few-shot prompting produced larger accuracy gains than model updates alone for both AI tools](few-shot-gains-exceed-model-update-gains.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [ChatGPT-4, Grok XI and Gemini showed strong test-retest consistency (kappa 0.869–0.916), whereas Qwen 2.5 (0.650) and DeepSeek-V3 (0.735) fluctuated more between sessions](llm-test-retest-consistency-dental-mcqs.md) — related
