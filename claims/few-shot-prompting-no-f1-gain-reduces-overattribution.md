---
type: claim
title: Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution
description: Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution
id: few-shot-prompting-no-f1-gain-reduces-overattribution
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: yoonsu-kim-2026
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Few-shot prompting did reduce tendencies toward evidence over-attribution and false-attribution. [→ Yoonsu Kim 2026](#yoonsu-kim-2026)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i?` · `causal · r1`

Same few-shot experiment. The article reports reduced over-attribution and false-attribution, suggesting examples encourage more cautious, evidence-grounded responses even while accuracy stays limited.

> "However, few-shot prompting did reduce tendencies toward evidence over-attribution and false-attribution, indicating that examples may encourage more cautious, evidence-grounded responses even when overall diagnostic accuracy remains limited."

## Discussion


## Related Claims
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — reports the opposite
- [LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution](applying-vs-knowing-skill-diagnosis-gap.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels](mathcog-benchmark-dataset.md) — related
