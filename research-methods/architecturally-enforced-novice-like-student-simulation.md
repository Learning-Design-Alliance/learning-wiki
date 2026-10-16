---
type: research-method
id: architecturally-enforced-novice-like-student-simulation
title: Architecturally enforced novice-like student simulation
description: "The article's central design recommendation is that realistic synthetic student behavior cannot be elicited from preference-tuned LLMs by persona prompting or context injection alone; it requires architectural enforcement."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Architecturally enforced novice-like student simulation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 6 claims (6 for) · 4 studies (2 causal, 1 design, 1 theoretical), `q1`–`q2` · 1 of 4 report an effect size · 6 claims rest on one study

## Description
The article's central design recommendation is that realistic synthetic student behavior cannot be elicited from preference-tuned LLMs by persona prompting or context injection alone; it requires architectural enforcement. Symbolic control (semi-Markov dynamics, BKT with flaw injection) and a decoupled Strategist/Executor constrain what the model can do, so that "sequence-level student simulation cannot be recovered through context engineering alone; architectural enforcement closes the gap." The +M baseline variants, which inject BEAGLE's metacognitive vocabulary without the architecture, empirically isolate prompt effects from architectural ones.

## Accounts
<!-- How each source describes or uses the method -->
- **Enforce novice-like simulation architecturally rather than through prompting or context engineering**: The article's central design recommendation is that realistic synthetic student behavior cannot be elicited from preference-tuned LLMs by persona prompting or context injection alone; it requires architectural enforcement. Symbolic control (semi-Markov dynamics, BKT with flaw injection) and a decoupled Strategist/Executor constrain what the model can do, so that "sequence-level student simulation cannot be recovered through context engineering alone; architectural enforcement closes the gap." The +M baseline variants, which inject BEAGLE's metacognitive vocabulary without the architecture, empirically isolate prompt effects from architectural ones. (Hanchen David Wang et al. (2026))
- **Knowledge-level student simulation pipeline: machine unlearning to initialize a stable novice state, then supervised and coach-guided relearning to model growth under tutoring**: This framework replaces prompt-only role assignment with model-level knowledge degradation for LLM teachable agents. It argues that "prompt-based role assignment does not alter the model's underlying pre-trained knowledge, often leading to expert knowledge leakage and unstable role fidelity". The pipeline runs in three stages: machine unlearning of targeted knowledge components via LoRA, controlled relearning via supervised fine-tuning on forgotten QA pairs, and instructional relearning in a three-agent teachable-agent environment where a coach agent gives corrective feedback used as training signals. (Jiajia Song et al. (2026))

### Claims

- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](../claims/beagle-ablation-semi-markov-and-decoupling.md) [+M]
- [Machine unlearning induces progressively stronger novice-level performance in an LLM teachable agent, with accuracy and F1 declining as the unlearning ratio increases](../claims/unlearning-induces-novice-level-degradation.md) [+M]
- [Teachable agents measurably but incompletely relearn unlearned knowledge, with the recovery gap to the base model widening under higher unlearning ratios (30%–50%)](../claims/relearning-recovers-knowledge-incompletely.md) [+M]
- [Coach-guided interactive teaching yields higher and more progressive recovery than static relearning, particularly under moderate forgetting levels (10%–30%)](../claims/coach-guided-relearning-beats-static.md) [+M]
- [The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices](../claims/competence-paradox-llm-student-simulation.md) [+W]
- [Baseline LLM reflective responses were highly detectable, and persona and typo prompts progressively reduced separability from real student responses](../claims/reflection-prompt-reduces-detectability.md) [+W]

## Related Research Methods
-

## Key Sources
- Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280
- Jiajia Song, Zhihan Guo, and Jionghao Lin. (2026). Simulating Novice Students Using Machine Unlearning and Relearning in Large Language Models. https://arxiv.org/abs/2603.26142
