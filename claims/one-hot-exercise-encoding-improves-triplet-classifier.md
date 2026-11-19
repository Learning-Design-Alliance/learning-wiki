---
type: claim
title: Adding a one-hot exercise index to the triplet classifier significantly improves graph-transition classification accuracy
description: Adding a one-hot exercise index to the triplet classifier significantly improves graph-transition classification accuracy
id: one-hot-exercise-encoding-improves-triplet-classifier
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: matt-grenander-2021
    resource: "https://doi.org/10.1609/aaai.v35i17.17829"
    title: "Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)"
    author: Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding a one-hot exercise index to the triplet classifier significantly improves graph-transition classification accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the generated graph-transition test set, the Baseline MLP reached 79.18% accuracy and the one-hot exercise variant 81.20%, with the improvement significant at p < 0.0001 by a z-test. [→ Matt Grenander 2021](#matt-grenander-2021)

## Evidence

### Matt Grenander 2021

Matt Grenander, Robert Belfer, Ekaterina Kochmar, Iulian V. Serban, François St-Hilaire, Jackie C. K. Cheung. (2021). Deep Discourse Analysis for Generating Personalized Feedback in Intelligent Tutor Systems. [doi:10.1609/aaai.v35i17.17829](https://doi.org/10.1609/aaai.v35i17.17829)

`q2 · i?` · `design · r2`

Triplet classifier experiment on 124,000 generated samples (split evenly positive/negative) with duplicate-grouped 80/10/10 splits. Table 4 prints Majority Baseline 50.39%, Baseline MLP 79.18 ± 0.71%, and One-Hot Exercise 81.20 ± 0.68%, significant at the 95% confidence level over the Baseline MLP; a "generalz-test" found the improvements significant with "p< 0.0001". No effect size is printed.

> "Using a generalz-test, we test if the one-hot ex- ercise index vector signiﬁcantly improves the Baseline MLP. Since the generated test set is so large, we ﬁnd that the im- provements are signiﬁcant withp< 0.0001."

## Discussion


## Related Claims
- [Adding non-textual learning traces (attachments, glossary links, tags, formatting) did not improve cognitive presence classification accuracy](learning-traces-no-classifier-improvement.md) — reports the opposite
