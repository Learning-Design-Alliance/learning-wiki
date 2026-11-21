---
type: claim
title: "LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection"
description: "LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection"
id: llms-detect-student-math-errors-82-88
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

# LLMs detect student math errors in tutoring transcripts with 82-88% accuracy, lower than praise detection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The same five LLMs detected student math errors (or tutor recognition of them) with 82-88% accuracy, lower than praise detection. [→ Danielle R. Thomas 2025](#danielle-r-thomas-2025)

## Evidence

### Danielle R. Thomas 2025

Danielle R. Thomas, Conrad Borchers, Jionghao Lin, Sanjit Kakarla, Shambhavi Bhushan, Erin Gatz, Shivang Gupta, Ralph Abboud, and Kenneth R. Koedinger. (2025). Leveraging LLMs to Assess Tutor Moves in Real-Life Dialogues: A Feasibility Study. arXiv preprint. [doi:10.1007/978-3-032-03873-9_35](https://doi.org/10.1007/978-3-032-03873-9_35)

`q2 · i?` · `design · r2`

Results section reporting bootstrap (10,000 samples) accuracy on the 50-transcript corpus. Table 2 shows error filter accuracies of 82-88 across the five models versus 94-98 for praise; prompts were modified to identify tutors' recognition of errors since transcripts lacked multimodal data.

> "model accuracy was high—over 94% for identifying tutor praise and 82% for detecting student math errors"

## Discussion


## Related Claims
- [LLMs reliably detect tutor praise in real-life math tutoring transcripts, with 94-98% accuracy across five models](llms-detect-tutor-praise-high-accuracy.md) — related
- [Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition](prompting-techniques-task-dependent-tutor-moves.md) — related
- [LLMs evaluate tutor responses to student math errors at 73-77% accuracy, the weakest performance](llms-evaluate-error-responses-73-77.md) — related
- [No single LLM significantly outperformed the others on these tutor-move tasks](no-llm-significantly-outperformed-others-tutor-moves.md) — related
