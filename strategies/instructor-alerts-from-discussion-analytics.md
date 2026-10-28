---
type: strategy
id: instructor-alerts-from-discussion-analytics
title: Use discussion analytics to alert instructors about students who may need more assistance
description: "The authors propose applying their predictive analysis results formatively: instructors can use discussion-derived indicators to identify struggling students and adjust participation strategies."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: jaebong-yoo-jihie-kim-2014
    resource: "https://doi.org/10.1007/s40593-013-0010-8"
    title: "Jaebong Yoo & Jihie Kim. (2014). Can Online Discussion Participation Predict Group Project Performance? Investigating the Roles of Linguistic Features and Participation Patterns. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-013-0010-8"
    author: "Jaebong Yoo & Jihie Kim"
---

# Use discussion analytics to alert instructors about students who may need more assistance

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The authors propose applying their predictive analysis results formatively: instructors can use discussion-derived indicators to identify struggling students and adjust participation strategies. "We expect that this predictive information can be used for alerting the instructor about students who may need more assistance or identifying strategies to improve the participation." Based on the findings, instructors can encourage students to help information-seeking peers and examine work pacing more closely.

## Design Implications

### Context
#### Requirements
- Automated analysis pipelines for discussion data must be in place to generate the predictive indicators
#### Constraints
- The framework was developed and evaluated in one computer science course; generalization to other courses is planned but not yet demonstrated

### Target Learners
- undergraduate students in project-based engineering courses

### Target Learning Goals
- improving group project performance through timely instructor support
- encouraging information provision and earlier work pacing

### Affordances
- [Discussion Participation Performance Prediction Framework](../research-methods/early-warning-indicator-construction.md)

## Claims

- [Earlier participation relative to project deadlines (higher APTTD) predicts higher project grades](../claims/early-posting-apttd-predicts-grades.md) [+W]
- [Simple participation quantity measures (total and reply message counts) correlate with project grades](../claims/message-frequency-correlates-grades.md) [+W]
- [Positive emotion expressions in discussion messages positively correlate with project grades](../claims/positive-emotion-correlates-grades.md) [+W]
- [A three-predictor regression model (Source, APTTD, positive emotion) explains 32% of variance in group project grades](../claims/regression-model-32-percent-variance-grades.md) [+W]
- [Machine-learned Sink/Source classifiers classify information roles with F-scores of 0.914 and 0.908 on noisy student discussion text](../claims/sink-source-role-classifiers-accuracy.md) [+W]
- [Groups that provide more information to others (Source role) achieve higher project grades](../claims/source-role-provision-predicts-project-grades.md) [+W]

## Related Strategies

- [Use coordination-based indicators rather than inactivity alone to trigger alerts and adaptive interventions for struggling groups](coordination-based-alert-strategy.md)
- [Learning Dashboards](learning-dashboards.md)
- [Pedagogical nudges triggered by WBA analytics to encourage engagement](wba-analytics-pedagogical-nudges.md)
- [Engage teachers with predictive analytics dashboards to trigger timely interventions with students at risk](teacher-engagement-with-pla-interventions.md)

## Examples
-

## Key Sources
- Jaebong Yoo & Jihie Kim. (2014). Can Online Discussion Participation Predict Group Project Performance? Investigating the Roles of Linguistic Features and Participation Patterns. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-013-0010-8
