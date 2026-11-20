---
type: strategy
id: automated-uptake-feedback-professional-development
title: Use automated uptake measurement as a scalable professional development feedback tool for teachers
description: "The authors propose their uptake measure as \"an automated tool to give feedback to teachers\", addressing professional development that is highly resource intensive because it relies on classroom observations and manua..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: dorottya-demszky-2021
    resource: "https://arxiv.org/abs/2106.03873"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. https://arxiv.org/abs/2106.03873"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
---

# Use automated uptake measurement as a scalable professional development feedback tool for teachers

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The authors propose their uptake measure as "an automated tool to give feedback to teachers", addressing professional development that is highly resource intensive because it relies on classroom observations and manual evaluation. Because existing approaches are costly, teachers in under-resourced school systems have had limited access to quality professional development on uptake; an unsupervised, scalable measure could close that gap. The authors note uptake would be classified by existing guidelines as a promising potential intervention because it is highly scalable and easily quantified.

## Design Implications

### Context
#### Requirements
- A trained unsupervised uptake model (e.g., the PJSD model) applicable to new conversation datasets without labeled data
#### Constraints
- The evidence is correlational: significant linear correlations with outcomes such as student satisfaction and instruction quality, not a tested causal effect on student learning
- Generalizability was tested on spoken, written and simulated settings, but the measure failed to correlate for the repetition baseline only in the written tutoring setting

### Target Learners
- K-12 teachers, especially those in under-resourced school systems

### Target Learning Goals
- improving teachers' uptake of student contributions through scalable feedback

### Affordances
- [Uptake As Pjsd Dependence Framework](../research-methods/uptake-formalized-as-pointwise-jensen-shannon-divergence-estimated-via-next-utterance-clas.md)

## Claims

- [Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set](../claims/elaboration-prompts-pjsd-advantage.md) [+W]
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](../claims/pjsd-captures-uptake-phenomena-switchboard.md) [+W]
- [PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting](../claims/pjsd-correlates-educational-outcomes-three-datasets.md) [+W]
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](../claims/pjsd-outperforms-repetition-baseline-uptake.md) [+W]
- [Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness](../claims/supervised-models-competitiveness-uptake.md) [+W]
- [Word-overlap measures outperform sentence-level similarity measures, including neural ones, at measuring uptake](../claims/token-overlap-outperforms-sentence-similarity-uptake.md) [+W]

## Related Strategies

- [Use automated funneling/focusing measures in teacher feedback and professional development tools](automated-feedback-funneling-focusing-tool-strategy.md)
- [Deliver scalable automated talk-move feedback to online instructors as a complement to professional development](automated-talk-move-feedback-strategy.md)

## Examples
-

## Key Sources
- Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. https://arxiv.org/abs/2106.03873
