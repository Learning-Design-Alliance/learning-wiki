---
type: product
id: omniedu-capability-oriented-instruction-tuning-corpus
title: OmniEdu capability-oriented instruction-tuning corpus
description: The OmniEdu corpus is a curated, audited, diverse instruction-tuning dataset for education-focused language models, created by Hao Liang et al.
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# OmniEdu capability-oriented instruction-tuning corpus

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The OmniEdu corpus is a curated, audited, diverse instruction-tuning dataset for education-focused language models, created by Hao Liang et al. from educational datasets and resources.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **OmniEdu capability-oriented instruction-tuning corpus and six-stage data pipeline**: A reproducible data-construction pipeline that curates an education-specific pool of approximately 1.34M examples drawn from more than 100 datasets and educational resources into 60,951 high-quality examples containing about 12.0M supervised response tokens. The six stages combine deterministic cleaning and evaluation decontamination, LLM-assisted semantic auditing and rewriting with 0-100 usability scoring, task-specific quality scoring, k-center greedy diversity selection over BGE-M3 embeddings under token budgets, and pedagogical instruction assignment. Together with 9,048 general-purpose examples, the final corpus contains 69,999 examples and 15.96M supervised response tokens, with provenance and audit metadata retained throughout. (Hao Liang et al. (2026))

### Claims

- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](../claims/omniedu-tuning-improves-all-three-educational-capability-groups.md) [+M]
- [Education-oriented tuning improves authentic K-12 problem solving, with OmniEdu-27B's MDK12-Bench open-question correctness rising from 62.08% to 78.77%](../claims/omniedu-k12-problem-solving-gains.md) [+W]
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](../claims/omniedu-general-capability-retained-after-specialization.md) [+W]

## Related Products and Programmes

- [K12-Train](k12-train.md)
- [Open audit dataset of 1,800 LLM history-tutor responses across five personas](open-audit-dataset-of-1800-llm-history-tutor-responses-across-five-personas.md)

## Key Sources
- Hao Liang, Qihan Lin, Meiyi Qiang, Linzhuang Sun, Hengyi Feng, Mingrui Chen, Sizhe Qiu, Wentao Zhang. (2026). OmniEdu: Open Foundation Models for Learning and Teaching. https://arxiv.org/abs/2609.23088
