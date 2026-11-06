---
type: claim
title: ChatGPT-4, Grok XI and Gemini showed strong test-retest consistency (kappa 0.869–0.916), whereas Qwen 2.5 (0.650) and DeepSeek-V3 (0.735) fluctuated more between sessions
description: ChatGPT-4, Grok XI and Gemini showed strong test-retest consistency (kappa 0.869–0.916), whereas Qwen 2.5 (0.650) and DeepSeek-V3 (0.735) fluctuated more between sessions
id: llm-test-retest-consistency-dental-mcqs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: alshammari-abdullah-f-2025
    resource: "https://doi.org/10.1186/s12909-025-07624-7"
    title: "Alshammari Abdullah F., Madfa Ahmed A., Anazi Bassam Ali, Alenezi Yousef E., Alkurdi Khlood A. (2025). Comparison of accuracy and consistency of AI Language models when answering standardised dental MCQs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07624-7"
    author: Alshammari Abdullah F., Madfa Ahmed A., Anazi Bassam Ali, Alenezi Yousef E., Alkurdi Khlood A.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT-4, Grok XI and Gemini showed strong test-retest consistency (kappa 0.869–0.916), whereas Qwen 2.5 (0.650) and DeepSeek-V3 (0.735) fluctuated more between sessions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cohen's kappa for test-retest agreement was 0.916 for ChatGPT-4, 0.869 for Grok XI and 0.874 for Gemini, versus 0.650 for Qwen 2.5 and 0.735 for DeepSeek-V3; all McNemar tests were non-significant. [→ Alshammari Abdullah F. 2025](#alshammari-abdullah-f-2025)

## Evidence

### Alshammari Abdullah F. 2025

Alshammari Abdullah F., Madfa Ahmed A., Anazi Bassam Ali, Alenezi Yousef E., Alkurdi Khlood A. (2025). Comparison of accuracy and consistency of AI Language models when answering standardised dental MCQs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07624-7

`q2 · i?` · `design · r2`

Test-retest consistency analysis of the two MCQ sessions using Cohen's kappa and McNemar's test (Table 2). ChatGPT-4's kappa was 0.916 with McNemar p = 1.000; the article reports kappa 0.869 (Grok XI), 0.874 (Gemini), 0.650 (Qwen 2.5) and 0.735 (DeepSeek-V3).

> "ChatGPT-4 demonstrated the highest level of response stability, with a kappa value of 0.916. Between the two testing sessions, 136 answers remained consistently correct, one response changed from correct to incorrect and one changed from incorrect to correct. McNemar's test yielded a p-value of 1.000."

## Discussion


## Related Claims
- [ChatGPT-4 achieved the highest accuracy of the five tested AI models on standardised dental MCQs, at 91.3% in both testing sessions](chatgpt-4-highest-accuracy-dental-mcqs-91-3.md) — related
- [Grok XI improved from 90.7% to 92.7% and Gemini from 87.3% to 88.7% between the two testing sessions, while DeepSeek-V3 declined from 87.3% to 86.7%](grok-gemini-accuracy-shift-between-sessions.md) — related
- [ChatGPT-4 and Grok XI answered the highest proportion of dental MCQs correctly overall, with top scores ranging from 89.3% to 92.7% across sessions](top-llm-scores-89-93-to-92-7-dental-mcqs.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [Large closed-weights LLMs show high test-retest reliability when scoring clinical summary statements across repeated runs](llm-high-test-retest-reliability-summary-statement-scoring.md) — related
- [Inter-model agreement is moderate, indicating models do not consistently identify the same questions correctly](moderate-inter-model-agreement-endodontic-questions.md) — related
