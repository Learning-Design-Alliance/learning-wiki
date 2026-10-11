---
type: product
id: omniedu-capability-oriented-instruction-tuning-corpus
title: OmniEdu capability-oriented instruction-tuning corpus
description: The OmniEdu corpus is a curated, audited, diverse instruction-tuning dataset for education-focused language models, created by Hao Liang et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# OmniEdu capability-oriented instruction-tuning corpus

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The OmniEdu corpus is a curated, audited, diverse instruction-tuning dataset for education-focused language models, created by Hao Liang et al. from educational datasets and resources.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **OmniEdu capability-oriented instruction-tuning corpus and six-stage data pipeline**: A reproducible data-construction pipeline that curates an education-specific pool of approximately 1.34M examples drawn from more than 100 datasets and educational resources into 60,951 high-quality examples containing about 12.0M supervised response tokens. The six stages combine deterministic cleaning and evaluation decontamination, LLM-assisted semantic auditing and rewriting with 0-100 usability scoring, task-specific quality scoring, k-center greedy diversity selection over BGE-M3 embeddings under token budgets, and pedagogical instruction assignment. Together with 9,048 general-purpose examples, the final corpus contains 69,999 examples and 15.96M supervised response tokens, with provenance and audit metadata retained throughout. (Hao Liang et al. (2026))

### Claims
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](../claims/omniedu-tuning-improves-all-three-educational-capability-groups.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088
