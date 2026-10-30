---
type: claim
title: A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation
description: A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation
id: german-transformer-sag-approximates-feature-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: ulrike-padó-2024
    resource: "https://doi.org/10.1007/s40593-023-00383-w"
    title: "Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w"
    author: Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In leave-one-question-out evaluation on four German corpora, the German Transformer model does not beat published literature results, but approximates the hand-crafted model on CSSAG (F 65.0 vs 66.6). [→ Ulrike Padó 2024](#ulrike-pado-2024)

## Evidence

### Ulrike Padó 2024

Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w

`q2 · i?` · `design · r2`

Evaluation of the German Transformer model trained separately on four German SAG corpora (CREG, CSSAG, ASAP-DE, SAF-DE) with leave-one-question-out 'unseen question' evaluation; weighted F-Scores are 72.1, 65.0, 59.8, and 71.7. The authors note it "approximate[s] the performance of the carefully hand-crafted model for CSSAG" but does not beat literature results.

> "It is quite clear from Table 3 that the German Transformer model does not beat the literature results. It does, however, approximate the performance of the carefully hand-crafted model for CSSAG."

## Discussion


## Related Claims
- [Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English](german-english-fscore-comparable.md) — related
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — related
- [Fine-tuned transformer DL models outperform feature-based SVM models for science readability classification across all three languages and configurations](dl-transformers-beat-svm-science-ara.md) — related
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — related
- [The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results](tokenizer-learner-language-creg-gap.md) — related
- [Where labelled training data is limited, adding hand-crafted features improves the performance of neural text evaluation models](handcrafted-features-improve-neural-low-resource.md) — related
