---
type: claim
title: Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested
description: Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested
id: within-judge-stability-llm-rubric
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: md-zabirul-islam-2026
    resource: "https://arxiv.org/abs/2606.20608"
    title: "Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608"
    author: Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across thirty ablation cells, twenty-six had identical scores across three judge repetitions, with mean per-cell standard deviation 0.063 and Krippendorff's alpha approximately 0.97; cross-judge-family agreement is treated as a separate limitation. [→ Md Zabirul Islam 2026](#md-zabirul-islam-2026)

## Evidence

### Md Zabirul Islam 2026

Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608

`q2 · i?` · `design · r2`

Reliability analysis of a single Gemini-Flash judge scored n=3 times across thirty cells (five topics, three PCK dimensions, two variants). The article reports mean per-cell standard deviation 0.063 and alpha approximately 0.97; these are reliability statistics, not effect sizes.

> "The mean per-cell standard deviation is 0.063, and Krippendorff’s α [44], treating repetitions as raters, is approximately 0.97. Thus, within-judge variance is negligible at this rubric resolution, while cross-judge-family agreement remains the next required check."

## Discussion


## Related Claims
- [Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation](engagement-contract-ablation-reduces-pck-scores.md) — related
- [LLM-as-judge automated evaluation can achieve human-level agreement when carefully validated](llm-as-judge-human-level-agreement-with-validation.md) — a broader claim this one bears on
- [Multimodal LLMs show moderate cross-model agreement on which image-Required items are solvable, with within-family agreement exceeding cross-family agreement](moderate-cross-model-agreement-solvability.md) — related
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [AI grading of the exam is highly stable across five independent runs at the total-score level (ICC(A,1) = 0.967), with lower but still strong cell-level stability (ICC(A,1) = 0.836)](ai-grading-run-to-run-reliability-icc.md) — related
- [Cross-model agreement on assertions is moderate (median 0.401) and higher among construct-derived than corpus-derived assertions](assertion-cross-model-agreement-moderate-median-0401.md) — related
- [Adding a cross-model agreement filter improves performance for the top three LLM annotators](cross-model-agreement-filter-improves-top-annotators.md) — related
