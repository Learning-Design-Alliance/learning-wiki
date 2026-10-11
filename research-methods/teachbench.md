---
type: research-method
id: teachbench
title: TeachBench
description: TeachBench evaluates LLMs as teacher agents by having them conduct multi-turn instruction over structured knowledge points derived from an exam syllabus, with a fixed-capability student agent as a learner proxy.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# TeachBench

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
TeachBench evaluates LLMs as teacher agents by having them conduct multi-turn instruction over structured knowledge points derived from an exam syllabus, with a fixed-capability student agent as a learner proxy. Teaching effectiveness is "assessed by the student's performance improvement after instruction", enabling controlled comparison across teacher agents. Restricting teachers to knowledge points and example problems "avoids information leakage and enables reuse of existing benchmarks". The workflow has three stages: knowledge structuring, a teaching loop, and evaluation.

## Accounts
<!-- How each source describes or uses the method -->
- **TeachBench: a syllabus-grounded framework measuring LLM teaching capability via post-instruction student performance improvement**: TeachBench evaluates LLMs as teacher agents by having them conduct multi-turn instruction over structured knowledge points derived from an exam syllabus, with a fixed-capability student agent as a learner proxy. Teaching effectiveness is "assessed by the student's performance improvement after instruction", enabling controlled comparison across teacher agents. Restricting teachers to knowledge points and example problems "avoids information leakage and enables reuse of existing benchmarks". The workflow has three stages: knowledge structuring, a teaching loop, and evaluation. (Zheng Li et al. (2026))

### Claims
- [Multi-turn teaching by LLM teacher agents yields larger student gains than knowledge-point exposure alone](../claims/multi-turn-teaching-beats-knowledge-point-exposure.md) [+M]
- [Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction](../claims/example-problems-degrade-llm-teaching.md) [+M]
- [LLM teaching effectiveness varies substantially across subject domains, strongest where knowledge points apply directly and weakest in physics and chemistry](../claims/llm-teaching-effectiveness-varies-by-domain.md) [+M]

## Related Research Methods
-

## Key Sources
- Zheng Li, Siyao Song, Jingyuan Ma, Rui Li, Ying Zeng, Minghao Li, Zhifang Sui. (2026). TeachBench: A Syllabus-Grounded Framework for Evaluating Teaching Ability in Large Language Models. https://arxiv.org/abs/2601.21375
