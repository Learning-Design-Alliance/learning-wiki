---
type: research-method
id: swim-proficiency-conditioned-essay-generation-and-proficiency-alignment-evaluation
title: "SWIM: proficiency-conditioned essay generation and proficiency-alignment evaluation"
description: "SWIM formalizes student writing simulation as proficiency-conditioned essay generation: given a writing prompt and a target trait-score profile, a generator produces an essay exhibiting the specified writing behavior, and \"an AES-based evaluation framework for\" measuring profile alignment scores the"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# SWIM: proficiency-conditioned essay generation and proficiency-alignment evaluation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 5 claims (4 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
SWIM formalizes student writing simulation as proficiency-conditioned essay generation: given a writing prompt and a target trait-score profile, a generator produces an essay exhibiting the specified writing behavior, and "an AES-based evaluation framework for" measuring profile alignment scores the output with a frozen multi-trait AES verifier using QWK. The authors train generators via SFT on real (essay, profile) pairs and then refine them with GRPO using the Proficiency Alignment Reward, a dense per-sample reward based on trait-normalized accuracy against the target profile.

## Accounts
<!-- How each source describes or uses the method -->
- **SWIM: proficiency-conditioned essay generation task with AES-based profile-alignment evaluation and the Proficiency Alignment Reward**: SWIM formalizes student writing simulation as proficiency-conditioned essay generation: given a writing prompt and a target trait-score profile, a generator produces an essay exhibiting the specified writing behavior, and "an AES-based evaluation framework for" measuring profile alignment scores the output with a frozen multi-trait AES verifier using QWK. The authors train generators via SFT on real (essay, profile) pairs and then refine them with GRPO using the Proficiency Alignment Reward, a dense per-sample reward based on trait-normalized accuracy against the target profile. (Heejin Do et al. (2026))

### Claims

- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](../claims/sft-improves-proficiency-alignment-over-prompting.md) [+M]
- [GRPO with the Proficiency Alignment Reward improves alignment over SFT across every writing trait and essay prompt](../claims/grpo-par-improves-alignment-across-all-traits.md) [+M]
- [SFT and GRPO alignment gains reflect learned proficiency-conditioned generation rather than memorization or output collapse](../claims/no-memorization-or-generation-collapse-in-trained-simulators.md) [+W]
- [Data scarcity and long-form generation remain bottlenecks: on Prompt 8 prompting outperforms SFT and GRPO](../claims/data-scarcity-and-length-bottleneck-prompt-8.md) [~W]
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](../claims/prompting-collapses-proficiency-variation-toward-idealized-students.md) [+W]

## Related Research Methods
-

## Key Sources
- Heejin Do, Jakub Kontak, Mrinmaya Sachan. (2026). SWIM: Student Writing Simulation via Proficiency-Conditioned Generation. arXiv preprint arXiv:2609.03215. https://arxiv.org/abs/2609.03215
