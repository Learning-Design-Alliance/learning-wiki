---
type: claim
title: Attendance, behavior, and course performance (the ABC indicators) reliably predict which secondary students are at risk of dropping out
description: Attendance, behavior, and course performance (the ABC indicators) reliably predict which secondary students are at risk of dropping out
id: abc-early-warning-indicators-predict-dropout
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
newest_evidence: 2017
source_checked: 2026-10-20
recheck_by: 2020
sources:
  - id: rumberger-2017
    resource: "https://ies.ed.gov/ncee/wwc/PracticeGuide/24"
    title: "Rumberger, R., Addis, H., Allensworth, E., Balfanz, R., Bruch, J., Dillon, E., Duardo, D., Dynarski, M., Furgeson, J., Jayanthi, M., Newman-Gonchar, R., Place, K., & Tuttle, C. (2017). Preventing dropout in secondary schools (NCEE 2017-4028). Washington, DC: National Center for Education Evaluation and Regional Assistance (NCEE), Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee/wwc/PracticeGuide/24"
    author: "Rumberger, R., Addis, H., Allensworth, E., Balfanz, R., Bruch, J., Dillon, E., Duardo, D., Dynarski, M., Furgeson, J., Jayanthi, M., Newman-Gonchar, R., Place, K., & Tuttle, C."
    q: 2
    i: "?"
    kind: review
    rigour: 3
---

