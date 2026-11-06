---
type: claim
title: "GPT-4o accuracy is comparable via API and web chat interfaces, but response consistency between the two deployments is only 87.5%"
description: "GPT-4o accuracy is comparable via API and web chat interfaces, but response consistency between the two deployments is only 87.5%"
id: gpt4o-api-web-consistency-87-5
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kim-hyun-jin-2025
    resource: "https://doi.org/10.1038/s41598-025-20066-x"
    title: "Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x"
    author: Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GPT-4o accuracy is comparable via API and web chat interfaces, but response consistency between the two deployments is only 87.5%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Web-based and API-based GPT-4o implementations showed no significant accuracy differences across all years, with 87.5% response consistency between implementations. [→ Kim Hyun Jin 2025](#kim-hyun-jin-2025)

## Evidence

### Kim Hyun Jin 2025

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `causal · r2`

Deployment-method comparison for GPT-4o on the same 942 KMLE questions. McNemar tests showed no significant differences across all years and overall; the response consistency rate between implementations was 87.5% (824/942). The authors attribute the lower cross-interface consistency to the web interface's default temperature (approximately 0.7–1.0).

> "Statistical analysis revealed comparable performance between the two versions, with the web-based model achieving an overall accuracy of 83.5% (787/942) compared to the API-based model accuracy of 79.8%, 84.1%, and 86.8% for 2022, 2023, and 2024, respectively."

## Discussion


## Related Claims
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
