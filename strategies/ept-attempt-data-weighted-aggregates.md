---
type: strategy
id: ept-attempt-data-weighted-aggregates
title: Use stored attempt-level test data to build weighted aggregate performance measures
description: "The authors propose exploiting the platform's stored attempt data to produce better measures of test performance: \"it is possible to use such data to produce a better measure of the quality of each student's EPT perfo..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: chongchitnan-2018
    resource: "https://arxiv.org/abs/1910.12314"
    title: "Chongchitnan, S. (2018). Electronic Preparatory Test for Mathematics Undergraduates: Implementation, Results and Correlations. https://arxiv.org/abs/1910.12314"
    author: Chongchitnan, S
---

# Use stored attempt-level test data to build weighted aggregate performance measures

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The authors propose exploiting the platform's stored attempt data to produce better measures of test performance: "it is possible to use such data to produce a better measure of the quality of each student's EPT performance (for example, by weighting the score of each test by the number of attempts needed to pass)." They also suggest a weighted combination of entry tariffs and EPT results that would maximise the correlation with examination results.

## Design Implications

### Context
#### Requirements
- The data for every attempt of the EPT is stored in the Möbius server, including how many times each student needed to take each sub-test before passing and how long each attempt took
#### Constraints
- Both proposed aggregates are investigations for future work; the article reports no results for them

### Target Learners
- beginning undergraduate mathematics students taking the EPT

### Target Learning Goals
- more accurate prediction of first-year examination performance from preparatory test data

## Claims

- [EPT scores show a positive correlation with average first-year examination marks (r=0.49)](../claims/ept-exam-correlation-r049.md) [+W]
- [The EPT score is the strongest of three correlates of first-year examination performance, ahead of the total entry tariff and the maths-only tariff](../claims/ept-strongest-correlator-vs-entry-tariffs.md) [+W]

## Related Strategies

- [Post-test follow-up protocol: flag failures to personal tutors and assign topic-specific handwritten exercises](ept-personal-tutor-followup-protocol.md)

## Examples
-

## Key Sources
- Chongchitnan, S. (2018). Electronic Preparatory Test for Mathematics Undergraduates: Implementation, Results and Correlations. https://arxiv.org/abs/1910.12314
