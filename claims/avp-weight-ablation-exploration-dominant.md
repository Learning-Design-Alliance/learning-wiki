---
type: claim
title: The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal
description: The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal
id: avp-weight-ablation-exploration-dominant
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: angela-chen-2026
    resource: "https://doi.org/10.48550/arxiv.2606.10051"
    title: "Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Yi-Chia Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). Empirically Grounded Behavioral Adaptivity for LLM-Based Virtual Patients in Psychotherapy Training. https://arxiv.org/abs/2606.10051 [doi:10.48550/arxiv.2606.10051](https://doi.org/10.48550/arxiv.2606.10051)"
    author: Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Yi-Chia Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The deployed empirically motivated weight vector outperforms equal, empathy-only, and exploration-only weightings in evaluator agreement, with exploration carrying most of the adaptive signal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Counterfactual re-scoring of logged turns showed the deployed weighting beat all alternatives: equal weights lost 10.5 pp, empathy-only lost 15.8 pp, and exploration-only lost only 7.2 pp of agreement. [→ Angela Chen 2026](#angela-chen-2026)

## Evidence

### Angela Chen 2026

Angela Chen, Siwei Jin, Catherine Bao, Canwen Wang, Yi-Chia Wang, Robert E. Kraut, Tongshuang Wu, and Haiyi Zhu. (2026). Empirically Grounded Behavioral Adaptivity for LLM-Based Virtual Patients in Psychotherapy Training. https://arxiv.org/abs/2606.10051 [doi:10.48550/arxiv.2606.10051](https://doi.org/10.48550/arxiv.2606.10051)

`q2 · i?` · `design · r2`

Counterfactual ablation re-running only the state-update rule on logged human-study turns under four weight schemes, with noise, multiplier, and thresholds pinned. The quote reports the printed agreement losses; Exploration-only retained ≈89% of deployed accuracy (0.579/0.651).

> "Uninformed loses 10.5 pp in A VP agreement; Empathy-only is worst (−15.8 pp) because without exploration the cumulative score cannot grow fast enough to cross the H threshold in the evaluator data"

## Discussion


## Related Claims
- [The adaptive virtual patient produces a steadily climbing disclosure trajectory across a session while a prompt-only baseline with the same LLM and persona stays flat](avp-climbing-disclosure-vs-static-flat.md) — related
- [In the AVP, per-turn disclosure change responds to trainee exploration but not measurably to trainee empathy, and the static baseline shows no significant joint response](avp-exploration-drives-disclosure-change.md) — related
- [The AVP's generated text matches its intended internal disclosure level about twice as often as the static baseline (0.651 vs. 0.311 agreement)](avp-faithful-realization-alignment.md) — related
- [Higher-skill trainees elicit faster-climbing AVP disclosure trajectories, directionally supporting skill sensitivity, though the formal interaction test is underpowered](avp-skill-sensitivity-directional.md) — related
