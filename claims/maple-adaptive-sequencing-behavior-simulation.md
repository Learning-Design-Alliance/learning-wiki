---
type: claim
title: MAPLE exhibited adaptive sequencing behavior, starting with easy questions and progressively proposing harder ones, unlike the comparison algorithms
description: MAPLE exhibited adaptive sequencing behavior, starting with easy questions and progressively proposing harder ones, unlike the comparison algorithms
id: maple-adaptive-sequencing-behavior-simulation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: avi-segal-2018
    resource: "https://doi.org/10.1007/978-3-319-93846-2_59"
    title: "Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom. (2018). Combining Difficulty Ranking with Multi-Armed Bandits to Sequence Educational Content. [doi:10.1007/978-3-319-93846-2_59](https://doi.org/10.1007/978-3-319-93846-2_59)"
    author: Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# MAPLE exhibited adaptive sequencing behavior, starting with easy questions and progressively proposing harder ones, unlike the comparison algorithms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MAPLE started by offering easy questions to most students and then moved to propose more difficult questions while continuing to propose easy questions, a behavior not observed in the other conditions. [→ Avi Segal 2018](#avi-segal-2018)

## Evidence

### Avi Segal 2018

Avi Segal, Yossi Ben David, Joseph Jay Williams, Kobi Gal, Yaar Shalom. (2018). Combining Difficulty Ranking with Multi-Armed Bandits to Sequence Educational Content. [doi:10.1007/978-3-319-93846-2_59](https://doi.org/10.1007/978-3-319-93846-2_59)

`q2 · i?` · `causal · r2`

Numerical simulation results shown in Figure 1 describe MAPLE's sequencing over time. The authors state this adaptive behavior "was not observed in the other conditions tested"; EduRank used mostly easy questions and Naive Maple did not exhibit adaptive behavior.

> "We can see that MAPLE started with offering easy questions to most students and then moved to propose more difﬁcult questions while at the same time continuing to propose easy questions for a long time. This behaviour demonstrates the adaptive nature of MAPLE and was not observed in the other conditions tested."

## Discussion


## Related Claims
- [MAPLE's adaptation needs improvement for weak simulated students, whose estimated skill declined after initial progress](maple-weak-students-needs-tuning.md) — related
- [Students reported significantly higher satisfaction with questions posed by MAPLE than with the Ascending and YBKT sequencing approaches](maple-higher-student-satisfaction-field-trial.md) — related
- [In a classroom field trial, 7th-grade students sequenced by MAPLE achieved higher post-test grades than students sequenced by the Ascending or YBKT algorithms](maple-field-trial-higher-posttest-grades.md) — related
