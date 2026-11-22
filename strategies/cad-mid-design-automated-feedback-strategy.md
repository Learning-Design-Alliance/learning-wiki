---
type: strategy
id: cad-mid-design-automated-feedback-strategy
title: Deliver automated real-time feedback within CAD software once a student is roughly halfway through a design task
description: "Because sequence-based logistic regression reaches greater than 60% prediction accuracy using the first 60% of design actions, the authors propose that CAD programs like Aladdin could provide useful automated feedback..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: jasmine-singh-2021
    resource: "https://github.com/singh486/Aladdin_machine_learning"
    title: "Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie. (2021). Using Machine Learning to Predict Engineering Technology Students' Success with Computer Aided Design. https://github.com/singh486/Aladdin_machine_learning"
    author: Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie
---

# Deliver automated real-time feedback within CAD software once a student is roughly halfway through a design task

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Because sequence-based logistic regression reaches greater than 60% prediction accuracy using the first 60% of design actions, the authors propose that CAD programs like Aladdin could provide useful automated feedback "when they are approximately halfway through their design." Such just-in-time intervention could help students recognize which actions will not lead to optimal designs, scaling formative assessment in large, online, hybrid, and HyFlex courses where instructor feedback is time-intensive.

## Design Implications

### Context
#### Requirements
- CAD software must log timestamped design actions and embed trained prediction models; the authors suggest future tie-ins to on-screen avatar mentors using a dialogic framework of describing, evaluating, speculating, and planning.
#### Constraints
- The authors state they do not know why certain design action sequences produced successful designs, and current models only permit interventions around the midpoint of the design process.

### Target Learners
- first-year undergraduate engineering technology students in large or online courses

### Target Learning Goals
- engineering design success
- understanding effects of design actions on outcomes such as net energy use

## Claims

- [Logistic regression on the first 60% of a student's design action sequence predicts zero-net-energy design success with greater than 60% accuracy](../claims/early-design-action-sequences-predict-cad-success.md) [+W]
- [Logistic regression on tallied design action counts predicts success with accuracy consistently above 50% and mostly above 65%](../claims/logistic-tallied-counts-above-chance.md) [+W]
- [Linear regression on tallied design actions cannot accurately predict final net energy values](../claims/linear-regression-tallied-actions-inaccurate.md) [+W]

## Related Strategies

- [Provide real-time hints and automated feedback on qualitative analysis within an unconstrained online problem-solving environment](pslp-real-time-hints-and-text-feedback-strategy.md)

## Examples
-

## Key Sources
- Jasmine Singh, Viranga Perera, Alejandra J. Magana, Brittany Newell, Jin Wei-Kocsis, Ying Ying Seah, Greg J. Strimel, and Charles Xie. (2021). Using Machine Learning to Predict Engineering Technology Students' Success with Computer Aided Design. https://github.com/singh486/Aladdin_machine_learning
