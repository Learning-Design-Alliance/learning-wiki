---
type: claim
title: Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words
description: Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words
id: successful-insertion-words-correlate-with-correct-answers
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
  - id: anna-filighera-2024-2
    resource: "https://doi.org/10.1007/s40593-023-00361-2"
    title: "Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2"
    author: Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correct SciEntsBank training answers average more adjectives and adverbs per answer than incorrect ones, and the most successful insertion words were either much more common in correct responses or rare in the training set. [→ Anna Filighera 2024](#anna-filighera-2024)
`q2 i?` One exception exists: the adjective 'better' occurred 15 times in incorrect responses and only 4 times in correct answers, so the evidence supports the spurious-correlation account only for most adjectives and adverbs. [→ Anna Filighera 2024 (2)](#anna-filighera-2024-2)

## Evidence

### Anna Filighera 2024

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Descriptive analysis of adjective and adverb distribution in the SciEntsBank training data, reported in the Results section. Correct answers average "more adjectives (1.1) and adverbs (0.6) per answer than incorrect ones (0.8 and 0.5, respectively)"; the dataset holds 2462 incorrect and 2008 correct responses.

> "Correct answers also average more adjectives (1.1) and adverbs (0.6) per answer than incorrect ones (0.8 and 0.5, respectively)."

### Anna Filighera 2024 (2)

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Occurrence analysis of the 10 most successful adjectives and adverbs per class in the SciEntsBank training set (Fig. 4), reported in Results. The counterexample 'better' shows the spurious-correlation account does not hold for every successful insertion word.

> "Only one of the most successful insertion words appeared notably more often in incorrect student responses. The adjective “better” occurred 15 times in incorrect responses and only 4 times in correct answers. Thus, we conclude that our evidence supports E2 for most adjectives and adverbs, but not all."

## Discussion


## Related Claims
- [Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points](adjective-adverb-insertion-attack-degrades-asag-accuracy.md) — related
- [The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers](attack-does-not-increase-grader-suspicion.md) — related
- [The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65](attack-succeeds-on-low-confidence-predictions.md) — related
- [The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent](insertion-attack-vs-textfooler-dataset-dependent.md) — related
- [Graders' mistrust correlates negatively with naturalness and correctness in the control group, but these correlations weaken sharply for adversarially modified answers](mistrust-correlates-with-poor-writing-absent-other-clues.md) — related
