---
type: claim
title: The authors state that successful cross-language SRL transfer requires same-domain training data and that declines grow with extensive, unfamiliar scaffolding
description: The authors state that successful cross-language SRL transfer requires same-domain training data and that declines grow with extensive, unfamiliar scaffolding
id: conditions-for-cross-language-srl-transfer
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: weak
sources:
  - id: conrad-borchers-2025
    resource: "https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    title: "Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    author: Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The authors state that successful cross-language SRL transfer requires same-domain training data and that declines grow with extensive, unfamiliar scaffolding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` For successful language transfer, models must be trained within the same instructional domain, and declines may be more pronounced with extensive scaffolding and unfamiliar instructional strategies. [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

`q1 · i?` · `design · r2`

The authors' statement of their second contribution in the introduction, summarizing the study's transfer findings; the article offers this as its own interpretation of the RQ2 and RQ3 analyses rather than as a printed effect size.

> "Additionally, performance declines may be more pronounced in tutoring systems that feature extensive scaffolding and employ instructional strategies unfamiliar to the target population."

## Discussion


## Related Claims
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](llm-srl-classifiers-transfer-across-languages-within-domain.md) — related
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](srl-transfer-degradation-tenth-auc-within-domain.md) — related
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](srl-transfer-errors-subject-specific-terminology.md) — related
