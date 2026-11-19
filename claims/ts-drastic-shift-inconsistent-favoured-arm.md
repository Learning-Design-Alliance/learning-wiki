---
type: claim
title: Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks
description: Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks
id: ts-drastic-shift-inconsistent-favoured-arm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
source_checked: 2026-11-19
recheck_by: 2024
sources:
  - id: zavaleta-bernuy-2021
    resource: "https://doi.org/10.1007/978-3-030-78270-2_75"
    title: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2021). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. [doi:10.1007/978-3-030-78270-2_75](https://doi.org/10.1007/978-3-030-78270-2_75)"
    author: "Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Thompson Sampling drastically shifted assignment toward a favoured arm with minimal exploration room, but the favoured arm varied across weeks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2021 · checked against its sources 2026-11-19 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the epsilon[0.5]-TS weeks, the algorithm drastically shifted to the arm with the highest previous-batch reward and left minimal room for exploration in batch 3, while the seemingly favoured arm varied across weeks and was not consistent. [→ Zavaleta-Bernuy 2021](#zavaleta-bernuy-2021)

## Evidence

### Zavaleta-Bernuy 2021

Zavaleta-Bernuy, A., Zheng, Q.Y., Shaikh, H., Nogas, J., Rafferty, A., Petersen, A., & Williams, J.J. (2021). Using Adaptive Experiments to Rapidly Help Students. arXiv preprint. [doi:10.1007/978-3-030-78270-2_75](https://doi.org/10.1007/978-3-030-78270-2_75)

`q1 · i?` · `causal · r2`

Numerical results from the three-week field deployment, with cumulative click rates and assignment probabilities per arm and batch shown in Table 1 via 1000000 Monte Carlo simulations. The article reports the algorithm "drastically shifts to the arm with the highest re-ward" in batch 3.

> "Even though the probability of assignment aligns with the click rates from the previous batch, the algorithm drastically shifts to the arm with the highest re-ward and leaves minimal room for exploration in batch 3."

## Discussion


## Related Claims
- [Thompson Sampling and TS† exploit a single arm even when no significant difference exists among arm means](bandit-exploitation-without-significant-arm-difference.md) — related
- [Even when two arms have equal reward, Thompson Sampling can misleadingly allocate many participants to one arm](ts-misallocates-participants-equal-reward.md) — a broader claim this one bears on
- [In a real classroom deployment, Thompson Sampling allocated over 88% of students to a single arm in Experiment 2 despite no statistically significant difference between arms](classroom-ts-deployment-uneven-allocation.md) — related
