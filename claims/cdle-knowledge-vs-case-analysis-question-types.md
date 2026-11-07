---
type: claim
title: New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)
description: New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)
id: cdle-knowledge-vs-case-analysis-question-types
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhang-jiarui-2025
    resource: "https://doi.org/10.1186/s12903-025-07540-8"
    title: "Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8"
    author: Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` For A1 questions Gemini 2.5 Pro was highest (92.43%) and for B1 GPT-5 Thinking highest (94.19%, vs GPT-4o 73.26%), with GPT-4o significantly worse on both; for case analysis questions (A2 and A3/A4) no significant differences were observed among the five models. [→ Zhang Jiarui 2025](#zhang-jiarui-2025)

## Evidence

### Zhang Jiarui 2025

Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8

`q3 · i?` · `design · r2`

Question-type analysis of the 600-question CDLE benchmark across four types (A1 n = 304, A2 n = 121, A3/A4 n = 89, B1 n = 86), tested with chi-square/Fisher's exact tests and Bonferroni post hoc comparisons. The article reports "The performance of GPT-4o was significantly worse than OpenAI o3, GPT-5 Thinking, and Gemini 2.5 Pro (p < 0.05)" on B1 questions.

> "For B1 questions, GPT-5 Thinking exhibited the highest accuracy (94.19%), while GPT-4o had the lowest (73.26%). The performance of GPT-4o was significantly worse than OpenAI o3, GPT-5 Thinking, and Gemini 2.5 Pro (p < 0.05)."

## Discussion


## Related Claims
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — related
- [On recall-type questions, all four LLMs outperformed both residents and fellows, with ChatGPT-5 highest at 92.59%](llms-outperform-trainees-recall-type-questions.md) — related
- [ChatGPT-5 achieved the highest overall accuracy on ophthalmology board-style questions (92.59%), with no statistically significant differences among the four LLMs](chatgpt-5-highest-overall-accuracy-ophthalmology-board-questions.md) — related
- [Across the ten dentistry sub-disciplines, significant model differences appear only in prosthodontics and oral anatomy, where GPT-4o is lowest](cdle-subdiscipline-prosthodontics-oral-anatomy.md) — a broader claim this one bears on
- [GPT-4o showed the highest accuracy (92.9%) on anatomy MCQs, followed by Claude, Copilot, and Gemini](gpt-4o-highest-anatomy-mcq-accuracy.md) — related
- [GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions](gpt4o-advantage-complex-question-formats.md) — reports the opposite
