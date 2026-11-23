---
type: claim
title: For large score-range prompts, raising scores of high-score back-translation essays (Equation 4) outperforms keeping original scores
description: For large score-range prompts, raising scores of high-score back-translation essays (Equation 4) outperforms keeping original scores
id: equation4-score-adjustment-large-range-prompts
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

# For large score-range prompts, raising scores of high-score back-translation essays (Equation 4) outperforms keeping original scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For prompts 7 and 8, augmented data scored with Equation 4 showed higher performance than augmented data scored with original scores. [→ You-Jin Jong 2022](#you-jin-jong-2022)

## Evidence

### You-Jin Jong 2022

You-Jin Jong, Yong-Jin Kim, Ok-Chol Ri. (2022). Improving Performance of Automated Essay Scoring by using back-translation essays and adjusted scores. [doi:10.1155/2022/6906587](https://doi.org/10.1155/2022/6906587)

`q2 · i?` · `design · r2`

Numerical results in Table 5 for the 'Manipulating-Length-GRU' model on prompts 7 and 8, comparing score-adjustment equations. The quote is from the Analysis section; no effect size is printed. For prompt 8 augmented data beat original data; for prompt 7 original data was best.

> "In contrast, the augmented data using Equation 4 showed a  higher performance than when using original scores."

## Discussion


## Related Claims
- [Training AES models on back-translation-augmented data improves QWK performance by 0.2% on average for both tested models](backtranslation-augmentation-improves-aes-qwk.md) — related
- [Back-translation slightly raises essay quality because translators correct errors, motivating score adjustment for high-score essays](backtranslation-raises-essay-quality.md) — a broader claim this one bears on
- [For prompts with a small score range, keeping the original essay score for back-translation essays is effective, but prompt 1 did not improve](small-score-range-keep-original-scores.md) — related
