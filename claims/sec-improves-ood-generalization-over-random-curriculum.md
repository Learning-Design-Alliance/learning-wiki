---
type: claim
title: SEC improves OOD generalization of RL fine-tuned LLMs over random and difficulty-ordered curricula across planning, inductive reasoning, and mathematics tasks
description: SEC improves OOD generalization of RL fine-tuned LLMs over random and difficulty-ordered curricula across planning, inductive reasoning, and mathematics tasks
id: sec-improves-ood-generalization-over-random-curriculum
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

# SEC improves OOD generalization of RL fine-tuned LLMs over random and difficulty-ordered curricula across planning, inductive reasoning, and mathematics tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For Qwen2.5-3B, SEC improves OOD accuracy on Countdown by approximately 13% relative over random and approximately 69% relative over the difficulty-ordered curriculum. [→ Xiaoyin Chen 2025](#xiaoyin-chen-2025)
`q2 i?` SEC attains approximately 21% relative OOD improvement on Zebra puzzles and approximately 33% relative improvement on AIME24 over the random baseline for Qwen2.5-3B. [→ Xiaoyin Chen 2025](#xiaoyin-chen-2025)

## Evidence

### Xiaoyin Chen 2025

Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo. (2025). Self-Evolving Curriculum for LLM Reasoning. arXiv preprint. [doi:10.52202/085713-4647](https://doi.org/10.52202/085713-4647)

`q2 · i?` · `causal · r2`

RL fine-tuning experiments (Results, Table 1) fine-tuning Qwen2.5-3B and 7B with GRPO, comparing SEC against random and difficulty-ordered curricula, reporting pass@1 averaged over 8 generations. The paper reports "approximately 13% relative (0.48 → 0.54)" on Countdown OOD, plus 21% on Zebra and 33% on AIME24.

> "on Countdown, SEC significantly improves OOD accuracy by approximately 13% relative (0.48 → 0.54) compared to the random baseline, and by approximately 69% relative (0.32 → 0.54) compared to the difficulty-ordered baseline."

## Discussion


## Related Claims
- SEC-2D, with one arm per problem-type × difficulty combination, outperforms random curricula and stabilizes multi-task RL fine-tuning across three reasoning domains — possibly the same claim (merge candidate)
- SEC's advantage over random curricula is smaller for stronger base models but re-emerges when task difficulty increases — related
- [SEC remains effective when curriculum categories are automatically inferred from empirical success rates rather than manual difficulty labels](sec-works-with-inferred-curriculum-categories.md) — related
