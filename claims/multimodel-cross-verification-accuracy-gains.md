---
type: claim
title: "Multi-model cross-verification outperformed the single best model, reaching 94.17% accuracy with two models and 96.33% with three"
description: "Multi-model cross-verification outperformed the single best model, reaching 94.17% accuracy with two models and 96.33% with three"
id: multimodel-cross-verification-accuracy-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yao-zhong-2025
    resource: "https://doi.org/10.2196/69485"
    title: "Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485"
    author: Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multi-model cross-verification outperformed the single best model, reaching 94.17% accuracy with two models and 96.33% with three

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adopting models' answers when they agree and human judgment when they disagree, dual-model (Baichuan+ChatGPT) verification achieved 94.17% accuracy and tri-model (plus ERNIE Bot) achieved 96.33%, with the largest gains on simple question types. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Comparative analysis of single-model (Baichuan) versus multimodel cross-verification on the CNMLE, shown in Figure 3E. The article reports "significant hallucination rate reduction through cross-verification," most pronounced in professional knowledge and lower-order thinking domains.

> "If we simultaneously use 2 models (Baichuan+ ChatGPT) to take a medical examination, adopting the LLMs' answer when they agree and resorting to human judgment when they disagree, we could potentially achieve an accuracy rate of 94.17%. Moreover, using the same approach with three models (Baichuan+ChatGPT+ERNIE bot) could further improve accuracy to 96.33%."

## Discussion


## Related Claims
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
