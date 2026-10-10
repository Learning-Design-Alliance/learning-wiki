---
type: claim
title: On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap
description: On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap
id: rf-xgboost-beat-thresholds-and-llms-on-course-overlap
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: arthur-nijdam-2026
    resource: "https://arxiv.org/abs/2608.05910"
    title: "Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910"
    author: Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: arthur-nijdam-2026-2
    resource: "https://arxiv.org/abs/2608.05910"
    title: "Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910"
    author: Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` In 5-fold cross-validation on the TU/e dataset, Random Forest achieved F1 = 0.74 and XGBoost F1 = 0.73, the best balance of precision and recall among evaluated methods. [→ Arthur Nijdam 2026](#arthur-nijdam-2026)
`q2 i?` Zero-shot LLMs achieved relatively high precision but very low recall, making them too conservative for this application. [→ Arthur Nijdam 2026 (2)](#arthur-nijdam-2026-2)

## Evidence

### Arthur Nijdam 2026

Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910

`q2 · i?` · `design · r2`

5-fold cross-validation on the TU/e CS dataset (60 overlapping and 180 non-overlapping pairs) comparing thresholding, classical ML, and zero-shot LLMs. The article reports "F1 scores of 0.74 and 0.73" for Random Forest and XGBoost, with XGBoost accuracy 0.85 (±0.03).

> "The supervised NLP methods perform best overall. Random Forest and XGBoost provide the best balance between precision and recall, with F1 scores of 0.74 and 0.73, respectively."

### Arthur Nijdam 2026 (2)

Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910

`q2 · i?` · `design · r2`

Cross-validated comparison on the TU/e dataset shows ChatGPT-5.4, ChatGPT-5.4-mini, and DeepSeek-V3 reach high precision (0.69–0.74) but recall of only 0.17–0.30, so the authors judge them "too conservative for our application".

> "The zero-shot LLMs achieve relatively high precision but very low recall, making them too conservative for our application, where missing overlapping courses is more costly than false positives."

## Discussion


## Related Claims
- [CourseGraph's nearest-neighbor course mappings largely align with a program director's judgments on real Erasmus+ decisions, with errors traced to ignored pedagogical differences](coursegraph-mappings-align-with-program-director.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
