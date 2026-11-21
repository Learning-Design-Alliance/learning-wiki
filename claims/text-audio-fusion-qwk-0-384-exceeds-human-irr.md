---
type: claim
title: Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset
description: Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset
id: text-audio-fusion-qwk-0-384-exceeds-human-irr
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ruikun-hou-2025
    resource: "https://doi.org/10.48550/arXiv.2505.07902"
    title: "Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)"
    author: Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Integrating audio signals into the textual context produced the highest overall QWK (0.384) among tested modality configurations, surpassing the human inter-rater reliability of 0.326. [→ Ruikun Hou 2025](#ruikun-hou-2025)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Cross-validated model comparison (teacher-independent nested 5-fold) on 367 16-minute segments from 92 GTI Germany math lessons. The results section reports that text-audio fusion "yielded the best average QWK score of 0.384 among all tested modalities"; human IRR was 0.326 (Table 3). No standardized effect size is printed.

> "Integrating audio signals into the textural context yielded the best average QWK score of 0.384 among all tested modalities, particularly with a notable performance boost in the Nature of Discourse component."

## Discussion


## Related Claims
- [Text alone surpasses human inter-rater reliability for assessing discourse quality, especially on high-inference components](text-modality-surpasses-human-irr-discourse.md) — related
- [Video features underperform for discourse-quality assessment, with an average QWK of 0.138 across components](video-modality-underperforms-discourse-assessment.md) — related
- [Model-predicted discourse scores show weak but partially human-aligned correlations with student outcomes, including a positive link between Explanations and achievement](predicted-discourse-scores-correlate-weakly-student-outcomes.md) — related
