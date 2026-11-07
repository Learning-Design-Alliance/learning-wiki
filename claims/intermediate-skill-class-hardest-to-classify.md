---
type: claim
title: Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class
description: Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class
id: intermediate-skill-class-hardest-to-classify
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

# Novice and proficient suturing skill classes are easier for models and raters to classify than the intermediate class

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Classwise F1 was markedly lower for the intermediate class than for novice and proficient classes across all tested backbones. [→ Hoffmann Hanna 2024](#hoffmann-hanna-2024)
`q2 i?` Model misclassifications were typically border cases near the class delimiters of 16 and 24, and half of the Video Swin Tiny model's fourteen misclassified videos involved rater disagreement. [→ Hoffmann Hanna 2024 (2)](#hoffmann-hanna-2024-2)

## Evidence

### Hoffmann Hanna 2024

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q2 · i?` · `design · r2`

Classwise F1 on the unseen test set (Table 1): e.g., I3D scored 0.8571 novice, 0.4030 intermediate, 0.7514 proficient. The article states "Novice and proficient classes were easier for the models to classify than the intermediate class."

> "Novice and proficient classes were easier for the models to classify than the intermediate class."

### Hoffmann Hanna 2024 (2)

Hoffmann Hanna, Funke Isabel, Peters Philipp, Venkatesh Danush Kumar, Egger Jan, Rivoir Dominik, Röhrig Rainer, Hölzle Frank, Bodenstedt Sebastian, Willemer Marie-Christin, Speidel Stefanie, Puladi Behrus. (2024). AIxSuture: vision-based assessment of open suturing skills. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-024-03093-3

`q2 · i?` · `design · r2`

Error analysis with the Video Swin Tiny model using majority voting over three runs (Fig. 5). The article found misclassifications typically involved border cases near GRS 16 and 24, and reports that "seven videos had a disagreement of at least one rater".

> "The Video Swin Tiny model classified fourteen videos incorrectly. Of those misclassifications, seven videos had a disagreement of at least one rater."

## Discussion


## Related Claims
- [Deep learning models classify open suturing videos into three skill levels with up to 75% accuracy and 72% F1, comparable to individual human raters](video-models-three-level-open-suturing-skill-classification.md) — related
- [Random Forest most accurately predicts novices' visual behavior levels from CV-DL-extracted metrics, with fixation rates on objects and tool speed as key predictors](random-forest-predicts-visual-behavior-levels.md) — related
- [Shorter video snippet lengths with more segments improved skill classification for the I3D and Video Swin Tiny models](shorter-snippet-lengths-aid-skill-assessment.md) — related
