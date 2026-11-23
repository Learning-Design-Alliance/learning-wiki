---
type: claim
title: SEC remains effective when curriculum categories are automatically inferred from empirical success rates rather than manual difficulty labels
description: SEC remains effective when curriculum categories are automatically inferred from empirical success rates rather than manual difficulty labels
id: sec-works-with-inferred-curriculum-categories
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: xiaoyin-chen-2025
    resource: "https://doi.org/10.52202/085713-4647"
    title: "Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo. (2025). Self-Evolving Curriculum for LLM Reasoning. arXiv preprint. [doi:10.52202/085713-4647](https://doi.org/10.52202/085713-4647)"
    author: Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# SEC remains effective when curriculum categories are automatically inferred from empirical success rates rather than manual difficulty labels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SEC variants using k=3 and k=5 equal-width bins of empirical success rates outperform the random baseline on MATH500, AMC22-23, and AIME24. [→ Xiaoyin Chen 2025](#xiaoyin-chen-2025)

## Evidence

### Xiaoyin Chen 2025

Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo. (2025). Self-Evolving Curriculum for LLM Reasoning. arXiv preprint. [doi:10.52202/085713-4647](https://doi.org/10.52202/085713-4647)

`q2 · i?` · `causal · r2`

Mathematics RL fine-tuning experiment (Section 3.5, Table 4) using success rates estimated by sampling from Qwen2.5-MATH-7B, discretized into k=3 and k=5 equal-width bins; e.g., AMC22-23 0.389 (k=3) and 0.358 (k=5) vs random 0.312. The paper reports that "Both SEC variants outperform the random base- line on the three math benchmarks."

> "SEC remains effective when curriculum categories are derived from empirical success rates rather than manual labels."

## Discussion


## Related Claims
- SEC-2D, with one arm per problem-type × difficulty combination, outperforms random curricula and stabilizes multi-task RL fine-tuning across three reasoning domains — related
- SEC's advantage over random curricula is smaller for stronger base models but re-emerges when task difficulty increases — related
- [SEC improves OOD generalization of RL fine-tuned LLMs over random and difficulty-ordered curricula across planning, inductive reasoning, and mathematics tasks](sec-improves-ood-generalization-over-random-curriculum.md) — related
- [LLM-assigned difficulty labels fail to predict empirical item difficulty in classroom retrieval practice (ρ=0.06), as do co-generated Bloom levels (ρ=0.02)](llm-difficulty-labels-fail-to-predict-empirical-item-difficulty.md) — related
