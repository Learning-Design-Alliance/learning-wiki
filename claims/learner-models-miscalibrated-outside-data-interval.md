---
type: claim
title: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
description: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
id: learner-models-miscalibrated-outside-data-interval
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: theophile-gervet-2020
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: theophile-gervet-2020-2
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` On assistments09, both Best-LR and DKT severely overestimate learners when the probability of correct answer is low and underestimate when it is high. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` In general, models are calibrated only in the interval containing most of the data; on large datasets like squirrel both models are close to perfectly calibrated. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i? · the article prints no effect size for this finding` · `design · r2`

Calibration analysis (Figure 9) of Best-LR and DKT binned by item-wise observed frequency of correctness. "both models severely overestimate learners when the probability of correct answer is low"; no standard technique can correct these biases.

> "on the assistments09 dataset, both models severely overestimate learners when the probability of correct answer is low, and underestimate learners when the probability of correct answer is high"

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i? · the article prints no effect size for this finding` · `associational · r2`

Section 8 calibration analysis with reliability diagrams binned by predicted and observed probabilities; calibration plots binned by predicted probabilities revealed no biases, while observed-probability bins revealed systematic ones.

> "In general, models are calibrated only in the interval containing most of the data."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can the system's diagnosis of the learner be trusted?* This table gathers the studies behind this claim and the 6 narrower claims that bear on it: **7 distinct studies** (4 design, 2 causal, 1 review), `q2`–`q3`, 1 of 7 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Theophile Gervet 2020 | q2 · design · r2 | i? | this claim |
| Kirk Vanacore 2026 | q2 · review · r2 | i? | [Emerging evidence indicates generative AI tutors currently struggle to accurately infer st](genai-tutors-struggle-infer-student-knowledge.md) (supports) |
| Jaewook Kim 2026 | q2 · causal · r2 | i? | [Failing to sort student attempt sequences by ServerTimestamp violates temporal causality a](pkt-temporal-causality-violation-inflates-performance.md) (supports) |
| Lu 2024 | q3 · design · r2 | i2 | [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an ](transformer-kt-first-place-edm-cup-2023.md) (qualifies) |
| Liangbei Xu and Mark A. Davenport 2020 | q2 · causal · r2 | i? | [Replacing concept/skill tags with question identifiers significantly degrades DKT and DKVM](dynemb-tracks-knowledge-without-skill-tags.md) (qualifies) |
| Hooshyar 2026 | q2 · design · r2 | i? | [Symbolic knowledge injection improves temporal reliability of predictions, yielding lower ](responsible-dkt-temporal-reliability.md) (qualifies) |
| Peilin Zhan 2026 | q2 · design · r2 | i? | [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains pla](tsdr-improves-calibration-acc-rmse.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Logistic regression with the best feature vector outperforms all other approaches on 4 of 9 datasets while DKT leads on the remaining 5, and Markov process methods lag behind](best-lr-and-dkt-lead-markov-methods-lag-nine-datasets.md) — related
- [DKT fails to retain long-term information on datasets with thousands of interactions per learner, but reaches peak performance on a new student faster than logistic regression](dkt-long-term-information-and-faster-burn-in.md) — related
- [DynEmb outperforms BMF and DKT baselines in future response prediction across five tutoring datasets, with AUC improvement up to 5.43% in the New User setting](dynemb-outperforms-dkt-and-bmf-baselines.md) — related
- [Experts identified pervasive limitations of today's AI for learning, including biased data, inequity, non-graceful failure, and weak context grasp](expert-panel-ai-limitations-list.md) — related
- [A structured mixture-of-experts candidate improved some corrections on fixed-evidence cases but introduced new factual and continuity regressions, so activation was held](moe-candidate-mixed-fidelity-result.md) — related
