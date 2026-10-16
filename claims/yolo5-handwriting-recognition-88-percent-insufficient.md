---
type: claim
title: "An earlier YOLO-5-based handwriting recognition method reached only 88.28% accuracy on examination table fields, which the authors judge insufficient for summative assessment"
description: "An earlier YOLO-5-based handwriting recognition method reached only 88.28% accuracy on examination table fields, which the authors judge insufficient for summative assessment"
id: yolo5-handwriting-recognition-88-percent-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: hartwig-grabowski-2026
    resource: "https://doi.org/10.48550/arxiv.2606.08855"
    title: "Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855 [doi:10.48550/arxiv.2606.08855](https://doi.org/10.48550/arxiv.2606.08855)"
    author: Hartwig Grabowski, Michael Canz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# An earlier YOLO-5-based handwriting recognition method reached only 88.28% accuracy on examination table fields, which the authors judge insufficient for summative assessment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` A domain-specifically trained YOLO-5-based method achieved 88.28% recognition performance on handwritten examination entries, which the authors consider insufficient because roughly one error per ten letters would risk legally relevant misgrading. [→ Hartwig Grabowski 2026](#hartwig-grabowski-2026)

## Evidence

### Hartwig Grabowski 2026

Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855 [doi:10.48550/arxiv.2606.08855](https://doi.org/10.48550/arxiv.2606.08855)

`q2 · i?` · `design · r2`

The article reports its authors' earlier implementation, a YOLO-5-based recognizer trained on image segments from examination table fields: "recognition performance remained at 88.28%". The authors state this level is insufficient for summative assessment. No effect size or sample size is printed for this result.

> "An earlier implementation used a YOLO-5-based method (Redmon et al., 2016) trained on image segments extracted from the relevant table fields (Grabowski, 2023). Despite this domain-specific training, recognition performance remained at 88.28%."

## Discussion


## Related Claims
- [In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)](vision-llm-letter-recognition-98-84-percent.md) — related
