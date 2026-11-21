---
type: claim
title: Text alone surpasses human inter-rater reliability for assessing discourse quality, especially on high-inference components
description: Text alone surpasses human inter-rater reliability for assessing discourse quality, especially on high-inference components
id: text-modality-surpasses-human-irr-discourse
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

# Text alone surpasses human inter-rater reliability for assessing discourse quality, especially on high-inference components

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The transcript-only model achieved the highest unimodal overall QWK (0.356), exceeding human IRR (0.326), and was strongest on Questioning and Explanations. [→ Ruikun Hou 2025](#ruikun-hou-2025)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Unimodal results from the same teacher-independent nested 5-fold cross-validation over GTI Germany segments (§5.1.2). The text-only model's "highest overall score of 0.356" beat human agreement; per-component QWKs are printed in Table 3 (e.g., 0.387 for Questioning).

> "Among unimodal approaches, the highest overall score of 0.356 was observed in the textural pathway, surpassing human IRR. Its strength lies in the effective assessment of the higher-inference components (Questioning and Explanations)."

## Discussion


## Related Claims
- [Text-audio fusion yields the best discourse-quality prediction (average QWK 0.384), exceeding human inter-rater reliability of 0.326 on the GTI Germany dataset](text-audio-fusion-qwk-0-384-exceeds-human-irr.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [Video features underperform for discourse-quality assessment, with an average QWK of 0.138 across components](video-modality-underperforms-discourse-assessment.md) — related
