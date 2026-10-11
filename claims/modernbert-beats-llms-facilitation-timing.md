---
type: claim
title: ModernBert classifiers are more consistent than out-of-the-box LLMs at facilitation timing prediction, outperforming them in three of five datasets
description: ModernBert classifiers are more consistent than out-of-the-box LLMs at facilitation timing prediction, outperforming them in three of five datasets
id: modernbert-beats-llms-facilitation-timing
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dimitris-tsirmpas-2026
    resource: "https://arxiv.org/abs/2607.28643"
    title: "Dimitris Tsirmpas, Katerina Korre, John Pavlopoulos. (2026). To Facilitate or not to Facilitate: Human and LLM Facilitator Tendencies in Online Discussions. https://arxiv.org/abs/2607.28643"
    author: Dimitris Tsirmpas, Katerina Korre, John Pavlopoulos
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ModernBert classifiers are more consistent than out-of-the-box LLMs at facilitation timing prediction, outperforming them in three of five datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Trained ModernBert encoder classifiers outperform out-of-the-box LLMs with generic prompting in three out of five datasets and achieve the highest F1p across all datasets. [→ Dimitris Tsirmpas 2026](#dimitris-tsirmpas-2026)

## Evidence

### Dimitris Tsirmpas 2026

Dimitris Tsirmpas, Katerina Korre, John Pavlopoulos. (2026). To Facilitate or not to Facilitate: Human and LLM Facilitator Tendencies in Online Discussions. https://arxiv.org/abs/2607.28643

`q2 · i?` · `design · r2`

Comparison of a trained ModernBert classifier against six open-source LLMs on facilitator intervention prediction over PEFK (Table 4), using a 60–20–20 split and 2,000 sampled test instances for LLM evaluation. ModernBert was "outperforming them in three out of the five datasets."

> "the ModernBert classifiers can generally compete with LLMs in this task, and seem much more consistent, outperforming them in three out of the five datasets, and scoring the highestF1 p scores across all datasets."

## Discussion


## Related Claims
- [Defining facilitation as speech produced by facilitators imposes a low performance ceiling on predictive facilitative models](facilitator-speech-definition-performance-ceiling.md) — related
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
