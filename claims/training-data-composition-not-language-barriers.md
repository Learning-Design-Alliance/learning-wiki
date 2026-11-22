---
type: claim
title: Performance gaps between English- and Chinese-trained LLMs are attributed to training-data composition rather than language communication barriers
description: Performance gaps between English- and Chinese-trained LLMs are attributed to training-data composition rather than language communication barriers
id: training-data-composition-not-language-barriers
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

# Performance gaps between English- and Chinese-trained LLMs are attributed to training-data composition rather than language communication barriers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The article concludes that ChatGPT's performance gap versus Chinese LLMs in the CNMLE is not primarily due to communication barriers but to limited representation of Chinese corpora in training datasets. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Authors' interpretation in the Discussion, supported by their finding and prior cross-language studies showing no significant difference when questions are translated into English versus asked directly in Chinese. The disparity also includes content differences such as epidemiology, traditional Chinese medicine, policy, and ethics.

> "This suggests that the performance gap in Chinese contexts is not primarily due to communication barriers but is more likely attributable to the limited representation of Chinese corpora in the training datasets."

## Discussion


## Related Claims
- [Six of seven LLMs exceeded the CNMLE passing threshold under zero-shot settings, with Chinese-corpus model Baichuan achieving the highest accuracy (86.67%)](llm-cnmle-zero-shot-accuracy-baichuan-highest.md) — related
- [Error-set overlap analysis found 16 questions all six passing models answered incorrectly, and ChatGPT's error profile resembled the Chinese models'](llm-error-set-overlap-venn-analysis.md) — related
- [ChatGPT-4o showed a language-related performance gap, performing better on English than Chinese questions while humans showed the reverse pattern](chatgpt-4o-language-performance-gap-english-chinese.md) — reports the opposite
