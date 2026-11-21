---
type: claim
title: Conditional dependence of advisor actions and student outcomes given algorithmically available features is a necessary condition for expertly targeted action and sufficient for weakened criteria (impactful or non-algorithmic action)
description: Conditional dependence of advisor actions and student outcomes given algorithmically available features is a necessary condition for expertly targeted action and sufficient for weakened criteria (impactful or non-algo...
id: conditional-dependence-necessary-condition-expertise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: schechtman-2025
    resource: "https://doi.org/10.1145/3757887.3767689"
    title: "Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T. (2025). Discretion in the Loop: Human Expertise in Algorithm-Assisted College Advising. arXiv preprint. [doi:10.1145/3757887.3767689](https://doi.org/10.1145/3757887.3767689)"
    author: "Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T."
    q: 1
    i: "?"
    kind: associational
    rigour: 2
  - id: schechtman-2025-2
    resource: "https://doi.org/10.1145/3757887.3767689"
    title: "Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T. (2025). Discretion in the Loop: Human Expertise in Algorithm-Assisted College Advising. arXiv preprint. [doi:10.1145/3757887.3767689](https://doi.org/10.1145/3757887.3767689)"
    author: "Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Conditional dependence of advisor actions and student outcomes given algorithmically available features is a necessary condition for expertly targeted action and sufficient for weakened criteria (impactful or non-algorithmic action)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under faithfulness, A_t is conditionally dependent on Y_t+1 given X_t whenever expertly targeted action occurs (Proposition 4.2). [→ Schechtman 2025](#schechtman-2025)
`q1 i?` If the conditional dependence holds, at least one of impactful action or non-algorithmic action is met (Proposition 4.3). [→ Schechtman 2025 (2)](#schechtman-2025-2)

## Evidence

### Schechtman 2025

Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T. (2025). Discretion in the Loop: Human Expertise in Algorithm-Assisted College Advising. arXiv preprint. [doi:10.1145/3757887.3767689](https://doi.org/10.1145/3757887.3767689)

`q1 · i?` · `associational · r2`

Analytical derivation in §4.3.3: detecting conditional dependence identifies a superset of actions exhibiting human expertise. The article states this "allows us to identify interventions that meet a necessary condition of expertly targeted action (Proposition 4.2)."

> "Proposition 4.2.Suppose the DAG induced byAmeets the constraints in Figure 1(Assumption 4.1) and Ais causally faithful (Assumption 4.4). ThenAt ̸⊥Y t+1|Xt."

### Schechtman 2025 (2)

Schechtman, K., Brandon, B., Stafford, J., Li, H., & Liu, L. T. (2025). Discretion in the Loop: Human Expertise in Algorithm-Assisted College Advising. arXiv preprint. [doi:10.1145/3757887.3767689](https://doi.org/10.1145/3757887.3767689)

`q1 · i?` · `causal · r2`

Analytical result in §4.3.4 showing the statistical condition guarantees weakened criteria without requiring faithfulness. The article notes the condition does not establish whether the action's effect is heterogeneous with respect to non-algorithmic context or whether it improves rather than merely changes outcomes.

> "Proposition4.3.SupposetheDAGmeetstheconstraintsinFigure1(Assumption4.1),andbothAssump- tions 4.2 and 4.3 are satisfied. IfAt ̸⊥Y t+1|X t, then at least one ofimpactful action(Definition 4.2) or non-algorithmic action(Definition 4.3) is met."

## Discussion


## Related Claims
- [Qualitative analysis of advisor notes shows advisors incorporate non-algorithmic contextual information—personal circumstances, career goals, financial troubles—into their intervention decisions](advisor-notes-non-algorithmic-context-use.md) — related
- [Expertly targeted action cannot be identified from observational data alone, even under standard causal assumptions](impossibility-identifying-expertise-observational-data.md) — related
