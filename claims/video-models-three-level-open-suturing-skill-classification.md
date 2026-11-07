---
type: claim
title: "Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters"
description: "Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters"
id: video-models-three-level-open-suturing-skill-classification
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
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
  - id: hoffmann-hanna-2024-2
    resource: "https://doi.org/10.1007/s11548-024-03093-3"
    title: "Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3"
    author: Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Temporal segment network models with I3D and Video Swin backbones achieved F1 scores of up to 72% and accuracies of 75% on three-class open suturing skill classification. [→ Hoffmann Hanna 2024](#hoffmann-hanna-2024)
`q2 i?` Model performance was similar to that of individual human raters, whose rater mean macro F1 was 0.7356 versus the Video Swin Tiny model's 0.7157. [→ Hoffmann Hanna 2024 (2)](#hoffmann-hanna-2024-2)

## Evidence

### Hoffmann Hanna 2024

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q2 · i?` · `design · r2`

Benchmarking of TSN models with I3D and Video Swin backbones on the AIxSuture test split, trained for 400 epochs with three runs per experiment. The article reports "F1 scores of up to 72% and accuracies of 75%", with classwise variation shown in Table 1.

> "Overall performance of the models was good, achieving F1 scores of up to 72% and accuracies of 75%. For all tested backbones, model performance varied by class as can be seen in Table 1."

### Hoffmann Hanna 2024 (2)

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q2 · i?` · `design · r2`

Rater baseline analysis on the same test videos, discretizing each rater's GRS into the same three classes and computing classwise F1, macro F1 and accuracy (Table 3). Rater A's macro F1 of 0.7978 was best; the article states "scoring by rater A was the closest to the ground truth".

> "Overall, scoring by rater A was the closest to the ground truth classification for a given video."

## Discussion


## Related Claims
- [Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class](intermediate-skill-class-hardest-to-classify.md) — related
- [Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models](shorter-snippet-lengths-aid-skill-assessment.md) — related
- [A CNN-LSTM deep learning network classifies suturing versus dissection actions from robotic cardiac surgery simulation video with 93% test accuracy](dl-action-recognition-93-percent-robotic-cardiac-wetlab.md) — related
- [The skill assessment network distinguishing novice from expert surgeons reached only 56% test accuracy, failing to achieve useful performance](skill-assessment-network-56-percent-accuracy-failed.md) — related
- [In the narrative synthesis, deep learning models classify surgeon skill levels from kinematic data with accuracy up to 95.4%](deep-learning-skill-classification-up-to-95-percent.md) — related
