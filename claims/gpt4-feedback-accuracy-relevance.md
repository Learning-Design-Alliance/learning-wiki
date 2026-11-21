---
type: claim
title: Zero-shot GPT-4 generates feedback judged more accurate and relevant than GOAT and SBERT-Canberra by teacher evaluators
description: Zero-shot GPT-4 generates feedback judged more accurate and relevant than GOAT and SBERT-Canberra by teacher evaluators
id: gpt4-feedback-accuracy-relevance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: sami-baral-2024
    resource: "https://doi.org/10.48550/arXiv.2411.08910"
    title: "Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)"
    author: Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: sami-baral-2024-2
    resource: "https://doi.org/10.48550/arXiv.2411.08910"
    title: "Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)"
    author: Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Zero-shot GPT-4 generates feedback judged more accurate and relevant than GOAT and SBERT-Canberra by teacher evaluators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4 feedback reached 86% consensus accuracy versus 68% for GOAT and 52% for SBERT. [→ Sami Baral 2024](#sami-baral-2024)
`q2 i?` GPT-4 feedback reached 91% consensus relevance versus 88% for GOAT and 76% for SBERT. [→ Sami Baral 2024 (2)](#sami-baral-2024-2)

## Evidence

### Sami Baral 2024

Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)

`q2 · i?` · `design · r2`

Qualitative evaluation in which two experienced teachers rated 100 sampled test answers across 50 problems; accuracy required unanimous recognition by both evaluators, with GPT-4 at "a consensus accuracy rate of 86%".

> "In the aspect of feedback accuracy, the GPT-4 model excelled beyond the SBERT and GOAT models, achieving a consensus accuracy rate of 86% from both evaluators."

### Sami Baral 2024 (2)

Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)

`q2 · i?` · `design · r2`

Same two-teacher evaluation of 100 sampled feedback messages, rated on binary relevance to the student's answer; GPT-4 secured "a unanimous relevance score of 91%", with GOAT at 88% and SBERT at 76%.

> "GPT-4 once again outperformed the other two models, securing a unanimous relevance score of 91% from the evaluators. GOAT was closely behind with 88% relevance, nearly matching GPT-4, whereas SBERT received a lower relevance score of 76%."

## Discussion


## Related Claims
- [GPT-4 feedback was rated slightly more motivating and least demotivating, but motivational judgments were similar across models](feedback-motivation-ratings.md) — related
- [GOAT's feedback quality is limited by low-quality teacher feedback in its training data](goat-feedback-limited-by-training-data-quality.md) — related
- [The fine-tuned GOAT model outperforms SBERT-Canberra and GPT-4 in predicting teacher scores for open-ended math responses](goat-outperforms-sbert-gpt4-scoring.md) — related
- [Teachers prefer GPT-4 feedback over GOAT and SBERT-Canberra feedback by a wide margin](gpt4-preferred-feedback.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
