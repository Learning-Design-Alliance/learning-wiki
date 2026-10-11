---
type: claim
title: "A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity"
description: "A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity"
id: small-labeled-data-plateaus-evaluator
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: tahmid-al-hannan-2026
    resource: "https://arxiv.org/abs/2607.10647"
    title: "Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647"
    author: Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A model trained only on the 300-conversation BEA dataset plateaus at 74.84% average macro F1 due to limited data size and diversity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Training on only the 2,480 labeled responses from the BEA 2025 dataset produced a model that plateaued at an average macro F1 of 74.84%. [→ Tahmid Al Hannan 2026](#tahmid-al-hannan-2026)

## Evidence

### Tahmid Al Hannan 2026

Tahmid Al Hannan, Diego Garcia, Alex Njoroge, Suha Al Juboori, Tarek Sakakini. (2026). Knowledge Distillation for Automated AI Tutor Evaluation. https://arxiv.org/abs/2607.10647

`q2 · i?` · `design · r2`

Initial training of FATE on the 300 BEA 2025 student-tutor conversations. The article attributes the plateau at "an average macro F1 score of 74.84%" to the dataset's limited size and diversity, motivating the distillation expansion.

> "Although these conversations contained 2,480 AI tutor (AIT) and human tutor responses, the resulting model plateaued at an average macro F1 score of 74.84%, largely due to the dataset's limited size and diversity."

## Discussion


## Related Claims
- [Knowledge distillation from a frontier LLM substantially improves lightweight AI-tutor evaluation across all four pedagogical dimensions](distillation-improves-ai-tutor-evaluation.md) — related
- [EduBehaviors underperforms the fine-tuned RoBERTa encoder trained on expert-labeled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
- [The framework offers a scalable alternative to manual curation, but the small dataset and label dependence limit current conclusions](scalable-curation-alternative-with-limits.md) — related
