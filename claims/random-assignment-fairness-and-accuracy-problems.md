---
type: claim
title: Random reviewer assignment produces inconsistent grading and fairness concerns, though calibration and dynamic allocation can mitigate specific problems
description: Random reviewer assignment produces inconsistent grading and fairness concerns, though calibration and dynamic allocation can mitigate specific problems
id: random-assignment-fairness-and-accuracy-problems
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: uchswas-paul-2026
    resource: "https://doi.org/10.1007/978-3-032-15743-0_27"
    title: "Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer. (2026). Optimizing Peer Grading: A Systematic Literature Review of Reviewer Assignment Strategies and Quantity of Reviewers. Originally published 2025. [doi:10.1007/978-3-032-15743-0_27](https://doi.org/10.1007/978-3-032-15743-0_27)"
    author: Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer
    q: 2
    i: "?"
    kind: review
    rigour: 3
  - id: uchswas-paul-2026-2
    resource: "https://doi.org/10.1007/978-3-032-15743-0_27"
    title: "Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer. (2026). Optimizing Peer Grading: A Systematic Literature Review of Reviewer Assignment Strategies and Quantity of Reviewers. Originally published 2025. [doi:10.1007/978-3-032-15743-0_27](https://doi.org/10.1007/978-3-032-15743-0_27)"
    author: Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Random reviewer assignment produces inconsistent grading and fairness concerns, though calibration and dynamic allocation can mitigate specific problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Random assignment leads to overgrading, harsh underrating, arbitrary grading, and fairness concerns when low-quality reviewers are unevenly distributed across submissions. [→ Uchswas Paul 2026](#uchswas-paul-2026)
`q2 i?` Incorporating calibration papers under random reviewer assignment reduced grading error by up to 39.13 MSE points (Yuan et al.). [→ Uchswas Paul 2026 (2)](#uchswas-paul-2026-2)

## Evidence

### Uchswas Paul 2026

Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer. (2026). Optimizing Peer Grading: A Systematic Literature Review of Reviewer Assignment Strategies and Quantity of Reviewers. Originally published 2025. [doi:10.1007/978-3-032-15743-0_27](https://doi.org/10.1007/978-3-032-15743-0_27)

`q2 · i?` · `review · r3`

Qualitative synthesis (RQ2) of studies using random assignment. The review reports that some students overgrade, some harshly underrate, and a few grade arbitrarily; Toll et al. noted students' scores depending on the "luck" of receiving conscientious reviewers, and Albano et al. reported three students received no evaluations despite each submission being assigned three reviewers.

> "Random assignment can engender fairness concerns—particularly when low-quality reviewers are unevenly assigned, disproportionately affecting certain submissions."

### Uchswas Paul 2026 (2)

Uchswas Paul, Shail Shah, Sri Vaishnavi Mylavarapu, M. Parvez Rashid, and Edward Gehringer. (2026). Optimizing Peer Grading: A Systematic Literature Review of Reviewer Assignment Strategies and Quantity of Reviewers. Originally published 2025. [doi:10.1007/978-3-032-15743-0_27](https://doi.org/10.1007/978-3-032-15743-0_27)

`q2 · i?` · `quant-synthesis · r2`

Synthesis of mitigation techniques for random assignment. The review reports calibration papers reduced grading error by up to 39.13 MSE points; dynamic allocation (e.g., selecting submissions with the fewest current reviews) addresses reviewers not completing assigned reviews, and priority mechanisms incentivize participation.

> "Yuan et al. [31] reduced grading error by up to 39.13 MSE points, even under random reviewer assignment, by incorporating calibration papers."

## Discussion


## Related Claims
- [Competency-based reviewer assignment systematically mitigates skewed grading and, by assigning diverse reviewers, yields complementary feedback with learning benefits](competency-based-assignment-improves-accuracy-fairness.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — related
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — related
