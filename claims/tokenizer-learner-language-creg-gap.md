---
type: claim
title: "The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results"
description: "The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results"
id: tokenizer-learner-language-creg-gap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
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

# The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Tokenization analysis shows word representations reminiscent of German lemmatization for native-speaker text, while learner errors such as missing capitalization and misspellings cause unfounded token splits. [→ Ulrike Padó 2024](#ulrike-pado-2024)

## Evidence

### Ulrike Padó 2024

Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w

`q2 · i?` · `design · r2`

Qualitative analysis of WordPiece tokenizations (Table 4) of native-speaker CSSAG text and learner CREG text. Tokens mostly correspond to morphemes for native text, but missing capitalization of Kenntnis and the misspelling in österreichische produce "a complete, but linguistically unfounded representation", which "may explain" the CREG gap.

> "These observations may explain why the German Transformer model so clearly stays below the literature results for the learner data in CREG."

## Discussion


## Related Claims
- [Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English](german-english-fscore-comparable.md) — related
- [A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation](german-transformer-sag-approximates-feature-models.md) — related
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — related
