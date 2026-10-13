---
type: product
id: special-r1
title: Special-R1
description: Special-R1 is a released artifact suite comprising a ZPD-filtered multi-domain tutoring corpus, the SPED-Tutor-Mix disability-aware evaluation set, seven model checkpoints, and an evaluation pipeline created by Unggi Lee et al.
product_kind: dataset
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Special-R1

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
Special-R1 is a released artifact suite comprising a ZPD-filtered multi-domain tutoring corpus, the SPED-Tutor-Mix disability-aware evaluation set, seven model checkpoints, and an evaluation pipeline created by Unggi Lee et al.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Released Special-R1 artifacts: multi-domain ZPD-filtered corpus, SPED-Tutor-Mix evaluation set, seven checkpoints, and disability-aware evaluation pipeline**: The article releases the training and evaluation artifacts behind Special-R1. The training corpus contains approximately 54k problems across four domains (mathematics, reading comprehension, social reasoning, life skills), filtered to a ZPD window of 1-60% solve rate by the Llama-3.1-8B student simulator and annotated with baseline accuracy. The evaluation set is the persona-augmented SPED-Tutor-Mix test split in which "every item carries a disability profile so that persona-aware metrics can be computed." The disability rubric is released as disability_types.yaml alongside the code, together with all seven model checkpoints and the evaluation pipeline. (Unggi Lee et al. (2026))

### Claims

- [The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline](../claims/special-r1-raises-persona-fit-and-sped-helpfulness.md) [+W]
- [Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM](../claims/sped-training-no-ood-knowledge-cost.md) [+W]
- [Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models](../claims/sld-math-weakest-persona-profile.md) [-W]

## Related Products and Programmes

- [Open audit dataset of 1,800 LLM history-tutor responses across five personas](open-audit-dataset-of-1800-llm-history-tutor-responses-across-five-personas.md)

## Key Sources
- Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670
