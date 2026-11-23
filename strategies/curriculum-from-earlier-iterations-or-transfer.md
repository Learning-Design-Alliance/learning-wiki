---
type: strategy
id: curriculum-from-earlier-iterations-or-transfer
title: Use earlier model iterations or a stronger transfer-learning model to generate a curriculum for a weaker learner
description: "Since the optimal hypothesis needed for the Ideal Difficulty Score is unknown in practice, the article recommends exploiting scenarios with sequences of model improvement: results from earlier iterations can generate..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: daphna-weinshall-and-dan-amir-2018
    resource: "https://arxiv.org/abs/1812.03472"
    title: "Daphna Weinshall and Dan Amir. (2018). Theory of Curriculum Learning, with Convex Loss Functions. arXiv preprint. https://arxiv.org/abs/1812.03472"
    author: Daphna Weinshall and Dan Amir
---

# Use earlier model iterations or a stronger transfer-learning model to generate a curriculum for a weaker learner

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Since the optimal hypothesis needed for the Ideal Difficulty Score is unknown in practice, the article recommends exploiting scenarios with sequences of model improvement: results from earlier iterations can generate a curriculum for subsequent iterations, or a stronger learner's difficulty scores can be transferred to train a weaker learner. The article states: "results from earlier iterations can be used to generate a curriculum for subsequent iterations. Another scenario involves transfer learning from a strong learner to a weaker learner."

## Design Implications

### Context
#### Requirements
- A setting with iterated model improvement or access to a stronger model whose difficulty scores can rank examples
#### Constraints
- The article cites Weinshall et al. (2018) for the transfer-learning result rather than demonstrating it in this paper

### Target Learners
- machine learning models, including weaker models trained via transfer from stronger models

### Target Learning Goals
- faster training and better final solutions for the weaker learner

### Affordances
- Ideal Difficulty Score Global Local

## Related Strategies

- [Use higher-aligned curricula as practical models for targeted AMS curriculum revision across professions](high-alignment-curricula-as-revision-models.md)

## Examples
-

## Key Sources
- Daphna Weinshall and Dan Amir. (2018). Theory of Curriculum Learning, with Convex Loss Functions. arXiv preprint. https://arxiv.org/abs/1812.03472
