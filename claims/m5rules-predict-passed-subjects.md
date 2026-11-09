---
type: claim
title: "An M5Rules rule model predicts the number of passed subjects from device and connection data with about 72% correlation on average"
description: "An M5Rules rule model predicts the number of passed subjects from device and connection data with about 72% correlation on average"
id: m5rules-predict-passed-subjects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-08
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: fernández-soriano-francisco-luis-2019
    resource: "https://doi.org/10.3390/s19143226"
    title: "Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226"
    author: Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena
    q: 2
    i: "?"
  - id: fernández-soriano-francisco-luis-2019-2
    resource: "https://doi.org/10.3390/s19143226"
    title: "Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226"
    author: Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena
    q: 2
    i: "?"
  - id: fernández-soriano-francisco-luis-2019-3
    resource: "https://doi.org/10.3390/s19143226"
    title: "Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226"
    author: Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena
    q: 2
    i: "?"
---

# An M5Rules rule model predicts the number of passed subjects from device and connection data with about 72% correlation on average

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · `q2` quasi-experiment
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The M5Rules rule model was judged robust, giving similar results across five random repetitions. [→ Fernández-Soriano Francisco Luis 2019](#fernandez-soriano-francisco-luis-2019)
`q2 i?` The model predicts passed subjects with an average error of almost 2 subjects and a correlation of 72% on average. [→ Fernández-Soriano Francisco Luis 2019 (2)](#fernandez-soriano-francisco-luis-2019-2)
`q2 i?` The most relevant predictor variables were average and maximum connections per week, educational stage and device type. [→ Fernández-Soriano Francisco Luis 2019 (3)](#fernandez-soriano-francisco-luis-2019-3)

## Evidence

### Fernández-Soriano Francisco Luis 2019

Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226

`q2 · i?`

Predictive modeling experiment with the M5Rules algorithm on the LMS connection dataset, repeated with different random training/test splits; the authors judge the model "robust since after repeating it for 5 times randomly it has given similar results obtaining a low standard deviation".

> "The initial model of rules created using the M5Rules algorithm is robust since after repeating it for 5 times randomly it has given similar results obtaining a low standard deviation."

### Fernández-Soriano Francisco Luis 2019 (2)

Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226

`q2 · i?`

Model fitness was evaluated with RMSE, MAE and correlation coefficient over the repeated runs; the model "obtains an average error of almost 2 subjects when predicting the number of passed subjects" and a correlation "of 72% on average".

> "Although the results can be improved, the model obtains an average error of almost 2 subjects when predicting the number of passed subjects and obtains a correlation between the input attributes and the target attribute of 72% on average."

### Fernández-Soriano Francisco Luis 2019 (3)

Fernández-Soriano Francisco Luis, López Belén, Martínez-España Raquel, Muñoz Andrés, Cantabella Magdalena. (2019). Use of Computing Devices as Sensors to Measure Their Impact on Primary and Secondary Students' Performance. Sensors (Basel, Switzerland). https://doi.org/10.3390/s19143226

`q2 · i?`

Variable-relevance analysis of the rule list, counting variables used in at least 90% of rules: "Average number of connections per week (92.3%), maximum number of connections per week (95.4%), educational stage and type of device (98.1%)".

> "The most relevant variables are (in brackets the percentage of occurrence of each variable regarding the total number of rules): Average number of connections per week (92.3%), maximum number of connections per week (95.4%), educational stage and type of device (98.1%)."

## Discussion


## Related Claims
- [Number of failed subjects differs significantly by connecting device type among LMS-connecting students](device-type-failed-subjects-differences.md) — related
- [Number of passed subjects differs significantly by connecting device type, with Bonferroni-adjusted pairwise differences between smartphones, PCs and tablets](device-type-passed-subjects-differences.md) — related
- [Number of passed subjects differs significantly by the operating system used to connect to the LMS](os-passed-subjects-differences.md) — related
