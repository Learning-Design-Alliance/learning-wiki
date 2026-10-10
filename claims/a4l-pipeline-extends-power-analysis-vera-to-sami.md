---
type: claim
title: "Statistical power analysis for Welch's t-test originally developed for the VERA domain was extended to the SAMI domain through configuration alone"
description: "Statistical power analysis for Welch's t-test originally developed for the VERA domain was extended to the SAMI domain through configuration alone"
id: a4l-pipeline-extends-power-analysis-vera-to-sami
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: y-bai-2025
    resource: "https://arxiv.org/abs/2605.30303"
    title: "Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2605.30303"
    author: Y. Bai, P. Thajchayapong, A. Goel
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Statistical power analysis for Welch's t-test originally developed for the VERA domain was extended to the SAMI domain through configuration alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Applying the pipeline's power function to SAMI fall 2024 data yielded power of 0.403 for Sense of Belonging (t = 1.41, p = 0.080) and 0.642 for Comfortable Interacting (t = 1.87, p = 0.032). [→ Y. Bai 2025](#y-bai-2025)

## Evidence

### Y. Bai 2025

Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2605.30303

`q2 · i?` · `design · r2`

Extension demonstration in Results §5.2: only the VERA domain had used power calculation; the pipeline computed it for SAMI. Table 3 reports Sense of Belonging t = 1.41, p = 0.080, power 0.403; Comfortable Interacting t = 1.87, p = 0.032, power 0.642, complementing Wójcik et al 2025's findings.

> "This research applied the statistical power calculation to the SAMI domain by creating an analysis configuration payload that invoked the power function in the analysis module with parameters specific to the SAMI dataset."

## Discussion


## Related Claims
- [The pipeline's contingency table option applied identically across all three domains reproduced previous descriptive findings](a4l-contingency-table-option-matches-prior-findings-all-domains.md) — related
- [A single configurable analytics codebase replicates prior research findings across three educational AI assistant domains](a4l-pipeline-replicates-analyses-across-three-domains.md) — a broader claim this one bears on
