---
type: claim
title: "Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward"
description: "Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward"
id: edu-qurater-rewards-alone-below-parity-instruction-following
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: garrod-2026
    resource: "https://arxiv.org/abs/2609.09425"
    title: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425"
    author: "Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The Edu-QuRating reward alone produces the highest single-source pedagogical-quality win rate (77.70%) but an instruction-following win rate below parity with the base model (40.54%). [→ Garrod 2026](#garrod-2026)

## Evidence

### Garrod 2026

Garrod, O. G. B., Ince, R. A. A., Liu, M., Huti, M., Boos, M., Waldock, A., Andrews, D., Alonso-Kropil, R., & Atherton, P. (2026). Edu-QuRating: Multi-Dimensional Educational Data Curation with Distilled Pairwise Judgements. arXiv. https://arxiv.org/abs/2609.09425

`q2 · i?` · `design · r2`

Same held-out pairwise judge evaluation of GRPO checkpoints against the Qwen3-4B base model, for the Edu-QuRating-only reward configuration. The article reports win rates of 77.70% (pedagogical quality) and 40.54% (instruction following).

> "The Edu-QuRating reward alone produces the highest pedagogical-quality win rate of the two single-source reward conditions (77.70%), but its instruction-following win rate falls below parity with the base model (40.54%)."

## Discussion


## Related Claims
- [In held-out pairwise judge evaluation, combining Edu-QuRater and answer-structure GRPO rewards yields the highest pedagogical-quality win rate (81.08%) while retaining instruction-following above parity (68.24%) against the Qwen3-4B base model](edu-qurater-grpo-rewards-improve-responses.md) — related
- [RL policies risk three failure modes when reward signals are poorly specified: reward hacking, engagement optimization over learning, and scaffolding dependency](rl-reward-misalignment-failure-modes.md) — a broader claim this one bears on
- [A screenshot-only reward was reward-hacked into producing visually convincing but unplayable games; hardening the reward with an interactivity probe and hard-fail gate reversed the collapse](reward-hacking-games-interactivity-probe.md) — related
- [Edu-QuRaters recover held-out GPT-4.1-mini pairwise educational preferences from single-text scores, with mean accuracy rising from 0.895 (Sheared-LLaMA-1.3B) to 0.917 (Gemma-3-4B-PT)](edu-quraters-distill-pairwise-educational-preferences.md) — related
