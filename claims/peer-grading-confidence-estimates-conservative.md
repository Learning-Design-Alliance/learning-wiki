---
type: claim
title: "The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct"
description: "The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct"
id: peer-grading-confidence-estimates-conservative
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-16
evidence_strength: moderate
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

# The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Binned confidence estimates were validated against actual pass rates; when the model claims 90–95% confidence, its estimate is correct over 95% of the time, indicating conservative rather than overconfident calibration. [→ Chris Piech 2013](#chris-piech-2013)

## Evidence

### Chris Piech 2013

Chris Piech, Jonathan Huang, Zhenghao Chen, Chuong Do, Andrew Ng, Daphne Koller. (2013). Tuned Models of Peer Assessment in MOOCs. arXiv. https://arxiv.org/abs/1307.2579

`q2 · i?` · `design · r2`

Simulation experiment on ground-truth submissions: over 5000 predictions per confidence range, the article binned estimated confidences and tested pass rates, comparing model confidence to actual success rate (Figure 3c). The model was found "on the conservative side" rather than overconfident.

> "the results, shown in Figure 3(c), demonstrate that our conﬁdence estimates are on the conservative side — for example over 95% of the time that our model claims it is between 90 and 95% conﬁdent of a prediction, the model's estimate is correct."

## Discussion


## Related Claims
-
