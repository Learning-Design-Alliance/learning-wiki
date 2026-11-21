---
type: claim
title: "GOAT's feedback quality is limited by low-quality teacher feedback in its training data"
description: "GOAT's feedback quality is limited by low-quality teacher feedback in its training data"
id: goat-feedback-limited-by-training-data-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: sami-baral-2024
    resource: "https://doi.org/10.48550/arXiv.2411.08910"
    title: "Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)"
    author: Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# GOAT's feedback quality is limited by low-quality teacher feedback in its training data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Training on inaccurate, irrelevant, and demotivating teacher feedback caused GOAT to reproduce unhelpful feedback patterns. [→ Sami Baral 2024](#sami-baral-2024)

## Evidence

### Sami Baral 2024

Sami Baral, Eamon Worden, Wen-Chiang Lim, Zhuang Luo, Christopher Santorelli, Ashish Gurung, Neil Heffernan. (2024). Automated Feedback in Math Education: A Comparative Analysis of LLMs for Open-Ended Responses. arXiv. [doi:10.48550/arXiv.2411.08910](https://doi.org/10.48550/arXiv.2411.08910)

`q1 · i?` · `design · r2`

Authors' interpretation in the limitations section, not a tested result: teacher time constraints produced vague, generic, or merely corrective feedback, and GOAT mimicked it, "captur[ing] aspects of teacher feedback that are not as meaningful".

> "By training on inaccurate, irrelevant, demotivating, and low-quality feedback messages, the GOAT model captures aspects of teacher feedback that are not as meaningful."

## Discussion


## Related Claims
- [GPT-4 feedback was rated slightly more motivating and least demotivating, but motivational judgments were similar across models](feedback-motivation-ratings.md) — related
- [Teachers prefer GPT-4 feedback over GOAT and SBERT-Canberra feedback by a wide margin](gpt4-preferred-feedback.md) — related
- [Zero-shot GPT-4 generates feedback judged more accurate and relevant than GOAT and SBERT-Canberra by teacher evaluators](gpt4-feedback-accuracy-relevance.md) — related
- [The fine-tuned GOAT model outperforms SBERT-Canberra and GPT-4 in predicting teacher scores for open-ended math responses](goat-outperforms-sbert-gpt4-scoring.md) — related
- [Teacher evaluators disagreed on what counts as demotivating feedback, with differences attributed to cultural and teaching backgrounds](rater-disagreement-demotivating-feedback.md) — related
