---
type: claim
title: LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution
description: LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution
id: applying-vs-knowing-skill-diagnosis-gap
status: draft
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
    rigour: 2
  - id: yoonsu-kim-2026-2
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2`–`r3` · `q2`

## Subclaims
`q2 i?` Contrary to expectations, models performed better on Applying than Knowing skills in F1 (t= 4.34, p < .001) and accuracy (t= 4.85, p < .001). [→ Yoonsu Kim 2026](#yoonsu-kim-2026)
`q2 i?` Applying skills also exhibited higher evidence over-attribution (t= 5.44, p < .001) and false-attribution (t= 7.66, p < .001) than Knowing skills. [→ Yoonsu Kim 2026 (2)](#yoonsu-kim-2026-2)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)

`q2 · i?` · `design · r2`

Skill-specific analysis of the 18-model MathCog evaluation (Figure 3). The article reports the Applying-versus-Knowing contrast with t= 4.34 (F1) and t= 4.85 (accuracy), both p < .001, noting the gain "came with increased evidential errors."

> "models performed better onApplyingskills in bothF1 score (t= 4.34,p < .001) and accuracy (t= 4.85,p < .001). However, this performance gain came with increased evidential errors."

### Yoonsu Kim 2026 (2)

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i?` · `design · r3`

Same skill-specific analysis. The article reports higher over-attribution (t= 5.44) and false-attribution (t= 7.66) for Applying than Knowing skills, both p < .001, indicating overstated evidential support for higher-level skills.

> "Applyingskills exhib-ited higher evidence over-attribution (t= 5.44,p < .001) and false-attribution(t= 7.66,p < .001) thanKnowingskills, indicating a tendency to overstate evidential support when diagnosing higher-level cognitive skills."

## Discussion


## Related Claims
- [LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated](evidence-over-attribution-false-attribution.md) — related
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — related
- [Few-shot prompting does not improve diagnostic F1 or accuracy but reduces evidence over-attribution and false-attribution](few-shot-prompting-no-f1-gain-reduces-overattribution.md) — related
- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](llms-f1-below-05-cognitive-skill-diagnosis.md) — related
- [MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels](mathcog-benchmark-dataset.md) — related
