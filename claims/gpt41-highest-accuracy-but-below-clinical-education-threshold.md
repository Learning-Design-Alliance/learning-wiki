---
type: claim
title: GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use
description: GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use
id: gpt41-highest-accuracy-but-below-clinical-education-threshold
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: lei-yung-hsu-2025
    resource: "https://doi.org/10.1080/10872981.2025.2602788"
    title: "Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788"
    author: Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On multiple-choice questions GPT-4.1 significantly outperformed both GPT-4o (46 ± 5 vs 36 ± 4) and GPT-4 (46 ± 5 vs 28 ± 6). [→ Lei Yung-Hsu 2025](#lei-yung-hsu-2025)
`q2 i?` None of the tested models achieved accuracy the authors consider sufficient to support clinical education independently. [→ Lei Yung-Hsu 2025](#lei-yung-hsu-2025)

## Evidence

### Lei Yung-Hsu 2025

Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788

`q2 · i?` · `causal · r2`

Phase 1 API evaluation of 466 single-choice and 179 multiple-choice official board questions (2020–2022) across three models with identical procedures; Table 4 reports multiple-choice accuracy of 46 ± 5 (GPT-4.1), 36 ± 4 (GPT-4o), 28 ± 6 (GPT-4), all p < 0.001.

> "GPT-4.1 significantly outperforms both GPT-4o and GPT-4 in accuracy, with all comparisons reaching statistical significance. While GPT-4o remains the fastest, GPT-4.1 offers a substantial accuracy gain at the cost of moderately increased response time."

## Discussion


## Related Claims
- [ChatGPT-5 achieved the highest overall accuracy on ophthalmology board-style questions (92.59%), with no statistically significant differences among the four LLMs](chatgpt-5-highest-overall-accuracy-ophthalmology-board-questions.md) — related
- [Ten large language models achieved mean accuracies of 72–85% on the complete 300-item European Board of Hand Surgery written examination, with seven of ten reaching or exceeding an illustrative 75% pass threshold.](llm-ebhs-exam-accuracy-range-72-85-percent.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy](deepseek-qwen32b-outperform-gpt4o-clinical-cases.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [Across all question types and languages, Doubao-1.5-pro achieved the highest accuracy (92.0% ± 1.3%) and ChatGPT-4o the lowest (82.8% ± 3.7%) among six LLMs benchmarked](doubao-highest-chatgpt4o-lowest-accuracy.md) — related
- [On recall-type questions, all four LLMs outperformed both residents and fellows, with ChatGPT-5 highest at 92.59%](llms-outperform-trainees-recall-type-questions.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Segmenting domain content into moderate token chunks significantly improves GPT-4.1 accuracy on specialised medical board questions compared with no prior content input](token-splitting-improves-gpt41-specialised-exam-accuracy.md) — related
