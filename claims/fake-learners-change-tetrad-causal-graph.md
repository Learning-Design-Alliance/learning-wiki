---
type: claim
title: "Removing fake learners changed the Tetrad causal graph: the links watching → quizScore and reading → IRT disappeared."
description: "Removing fake learners changed the Tetrad causal graph: the links watching → quizScore and reading → IRT disappeared."
id: fake-learners-change-tetrad-causal-graph
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: alexandron-2019
    resource: "https://doi.org/10.1007/s40593-019-00183-1"
    title: "Alexandron, G., Yoo, L. Y., Ruipérez-Valiente, J. A., Lee, S., & Pritchard, D. E. (2019). Are MOOC Learning Analytics Results Trustworthy? With Fake Learners, They Might Not Be! International Journal of Artificial Intelligence in Education, 29, 484–506. https://doi.org/10.1007/s40593-019-00183-1"
    author: "Alexandron, G., Yoo, L. Y., Ruipérez-Valiente, J. A., Lee, S., & Pritchard, D. E."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Removing fake learners changed the Tetrad causal graph: the links watching → quizScore and reading → IRT disappeared.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In the Tetrad causal-inference replication, two causal links (watching → quizScore and reading → IRT) disappeared after removing fake learners; with fake learners, reading had a negative weight on IRT ability. [→ Alexandron 2019](#alexandron-2019)

## Evidence

### Alexandron 2019

Alexandron, G., Yoo, L. Y., Ruipérez-Valiente, J. A., Lee, S., & Pritchard, D. E. (2019). Are MOOC Learning Analytics Results Trustworthy? With Fake Learners, They Might Not Be! International Journal of Artificial Intelligence in Education, 29, 484–506. https://doi.org/10.1007/s40593-019-00183-1

`q3 · i?` · `associational · r2`

Replication Study 1's Analysis 1B re-ran Tetrad on 8.MReVx data with and without fake learners. "the causal graph changes significantly after removing fake learners data": the links watching → quizScore and reading → IRT disappeared, and with fake learners included, reading had a negative effect on IRT ability.

> "the causal graph changes significantly after removing fake learners data. First, when removing fake learners (moving from the left to the right figures), two causal link disappear ( watching → quizScore and reading → IRT )."

## Discussion


## Related Claims

- In the Champaign et al. replication, removing fake learners moved three correlations (Ability vs. Homework Time, Ability vs. Reading Time, Weekly Improvement vs. Homework Time) in the positive direction, but no correlation changed qualitatively. — related
- [A simulated doubling of fake learners (from ~15% to ~26%) significantly increased the bias in Analysis 1A, making 'Doers who are neither Watchers nor Readers' by far the most successful group.](doubling-fake-learners-increases-bias.md) — related
- [Fake learners spent significantly less time on each type of instructional resource than true learners in the MITx 8.MReVx MOOC.](fake-learners-less-time-on-instructional-resources.md) — related
- [Fake learners attempted a smaller proportion of assessment items than true learners, with the smallest gap on homework items.](fake-learners-attempt-fewer-items.md)
- [Fake learners solved exercises significantly faster than true learners and showed higher weekly improvement, but did not differ significantly on grade, ability, or CFA.](fake-learners-faster-and-higher-weekly-improvement.md)
