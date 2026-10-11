---
type: claim
title: Small language models used as automated judges exhibit severe leniency bias against tutoring responses
description: Small language models used as automated judges exhibit severe leniency bias against tutoring responses
id: slm-judges-show-severe-leniency-bias
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: h-chad-lane-2026
    resource: "https://github.com/InviteInstitute/CSTutorBench"
    title: "H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench"
    author: H. Chad Lane, Bryson Kageler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Small language models used as automated judges exhibit severe leniency bias against tutoring responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Phi4:14b scored gemma3:27b (Trial 1) responses at 91–96% across multiple configurations while a human rater scored the same responses at 61%. [→ H. Chad Lane 2026](#h-chad-lane-2026)

## Evidence

### H. Chad Lane 2026

H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench

`q2 · i?` · `design · r2`

Judge-selection analysis during pipeline development. The authors selected Claude Sonnet 4 instead, whose v4 rubric produced overall scores within 0–7 percentage points of the human baseline for three of four validated models, with deepseek-r1:8b showing a larger gap. No effect sizes are printed.

> "We initially explored using SLMs as automated judges but found severe leniency bias. Phi4:14b, for example, scored gemma3:27b (Trial 1) responses at 91–96% across multiple configurations, while a human rater scored the same responses at 61%."

## Discussion


## Related Claims
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — reports the opposite
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [RAG prompting shows systematic leniency, over-scoring relative to teacher mean scores in all four rubric dimensions (total bias = 1.787)](rag-systematic-leniency-overscoring.md) — related
