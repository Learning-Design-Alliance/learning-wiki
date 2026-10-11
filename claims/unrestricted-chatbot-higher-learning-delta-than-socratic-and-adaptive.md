---
type: claim
title: In an immediate post-test design, participants with an unrestricted chatbot achieved significantly higher learning deltas than participants with a Socratic chatbot (d = 0.80) or an EEG-adaptive exercise system (d = 0.85)
description: In an immediate post-test design, participants with an unrestricted chatbot achieved significantly higher learning deltas than participants with a Socratic chatbot (d = 0.80) or an EEG-adaptive exercise system (d = 0.85)
id: unrestricted-chatbot-higher-learning-delta-than-socratic-and-adaptive
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alexandre-clin-deffarges-2026
    resource: "https://arxiv.org/abs/2609.00584"
    title: "Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584"
    author: Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes
    q: 2
    i: 3
    kind: causal
    rigour: 2
  - id: alexandre-clin-deffarges-2026-2
    resource: "https://arxiv.org/abs/2609.00584"
    title: "Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584"
    author: Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In an immediate post-test design, participants with an unrestricted chatbot achieved significantly higher learning deltas than participants with a Socratic chatbot (d = 0.80) or an EEG-adaptive exercise system (d = 0.85)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` The unrestricted chatbot condition produced significantly higher learning delta than the Socratic condition (d = 0.80) and the adaptive condition (d = 0.85), against the authors' hypothesis H1. [→ Alexandre Clin Deffarges 2026](#alexandre-clin-deffarges-2026)
`q2 i?` A linear mixed model on 500 per-question change scores confirmed the same pattern: Full significantly outperformed Socratic and Adaptive, which did not differ from each other. [→ Alexandre Clin Deffarges 2026 (2)](#alexandre-clin-deffarges-2026-2)

## Evidence

### Alexandre Clin Deffarges 2026

Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584

`q2 · i3` · `causal · r2`

Controlled experiment with 50 participants randomized by sequential allocation to three modes (17 Full, 17 Socratic, 16 Adaptive). One-way ANOVA on per-participant mean delta showed a significant main effect of mode (F(2,47)=3.948, p=.026); Welch's t-tests gave a large effect of "𝑑= 0.80(large effect)" for Full vs. Socratic and d = 0.85 for Full vs. Adaptive.

> "Full vs. Socratic: 𝑡= 2.345,𝑝=. 025,𝑑= 0.80(large effect). Participants with unrestricted access achieved significantly higher deltas than those in the Socratic condition."

### Alexandre Clin Deffarges 2026 (2)

Alexandre Clin Deffarges, Nataliya Kosmyna, and Pattie Maes. (2026). Socrates went Nuclear: Comparing Interaction Strategies for AI systems in a Learning Context using Brain Sensing. arXiv preprint arXiv:2609.00584. https://arxiv.org/abs/2609.00584

`q2 · i?` · `causal · r2`

Linear mixed model on all 500 per-question learning-delta change scores with participant as random intercept; Socratic/Full estimate = -9.60, p=.009; Adaptive/Full estimate = -8.92, p=.017; Adaptive/Socratic estimate = 0.68, p=.855. No effect size printed for the LMM contrasts.

> "The LMM confirms the same pattern as the ANOVA/Welch analyses : the Full condition significantly outperforms the 2 other conditions, while Socratic and Adaptive do not differ significantly."

## Discussion


## Related Claims
- [The adaptive mode showed a progressive per-question learning-delta increase across the session (from Δ = 3.16 on Q1 to Δ = 19.97 on Q9), suggesting a warm-up effect as participants learned the system](adaptive-mode-per-question-delta-increase-warm-up.md) — related
- [No significant difference in perceived learning across the three modes (p = .845), despite the unrestricted mode's nearly double objective learning delta](no-perceived-learning-difference-across-modes.md) — related
- [Socratic-mode participants progressively disengaged from the chatbot: message counts declined after question 5 and EEG engagement fell to its lowest value at question 10](socratic-mode-progressive-disengagement.md) — related
- [Socratic participants required nearly twice as many attempts to reach the 80% mastery threshold as Full participants (d = -2.01), and 58% of their abandoned exercises never reached the threshold](socratic-more-attempts-many-never-reach-mastery.md) — related
- [The EEG-adaptive exercise condition produced significantly higher cognitive engagement during training than the unrestricted chatbot condition (p = .018), and was the only condition above the 0.5 baseline](adaptive-mode-higher-eeg-engagement.md) — related
- [Most unrestricted-mode interactions were direct answer retrieval: 52.9% of exercise interactions were copy-paste of the question, and participant answers were linguistically near-identical to chatbot text in 25.3% of cases](unrestricted-mode-answer-retrieval-copy-paste.md) — related
