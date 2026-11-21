---
type: claim
title: No single LLM significantly outperformed the others on these tutor-move tasks
description: No single LLM significantly outperformed the others on these tutor-move tasks
id: no-llm-significantly-outperformed-others-tutor-moves
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: danielle-r-thomas-2025
    resource: "https://doi.org/10.1007/978-3-032-03873-9_35"
    title: "Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. [doi:10.1007/978-3-032-03873-9_35](https://doi.org/10.1007/978-3-032-03873-9_35)"
    author: Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# No single LLM significantly outperformed the others on these tutor-move tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Using 95% bootstrap confidence intervals, all five LLMs performed comparably on filter and evaluation prompts for both tutor skills. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. [doi:10.1007/978-3-032-03873-9_35](https://doi.org/10.1007/978-3-032-03873-9_35)

`q2 · i?` · `design · r2`

Bootstrap analysis (10,000 samples) of accuracy scores with 95% percentile confidence intervals across GPT-4, GPT-4o, GPT-4 Turbo, Gemini 1.5 Pro, and LearnLM on the 50-transcript corpus; overlapping intervals indicate comparable performance.

> "Using 95% bootstrap confi- denceintervals,weobservedthatallLLMsperformedcomparably,withnomodel significantly outperforming others."

## Discussion


## Related Claims
- [LLMs reliably detect tutor praise in real-life math tutoring transcripts, with 94-98% accuracy across five models](llms-detect-tutor-praise-high-accuracy.md) — related
- [LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection](llms-detect-student-math-errors-82-88.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [LLMs evaluate tutor praise quality in line with human judgments at 83-89% accuracy](llms-evaluate-praise-quality-83-89.md) — related
