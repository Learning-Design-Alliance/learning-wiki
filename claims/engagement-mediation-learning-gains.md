---
type: claim
title: Engagement (words typed) correlates with learning gains and may mediate the treatment effect
description: Engagement (words typed) correlates with learning gains and may mediate the treatment effect
id: engagement-mediation-learning-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: alessandro-vanzo-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-long.1502"
    title: "Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)"
    author: Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan
    q: 3
    i: 2
    kind: causal
    rigour: 2
  - id: alessandro-vanzo-2025-2
    resource: "https://doi.org/10.18653/v1/2025.acl-long.1502"
    title: "Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)"
    author: Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# Engagement (words typed) correlates with learning gains and may mediate the treatment effect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i2`–`i3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i2` Words typed correlated positively with learning gains (R = 0.316, P = 0.009). [→ Alessandro Vanzo 2025](#alessandro-vanzo-2025)
`q3 i3` Treatment students typed significantly more words than controls (d = 1.421, P < 0.001). [→ Alessandro Vanzo 2025 (2)](#alessandro-vanzo-2025-2)
`q3 i?` In an OLS regression with condition, words_typed and year, the treatment coefficient was non-significant (coef = -0.446, P = 0.666). [→ Alessandro Vanzo 2025](#alessandro-vanzo-2025)

## Evidence

### Alessandro Vanzo 2025

Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)

`q3 · i2` · `causal · r2`

Secondary correlational analysis of RCT data found words_typed and learning_gains were "positively correlated" with printed effect size R = 0.316 (P = 0.009); the correlation is largely driven by the third year, and the authors interpret the regression as suggesting the treatment benefit is largely mediated by engagement.

> "words_typed and learning_gains were positively correlated (𝑅 = 0.316, 𝑃 = 0.009)."

### Alessandro Vanzo 2025 (2)

Alessandro Vanzo, Sankalan Pal Chowdhury, and Mrinmaya Sachan. (2025). GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes. Arxiv Preprint. Originally published 2024. [doi:10.18653/v1/2025.acl-long.1502](https://doi.org/10.18653/v1/2025.acl-long.1502)

`q3 · i3` · `causal · r2`

Comparative analysis of platform usage in the RCT; treatment students typed significantly more words than controls with printed effect size "d = 1.421, 𝑃 < 0.001".

> "We further note that, overall, the words_typed is significantly higher for the treatment group (𝑑 = 1.421, 𝑃 < 0.001)"

## Discussion


## Related Claims
- [Effort appraisals correlate negatively with monitoring judgments: high mental effort is associated with poorer performance judgments](effort-appraisals-negative-correlation-monitoring.md) — related
- [GPT-4 interactive homework improved grammar learning gains for third-year students but not fifth-year students](gpt4-homework-tutor-learning-gains.md) — related
- [Weaker students benefited more from GPT-4 tutoring, contrary to prior findings](weaker-students-benefit-more-gpt4-tutoring.md) — related
