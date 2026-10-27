---
type: design
id: e-tutor-dynamic-learner-model-phrase-descriptors
title: "E-Tutor's dynamic learner model: skill-specific scores and phrase descriptors modulate feedback and remediation"
description: "E-Tutor's learner model provides a dynamic assessment of each learner by considering past and current performance and behavior."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: trude-heift-2016
    resource: "https://doi.org/10.1007/s40593-015-0061-0"
    title: "Trude Heift. (2016). Web Delivery of Adaptive and Interactive Language Tutoring: Revisited. Int J Artif Intell Educ 26:489–503. https://doi.org/10.1007/s40593-015-0061-0"
    author: Trude Heift
---

# E-Tutor's dynamic learner model: skill-specific scores and phrase descriptors modulate feedback and remediation

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
E-Tutor's learner model provides a dynamic assessment of each learner by considering past and current performance and behavior. The grammar and parser generate phrase descriptors, frame structures modeling grammatical phenomena (e.g., subject-verb agreement, noun gender) with values correct, error, or absent, which "correspond to structures in the learner model and are the interface medium between the learner model and the grammar". For each grammar constraint the model keeps a per-student score that increases or decreases with evidence of successful or unsuccessful use; feedback wording and amount depend on the learner's rank (novice vs. expert) per skill, and remedial exercises target individual weaknesses.

## Design Implications

### Context
#### Requirements
- A fully specified lexicon and a grammar and parser that generate phrase descriptors for each grammatical constraint
- Separation of feedback generation from linguistic analysis and learning activity so feedback messages can be adjusted per exercise
#### Constraints
- Scores for each grammar skill are tracked independently, so a student may be expert at one skill and novice at another

### Target Learners
- University learners of German as a foreign language

### Learning Goals
- Individualized error-contingent feedback and remediation across German grammar skills

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Trude Heift. (2016). Web Delivery of Adaptive and Interactive Language Tutoring: Revisited. Int J Artif Intell Educ 26:489–503. https://doi.org/10.1007/s40593-015-0061-0
