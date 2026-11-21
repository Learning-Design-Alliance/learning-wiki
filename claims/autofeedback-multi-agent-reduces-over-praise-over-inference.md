---
type: claim
title: The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback
description: The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback
id: autofeedback-multi-agent-reduces-over-praise-over-inference
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: guo-2024
    resource: "https://doi.org/10.48550/arXiv.2411.07407"
    title: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)"
    author: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: guo-2024-2
    resource: "https://doi.org/10.48550/arXiv.2411.07407"
    title: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)"
    author: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding a validation agent significantly reduced over-praise (15.42% to 1.25%), over-inference (27.20% to 7.08%), and both issues (9.58% to 0.83%) compared with a single agent. [→ Guo 2024](#guo-2024)

## Evidence

### Guo 2024

Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)

`q2 · i?` · `design · r2`

Comparison on the same 240-response dataset: single-agent versus AutoFeedback (Agent 1 plus Agent 2 validation), both using GPT-4o. Table 1 reports over-praise falling from 37/15.42 to 3/1.25, over-inference from 68/27.20 to 17/7.08, and both issues from 23/9.58 to 2/0.83, with chi-square p = 0.000 for each contrast.

> "The chi-square test revealed that the AutoFeedback generated significantly less feedback with over-praise and/or over-inference problems (p < 0.001), indicating that the GenAI multi-agent significantly outperformed the GenAI single-agent system, resulting in a higher proportion of more qualified automatic feedback."

### Guo 2024 (2)

Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)

`q2 · i?` · `causal · r2`

The conclusions section restates the same comparison as percentage-point decreases: "over-praise and over-inference decreased by 14.17% and 20.21%, respectively", and an 8.75% reduction for feedback with both problems.

> "By using AutoFeedback, the occurrence of over-praise and over-inference decreased by 14.17% and 20.21%, respectively, compared to a single agent. For feedback containing both over-praise and over-inference (9.58%), AutoFeedback reduced the percentage by 8.75%."

## Discussion


## Related Claims
- [A single GenAI agent generating feedback on science constructed responses produces over-praise in 15.42% of feedback and over-inference in 27.20%, with 9.58% exhibiting both](single-agent-genai-feedback-over-praise-over-inference-rates.md) — possibly the same claim (merge candidate)
- [Even with the multi-agent system, some feedback still contains over-praise and over-inference, and Agent 2's detection and revision are not fully accurate](residual-feedback-issues-multi-agent.md) — related
- [Multi-agent tutoring architectures show superior behaviour modelling and feedback compared to single-agent or rule-based tutors](multi-agent-tutoring-superior-single-agent.md) — a broader claim this one bears on
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
