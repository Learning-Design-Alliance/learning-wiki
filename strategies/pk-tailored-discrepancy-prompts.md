---
type: strategy
id: pk-tailored-discrepancy-prompts
title: Adaptive systems should deliver prior-knowledge-tailored discrepancy prompts and regular self-assessment calibration prompts
description: "The authors recommend adaptive systems incorporate discrepancy prompts tailored to prior knowledge: for LPK learners, prompts encouraging reflective engagement with foundational tasks; for HPK learners, prompts that c..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: man-su-2025
    resource: "https://doi.org/10.1038/s41539-025-00366-7"
    title: "Man Su, Belle Dang, Andy Nguyen & Tomohiro Nagashima. (2025). Choice-making in an adaptive learning system with motivational pedagogical agents. npj Science of Learning. https://doi.org/10.1038/s41539-025-00366-7"
    author: "Man Su, Belle Dang, Andy Nguyen & Tomohiro Nagashima"
---

# Adaptive systems should deliver prior-knowledge-tailored discrepancy prompts and regular self-assessment calibration prompts

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (1 for, 3 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The authors recommend adaptive systems incorporate discrepancy prompts tailored to prior knowledge: for LPK learners, prompts encouraging reflective engagement with foundational tasks; for HPK learners, prompts that challenge intuitive reasoning and heuristics even after correct answers (e.g., asking students to explain or simplify their steps). Systems should also "regularly prompt learners to self-assess and calibrate their understanding ag ainst task complexity and personal learning goals". Table 6 gives concrete redesigned prompt examples for each context.

## Design Implications

### Context
#### Requirements
- Some estimate of learners' prior knowledge to tailor prompts
- Prompt content targeting reflection on reasoning rather than only correctness feedback
#### Constraints
- In this study prompts were delivered at fixed points within tasks and not personalized beyond choice-making scenario type, which the authors list as a possible reason for null main effects

### Target Learners
- Secondary school students (9th and 10th grade) with varying prior knowledge in algebra

### Target Learning Goals
- Metacognitive reflection, calibration of understanding, and disruption of heuristic error-prone strategies

### Affordances
- [Choice Making Srl Operationalization](../theories/self-regulated-learning.md)

## Claims

- [Prior knowledge significantly predicted algebra posttest scores and learning gains, with high-prior-knowledge students scoring higher and low-prior-knowledge students gaining more](../claims/prior-knowledge-moderates-algebra-outcomes.md) [+W]
- [Lag sequential analysis revealed distinct choice-making trajectories: HPK students showed confidence-driven extra-task engagement and unre reflective repeated-failure sequences, while LPK students relied on preparatory worked examples](../claims/lsa-pk-choice-trajectories.md) [~W]
- [Process mining showed LPK students began with preparatory tasks and achieved a higher proportion of correct decisions, while HPK students skipped preparation and increasingly took advanced tasks](../claims/process-mining-correct-decision-lpk.md) [~W]
- [Overall choice frequency did not differ by condition or prior knowledge, but the condition pattern reversed across prior-knowledge groups](../claims/choice-frequency-pk-condition-reversal.md) [~W]

## Related Strategies

- [Embed metacognitive scaffolds in GenAI search systems — prompting sub-question formulation, guiding output comparison, and encouraging reflection on AI-user knowledge discrepancies](genai-metacognitive-scaffolds-for-laziness.md)
- [Scaffold question formulation and active help-seeking in AI-supported tutoring systems](scaffold-question-formulation-ai-help-seeking.md)
- [Adaptive systems should scaffold strategic disengagement as a reflective metacognitive choice rather than penalize it](scaffold-strategic-disengagement.md)

## Examples
-

## Key Sources
- Man Su, Belle Dang, Andy Nguyen & Tomohiro Nagashima. (2025). Choice-making in an adaptive learning system with motivational pedagogical agents. npj Science of Learning. https://doi.org/10.1038/s41539-025-00366-7
