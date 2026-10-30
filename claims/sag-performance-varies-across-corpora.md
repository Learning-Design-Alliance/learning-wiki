---
type: claim
title: SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets
description: SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets
id: sag-performance-varies-across-corpora
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

# SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the same model architecture and language model, prediction performance varies widely across German corpora (F-Score 59.8 to 72.1 in unseen-question evaluation). [→ Ulrike Padó 2024](#ulrike-pado-2024)

## Evidence

### Ulrike Padó 2024

Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w

`q2 · i?` · `design · r2`

Same-corpus evaluation experiments across the four German SAG corpora show a spread in weighted F-Score from 59.8 (ASAP-DE) to 72.1 (CREG) under identical architecture, supporting the claim that "prediction performance can vary quite widely across corpora" and cannot be reliably predicted from benchmarks.

> "Second, we see clearly that for the same machine learning model architecture and underlying language model, prediction performance can vary quite widely across corpora."

## Discussion


## Related Claims
- [Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English](german-english-fscore-comparable.md) — related
- [A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation](german-transformer-sag-approximates-feature-models.md) — related
- [The predictive value of grade 3 screening benchmarks for MCAS ELA proficiency varies widely: 15 to 69 percent of students classified as on track did not reach MCAS proficiency, and students flagged at risk rarely met proficiency](screening-predictive-value-varies-15-69-percent.md) — related
- [Science readability models trained on context-specific corpora fail to generalize to unseen test corpora in all three languages](science-ara-models-poor-generalization-unseen-corpora.md) — a narrower finding that bears on this claim
- [Supervised ML/DL Bloom question classifiers trained on one dataset drop substantially in weighted F1 when tested on unseen datasets](supervised-bloom-classifiers-degrade-cross-dataset.md) — a broader claim this one bears on
- [The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results](tokenizer-learner-language-creg-gap.md) — related
