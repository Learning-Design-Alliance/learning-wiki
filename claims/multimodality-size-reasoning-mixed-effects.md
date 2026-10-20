---
type: claim
title: Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results
description: Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results
id: multimodality-size-reasoning-mixed-effects
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: mixed
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
    i: 2
    kind: associational
    rigour: 1
---

# Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2` · `i2` medium

## Subclaims
`q2 i?` Image-input models consistently outperformed their text-only counterparts in accuracy, but F1 improvements were inconsistent. [→ Yoonsu Kim 2026](#yoonsu-kim-2026)
`q2 i2` Model size showed a moderate positive relationship with F1 (Spearman's ρ=.570, p=.053). [→ Yoonsu Kim 2026 (2)](#yoonsu-kim-2026-2)

## Evidence

### Yoonsu Kim 2026

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843 [doi:10.48550/arxiv.2504.00843](https://doi.org/10.48550/arxiv.2504.00843)

`q2 · i?` · `design · r2`

Factor analysis of the 18-model MathCog evaluation (Table 2). The article reports image-input models "consistently outperformed their text-only counterparts in accuracy" while F1 gains were inconsistent, as visual input can introduce noise.

> "Models supporting image input consistently outperformed their text-only counterparts in accuracy, indicating that access to handwritten layouts and visual cues helps mitigate errors introduced by OCR transcription. However,improvements in F1 score were inconsistent"

### Yoonsu Kim 2026 (2)

Yoonsu Kim, Hyoungwook Jin, Hayeon Doh, Eunhye Kim, Dongyun Jung, Seungju Kim, Kiyoon Choi, Jinho Son, and Juho Kim. (2026). Benchmarking Large Language Models for Diagnosing Students' Cognitive Skills from Handwritten Math Work. arXiv. https://arxiv.org/abs/2504.00843

`q2 · i2` · `associational · r1`

Correlational analysis of model size versus F1 across the 18 models. The article reports Spearman's ρ=.570, p=.053, concluding scale alone is insufficient to explain performance variability.

> "the correlation was moderate (Spearman'sρ=.570,p=.053), sug-gesting that scale alone is insufficient to account for the substantial variability in performance across models."

## Discussion


## Related Claims
- [LLMs diagnose Applying skills better than Knowing skills, but with higher evidence over-attribution and false-attribution](applying-vs-knowing-skill-diagnosis-gap.md) — related
- [All 18 evaluated LLMs score macro F1 below 0.5 in diagnosing students' cognitive skills from handwritten math work](llms-f1-below-05-cognitive-skill-diagnosis.md) — related
- [MathCog: a benchmark of 3,036 teacher-annotated diagnostic verdicts over 639 handwritten student responses to 110 math problems with Evident/Vague evidence labels](mathcog-benchmark-dataset.md) — related
- Family-level permutation tests do not detect reliable reasoning-versus-non-reasoning differences in accuracy, refusal, or consistency — related
- With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models — related
- In a contrastive audit, visual misreading is the dominant failure mode for non-reasoning models on items reasoning models solve — related
- [Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides](multimodal-vs-ocr-pipeline-slide-type-comparison.md) — a narrower finding that bears on this claim
- [The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective](ocr-input-lower-token-cost-than-image-input.md) — reports the opposite
- [Multimodal LLMs grading handwritten student work achieved κ = 0.90 on arithmetic but κ ≈ 0.47 on interpreting student illustrations](multimodal-llm-grading-kappa-arithmetic-illustrations.md) — related
- [Fusing transformer text classifiers with a linguistic-feature neural network significantly outperforms unimodal models for UK Key Stage classification, with ELECTRA + ANN reaching F1 = 0.996](multimodal-fusion-outperforms-unimodal-key-stage-classification.md) — reports the opposite
- [StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants](structrag-outperforms-baselines-stem-diagrams.md) — related
