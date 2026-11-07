---
type: claim
title: "Language input affects accuracy: English input yields higher NCLEX-RN accuracy, while NNLE results show no significant language difference for ChatGPT 4.0"
description: "Language input affects accuracy: English input yields higher NCLEX-RN accuracy, while NNLE results show no significant language difference for ChatGPT 4.0"
id: language-input-effect-llm-nursing-mcq-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: mixed
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: wu-zelin-2024
    resource: "https://doi.org/10.2196/52746"
    title: "Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi. (2024). Performance of ChatGPT on Nursing Licensure Examinations in the United States and China: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/52746"
    author: Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: wu-zelin-2024-2
    resource: "https://doi.org/10.2196/52746"
    title: "Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi. (2024). Performance of ChatGPT on Nursing Licensure Examinations in the United States and China: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/52746"
    author: Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Language input affects accuracy: English input yields higher NCLEX-RN accuracy, while NNLE results show no significant language difference for ChatGPT 4.0

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For NCLEX-RN MCQs, original English input was significantly more accurate than Chinese-translated input for both ChatGPT 4.0 (P=.03) and ChatGPT 3.5 (P=.02). [→ Wu Zelin 2024](#wu-zelin-2024)
`q2 i?` For NNLE MCQs, ChatGPT 4.0 showed no statistically significant difference between original Chinese and translated English input (theoretical P=.92; practical P=.77), though ChatGPT 3.5's English input was significantly more accurate on practical MCQs (P=.02). [→ Wu Zelin 2024 (2)](#wu-zelin-2024-2)

## Evidence

### Wu Zelin 2024

Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi. (2024). Performance of ChatGPT on Nursing Licensure Examinations in the United States and China: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/52746

`q2 · i?` · `causal · r1`

Cross-language comparison in which ChatGPT 3.5 translated NCLEX-RN MCQs into Chinese before input. The article reports English input accuracy "statistically significantly higher than that of inputs translated into Chinese" for both models (ChatGPT 4.0: 88.7% vs 79.3%).

> "the accuracy of inputs in the original English version was statistically significantly higher than that of inputs translated into Chinese for both ChatGPT 4.0 (P=.03) and ChatGPT 3.5 (P=.02)"

### Wu Zelin 2024 (2)

Wu Zelin, Gan Wenyi, Xue Zhaowen, Ni Zhengxin, Zheng Xiaofei, Zhang Yiyi. (2024). Performance of ChatGPT on Nursing Licensure Examinations in the United States and China: Cross-Sectional Study. JMIR Medical Education. https://doi.org/10.2196/52746

`q2 · i?` · `associational · r2`

Cross-language comparison for NNLE MCQs translated from Chinese to English. The article reports no significant difference for ChatGPT 4.0 (theoretical P=.92; practical P=.77), but ChatGPT 3.5's English input was significantly more accurate on practical MCQs (P=.02).

> "The difference was not statistically significant between the accuracy of inputs in the original Chinese version and the inputs of the translated English version for both ChatGPT 4.0 (P=.92) and ChatGPT 3.5 (P=.58) when processing NNLE Theoretical MCQs"

## Discussion


## Related Claims
- [On English-translated NNLE MCQs, ChatGPT 4.0 significantly outperformed ChatGPT 3.5 and Google Bard on theoretical questions, but not ChatGPT 3.5 on practical questions](chatgpt-4-english-translated-nnle-performance.md) — related
- [ChatGPT 4.0 significantly outperforms ChatGPT 3.5 and Google Bard in accuracy on English NCLEX-RN practice MCQs](chatgpt-4-highest-accuracy-english-nclex-rn-mcqs.md) — related
- [LLM accuracy does not differ significantly across question languages, ranging from 62% in Polish to 77% in German](llm-accuracy-language-differences-nonsignificant.md) — related
- [Translating non-English examination questions into English improved GPT-3.5's performance but had limited effect on GPT-4](english-translation-improves-gpt35-not-gpt4.md) — related
