---
type: claim
title: "Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions"
description: "Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions"
id: bard-image-upload-failures-two-of-100
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: pranav-gupta-2023
    resource: "https://doi.org/10.48550/arXiv.2312.04613"
    title: "Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. [doi:10.48550/arXiv.2312.04613](https://doi.org/10.48550/arXiv.2312.04613)"
    author: Pranav Gupta
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Bard's safety guardrails blocked image upload for 2 of the 100 Physics GRE questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Bard refused or failed to accept 2 of the 100 question images, likely due to safety guardrails falsely flagging them. [→ Pranav Gupta 2023](#pranav-gupta-2023)

## Evidence

### Pranav Gupta 2023

Pranav Gupta. (2023). Testing an LLM's performance on the Physics GRE: some observations. [doi:10.48550/arXiv.2312.04613](https://doi.org/10.48550/arXiv.2312.04613)

`q1 · i?` · `design · r2`

Methodology observation from the image-snippet submission procedure: the PDF was split into individual question images with question numbers removed, and "This happened in 2 out of the 100 questions" — image upload failed, likely due to safety checks.

> "However, there were certain questions that Bard did not accept, possibly due to the images getting falsely flagged by Bard's safety guardrails. This happened in 2 out of the 100 questions."

## Discussion


## Related Claims
- [Bard answered 26 of 98 Physics GRE questions correctly, earning a raw score of 8 out of 100 and placing in the bottom 2% of test-takers](bard-bottom-2-percent-physics-gre.md) — related
- [Among questions Bard answered correctly, some correct options were chosen by chance with fabricated explanations, and Bard hallucinated numerical values for variables](bard-hallucinated-explanations-physics-gre.md) — related
