---
type: claim
title: Confounding may explain the large retention effects reported for the Course Signals early warning system
description: Confounding may explain the large retention effects reported for the Course Signals early warning system
id: course-signals-confounding-number-of-classes
aliases: [course-signals-selection-effect-caution]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
newest_evidence: 2026
source_checked: 2026-10-18
sources:
  - id: weidlich-2022
    resource: "https://doi.org/10.18608/jla.2022.7577"
    title: "Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577"
    author: Weidlich, J., Gašević, D., Drachsler, H.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: kaushik-dutta-2026
    resource: "https://doi.org/10.48550/arxiv.2608.06322"
    title: "Kaushik Dutta. (2026). From Precision Medicine to Precision Education: A Vision for AI-Powered Student Digital Twins, Preventive Student Success, and Career-Aligned Academic Pathways. arXiv preprint. https://arxiv.org/abs/2608.06322 [doi:10.48550/arxiv.2608.06322](https://doi.org/10.48550/arxiv.2608.06322)"
    author: Kaushik Dutta
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Confounding may explain the large retention effects reported for the Course Signals early warning system

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 theoretical `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-18 (automated, 2 of 2 entries) · not reviewed by a person

## Subclaims

`q2 i?` The reported retention advantage for Course Signals students is potentially confounded by the number of classes taken, leaving the causal effect unidentified via an open back-door path. [→ Weidlich 2022](#weidlich-2022)

`q2 i?` Purdue's Course Signals reported gains in help-seeking, lower D and F rates, and improved retention, but critics argued some retention gains reflected a selection effect rather than a treatment effect. [→ Kaushik Dutta 2026](#kaushik-dutta-2026)

## Evidence

### Weidlich 2022

Weidlich, J., Gašević, D., Drachsler, H. (2022). Causal Inference and Bias in Learning Analytics: A Primer on Pitfalls Using Directed Acyclic Graphs. Journal of Learning Analytics, 9(3), 183–199. https://doi.org/10.18608/jla.2022.7577

`q2 · i?` · `theoretical · r3`

The article's re-analysis of the observational Course Signals evaluation by Arnold & Pistilli (2012) reports the printed retention comparison of 93.24% versus 69.4%. It argues the effect is "unidentified due to the open back-door path" through number of classes taken, which affects both treatment encounter and retention.

> "the retention rate was more than 20% higher for 4th-year students who had encountered Course Signals in two or more of their classes (93.24%) than those who had not encountered the system at all (69.4%)"

### Kaushik Dutta 2026

Kaushik Dutta. (2026). From Precision Medicine to Precision Education: A Vision for AI-Powered Student Digital Twins, Preventive Student Success, and Career-Aligned Academic Pathways. arXiv preprint. https://arxiv.org/abs/2608.06322 [doi:10.48550/arxiv.2608.06322](https://doi.org/10.48550/arxiv.2608.06322)

`q2 · i?` · `theoretical · r2`

The paper's review of the Course Signals deployment, piloted at Purdue in 2007, reports institution-claimed outcomes and their later methodological challenge. Critics argued students who took more Course Signals courses were, by construction, students who persisted longer — "a selection effect rather than a treatment effect." No effect sizes are printed.

> "Purdue reported gains in help-seeking, lower D and F rates, and improved retention. These reported outcomes were later questioned on methodological grounds."

## Discussion



## Related Claims

- [AI-powered predictive analytics improves academic performance by enabling early identification of at-risk students and timely intervention](ai-predictive-analytics-improves-academic-performance.md) — the general claim this finding bears on, with the studies behind it
- Most non-STAR studies could not be used in the synthesis because of high risk of bias, chiefly confounding — related
- Propensity score stratification using multilevel models reduces selection bias from confounding variables and improves accuracy of charter school effect estimations — related
- Randomized experiments de-confound by deleting back-door paths, but imperfect compliance can reintroduce confounding — related
- [Written examination scores were low and confounded, providing a serious warning about students' unaided performance on foundational calculations](kt1-exam-low-unaided-performance-warning.md) — related
- Conventional regression models cannot consistently estimate effects of time-varying treatments when time-varying confounders are affected by past treatment — related
- [In an AI-based early warning system, the predictive importance of CAM dimensions shifted over an instructional unit, with affect/metacognition self-reports leading early and cognitive artifacts gaining accuracy toward the end](early-warning-system-cam-predictive-importance-shifts-over-unit.md) — related
- [Prior cross-sectional between-group research on the platform found a positive usage–test-score relationship but could not rule out unobserved confounding](prior-cross-sectional-platform-usage-achievement-link.md) — related
- [Early warning and proactive support agents are associated with reported retention and grade improvements in institutional deployments](early-warning-agents-retention-gains.md) — reports the opposite
- [General composing heuristics produced mixed results in studies of their effectiveness](general-heuristics-mixed-effectiveness-results.md) — related
- Causal inference always goes beyond the data, even in randomized experiments, because experimental manipulations may affect other variables that caused the effect — related
- [Uncontrolled estimates of retention effects on dropout are larger than propensity-adjusted estimates, suggesting confounding inflates naive associations](confounding-inflates-retention-dropout-estimates.md) — related
- [Sensitivity analysis indicated medium-to-large unobserved confounding would be needed to eliminate the reported pandemic effects](unobserved-confounder-sensitivity-pandemic-effects.md) — related
