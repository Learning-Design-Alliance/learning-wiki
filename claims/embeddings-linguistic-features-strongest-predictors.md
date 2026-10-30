---
type: claim
title: In reviewed studies, word embeddings and linguistic features were the strongest difficulty predictors, with combined features giving the best results (RMSE 22.45 vs ZeroR 23.65)
description: In reviewed studies, word embeddings and linguistic features were the strongest difficulty predictors, with combined features giving the best results (RMSE 22.45 vs ZeroR 23.65)
id: embeddings-linguistic-features-strongest-predictors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: samah-alkhuzaey-2023
    resource: "https://doi.org/10.1007/s40593-023-00362-1"
    title: "Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1"
    author: Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# In reviewed studies, word embeddings and linguistic features were the strongest difficulty predictors, with combined features giving the best results (RMSE 22.45 vs ZeroR 23.65)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The review reports, citing Yaneva et al. (2019, 2020), that an ablation study found embeddings (word2vec and ELMo) and linguistic features were the strongest predictors of difficulty with comparable performance, and all features combined achieved RMSE 22.45 versus ZeroR 23.65. [→ Samah AlKhuzaey 2023](#samah-alkhuzaey-2023)

## Evidence

### Samah AlKhuzaey 2023

Samah AlKhuzaey, Floriana Grasso, Terry R. Payne, Valentina Tamma. (2023). Text-based Question Difficulty Prediction: A Systematic Review of Automatic Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00362-1

`q2 · i?` · `review · r2`

The review reports, citing Yaneva et al. (2019, 2020), a feature-ablation analysis on MCQs in high-stakes medical exams using word2vec and ELMo embeddings pretrained on MEDLINE abstracts, linguistic features from the Stanford NLP parser, and information retrieval features; the combination reported the best results (RMSE = 22.45 compared to ZeroR 23.65).

> "As a result of an ablation study that was carried out to examine the effect of each set of features, they found that embeddings (word2ved and ELMo) and linguistic features were the strongest predictors of difficulty with comparable performance."

## Discussion


## Related Claims
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [Surface readability measures are weak predictors of question difficulty, per reviewed studies](readability-weak-difficulty-predictors.md) — related
