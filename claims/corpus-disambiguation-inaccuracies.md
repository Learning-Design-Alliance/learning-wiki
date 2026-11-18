---
type: claim
title: Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate
description: Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate
id: corpus-disambiguation-inaccuracies
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: weak
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: atish-pawar-and-vijay-mago-2018
    resource: "https://doi.org/10.48550/arXiv.1804.06333"
    title: "Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. [doi:10.48550/arXiv.1804.06333](https://doi.org/10.48550/arXiv.1804.06333)"
    author: Atish Pawar and Vijay Mago
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Corpus disambiguation can assign inaccurate word senses, which frequency statistics partly mitigate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In the Chemistry corpus, the disambiguation function assigns incorrect contextual senses to some words (e.g., structure and table), and using the frequency of the sense in the corpus reduces this inaccuracy. [→ Atish Pawar and Vijay Mago 2018](#atish-pawar-and-vijay-mago-2018)

## Evidence

### Atish Pawar and Vijay Mago 2018

Atish Pawar and Vijay Mago. (2018). Similarity between Learning Outcomes from Course Objectives using Semantic Analysis, Bloom's taxonomy and Corpus statistics. [doi:10.48550/arXiv.1804.06333](https://doi.org/10.48550/arXiv.1804.06333)

`q1 · i?` · `design · r2`

The authors' qualitative inspection of the disambiguated data for LO3 in the Illustrative Example section. The expected meaning of table is "a tabular array (a set of data arranged in rows and columns)" and structure "the manner of construction of something", but disambiguation returned other senses.

> "we conclude that there are some inaccuracies with the words such as structure and table. The meaning of these words we get after disambiguation is diﬀerent from their contextual sense in the sentence."

## Discussion


## Related Claims
- [The disambiguation-enhanced word similarity algorithm produces better results than the baseline Li et al. algorithm for synonym pairs with similar meaning, and comparable results otherwise](disambiguation-word-similarity-better-for-synonyms.md) — related
- [Contextual diversity — the number of unique documents a word appears in — is more closely associated with adult lexical processing than raw frequency](contextual-diversity-beats-raw-frequency.md) — related
- [The underlying sentence similarity algorithm achieves Pearson correlations of 0.8753 for word similarity and 0.8794 for sentence similarity against benchmarks](sentence-similarity-benchmark-correlations.md) — related
