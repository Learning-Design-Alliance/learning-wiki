---
type: claim
title: Neither ChatGPT nor BingChat can reliably answer physics questions at the high application level
description: Neither ChatGPT nor BingChat can reliably answer physics questions at the high application level
id: llms-fail-high-application-physics-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: xuan-quy-dao-2023
    resource: "https://doi.org/10.48550/arXiv.2306.04538"
    title: "Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo. (2023). Evaluation of ChatGPT and Microsoft Bing AI Chat Performances on Physics Exams of Vietnamese National High School Graduation Examination. arXiv preprint. [doi:10.48550/arXiv.2306.04538](https://doi.org/10.48550/arXiv.2306.04538)"
    author: Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: xuan-quy-dao-2023-2
    resource: "https://doi.org/10.48550/arXiv.2306.04538"
    title: "Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo. (2023). Evaluation of ChatGPT and Microsoft Bing AI Chat Performances on Physics Exams of Vietnamese National High School Graduation Examination. arXiv preprint. [doi:10.48550/arXiv.2306.04538](https://doi.org/10.48550/arXiv.2306.04538)"
    author: Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Neither ChatGPT nor BingChat can reliably answer physics questions at the high application level

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Accuracy on VNHSGE physics questions falls below 50% for the hardest final questions: ChatGPT exceeds 50% for questions 1–32 but drops below 50% for questions 33–40, and the models struggle at high application level. [→ Xuan-Quy Dao 2023](#xuan-quy-dao-2023)
`q2 i?` In worked sample cases, both models failed the application-level question requiring multiple reasoning steps, though ChatGPT answered one high-application question correctly in a special case. [→ Xuan-Quy Dao 2023 (2)](#xuan-quy-dao-2023-2)

## Evidence

### Xuan-Quy Dao 2023

Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo. (2023). Evaluation of ChatGPT and Microsoft Bing AI Chat Performances on Physics Exams of Vietnamese National High School Graduation Examination. arXiv preprint. [doi:10.48550/arXiv.2306.04538](https://doi.org/10.48550/arXiv.2306.04538)

`q2 · i?` · `design · r2`

Five-year average correctness by question order (Fig. 2, Table I) on 200 multiple-choice VNHSGE physics questions, ordered by difficulty. The article reports ChatGPT "has an accuracy rate of over 50 % for questions 1-32 but falls below 50 % for questions 33-40" and that Min's accuracy drops to almost 0% from question 32 onwards.

> "ChatGPT has an accuracy rate of over 50 % for questions 1-32 but falls below 50 % for questions 33-40."

### Xuan-Quy Dao 2023 (2)

Xuan-Quy Dao, Ngoc-Bich Le, Xuan-Dung Phan, Bac-Bien Ngo, The-Duy Vo. (2023). Evaluation of ChatGPT and Microsoft Bing AI Chat Performances on Physics Exams of Vietnamese National High School Graduation Examination. arXiv preprint. [doi:10.48550/arXiv.2306.04538](https://doi.org/10.48550/arXiv.2306.04538)

`q2 · i?` · `design · r2`

Qualitative analysis of model responses to sample questions at four difficulty levels (Section IV.A). Both models solved the knowledge and comprehension samples but "were unable to come up with an answer for the application-level question"; BingChat also declined a high-application question needing image information while ChatGPT answered it correctly.

> "Both ChatGPT and BingChat were unable to come up with an answer for the application-level question, which necessitates comprehensive knowledge for determining the right response."

## Discussion


## Related Claims
- [ChatGPT and BingChat perform worse than Vietnamese students on high school physics graduation exams](chatgpt-bingchat-below-vietnamese-students-physics-exams.md) — related
- [ChatGPT scored 61% on VNHSGE physics, within the 30–66% range OpenAI reported for GPT-3.5 on AP Physics](chatgpt-vnhsge-within-ap-physics-range.md) — related
- [BingChat achieved higher accuracy than ChatGPT on VNHSGE physics, but ChatGPT was more consistent](bingchat-higher-accuracy-chatgpt-more-consistent.md) — related
- [The best-case combination of ChatGPT and BingChat (Max) outperformed both individual LLMs and Vietnamese students' average score](max-combination-beats-llms-and-student-average.md) — related
- [BingChat outperforms ChatGPT on the VNHSGE in all subjects except literature](bingchat-beats-chatgpt-vnhsge-except-literature.md) — related
- [BingChat matches ChatGPT in the natural combination and exceeds it in the social combination](bingchat-combination-scores-social-superior.md) — related
- [ChatGPT outperforms BingChat specifically in literature on the VNHSGE](chatgpt-outperforms-bingchat-literature.md) — related
