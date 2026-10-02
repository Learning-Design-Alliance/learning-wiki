---
type: element
id: trim-and-fill-publication-bias-procedure
title: Trim-and-fill publication-bias analysis procedure applied to learning-effectiveness meta-analysis
description: "The article applies the trim and fill method (Duval & Tweedie) as its publication-bias analysis procedure within a five-step meta-analysis pipeline: effect size calculation, heterogeneity testing, summary effect calcu..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-02
sources:
  - id: ridwan-2021
    resource: "https://doi.org/10.46328/ijres.2287"
    title: "Ridwan, M. R., Retnawati, H., Hadi, S., & Jailani (2021). The effectiveness of innovative learning on mathematical problem-solving ability: A meta-analysis. International Journal of Research in Education and Science (IJRES), 7(3), 910-932. https://doi.org/10.46328/ijres.2287"
    author: "Ridwan, M. R., Retnawati, H., Hadi, S., & Jailani"
---

# Trim-and-fill publication-bias analysis procedure applied to learning-effectiveness meta-analysis

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies (2 quant-synthesis), `q2`–`q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The article applies the trim and fill method (Duval & Tweedie) as its publication-bias analysis procedure within a five-step meta-analysis pipeline: effect size calculation, heterogeneity testing, summary effect calculation, forest-plot analysis, and funnel-plot bias analysis. The article describes the mechanism: "The trim and fill method uses an iterative procedure to eliminate the most extreme small studies from the funnel plot's positive side and recalculate each iteration's effect size until the funnel plot becomes symmetrical." Symmetry of the funnel plot indicates no publication bias; asymmetry would indicate bias. The procedure was implemented with JASP software for the forest plot and R software for the summary effect.

## Design Implications

### Context
#### Requirements
- Effect size and standard error for each research data based on a random-effects model
- Funnel-plot identification of extreme small studies on the positive side
#### Constraints
- The article states the limitation that grouped research came from published journal results without attention to publication status

### Target Learners
- junior high school students

### Target Learning Goals
- mathematical problem-solving ability

## Claims

- [Trim-and-fill analysis shows no publication bias in the meta-analysis of innovative learning effects on mathematical problem-solving ability](../claims/trim-fill-no-publication-bias-innovative-learning.md) [+W]
- [Funnel plot and Egger's test indicate publication bias in the PBL tutor-background data, and trim-and-fill suggests the overall effect is overestimated](../claims/publication-bias-pbl-tutor-meta-analysis.md) [-W]

## Related Elements

- [Coded dataset of 31 studies comparing innovative and conventional learning on junior high school mathematics problem-solving ability](dataset-31-studies-innovative-learning-problem-solving.md)

## Examples

- [Follow transparent, replicable meta-analysis practices tailored to PBL: multiple databases, gray literature, full heterogeneity reporting, funnel plots with Egger's test, and RVE for dependent outcomes](../strategies/pbl-meta-analysis-best-practices.md)

## Key Sources
- Ridwan, M. R., Retnawati, H., Hadi, S., & Jailani (2021). The effectiveness of innovative learning on mathematical problem-solving ability: A meta-analysis. International Journal of Research in Education and Science (IJRES), 7(3), 910-932. https://doi.org/10.46328/ijres.2287
