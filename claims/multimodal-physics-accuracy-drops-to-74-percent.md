---
type: claim
title: "LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models"
description: "LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models"
id: multimodal-physics-accuracy-drops-to-74-percent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: akshay-syal-2026
    resource: "https://doi.org/10.48550/arxiv.2605.04131"
    title: "Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education. https://arxiv.org/abs/2605.04131 [doi:10.48550/arxiv.2605.04131](https://doi.org/10.48550/arxiv.2605.04131)"
    author: Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: akshay-syal-2026-2
    resource: "https://arxiv.org/abs/2605.04131"
    title: "Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education. https://arxiv.org/abs/2605.04131"
    author: Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM accuracy drops from 96% on text-only to 74% on multimodal physics problems, with significant differences emerging among models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Akshay Syal 2026: the intervention came bundled with another change · Akshay Syal 2026 (2): the intervention came bundled with another change (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` On multimodal questions with a figure essential for solving the problem, overall accuracy dropped to 74% (95% CI [0.66, 0.82]). [→ Akshay Syal 2026](#akshay-syal-2026)
`q2 i?` Unlike the text-only baseline, the multimodal task revealed a highly significant difference in model capabilities (Cochran's Q = 10.2, df = 2, p = 0.006). [→ Akshay Syal 2026 (2)](#akshay-syal-2026-2)

## Evidence

### Akshay Syal 2026

Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education. https://arxiv.org/abs/2605.04131 [doi:10.48550/arxiv.2605.04131](https://doi.org/10.48550/arxiv.2605.04131)

`q2 · i?` · `causal · r1`

Evaluation of the same three models on 44 multimodal OpenStax physics problems containing graphs, diagrams, tables, or visual equations essential to the solution. The article reports accuracy "dropped to 74% (95% CI [0.66, 0.82])", with per-model success of Claude 64%, Gemini 89%, ChatGPT 70%.

> "However, on multimodal questions with a figure essential for solving the problem (Table 2), overall accuracy dropped to 74% (95% CI [0.66, 0.82])."

### Akshay Syal 2026 (2)

Akshay Syal, Lawrence Swaminathan Xavier Prince, Evin Gultepe, Nik Bear Brown, Srinivas Sridhar. (2026). A Dialogue-Based Framework for Correcting Multimodal Errors in AI-Assisted STEM Education. https://arxiv.org/abs/2605.04131

`q2 · i?` · `causal · r1`

Cochran's Q test for paired proportions comparing the three models on the 44 multimodal problems. The article reports "Cochran’s Q = 10.2, df = 2, p = 0.006", indicating the addition of visual data created a performance gap absent in text-only reasoning.

> "Unlike the text-only baseline, where performance was uniform, the multimodal task revealed a highly significant difference in model capabilities (Cochran’s Q = 10.2, df = 2, p = 0.006)."

## Discussion


## Related Claims
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — reports the opposite
- [Three publicly available LLMs achieve 96% average accuracy on text-only physics problems with no significant differences among models](llms-96-percent-text-only-physics-accuracy.md) — related
- [The Multimodal Interference Effect: mapping visual representations to physical concepts degrades LLM performance even on non-visual problem aspects](multimodal-interference-effect-llms.md) — related
- With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models — related
- [A three-step structured multimodal dialogue intervention corrected 82% of baseline errors and raised multimodal accuracy to 95%, with visual processing errors corrected at 100% but context misinterpretation errors resistant](structured-dialogue-corrects-82-percent-llm-errors.md) — related
- [Differences between AI-generated and teacher assessments of laboratory reports may stem from difficulties retrieving and interpreting equations, graphs, tables, and units, not only from model reasoning capabilities.](ai-teacher-assessment-gaps-tied-to-evidence-retrieval.md) — related
- [Four process-level error categories account for roughly nine in ten attributed failures in VCoT geometry solving](four-process-error-categories-dominate-failures.md) — related
- [The review reports, citing Polverini and Gregorcic, that ChatGPT-4-Turbo solves physics tasks with line graphs with a similar overall score as high school students](chatgpt-4-turbo-line-graph-physics-score-similar-high-school-students.md) — related
- [Studies using both text- and image-based questions show higher pooled LLM accuracy (78%) than text-only studies (71%)](multimodal-questions-higher-llm-accuracy.md) — reports the opposite
- [LLMs underperformed on image-based dental examination questions compared with text-based questions](llms-underperform-image-based-questions.md) — related
