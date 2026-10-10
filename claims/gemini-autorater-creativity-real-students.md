---
type: claim
title: "A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)"
description: "A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)"
id: gemini-autorater-creativity-real-students
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: globerson-2026
    resource: "https://arxiv.org/abs/2609.15864"
    title: "Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864"
    author: Globerson, A., Keeling, A., Choudhury, A., et al
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: globerson-2026-2
    resource: "https://arxiv.org/abs/2609.15864"
    title: "Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864"
    author: Globerson, A., Keeling, A., Choudhury, A., et al
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# A Gemini-based creativity autorater scores real students' complex multimedia creativity tasks on par with human experts (item Kappa 0.66; total-score Pearson r = 0.88)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i?` Item-level agreement between autorater and expert raters on 0-2 scores was Cohen's Kappa 0.66, described as good agreement. [→ Globerson 2026](#globerson-2026)
`q2 i3` Autorater total scores correlated with human expert total scores at Pearson's r = 0.88 on held-out student submissions. [→ Globerson 2026 (2)](#globerson-2026-2)

## Evidence

### Globerson 2026

Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864

`q2 · i?` · `design · r2`

Lab study with OpenMic: 280 students designed a news segment from a story; 100 submissions refined the prompt and rubrics and 180 evaluated autorater accuracy against trained experts. Item-level "Cohen’s Kappa was0.66", an agreement statistic the article reports without a standardized effect size.

> "At the specific item0−2scores, the agreement between the scores of the autorater and those of the human expert raters as measured using Cohen’s Kappa was0.66, corresponding to good agreement [28]."

### Globerson 2026 (2)

Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864

`q2 · i3` · `design · r2`

Same OpenMic lab study, evaluated on 180 held-out submissions: autorater overall scores vs human expert scores gave "Pearson’s correlation of0.88" (r = 0.88), a large correlation; Figure 11 shows the scatter plot of the two raters' scores.

> "A comparison of the autorater overall scores and those of the human experts reveals an extremely high Pearson’s correlation of0.88."

## Discussion


## Related Claims
- [An LLM-based AI Evaluator agrees with expert human raters on collaboration transcripts at a level similar to inter-expert agreement](llm-evaluator-agreement-matches-expert-raters.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [An LLM-based analogy judge validated against expert judgments shows moderate-to-strong agreement and screens most generated analogies as meeting baseline adequacy](anvil-llm-judge-analogy-screening.md) — related
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](ca-selective-best-average-agreement-drawings.md) — related
