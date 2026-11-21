---
type: claim
title: GPT-4o significantly outperformed GPT-3.5 on every grading measure under all prompt versions for Question 1, and outperformed it across all conditions for Questions 2 and 3
description: GPT-4o significantly outperformed GPT-3.5 on every grading measure under all prompt versions for Question 1, and outperformed it across all conditions for Questions 2 and 3
id: gpt4o-outperforms-gpt35-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhongzhou-chen-and-tong-wan-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010126"
    title: "Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: zhongzhou-chen-and-tong-wan-2025-2
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010126"
    title: "Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o significantly outperformed GPT-3.5 on every grading measure under all prompt versions for Question 1, and outperformed it across all conditions for Questions 2 and 3

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For Question 1, GPT-4o outperformed GPT-3.5 on every measure under all prompt versions. [→ Zhongzhou Chen and Tong Wan 2025](#zhongzhou-chen-and-tong-wan-2025)
`q2 i?` For Questions 2 and 3, GPT-4o also outperformed GPT-35 in all conditions tested and across all metrics. [→ Zhongzhou Chen and Tong Wan 2025 (2)](#zhongzhou-chen-and-tong-wan-2025-2)

## Evidence

### Zhongzhou Chen and Tong Wan 2025

Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)

`q2 · i?` · `causal · r2`

Comparison of gpt-35-turbo and gpt-4o grading the same 96 Question 1 responses across four prompt styles (Simple COT, Detailed COT, Detailed Compare, Forced Compare), with GPT-4o better on SMD, match rate, diff-both, Macro F1 and QWK.

> "GPT-4o model significantly outperformed GPT -3.5 
model on every measure under all prompt versions."

### Zhongzhou Chen and Tong Wan 2025 (2)

Zhongzhou Chen and Tong Wan. (2025). Using Large Language Models to Assign Partial Credit to Students' Explanations of Problem-Solving Process: Grade at Human Level Accuracy with Grading Confidence Index and Personalized Student-facing Feedback. Originally published 2024. [doi:10.1103/physrevphyseducres.21.010126](https://doi.org/10.1103/physrevphyseducres.21.010126)

`q2 · i?` · `design · r2`

Results section for Question 3 (77 responses, 2-D collision momentum problem) reports GPT-4o outperforming GPT-35 across all tested conditions and metrics, consistent with the Question 2 results in Table 5.

> "GPT-4o still outperform ed GPT-35 in all conditions 
tested and across all metrics."

## Discussion


## Related Claims
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — related
- [GPT-4's March and June 2023 versions showed no notable overall difference on the English exams, but differed on individual questions](gpt4-march-june-versions-comparable-overall.md) — related
- [LLM version progression explains about half of the variance in biomedical MCQ accuracy, with GPT‐4o_o1 over six times as likely as GPT‐3/3.5 to answer correctly](llm-version-meta-regression-explains-accuracy-variance.md) — related
- [GPT-4o achieves the highest accuracy on USMLE-style MCQs (90.4%), outperforming GPT-4 (81.1%) and GPT-3.5 (60.0%)](gpt-4o-90-percent-usmle-mcq-accuracy-outperforms-predecessors.md) — related
- [GPT-4o answered image-based USMLE sample items with 89.5% accuracy versus GPT-4's 73.4%, a numerically higher but not statistically significant difference](gpt4o-89-5-percent-image-usmle-accuracy.md) — related
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [Newer Anthropic and DeepSeek models approach GPT‐4o–o1 accuracy on biomedical MCQs, while Google Gemini and Microsoft Copilot trail the leading companies](llm-company-comparison-biomedical-mcq-accuracy.md) — related
- [On USMLE imaging-based questions, GPT-4o and GPT-4 did not differ significantly from each other but both outperformed Google Bard](gpt4o-gpt4-outperform-bard-imaging-questions.md) — related
