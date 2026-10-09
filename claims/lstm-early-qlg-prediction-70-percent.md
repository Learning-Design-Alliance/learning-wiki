---
type: claim
title: "LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees"
description: "LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees"
id: lstm-early-qlg-prediction-70-percent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: mixed
sources:
  - id: ye-mao-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: ye-mao-2018-2
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LSTM predicts learning gains as well with the earliest 70% of sequences as with the full sequences, while BKT+SK excels at 30% only on Pyrenees

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`

## Subclaims
`q2 i?` Using the earliest 70% of training sequences, LSTM reached QLG prediction performance similar to using the entire sequences on both datasets. [→ Ye Mao 2018](#ye-mao-2018)
`q2 i?` On Pyrenees only, BKT+SK achieved excellent early QLG prediction with the first 30% of sequences (AUC 0.696, F1 0.751), beating LSTM's 0.659 AUC and 0.740 F1 at that point. [→ Ye Mao 2018 (2)](#ye-mao-2018-2)

## Evidence

### Ye Mao 2018

Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318

`q2 · i?` · `associational · r1`

QLG early-prediction curves (Section 5.3.2, Figure 11) on Cordillera: LSTM's AUC rose from 0.576 to 0.689 between 10% and 40% and F1 from 0.688 to 0.720, with only slight changes after 70%.

> "The results suggest that areasonable prediction of QLG can be accomplished by using the ﬁrst 40% of the entire sequences, and that using the earliest 70% of the sequences is as good as using the entire sequences."

### Ye Mao 2018 (2)

Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318

`q2 · i?` · `design · r2`

QLG early-prediction curves on Pyrenees (Section 5.3.2, Figure 12); the article notes "Note that this results only hold for Pyrenees dataset", so the BKT+SK early advantage is dataset-specific.

> "Indeed, BKT+SK (blue dashed line with circle points) exhibits an excellent prediction on QLG with only the ﬁrst 30% of the entire sequences, 0.696 on AUC and 0.751 on F1-measure."

## Discussion


## Related Claims
- [BKT and BKT+SK are the best models for predicting students' post-test scores in tutoring systems with elicit and tell interventions](bkt-best-post-test-prediction-intervention-tutors.md) — related
- [BKT+SK reliably predicts post-test scores using only the earliest 50% of training sequences](bkt-sk-early-posttest-prediction-50-percent.md) — related
- [LSTM and LSTM+SK outperform the Bayesian models on predicting quantized learning gains](lstm-best-learning-gain-prediction.md) — related
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
