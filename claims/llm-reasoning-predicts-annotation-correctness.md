---
type: claim
title: "Supervised classifiers can predict whether an LLM's Talk Moves annotation is correct using only the LLM's accompanying reasoning text, with a Random Forest reaching F1 = 0.83"
description: "Supervised classifiers can predict whether an LLM's Talk Moves annotation is correct using only the LLM's accompanying reasoning text, with a Random Forest reaching F1 = 0.83"
id: llm-reasoning-predicts-annotation-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ahtisham-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09832"
    title: "Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)"
    author: Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Supervised classifiers can predict whether an LLM's Talk Moves annotation is correct using only the LLM's accompanying reasoning text, with a Random Forest reaching F1 = 0.83

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A Random Forest classifier trained on TF-IDF features of LLM reasoning predicted label correctness with Precision 0.807, Recall 0.854, and F1 0.830 on a held-out test set, outperforming four other classifiers. [→ Ahtisham 2026](#ahtisham-2026)

## Evidence

### Ahtisham 2026

Ahtisham, B.; Vanacore, K.; Zhou, Z.; Lee, J.; Kizilcec, R. F. (2026). LLM Reasoning Predicts When Models Are Right: Evidence from Coding Classroom Discourse. [doi:10.48550/arXiv.2602.09832](https://doi.org/10.48550/arXiv.2602.09832)

`q2 · i?` · `associational · r2`

Evaluation of five supervised classifiers on the held-out test set (N = 6,110) of LLM reasoning texts, predicting whether the accompanying Talk Moves label matched expert human annotations. The Random Forest achieved the highest F1 (0.830 ± 0.009, accuracy 81.1%), "achieving a Precision of 0.807 and a Recall of 0.854", with F1 scores ranging from 0.79 to 0.83 across models.

> "The Random Forest classifier yielded the top performance, achieving a Precision of 0.807 and a Recall of 0.854."

## Discussion


## Related Claims
- [Reasoning for correct annotations is significantly shorter than for incorrect ones for most Talk Moves constructs, with Relating to Others the sole significant exception where correct reasoning is longer](concise-reasoning-predicts-correct-annotations.md) — related
- [Each Talk Moves construct has a distinct linguistic fingerprint: correctness markers differ by move type (exactness terms for Restating, causal language for Pressing for Reasoning, collective nouns for social moves)](linguistic-fingerprints-of-talk-move-correctness.md) — related
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
- [SGD classifiers on document-term matrices outperformed explicit linguistic-feature filters for removing low-scoring responses](sgd-classifier-filtering-outperformed-linguistic-features.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
