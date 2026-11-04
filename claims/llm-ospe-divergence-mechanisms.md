---
type: claim
title: "Item characteristics associated with LLM-human discrepancy on multimodal OSPE items cluster into three mechanisms: non-standard histological staining, 3D spatial reasoning from 2D images, and semantic inflexibility in short-answer evaluation"
description: "Item characteristics associated with LLM-human discrepancy on multimodal OSPE items cluster into three mechanisms: non-standard histological staining, 3D spatial reasoning from 2D images, and semantic inflexibility in..."
id: llm-ospe-divergence-mechanisms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: akhund-2026
    resource: "https://doi.org/10.1080/10872981.2026.2684837"
    title: "Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837"
    author: Akhund, S. A., et al
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: akhund-2026-2
    resource: "https://doi.org/10.1080/10872981.2026.2684837"
    title: "Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837"
    author: Akhund, S. A., et al
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: akhund-2026-3
    resource: "https://doi.org/10.1080/10872981.2026.2684837"
    title: "Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837"
    author: Akhund, S. A., et al
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Item characteristics associated with LLM-human discrepancy on multimodal OSPE items cluster into three mechanisms: non-standard histological staining, 3D spatial reasoning from 2D images, and semantic inflexibility in short-answer evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Items using non-standard stains (toluidine blue vs H&E) showed student success above 95% with markedly lower LLM scores and gaps exceeding 50 percentage points. [→ Akhund 2026](#akhund-2026)
`q3 i?` A pelvic 3D model item on which 93.28% of students succeeded by human grading received universal zero scores from Claude and Gemini, a 93.3 percentage-point gap. [→ Akhund 2026 (2)](#akhund-2026-2)
`q3 i?` One model (ChatGPT) selectively underscored an item permitting multiple anatomically correct responses, consistent with an overly narrow lexical match. [→ Akhund 2026 (3)](#akhund-2026-3)

## Evidence

### Akhund 2026

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Item-level gap analysis in the same retrospective study. MTI-Q5 (cardiac muscle histology) was rated high by the human grader (mean = 1.45) but low by Gemini (mean = 0.75), attributed to toluidine blue rather than standard H&E staining.

> "MTI-Q5 used toluidine blue staining and showed student success above 95% with markedly lower LLM scores, with a gap exceeding 50 percentage points."

### Akhund 2026 (2)

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Gap analysis comparing human-derived success rates with normalised LLM scores (Supplementary Table S4, Figure S4). FN-Q16 required reasoning about three-dimensional spatial relationships from a two-dimensional photograph; Claude and Gemini assigned zero marks to all 309 students.

> "The largest gap was for FN-Q16 (pelvic 3D model): 93.28% of students answered correctly by human grading; however, the lowest LLM score was 0.0%, representing a performance gap of 93.3 percentage points."

### Akhund 2026 (3)

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Error analysis of discordant items in the same retrospective study. The divergence suggests ChatGPT applied an overly narrow lexical match against expected answer strings rather than evaluating semantic equivalence, a known limitation of zero-shot scoring.

> "FN-Q14 (ureter constrictions) was scored consistently high by the human graders Claude and Gemini, but ChatGPT classified it as low-performing (mean = 0.54), a pattern consistent with semantic inflexibility when multiple anatomically correct responses were acceptable."

## Discussion


## Related Claims
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — related
- [LLM factual errors during collaborative circuit debugging occurred almost exclusively after image inputs, attributed to limited 3D spatial reasoning from breadboard or PCB photos](llm-factual-errors-after-image-inputs-3d-reasoning.md) — related
- [LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models](multimodal-physics-accuracy-drops-to-74-percent.md) — related
