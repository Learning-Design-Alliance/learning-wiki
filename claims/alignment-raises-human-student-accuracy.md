---
type: claim
title: In a 480-participant human experiment, higher teacher-student representational alignment generally induces higher student accuracy, and large increases in teacher error can be offset by increasing alignment
description: In a 480-participant human experiment, higher teacher-student representational alignment generally induces higher student accuracy, and large increases in teacher error can be offset by increasing alignment
id: alignment-raises-human-student-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: ilia-sucholutsky-2024
    resource: "https://doi.org/10.48550/arXiv.2406.04302"
    title: "Ilia Sucholutsky, Katherine M. Collins, Maya Malaviya, Nori Jacoby, Weiyang Liu, Theodore R. Sumers, Michalis Korakakis, Umang Bhatt, Mark Ho, Joshua B. Tenenbaum, Brad Love, Zachary A. Pardos, Adrian Weller, Thomas L. Griffiths. (2024). Representational Alignment Supports Effective Teaching. arXiv. [doi:10.48550/arXiv.2406.04302](https://doi.org/10.48550/arXiv.2406.04302)"
    author: Ilia Sucholutsky, Katherine M. Collins, Maya Malaviya, Nori Jacoby, Weiyang Liu, Theodore R. Sumers, Michalis Korakakis, Umang Bhatt, Mark Ho, Joshua B. Tenenbaum, Brad Love, Zachary A. Pardos, Adrian Weller, Thomas L. Griffiths
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
---

# In a 480-participant human experiment, higher teacher-student representational alignment generally induces higher student accuracy, and large increases in teacher error can be offset by increasing alignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q3`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` Across simple-features and salient-dinos tasks with human learners, higher representational alignment of machine teachers generally induces higher average student accuracy. [→ Ilia Sucholutsky 2024](#ilia-sucholutsky-2024)
`q3 i?` Large increases in teacher error rate can be offset by increasing representational alignment, e.g., a teacher with error rate 0 and alignment 0.3 yields similar student outcomes to a teacher with error rate 0.4 and alignment 0.8. [→ Ilia Sucholutsky 2024](#ilia-sucholutsky-2024)

## Evidence

### Ilia Sucholutsky 2024

Ilia Sucholutsky, Katherine M. Collins, Maya Malaviya, Nori Jacoby, Weiyang Liu, Theodore R. Sumers, Michalis Korakakis, Umang Bhatt, Mark Ho, Joshua B. Tenenbaum, Brad Love, Zachary A. Pardos, Adrian Weller, Thomas L. Griffiths. (2024). Representational Alignment Supports Effective Teaching. arXiv. [doi:10.48550/arXiv.2406.04302](https://doi.org/10.48550/arXiv.2406.04302)

`q3 · i?` · `causal · r?`

Human experiment with N = 480 Prolific participants in which machine teachers taught humans categorization on grids; a utility curve paralleling the simulations was constructed by post-hoc varying teacher error rate. The authors report that "higher representational alignment induces higher average student accuracy"; correlations are in Table 1 and no effect size is printed for this overall pattern.

> "We find in Figure 2 that across both tasks (simple-features and salient-dinos), generally, higher representational alignment induces higher average student accuracy, and report correlations in Table 1. We find that even large increases in teacher error rate can be offset by increasing representational alignment"

## Discussion


## Related Claims
- [Correlations between teacher-student representational alignment and human student accuracy vary by condition, from r = 0.91 (p = 0.013) for simple-features quadrants to non-significant values](alignment-accuracy-correlations-by-condition.md) — a narrower finding that bears on this claim
- [The utility-curve matching approach generalizes to dino stimuli, boosting accuracy particularly for top-performing students relative to baselines ignoring misalignment](utility-matching-generalizes-dino-stimuli.md) — related
- [In GRADE simulations, students can achieve higher accuracy learning from more erroneous but representationally aligned teachers than from more accurate but misaligned teachers](aligned-erroneous-teachers-beat-misaligned-experts-simulation.md) — possibly the same claim (merge candidate)
