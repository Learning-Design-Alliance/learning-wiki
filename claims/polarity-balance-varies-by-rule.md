---
type: claim
title: "Polarity balance of teacher corpora varies by rule: more negatives for zip-code, more positives for suffix-s"
description: "Polarity balance of teacher corpora varies by rule: more negatives for zip-code, more positives for suffix-s"
id: polarity-balance-varies-by-rule
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2017
sources:
  - id: long-ouyang-2017
    resource: "https://doi.org/10.48550/arXiv.1711.09401"
    title: "Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)"
    author: Long Ouyang, Michael C. Frank
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: long-ouyang-2017-2
    resource: "https://doi.org/10.48550/arXiv.1711.09401"
    title: "Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)"
    author: Long Ouyang, Michael C. Frank
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Polarity balance of teacher corpora varies by rule: more negatives for zip-code, more positives for suffix-s

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For the zip-code rule teachers gave significantly more negative than positive examples. [→ Long Ouyang 2017](#long-ouyang-2017)
`q2 i?` For the suffix-s rule teachers gave significantly more positive than negative examples. [→ Long Ouyang 2017 (2)](#long-ouyang-2017-2)

## Evidence

### Long Ouyang 2017

Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)

`q2 · i?` · `associational · r1`

Paired t-tests over the teaching corpora showed rule-dependent polarity: for zip-code, "teachers gave signiﬁcantly more negative examples (M = 0.64, SD = 1.85 more negative examples than positive)", t(38) = -2.15, p < 0.05.

> "For the zip-code rule, teachers gave signiﬁcantly more negative examples (M = 0.64, SD = 1.85 more negative examples than positive), t(38) = -2.15, p < 0.05 by a paired t-test."

### Long Ouyang 2017 (2)

Long Ouyang, Michael C. Frank (2017). Pedagogical learning. 31st Conference on Neural Information Processing Systems (NIPS 2017). [doi:10.48550/arXiv.1711.09401](https://doi.org/10.48550/arXiv.1711.09401)

`q2 · i?` · `associational · r1`

For suffix-s the same analysis found "teachers gave signiﬁcantly more positive examples than negative (M = 0.69, SD = 1.21)", t(38) = 3.55, p < 0.005.

> "For the sufﬁx-s rule, teachers gave signiﬁcantly more positive examples than negative (M = 0.69, SD = 1.21),t(38) = 3.55, p < 0.005)."

## Discussion


## Related Claims
- [Human learners can infer complex rules from teachers' example corpora, which were verified as helpful evidence](human-learners-guess-regex-from-corpora.md) — related
- [Unconstrained teacher corpora ranged from 1 to 13 examples with a low but nonzero labeling error rate of 6.6%](teaching-corpus-size-and-error-rate.md) — related
- [Teachers of regular expressions produce minimal-pair clustering structure, editing positive examples into near-boundary negative examples](minimal-pair-clustering-regex-teaching.md) — related
- [Teacher corpora have internal temporal structure: the first example in a cluster tends to be positive and clusters occur in contiguous spans](temporal-cluster-structure-teaching-corpora.md) — related
