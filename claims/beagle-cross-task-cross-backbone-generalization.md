---
type: claim
title: "BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores"
description: "BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores"
id: beagle-cross-task-cross-backbone-generalization
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hanchen-david-wang-2026
    resource: "https://doi.org/10.48550/arxiv.2602.13280"
    title: "Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280 [doi:10.48550/arxiv.2602.13280](https://doi.org/10.48550/arxiv.2602.13280)"
    author: Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Cross-backbone: all six frontier backbones clear the strongest baseline on DKL, Debug, Lang, and Realism; on P_recur two exceed and four sit within ~1.5%. [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280 [doi:10.48550/arxiv.2602.13280](https://doi.org/10.48550/arxiv.2602.13280)

`q2 · i?` · `design · r2`

Cross-backbone generalization (Fig. 10, Particle Simulator, N=50, T=30) across Gemini 2.0/2.5/3 Flash, GPT-4o-mini, GPT-4.1-mini, and Claude Haiku 4.5, with the red-dashed line marking the strongest non-BEAGLE baseline (FewShot+M on Gemini 2.0 Flash).

> "every one of six frontier backbones clears the strongest baseline onD KL, Debug, Lang, and Realism; onP recur, two exceed and four sit within∼1.5%."

## Discussion


## Related Claims
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](beagle-error-recurrence-novice-envelope.md) — related
- [In a preliminary 2×3 controlled lesson study across five backbone LLMs, structured student agents produce more differentiated mastery and misconception traces than a baseline simulator](structured-student-agents-differentiated-mastery-traces.md) — related
- [Expert evaluation finds larger, more capable LLM backbones produce higher-quality multi-domain graphs, with GPT-5 pro rated best](llm-backbone-graph-quality-expert-evaluation.md) — related
- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](varia-frontier-nonfrontier-tier-gap.md) — related
- [Two of seven frontier LLMs show behavioral inconsistency between monitored and unmonitored conditions (Grok-4.1-fast 5.50; Gemini-3-Pro 5.00), while four show perfect consistency (1.0)](alignment-faking-inconsistency-educational-llms.md) — related
