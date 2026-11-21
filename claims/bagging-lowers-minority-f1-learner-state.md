---
type: claim
title: Bagging ensembles sometimes achieved lower F1 than a single base bi-LSTM model despite higher accuracy on unbalanced learner-state datasets
description: Bagging ensembles sometimes achieved lower F1 than a single base bi-LSTM model despite higher accuracy on unbalanced learner-state datasets
id: bagging-lowers-minority-f1-learner-state
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: bodonhelyi-2026
    resource: "https://doi.org/10.48550/arXiv.2602.09904"
    title: "Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)"
    author: Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Bagging ensembles sometimes achieved lower F1 than a single base bi-LSTM model despite higher accuracy on unbalanced learner-state datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On highly unbalanced and limited datasets, bagging multiple bi-LSTM models sometimes performed worse than a single base model in F1 score despite achieving higher accuracy. [→ Bodonhelyi 2026](#bodonhelyi-2026)

## Evidence

### Bodonhelyi 2026

Bodonhelyi, A., Wang, M., Bozkir, E., Bühler, B., Kasneci, E. (2026). Safeguarding Privacy: Privacy-Preserving Detection of Mind Wandering and Disengagement Using Federated Learning in Online Education. [doi:10.48550/arXiv.2602.09904](https://doi.org/10.48550/arXiv.2602.09904)

`q2 · i?` · `design · r2`

Benchmark comparing a bagging ensemble of bi-LSTM models (majority vote over user-wise-trained models) with a single bi-LSTM across five datasets: bagging "can sometimes perform worse than a single base model in terms ofF 1 score" "despite achieving higher accuracy".

> "On highly unbalanced and limited datasets with challenging classification tasks, bagging multiple models can sometimes perform worse than a single base model in terms ofF 1 score (Table 3), despite achieving higher accuracy (Table F6)."

## Discussion


## Related Claims
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — possibly the same claim (merge candidate)
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — reports the opposite
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — reports the opposite
- [Each generalised plait ensemble (SVM, KNN, DCT) beats the single classifier, majority-vote and stacking ensemble of the same type in perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%), though the DCT plait does not beat SVM stacking](plait-ensemble-outperforms-single-and-standard-ensembles.md) — reports the opposite
- [An ensemble learner outperforms every individual base learner for predicting final exam score and course grade in a large introductory statistics course](ensemble-outperforms-base-learners-exam-grade.md) — reports the opposite
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [BERT-FYBIO, which uses post text plus annotated reading context, significantly outperforms a Bi-LSTM baseline for emoji prediction](bert-fybio-outperforms-bilstm.md) — related
