---
type: claim
title: Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators
description: Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators
id: multi-turn-reflection-does-not-restore-sfs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: heejin-do-2026
    resource: "https://doi.org/10.48550/arxiv.2605.12748"
    title: "Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)"
    author: Heejin Do, Shashank Sonkar, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Multi-turn reflective interaction does not restore selective updating and destabilizes weaker simulators

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In a multi-turn setting where the model first generates reflective reasoning for its incorrect answer, SFS remains low and largely indistinguishable from single-turn, with weaker models degrading further. [→ Heejin Do 2026](#heejin-do-2026)

## Evidence

### Heejin Do 2026

Heejin Do, Shashank Sonkar, Mrinmaya Sachan. (2026). Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators. Preprint. https://arxiv.org/abs/2605.12748 [doi:10.48550/arxiv.2605.12748](https://doi.org/10.48550/arxiv.2605.12748)

`q2 · i?` · `causal · r2`

Multi-turn simulation experiment in which models first generate first-turn reasoning judged for coherence and misconception alignment by GPT-4o-mini; the text reports "SFS remains low and largely indistinguishable from the single-turn setting."

> "Figure 4(right)shows that multi-turn interaction does not resolve the failure: SFS remains low and largely indistinguishable from the single-turn setting. In weaker models, performance further degrades, indicating that additional reasoning step introduces instability rather than improving selective updating."

## Discussion


## Related Claims
- [Stronger problem-solving capability predicts lower misconception faithfulness: flip rate under generic feedback correlates negatively with SFS (Pearson r = -0.94, p = 0.002)](model-capability-negatively-correlates-sfs.md) — related
- [LLM student simulators exhibit near-zero Selective Flip Score, flipping at similarly high rates under targeted, misaligned, and generic feedback](llm-simulators-near-zero-sfs-indiscriminate-flipping.md) — a broader claim this one bears on
- [Supervised fine-tuning on misconception-faithful demonstrations sharply improves SFS (up to +0.555 on Malrule for Qwen3-4B)](sft-improves-selective-update-behavior.md) — related
- [SFS-aligned post-training generalizes out-of-domain: models trained on one dataset retain substantial SFS gains on the other](sfs-post-training-cross-domain-generalization.md) — related
- [A 4B per-student simulator solves a held-out Socratic-guidance chess case where prompted GPT-5.4 fails, indicating multi-turn training adds guidance-following capability beyond hint copying](studentsim-socratic-case-beats-prompted-frontier-llm.md) — related
- [The competence paradox: broadly capable LLMs cannot genuinely unknow expert knowledge when simulating novices](competence-paradox-llm-student-simulation.md) — related
