---
type: strategy
id: teacher-in-the-loop-diagnostic-verification
title: Use teacher-in-the-loop verification targeted at each error stage rather than fully automated LLM diagnosis
description: "The article recommends moving \"beyond fully automated diagnosis toward transparency and selective human verification.\" Teachers intervene at specific pipeline stages: validating whether identified evidence is actually..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: yoonsu-kim-2026
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
---

# Use teacher-in-the-loop verification targeted at each error stage rather than fully automated LLM diagnosis

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends moving "beyond fully automated diagnosis toward transparency and selective human verification." Teachers intervene at specific pipeline stages: validating whether identified evidence is actually present, checking model interpretations against diagnostic criteria, scrutinizing whether inferred skills are supported by observable evidence, and overseeing coherence between intermediate reasoning and final judgments. This targets the five recurring error types the analysis identified.

## Design Implications

### Context
#### Requirements
- Teachers available to validate identified evidence, check rubric interpretation, scrutinize over-inference, and oversee consistency between reasoning and final verdicts
#### Constraints
- The article states current LLMs are not yet reliable for cognitive skill diagnosis without intermediate verification, as errors cascade throughout the diagnostic pipeline

### Target Learners
- middle school math students

### Target Learning Goals
- diagnosis of students' cognitive skills (knowing and applying) in mathematics from handwritten work

## Claims

- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](../claims/llms-f1-below-05-cognitive-skill-diagnosis.md) [+W]
- [LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated](../claims/evidence-over-attribution-false-attribution.md) [+W]

## Related Strategies

- [Use accuracy-rejection curves with reliability analysis to select operating points for selective delegation in human-in-the-loop grading](arc-based-selective-delegation-grading.md)

## Examples
-

## Key Sources
- Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843
