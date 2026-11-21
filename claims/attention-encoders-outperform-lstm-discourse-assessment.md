---
type: claim
title: Attention-based encoders outperform LSTM-based encoders for multimodal discourse assessment in overall and component-level performance except Nature of Discourse
description: Attention-based encoders outperform LSTM-based encoders for multimodal discourse assessment in overall and component-level performance except Nature of Discourse
id: attention-encoders-outperform-lstm-discourse-assessment
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

# Attention-based encoders outperform LSTM-based encoders for multimodal discourse assessment in overall and component-level performance except Nature of Discourse

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` In the ablation study, the attention-based encoder outperformed the LSTM-based encoder on Questioning, Explanations, and overall performance, though not on Nature of Discourse. [→ Ruikun Hou 2025](#ruikun-hou-2025)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Ablation study (§5.2.1) on the best text-audio configuration, altering one element at a time under the same cross-validation conditions. Table 4 shows the attention model's overall QWK (0.384) versus the LSTM model's (0.319); the text names the one exception explicitly.

> "Except for Nature of Discourse, the attention-based encoder (last row in Table 4) outperformed the LSTM-based model (first row) across other components and in overall performance."

## Discussion


## Related Claims
- [Attention-based neural classifiers outperformed vanilla neural models on Bloom's taxonomy question classification](attention-models-beat-vanilla-neural-baselines.md) — related
- [Almost all neural network models benefit from adding handcrafted wLDA and online dialogue features](handcrafted-features-improve-neural-argument-classifiers.md) — related
