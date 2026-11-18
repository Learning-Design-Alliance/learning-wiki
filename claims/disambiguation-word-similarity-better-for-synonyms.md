---
type: claim
title: The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise
description: The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al.
id: disambiguation-word-similarity-better-for-synonyms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2018
source_checked: 2026-11-18
recheck_by: 2021
sources:
  - id: atish-pawar-2018
    resource: "https://doi.org/10.48550/arXiv.1804.06339"
    title: "Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago. (2018). Are we on the same learning curve: Visualization of Semantic Similarity of Course Objectives. arXiv preprint. [doi:10.48550/arXiv.1804.06339](https://doi.org/10.48550/arXiv.1804.06339)"
    author: Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2018 · checked against its sources 2026-11-18 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` On the Rubenstein and Goodenough theme word pairs, the proposed algorithm's results are better for words having similar meaning and close to the Li et al. algorithm for other cases. [→ Atish Pawar 2018](#atish-pawar-2018)

## Evidence

### Atish Pawar 2018

Atish Pawar, Sahib Budhiraja, Daniel Kivi, Vijay Mago. (2018). Are we on the same learning curve: Visualization of Semantic Similarity of Course Objectives. arXiv preprint. [doi:10.48550/arXiv.1804.06339](https://doi.org/10.48550/arXiv.1804.06339)

`q1 · i?` · `design · r2`

Numerical evaluation on theme word pairs from Rubenstein and Goodenough's 'Contextual correlates of synonymy'; the article reports results are "better for the words having similar meaning" and close to the baseline algorithm elsewhere, with a figure comparing the results.

> "We tested this algorithm on the theme word pairs from Herbert Rubenstein and John B Goodenough's 'Contextual correlates of synonymy'[14]. The results are better for the words having similar meaning. For other cases, the results are close to the algorithm implemented in [9]."

## Discussion


## Related Claims
- [Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate](corpus-disambiguation-inaccuracies.md) — related
- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](sentence-similarity-benchmark-correlations.md) — related
