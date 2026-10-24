---
type: claim
title: "Estimating each grader's bias alone accounts for 95% of the RMSE reduction, while modeling grader reliability contributes little with only four grades per student"
description: "Estimating each grader's bias alone accounts for 95% of the RMSE reduction, while modeling grader reliability contributes little with only four grades per student"
id: grader-bias-estimation-dominates-accuracy-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
newest_evidence: 2013
recheck_by: 2016
sources:
  - id: chris-piech-2013
    resource: "https://arxiv.org/abs/1307.2579"
    title: "Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579"
    author: Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Estimating each grader's bias alone accounts for 95% of the RMSE reduction, while modeling grader reliability contributes little with only four grades per student

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2013 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2016**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The single change of estimating each grader's bias (Model PG1-bias) is responsible for 95% of the reduction in RMSE; modeling grader precision does little to improve performance. [→ Chris Piech 2013](#chris-piech-2013)

## Evidence

### Chris Piech 2013

Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

`q2 · i?` · `design · r2`

Simulation-based evaluation on the HCI datasets (Table 2). The article reports that the bias-only model "is responsible for 95% of our reduction in RMSE", and that on a synthetic dataset generated from Model PG1, reliability is hard to estimate with only four grades per student, becoming notable only with more than 10 assignments graded.

> "But the single change that provides the most signiﬁcant gains in accuracy is obtained by estimating each grader's bias (Model PG1-bias ). This simple model is responsible for 95% of our reduction in RMSE."

## Discussion


## Related Claims
- [Probabilistic peer grading models that estimate grader bias and reliability reduce RMSE against ground-truth grades by 33% and 31% on two HCI course offerings](probabilistic-peer-grading-reduces-rmse-over-30-percent.md) — related
