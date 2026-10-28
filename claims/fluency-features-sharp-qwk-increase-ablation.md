---
type: claim
title: Adding fluency features to content features sharply increases scoring QWK for every prompt
description: Adding fluency features to content features sharply increases scoring QWK for every prompt
id: fluency-features-sharp-qwk-increase-ablation
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

# Adding fluency features to content features sharply increases scoring QWK for every prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Incrementally adding fluency features to content features produces a sharp QWK increase on every prompt in the additive ablation study. [→ Pakhi Bamdev 2023](#pakhi-bamdev-2023)

## Evidence

### Pakhi Bamdev 2023

Pakhi Bamdev, Manraj Singh Grover, Yaman Kumar Singla, Payman Vafaee, Mika Hama, Rajiv Ratn Shah. (2023). Automated Speech Scoring System Under The Lens Evaluating and interpreting the linguistic cues for language proficiency. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-022-00291-5

`q2 · i?` · `design · r2`

Additive ablation study with the XGBoost regressor trained from scratch per feature combination (Table 13). The authors report "the sharp increase in QWK for every prompt" when fluency features join content features; a similar increase occurs when grammar and vocabulary features are added.

> "Figure 8 and Table 13 depict the sharp increase in QWK for every prompt when the fluency features (FF) are introduced to the content features (CF)."

## Discussion


## Related Claims

- [Acoustic features have none to least impact on scoring QWK except for prompts 2 and 6](acoustic-features-least-impact-except-prompts-2-6.md) — related
- [Removing grammar and vocabulary features drops scoring QWK by 7-13% across prompts](gvf-removal-drops-qwk-7-13-percent.md) — related
- [A response-length-only baseline scores poorly, showing scores depend on broader linguistic features](length-only-baseline-performs-poorly.md)
- [Ablation tests identify unique trait-relevant information in specific feature groups: readability and syntactic complexity for content, cohesion and readability for organization, and occurrence, length, or error features for language](ablation-tests-unique-feature-contributions.md) — related
