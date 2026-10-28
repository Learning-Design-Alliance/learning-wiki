---
type: strategy
id: recommendations-safer-asag-deployment
title: Recommendations for using automatic grading systems more securely in practice
description: "Based on their attack experiments, human evaluation, and brittleness analysis, the authors formulate recommendations for deploying automatic grading systems more securely, stating \"we provide recommendations for utili..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: anna-filighera-2024
    resource: "https://doi.org/10.1007/s40593-023-00361-2"
    title: "Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2"
    author: Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel
---

# Recommendations for using automatic grading systems more securely in practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
Based on their attack experiments, human evaluation, and brittleness analysis, the authors formulate recommendations for deploying automatic grading systems more securely, stating "we provide recommendations for utilizing automatic grading systems more safely in practice". The recommendations rest on the demonstrated vulnerability of transformer graders to adjective and adverb insertion and on the finding that human graders detect the manipulation poorly.

## Design Implications

### Context
#### Requirements
- Educators deploying automatic short answer grading should account for models' use of spurious correlations between adjective and adverb usage and answer correctness, as the article demonstrates this brittleness empirically.
#### Constraints
- The attack underlying these recommendations is suited for academic disciplines where the factual correctness of responses is essential and may be unsuited to language learning scenarios where linguistic expression is vital.

### Target Learners
- primary and middle school students assessed via short answer questions
- university students in courses using automatic short answer grading

### Target Learning Goals
- accurate assessment of constructed-response answers
- prevention of academic dishonesty in automatically graded assessments

## Claims

- [Inserting common adjectives and adverbs into incorrect student answers reduces BERT's and T5's ASAG accuracy by 8 to 22 percentage points](../claims/adjective-adverb-insertion-attack-degrades-asag-accuracy.md) [+W]
- [The attack does not increase graders' suspicion of cheating; graders even intended to act on manipulated answers less often than on control answers](../claims/attack-does-not-increase-grader-suspicion.md) [+W]
- [The insertion attack succeeds primarily on low-confidence predictions, where soon-to-be adversarial examples receive probabilities between roughly 0.45 and 0.65](../claims/attack-succeeds-on-low-confidence-predictions.md) [+W]
- [The insertion attack slightly outperforms TextFooler on ASAG but is outperformed by TextFooler on entailment and paraphrase tasks, making attack performance dataset-dependent](../claims/insertion-attack-vs-textfooler-dataset-dependent.md) [+W]
- [Human graders perceive answers with inserted adjectives and adverbs as less natural than unmodified student answers](../claims/manipulated-answers-perceived-less-natural.md) [+W]
- [Graders' mistrust correlates negatively with naturalness and correctness in the control group, but these correlations weaken sharply for adversarially modified answers](../claims/mistrust-correlates-with-poor-writing-absent-other-clues.md) [+W]

## Related Strategies

- [Protect AI-mediated assessment through isolated environments, clear guidelines, resilience assessments, and teaching prompt-processing awareness](protect-ai-grading-from-prompt-injection-strategies.md)

## Examples
-

## Key Sources
- Anna Filighera, Sebastian Ochs, Tim Steuer, Thomas Tregel. (2024). Cheating Automatic Short Answer Grading with the Adversarial Usage of Adjectives and Adverbs. International Journal of Artificial Intelligence in Education, 34, 616–646. https://doi.org/10.1007/s40593-023-00361-2
