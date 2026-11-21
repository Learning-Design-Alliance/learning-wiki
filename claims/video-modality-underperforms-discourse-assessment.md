---
type: claim
title: Video features underperform for discourse-quality assessment, with an average QWK of 0.138 across components
description: Video features underperform for discourse-quality assessment, with an average QWK of 0.138 across components
id: video-modality-underperforms-discourse-assessment
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

# Video features underperform for discourse-quality assessment, with an average QWK of 0.138 across components

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The video-only pathway underperformed on all three discourse components (average QWK 0.138), and adding video did not improve over the text-audio combination. [→ Ruikun Hou 2025](#ruikun-hou-2025)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Unimodal comparison in §5.1.2 on the GTI Germany cross-validation setup. The results text reports the video pathway "with an average QWK score of 0.138"; Table 3 also shows T+A+V (0.364) below T+A (0.384).

> "In contrast, the video modality un- derperformed across all components, with an average QWK score of 0.138, indicating the low dependency of the discourse assessment on visual cues."

## Discussion


## Related Claims
- [Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset](text-audio-fusion-qwk-0-384-exceeds-human-irr.md) — related
- [Text alone surpasses human inter-rater reliability for assessing discourse quality, especially on high-inference components](text-modality-surpasses-human-irr-discourse.md) — related
