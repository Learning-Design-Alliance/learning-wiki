---
type: strategy
id: lm-as-coarse-evaluator-augmentor
title: Use LM evaluators as coarse, preliminary evaluators to speed up educational content design, not as replacements for human evaluators or empirical studies
description: "The article recommends positioning LM-based simulated experts as human augmentors in the instructional design loop: they can provide cheap, fast preliminary evaluations that inform the design of costly human-subjects..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: joy-he-yueya-2024
    resource: "https://arxiv.org/abs/2403.02795"
    title: "Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. https://arxiv.org/abs/2403.02795"
    author: Joy He-Yueya, Noah D. Goodman, Emma Brunskill
---

# Use LM evaluators as coarse, preliminary evaluators to speed up educational content design, not as replacements for human evaluators or empirical studies

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends positioning LM-based simulated experts as human augmentors in the instructional design loop: they can provide cheap, fast preliminary evaluations that inform the design of costly human-subjects experiments. The authors conclude that "the LM may be useful as a coarse evaluator to help speed up content design as a human augmentor but not to replace human evaluators or empirical studies", given observed human-LM divergences.

## Design Implications

### Context
#### Requirements
- Human teacher or empirical validation of LM-optimized materials before deployment; awareness that LMs may not consistently replicate established educational results
#### Constraints
- Discrepancies exist between LM and human teacher evaluations; evaluations limited to teacher perspective and to mathematics with GPT-3.5 and GPT-4

### Target Learners
- instructional designers and education researchers

### Target Learning Goals
- accelerating formative evaluation and iterative improvement of instructional materials

### Affordances
- [Simulated Expert Evaluation See](../products/ai-see-framework.md)

## Claims

- [An optimizer LM can iteratively improve math word problem worksheets using an evaluator LM's judgments as the reward function](../claims/instruction-optimization-improves-worksheets.md) [+M]
- [Human teachers' preferences for LM-generated worksheets correlate significantly with evaluator LM judgments (r = 0.661), but teachers sometimes cannot distinguish worksheets the LM perceives as different](../claims/lm-judgments-align-with-teacher-preferences.md) [+M]
- [LM judgments are internally consistent: SEEs designed to replicate the Variability Effect also replicate the Expertise Reversal Effect](../claims/see-judgments-consistent-across-replications.md) [+M]
- [LM-based simulated expert evaluations replicate the Expertise Reversal Effect: low-expertise learners benefit more from worked examples than practice, with no such difference among high-expertise learners](../claims/see-replicates-expertise-reversal-effect.md) [+M]
- [LM-based simulated expert evaluations replicate the Variability Effect: high variability enhances performance in worked-example conditions but has no effect in practice conditions](../claims/see-replicates-variability-effect.md) [+M]

## Related Strategies

- [Use LLM persona simulation only for preliminary experimentation, stress testing, and hypothesis generation, with separate validation for consequential applications](persona-simulation-preliminary-use-only.md)
- [Allocate human and AI effort by dimension type: automate explicit-criteria dimensions, retain human review for pedagogical judgment](human-ai-division-of-labor-mcq-generation.md)
- [Implement AI in assessment as a hybrid support tool for low-stakes, formative stages while humans retain final grading authority](hybrid-ai-human-assessment-implementation.md)
- [Deploy simulated students in four directions: teacher training, social learning, data generation, and content evaluation](four-directions-llm-simulated-students.md)

## Examples
-

## Key Sources
- Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. https://arxiv.org/abs/2403.02795
