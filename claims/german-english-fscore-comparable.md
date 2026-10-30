---
type: claim
title: "Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English"
description: "Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English"
id: german-english-fscore-comparable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
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

# Under unseen-answers evaluation, the German Transformer model's F-Scores are numerically similar to state-of-the-art Transformer results for English

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In stratified unseen-answers evaluation, German F-Scores (81.7–86.2) are numerically similar to English SemEval-2013 corpus results (83.4, 91.2). [→ Ulrike Padó 2024](#ulrike-pado-2024)

## Evidence

### Ulrike Padó 2024

Ulrike Padó, Yunus Eryilmaz, Larissa Kirschner. (2024). Short-Answer Grading for German: Addressing the Challenges. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-023-00383-w

`q2 · i?` · `design · r2`

Cross-language comparison using a fixed train-test split stratified by question (unseen answers), an easier task than unseen questions. German F-Scores range from 81.7 (CREG) to 86.2 (ASAP-DE, SAF-DE); English albert-large results are 83.4 (SciEntsBank) and 91.2 (Beetle). The authors state this "indicates" rather than proves comparability.

> "Table 5 does demonstrate, though, that evaluation results for our German Transformer model in terms of F-Score are numerically similar to state-of-the-art Transformer results for the SemEval-2013 English standard corpora"

## Discussion


## Related Claims
- [A fine-tuned SBERT Transformer SAG model for German approximates but does not beat hand-crafted feature-based models in unseen-question evaluation](german-transformer-sag-approximates-feature-models.md) — related
- [SAG model prediction performance varies widely across corpora even with the same architecture, so benchmark results cannot predict performance on new data sets](sag-performance-varies-across-corpora.md) — related
- [Fine-tuned LaBSE achieves about 86.5% accuracy classifying all answers as correct or incorrect on a large multilingual dataset](finetuned-labse-86-5-percent-autograding-accuracy.md) — related
- [The German Transformer model's tokenization handles native-speaker morphology well but struggles with learner-language errors, possibly explaining lower CREG results](tokenizer-learner-language-creg-gap.md) — related
