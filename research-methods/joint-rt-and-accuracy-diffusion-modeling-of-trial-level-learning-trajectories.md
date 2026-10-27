---
type: research-method
id: joint-rt-and-accuracy-diffusion-modeling-of-trial-level-learning-trajectories
title: Joint RT-and-accuracy diffusion modeling of trial-level learning trajectories
description: The article recommends analyzing learning with by-trial evidence-accumulation models fit to the joint distributions of response time and accuracy, rather than aggregating across sessions or relying on accuracy alone.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-26
---

# Joint RT-and-accuracy diffusion modeling of trial-level learning trajectories

> **Research Method** · [All research methods](index.md)
> **Evidence** · 4 claims (4 for) · 2 studies (1 causal, 1 associational), `q3` · 1 of 2 report an effect size · 4 claims rest on one study

## Description
The article recommends analyzing learning with by-trial evidence-accumulation models fit to the joint distributions of response time and accuracy, rather than aggregating across sessions or relying on accuracy alone. It argues that "using only impoverished discrete-choice behavioral data could prevent or bias possible inferences regarding learning trajectories". The approach provides a clear justification for using the diffusion model's drift rate parameter as an index of perceptual learning as a function of each training trial.

## Accounts
<!-- How each source describes or uses the method -->
- **Model learning with joint RT-and-accuracy diffusion models at the trial level rather than accuracy-only aggregated analyses**: The article recommends analyzing learning with by-trial evidence-accumulation models fit to the joint distributions of response time and accuracy, rather than aggregating across sessions or relying on accuracy alone. It argues that "using only impoverished discrete-choice behavioral data could prevent or bias possible inferences regarding learning trajectories". The approach provides a clear justification for using the diffusion model's drift rate parameter as an index of perceptual learning as a function of each training trial. (Cochrane et al. (2023))
- **Drift-diffusion model decomposition of working-memory decision processes**: The drift-diffusion model (DDM) is a perceptual decision-making framework that separates components hidden in raw accuracy and reaction-time data by modeling stochastic evidence accumulation from a starting point to a decision boundary. The article fits four parameters: drift rate (v, average evidence accumulation speed), decision boundary (a, response caution), bias (z, starting point), and nondecision time (t). The article states that "The DDM provides a robust framework for decomposing decision processes into distinct components," and uses it here to identify which component of working-memory performance mindfulness training changes. (Kou et al. (2025))

### Claims
- [Response time reliably decreased at all coherence levels while accuracy improved reliably only at intermediate coherence levels](../claims/rt-decreased-all-coherences-accuracy-intermediate.md) [+M]
- [Model comparison favors continuous drift rate with flexible response boundary over constant, fully continuous, and day-resetting alternatives](../claims/model-comparison-continuous-dr-flexible-rb.md) [+M]
- [Mindfulness training increases drift rates in the delayed match-to-sample task across emotional categories, indicating faster evidence accumulation](../claims/mindfulness-training-increases-drift-rate.md) [+M]
- [Mindfulness training does not change reaction times, decision boundary, or response bias, with only emotion-specific nondecision-time increases](../claims/mindfulness-training-leaves-other-ddm-parameters-unchanged.md) [+M]

## Related Research Methods
-

## Key Sources
- Cochrane, A., Sims, C. R., Bejjanki, V. R., Green, C. S., & Bavelier, D. (2023). Multiple timescales of learning indicated by changes in evidence-accumulation processes during perceptual decision-making. npj Science of Learning 8:19. https://doi.org/10.1038/s41539-023-00168-9
- Kou, H., Luo, W., Li, X. et al. (2025). Mindfulness training enhances face working memory: evidence from the drift-diffusion model. npj Science of Learning. https://doi.org/10.1038/s41539-025-00389-0
