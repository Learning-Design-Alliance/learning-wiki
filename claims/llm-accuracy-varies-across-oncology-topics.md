---
type: claim
title: "LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)"
description: "LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)"
id: llm-accuracy-varies-across-oncology-topics
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

# LLM accuracy varied significantly across oncology topics, with the lowest performance in colorectal tumors (mean 48.3%) and genitourinary tumors (mean 50.8%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A one-way repeated measures ANOVA found significant differences in model performance across topics (F = 4.88, p < 0.001), with the lowest performance in colorectal tumors (mean = 48.3%, SD = 17.7%) and genitourinary tumors (mean = 50.8%, SD = 15.5%). [→ Erdat 2025](#erdat-2025)

## Evidence

### Erdat 2025

Erdat, E. C., & Kavak, E. E. (2025). Benchmarking LLM chatbots’ oncological knowledge with the Turkish Society of Medical Oncology’s annual board examination questions. *BMC Cancer*. [doi:10.1186/s12885-025-13596-0](https://doi.org/10.1186/s12885-025-13596-0)

`q2 · i?` · `design · r2`

Topic-level analysis of the 790-question benchmark reported in the Results section with per-category accuracy in Table 3. The repeated measures ANOVA was significant (F = 4.88, p < 0.001); the printed means identify colorectal and genitourinary tumors as the weakest categories.

> "Based on the one-way repeated measures ANOVA results (F = 4.88, p < 0.001), there were significant differences in model performance across topics. In particular, the lowest performance was observed in colorectal tumors (mean = 48.3%, SD = 17.7%) and genitourinary tumors (mean = 50.8%, SD = 15.5%)."

## Discussion


## Related Claims
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — related
- [LLM accuracy varied sharply by histology topic: perfect in foundational areas and lowest in Muscle (76.0%)](histology-topic-difficulty-llm-performance.md) — related
- [Histology topic, not LLM platform, was the primary factor in performance variance (η2 = 0.452 vs 0.006), with a significant system-by-topic interaction](topic-effect-dominates-system-effect-llm-histology.md) — related
- [Question type significantly affects LLM accuracy on Chinese medical licensing exam questions, with Type A basic-knowledge items answered better than Type B and Type C items](question-type-effect-llm-chinese-medical-licensing.md) — related
- [GPT-4o's accuracy on the CONACEM anesthesiology exam varies significantly by cognitive domain, highest in Understanding (90.10%) and lowest in Application (76.83%) and Analysis (76.54%)](gpt4o-conacem-accuracy-varies-by-cognitive-domain.md) — related
- [Overall performance differed significantly among the four LLMs, with a post-hoc ordering of Claude 3.5 Sonnet > ChatGPT 4o > Llama-3 ≈ Gemini 1.5, while passed-exam counts did not differ significantly](significant-llm-performance-differences-oncology-exams-anova.md) — related
- [Claude 3.5 Sonnet outperformed ChatGPT 4o, Llama-3 and Gemini 1.5 on Turkish oncology board examination questions, passing all eight annual exams with an average score of 77.6%](claude-35-sonnet-outperforms-other-llms-oncology-board-exams.md) — related
- [ChatGPT 4o outperformed Llama-3 and Gemini 1.5 across all question categories, with an average score of 67.8 and its highest accuracy in basic oncology (86.4%)](chatgpt-4o-second-tier-oncology-exam-performance.md) — related
