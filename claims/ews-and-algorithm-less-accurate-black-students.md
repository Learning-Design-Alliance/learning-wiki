---
type: claim
title: Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black
description: Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black
id: ews-and-algorithm-less-accurate-black-students
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
newest_evidence: 2021
source_checked: 2026-10-20
recheck_by: 2024
sources:
  - id: lindsay-cattell-2021
    resource: "https://ies.ed.gov/ncee/edlabs"
    title: "Lindsay Cattell, Julie Bruch. (2021). Identifying Students At Risk Using Prior Performance Versus a Machine Learning Algorithm. Regional Educational Laboratory Mid-Atlantic, U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov/ncee/edlabs"
    author: Lindsay Cattell, Julie Bruch
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
---

# Both prior performance flags and the machine learning algorithm are less accurate when predicting outcomes for students who are Black

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r?` · `q2`
> **Currency** · newest study 2021 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Accuracy is lower for students who are Black under both the prior performance flags and the algorithm. [→ Lindsay Cattell 2021](#lindsay-cattell-2021)

## Evidence

### Lindsay Cattell 2021

Lindsay Cattell, Julie Bruch. (2021). Identifying Students At Risk Using Prior Performance Versus a Machine Learning Algorithm. Regional Educational Laboratory Mid-Atlantic, U.S. Department of Education, Institute of Education Sciences. https://ies.ed.gov/ncee/edlabs

`q2 · i?` · `associational · r?`

The report's findings summary states that "Both the prior performance flags and the algorithm are less accurate" for students who are Black, indicating an equity limitation shared by both identification approaches.

> "Both the prior performance flags and the algorithm are less accurate when predicting outcomes for students who are Black."

## Studies bearing on this claim

<!-- synthesis:start -->
*Are at-risk predictions equally accurate for every student group, and do fairness fixes close the gap?* This table gathers the studies behind this claim and the 11 narrower claims that bear on it: **7 distinct studies** (2 associational, 2 causal, 1 review, 1 design, 1 theoretical), `q1`–`q2`, 1 of 7 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Lindsay Cattell 2021 | q2 · associational · r? | i? | this claim |
| Tanner 2025 | q2 · associational · r2 | i? | [At-risk identification is demographically patterned, with Black, Hispanic, and male studen](at-risk-identification-demographic-patterns.md) (supports) |
| [Theodora 2026](https://doi.org/10.48550/arxiv.2605.16296) | q2 · review · r? | i? | [Algorithmic bias and data privacy are central ethical risks of AI in adult education](algorithmic-bias-privacy-risks-adult-education.md) (supports) |
| [McConvey 2026](https://doi.org/10.48550/arxiv.2609.38552) | q1 / q2 · causal · r? | i? | [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities acros](six-posthoc-interventions-redistribute-disparities.md) (supports); [When demographic groups have different base rates, no method can satisfy calibration, equa](impossibility-fairness-metrics-base-rates.md) (qualifies) |
| [Alison Cheng 2025](https://doi.org/10.18608/jla.2025.8761) | q2 · design · r2 | i?; i3 | [Incorporating more learning activity data reduced the potential bias caused by overrelianc](learning-activity-data-reduces-demographic-bias.md) (qualifies); [Post-processing mitigation with ThresholdOptimizer reduced bias on most fairness metrics w](thresholdoptimizer-reduces-bias-accuracy-tradeoff.md) (qualifies); [Balancing the dataset significantly improved model predictive performance but increased bi](data-balancing-improves-accuracy-increases-bias.md) (qualifies); [Removing the sensitive race feature caused little impact on predictive performance at Stag](removing-race-feature-little-performance-impact.md) (qualifies) |
| [Raymond A. Opoku 2025](https://doi.org/10.18608/jla.2025.8543) | q2 · causal · r2 | i? | [Preprocessing bias mitigation (DIR, RW, SUP) reduced subgroup disparities in TPR on OULAD,](preprocessing-mitigation-reduces-disparities-oulad.md) (qualifies) |
| [Baker 2023](https://doi.org/10.35542/osf.io/y4wvj) | q1 · theoretical · r3 | i? | [Evidence is mixed on whether including demographic variables as predictors improves model ](mixed-evidence-demographic-predictor-performance.md) (qualifies); [Including demographic variables as predictors can reduce actionability by de-emphasizing c](demographic-predictors-reduce-actionability.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [A prior performance early warning system and a machine learning algorithm with same-percentage risk-score cutoffs are similarly accurate at identifying students who experience academic problems](prior-performance-ews-similarly-accurate-same-percentage-cutoffs.md) — related
- [A machine learning algorithm with 10-percent risk-score cutoffs better targets students most likely to experience academic problems and has the advantage in predicting suspensions](algorithm-ten-percent-cutoffs-targets-highest-risk.md) — related
- [Prediction algorithms forecast student achievement from small windows of data, more accurately when data are enriched with instructional design and learning-process detail](enriched-data-improve-achievement-prediction.md) — related
- Predicting student outcomes was a common AIEd use in higher education, with ten studies predicting academic performance — related
- [The review reports AI curriculum-design tools identify learning gaps and equity-analysis tools examine differential policy impacts on student populations](ai-teaching-enhancement-and-equity-analysis-reported.md) — related
- [Post-hoc fairness interventions on a vendor-controlled EWS redistributed disparities across demographic groups without consistently reducing them](six-posthoc-interventions-redistribute-disparities.md) — related
- [When demographic groups have different base rates, no method can satisfy calibration, equalized odds, and statistical parity simultaneously](impossibility-fairness-metrics-base-rates.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — related
