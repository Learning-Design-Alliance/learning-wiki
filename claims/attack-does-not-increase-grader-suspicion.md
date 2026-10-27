---
type: claim
title: "The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers"
description: "The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers"
id: attack-does-not-increase-grader-suspicion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
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
    rigour: "?"
---

# The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Two one-sided Mann–Whitney U tests show experimental-group graders thought students were cheating less or as often as the control group (p = 0.031). [→ Anna Filighera 2024](#anna-filighera-2024)
`q2 i?` Graders reported intention to act on their suspicion 14 times for control answers but only 5 times for adversarial examples. [→ Anna Filighera 2024 (2)](#anna-filighera-2024-2)

## Evidence

### Anna Filighera 2024

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r2`

Two one-sided Mann–Whitney U tests on mistrust ratings from the 7-grader survey, reported in Results, testing H6 with 30 answers per group. The finding "consistent with H6" carries only a p-value (0.031); no effect size is printed.

> "We found that human graders in the experimental group generally thought the students were cheating less or as often as in the control group (  n1 = n2 = 30, U control = 576, U adv = 324, p = 0.031)."

### Anna Filighera 2024 (2)

Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2

`q2 · i?` · `causal · r?`

Descriptive counts from the conditional action question in the same survey, reported in Results: graders "reported the intention of acting 14 times" on control answers versus 5 times on adversarial examples. No statistical test is printed for this contrast.

> "In the control group, graders reported the intention of acting 14 times (N  = 120). Conversely, graders only wanted to act 5 times (N  = 90) on the adversarial examples."

## Discussion


## Related Claims
- [Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points](adjective-adverb-insertion-attack-degrades-asag-accuracy.md) — related
- [Human graders perceive answers with inserted adjectives and adverbs as less natural than unmodified student answers](manipulated-answers-perceived-less-natural.md) — related
- [Successful attack adjectives and adverbs mostly appear more often in correct than incorrect training answers, supporting the spurious-correlation explanation for most, but not all, insertion words](successful-insertion-words-correlate-with-correct-answers.md) — related
- [Graders' mistrust correlates negatively with naturalness and correctness in the control group, but these correlations weaken sharply for adversarially modified answers](mistrust-correlates-with-poor-writing-absent-other-clues.md) — related
