---
type: theory
title: Fuzzy time series and its first-order time-invariant model
description: The article defines a fuzzy time series as a sequence of fuzzy sets F(t) defined on the universe of a conventional time series Y(t).
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: song-1991
    resource: "https://eric.ed.gov/?id=ED340733"
    title: "Song, Qiang; Chissom, Brad S. (1991). Forecasting Enrollments with Fuzzy Time Series. https://eric.ed.gov/?id=ED340733"
    author: Song, Qiang; Chissom, Brad S
---

# Fuzzy time series and its first-order time-invariant model

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study, `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
The article defines a fuzzy time series as a sequence of fuzzy sets F(t) defined on the universe of a conventional time series Y(t). A first-order model expresses the relation "F(t-1)-->F(t)" as F(t)=F(t-1)∘R(t,t-1), where R(t,t-1) is a fuzzy relationship; the series is time-invariant when R is independent of t. Theorem 2 gives a matrix formula for computing R from historical fuzzy-set transitions, which the authors use to build the enrollment forecasting model via fuzzy logical reasoning.

## Design Implications

### Context
#### Requirements
- Fuzzy sets with memberships must be defined on the universe of the historical data, and historical experience knowledge (or data) is needed to establish the fuzzy logical relationships.
#### Constraints
- The article applies only the first-order, time-invariant model and notes that in cases of quite severe non-linearity different fuzzy time series approaches should be sought.

### Target Learners
- higher education administrators and planners forecasting university enrollment

### Target Learning Objectives
- long-range enrollment projection for institutional planning

### Claims
- [Fuzzy Time Series More Precise Than Linear Regression Enrollment](../claims/fuzzy-time-series-more-precise-than-linear-regression-enrollment.md) [+M]

## Related Theories
- 

## Examples

- [Two-step fuzzy forecasting pattern: fuzzylise the universe, then interpret the fuzzy output](../patterns/two-step-fuzzylise-then-interpret-forecasting-pattern.md)

## Key Sources
- Song, Qiang; Chissom, Brad S. (1991). Forecasting Enrollments with Fuzzy Time Series. https://eric.ed.gov/?id=ED340733
