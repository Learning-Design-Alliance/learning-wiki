---
type: claim
title: "Feature-based MLP deep learning models predict ASAP D7 rubric scores with an average QWK of 0.72 against human raters' resolved scores, exceeding the 0.60 average agreement between the two human raters"
description: "Feature-based MLP deep learning models predict ASAP D7 rubric scores with an average QWK of 0.72 against human raters' resolved scores, exceeding the 0.60 average agreement between the two human raters"
id: aes-d7-rubric-qwk-072-exceeds-human-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: kumar-2020
    resource: "https://doi.org/10.1007/s40593-020-00211-5"
    title: "Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5"
    author: "Kumar, V. S., & Boulanger, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Feature-based MLP deep learning models predict ASAP D7 rubric scores with an average QWK of 0.72 against human raters' resolved scores, exceeding the 0.60 average agreement between the two human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Deep neural network rubric scoring models trained on ASAP D7 reached an average per-rubric QWK of 0.72 with human raters' resolved scores, above the human-human agreement of 0.60 on average. [→ Kumar 2020](#kumar-2020)

## Evidence

### Kumar 2020

Kumar, V. S., & Boulanger, D. (2020). Automated Essay Scoring and the Deep Learning Black Box: How Are Rubric Scores Determined? International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00211-5

`q2 · i?` · `design · r2`

Study of six MLP architectures trained on 1567 ASAP D7 essays (80/20 train/test split, five averaged testing iterations), each essay represented by 397 writing features. The article reports an average per-rubric QWK of "0.72 (QWK), well beyond the agreement level between the two human raters" (0.60 average).

> "In contrast, this research's findings report an average agreement level per rubric with the two human raters' resolved scores of 0.72 (QWK), well beyond the agreement level between the two human raters."

## Discussion


## Related Claims
- [The two human raters of ASAP D7 showed an average inter-rater agreement of 0.60 QWK across rubrics, with rubric-level agreements ranging from 0.46 (Ideas–Conventions) to 0.79 (Ideas–Organization)](d7-human-rater-agreement-qwk-060.md) — related
- [Among six tested MLP architectures, classifiers achieved higher exact-match accuracy on rubric scores, while regression and ensemble variants achieved higher QWK on some rubrics](aes-architecture-comparison-d7.md) — a narrower finding that bears on this claim
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — related
- [The introduction reports that deep learning and NLP techniques predicted fine-grained rubric scores of student essays with success well beyond the agreement level between two human raters](deep-learning-essay-scoring-beyond-human-rater-agreement.md) — possibly the same claim (merge candidate)
- [The proposed AES system predicts holistic essay scores through predicted rubric scores, achieving a QWK of 0.78, competitive with cutting-edge AES tools reporting 0.77–0.81](aes-holistic-qwk-078-competitive.md) — related
