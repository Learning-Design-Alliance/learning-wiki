---
type: claim
title: Concise expert-written explanations significantly outperform both self-learning and pipeline-generated explanations among high-baseline learners
description: Concise expert-written explanations significantly outperform both self-learning and pipeline-generated explanations among high-baseline learners
id: expert-explanations-benefit-high-baseline-learners
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
    i: 3
    kind: causal
    rigour: 2
  - id: lun-ai-2025-2
    resource: "https://doi.org/10.48550/arXiv.2509.00961"
    title: "Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)"
    author: Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton
    q: 3
    i: 3
    kind: causal
    rigour: 2
---

# Concise expert-written explanations significantly outperform both self-learning and pipeline-generated explanations among high-baseline learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i3` large
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Lun Ai 2025: the intervention came bundled with another change · Lun Ai 2025 (2): the intervention came bundled with another change (read from the study by two models, 2026-11-21)

## Subclaims
`q3 i3` Among high-baseline participants in the electric circuits domain, expert-written explanations (Hr) significantly outperformed control (d = 1.08) and pipeline-generated explanations (d = 0.97), while pipeline explanations did not differ from control. [→ Lun Ai 2025](#lun-ai-2025)
`q3 i3` In list binary search, high-baseline engaged readers showed a significant Hr advantage over control (d = 1.35) and over pipeline explanations (d = 1.31). [→ Lun Ai 2025 (2)](#lun-ai-2025-2)

## Evidence

### Lun Ai 2025

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q3 · i3` · `causal · r2`

Exploratory subgroup analysis of the human trial: high-baseline participants (n=56) split by median on first-trial performance, in the electric circuits domain. Among high-baseline participants, Kruskal-Wallis indicated a significant condition effect (H(2) = 8.23, p=.016); the article reports "expert-written explanations based on the learned programs (Hr) significantly outperformed control".

> "Post-hoc Mann-Whitney U-tests with FDR correction showed that expert-written explanations based on the learned programs (Hr) significantly outperformed control (pF DR=.046,d= 1.08) and pipeline-generated explanations (pF DR=.038,d= 0.97)."

### Lun Ai 2025 (2)

Lun Ai, Johannes Langer, Ute Schmid, and Stephen Muggleton. (2025). Ultra Strong Machine Learning: LLM-Generated Explanations Do Not Yet Suffice for Teaching Humans Active Learning Strategy. arXiv preprint. [doi:10.48550/arXiv.2509.00961](https://doi.org/10.48550/arXiv.2509.00961)

`q3 · i3` · `causal · r2`

Exploratory subgroup analysis combining a median split on reading time (engaged/quick) with baseline, for list binary search (Figure 5b, High Baseline + Engaged, n=28). The article reports a "significantHr advantage over control" with d = 1.35 and over pipeline explanations with d = 1.31.

> "For list binary search (Figure 5b), high-baseline engaged readers showed a significantHr advantage over control (pF DR=.046, d= 1.35) andH 2 (pF DR=.046,d= 1.31)."

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims
- [Pipeline-generated LLM explanations of an ILP-learned active learning strategy do not improve human task performance over self-learning in any of three domains](llm-pipeline-explanations-no-advantage-over-self-learning.md) — related
- [Initial performance interacts with explanation condition in affecting electric-circuit task performance](initial-performance-condition-interaction-circuits.md) — a broader claim this one bears on
- [Reviews report that the split-attention benefit for novices reverses into a redundancy effect for more experienced learners: Kalyuga et al. (2003) cite Kalyuga et al. (1998) and Yeung et al. (1998), and Ginns (2006) cites Kalyuga et al. (1998)](expertise-reversal-split-attention-redundancy-review.md) — related
