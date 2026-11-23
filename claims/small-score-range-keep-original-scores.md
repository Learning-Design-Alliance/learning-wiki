---
type: claim
title: For prompts with a small score range, keeping the original essay score for back-translation essays is effective, but prompt 1 did not improve
description: For prompts with a small score range, keeping the original essay score for back-translation essays is effective, but prompt 1 did not improve
id: small-score-range-keep-original-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: you-jin-jong-2022
    resource: "https://doi.org/10.1155/2022/6906587"
    title: "You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri. (2022). Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores. [doi:10.1155/2022/6906587](https://doi.org/10.1155/2022/6906587)"
    author: You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# For prompts with a small score range, keeping the original essay score for back-translation essays is effective, but prompt 1 did not improve

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For prompts 2 to 6, performance improved using back-translation essays with original scores, except 'Ori + Ch' for prompt 5; prompt 1 did not improve. [→ You-Jin Jong 2022](#you-jin-jong-2022)

## Evidence

### You-Jin Jong 2022

You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri. (2022). Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores. [doi:10.1155/2022/6906587](https://doi.org/10.1155/2022/6906587)

`q2 · i?` · `design · r2`

Numerical results in Table 4 for the 'Manipulating-Length-GRU' model on prompts 1-6 with unadjusted back-translation scores. The article reports that except for 'Ori + Ch' on prompt 5, "for prompts 2 to 6, the performance was improved by using back -translation essays and original scores".

> "For prompt 1, the performance did not improve, and we suspect that this is because prompt 1 has a relatively larger score range than prompts 2 to 6."

## Discussion


## Related Claims
- [For large score-range prompts, raising scores of high-score back-translation essays (Equation 4) outperforms keeping original scores](equation4-score-adjustment-large-range-prompts.md) — related
- [Back-translation slightly raises essay quality because translators correct errors, motivating score adjustment for high-score essays](backtranslation-raises-essay-quality.md) — related
- [Training AES models on back-translation-augmented data improves QWK performance by 0.2% on average for both tested models](backtranslation-augmentation-improves-aes-qwk.md) — a broader claim this one bears on
