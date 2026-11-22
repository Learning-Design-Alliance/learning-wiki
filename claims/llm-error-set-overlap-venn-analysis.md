---
type: claim
title: "Error-set overlap analysis found 16 questions all six passing models answered incorrectly, and ChatGPT's error profile resembled the Chinese models'"
description: "Error-set overlap analysis found 16 questions all six passing models answered incorrectly, and ChatGPT's error profile resembled the Chinese models'"
id: llm-error-set-overlap-venn-analysis
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

# Error-set overlap analysis found 16 questions all six passing models answered incorrectly, and ChatGPT's error profile resembled the Chinese models'

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Venn analysis of the six consistent models' error sets identified 16 common incorrect questions, with unique error counts of 15 (ChatGPT), 12 (ERNIE Bot), 25 (Kimi), 6 (Baichuan), 10 (ChatGLM), and 44 (Yi-large). [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Error-set analysis compiling each model's incorrectly answered CNMLE questions and visualizing intersections with a Venn diagram. The article reports the printed unique-error counts and that 3 of the 16 common errors showed identical incorrect selections across all 6 models.

> "Figure 3A demonstrates that there were 16 common incorrect questions that all LLMs answered incorrectly. Within ChatGPT's error set, there were 15 unique incorrect questions that were answered incorrectly by ChatGPT alone, despite being correctly addressed by the other models."

## Discussion


## Related Claims
- [Ten JNEOT questions were answered incorrectly by all four LLMs, six of them visually-based](ten-questions-incorrect-by-all-llms.md) — related
- [ChatGPT 4.0 had the most uniquely correct and fewest uniquely incorrect responses among the three LLMs across both languages](chatgpt-4-most-unique-correct-responses-venn.md) — related
- [Performance gaps between English- and Chinese-trained LLMs are attributed to training-data composition rather than language communication barriers](training-data-composition-not-language-barriers.md) — related
