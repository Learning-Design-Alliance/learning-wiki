---
type: research-method
id: reinforcement-learning-measurement-model-rlmm
title: Reinforcement Learning Measurement Model (RLMM)
description: "The RLMM is a psychometric measurement framework for sequential process data that treats a person's inverse-temperature parameter βj as an ability to choose higher-valued actions under a Boltzmann policy."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Reinforcement Learning Measurement Model (RLMM)

> **Research Method** · [All research methods](index.md)
> **Evidence** · 7 claims (7 for) · 2 studies (1 causal, 1 design), `q2`–`q3` · 2 of 2 report an effect size · 7 claims rest on one study

## Description
The RLMM is a psychometric measurement framework for sequential process data that treats a person's inverse-temperature parameter βj as an ability to choose higher-valued actions under a Boltzmann policy. It replaces the MDP-MM's person-specific tabular value functions with "a shared parametric action-value function Qθ(s,a)", using centered and globally normalized advantages, a soft Bellman-consistency penalty encoding known task dynamics, and a block-coordinate MAP estimation procedure. It also yields step-level influence diagnostics that identify behaviorally critical decisions.

## Accounts
<!-- How each source describes or uses the method -->
- **Reinforcement Learning Measurement Model (RLMM)**: The RLMM is a psychometric measurement framework for sequential process data that treats a person's inverse-temperature parameter βj as an ability to choose higher-valued actions under a Boltzmann policy. It replaces the MDP-MM's person-specific tabular value functions with "a shared parametric action-value function Qθ(s,a)", using centered and globally normalized advantages, a soft Bellman-consistency penalty encoding known task dynamics, and a block-coordinate MAP estimation procedure. It also yields step-level influence diagnostics that identify behaviorally critical decisions. (Wenqian Xu (2026))
- **Dual-system reinforcement learning framework: model-based versus model-free strategies**: The article adopts the dual-system RL framework in which "the model-based strategy is characterized by its ﬂexibility and is typically driven by speciﬁc goals, taking current states into account", while "the model-free strategy is more efﬁcient and resource-conserving" and driven by habits and immediate rewards. A validated computational model estimates parameters — learning rate, eligibility trace, inverse temperature, and a mixing weight — that quantify each learner's reliance on the two systems in a two-stage task. The article uses this framework to show that WM load arbitrates between the strategies. (Chengyan Yang et al. (2025))

### Claims
- [In peg-solitaire simulations with known true abilities, the RLMM attains lower RMSE of log βj than the MDP-MM on all four original boards](../claims/rlmm-lower-rmse-than-mdp-mm-peg-solitaire.md) [+M]
- [RLMM runtime stays within approximately 15–20 seconds across the four peg-solitaire boards while MDP-MM runtime grows with task complexity, reaching a 19.1× speedup on the diamond board](../claims/rlmm-stable-runtime-speedup-growing-complexity.md) [+M]
- [The RLMM recovers ability parameters on peg-solitaire boards with up to more than 23 million states, where tabular MDP-MM estimation is impractical](../claims/rlmm-scales-to-millions-of-states.md) [+M]
- [In AQUALAB gameplay logs, the estimated RLMM person parameter is positively associated with cumulative trajectory reward (Pearson 0.5842, Spearman 0.5760)](../claims/aqualab-beta-associated-with-cumulative-reward.md) [+M]
- [Influence-function diagnostics identify steps 3–8 of the Big-L peg-solitaire board as the most consequential region, with the lowest-β participants showing substantially larger absolute influence values there](../claims/rlmm-influence-diagnostics-big-l-steps-3-8.md) [+W]
- [In AQUALAB, estimated β is ordered across episode completion status (means 1.181, 1.506, 2.343; Kruskal–Wallis p = 8.62×10−29) and higher-β quintiles complete more content more efficiently](../claims/aqualab-beta-completion-and-efficiency.md) [+W]
- [High WM load shifts learners from model-based toward model-free reinforcement learning strategies](../claims/high-wm-load-shifts-to-model-free-strategy.md) [+M]

## Related Research Methods
-

## Key Sources
- Wenqian Xu, Feng Ji. (2026). Reinforcement Learning Measurement Model. arXiv. https://arxiv.org/abs/2605.09305
- Chengyan Yang, Tongran Liu, Mengxin Wen & Xun Liu. (2025). The distinct functions of working memory and intelligence in model-based and model-free reinforcement learning. npj Science of Learning 10:72. https://doi.org/10.1038/s41539-025-00363-w
