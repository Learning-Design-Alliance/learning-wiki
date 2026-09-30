---
type: method
id: impact-evidence-comparison
title: Comparing learning intervention effects
description: Check the learner, contrast, intended outcome, instrument and timing before interpreting or comparing a reported effect size.
status: draft
sources:
  - id: kraft-2020
    resource: "https://doi.org/10.3102/0013189X20912798"
    title: "Kraft, M. A. (2020). Interpreting effect sizes of education interventions. Educational Researcher, 49(4), 241–253."
    author: "Kraft, M. A."
  - id: lipsey-et-al-2012
    resource: "https://ies.ed.gov/sites/default/files/migrated/nces_pubs/ncser/pubs/20133000/pdf/20133000.pdf"
    title: "Lipsey, M. W., Puzio, K., Yun, C., Hebert, M. A., Steinka-Fry, K., Cole, M. W., Roberts, M., Anthony, K. S., & Busick, M. D. (2012). Translating the statistical representation of the effects of education interventions into more readily interpretable forms. IES."
    author: "Lipsey, M. W., et al."
---

# Comparing learning intervention effects

> **Design Method** · [All design methods](index.md)

The wiki's `i0`–`i3` codes are legacy Cohen-like bins for a printed statistic. They are not a scale of educational value or a prediction for an individual learner. In particular, an effect below d = .20 is not necessarily negligible for a broad achievement measure. Preserve the estimate, direction and uncertainty alongside its code.

## Comparison record

For each effect, identify the following from the study, or write **unknown**. A pooled mean may combine unlike studies; inspect the underlying effects before assigning shared properties to the mean.

| Dimension | Question |
|---|---|
| Learner state | Who was sampled? What starting capability and relevant characteristics did they have? Were the arms comparable at baseline? |
| Assignment | How were conditions assigned? What attrition, confounding or contamination could alter the contrast? |
| Activity and context | What did the intervention and comparison groups actually do, where, and for how long? |
| Objective and target | What specific capability and observable change were intended? |
| Outcome instrument | What was measured? How close was the instrument to the taught task? Could it detect the target change? Did ceiling, floor or range restriction matter? |
| Effect construction | What statistic, direction, standardization denominator and uncertainty interval were reported? |
| Horizon | When was the outcome measured, and was transfer or persistence assessed? |

Two effects are numerically comparable only to the extent that their learner populations, contrasts, outcomes, measures, denominators and horizons are compatible. Unknown is a finding about the available record, not an assumption that the groups or measures match. A local design forecast additionally needs an observed initial state and an explicit goal criterion for the learner in question.

## Kraft's bounded reference class

[Kraft (2020)](https://doi.org/10.3102/0013189X20912798) proposes empirical bins for causal pre-K–12 intervention studies using standardized achievement outcomes: **small** below .05 SD, **medium** .05 to below .20, and **large** .20 or above. These are distributional reference points for that class, not effect forecasts or universal significance thresholds. The [IES methods guide](https://ies.ed.gov/sites/default/files/migrated/nces_pubs/ncser/pubs/20133000/pdf/20133000.pdf) documents different distributions for broad standardized tests, narrow tests and specialized researcher-developed tests.

`evidence-scales.json` records the legacy and Kraft scales separately. `python3 scripts/impact_benchmarks.py --summary` audits coded source records; `--json` lists their missing context. An optional `sources[].impact_context` object can record one checked effect:

```yaml
impact_context:
  verified_against_source: true
  unit: single-study                 # or homogeneous-synthesis
  population: pre-k-12
  assignment: randomized            # or credible-quasi-experiment
  comparator: usual instruction
  learner_start: baseline score and arm balance as reported
  objective: specified reading capability
  outcome_measure: standardized-achievement
  measure_alignment: broad reading test
  score_range: no reported ceiling or floor analysis
  effect_metric: d                   # d, g or SMD
  effect_value: 0.12
  standardization_denominator: control-group pretest SD
  horizon: end of intervention
  uncertainty: 95% CI as reported
```

This block illustrates field shape only; none of its sample values describes a particular study. `verified_against_source: true` requires the original source and the particular effect to be checked. Missing fields, an unreviewed synthesis, a researcher-designed test, a different outcome, or a negative effect receives **no automatic Kraft tier**. The script does not overwrite the legacy `i` code. A separate versioned migration can follow review of the eligible records.
