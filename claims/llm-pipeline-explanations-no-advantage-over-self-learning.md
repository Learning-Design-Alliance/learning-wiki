---
type: claim
title: Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains
description: Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains
id: llm-pipeline-explanations-no-advantage-over-self-learning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: lun-ai-2025
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Lun Ai 2025: the intervention came bundled with another change (read from the study by two models, 2026-11-21)

## Subclaims
`q3 i?` Across electric circuits, waterflow, and list binary search trial items, condition (self-learning vs pipeline explanations vs expert explanations) had no significant effect on performance. [→ Lun Ai 2025](#lun-ai-2025)

## Evidence

### Lun Ai 2025

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q3 · i?` · `causal · r2`

Pre-registered human trial on Prolific with 144 analyzed participants (40 self-learning H1, 62 pipeline-explanation H2, 42 expert-explanation Hr), Kruskal-Wallis H-tests with FDR correction per domain. The article reports "no significant effect of condition on performance in any domain"; equivalence was not tested.

> "Test results revealed no significant effect of condition on performance in any domain (electric circuits: H(2) = 2.28, p=.32; waterflow: H(2) = 0.33, p=.85; list binary search: H(2) = 1.77, p=.41)."

## Discussion


## Related Claims
- [Concise expert-written explanations significantly outperform both self-learning and pipeline-generated explanations among high-baseline learners](expert-explanations-benefit-high-baseline-learners.md) — related
- [Initial performance interacts with explanation condition in affecting electric-circuit task performance](initial-performance-condition-interaction-circuits.md) — related
- [LLM judges rate pipeline-generated explanations higher than direct prompting and hand-crafted templates across USML domains](llm-judges-rate-pipeline-explanations-higher.md) — related
- [LLM quality metrics do not predict human learning outcomes from explanations](llm-quality-metrics-do-not-predict-human-learning.md) — related
