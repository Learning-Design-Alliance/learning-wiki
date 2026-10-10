---
type: claim
title: "BEAGLE's HIGH and LOW performer profiles differentiate by SRL strategy: HIGH performers allocate 72% of steps to PLANNING and MONITORING while LOW performers spend 50.8% trapped in ENACTING"
description: "BEAGLE's HIGH and LOW performer profiles differentiate by SRL strategy: HIGH performers allocate 72% of steps to PLANNING and MONITORING while LOW performers spend 50.8% trapped in ENACTING"
id: beagle-profile-strategy-differentiation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: hanchen-david-wang-2026
    resource: "https://arxiv.org/abs/2602.13280"
    title: "Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280"
    author: Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BEAGLE's HIGH and LOW performer profiles differentiate by SRL strategy: HIGH performers allocate 72% of steps to PLANNING and MONITORING while LOW performers spend 50.8% trapped in ENACTING

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Simulated HIGH and LOW profiles reproduce the wheel-spinning pattern: HIGH performers spend 72% of steps planning and monitoring; LOW performers spend 50.8% in ENACTING. [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

Performance-differentiation analysis in the RQ1 behavioral-fidelity evaluation, comparing BEAGLE runs configured with HIGH versus LOW behavioral profiles. The paper reports profile-driven solve-rate gaps that scale with backbone capability (e.g., +40% on Gemini 2.5 Flash), whereas vanilla LLMs show no profile sensitivity (+0%).

> "HIGHperformers allocate 72% of steps to PLANNING and MONITORING , while LOWperformers spend 50.8% trapped in ENACTING (Fig. 6), reproducing the "wheel-spinning" pattern documented in SRL literature [3]."

## Discussion


## Related Claims
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
- [A 15-feature J48 decision tree model distinguishes wheel-spinning from productive persistence in ASSISTments Skill Builders at AUC ROC 0.684 under student-skill-level cross-validation](j48-model-distinguishes-wheel-spinning-productive-persistence.md) — related
- [The relationship between bottom-out hint use and wheel-spinning is nuanced, depending on whether students avoid hints entirely](bottom-out-hint-use-nuanced-wheel-spinning.md) — related
