---
type: strategy
id: automated-feedback-funneling-focusing-tool-strategy
title: Use automated funneling/focusing measures in teacher feedback and professional development tools
description: "The authors propose building automated feedback tools that show teachers the extent to which they are focusing or funneling in their own classrooms, motivated by prior tools that improved teachers' uptake of student c..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: sterling-alic-2022
    resource: "https://arxiv.org/abs/2208.04715"
    title: "Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. https://arxiv.org/abs/2208.04715"
    author: Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky
---

# Use automated funneling/focusing measures in teacher feedback and professional development tools

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (4 for, 1 against) · 2 studies (2 associational), `q2` · 0 of 2 report an effect size · 5 claims rest on one study

## Description
The authors propose building automated feedback tools that show teachers the extent to which they are focusing or funneling in their own classrooms, motivated by prior tools that improved teachers' uptake of student contributions. They state the high performance of the supervised measure "indicates its promise for supporting teachers in their instruction" and that the RoBERTa model shows "the potential of the RoBERTa model to be used in future feedback and professional development tools for teachers."

## Design Implications

### Context
#### Requirements
- A validated computational measure of funneling and focusing, such as the fine-tuned RoBERTa model, applied to classroom transcripts
#### Constraints
- The authors note generalizability to other classrooms and domains still needs testing, and it is unexplored whether quantitative feedback on focusing versus funneling is actually helpful to teachers

### Target Learners
- Elementary math teachers (K-12 teachers more broadly)

### Target Learning Goals
- Improving teachers' use of focusing question patterns to support student sensemaking and achievement

## Claims

- [A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set](../claims/roberta-funneling-focusing-correlation-761.md) [+W]
- [RoBERTa model outputs correlate significantly with math instruction quality scores and with teacher value-added scores](../claims/roberta-measure-correlates-educational-outcomes.md) [+W]
- [The question words \"why\", \"how do\", and \"what else\" correlate positively with focusing labels while \"when\" correlates negatively on the FILTERED set](../claims/question-word-lexical-patterns-focusing.md) [+W]
- [The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)](../claims/forwards-range-unsupervised-correlations.md) [-W]
- [Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness](../claims/supervised-models-competitiveness-uptake.md) [+W]

## Related Strategies

- [Use automated uptake measurement as a scalable professional development feedback tool for teachers](automated-uptake-feedback-professional-development.md)

## Examples
-

## Key Sources
- Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. https://arxiv.org/abs/2208.04715
