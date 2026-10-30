---
type: claim
title: The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent
description: The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent
id: insertion-attack-vs-textfooler-dataset-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: mixed
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

# The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the SciEntsBank ASAG test splits the insertion attack drops accuracy by an additional 0.4 to 3.8 percentage points beyond TextFooler, while TextFooler outperforms it by 2.9 to 8.1 percentage points on the other tasks. [→ Anna Filighera 2024](#anna-filighera-2024)

## Evidence

### Anna Filighera 2024

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Comparison against the state-of-the-art TextFooler attack on BERT and T5 reported in Results (Table 2). The attack "seems to be slightly more effective at dropping models’ accuracy on the ASAG task" but loses on entailment and paraphrase tasks. TextFooler also runs faster on every dataset because it uses prediction scores students would not have.

> "Even though our search is less guided, our attack seems to be slightly more effective at dropping models’ accuracy on the ASAG task, degrading the accuracy by an additional 0.4—3.8 percentage points across the SciEntsBank test splits. However, since TextFooler outperforms our attack on the other tasks (by 2.9—8.1 percentage points), we conclude that the attacks’ performance is dataset-dependent."

## Discussion


## Related Claims
- [Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points](adjective-adverb-insertion-attack-degrades-asag-accuracy.md) — related
- [Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words](successful-insertion-words-correlate-with-correct-answers.md) — related
- [The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65](attack-succeeds-on-low-confidence-predictions.md) — related
