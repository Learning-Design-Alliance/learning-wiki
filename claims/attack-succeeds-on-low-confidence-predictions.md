---
type: claim
title: The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65
description: The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65
id: attack-succeeds-on-low-confidence-predictions
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

# The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Soon-to-be adversarial examples elicit lower model confidence before the attack than most predictions, and after the attack the model assigns similar confidence levels to the target (correct) class. [→ Anna Filighera 2024](#anna-filighera-2024)

## Evidence

### Anna Filighera 2024

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Analysis of BERT softmax confidence scores before and after adversarial insertion, plotted in Fig. 5 and reported in Results. Most test answers score 0.8 to 1 while soon-to-be adversarial examples score between 0.45 and 0.65, which the authors state is in line with their expectation E3.

> "Most test answers are classified with a confidence score between 0.8 and 1, while the model estimates most soon-to-be adversarial examples to be incorrect with a probability between 0.45 and 0.65. Since we have three classes in the dataset, a class needs at least a probability of 0.33 to be selected."

## Discussion


## Related Claims
- [Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points](adjective-adverb-insertion-attack-degrades-asag-accuracy.md) — related
- [Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words](successful-insertion-words-correlate-with-correct-answers.md) — related
- [The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent](insertion-attack-vs-textfooler-dataset-dependent.md) — related
