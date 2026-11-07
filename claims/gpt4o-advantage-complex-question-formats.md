---
type: claim
title: "GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions"
description: "GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions"
id: gpt4o-advantage-complex-question-formats
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: luo-dingyuan-2025
    resource: "https://doi.org/10.1038/s41598-025-98949-2"
    title: "Luo Dingyuan, Liu Mengke, Yu Runyuan, Liu Yulian, Jiang Wenjun, Fan Qi, Kuang Naifeng, Gao Qiang, Yin Tao, Zheng Zuncheng. (2025). Evaluating the performance of GPT-3.5, GPT-4, and GPT-4o in the Chinese National Medical Licensing Examination. Scientific Reports 15, 14119. https://doi.org/10.1038/s41598-025-98949-2"
    author: Luo Dingyuan, Liu Mengke, Yu Runyuan, Liu Yulian, Jiang Wenjun, Fan Qi, Kuang Naifeng, Gao Qiang, Yin Tao, Zheng Zuncheng
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o shows a clear advantage in complex question formats, exceeding 85% accuracy on case analysis (A3/A4) and matching (B1) questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` GPT-4o achieved over 80% accuracy across all question types, with case analysis and standard matching questions exceeding 85%. [→ Luo Dingyuan 2025](#luo-dingyuan-2025)
`q3 i?` GPT-4 and GPT-3.5 struggled with complex types: the GPT-4 vs GPT-3.5 difference was not significant for 2020 A3/A4 questions, and GPT-3.5 scored worst on B1 questions (33.8% in 2020, 40% in 2021). [→ Luo Dingyuan 2025](#luo-dingyuan-2025)

## Evidence

### Luo Dingyuan 2025

Luo Dingyuan, Liu Mengke, Yu Runyuan, Liu Yulian, Jiang Wenjun, Fan Qi, Kuang Naifeng, Gao Qiang, Yin Tao, Zheng Zuncheng. (2025). Evaluating the performance of GPT-3.5, GPT-4, and GPT-4o in the Chinese National Medical Licensing Examination. Scientific Reports 15, 14119. https://doi.org/10.1038/s41598-025-98949-2

`q3 · i?` · `design · r2`

Subgroup analysis by question type (A1, A2, A3/A4, B1) across both exam years, tested with chi-square tests and pairwise comparisons. The article reports "GPT-3.5 performed the worst on B1-type questions, with 33.8% and 40% accuracy rates in 2020 and 2021, respectively."

> "However, GPT-4o demonstrated superior performance across all question types, achieving over 80% accuracy, with case analysis and standard matching questions exceeding 85%."

## Discussion


## Related Claims
- [New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)](cdle-knowledge-vs-case-analysis-question-types.md) — reports the opposite
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — reports the opposite
- [Across the ten dentistry sub-disciplines, significant model differences appear only in prosthodontics and oral anatomy, where GPT-4o is lowest](cdle-subdiscipline-prosthodontics-oral-anatomy.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
- [GPT-4o achieves significantly higher overall accuracy than GPT-4 and GPT-3.5 on the 2020 and 2021 Chinese NMLE](gpt4o-highest-accuracy-chinese-nmle.md) — related
