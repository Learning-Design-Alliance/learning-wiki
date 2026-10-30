---
type: claim
title: "Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points"
description: "Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points"
id: adjective-adverb-insertion-attack-degrades-asag-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: anna-filighera-2024
    resource: "https://doi.org/10.1007/s40593-023-00361-2"
    title: "Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2"
    author: Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all models and datasets, the adjective/adverb insertion attack deteriorates model accuracy by 8 to 22 percentage points. [→ Anna Filighera 2024](#anna-filighera-2024)

## Evidence

### Anna Filighera 2024

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Attack experiments on BERT and T5 across SciEntsBank (UA, UQ, UD) and GLUE/SuperGLUE entailment and paraphrase datasets, reported in the Results section (Table 2). The article states "our attack deteriorates a model’s accuracy by 8 to 22 percentage points" across all tested models and datasets.

> "Across all models and datasets, our attack deteriorates a model’s accuracy by 8 to 22 percentage points."

## Discussion


## Related Claims
- [The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent](insertion-attack-vs-textfooler-dataset-dependent.md) — related
- [Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words](successful-insertion-words-correlate-with-correct-answers.md) — related
- [The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65](attack-succeeds-on-low-confidence-predictions.md) — related
- [Human graders perceive answers with inserted adjectives and adverbs as less natural than unmodified student answers](manipulated-answers-perceived-less-natural.md) — related
- [The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers](attack-does-not-increase-grader-suspicion.md) — related
