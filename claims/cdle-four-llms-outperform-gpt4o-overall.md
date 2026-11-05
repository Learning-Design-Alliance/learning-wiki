---
type: claim
title: "On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%"
description: "On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%"
id: cdle-four-llms-outperform-gpt4o-overall
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

# On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Overall accuracy differed significantly across the five LLMs (p < 0.001), with Gemini 2.5 Pro highest at 91.67% and GPT-4o lowest at 81.17%; pairwise comparisons showed GPT-4o significantly below the other four, with no significant differences among the other four. [→ Zhang Jiarui 2025](#zhang-jiarui-2025)

## Evidence

### Zhang Jiarui 2025

Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8

`q3 · i?` · `design · r2`

Benchmark of 600 stratified-sampled CDLE multiple-choice questions submitted individually via web interfaces to five LLMs, scored against official answer keys and compared with chi-square tests and Bonferroni-corrected post hoc pairwise comparisons. The article reports "Gemini 2.5 Pro achieved the highest accuracy at 91.67%" and GPT-4o lowest at 81.17%.

> "the overall accuracy differed significantly across the five LLMs (p < 0.001). Gemini 2.5 Pro achieved the highest accuracy at 91.67%, while GPT-4o had the lowest at 81.17%."

## Discussion


## Related Claims
- [GPT-4o significantly lags the other four LLMs on dentistry questions, while in clinical medicine no significant pairwise differences were detected](cdle-dentistry-gpt4o-lags-subjects.md) — possibly the same claim (merge candidate)
- [New-generation LLMs significantly outperform GPT-4o on knowledge-based question types (A1, B1) but not on case-analysis types (A2, A3/A4)](cdle-knowledge-vs-case-analysis-question-types.md) — related
- [Across the ten dentistry sub-disciplines, significant model differences appear only in prosthodontics and oral anatomy, where GPT-4o is lowest](cdle-subdiscipline-prosthodontics-oral-anatomy.md) — related
- [Across all question types and languages, Doubao-1.5-pro achieved the highest accuracy (92.0% ± 1.3%) and ChatGPT-4o the lowest (82.8% ± 3.7%) among six LLMs benchmarked](doubao-highest-chatgpt4o-lowest-accuracy.md) — related
- [Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying](gemini-highest-case-accuracy-sequential.md) — related
- [The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance](llm-accuracy-differs-independent-query-dus-prosthodontics.md) — related
- [Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro](sequential-querying-degrades-gpt-knowledge-accuracy.md) — related
- [Mainstream non-Chinese LLMs performed comparably to DeepSeek-R1 on the Chinese-language CDLE, suggesting prior linguistic-basis disadvantages have been mitigated](cdle-language-bias-mitigated-new-generation.md) — possibly the same claim (merge candidate)
- [GPT-4.1 achieved the highest accuracy among GPT-4.1, GPT-4o and GPT-4 on Taiwan plastic surgery board questions, but no model reached accuracy sufficient for independent clinical education use](gpt41-highest-accuracy-but-below-clinical-education-threshold.md) — related
