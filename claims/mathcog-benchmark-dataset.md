---
type: claim
title: "MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels"
description: "MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels"
id: mathcog-benchmark-dataset
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yoonsu-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` MathCog contains 3,036 diagnostic verdicts across 639 student responses to 110 math problems, annotated by 15 middle school teachers using TIMSS-grounded checklists. [→ Yoonsu Kim 2026](#yoonsu-kim-2026)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)

`q2 · i?` · `design · r3`

Dataset construction with 5 education experts and 15 middle school teachers (average 6.1±4.3 years experience). Each check item received a Yes/No judgment plus an Evident/Vague evidential-strength label; topics below 70% inter-rater agreement were excluded to secure stable ground truth.

> "we constructedMathCog, a benchmark dataset containing 3,036 diagnostic verdicts across 639 student responses to 110 math problems, annotated by teachers using TIMSS-grounded cognitive skill checklists with eviden-tial strength labels (Evident/Vague)."

## Discussion


## Related Claims
- [LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated](evidence-over-attribution-false-attribution.md) — related
- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](llms-f1-below-05-cognitive-skill-diagnosis.md) — related
- [LLM diagnostic performance drops sharply when student responses contain vague rather than evident evidence](vague-evidence-degrades-llm-diagnosis.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution](applying-vs-knowing-skill-diagnosis-gap.md) — related
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — related
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](few-shot-prompting-no-f1-gain-reduces-overattribution.md) — related
