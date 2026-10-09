---
type: claim
title: "BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions"
description: "BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions"
id: bkt-best-post-test-prediction-intervention-tutors
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: ye-mao-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Across two ITS datasets, conventional BKT outperformed IBKT and LSTM, and BKT+SK outperformed IBKT+SK and LSTM+SK, on 5-fold cross-validation RMSE for post-test score prediction. [→ Ye Mao 2018](#ye-mao-2018)

## Evidence

### Ye Mao 2018

Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318

`q2 · i?` · `associational · r2`

Model-comparison results (Section 5.2.1) evaluating six models on two ITS datasets with 5-fold cross-validation RMSE; Table 2 prints best RMSE of 0.147 for BKT on Cordillera and 0.159 for BKT+SK on Pyrenees. The authors state "BKT and BKT+SK are the two best models for both datasets".

> "Among the three basic models (row 1, 2, 3), conventional BKT outperformed both IBKT and LSTM across two datasets. The same pattern was found when incorporating automatic skill discovery into the three models (row 4, 5, 6): BKT+SK generated lower RMSE than IBKT+SK and LSTM+SK."

## Discussion


## Related Claims
- [LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains](lstm-best-learning-gain-prediction.md) — reports the opposite
- [LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees](lstm-early-qlg-prediction-70-percent.md) — related
- [BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences](bkt-sk-early-posttest-prediction-50-percent.md) — related
- [On seven of eight real-world datasets, the novel BKT extensions achieve prediction performance within 0.04 AUC-ROC points of state-of-the-art models](bkt-extensions-close-to-state-of-art-auc.md) — related
- [BKT with generalizable multidimensional student and problem effects matches DKT on some real-world datasets, and multidimensional abilities improve upon unidimensional ones on some datasets](bkt-irt-matches-dkt-some-datasets.md) — related
