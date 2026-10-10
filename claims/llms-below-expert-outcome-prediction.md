---
type: claim
title: Current LLMs fall short of human experts in predicting classroom intervention outcomes
description: Current LLMs fall short of human experts in predicting classroom intervention outcomes
id: llms-below-expert-outcome-prediction
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: michal-štefánik-2026
    resource: "https://arxiv.org/abs/2609.20484"
    title: "Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484"
    author: Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Current LLMs fall short of human experts in predicting classroom intervention outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On 310 Edustories case studies, the best language model (Qwen3-30B) reached 0.580 outcome-prediction accuracy versus 0.642 for the best human expert, with 5 of 6 models below the lower bound of expert assessment. [→ Michal Štefánik 2026](#michal-stefanik-2026)

## Evidence

### Michal Štefánik 2026

Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484

`q2 · i?` · `design · r2`

Evaluation on n=310 Edustories case studies comparing six open-source LLMs' direct outcome prediction against appropriateness ratings from five independent educational experts. The best model achieved "0.580 compared to 0.573–0.587 for the lower-performing experts"; the best expert reached 0.642 and the most common label baseline 0.446.

> "Among all evaluated models, only one model (Qwen-3-30B) reaches performance overlapping with human expert accuracy, achieving 0.580 compared to 0.573–0.587 for the lower-performing experts."

## Discussion


## Related Claims
- [Human experts and LLMs show qualitatively different error patterns in outcome prediction](expert-llm-error-patterns-differ.md) — related
- [Model size is not the primary factor in outcome-prediction performance](model-size-not-primary-outcome-prediction-factor.md) — related
- [Expert annotators show high agreement on intervention appropriateness ratings](expert-annotator-high-agreement.md) — related
- [A research-grounded prompt revision improved scores for 10 of 11 models, with gains of 6.6 to 16.2 percentage points](prompt-revision-improves-tutoring-scores-ten-of-eleven.md) — related
