---
type: claim
title: "Even with the multi-agent system, some feedback still contains over-praise and over-inference, and Agent 2's detection and revision are not fully accurate"
description: "Even with the multi-agent system, some feedback still contains over-praise and over-inference, and Agent 2's detection and revision are not fully accurate"
id: residual-feedback-issues-multi-agent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: guo-2024
    resource: "https://doi.org/10.48550/arXiv.2411.07407"
    title: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)"
    author: "Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X."
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Even with the multi-agent system, some feedback still contains over-praise and over-inference, and Agent 2's detection and revision are not fully accurate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Residual over-praise and over-inference persist after multi-agent validation; Agent 2 sometimes mis-evaluates feedback, leading to unsatisfactory revisions. [→ Guo 2024](#guo-2024)

## Evidence

### Guo 2024

Guo, S., Latif, E., Zhou, Y., Huang, X., & Zhai, X. (2024). Using Generative AI and Multi-Agents to Provide Automatic Feedback. [doi:10.48550/arXiv.2411.07407](https://doi.org/10.48550/arXiv.2411.07407)

`q1 · i?` · `causal · r2`

Authors' stated limitation in the Limitations and Future Study section, acknowledging incomplete detection accuracy and incomplete revision by the validation agent; no error rate for these residual failures is printed.

> "Although AutoFeedback developed in this study significantly lowered the occurrence of over-praise and over-inference, Agent 2 did not always detect these problems with complete accuracy. At the same time, not all of the issues identified by Agent 2 were fully resolved in the final feedback."

## Discussion


## Related Claims
- [The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback](autofeedback-multi-agent-reduces-over-praise-over-inference.md) — related
- [A single GenAI agent generating feedback on science constructed responses produces over-praise in 15.42% of feedback and over-inference in 27.20%, with 9.58% exhibiting both](single-agent-genai-feedback-over-praise-over-inference-rates.md) — related
- [Judge-condition verification did not consistently improve LLM feedback quality and often propagated Peer agents' errors](judge-verification-propagates-peer-errors.md) — related
- [Accurate LLM solution diagnosis does not reliably produce pedagogically actionable feedback, with lowest rubric scores on error identification and actionability](accurate-diagnosis-not-actionable-feedback.md) — related
