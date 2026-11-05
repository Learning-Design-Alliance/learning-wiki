---
type: claim
title: GPT-4o significantly lags the other four LLMs on dentistry questions, while in clinical medicine no significant pairwise differences were detected
description: GPT-4o significantly lags the other four LLMs on dentistry questions, while in clinical medicine no significant pairwise differences were detected
id: cdle-dentistry-gpt4o-lags-subjects
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
    kind: causal
    rigour: 2
---

# GPT-4o significantly lags the other four LLMs on dentistry questions, while in clinical medicine no significant pairwise differences were detected

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In dentistry, Gemini 2.5 Pro achieved the highest accuracy at 90.32% and GPT-4o the lowest at 79.35%, with GPT-4o significantly lower than the other four LLMs (p < 0.05); in clinical medicine the omnibus test was significant but post hoc pairwise comparisons were not. [→ Zhang Jiarui 2025](#zhang-jiarui-2025)

## Evidence

### Zhang Jiarui 2025

Zhang Jiarui, Ubuzima Pascal, Huang Gaoyang, Lee En-Hsuan, Wang Yuting, Xu Huifang, Xia Lei, Wu Tingting. (2025). From accuracy to robustness: a comparative study of five advanced large language models on the Chinese dental licensing examination. BMC Oral Health. https://doi.org/10.1186/s12903-025-07540-8

`q3 · i?` · `causal · r2`

Subject-stratified analysis of the 600-question CDLE benchmark (dentistry n = 465, clinical medicine n = 39, among five subjects), compared with chi-square/Fisher's exact tests and Bonferroni post hoc pairwise comparisons. The article reports "The accuracy of GPT-4o was significantly lower than the other four LLMs (p < 0.05)" in dentistry.

> "In dentistry, Gemini 2.5 Pro achieved the highest accuracy at 90.32%, while GPT-4o recorded the lowest at 79.35%. The accuracy of GPT-4o was significantly lower than the other four LLMs (p < 0.05)."

## Discussion


## Related Claims
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — possibly the same claim (merge candidate)
- [Across the ten dentistry sub-disciplines, significant model differences appear only in prosthodontics and oral anatomy, where GPT-4o is lowest](cdle-subdiscipline-prosthodontics-oral-anatomy.md) — a narrower finding that bears on this claim
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
