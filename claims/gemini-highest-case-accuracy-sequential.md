---
type: claim
title: "Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying"
description: "Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying"
id: gemini-highest-case-accuracy-sequential
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
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

# Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under sequential querying, Gemini 2.5 Pro attained the highest case-based accuracy of the four models (91%, 20/22), though between-model case differences were not statistically significant. [→ Erdal Selda Gökçe 2026](#erdal-selda-gokce-2026)

## Evidence

### Erdal Selda Gökçe 2026

Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5

`q2 · i?` · `causal · r1`

Descriptive result from the sequential-query phase of the benchmark; Table 1 reports Gemini 2.5 Pro at 91% (20/22) on case questions versus 77% (GPT-5), 68% (GPT-4o), and 64% (DeepSeek). The omnibus test was not significant (p = 0.165), so the ranking is descriptive only.

> "Notably, Gemini 2.5 Pro yielded the highest performance in case-based questions (91%) with sequential query."

## Discussion


## Related Claims
- [Case-based question accuracy does not differ significantly across the four LLMs under either querying method](case-based-accuracy-no-model-difference.md) — related
- [Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro](sequential-querying-degrades-gpt-knowledge-accuracy.md) — related
- [The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance](llm-accuracy-differs-independent-query-dus-prosthodontics.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
