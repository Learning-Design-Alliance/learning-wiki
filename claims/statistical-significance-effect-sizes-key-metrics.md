---
type: claim
title: "Improvements over baselines are statistically significant, with Cohen's d ranging from 1.2 to 1.8 for key metrics"
description: "Improvements over baselines are statistically significant, with Cohen's d ranging from 1.2 to 1.8 for key metrics"
id: statistical-significance-effect-sizes-key-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: li-2025
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# Improvements over baselines are statistically significant, with Cohen's d ranging from 1.2 to 1.8 for key metrics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` Paired t-tests on ICS across 30 cross-validation folds yield p-values < 0.01 with Cohen's d from 1.2 to 1.8; the Wilcoxon signed-rank test on ExpScore shows p < 0.001, and results withstand Bonferroni correction. [→ Li 2025](#li-2025)

## Evidence

### Li 2025

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i3` · `design · r2`

Statistical significance testing (§5.4, Table 10) reports ICS p = 0.0032 with "Cohen's d" 1.42, ExpScore p = 0.0008 with d = 1.78, and Review Time p = 0.0041 with d = 1.29, with confidence intervals printed for each metric.

> "Paired t-tests on ICS scores across 30 cross-validation folds yield p-values < 0.01, with effect sizes (Cohen's d) ranging from 1.2 to 1.8 for key metrics. The Wilcoxon signed-rank test on explanation quality (ExpScore) shows even stronger significance (p < 0.001)"

## Discussion


## Related Claims
- [ProfileRL outperforms prompting and fine-tuning baselines on turn-level student simulation, with statistically significant gains on Acts, Correctness, and Errors](profilerl-outperforms-student-simulation-baselines.md) — related
- [Federated improvements over the single-LLM baseline are statistically significant across all three datasets, with Cohen's d from 0.62 to 0.89](statistical-significance-federated-diagnosis-gains.md) — related
- [A within-subjects pilot with 27 professional software engineers found statistically significant self-reported self-efficacy gains across all 10 assessed skill areas after completing the cc-self-train curriculum](cc-self-train-pilot-self-efficacy-gains.md) — related
