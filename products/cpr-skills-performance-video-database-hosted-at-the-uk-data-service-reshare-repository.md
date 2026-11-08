---
type: product
id: cpr-skills-performance-video-database-hosted-at-the-uk-data-service-reshare-repository
title: CPR skills performance video database hosted at the UK Data Service ReShare Repository
description: A UK Data Service ReShare Repository dataset of multi-angle CPR performance videos, expert quality ratings, participant self-reports, and demographics, created by Constable et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
---

# CPR skills performance video database hosted at the UK Data Service ReShare Repository

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (5 for) · 2 studies (1 causal, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
A UK Data Service ReShare Repository dataset of multi-angle CPR performance videos, expert quality ratings, participant self-reports, and demographics, created by Constable et al. for research and learning use.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Seven standardized 12-second CPR video sequences at three artificial quality levels (high 1920x1080, medium 320x240, low 128x96 ppi)**: A stimulus set of seven 12-second high-quality video clips recorded on a standardized CPR training manikin, showing either guideline-conformant compression-only CPR or one of six typical errors: "Low compression rate", "High compression rate", "Increased compression depth", "Superficial compression depth", "Wrong hand position", and "Incomplete thorax release" (Table 1). Resolution was artificially reduced with software to three quality levels, all at 30 fps, and sequences were randomly assigned to evaluators in a randomized, double-blinded evaluation with a standardized multiple-choice questionnaire. (Plata Christopher et al. (2021))

### Claims
- [Two expert raters rating CPR cycles alone reached moderate agreement for Cycles 2-4 but poor agreement for Cycle 1, which the authors attribute to inconsistencies in an initial 'practice' cycle.](../claims/expert-rater-agreement-cpr-performance-cycles.md) [+M]
- [Fusing pose information from multiple camera views makes the model's pose-related ratings more robust than single-view human judgements, which are limited by participant angle and initial posture.](../claims/multiview-fusion-robust-pose-ratings.md) [+W]
- [A multiview pose-estimation deep learning model assesses overall CPR performance quality with mean absolute error comparable to expert human raters, with margins typically below 1 point on a 4-point item scale.](../claims/aqa-stgcn-mae-comparable-to-expert-raters.md) [+W]
- [The automatic CPR assessment system shows lower error than human raters on hand, arm and shoulder position items but higher error on compression depth and rate, which depend on human-object interaction the model does not capture.](../claims/aqa-pose-items-outperform-depth-rate-items.md) [+W]
- [Video quality has no significant impact on correct evaluation of CPR performance in video sequences, with even low quality yielding an acceptable correct-evaluation rate](../claims/video-quality-no-impact-cpr-evaluation.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Constable, M. D., Zhang, F. X., Conner, T., Monk, D., Rajsic, J., Ford, C., Park, L. J., Platt, A., Porteous, D., Grierson, L., & Shum, H. P. H. (2025). Advancing healthcare practice and education via data sharing: demonstrating the utility of open data by training an artificial intelligence model to assess cardiopulmonary resuscitation skills. Advances in Health Sciences Education, 30(1), 15-35. https://doi.org/10.1007/s10459-024-10369-5
- Plata Christopher, Nellessen Martin, Roth Rebecca, Ecker Hannes, Böttiger Bernd W., Löser Johannes, Wetsch Wolfgang A. (2021). Impact of video quality when evaluating video-assisted cardiopulmonary resuscitation: a randomized, controlled simulation trial. BMC Emergency Medicine. https://doi.org/10.1186/s12873-021-00486-4
