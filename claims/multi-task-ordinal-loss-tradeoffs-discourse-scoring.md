---
type: claim
title: Multi-task learning achieves near single-task performance with one joint model, and ordinal log-loss improves over cross-entropy and regression losses
description: Multi-task learning achieves near single-task performance with one joint model, and ordinal log-loss improves over cross-entropy and regression losses
id: multi-task-ordinal-loss-tradeoffs-discourse-scoring
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
  - id: ruikun-hou-2025-2
    resource: "https://doi.org/10.48550/arXiv.2505.07902"
    title: "Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)"
    author: Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci
    q: 3
    i: "?"
    kind: design
    rigour: 2
---

# Multi-task learning achieves near single-task performance with one joint model, and ordinal log-loss improves over cross-entropy and regression losses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Single-task specialists scored slightly higher (peak QWK 0.528 for Nature of Discourse), but multi-task learning showed only a marginal decrease while using a single shared model. [→ Ruikun Hou 2025](#ruikun-hou-2025)
`q3 i?` Ordinal log-loss (OLL) outperformed cross-entropy overall and beat L1 regression loss particularly on Questioning and Explanations. [→ Ruikun Hou 2025 (2)](#ruikun-hou-2025-2)

## Evidence

### Ruikun Hou 2025

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Ablation §5.2.2 on the text-audio setting: single-task specialists reached an overall QWK of 0.404 with "a peak QWK score of 0.528 for Nature of Discourse", while the joint model "constructs a single model for joint assessment" at 0.384 (Table 4).

> "However, multi-task learning constructs a single model for joint assessment with only a marginal de- crease in performance, revealing the efficiency and general- izability of the shared representation that learns the com- mon aspects of classroom discourse."

### Ruikun Hou 2025 (2)

Ruikun Hou, Babette Bühler, Tim Fütterer, Efe Bozkir, Peter Gerjets, Ulrich Trautwein, and Enkelejda Kasneci. (2025). Multimodal Assessment of Classroom Discourse Quality: A Text-Centered Attention-Based Multi-Task Learning Approach. arXiv preprint. [doi:10.48550/arXiv.2505.07902](https://doi.org/10.48550/arXiv.2505.07902)

`q3 · i?` · `design · r2`

Ablation §5.2.3 comparing losses under identical class weighting: multi-task OLL averaged 0.384, L1 regression 0.359, cross-entropy 0.332 (Table 4). The quote identifies where OLL's "additional improvement over L1 loss" was concentrated.

> "The use of OLL showed additional improvement over L1 loss, particularly in Questioning and Explanations."

## Discussion


## Related Claims
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
- [Fine-tuning LLMs and MLMs with cross-entropy loss using soft targets outperforms standard discretization and regression-head approaches on vocabulary difficulty prediction](soft-target-finetuning-beats-standard-loss-vocabulary-difficulty.md) — related
- [MSE loss performed at least as well as cross-entropy loss for pseudo-regression scoring of constructed response items](mse-loss-at-least-as-effective-as-cross-entropy.md) — related
- [In peer-assessment data from three courses, a multitask matrix factorization approach that jointly learns grades across assessment labels had lower error than a single-task (binary relevance) baseline in 8 of 10 comparisons.](multitask-matrix-factorization-outperforms-single-task-baseline.md) — related
