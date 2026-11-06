---
type: claim
title: "Unsupported medical claims are significantly more prevalent in the Understanding domain than other domains (Cramér's V = 0.382), the only error type significant after correction"
description: "Unsupported medical claims are significantly more prevalent in the Understanding domain than other domains (Cramér's V = 0.382), the only error type significant after correction"
id: unsupported-claims-prevalent-understanding-domain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-08084-9"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E.
    q: 3
    i: 2
    kind: design
    rigour: 2
  - id: altermatt-fernando-r-2025-2
    resource: "https://doi.org/10.1186/s12909-025-08084-9"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E.
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Unsupported medical claims are significantly more prevalent in the Understanding domain than other domains (Cramér's V = 0.382), the only error type significant after correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3` · `i2` medium
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i2` Chi-square tests with Holm correction found only one error type significantly distributed across domains: unsupported medical claims, concentrated in Understanding (χ² = 17.47, corrected p = 0.0045, Cramér's V = 0.382). [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)
`q3 i?` Reasonable responses showed a higher-occurrence pattern in the Application domain that did not survive correction (corrected p = 0.0521). [→ Altermatt Fernando R. 2025 (2)](#altermatt-fernando-r-2025-2)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9

`q3 · i2` · `design · r2`

Chi-square analysis of error-type distributions across the four cognitive domains in the annotated sample, with Holm correction and Monte Carlo simulation for sparse cells. The printed effect size for this finding is Cramér's V = 0.382, a medium effect, for unsupported medical claims in the Understanding domain.

> "Unsupported medical claims were significantly more prevalent in the Understanding domain, as indicated by a chi-square value of 17.47 (p = 0.0006, corrected p = 0.0045), with a medium effect size (Cramér's V = 0.382)."

### Altermatt Fernando R. 2025 (2)

Altermatt Fernando R., Neyem Andres, Sumonte Nicolás I., Villagrán Ignacio, Mendoza Marcelo, Lacassie Hector J., Delfino Alejandro E. (2025). Evaluating GPT-4o in high-stakes medical assessments: performance and error analysis on a Chilean anesthesiology exam. BMC Medical Education. https://doi.org/10.1186/s12909-025-08084-9

`q3 · i?` · `design · r2`

Same chi-square analysis: the reasonable-response pattern in Application had a printed Cramér's V = 0.316 but "did not reach statistical significance after correction"; equivalence was not tested.

> "Although reasonable responses—defined as plausible but ultimately incorrect answers—showed a pattern of higher occurrence within the Application domain (χ² = 11.98, p = 0.0074), this difference did not reach statistical significance after correction for multiple comparisons (corrected p = 0.0521)"

## Discussion


## Related Claims
- [GPT-4o's unsupported medical claims co-occur with incorrect or vague conclusions (ϕ = 0.386), indicating compounded errors in complex reasoning](gpt4o-error-co-occurrence-claims-vague-conclusions.md) — related
- [Among GPT-4o's incorrect CONACEM responses, unsupported medical claims are the most common error (40.69%), followed by incorrect or vague conclusions (22.07%)](gpt4o-unsupported-medical-claims-most-common-error.md) — related
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — related
