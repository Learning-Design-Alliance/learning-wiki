---
type: claim
title: Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors
description: Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors
id: srl-transfer-degradation-tenth-auc-within-domain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: conrad-borchers-2025
    resource: "https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    title: "Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud"
    author: Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Transferring SRL classifiers to a second language cost roughly 0.1 AUC compared with same-language cross-validation, except for the realizing errors category. [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

`q2 · i?` · `design · r2`

Comparison of Table 4 language-transfer AUCs against Table 3 within-language 5-fold student-level cross-validation AUCs on chemistry data. The article reports "about 0.1 AUC" degradation "except for the realizing errors category".

> "there was some level of model degrada tion (about 0.1 AUC except for the realizing errors category) when models were transferred to a second language"

## Discussion


## Related Claims
- [The authors state that successful cross-language SRL transfer requires same-domain training data and that declines grow with extensive, unfamiliar scaffolding](conditions-for-cross-language-srl-transfer.md) — related
- [OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German](embedding-srl-classifiers-satisfactory-within-language-german-english.md) — related
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](llm-srl-classifiers-transfer-across-languages-within-domain.md) — related
- [Process and enact SRL categories transfer slightly better from German to English than English to German](srl-transfer-asymmetric-german-english-process-enact.md) — related
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](srl-transfer-errors-subject-specific-terminology.md) — related
