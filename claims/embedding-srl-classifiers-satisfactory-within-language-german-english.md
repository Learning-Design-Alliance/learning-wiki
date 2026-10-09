---
type: claim
title: OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German
description: OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German
id: embedding-srl-classifiers-satisfactory-within-language-german-english
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

# OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Within-language 5-fold student-level cross-validation AUCs were satisfactory and comparable for English and German chemistry utterances across all four SRL categories. [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

`q2 · i?` · `design · r2`

Baseline cross-validation on chemistry data only, with student-level 5-fold splits. Printed AUCs: English Process 0.893, Plan 0.878, Enact 0.821, Realizing Errors 0.885; German 0.863, 0.826, 0.792, 0.894.

> "Cross-validation results replicated the prior finding on English data that the OpenAI embedding model achieved satisfactory cross-validation performance (Zhang et al., 2024a) when trained on German data."

## Discussion


## Related Claims
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](llm-srl-classifiers-transfer-across-languages-within-domain.md) — related
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](srl-transfer-degradation-tenth-auc-within-domain.md) — related
- [Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category](srl-transfer-errors-subject-specific-terminology.md) — related
- [Process and enact SRL categories transfer slightly better from German to English than English to German](srl-transfer-asymmetric-german-english-process-enact.md) — related
