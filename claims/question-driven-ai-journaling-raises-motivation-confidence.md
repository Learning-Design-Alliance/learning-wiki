---
type: claim
title: Question-driven AI journaling increases intrinsic motivation and acting confidence among actors
description: Question-driven AI journaling increases intrinsic motivation and acting confidence among actors
id: question-driven-ai-journaling-raises-motivation-confidence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: sora-kang-2026
    resource: "https://doi.org/10.48550/arxiv.2607.24751"
    title: "Sora Kang. (2026). Stop Writing for Me: Generative Refusal in AI Tools for Thought. In Proceedings of CHI 2026 Workshop on Tools for Thought. https://arxiv.org/abs/2607.24751 [doi:10.48550/arxiv.2607.24751](https://doi.org/10.48550/arxiv.2607.24751)"
    author: Sora Kang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: sora-kang-2026-2
    resource: "https://arxiv.org/abs/2607.24751"
    title: "Sora Kang. (2026). Stop Writing for Me: Generative Refusal in AI Tools for Thought. In Proceedings of CHI 2026 Workshop on Tools for Thought. https://arxiv.org/abs/2607.24751"
    author: Sora Kang
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Question-driven AI journaling increases intrinsic motivation and acting confidence among actors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` Intrinsic motivation increased significantly in the AI-assisted condition (eta-squared = .201). [→ Sora Kang 2026](#sora-kang-2026)
`q3 i?` Acting confidence also increased significantly (partial eta-squared, η²p = .352), which the authors attribute to questions concretizing character interpretation. [→ Sora Kang 2026 (2)](#sora-kang-2026-2)

## Evidence

### Sora Kang 2026

Sora Kang. (2026). Stop Writing for Me: Generative Refusal in AI Tools for Thought. In Proceedings of CHI 2026 Workshop on Tools for Thought. https://arxiv.org/abs/2607.24751 [doi:10.48550/arxiv.2607.24751](https://doi.org/10.48550/arxiv.2607.24751)

`q3 · i?` · `causal · r2`

Same 14-day randomized crossover field study with 29 actors; daily surveys measured intrinsic motivation. The AI-assisted phase showed "an increase in Intrinsic Motivation", with the article printing an effect size of eta-squared = .201 (p = .017).

> "results showed a sig- nificant decrease in Cognitive Burden (𝜂2 𝑝 =.381, 𝑝<.001) and an increase in Intrinsic Motivation (𝜂2 𝑝 =. 201, 𝑝=. 017)"

### Sora Kang 2026 (2)

Sora Kang. (2026). Stop Writing for Me: Generative Refusal in AI Tools for Thought. In Proceedings of CHI 2026 Workshop on Tools for Thought. https://arxiv.org/abs/2607.24751

`q3 · i?` · `causal · r2`

Same crossover study's daily survey measure of acting confidence. The article reports "Acting Confidence also increased significantly", printing an effect size of partial eta-squared, η²p = .352 (p < .001), and interprets this as questions concretizing interpretation.

> "Acting Confidence also increased significantly (𝜂2 𝑝 =. 352, 𝑝<. 001), suggesting that the AI-generated questions concretized character interpretation."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does an AI journaling assistant help learners keep a journal, and should it ask questions rather than write for them?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **3 distinct studies** (2 causal, 1 design), `q2`–`q3`, 2 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Sora Kang 2026](https://doi.org/10.48550/arxiv.2607.24751) | q3 · causal · r2 | i?; i3 | this claim; [AI-generated questions instead of draft text significantly reduce actors' cognitive burden](generative-refusal-reduces-cognitive-burden-journaling.md) (supports); [AI-assisted journal entries show higher lexical diversity and more emotion-word usage than](ai-questions-deepen-reflective-writing-quality.md) (supports) |
| [Sven Scheu 2026](https://doi.org/10.1186/s41239-026-00589-7) | q3 · causal · r2 | i?; i2 | [The LLM-based journaling assistant shows no significant effect on students' intrinsic moti](journaling-assistant-no-intrinsic-motivation-effect.md) (qualifies); [Both the course and the assistant increase behavioral engagement, measured as characters w](course-and-assistant-increase-writing-engagement.md) (supports); [Course users create their journal entries earlier relative to the daily notification, whil](course-users-earlier-journal-entry-timing.md) (qualifies) |
| [Rajan Kadel 2026](https://doi.org/10.48550/arxiv.2609.03413) | q2 · design · r1 | i? | [Minority of undergraduate health science students reported using GenAI for reflective writ](minority-health-students-genai-reflective-writing.md) (qualifies); [Educators struggled to reliably differentiate student-written from GenAI-generated reflect](educators-cannot-reliably-detect-genai-reflections.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

## Learner Variables
- [Motivation](../learner-variables/motivation.md) — outcome: instruction changes it

## Related Claims

- [GenAI-assisted education produces significantly higher learning motivation than non-GenAI approaches (g = 0.81)](genai-learning-motivation-g081.md) — the general claim this finding bears on, with the studies behind it
- [The tool's effect differs by timing: early AI acts as a momentum starter, later AI as a deepener raising narrative transportation](ai-scaffolding-effect-depends-on-workflow-timing.md) — related
- [AI-generated questions instead of draft text significantly reduce actors' cognitive burden during character journaling](generative-refusal-reduces-cognitive-burden-journaling.md) — related
- [Tablet-PC-supported peer-assisted learning reduced EFL learners' anxiety and promoted motivation and confidence in collaborative reading](tablet-pc-peer-assisted-learning-reduces-anxiety.md) — related
- [AI Prompting Literacy is indirectly and significantly associated with Deep Revision Engagement through Perceived Competence, Intrinsic Motivation, and Psychological Safety](apl-parallel-mediation-deep-revision.md) — related
- [Perceived Competence, Intrinsic Motivation, and Psychological Safety each significantly positively predict Deep Revision Engagement](psychological-mediators-predict-deep-revision.md) — related
- [Intrinsically motivated students show significantly higher proportions of evaluation and elaboration messages, while extrinsically motivated students concentrate in planning and orientation](intrinsic-motivation-higher-order-metacognition.md) — related
- [Actors internalized the AI's questioning style, self-generating similar questions after the tool was removed](questioning-habits-internalized-after-ai-removal.md) — related
- [Both the course and the assistant increase behavioral engagement, measured as characters written per journaling prompt](course-and-assistant-increase-writing-engagement.md) — related
- [The LLM-based journaling assistant shows no significant effect on students' intrinsic motivation for creating a learning journal](journaling-assistant-no-intrinsic-motivation-effect.md) — related
- [Students value GenAI corrective feedback with rationales and report increased motivation and confidence](genai-corrective-feedback-motivation-benefits.md) — related
- [An example-based built-in course in a mobile chatbot journaling system increases students' intrinsic motivation for creating a learning journal](example-based-course-increases-journaling-intrinsic-motivation.md) — related
