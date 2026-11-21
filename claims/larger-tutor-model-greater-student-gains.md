---
type: claim
title: A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages
description: A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages
id: larger-tutor-model-greater-student-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: junior-cedric-tonga-2026
    resource: "https://doi.org/10.18653/2026.mathnlp-main.16"
    title: "Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)"
    author: Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A larger tutor model (LLaMA-3.3-70B) yields greater student gains than a smaller one, especially for low-resource languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` LLaMA-3.3-70B consistently outperforms LLaMA-3.1-8B as tutor across student models and hint prompts, with the effect most pronounced for low-resource languages. [→ Junior Cedric Tonga 2026](#junior-cedric-tonga-2026)

## Evidence

### Junior Cedric Tonga 2026

Junior Cedric Tonga, KV Aditya Srivatsa, Kaushal Kumar Maurya, Fajri Koto, Ekaterina Kochmar. (2026). Simulating Student-Tutor Interactions with LLMs for Multilingual Math Feedback. arXiv. Originally published 2025. [doi:10.18653/2026.mathnlp-main.16](https://doi.org/10.18653/2026.mathnlp-main.16)

`q2 · i?` · `causal · r1`

Boxplot comparison (Appendix Figure A) of median student gains for the two tutor models; the authors report LLaMA-3.3-70B "consistently yields greater gains across both student models and hint generation prompts," with median gains of 8.6% versus 7.7% in the multilingual setup with Mistral-7B.

> "we observe that LLaMA-3.3-70B consistently yields greater gains across both student models and hint generation prompts, outperforming LLaMA-3.1-8B for HRLs and LRLs."

## Discussion


## Related Claims
- [Gold answer leakage in generated hints is low for the main tutor model but higher for low-resource languages](gold-answer-leakage-low-lrl-higher.md) — related
- [Hint language substantially impacts student gains, with English hints generally most effective from larger tutors but native-language hints competitive in specific cases](hint-language-impacts-student-gains.md) — related
- [Model size is not the primary factor in outcome-prediction performance](model-size-not-primary-outcome-prediction-factor.md) — reports the opposite
- [LLM grading performance generally correlates with parameter count, and 4-bit quantization has negligible effect on grading performance](llm-grading-performance-scales-with-parameters.md) — a broader claim this one bears on
