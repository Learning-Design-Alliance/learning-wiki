---
type: claim
title: Most models had higher accuracy on simple questions (medical knowledge, lower-order, positive) than on complex ones, with Llama showing the reverse pattern
description: Most models had higher accuracy on simple questions (medical knowledge, lower-order, positive) than on complex ones, with Llama showing the reverse pattern
id: simple-vs-complex-question-accuracy-pattern
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

# Most models had higher accuracy on simple questions (medical knowledge, lower-order, positive) than on complex ones, with Llama showing the reverse pattern

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Six models scored higher on medical-knowledge than clinical-case-analysis questions and on lower-order than higher-order thinking questions, while Llama exhibited the opposite trend on both. [→ Yao Zhong 2025](#yao-zhong-2025)

## Evidence

### Yao Zhong 2025

Yao Zhong, Duan Liantan, Xu Shuo, Chi Lingyi, Sheng Dongfang. (2025). Performance of Large Language Models in the Non-English Context: Qualitative Study of Models Trained on Different Languages in Chinese Medical Examinations. JMIR Medical Informatics. https://doi.org/10.2196/69485

`q2 · i?` · `design · r2`

Subgroup analyses stratifying the 600 questions by format (245 medical knowledge vs 355 clinical case analysis), polarity (541 positive vs 59 negative), and Bloom's Taxonomy (298 lower-order vs 302 higher-order). The same six-model pattern held across format and Bloom strata.

> "6 LLMs (ERNIE Bot, Kimi, Baichuan, ChatGLM, Yi-large, and ChatGPT) achieved better accuracy on lower-order thinking questions than on higher-order thinking questions. Llama, however, exhibited the opposite trend, with a higher accuracy rate on higher-order thinking questions than on lower-order ones."

## Discussion


## Related Claims
- [English-corpus models performed relatively better on Chinese policies-and-ethics questions than Chinese-corpus models did](english-models-ethics-policy-subgroup-advantage.md) — related
- [LLM accuracy declines steadily as question complexity increases, from roughly 80% on recall questions to 28.6–33.3% on case-analysis questions, mirroring the human trend](llm-accuracy-declines-with-question-complexity.md) — reports the opposite
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [Case-based (vignette) MCQs are classified as testing higher-order thinking and discriminate better between low- and high-information students](case-based-questions-higher-order-value.md) — related
