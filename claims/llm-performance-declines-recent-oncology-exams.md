---
type: claim
title: LLM performance declined on more recent exams, with ChatGPT 4o failing the 2024 exam and Llama-3 failing the last four consecutive years, suggesting outdated training data
description: LLM performance declined on more recent exams, with ChatGPT 4o failing the 2024 exam and Llama-3 failing the last four consecutive years, suggesting outdated training data
id: llm-performance-declines-recent-oncology-exams
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
    kind: design
    rigour: 2
---

# LLM performance declined on more recent exams, with ChatGPT 4o failing the 2024 exam and Llama-3 failing the last four consecutive years, suggesting outdated training data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ChatGPT 4o passed 7 of 8 exams, failing only 2024 with 44 points below the required 50, and Llama-3 failed to achieve the passing score in the last four consecutive years, indicating a declining trend in performance. [→ Erdat 2025](#erdat-2025)

## Evidence

### Erdat 2025

Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)

`q2 · i?` · `design · r2`

Per-year results in the Results section and Table 2 show declining scores toward the end of the study period; the article interprets the 2024 decline as suggesting the models may not be up to date with the most recent oncology advancements.

> "ChatGPT 4o passed 7 out of 8 exams, failing only in 2024 when it scored 44 points, which was below the required 50 points for passing."

## Discussion


## Related Claims
- [Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%](claude-35-sonnet-outperforms-other-llms-oncology-board-exams.md) — related
- [ChatGPT 4o outperformed Llama-3 and Gemini 1.5 across all question categories, with an average score of 67.8 and its highest accuracy in basic oncology (86.4%)](chatgpt-4o-second-tier-oncology-exam-performance.md) — related
- [Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly](significant-llm-performance-differences-oncology-exams-anova.md) — related
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
