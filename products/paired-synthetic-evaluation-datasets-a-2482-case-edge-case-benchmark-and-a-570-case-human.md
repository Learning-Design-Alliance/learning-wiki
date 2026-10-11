---
type: product
id: paired-synthetic-evaluation-datasets-a-2482-case-edge-case-benchmark-and-a-570-case-human
title: "Paired synthetic evaluation datasets: a 2,482-case edge-case benchmark and a 570-case human-reviewed egregious-failure set"
description: A dataset pair created by Chris Rohlfs et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Paired synthetic evaluation datasets: a 2,482-case edge-case benchmark and a 570-case human-reviewed egregious-failure set

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A dataset pair created by Chris Rohlfs et al. for measuring educational-AI evaluator activation and coverage of deliberately severe failure cases.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Paired synthetic evaluation datasets: a 2,482-case edge-case benchmark and a 570-case human-reviewed egregious-failure set**: The article contributes a paired protocol of two synthetic datasets for calibrating evaluators. The benchmark "measures how much a configuration flags," reporting benchmark activation rate (BMK%) as the fraction of cases returning a primary fail verdict; it is unlabeled, so BMK% is an activation rate, not a false-positive rate. The egregious set is "a check on severe-case coverage": 570 fully synthetic cases, each designed to exhibit an unambiguous violation of one evaluator's failure mode, with every retained case human-reviewed and borderline cases dropped. (Chris Rohlfs et al. (2026))

### Claims
- [Post-calibration evaluators captured 100% of synthetic egregious failures across all 21 deployed evaluators, up from a pre-calibration range of 73.3–100%](../claims/egregious-capture-100-percent-after-calibration.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Chris Rohlfs, Rodrigo Vergara Bosse, Priscilla Hopper, Keanon O'Keefe, Patrick J. Russell. (2026). When Evaluators Cry Wolf: Lessons from Production LLM-as-Judge Evaluation in Educational AI. https://arxiv.org/abs/2609.28478
