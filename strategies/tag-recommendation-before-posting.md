---
type: strategy
id: tag-recommendation-before-posting
title: "Use tag recommendation before question posting to increase learners' chances of getting answers"
description: The article recommends that tag recommendation methods like BERT-CBA be deployed to suggest appropriate tags to learners before they post questions on Stack Overflow.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: olatinwo-2025
    resource: "https://doi.org/10.1007/s40593-024-00441-x"
    title: "Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x"
    author: "Olatinwo, S. O., & Demmans Epp, C"
---

# Use tag recommendation before question posting to increase learners' chances of getting answers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 8 claims (5 for, 3 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 8 claims rest on one study

## Description
The article recommends that tag recommendation methods like BERT-CBA be deployed to suggest appropriate tags to learners before they post questions on Stack Overflow. Because inappropriate tags prevent experts who subscribe to relevant tags from seeing questions, pre-posting recommendations could increase question visibility and answer rates. The article suggests SO "could use a tag recommendation engine to help learners choose suitable tags for their questions before posting them."

## Design Implications

### Context
#### Requirements
- A trained tag recommendation model with acceptable precision and recall
- Integration into the question posting workflow
#### Constraints
- BERT-based models have slower response times (around 12 seconds during cross-validation, 5–6 seconds on test data) than linear methods like MNB and SVM (1 second)

### Target Learners
- Novice question askers on Stack Overflow
- Computer-science learners seeking help online

### Target Learning Goals
- Connecting learner questions with experts who can answer them
- Supporting lifelong learning through answered questions

### Affordances
- Bert Cba Architecture

## Claims

- [BERT-CBA outperformed BERT-FFNN by 6–15% on Precision@K, with t(5) = 6.56, p = .001, d = 4.64](../claims/bert-cba-beats-bert-ffnn.md) [+W]
- [BERT-CBA outperformed BERT-LSTM by 4–9% and BERT-GRU by 2–10% on F1@K](../claims/bert-cba-beats-lstm-gru.md) [+W]
- [BERT-CBA outperformed MNB by 40–73% across metrics, with t(5) = 5.55, p = .002, d = 10.20 for precision](../claims/bert-cba-beats-mnb-40-73-percent.md) [+W]
- [BERT-CBA outperformed SVM by 44–73% on Precision@K, with t(5) = 5.62, p = .002, d = 7.13](../claims/bert-cba-beats-svm-precision.md) [+W]
- [BERT-CBA outperformed baseline tag recommendation methods on Precision@K, Recall@K, and F1@K under cross-validation](../claims/bert-cba-outperforms-baselines-cross-validation.md) [+W]
- [Error analysis showed the model failed to predict the \"Java\" tag when question wording emphasized \"Android\" and \"React Native\"](../claims/error-analysis-java-tag-miss.md) [~W]
- [F1@K decreased as K increased for all methods](../claims/f1-decreases-with-k.md) [~W]
- [The highway layer ablation showed no measurable performance difference between BERT-CBA variants](../claims/highway-layer-ablation-null-result.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Olatinwo, S. O., & Demmans Epp, C. (2025). Predicting Tags for Learner Questions on Stack Overflow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00441-x
