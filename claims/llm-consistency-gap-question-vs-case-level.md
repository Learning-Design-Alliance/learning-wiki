---
type: claim
title: "LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%"
description: "LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%"
id: llm-consistency-gap-question-vs-case-level
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-04
recheck_by: 2029
sources:
  - id: cha-j-2026
    resource: "https://doi.org/10.2196/95342"
    title: "Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342"
    author: Cha J, Zhao Y, Zong H.
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# LLMs with high question-level accuracy on medical licensing exam cases show substantially lower case-level accuracy, with consistency gaps of 10% to 17.9%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2026 · checked against its sources 2026-11-04 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` All four evaluated LLMs achieved question pass rates above 83%, but case pass rates were lower for all models, producing consistency gaps ranging from 10% (DeepSeek-R1) to 17.9% (GPT-4o). [→ Cha J 2026](#cha-j-2026)

## Evidence

### Cha J 2026

Cha J, Zhao Y, Zong H. (2026). Large Language Model Performance on Multistep Clinical Cases: Comparative Study Across Question and Case Levels. JMIR Medical Education. https://doi.org/10.2196/95342

`q3 · i?` · `design · r2`

Benchmark evaluation of four LLMs on 189 CNMLE clinical cases (473 questions), each question submitted independently in separate conversations. All models exceeded 83% QPR, but case pass rates were lower, with consistency gaps of 10% for DeepSeek-R1 and 17.9% for GPT-4o, the largest decline.

> "All 4 LLMs achieved QPR above 83% (Figure 1). DeepSeek-R1 showed the highest QPR at 89.9% (425/473), closely followed by Qwen2.5-32B at 89.6% (424/473)"

## Discussion


## Related Claims
- [The consistency gap increases with case complexity, though the 4-question subgroup contained only 7 cases](case-complexity-increases-consistency-gap.md) — possibly the same claim (merge candidate)
- [DeepSeek-R1 and Qwen2.5-32B significantly outperformed GPT-4o on both question-level and case-level accuracy](deepseek-qwen32b-outperform-gpt4o-clinical-cases.md) — related
- [GPT-4 achieves passing accuracy on USMLE Steps 1–3 (mean 86%), significantly exceeding GPT-3.5 (mean 56%)](gpt4-usme-passing-accuracy-exceeds-gpt35.md) — related
- [ChatGPT-4.0 outperforms ChatGPT-3.5 in medical licensing exams, achieving a pooled accuracy of 81.8% versus 60.8%](chatgpt-4-pooled-accuracy-818-percent-licensing-exams.md) — related
- [GPT-4 passed medical licensing examinations in 26 of 29 cases and outperformed average medical students in 13 of 17 cases, while GPT-3.5 passed in only 10 of 26 and surpassed students in 4 of 14](gpt4-pass-and-student-comparison-rates.md) — related
- [LLMs, particularly GPT-4, can match or exceed medical students' examination performance](llms-match-or-exceed-medical-students-exam-performance.md) — related
- [GPT-4 achieves a pooled MCQ accuracy of 81% on medical licensing examinations, significantly surpassing GPT-3.5's 58%](gpt4-81-percent-pooled-accuracy-surpasses-gpt35.md) — related
- [Scaling Qwen2.5 from 3B to 32B parameters improved both metrics and reduced the consistency gap by approximately 50%](model-scaling-reduces-consistency-gap.md) — related
- [Observed case pass rates closely align with expected case pass rates computed under question independence](observed-cpr-matches-expected-independence-benchmark.md) — related
- [The authors argue complex integrative medical questions are particularly useful for evaluating and comparing the reasoning abilities of different LLMs](complex-questions-evaluate-llm-reasoning.md) — related
