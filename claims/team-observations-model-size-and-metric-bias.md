---
type: claim
title: Participating teams found that smaller fine-tuned models can be competitive and that DialogRPT tends to prefer complete answers over pedagogically scaffolded ones.
description: Participating teams found that smaller fine-tuned models can be competitive and that DialogRPT tends to prefer complete answers over pedagogically scaffolded ones.
id: team-observations-model-size-and-metric-bias
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: anaïs-tack-2023
    resource: "https://doi.org/10.18653/v1/2023.bea-1.64"
    title: "Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech. (2023). The BEA 2023 Shared Task on Generating AI Teacher Responses in Educational Dialogues. [doi:10.18653/v1/2023.bea-1.64](https://doi.org/10.18653/v1/2023.bea-1.64)"
    author: Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Participating teams found that smaller fine-tuned models can be competitive and that DialogRPT tends to prefer complete answers over pedagogically scaffolded ones.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Data Science-NLP-HSG team found GPT-2, with 124 million parameters, achieved competitive performance compared to the T5-base model, and the NAIST team noted DialogRPT preferred complete, non-teacher-like answers. [→ Anaïs Tack 2023](#anais-tack-2023)

## Evidence

### Anaïs Tack 2023

Anaïs Tack, Ekaterina Kochmar, Zheng Yuan, Serge Bibauw, Chris Piech. (2023). The BEA 2023 Shared Task on Generating AI Teacher Responses in Educational Dialogues. [doi:10.18653/v1/2023.bea-1.64](https://doi.org/10.18653/v1/2023.bea-1.64)

`q2 · i?` · `design · r2`

Secondary observations reported from participating teams' system papers. The NAIST team separately noted that "DialogRPT often preferred complete answers that were not very teacher-like over responses that helped the student find the answer by themselves."

> "Huber et al. (Data Science-NLP-HSG) found that GPT-2—a smaller model with 124 million parameters—achieved competitive performance compared to the T5-base model."

## Discussion


## Related Claims
- [DialogRPT scores were highly sensitive to the presence of a teacher prefix: identical GPT-4 responses scored 0.52 on updown with the prefix but 0.40 without it.](dialogrpt-teacher-prefix-sensitivity.md) — related
- [A trivial baseline generating \"Hello\" for every prompt achieved the best BERTScore precision and DialogRPT updown scores, exposing construct-irrelevant sensitivity in the automated metrics.](hello-baseline-best-automated-metrics.md) — related
- [Users experienced a trade-off between conversational depth and interaction efficiency between the fine-tuned and baseline chatbots](depth-efficiency-tradeoff-instructional-chatbots.md) — related
- [In a user study, the GPT-4o-mini baseline was preferred overall, but participants more often attributed learning to the fine-tuned TeachingCoach model](preference-learning-attribution-diverge-chatbots.md) — related
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
