---
type: claim
title: Character-level embeddings increase robustness to student misspellings, but spelling correction as pre-processing was found more effective
description: Character-level embeddings increase robustness to student misspellings, but spelling correction as pre-processing was found more effective
id: character-embeddings-misspelling-robustness-mixed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: mixed
newest_evidence: 2023
sources:
  - id: xiaoyu-bai-manfred-stede-2023
    resource: "https://doi.org/10.1007/s40593-022-00323-0"
    title: "Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0"
    author: Xiaoyu Bai · Manfred Stede
    q: 2
    i: "?"
    kind: review
    rigour: 2
  - id: xiaoyu-bai-manfred-stede-2023-2
    resource: "https://doi.org/10.1007/s40593-022-00323-0"
    title: "Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0"
    author: Xiaoyu Bai · Manfred Stede
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# Character-level embeddings increase robustness to student misspellings, but spelling correction as pre-processing was found more effective

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · review `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Models incorporating character embeddings have been shown to be more robust against spelling errors in students' texts (Horbach et al., 2017). [→ Xiaoyu Bai · Manfred Stede 2023](#xiaoyu-bai-manfred-stede-2023)
`q2 i?` Riordan et al. (2019) found character-level information showed positive effects but was not as effective as performing spelling correction on the training data as a pre-processing step. [→ Xiaoyu Bai · Manfred Stede 2023 (2)](#xiaoyu-bai-manfred-stede-2023-2)

## Evidence

### Xiaoyu Bai · Manfred Stede 2023

Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0

`q2 · i?` · `review · r2`

The survey reports, citing Horbach et al. (2017), that character embeddings capture the relatedness between a word and its misspelled counterpart because they share many substrings. No effect size is printed.

> "models incorporating character embeddings have been shown to be more robust against spelling errors in students' texts (Horbach et al., 2017)"

### Xiaoyu Bai · Manfred Stede 2023 (2)

Xiaoyu Bai · Manfred Stede. (2023). A Survey of Current Machine Learning Approaches to Student Free-Text Evaluation for Intelligent Tutoring. International Journal of Artificial Intelligence in Education (2023) 33:994–1032. https://doi.org/10.1007/s40593-022-00323-0

`q2 · i?` · `review · r2`

The survey reports Riordan et al. (2019)'s GRU-based short-answer scoring studies with character-level information; the survey states the benefits of character-level embeddings for misspellings are inconclusive. No effect size is printed.

> "Riordan et al. ( 2019) found in their studies that while they did show positive effects, they were not as effective as performing spelling correction on the training data as a pre-processing step."

## Discussion


## Related Claims
- [Spellcheck and autocorrect are not foolproof: efficacy is bounded near 80% and the most common student writing error is now correctly spelled but inappropriate words](spellcheck-not-foolproof-wrong-word-errors.md) — related
- [Holistic scoring of German university students' essays posed significant challenges to both a neural model and an SVM with n-gram features](german-essay-scoring-challenges-both-models.md) — related
