---
type: claim
title: "Fine-tuned ELECTRA classifies Gibbs cycle phases in reflective sentences, with top-3 predictions reaching up to 98% F1"
description: "Fine-tuned ELECTRA classifies Gibbs cycle phases in reflective sentences, with top-3 predictions reaching up to 98% F1"
id: papagai-electra-gibbs-cycle-top3-f1-098
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: solopova-2023
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuned ELECTRA classifies Gibbs cycle phases in reflective sentences, with top-3 predictions reaching up to 98% F1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A multi-class Gibbs cycle phase classifier built on pre-trained ELECTRA scored 65% F1 macro with one-hot prediction but up to 98% F1 macro and micro when the top 3 predictions were matched to all phases present. [→ Solopova 2023](#solopova-2023)

## Evidence

### Solopova 2023

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Model-development evaluation on annotated reflective sentences: a pre-trained ELECTRA model was trained as a multi-class classifier of Gibbs cycle phases, and the article reports that "the top 3 predictions achieve up to 98% F1 macro and micro" while one-hot matching scored 65% F1 macro.

> "While one-hot matching only managed to score 65% F1 macro, the top 3 predictions achieve up to 98% F1 macro and micro."

## Discussion


## Related Claims
- [The best-scoring prompt-engineered approaches did not match the fine-tuned models on emotion detection and Gibbs cycle tasks](papagai-finetuned-outperforms-gpt3-davinci.md) — possibly the same claim (merge candidate)
- [Fine-tuned RoBERTa detects sentence-level emotions in reflective essays with a micro F1 of 0.70](papagai-roberta-emotion-detection-f1-070.md) — related
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [A fine-tuned BERT model achieves almost perfect agreement with human coders when classifying student self-affirmation essays, matching human-human reliability](fine-tuned-bert-matches-human-coders-self-affirmation-essays.md) — related
- [Only two EduBehaviors configurations reach macro-F1 comparable to the fine-tuned RoBERTa encoder (0.76) trained on expert-labelled TalkMoves data](edubehaviors-underperforms-finetuned-encoder.md) — related
