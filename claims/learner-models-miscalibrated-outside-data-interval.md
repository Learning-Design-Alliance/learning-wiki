---
type: claim
title: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
description: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
id: learner-models-miscalibrated-outside-data-interval
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: theophile-gervet-2020
    resource: "https://doi.org/10.5281/zenodo.4143614"
    title: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614) Code: https://github.com/theophilee/learner-performance-prediction"
    author: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: theophile-gervet-2020-2
    resource: "https://doi.org/10.5281/zenodo.4143614"
    title: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614) Code: https://github.com/theophilee/learner-performance-prediction"
    author: "Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On assistments09, both Best-LR and DKT severely overestimate learners when the probability of correct answer is low and underestimate when it is high. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` In general, models are calibrated only in the interval containing most of the data; on large datasets like squirrel both models are close to perfectly calibrated. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614) Code: https://github.com/theophilee/learner-performance-prediction

`q2 · i? · the article prints no effect size for this finding` · `design · r2`

Calibration analysis (Figure 9) of Best-LR and DKT binned by item-wise observed frequency of correctness. "both models severely overestimate learners when the probability of correct answer is low"; no standard technique can correct these biases.

> "on the assistments09 dataset, both models severely overestimate learners when the probability of correct answer is low, and underestimate learners when the probability of correct answer is high"

### Theophile Gervet 2020 (2)

Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *Journal of Educational Data Mining, 12*(3), 31–54. [doi:10.5281/zenodo.4143614](https://doi.org/10.5281/zenodo.4143614) Code: https://github.com/theophilee/learner-performance-prediction

`q2 · i? · the article prints no effect size for this finding` · `associational · r2`

Section 8 calibration analysis with reliability diagrams binned by predicted and observed probabilities; calibration plots binned by predicted probabilities revealed no biases, while observed-probability bins revealed systematic ones.

> "In general, models are calibrated only in the interval containing most of the data."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can the system's diagnosis of the learner be trusted?* This table gathers the studies behind this claim and the 5 narrower claims that bear on it: **6 distinct studies** (4 design, 1 review, 1 causal), `q2`–`q3`, 1 of 6 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Theophile Gervet 2020](https://doi.org/10.5281/zenodo.4143614) | q2 · design · r2 | i? | this claim |
| [Kirk Vanacore 2026](https://doi.org/10.48550/arxiv.2602.19303) | q2 · review · r2 | i? | [Emerging evidence indicates generative AI tutors currently struggle to accurately infer st](genai-tutors-struggle-infer-student-knowledge.md) (supports) |
| [Jaewook Kim 2026](https://doi.org/10.48550/arxiv.2605.04727) | q2 · causal · r2 | i? | [Failing to sort student attempt sequences by ServerTimestamp violates temporal causality a](pkt-temporal-causality-violation-inflates-performance.md) (supports) |
| [Lu 2024](https://doi.org/10.31219/osf.io/3k7z2) | q3 · design · r2 | i2 | [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an ](transformer-kt-first-place-edm-cup-2023.md) (qualifies) |
| [Hooshyar 2026](https://doi.org/10.48550/arxiv.2604.08263) | q2 · design · r2 | i? | [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower ](responsible-dkt-temporal-reliability.md) (qualifies) |
| [Peilin Zhan 2026](https://doi.org/10.48550/arxiv.2605.05958) | q2 · design · r2 | i? | [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains pla](tsdr-improves-calibration-acc-rmse.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

<!-- deprecated 2026-11-05 (the study now carries its DataCite DOI, 10.5281/zenodo.4143614, verified by title, authors and year):
> **Evidence quality** · No study behind this claim is a peer-reviewed article with a DOI: it rests on a source with no registered publication record (a web page, book or unpublished report). It is kept because a design page cites it; treat it as a lead to check, not an established finding.
-->


## Related Claims
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — the same study
- [Expert-designed knowledge-component models add little to the accuracy of logistic-regression learner models on most tutoring datasets](expert-kc-models-add-little-to-performance-prediction.md) — the same study
- Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind — related
- DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression — related
- DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting — related
- [Experts identified pervasive limitations of today's AI for learning, including biased data, inequity, non-graceful failure, and weak context grasp](expert-panel-ai-limitations-list.md) — related
- [A structured mixture-of-experts candidate improved some corrections on fixed-evidence cases but introduced new factual and continuity regressions, so activation was held](moe-candidate-mixed-fidelity-result.md) — related
- [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower early- and mid-sequence errors and the lowest prediction inconsistency rates across sequence lengths](responsible-dkt-temporal-reliability.md) — related
- [Emerging evidence indicates generative AI tutors currently struggle to accurately infer student knowledge at the outset of an interaction or as the activity progresses](genai-tutors-struggle-infer-student-knowledge.md) — related
- [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau](tsdr-improves-calibration-acc-rmse.md) — related
- [In open-ended constructivist activities, task success or failure is not a reliable indicator of learning, so learner models based only on performance risk misjudging learners](performance-not-indicator-learning-open-ended.md) — related
- [DKT+ regularization addresses two DKT deficits: failure to reconstruct observed interactions and inconsistent knowledge-state transitions across time steps.](dkt-plus-regularization-addresses-reconstruction-and-transition-consistency.md) — related
