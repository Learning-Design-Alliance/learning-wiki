---
type: claim
title: "Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly"
description: "Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly"
id: significant-llm-performance-differences-oncology-exams-anova
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
  - id: erdat-2025-2
    resource: "https://doi.org/10.1186/s12885-025-13596-0"
    title: "Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)"
    author: "Erdat, E. C., & Kavak, E. E."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A one-way ANOVA found significant differences in exam scores among the four LLMs (F = 19.31, p < 0.001), with Tukey HSD post-hoc comparisons showing Claude 3.5 Sonnet significantly higher than the other three and ChatGPT 4o significantly higher than Llama-3 and Gemini 1.5. [→ Erdat 2025](#erdat-2025)
`q2 i?` A chi-square test showed no significant differences between passed exams among the different LLMs (p = 0.378); equivalence was not otherwise tested. [→ Erdat 2025 (2)](#erdat-2025-2)

## Evidence

### Erdat 2025

Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)

`q2 · i?` · `design · r2`

Omnibus one-way ANOVA over the eight annual exams reported in the Results section: significant difference in performance among the four LLMs (F = 19.31, p < 0.001). Post-hoc Tukey HSD comparisons established the pairwise ordering among the named models.

> "A one-way analysis of variance (ANOVA) was conducted to determine if there were statistically significant differences in exam scores among the three LLMs and there was a significant difference in performance among four LLMs among years, (ANOVA test, F = 19.31, p < 0.001)."

### Erdat 2025 (2)

Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)

`q2 · i?` · `design · r2`

Chi-square test on the number of passed exams per model, reported in the Results section, was not significant (p = 0.378). No effect size is printed, so no magnitude is asserted.

> "The chi-square test showed no significant differences between passed exams among different LLMs (p = 0.378)."

## Discussion


## Related Claims
- [ChatGPT 4o outperformed Llama-3 and Gemini 1.5 across all question categories, with an average score of 67.8 and its highest accuracy in basic oncology (86.4%)](chatgpt-4o-second-tier-oncology-exam-performance.md) — possibly the same claim (merge candidate)
- [Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%](claude-35-sonnet-outperforms-other-llms-oncology-board-exams.md) — possibly the same claim (merge candidate)
- [LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)](llm-accuracy-varies-across-oncology-topics.md) — related
- [LLM performance declined on more recent exams, with ChatGPT 4o failing the 2024 exam and Llama-3 failing the last four consecutive years, suggesting outdated training data](llm-performance-declines-recent-oncology-exams.md) — related
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
