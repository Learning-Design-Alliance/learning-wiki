---
type: claim
title: "The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance"
description: "The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance"
id: llm-accuracy-differs-independent-query-dus-prosthodontics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
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

# The four LLMs differ significantly in overall and knowledge-question accuracy on DUS prosthodontics questions under independent querying, driven by DeepSeek's lower performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under independent querying, accuracy on knowledge-based and total questions differed significantly across GPT-5, GPT-4o, DeepSeek, and Gemini 2.5 Pro (p < 0.05), attributable mainly to DeepSeek's lower performance. [→ Erdal Selda Gökçe 2026](#erdal-selda-gokce-2026)

## Evidence

### Erdal Selda Gökçe 2026

Erdal Selda Gökçe, Güdül Aynur Beyza Çavuşculu, Köroğlu Ayşegül. (2026). The effectiveness of large language models in dental specialty questions: a comparative study in the field of prosthodontics. BMC Medical Education. https://doi.org/10.1186/s12909-026-08808-5

`q2 · i?` · `causal · r1`

Benchmark-style testing of 128 DUS prosthodontics questions (106 knowledge, 22 case) from 13 exams, each model queried once per item in fresh sessions. Total accuracy was 86% (GPT-5), 83% (GPT-4o), 66% (DeepSeek), 85% (Gemini 2.5 Pro); "the GPT-5, GPT-4o and Gemini 2.5 Pro models exhibited similar and high success rates" while DeepSeek scored 71% on knowledge items.

> "Using the independent query method, statistically significant differences were observed among the four artificial intelligence models in terms of knowledge-based questions and total questions (p < 0.05)."

## Discussion


## Related Claims
- [Case-based question accuracy does not differ significantly across the four LLMs under either querying method](case-based-accuracy-no-model-difference.md) — related
- [Sequential querying significantly reduces knowledge-question accuracy for GPT-5 (91% to 75%) and GPT-4o (86% to 73%), but not for DeepSeek or Gemini 2.5 Pro](sequential-querying-degrades-gpt-knowledge-accuracy.md) — related
- [The evaluated LLMs show higher accuracy on knowledge-based than case-based DUS questions, indicating a limitation in clinically oriented reasoning](llm-knowledge-beats-case-based-prosthodontics.md) — related
- [Gemini 2.5 Pro achieved the highest case-based accuracy (91%) under sequential querying](gemini-highest-case-accuracy-sequential.md) — related
- [On the CDLE benchmark, DeepSeek-R1, GPT-5 Thinking, Gemini 2.5 Pro, and OpenAI o3 significantly outperform GPT-4o in overall accuracy, with Gemini 2.5 Pro highest at 91.67%](cdle-four-llms-outperform-gpt4o-overall.md) — related
