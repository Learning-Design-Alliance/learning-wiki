---
type: claim
title: "Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation"
description: "Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation"
id: attribution-analysis-identifies-bert-classification-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: wulff-2023
    resource: "https://doi.org/10.1007/s40593-022-00290-6"
    title: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6"
    author: "Wulff, P., Mientus, L., Nowak, A., & Borowski, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Attribution analysis identifies interpretable input features for BERT's classification decisions, including subjunctive verbs in alternatives and appraisal words in evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Layer-integrated gradients assigned attribution scores to input tokens, revealing interpretable features such as subjunctive verb modes in alternatives and appraisal words like "good" in evaluation. [→ Wulff 2023](#wulff-2023)

## Evidence

### Wulff 2023

Wulff, P., Mientus, L., Nowak, A., & Borowski, A. (2023). Utilizing a Pretrained Language Model (BERT) to Classify Preservice Physics Teachers' Written Reflections. International Journal of Artificial Intelligence in Education, 33, 439–466. https://doi.org/10.1007/s40593-022-00290-6

`q2 · i?` · `design · r2`

Layer-integrated gradients were calculated for all test-data inputs, averaging attributions across embedding dimensions for correctly classified segments. Table 3 reports the highest-attribution nouns, verbs and adjectives per element; the authors note "the subjunctive mode of verbs in alternatives" and appraisal words in evaluation.

> "Note, for example, the subjunctive mode of verbs in alternatives. Furthermore, there are words of appraisal such as "good" in evaluation. Also the nouns in circumstances are somewhat prototypical of that element given that the preservice teachers were meant to describe the "class", state their "goals", and characterize the "lesson"."

## Discussion


## Related Claims
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [LLMs show robust zero- and few-shot Bloom classification of OOD AI-assisted questions compared with ML and BERT models](llms-robust-ood-bloom-classification.md) — related
- [Feature-based ML Bloom classifiers trained on IID data degrade sharply on out-of-distribution AI-assisted questions](ml-bloom-classifiers-degrade-ood-aeq.md) — related
