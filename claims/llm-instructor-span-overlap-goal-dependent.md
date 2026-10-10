---
type: claim
title: LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay
description: LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay
id: llm-instructor-span-overlap-goal-dependent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: yijun-liu-2026
    resource: "https://arxiv.org/abs/2606.06271"
    title: "Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271"
    author: Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yijun-liu-2026-2
    resource: "https://arxiv.org/abs/2606.06271"
    title: "Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271"
    author: Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: yijun-liu-2026-3
    resource: "https://arxiv.org/abs/2606.06271"
    title: "Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271"
    author: Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` Pairwise span overlap is modest overall and highest within LLM pairs (19.2%) versus human-model (18.0%) and human-human pairs (17.0%). [→ Yijun Liu 2026](#yijun-liu-2026)
`q2 i?` Span overlap is goal-dependent: agreement is higher for Counterclaim and Rebuttal than for Claim and Evidence. [→ Yijun Liu 2026 (2)](#yijun-liu-2026-2)
`q2 i?` All LLMs highlight a higher percentage of each essay than instructors, who highlight on average 42.8% of an essay. [→ Yijun Liu 2026 (3)](#yijun-liu-2026-3)

## Evidence

### Yijun Liu 2026

Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271

`q2 · i?` · `associational · r2`

Agreement analysis of highlight spans in FOXGLOVE (§4.1), classifying comment pairs as exact, inclusive, or partial agreement. Exact overlap was the most common type for all pair types (M-M 62.7%; H-H 52.8%; H-M 50.7%).

> "Overall, within-LLM pairs overlap most often (19.2%), ahead of H–M (18.0%) and H-H pairs (17.0%)."

### Yijun Liu 2026 (2)

Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271

`q2 · i?` · `associational · r2`

Goal-conditioned span overlap analysis shown in Figure 2, comparing overlap rates across argumentative goals. Overlap was lower for Claim and Evidence (M-M 27% each, H-H 17% and 21% respectively), and models tended to have the highest share of overlapping pairs across every goal.

> "Conditioning on the same essayandthe same goal, both instructors and models were more likely to agree on the same sentences forCounterclaim andRebuttal(M-M overlap 66% and 60%, H-H 36% and 31%, respectively)"

### Yijun Liu 2026 (3)

Yijun Liu, Yifan Song, John Gallagher, Sarah Sterman, Tal August. (2026). FOXGLOVE: Understanding Goal-Oriented and Anchored Writing Feedback from Experts and LLMs on Argumentative Essays. https://arxiv.org/abs/2606.06271

`q2 · i?` · `design · r2`

Descriptive analysis of highlighted-span percentages per feedback giver (§4.1, Table 6). Instructors highlighted on average 42.8% of each essay, while GPT-5.2 highlighted 88.3% and Claude Sonnet 4.5 highlighted 82.1% on average.

> "Instructors highlight on average 42.8% of essay. However, all LLMs highlight a higher percentage of essays than instructors, with GPT-5.2 and Claude Sonnet 4.5 highlighting the majority of each essay (over 80%)."

## Discussion


## Related Claims
- [Instructors use more first-person and second-person pronouns and more questions than LLMs in feedback comments](instructors-more-pronouns-and-questions.md) — related
- [LLM feedback receives higher expert ratings on six of seven quality dimensions, with tone the exception](llm-feedback-higher-expert-ratings.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Feedback givers agree on exact urgency tiers only about a fifth of the time, with most disagreements off by a single tier](low-urgency-rank-agreement.md) — related
- [Instructors and LLMs distribute feedback similarly across the five argumentative goals, with Claim receiving the most feedback from both](similar-goal-distribution-instructor-llm-feedback.md) — related
