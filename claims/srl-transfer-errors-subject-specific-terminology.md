---
type: claim
title: Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category
description: Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category
id: srl-transfer-errors-subject-specific-terminology
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

# Cross-language SRL misclassifications arise from subject-specific terminology that differs from commonplace translation, especially in the enact category

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` Thematic error analysis attributed language-transfer misclassifications to discrepancies between expert-based translations of tutoring systems and commonplace translation implicit in LLMs. [→ Conrad Borchers 2025](#conrad-borchers-2025)

## Evidence

### Conrad Borchers 2025

Conrad Borchers, Jiayi Zhang, Hendrik Fleischer, Sascha Schanze, Vincent Aleven, Ryan S. Baker. (2025). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. Journal of Educational Data Mining, Volume 17, No 2. https://github.com/pcla-code/EDM24_SRL-detectors-for-think-aloud

`q1 · i?` · `design · r2`

Thematic error analysis of misclassified utterances grouped by prediction task, coded independently by two bilingual researchers. The term "cancel" maps to "kürzen" or "streichen" in chemistry, and enact utterances with these words were incorrectly classified.

> "Here, the action word "canceling" (or "kürzen " in the original utterance) would be most commonly translated as "shortening," which an English embedding model might not have learned correctly as a consequence."

## Discussion


## Related Claims
- [The authors state that successful cross-language SRL transfer requires same-domain training data and that declines grow with extensive, unfamiliar scaffolding](conditions-for-cross-language-srl-transfer.md) — related
- [OpenAI text-embedding-3-small classifiers reach satisfactory within-language cross-validation performance for SRL coding in both English and German](embedding-srl-classifiers-satisfactory-within-language-german-english.md) — related
- [LLM embedding-based SRL classifiers trained on one language reliably classify SRL categories in the other language within the same instructional domain](llm-srl-classifiers-transfer-across-languages-within-domain.md) — related
- [Process and enact SRL categories transfer slightly better from German to English than English to German](srl-transfer-asymmetric-german-english-process-enact.md) — related
- [Cross-language SRL classifier transfer shows about 0.1 AUC degradation relative to within-language performance, except for realizing errors](srl-transfer-degradation-tenth-auc-within-domain.md) — related
