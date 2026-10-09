---
type: claim
title: LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains
description: LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains
id: lstm-best-learning-gain-prediction
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
    rigour: "?"
---

# LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`

## Subclaims
`q2 i?` On both datasets, the two LSTM-based models outperformed all other models on accuracy, F1-measure and AUC for QLG prediction using entire training sequences. [→ Ye Mao 2018](#ye-mao-2018)

## Evidence

### Ye Mao 2018

Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318

`q2 · i?` · `associational · r?`

QLG prediction results (Section 5.3.1, Table 3) on Cordillera and Pyrenees using entire training sequences; LSTM reached accuracy 0.740 and F1 0.756 on Cordillera, and LSTM+SK accuracy 0.733 and F1 0.765 on Pyrenees, against a majority baseline of 0.544 and 0.562.

> "Table 3(a) shows that two LSTM-based models (row 4, 7) outperformed all other models on every measure except Recall. IBKT achieves the highest recall (0.761), and LSTM achieves the second-best recall (0.739)."

## Discussion


## Related Claims
- [BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions](bkt-best-post-test-prediction-intervention-tutors.md) — reports the opposite
- [BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences](bkt-sk-early-posttest-prediction-50-percent.md) — related
- [LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees](lstm-early-qlg-prediction-70-percent.md) — related
