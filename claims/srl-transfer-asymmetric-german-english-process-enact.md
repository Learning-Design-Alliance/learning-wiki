---
type: claim
title: Process and enact SRL categories transfer slightly better from German to English than English to German
description: Process and enact SRL categories transfer slightly better from German to English than English to German
id: srl-transfer-asymmetric-german-english-process-enact
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

# Process and enact SRL categories transfer slightly better from German to English than English to German

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Reliable transfer asymmetries between languages appeared only for the process and enact categories, favoring German-to-English transfer. [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

`q2 · i?` · `design · r2`

Language-transfer analysis comparing direction of transfer on matched chemistry platforms. Asymmetry was judged by point estimates not overlapping with the other language's 95% confidence interval; e.g., enact 0.709 (G→E) vs 0.660 (E→G).

> "reliable differences in the transferability of models between the two languages were found only for the process and enact categories, which generalized slightly better from German to English than English to German"

## Discussion


## Related Claims
- [OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German](embedding-srl-classifiers-satisfactory-within-language-german-english.md) — related
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](llm-srl-classifiers-transfer-across-languages-within-domain.md) — related
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](srl-transfer-degradation-tenth-auc-within-domain.md) — related
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](srl-transfer-errors-subject-specific-terminology.md) — related
