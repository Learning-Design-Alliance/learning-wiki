---
type: strategy
id: preferences-as-engagement-optimization-inputs
title: Use learner preferences as inputs for engagement optimization in adaptive systems, rather than as static styles for improving grades
description: "This strategy recasts adaptive instructional systems: instead of categorizing students into static styles to raise scores, systems treat stated preferences as real-time inputs to maintain attention and motivation."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: adusumilli-2026
    resource: "https://arxiv.org/abs/2610.05178"
    title: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. https://arxiv.org/abs/2610.05178"
    author: "Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S"
---

# Use learner preferences as inputs for engagement optimization in adaptive systems, rather than as static styles for improving grades

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
This strategy recasts adaptive instructional systems: instead of categorizing students into static styles to raise scores, systems treat stated preferences as real-time inputs to maintain attention and motivation. The authors suggest adaptive systems "utilize preference-based content not to improve test scores directly, but to 'warm up' the learner's neural state" via theta/alpha regulation, and propose closed-loop systems that dynamically alter modality when EEG engagement indices drop.

## Design Implications

### Context
#### Requirements
- A real-time engagement detection pipeline; research-grade or improved EEG signal fidelity (semi-dry or active-electrode systems suggested for future implementations)
#### Constraints
- Does not improve test scores directly; consumer-grade EEG currently lacks fidelity for nuanced affective-state detection without extensive artifact correction; longitudinal persistence of engagement benefits is untested

### Target Learners
- graduate students in multimodal instruction
- learners in adaptive educational technologies

### Target Learning Goals
- maintaining learner attention and motivation during instruction

### Affordances
- [Eeg Theta Alpha Engagement Framework](../research-methods/eeg-based-continuous-online-cognitive-load-measurement.md)

## Claims

- [Aligning instructional modality with learner-stated VARK preference does not significantly improve short-term learning gains](../claims/preference-alignment-no-significant-learning-gains.md) [+W]
- [Subjective preference modulates neural engagement states (theta/alpha patterns) even though it does not optimize test performance](../claims/preference-modulates-neural-engagement-not-performance.md) [+W]
- [EEG theta and alpha spectral features classify preference-matched versus mismatched instructional epochs at 83.21% accuracy with OpenBCI hardware](../claims/eeg-classification-preference-matching-openbci-83.md) [+W]
- [Exploratory subgroup analyses suggest modality-matched Visual and Kinesthetic learners showed marginal, uncorrected performance improvements](../claims/modality-matched-subgroup-marginal-improvements.md) [~W]

## Related Strategies

- [Update student profiles dynamically as learners interact with an LLM-powered environment](dynamic-student-profile-updates-llm-tutoring.md)
- [Develop adaptive LLM learning-by-teaching systems that dynamically adjust to a learner's input style and cognitive capacity](st-adaptive-llm-lbt-input-style-adjustment.md)
- [Move beyond static skill-targeted rewriting toward interaction-aware adaptive error explanations](interaction-aware-adaptive-error-explanations.md)

## Examples
-

## Key Sources
- Adusumilli, S. J., Giri, D., Vaswani, P., Singh, P., Moncy, M., Pulavarthy, L. P., & Purkayastha, S. (2026). Preference vs. Performance: EEG-Based Classification of Learner Engagement in Multimodal Instruction. arXiv preprint. https://arxiv.org/abs/2610.05178
