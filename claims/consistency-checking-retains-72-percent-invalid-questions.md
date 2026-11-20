---
type: claim
title: "GPT-4 consistency checking retains 72% of synthetically generated invalid questions, discarding 27% classified as good and 1% as incorrect"
description: "GPT-4 consistency checking retains 72% of synthetically generated invalid questions, discarding 27% classified as good and 1% as incorrect"
id: consistency-checking-retains-72-percent-invalid-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-11-20
recheck_by: 2027
sources:
  - id: nischal-ashok-kumar-and-andrew-lan-2024
    resource: "https://doi.org/10.48550/arXiv.2403.00199"
    title: "Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)"
    author: Nischal Ashok Kumar and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4 consistency checking retains 72% of synthetically generated invalid questions, discarding 27% classified as good and 1% as incorrect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the data augmentation phase, a GPT-4 consistency-checking classification step filters generated questions, keeping 72% for the preference dataset. [→ Nischal Ashok Kumar and Andrew Lan 2024](#nischal-ashok-kumar-and-andrew-lan-2024)

## Evidence

### Nischal Ashok Kumar and Andrew Lan 2024

Nischal Ashok Kumar and Andrew Lan. (2024). Improving Socratic Question Generation using Data Augmentation and Preference Optimization. arXiv preprint arXiv:2403.00199. [doi:10.48550/arXiv.2403.00199](https://doi.org/10.48550/arXiv.2403.00199)

`q2 · i?` · `design · r2`

Results-section report on the GPT-4 consistency-checking classification over six categories during data augmentation. The article reports that "72% of the generated questions are considered for the preference dataset creation", with 27% labeled good and 1% incorrect.

> "In the consistency checking step of the data augmentation phase, we see that 72% of the generated questions are considered for the preference dataset creation as 27% of the generated questions are classified as “good” and 1% as “incorrect”."

## Discussion


## Related Claims
- [Augmentation levels below 20x produce unreliable classification performance in small educational datasets](low-augmentation-levels-unreliable.md) — related
- [LLM-generated responses outperform self-augmentation when augmenting small educational classification datasets](llm-generated-beats-self-augmentation.md) — related
