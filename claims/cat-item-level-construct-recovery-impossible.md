---
type: claim
title: CAT data cannot be fit into factor models at the item level, making item-level construct validity investigation meaningless for CAT
description: CAT data cannot be fit into factor models at the item level, making item-level construct validity investigation meaningless for CAT
id: cat-item-level-construct-recovery-impossible
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: shudong-wang-2012
    resource: "https://www.nwea.org/research/publication/examine-construct-validity-of-computerized-adaptive-test-in-k-12-assessments/"
    title: "Shudong Wang, Hong Jiao. (2012). Examine Construct Validity of Computerized Adaptive Test in K-12 Assessments. Paper presented at the annual meeting of the National Council on Measurement in Education. https://www.nwea.org/research/publication/examine-construct-validity-of-computerized-adaptive-test-in-k-12-assessments/"
    author: Shudong Wang, Hong Jiao
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# CAT data cannot be fit into factor models at the item level, making item-level construct validity investigation meaningless for CAT

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In simulation, factor models did not converge for CAT data (Design 5) at the item level, so items cannot serve as observable indicators for CAT construct validity. [→ Shudong Wang 2012](#shudong-wang-2012)

## Evidence

### Shudong Wang 2012

Shudong Wang, Hong Jiao. (2012). Examine Construct Validity of Computerized Adaptive Test in K-12 Assessments. Paper presented at the annual meeting of the National Council on Measurement in Education. https://www.nwea.org/research/publication/examine-construct-validity-of-computerized-adaptive-test-in-k-12-assessments/

`q2 · i?` · `causal · r2`

Simulation study calibrating Rasch, 2PL, and bifactor data with Mplus under five missing designs; at the item level, all calibrations converged "except for Design 5 at the item level," which the authors attribute to the CAT algorithm's MNAR missingness.

> "However, this is not the case for CAT and design 5 results show that it is impossible to fit CAT data into factor models at the item level for given simulated data and this implies that it is meaningless to investigate construct validity of tests using items as indicators for CAT data."

## Discussion


## Related Claims
- [The study examines how CAT test design and item bank distribution affect content coverage and test efficiency in a CCSS-aligned reading comprehension test](cat-design-and-bank-distribution-affect-coverage-and-efficiency.md) — related
- [Item parceling at the testlet level substantially improves model fit, allowing partial (Rasch, 2PL) or full (bifactor) recovery of CAT constructs](parceling-testlet-level-recovers-cat-construct.md) — reports the opposite
- [MCAR item and response missingness in linear tests shows no differential effect on model fit across Designs 1 to 4](mcar-missingness-linear-tests-no-fit-effect.md) — related
