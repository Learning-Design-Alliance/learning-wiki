---
type: claim
title: "Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts"
description: "Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts"
id: gvf-removal-drops-qwk-7-13-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: pakhi-bamdev-2023
    resource: "https://doi.org/10.1007/s40593-022-00291-5"
    title: "Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5"
    author: Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Dropping the grammar and vocabulary feature set reduces QWK by 7-13% per prompt, confirming the importance of grammatical construct and vocabulary usage. [→ Pakhi Bamdev 2023](#pakhi-bamdev-2023)

## Evidence

### Pakhi Bamdev 2023

Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5

`q2 · i?` · `design · r2`

Leave-one-category-out ablation (Table 14, Fig. 9) with the XGBoost regressor retrained from scratch. Removing GVF caused drops of "between 7-13% for each prompt"; content-feature removal caused 6% drops on prompts 1, 2, and 4 and about 4% on prompts 3 and 6.

> "The drop percentage ranges between 7-13% for each prompt, thus confirming the importance of capturing grammatical construct and vocabulary usage."

## Discussion


## Related Claims
- [Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6](acoustic-features-least-impact-except-prompts-2-6.md) — related
- [Adding fluency features to content features sharply increases scoring QWK for every prompt](fluency-features-sharp-qwk-increase-ablation.md) — related
