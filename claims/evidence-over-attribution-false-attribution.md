---
type: claim
title: LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated
description: LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated
id: evidence-over-attribution-false-attribution
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
    kind: design
    rigour: 3
  - id: yoonsu-kim-2026-2
    resource: "https://arxiv.org/abs/2504.00843"
    title: "Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843"
    author: Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim
    q: 2
    i: 3
    kind: associational
    rigour: 2
---

# LLMs frequently over-attribute evidential strength and assert Evident evidence even for incorrect diagnoses, and the two tendencies are strongly correlated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i3` large

## Subclaims
`q2 i?` Models assigned Evident to vague-evidence cases (OverAttr M=.580) and asserted Evident evidence on incorrect diagnoses (FalseAttr M=.585). [→ Yoonsu Kim 2026](#yoonsu-kim-2026)
`q2 i3` Over-attribution and false-attribution were strongly correlated across models (Spearman's ρ=.837, p < .001). [→ Yoonsu Kim 2026 (2)](#yoonsu-kim-2026-2)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i?` · `design · r3`

Aggregate metrics across the 18-model MathCog evaluation. The article reports OverAttr M=.580 (SD=.120) and FalseAttr M=.585 (SD=.145), meaning models "often assert[ed] strong evidence even when diagnoses were incorrect."

> "Models frequently over-attributed evidential strength (OverAttr;M=.580,SD=.120) and falsely attributed evidence (FalseAttr;M=.585,SD=.145), often asserting strong evidence even when diagnoses were incorrect."

### Yoonsu Kim 2026 (2)

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i3` · `associational · r2`

Correlational analysis across the 18 models in the RQ2 section. The article reports Spearman's ρ=.837, p < .001, linking over-attribution of evidential strength to producing incorrect diagnoses with asserted evidence.

> "these two tendencies were strongly correlated across models (Spearman'sρ=.837,p < .001), indicating that models prone to over-attributing evidential strength are also more likely to produce"

## Discussion


## Related Claims
- [LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution](applying-vs-knowing-skill-diagnosis-gap.md) — related
- [LLMs expressed unjustified confidence in recommendations based on visual inputs, asserting incorrect pin-connection diagnoses with high stated certainty](llm-unjustified-confidence-visual-recommendations.md) — related
- [MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels](mathcog-benchmark-dataset.md) — related
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](llms-f1-below-05-cognitive-skill-diagnosis.md) — related
