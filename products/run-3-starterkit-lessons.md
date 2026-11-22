---
type: product
id: run-3-starterkit-lessons
title: Run 3 Starterkit Lessons
description: "The Run 3 Starterkit Lessons are LHCb's online onboarding curriculum for newcomers to its software and analytical workflows, maintained through synchronized translations, external code files, automated testing, and expert review."
product_kind: curriculum
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Run 3 Starterkit Lessons

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The Run 3 Starterkit Lessons are LHCb's online onboarding curriculum for newcomers to its software and analytical workflows, maintained through synchronized translations, external code files, automated testing, and expert review.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CI-tested translation-maintainable Starterkit Lessons with external code scripts and synchronized languages**: The Run 3 Starterkit Lessons are the online follow-along lessons, first publicly released January 2025, used to onboard newcomers to LHCb software. Example code is "separated into their own source files" and reinjected into every translation, so code "cannot be different" across languages, and each example is executed in a GitLab CI pipeline before changes can merge. The CI framework runs Python code verification, automated linters, and a link checker, with an optional preview site for manual review. The system gates every merge on a successful CI pass plus expert and liaison review. (Morris et al. (2026))

### Claims

- [The Run 3 Starterkit receives about 30 visits per day, of which about 6.7 access at least one Chinese-language page](../claims/run3-starterkit-daily-visits-chinese-subset.md) [+M]
- [Roughly 22% of visits to the LHCb Starterkit website access at least one Chinese-language page](../claims/22-percent-visits-chinese-language-pages.md) [+W]

## Related Products and Programmes

- [HSF/IRIS-HEP training curriculum](hsfiris-hep-training-curriculum.md)

## Key Sources
- Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. https://arxiv.org/abs/2609.35830
