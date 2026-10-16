---
type: claim
title: Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels
description: Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels
id: fine-tuning-authentic-data-improves-pedagogical-benchmarks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: janos-perczel-2025
    resource: "https://doi.org/10.48550/arxiv.2510.05087"
    title: "Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087 [doi:10.48550/arxiv.2510.05087](https://doi.org/10.48550/arxiv.2510.05087)"
    author: Janos Perczel, Jin Chow, and Dorottya Demszky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Parameter-efficient fine-tuning of Gemini 2.5 Flash and GPT-4o on authentic Polygence data improves student talk time, words per tutor turn, questions per interrogative turn, turns before wrap-up, uncovering student background, and coding-skill checks. [→ Janos Perczel 2025](#janos-perczel-2025)

## Evidence

### Janos Perczel 2025

Janos Perczel, Jin Chow, and Dorottya Demszky. (2025). TeachLM: Post-Training LLMs for Education Using Authentic Learning Data. https://arxiv.org/abs/2510.05087 [doi:10.48550/arxiv.2510.05087](https://doi.org/10.48550/arxiv.2510.05087)

`q2 · i?` · `design · r2`

Automated multi-turn evaluations (Fig. 7) of fine-tuned Gemini 2.5 Flash and GPT-4o-2024-08-06 against the human training-data reference line. The article reports that "fine-tuning improves model performance on every benchmark," with simpler conversational metrics converging faster than complex pedagogical ones; no effect sizes are printed.

> "We see that fine-tuning improves model performance on every benchmark, bringing the resulting values closer to the human training data benchmarks."

## Discussion


## Related Claims
- [Users experienced a trade-off between conversational depth and interaction efficiency between the fine-tuned and baseline chatbots](depth-efficiency-tradeoff-instructional-chatbots.md) — related
- [A fine-tuned student model paired with GPT-4 produces conversational statistics closer to human-AI dialogues than two prompt-engineered base models](fine-tuned-student-model-approximates-human-ai-dialogue.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
- [Education-oriented instruction tuning consistently improves curriculum grounding, K-12 problem solving, and pedagogical tutoring at every evaluated model scale](omniedu-tuning-improves-all-three-educational-capability-groups.md) — related
- [Off-the-shelf LLM tutors are more verbose than human tutors, leaving students only 5-15% of talk time versus close to 30% in human tutoring](off-the-shelf-llms-verbose-low-student-talk-time.md) — related
