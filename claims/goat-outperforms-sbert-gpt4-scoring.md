---
type: claim
title: The fine-tuned GOAT model outperforms SBERT-Canberra and GPT-4 in predicting teacher scores for open-ended math responses
description: The fine-tuned GOAT model outperforms SBERT-Canberra and GPT-4 in predicting teacher scores for open-ended math responses
id: goat-outperforms-sbert-gpt4-scoring
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
---

# The fine-tuned GOAT model outperforms SBERT-Canberra and GPT-4 in predicting teacher scores for open-ended math responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GOAT achieved the best AUC (0.7), RMSE (1.119), and Kappa (0.422) of the three models on the scoring task. [→ Sami Baral 2024](#sami-baral-2024)

## Evidence

### Sami Baral 2024

Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)

`q2 · i?` · `design · r2`

Scoring evaluation on 1,000 held-out test entries from 50 open-response problems; models compared against teacher-assigned 0-4 scores using AUC, RMSE, and multi-class Cohen's Kappa. GOAT led on all three metrics, with a "Kappa score of 0.422".

> "Furthermore, it showed a Root Mean Square Error (RMSE) of 1.119, reflecting its precision in predicting numerical scores, and a Kappa score of 0.422, showcasing 42% agreement with teacher-provided scores beyond chance."

## Discussion


## Related Claims
- [Zero-shot GPT-4 generates feedback judged more accurate and relevant than GOAT and SBERT-Canberra by teacher evaluators](gpt4-feedback-accuracy-relevance.md) — related
- [Teachers prefer GPT-4 feedback over GOAT and SBERT-Canberra feedback by a wide margin](gpt4-preferred-feedback.md) — related
- [GPT-4 feedback was rated slightly more motivating and least demotivating, but motivational judgments were similar across models](feedback-motivation-ratings.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [GOAT's feedback quality is limited by low-quality teacher feedback in its training data](goat-feedback-limited-by-training-data-quality.md) — related
