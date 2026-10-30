---
type: claim
title: EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology
description: EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology
id: emcqg-three-million-questions-four-specialities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: j-leo-2019
    resource: "https://doi.org/10.1007/s40593-018-00172-w"
    title: "J. Leo, G. Kurdi, N. Matentzoglu, B. Parsia, U. Sattler, S. Forge, G. Donato, W. Dowling. (2019). Ontology-Based Generation of Medical, Multi-term MCQs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-018-00172-w"
    author: J. Leo, G. Kurdi, N. Matentzoglu, B. Parsia, U. Sattler, S. Forge, G. Donato, W. Dowling
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The implemented system generated more than 3 million questions for gastroenterology and hepatology, cardiology, internal medicine and orthopaedics. [→ J. Leo 2019](#j-leo-2019)

## Evidence

### J. Leo 2019

J. Leo, G. Kurdi, N. Matentzoglu, B. Parsia, U. Sattler, S. Forge, G. Donato, W. Dowling. (2019). Ontology-Based Generation of Medical, Multi-term MCQs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-018-00172-w

`q2 · i?` · `design · r2`

Effectiveness measure reported by the authors: the number of distinct questions generatable from EMMeT-OWL across four physician specialities. The count is the article's own printed figure; no statistical test accompanies it.

> "We generate more than 3 million questions for four physician specialities and evaluate our approach in a user study with 15 medical experts."

## Discussion


## Related Claims
- [Ontology-based generation produced exam-appropriate case-based MCQs, with 30% of a stratified sample rated appropriate by both expert raters and 50% by at least one](emcqg-expert-rated-exam-appropriate-questions.md) — related
- [Prior automatic MCQ generation approaches produce structurally simple questions (at most two stem entities) testing mainly recall](prior-aqg-simple-recall-questions.md) — related
- [Existing AQG approaches concentrate on non-technical domains, and technical-domain Wh-type generation has been limited to Bloom's cognitive Level I](existing-aqg-technical-domain-limited-non-technical.md) — reports the opposite
- [Prior AQG work shows ML yields grammatically correct Cloze questions while ontology approaches struggle with Cloze but produce meaningful Wh-type questions](ml-cloze-ontology-wh-grammaticality-gap.md) — related
