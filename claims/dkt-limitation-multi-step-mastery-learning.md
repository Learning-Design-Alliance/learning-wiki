---
type: claim
title: Deep Knowledge Tracing has a fundamental limitation that prevents it from supporting mastery learning on multi-step problems
description: Deep Knowledge Tracing has a fundamental limitation that prevents it from supporting mastery learning on multi-step problems
id: dkt-limitation-multi-step-mastery-learning
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
evidence_strength: moderate
sources:
  - id: dkt-1
    title: dkt-1
    q: 2
    i: 2
---

# Deep Knowledge Tracing has a fundamental limitation that prevents it from supporting mastery learning on multi-step problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment · `i2` medium

## Subclaims
`q2 i?` DKT predictions between problems confuse the mastery learning system on multi-step problems because some KCs cannot be correctly applied on the first step, making the system think the KC is unmastered. [→ dkt-1](#dkt-1)

## Evidence

### dkt-1

Qiao Zhang and Christopher MacLellan “Going Online: A simulated student approach for evaluating knowledge tracing in the context of mastery learning”. 2021. In: Proceedings of The 14th International Conference on Educational Data Mining (EDM21). International Educational Data Mining Society, 331-337. https://educationaldatamining.org/edm2021/

`q2 · i2`

Sequence analysis of DKT predictions for a single student's full sequence (Fig. 7) showed the student never masters "AD Answer Numerator" or "AD Answer Denominator", explaining why the DKT tutor gives almost all AD problems. The authors trace the erratic behavior to predictions sampled between problems.

> "Unfortunately, for multi-step problems some KCs cannot be correctly applied on the first step. DKT correctly predicts these KCs will have near 0% correctness (any attempts will be incorrect)."

## Discussion


## Related Claims
-
