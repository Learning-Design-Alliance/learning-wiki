---
type: product
id: trial-and-demonstration-tnd-framework
title: Trial-and-Demonstration (TnD) framework
description: A computational language-model training framework developed by Ma et al.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# Trial-and-Demonstration (TnD) framework

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A computational language-model training framework developed by Ma et al. that combines student trials, teacher demonstrations, corrective-feedback rewards, and alternating PPO/CLM updates to study word acquisition.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Trial-and-Demonstration (TnD) framework for interactive language learning**: The TnD framework simulates corrective-feedback-based language learning with three components: student model trials, teacher model demonstrations, and rewards. The student produces an utterance from a 5-token prompt, the teacher generates its own completion as a demonstration, and both are scored by an age-conditioned reward r = log(n̂/n) that rewards text emerging earlier than expected for the model's training-step 'age'. The student alternates interactive (PPO-based) and non-interactive (CLM) learning steps. The authors state the framework is "offering a general and unrestricted approach to simulate interactive language learning with corrective feedback." (Ziqiao Ma et al. (2025))

### Claims
- [TnD interactive learning with corrective feedback speeds word acquisition, especially in earlier training stages](../claims/tnd-accelerates-neural-word-acquisition.md) [+M]
- [Both trials and demonstrations contribute to accelerated word learning: demonstrations alone help, trials alone do not](../claims/trials-and-demonstrations-both-needed.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Ziqiao Ma, Zekun Wang, Joyce Chai. (2025). Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations. https://arxiv.org/abs/2405.13828
