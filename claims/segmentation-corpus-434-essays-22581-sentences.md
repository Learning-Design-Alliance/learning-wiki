---
type: claim
title: The segmentation training corpus covers 434 of 698 essays, yielding 22,581 coded sentences
description: The segmentation training corpus covers 434 of 698 essays, yielding 22,581 coded sentences
id: segmentation-corpus-434-essays-22581-sentences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: gombert-2024
    resource: "https://doi.org/10.1007/s40593-023-00387-6"
    title: "Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H. (2024). From the Automated Assessment of Student Essay Content to Highly Informative Feedback: a Case Study. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00387-6"
    author: "Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The segmentation training corpus covers 434 of 698 essays, yielding 22,581 coded sentences

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Gombert 2024: no comparison group (read from the study by two models, 2026-10-28)

## Subclaims
`q2 i?` Only 434 of the 698 collected essays were fully coded for the sentence-to-tip segmentation step, producing 22,581 coded sentences; the rest were not coded for segmentation. [→ Gombert 2024](#gombert-2024)

## Evidence

### Gombert 2024

Gombert, S., Fink, A., Giorgashvili, T., Jivet, I., Di Mitri, D., Yau, J., Frey, A., & Drachsler, H. (2024). From the Automated Assessment of Student Essay Content to Highly Informative Feedback: a Case Study. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00387-6

`q2 · i?` · `causal · r2`

Dataset construction from two cohorts of teacher students who submitted compulsory German-language essays via Moodle. The article reports that "Only 434 of the 698 essays were entirely coded", yielding the sentence-level segmentation dataset exported from INCEpTION as UIMA XMI files.

> "Only 434 of the 698 essays were entirely coded during this step, which resulted in a satisfactory number of 22,581 sentences. The remainder of the essays were not coded for the segmentation step."

## Discussion


## Related Claims
- [Sentence-to-learning-tip segmentation coding by three trained coders reached an average Cohen's Kappa of 0.96](segmentation-coding-kappa-096.md) — related
- [Learning-tip-to-lecture-topic coding by seven coders reached an overall agreement of 0.87 (Cohen's Kappa)](topic-coding-agreement-087.md) — related
