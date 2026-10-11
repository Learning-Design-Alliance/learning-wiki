---
type: claim
title: Gemini and Gemini Pro show the highest internal grading consistency across file upload volumes, with no clear monotonic lost-in-the-middle effect
description: Gemini and Gemini Pro show the highest internal grading consistency across file upload volumes, with no clear monotonic lost-in-the-middle effect
id: gemini-highest-consistency-across-file-volumes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: brevik-a-2026
    resource: "https://doi.org/10.3389/feduc.2026.1904452"
    title: "Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452"
    author: Brevik A, Jerpseth H and Lafontan SR
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Gemini and Gemini Pro show the highest internal grading consistency across file upload volumes, with no clear monotonic lost-in-the-middle effect

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`

## Subclaims
`q3 i?` Across file upload volumes of 1–8 files, Gemini and Gemini Pro had the highest Krippendorff's alpha (Gemini Pro up to 0.702), and no monotonic relationship between volume and consistency was found. [→ Brevik A 2026](#brevik-a-2026)

## Evidence

### Brevik A 2026

Brevik A, Jerpseth H and Lafontan SR (2026). Large language models as grading assistants in public health education: a method-comparison study of essay-style exam assessment. Front. Educ. 11:1904452. https://doi.org/10.3389/feduc.2026.1904452

`q3 · i?` · `causal · r1`

Krippendorff's alpha across single- and multi-file upload conditions (3, 5, 7/8 files). "Gemini and Gemini Pro appeared to be the most consistent" (Gemini Pro alphas 0.691–0.702); non-Google models showed lower alpha with multiple files, though the study lacked power to quantify U-shaped attention bias.

> "Considering the grading consistency across different file upload volumes (Table 3), Gemini and Gemini Pro appeared to be the most consistent. No clear evidence of a lost-in-the-middle problem or attention fatigue can be discerned from"

## Discussion


## Related Claims
- [ChatGPT in thinking mode shows the strongest agreement with human examiners on essay-style exam grading (weighted kappa 0.718)](chatgpt-thinking-mode-strongest-human-grading-agreement.md) — related
- [LLM-based essay grading is not fully reproducible: repeated ChatGPT sessions on the same submissions show only moderate consistency (Krippendorff's alpha 0.625)](llm-grading-session-variability-limited-reproducibility.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
