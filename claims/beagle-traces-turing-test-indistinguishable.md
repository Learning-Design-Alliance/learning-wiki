---
type: claim
title: "In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)"
description: "In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)"
id: beagle-traces-turing-test-indistinguishable
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
    i: 0
    kind: design
    rigour: 2
  - id: hanchen-david-wang-2026-2
    resource: "https://arxiv.org/abs/2602.13280"
    title: "Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280"
    author: Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i0` negligible

## Subclaims
`q2 i0` Turing test classification accuracy was statistically equivalent to chance, with discriminability d′ = 0.15 falling significantly within the equivalence bound of ±0.3. [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)
`q2 i?` Identification was asymmetric: participants correctly identified 62.2% of real traces but only 43.4% of AI traces, with a real-labeling response bias (c = −0.24). [→ Hanchen David Wang 2026 (2)](#hanchen-david-wang-2026-2)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i0` · `design · r2`

Human Turing test with N=71 participants (852 total classifications; each rated 12 traces across 3 scenarios) on pilot-study stimuli. A Two One-Sided Tests equivalence procedure showed "d′ = 0.15" within the ±0.3 bound; overall accuracy was 52.8% (p = 0.053).

> "Results confirm that the discriminability index ( d′ = 0.15 , where d′ = 0 indicates perfect indistinguishability) falls significantly within the equivalence bound of±0.3 (pTOST = 0.038)."

### Hanchen David Wang 2026 (2)

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

SDT analysis of the same Turing test (N=71) separated sensitivity from response tendency, revealing a bias toward labeling any trace as real (c = −0.24). AI traces were identified at "only 43.4%", below chance. No standardized effect size is printed for this asymmetry.

> "This bias manifests asymmetrically: participants correctly identified 62.2% of real traces but only 43.4% of AI traces, worse than random guessing."

## Discussion


## Related Claims
- [AI agent activity in an LMS is indistinguishable from normal student activity, defeating detection and proctoring](ai-agent-activity-indistinguishable-from-students.md) — related
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](beagle-error-recurrence-novice-envelope.md) — related
- [Admissions officers can often discriminate AI-written from human-written essays, achieving an AUC of 0.70, well above chance but below commercial detectors](admissions-officers-detect-ai-essays-auc-070.md) — related
