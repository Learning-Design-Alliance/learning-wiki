---
type: claim
title: Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models
description: Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models
id: shorter-snippet-lengths-aid-skill-assessment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: hoffmann-hanna-2024
    resource: "https://doi.org/10.1007/s11548-024-03093-3"
    title: "Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3"
    author: Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Increasing snippet length did not uniformly increase performance; I3D and Video Swin Tiny performed better with shorter snippet lengths, suggesting fine action details aid interpretation. [→ Hoffmann Hanna 2024](#hoffmann-hanna-2024)

## Evidence

### Hoffmann Hanna 2024

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q2 · i?` · `design · r2`

Ablation over snippet lengths and segment counts on the test set (Table 2), with each experiment run three times. The article reports that "The I3D and Video Swin Tiny models showed better performance with shorter snippet lengths."

> "Surprisingly, increasing the snippet length, and thereby increasing the amount of information the model sees at one time, does not result in increased model performance across the board. The I3D and Video Swin Tiny models showed better performance with shorter snippet lengths."

## Discussion


## Related Claims
- [Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters](video-models-three-level-open-suturing-skill-classification.md) — related
- [Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class](intermediate-skill-class-hardest-to-classify.md) — related
