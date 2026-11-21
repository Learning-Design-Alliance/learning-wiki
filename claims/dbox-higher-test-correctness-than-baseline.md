---
type: claim
title: In a within-subjects study (N=24), learners using DBox achieved significantly higher correctness scores on unassisted test problems than learners using freely chosen baseline tools
description: In a within-subjects study (N=24), learners using DBox achieved significantly higher correctness scores on unassisted test problems than learners using freely chosen baseline tools
id: dbox-higher-test-correctness-than-baseline
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: shuai-ma-2025
    title: Shuai Ma 2025
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In a within-subjects study (N=24), learners using DBox achieved significantly higher correctness scores on unassisted test problems than learners using freely chosen baseline tools

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Participants using DBox scored significantly higher on test-session correctness than in the baseline condition, per a linear mixed effects model. [→ Shuai Ma 2025](#shuai-ma-2025)

## Evidence

### Shuai Ma 2025

Shuai Ma, Junling Wang, Yuanhao Zhang, Xiaojuan Ma, and April Yi Wang. 2025. DBox: Scaffolding Algorithmic Programming Learning through Learner-LLM Co-Decomposition. In CHI Conference on Human Factors in Computing Systems (CHI '25). https://doi.org/10.1145/3706598.3713748

`q2 · i?` · `causal · r2`

Within-subjects user study with 24 participants comparing DBox against a baseline where participants freely used tools such as ChatGPT, Copilot, search engines, and LeetCode. The linear mixed effects model showed "correctness scores than those in the baseline condition" on unassisted test problems (Coef. = 0.198, p < 0.05).

> "participants using DBox achieved signifi- cantly higher correctness scores than those in the baseline condition (𝐶𝑜𝑒𝑓. =0.198,𝑝<0.05), suggesting that practicing with DBox bet- ter prepared learners to transfer their skills to similar algorithmic challenges"

## Discussion


## Related Claims
- [In math problem solving, a tutor-plus-peers LLM arrangement produced the strongest unassisted post-task test accuracy, with accuracy increasing monotonically from Control to Tutor + Peers](tutor-plus-peers-strongest-unassisted-math-accuracy.md) — related
- [AI access raises immediate unaided test scores by 7.2 percentage points (0.28 SD) after a timed learning phase](genai-access-raises-immediate-test-scores.md) — a broader claim this one bears on
- [In math problem solving, a tutor LLM alone significantly improved unassisted test accuracy over no-agent control, while peer-like error agents alone did not reach significance](tutor-alone-significant-peers-alone-not-math.md) — related
- [In a randomized experiment on fraction problems, participants who used an AI assistant solved fewer unassisted test problems and skipped more than control participants](ai-assistance-impairs-unassisted-fraction-performance-exp1.md) — reports the opposite
- [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 access in high-school mathematics raised assisted practice performance but left students worse off after withdrawal](gpt4-access-harms-learning-after-withdrawal.md) — reports the opposite
