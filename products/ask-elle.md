---
type: product
id: ask-elle
title: Ask-Elle
description: Ask-Elle is a web-based intelligent tutoring system developed for teaching first-year computer science students Haskell through strategy-based model tracing, property-based testing, and automated hints.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Ask-Elle

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
Ask-Elle is a web-based intelligent tutoring system developed for teaching first-year computer science students Haskell through strategy-based model tracing, property-based testing, and automated hints.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Class 3 programming exercises with teacher-configurable feedback and flexibility**: Ask-Elle offers class 3 programming exercises, which can be solved by applying alternative solution strategies, in contrast to class 1 exercises with a single correct solution and class 2 exercises with different implementation variants of a fixed strategy. Teachers add exercises by providing model solutions and a configuration file, and can use annotations (DESC, FB, MUSTUSE, ALT) to adapt feedback and control which implementations are accepted. This design allows teachers to accept or reject solutions based on different model solutions, such as an inefficient but simple recursive solution. (Gerdes et al. (2016))

### Claims

- [In log analysis of 3466 interactions, 56.1% of interactions and 46.3% of attempts were recognised as correct model solutions](../claims/ask-elle-log-analysis-recognition-rates.md) [+W]
- [Strategy-based assessment recognised 62 of 72 correct student programs (86%) from four model solutions with no false positives](../claims/ask-elle-assessment-recognises-62-of-72-programs.md) [+W]
- [Strategy-based assessment statically determines which solution strategy a student used and guarantees correctness of recognised programs](../claims/strategy-based-assessment-static-benefits.md) [+W]
- [Compiler errors accounted for over half of diagnosis interactions in the log analysis](../claims/ask-elle-compiler-errors-majority-of-interactions.md) [+W]
- [Students rated the tutor 3.4 out of 5 overall and particularly liked the worked-out solution feedback](../claims/ask-elle-student-satisfaction-3-4-of-5.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x
