---
type: claim
title: GRADE-Match, a utility-curve-based classroom matching procedure, outperforms random and MOOC-style assignment in simulation but does not attain optimal matching
description: GRADE-Match, a utility-curve-based classroom matching procedure, outperforms random and MOOC-style assignment in simulation but does not attain optimal matching
id: grade-match-beats-random-and-mooc-assignment
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
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GRADE-Match, a utility-curve-based classroom matching procedure, outperforms random and MOOC-style assignment in simulation but does not attain optimal matching

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GRADE-Match generally outperforms random matching and, particularly for top-performing students, is better than assigning students to the lowest-error-rate (MOOC-style) teacher who may be representationally distinct. [→ Ilia Sucholutsky 2024](#ilia-sucholutsky-2024)
`q2 i?` GRADE-Match does not attain optimal matching performance, which the authors attribute to a possible mismatch in the utility curve. [→ Ilia Sucholutsky 2024](#ilia-sucholutsky-2024)

## Evidence

### Ilia Sucholutsky 2024

Ilia Sucholutsky, Katherine M. Collins, Maya Malaviya, Nori Jacoby, Weiyang Liu, Theodore R. Sumers, Michalis Korakakis, Umang Bhatt, Mark Ho, Joshua B. Tenenbaum, Brad Love, Zachary A. Pardos, Adrian Weller, Thomas L. Griffiths. (2024). Representational Alignment Supports Effective Teaching. arXiv. [doi:10.48550/arXiv.2406.04302](https://doi.org/10.48550/arXiv.2406.04302)

`q2 · i?` · `causal · r2`

Simulation matching experiments over pools of 1000 students and 30 teachers on a 6x6 simple-features grid, comparing GRADE-Match against Random, MOOC (Min Err), and brute-force Optimal baselines (Figure 1H, Tables 2-3). In Table 2, Utility achieves 0.38 ± 0.01 average accuracy versus Random 0.33 ± 0.01 and Min Err 0.37 ± 0.01, below Optimal 0.43 ± 0.01. No effect size is printed.

> "Our matching algorithm, which groups students to teachers based on their representational alignment and teacher error rate, generally outperforms random matching and, particularly for top-performing students, is better than having assigned the student to an expert (minimal error rate teacher; MOOC) who may be representationally distinct"

## Discussion


## Related Claims
- [In GRADE simulations, students can achieve higher accuracy learning from more erroneous but representationally aligned teachers than from more accurate but misaligned teachers](aligned-erroneous-teachers-beat-misaligned-experts-simulation.md) — a narrower finding that bears on this claim
- [The utility-curve matching approach generalizes to dino stimuli, boosting accuracy particularly for top-performing students relative to baselines ignoring misalignment](utility-matching-generalizes-dino-stimuli.md) — possibly the same claim (merge candidate)