# Attendance, behavior, and course performance (the ABC indicators) reliably predict which secondary students are at risk of dropping out

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r3` · `q2`
> **Currency** · newest study 2017 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The three ABC indicators—attendance, behavior, and course performance—have consistently been shown to reliably predict dropout risk, and their impact captures many other risk factors. [→ Rumberger 2017](#rumberger-2017)

## Evidence

### Rumberger 2017

Rumberger, R., Addis, H., Allensworth, E., Balfanz, R., Bruch, J., Dillon, E., Duardo, D., Dynarski, M., Furgeson, J., Jayanthi, M., Newman-Gonchar, R., Place, K., & Tuttle, C. (2017). Preventing dropout in secondary schools (NCEE 2017-4028). Washington, DC: National Center for Education Evaluation and Regional Assistance (NCEE), Institute of Education Sciences, U.S. Department of Education. https://ies.ed.gov/ncee/wwc/PracticeGuide/24

`q2 · i?` · `review · r3`

The expert panel's synthesis statement in Recommendation 1, grounded in the panel's review of research on early warning indicators. The guide states these "ABC indicators have consistently been shown to be reliable predictors" and that other risk factors' impact is often captured through them.

> "Three key indicators—(1) attendance, (2) behavior, and (3) course performance—are reliable predictors of which students are at risk for dropping out."

## Studies bearing on this claim

<!-- synthesis:start -->
*Can models built from attendance, grades and interaction data tell which learners are at risk, early enough to act, and do they hold up in a new term or institution?* This table gathers the studies behind this claim and the 10 narrower claims that bear on it: **8 distinct studies** (4 associational, 3 design, 1 review), `q2`, 1 of 8 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Rumberger 2017 | q2 · review · r3 | i? | this claim |
| [Wei Dai 2025](https://doi.org/10.18608/jla.2025.8735) | q2 · design · r2 | i?; i3 | [Predictive models trained on one semester's offering of a course identified at-risk studen](cross-semester-at-risk-prediction-high-accuracy.md) (supports); [Random-forest models trained on a prior semester showed significantly lower AUC when teste](cross-semester-auc-decline-without-retraining.md) (qualifies) |
| [Alice Xu 2026](https://doi.org/10.18608/jla.2026.9099) | q2 · design · r2 | i? | [Predictive models built in a modelable ecosystem generalize across institutions](cross-institutional-generalizability-coursekata-models.md) (supports); [Behavioral-only metrics from an instrumented online textbook support early prediction of f](behavioral-only-early-prediction-flipped-statistics.md) (supports) |
| Gwynne 2024 | q2 · associational · r2 | i? | [Attendance and online platform participation remained predictive of students' course grade](attendance-predictive-of-grades-remote-learning.md) (supports) |
| Lindsay Cattell 2021 | q2 · associational · r? | i? | [A prior performance early warning system and a machine learning algorithm with same-percen](prior-performance-ews-similarly-accurate-same-percentage-cutoffs.md) (supports) |
| [Alison Cheng 2025](https://doi.org/10.18608/jla.2025.8761) | q2 · design · r2 | i? | [Stage 1 (after the first unit review assignment) is the optimal point for identifying at-r](stage1-optimal-early-at-risk-identification.md) (supports) |
| [Vincent Zhang 2025](https://doi.org/10.1007/s40593-025-00510-9) | q2 · associational · r2 | i? | [The approach offers a large real-time intervention window, with a median of 176.2-196.1 ho](large-prediction-window-real-time-intervention.md) (supports); [Exploratory heat maps reveal three student groups, including disengaged-but-successful stu](interaction-patterns-three-student-groups-heatmaps.md) (qualifies) |
| [Shihao Wang 2026](https://doi.org/10.48550/arxiv.2609.29874) | q2 · associational · r2 | i? | [Secondary outcomes differed in predictability: near-term related-task performance was hard](secondary-outcomes-varied-predictability.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [Low attendance is linked with lower academic skills, grades, and high school graduation, and high attendance with higher ones](attendance-linked-academic-skills-grades-graduation.md) — the general claim this finding bears on, with the studies behind it
- In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled — related
- [Students show signs of dropout risk early in high school, and schools that reach out in the ninth-grade year can keep them on track to graduate](ninth-grade-early-outreach-keeps-students-on-track.md) — related
- [Freshman on-track status is an early indicator correlated with later graduation, and being off track correlates with dropping out](on-track-early-indicator-graduation.md) — related
- [Ninth-grade on-track status predicts graduation more strongly than prior achievement, with a 55 percentage point gap after controls](ontrack-predicts-graduation-beyond-prior-achievement.md) — related
- [Monitoring all students and proactively intervening on early warning signs has minimal-level evidence of improving dropout-related outcomes](proactive-monitoring-minimal-evidence.md) — related
- [Behavior indicators show inconsistent predictive strength for high school graduation: several studies find them strongly predictive, but behavior was not predictive in Chicago above and beyond grades and attendance](behavior-indicators-inconsistent-graduation-prediction.md) — a narrower finding that bears on this claim
- [Strong early-warning monitoring systems paired with strong norms and routines help students recover emotionally and engage academically](early-warning-systems-norms-routines-support-recovery.md) — related
- [Predictive learning analytics can generate early warnings of dropout risk and trigger targeted interventions in adult education](predictive-analytics-early-warning-dropout-adults.md) — related
- [Reviewed studies indicate AI predictive analytics can project student progress, group learners by risk, and enable early intervention](ai-predictive-analytics-early-intervention.md) — related
- [AI-powered predictive analytics improves academic performance by enabling early identification of at-risk students and timely intervention](ai-predictive-analytics-improves-academic-performance.md) — related
- [A prior performance early warning system and a machine learning algorithm with same-percentage risk-score cutoffs are similarly accurate at identifying students who experience academic problems](prior-performance-ews-similarly-accurate-same-percentage-cutoffs.md) — related
- [Attendance and online platform participation remained predictive of students' course grades during remote learning, with relationships as large or larger than pre-pandemic](attendance-predictive-of-grades-remote-learning.md) — related
- [Agent-generated descriptions significantly improve prediction of student dropout in a lesson, outperforming all other measured approaches](agent-descriptions-improve-dropout-prediction.md) — related
- [Using predictive analytics while ignoring teacher knowledge may misidentify students at risk of dropping out and negatively influence teacher views](ignoring-teacher-knowledge-misidentifies-risk-students.md) — related
- [Chicago's graduation-rate improvements have been credited to changed ninth-grade dropout-prevention practices triggered by on-track accountability and real-time data reports, and the review states accountability by itself was not sufficient](ontrack-accountability-realtime-data-graduation-gains.md) — related
- [The article claims schools can improve attendance, test scores, and graduation rates by identifying high-impact metrics and fostering a collaborative culture of improvement](schools-improve-via-high-impact-metrics-and-collaboration.md) — related
- [A substantial share of dropouts show no clear signs of disengagement or major problems in the years before dropping out](forty-percent-dropouts-no-clear-disengagement.md) — related
