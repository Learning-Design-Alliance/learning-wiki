---
type: claim
title: "Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement"
description: "Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement"
id: claude-sonnet-superior-temporal-reliability-radiology-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: atlanoğlu-ş-2026
    resource: "https://doi.org/10.1097/MD.0000000000049517"
    title: "Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517"
    author: Atlanoğlu Ş, Gedik MA
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Claude 4.5 Sonnet achieved very good internal consistency (kappa = 0.872) between responses 1 week apart, whereas Grok-4 (kappa = 0.575) and ChatGPT-5 (kappa = 0.559) exhibited moderate agreement. [→ Atlanoğlu Ş 2026](#atlanoglu-s-2026)

## Evidence

### Atlanoğlu Ş 2026

Atlanoğlu Ş, Gedik MA. (2026). Large language models in radiology exams: A cross-sectional comparative analysis of performance in Turkish and English. Medicine 2026;105:26(e49517). https://doi.org/10.1097/MD.0000000000049517

`q3 · i?` · `causal · r1`

Temporal reliability analysis in which the full 100-question set was resubmitted to Grok-4, Claude 4.5 Sonnet, and ChatGPT-5 in two sessions 1 week apart, with agreement evaluated using Cohen kappa. McNemar tests found no significant accuracy change between sessions (P = .774, 1.000, .344).

> "The analysis demonstrated that Claude 4.5 Sonnet achieved a "very good" level of internal consistency (kappa = 0.872). In contrast, Grok-4 and ChatGPT-5 exhibited "moderate" agreement (kappa = 0.575 and kappa = 0.559, respectively; Table 2)."

## Discussion


## Related Claims
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
- [Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions](no-accuracy-difference-across-llm-versions-radiology.md) — related
