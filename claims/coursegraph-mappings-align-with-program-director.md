---
type: claim
title: "CourseGraph's nearest-neighbor course mappings largely align with a program director's judgments on real Erasmus+ decisions, with errors traced to ignored pedagogical differences"
description: "CourseGraph's nearest-neighbor course mappings largely align with a program director's judgments on real Erasmus+ decisions, with errors traced to ignored pedagogical differences"
id: coursegraph-mappings-align-with-program-director
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: arthur-nijdam-2026
    resource: "https://arxiv.org/abs/2608.05910"
    title: "Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910"
    author: Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: arthur-nijdam-2026-2
    resource: "https://arxiv.org/abs/2608.05910"
    title: "Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910"
    author: Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# CourseGraph's nearest-neighbor course mappings largely align with a program director's judgments on real Erasmus+ decisions, with errors traced to ignored pedagogical differences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` For validated exchange courses, CourseGraph's closest-match LU courses corresponded with the program director's annotations, e.g. Distributed Data Systems was assigned to Distributed Systems (EDAP25). [→ Arthur Nijdam 2026](#arthur-nijdam-2026)
`q2 i?` CourseGraph is not fully correct: Error Correcting Codes was mapped to a basic first-year course instead of the advanced course the program director chose. [→ Arthur Nijdam 2026 (2)](#arthur-nijdam-2026-2)

## Evidence

### Arthur Nijdam 2026

Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910

`q2 · i?` · `design · r2`

Qualitative hold-out analysis of 24 Erasmus+ decisions from 5 students across 3 universities (TU Delft, UC Santa Cruz, TU München), approved by the former LU program director. A t-SNE visualization (Fig. 3) shows the closest LU match "corresponds with the annotation of the program director".

> "Here, we see that Distributed Data Systems gets assigned to Distributed Systems (EDAP25), which corresponds with the annotation of the program director."

### Arthur Nijdam 2026 (2)

Arthur Nijdam, Paul Stankovski Wagner, Sara Ramezanian. (2026). CourseGraph: Finding overlaps and differences in Computer Science courses across universities. https://arxiv.org/abs/2608.05910

`q2 · i?` · `design · r2`

In the same hold-out analysis, one mismatch occurred: the director mapped Error Correcting Codes to the advanced EITN70, while CourseGraph chose the basic first-year EITA55. The authors attribute errors partly to not factoring in learning-method differences.

> "Error Correcting Codes, mapped to Channel Coding for Reliable Communication (EITN70) by the program director, was mapped to Communication Systems (EITA55) by CourseGraph."

## Discussion


## Related Claims
- [Component-level embeddings make CourseGraph interpretable: learning outcomes contributed most to an example overlap decision](coursegraph-component-level-interpretability.md) — related
- [On the TU/e CS overlap dataset, supervised NLP classifiers (Random Forest, XGBoost) outperform thresholding and zero-shot LLM baselines at detecting course overlap](rf-xgboost-beat-thresholds-and-llms-on-course-overlap.md) — related
