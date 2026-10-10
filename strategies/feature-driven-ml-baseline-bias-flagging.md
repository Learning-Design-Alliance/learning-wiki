---
type: strategy
id: feature-driven-ml-baseline-bias-flagging
title: Use interpretable feature-driven machine learning as a human-in-the-loop baseline for flagging ethnic bias in learning content
description: "The article positions learning analytics as supporting, not replacing, human review of educational texts: automated detection offers \"a scalable solution while retaining human judgment for nuanced evaluations\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: josmario-albuquerque-2026
    resource: "https://doi.org/10.18608/jla.2026.8905"
    title: "Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905"
    author: Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes
---

# Use interpretable feature-driven machine learning as a human-in-the-loop baseline for flagging ethnic bias in learning content

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article positions learning analytics as supporting, not replacing, human review of educational texts: automated detection offers "a scalable solution while retaining human judgment for nuanced evaluations". It recommends feature-based models (psycholinguistic markers, linguistic abstraction, valence, group mentions, context) because they "enable greater transparency and actionable insights for educational stakeholders", and provides "a baseline approach for more inclusive learning analytics (LA) in online environments". Practitioners would run such classifiers to pre-screen materials before human evaluation.

## Design Implications

### Context
#### Requirements
- A labelled dataset reflecting diverse student perspectives for training
- Feature extraction tooling (PoS tagging, psycholinguistic ratios, sentiment valence) and interpretable classifiers
#### Constraints
- The study is "an initial step toward automated bias classification in education"; bias is subjective and culturally shaped, so automated flags require human judgment

### Target Learners
- Higher education students
- Online learners using text-based open educational resources

### Target Learning Goals
- Equitable learning content review
- Detection of ethnic bias in curricula and learning platforms

## Related Strategies

- [Deploy AI-assisted classroom observation as a complementary first-pass screening and reflection tool, with raters retaining interpretive judgment](ai-assisted-observation-complementary-screening-strategy.md)

## Examples
-

## Key Sources
- Josmario Albuquerque, Bart Rienties, Martin Hlosta, Wayne Holmes. (2026). Learning Analytics to Uncover Ethnic Bias in Educational Texts: An Ensemble Learning Approach. Journal of Learning Analytics 13(1). https://doi.org/10.18608/jla.2026.8905
