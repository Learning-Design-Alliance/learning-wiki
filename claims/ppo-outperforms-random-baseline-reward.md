---
type: claim
title: The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7
description: The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7
id: ppo-outperforms-random-baseline-reward
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhu-z-2026
    title: Zhu Z 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After 300 training iterations the PPO mechanism's cumulative expected return remained stable at 95.12 ± 1.23 (about 0.79 per step), while a random policy baseline yielded 12.3 ± 4.7 under the same evaluation conditions. [→ Zhu Z 2026](#zhu-z-2026)

## Evidence

### Zhu Z 2026

Zhu Z, Luo C and Li L (2026) Adaptive teaching assistance model combining generative AI and big data analytics. Front. Psychol. 17:1844703. https://doi.org/10.3389/fpsyg.2026.1844703

`q2 · i?` · `causal · r1`

Numerical simulation/evaluation result comparing the trained PPO policy against a uniform random-action baseline over the same 120-step episode length, aggregated across 30 independent evaluation runs (10 per random seed). The PPO policy's cumulative reward was 95.12 ± 1.23 (mean across 3 seeds) versus the random baseline's 12.3 ± 4.7; no effect size is printed for this comparison.

> "a random policy baseline (uniform action sampling) yielded a cumulative reward of 12.3 ± 4.7 under the same evaluation conditions, confirming that the PPO-driven policy substantially outperforms chance"

## Discussion


## Related Claims
- [Sequencing rather than concept selection explains most of the EVOL–PPO-vanilla EP gap on ASSIST15 L=10](sequencing-explains-evol-ppo-gap.md) — related
- [Ablation baselines were configured to isolate the contribution of cross-modal attention, PPO clipping and Kalman filtering, but component-level results are not reported in the available text](ablation-baseline-configuration-component-isolation.md) — related
- [After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines](races-auxiliary-feedback-simcse-gains.md) — related
- [RACES configurations improve QWK essay-scoring agreement over evaluated pretrained baselines on ASAP 2.0, with LLaMA2-7B-based configurations slightly outperforming Qwen2.5-Instruct-7B-based ones](races-improves-qwk-over-evaluated-baselines.md) — related
