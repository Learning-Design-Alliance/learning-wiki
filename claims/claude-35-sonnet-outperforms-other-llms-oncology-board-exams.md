---
type: claim
title: "Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%"
description: "Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%"
id: claude-35-sonnet-outperforms-other-llms-oncology-board-exams
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: erdat-2025
    resource: "https://doi.org/10.1186/s12885-025-13596-0"
    title: "Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)"
    author: "Erdat, E. C., & Kavak, E. E."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Claude 3.5 Sonnet scored significantly higher than the other three LLMs on the oncology board exams (ANOVA F = 96.79, p < 0.001), passing all 8 exams with an average score of 77.6 (SD = 7.59). [→ Erdat 2025](#erdat-2025)

## Evidence

### Erdat 2025

Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)

`q2 · i?` · `causal · r1`

Benchmark study administering 790 Turkish multiple-choice oncology board questions (2016–2024) to four LLMs in separate chat sessions. The results section reports Claude 3.5 Sonnet "passing all the 8 exams" with mean 77.6 (SD = 7.59) and a significant ANOVA (F = 96.79, p < 0.001).

> "Claude 3.5 Sonnet outperformed all the other models. The model’s scores ranged from 67 to 86, with an average score 77.6 (SD = 7.59), passing all the 8 exams (ANOVA test, F = 96.79, p < 0.001)."

## Discussion


## Related Claims
- [ChatGPT 4o outperformed Llama-3 and Gemini 1.5 across all question categories, with an average score of 67.8 and its highest accuracy in basic oncology (86.4%)](chatgpt-4o-second-tier-oncology-exam-performance.md) — related
- [Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly](significant-llm-performance-differences-oncology-exams-anova.md) — possibly the same claim (merge candidate)
- [LLM performance declined on more recent exams, with ChatGPT 4o failing the 2024 exam and Llama-3 failing the last four consecutive years, suggesting outdated training data](llm-performance-declines-recent-oncology-exams.md) — related
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)](llm-accuracy-varies-across-oncology-topics.md) — related
