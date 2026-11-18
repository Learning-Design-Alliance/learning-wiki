---
type: claim
title: In a synthetic comparison, the pedagogical learner L1 generally outperforms the non-pedagogical learner L0 on human teaching data, though they are on par in some parameter regimes
description: In a synthetic comparison, the pedagogical learner L1 generally outperforms the non-pedagogical learner L0 on human teaching data, though they are on par in some parameter regimes
id: pedagogical-learner-outperforms-non-pedagogical
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2017
sources:
  - id: long-ouyang-2017
    resource: "https://doi.org/10.48550/arXiv.1711.09401"
    title: "Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)"
    author: Long Ouyang, Michael C. Frank
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: long-ouyang-2017-2
    resource: "https://doi.org/10.48550/arXiv.1711.09401"
    title: "Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)"
    author: Long Ouyang, Michael C. Frank
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# In a synthetic comparison, the pedagogical learner L1 generally outperforms the non-pedagogical learner L0 on human teaching data, though they are on par in some parameter regimes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q1`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Across parameter values, L1 generally outperformed L0 at recovering the correct regex from teaching corpora, sometimes by a dramatic margin. [→ Long Ouyang 2017](#long-ouyang-2017)
`q1 i?` At its worst L1 performed on par with L0, in the logβ =−0.1 column and α = 1 row. [→ Long Ouyang 2017 (2)](#long-ouyang-2017-2)

## Evidence

### Long Ouyang 2017

Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)

`q1 · i?` · `design · r2`

Synthetic comparison over a restricted regex space (each target plus two distractors), with the corpus space approximated by empirical human teaching data: "L1 generally outperforms L0, sometimes by a dramatic margin (e.g., L0 accuracy = 0.25 versus L1 accuracy = 0.8)" across α and β values.

> "As Figure 5 shows, L1 generally outperforms L0, sometimes by a dramatic margin (e.g., L0 accuracy = 0.25 versus L1 accuracy = 0.8)."

### Long Ouyang 2017 (2)

Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)

`q1 · i?` · `causal · r2`

Worst case in the same comparison: "At its worst,L1 performs on par withL0", in the logβ =−0.1 column and α = 1 row of Figure 5.

> "At its worst,L1 performs on par withL0; these are the logβ =−0.1 column and α = 1 row of the ﬁgure."

## Discussion


## Related Claims
- [Human Learners Guess Regex From Corpora](human-learners-guess-regex-from-corpora.md)
