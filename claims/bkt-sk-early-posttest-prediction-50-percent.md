---
type: claim
title: "BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences"
description: "BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences"
id: bkt-sk-early-posttest-prediction-50-percent
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

# BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` In early prediction, BKT+SK outperformed all other models from 20% to 100% of sequence length on both tutoring systems, and its RMSE stabilized after 50% of the sequences. [→ Ye Mao 2018](#ye-mao-2018)

## Evidence

### Ye Mao 2018

Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318

`q2 · i?` · `associational · r2`

Early-prediction analysis (Section 5.2.2, Figures 9 and 10) varying sequence length; on Cordillera RMSE improved from 0.186 at 10% to 0.149 at 50% with no improvement from 50% to 100%, and a similar plateau (0.158 to 0.159) appeared for Pyrenees.

> "More importantly, for both tutoring systems, BKT+SK can predict post-test scores using only 50% of the sequences as effectively as using the entire sequences."

## Discussion


## Related Claims
- [BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions](bkt-best-post-test-prediction-intervention-tutors.md) — related
- [LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees](lstm-early-qlg-prediction-70-percent.md) — related
- [LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains](lstm-best-learning-gain-prediction.md) — related
