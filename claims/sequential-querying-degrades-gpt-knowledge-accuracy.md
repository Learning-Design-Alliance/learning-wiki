---
type: claim
title: "Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro"
description: "Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro"
id: sequential-querying-degrades-gpt-knowledge-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: erdal-selda-gökçe-2026
    resource: "https://doi.org/10.1186/s12909-026-08808-5"
    title: "Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5"
    author: Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Within-model comparison shows a statistically significant drop in knowledge accuracy from independent to sequential querying for GPT-5 (χ²=8.38, p < 0.05) and GPT-4o (χ²=4.85, p < 0.05), while DeepSeek (p = 0.307) and Gemini 2.5 Pro (p = 0.338) show no significant change. [→ Erdal Selda Gökçe 2026](#erdal-selda-gokce-2026)

## Evidence

### Erdal Selda Gökçe 2026

Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5

`q2 · i?` · `causal · r1`

Within-model chi-square comparison of independent versus sequential querying for each LLM on 106 knowledge questions. The GPT-5 within-model test gave χ²=8.38, p < 0.05 and GPT-4o χ²=4.85, p < 0.05; DeepSeek (χ²=1.05, p = 0.307) and Gemini 2.5 Pro (χ²=0.92, p = 0.338) were not significant.

> "Within-model comparisons showed significant drops for knowledge items from Independent to Sequential querying for GPT-5 (91%→75%) and GPT-4o (86%→73%). DeepSeek and Gemini 2.5 Pro showed no significant changes."

## Discussion


## Related Claims
- [Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying](gemini-highest-case-accuracy-sequential.md) — related
- [The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance](llm-accuracy-differs-independent-query-dus-prosthodontics.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
