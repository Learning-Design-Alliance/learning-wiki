---
type: claim
title: A BERT-based model grades reflective level in English and German essays with a quadratic weighted kappa of 0.71
description: A BERT-based model grades reflective level in English and German essays with a quadratic weighted kappa of 0.71
id: papagai-bert-reflective-level-qwk-071
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
  - id: solopova-2023-2
    resource: "https://doi.org/10.1007/978-3-031-42608-7_16"
    title: "Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)"
    author: Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A BERT-based model grades reflective level in English and German essays with a quadratic weighted kappa of 0.71

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Two annotators labelled 600 texts according to Fleck & Fitzpatrick's scheme under didactics-specialist supervision, achieving moderate inter-annotator agreement of 0.68. [→ Solopova 2023](#solopova-2023)
`q2 i?` A model using pre-trained BERT large and complete document embeddings for English and German reached a QWK score of 0.71 in cross-validation for reflective level detection. [→ Solopova 2023 (2)](#solopova-2023-2)

## Evidence

### Solopova 2023

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Annotation study for the reflective-level detector: the article reports two annotators labelled 600 texts to Fleck & Fitzpatrick's scheme "achieving moderate inter-annotators agreement of 0.68".

> "Under the supervision of Didactics specialists two an- notators labelled 600 texts according to Fleck & Fitzpatrick’s scheme [11], achiev- ing moderate inter-annotators agreement of 0.68."

### Solopova 2023 (2)

Solopova, V., Rostom, E., Cremer, F., Gruszczynski, A., Witte, S., Zhang, C., Ramos López, F., Plößl, L., Hofmann, F., Romeike, R., Gläser-Zikuda, M., Benzmüller, C., Landgraf, T. (2023). PapagAI: Automated Feedback for Reflective Essays. [doi:10.1007/978-3-031-42608-7_16](https://doi.org/10.1007/978-3-031-42608-7_16)

`q2 · i?` · `design · r2`

Model-development evaluation with a 70/30 train-evaluation split: the article reports the BERT-large model with document embeddings achieved "QWK score of 0.71 in cross-validation" for reflective level detection in English and German.

> "With 70% of the data used for the training and 30% for evaluation, we used pre-trained BERT large and complete document embeddings for the English and German, resulting in QWK score of 0.71 in cross-validation."

## Discussion


## Related Claims
- [Fine-tuned BERT outperforms FFNN and LSTM deep learning architectures for classifying segments of written reflections, with weighted F1 average of .82](bert-outperforms-ffnn-lstm-reflective-writing-classification.md) — related
- [NLP models in LA studies typically reach moderate agreement (mean Cohen's kappa 0.54) and mean accuracy 0.79, with deep learning models outperforming others in most studies from 2021 onward](nlp-la-performance-kappa-accuracy-benchmarks.md) — a broader claim this one bears on
- [Machine learning detects five of eight reflective-writing categories with substantial or almost perfect reliability and three with moderate reliability (Cohen's κ .53–.85)](ml-detects-reflection-categories-kappa-053-085.md) — related
