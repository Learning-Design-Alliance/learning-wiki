---
type: claim
title: In the pilot workshop, the LLM unreliably produced fill-in-the-blank snippets, often returning complete code solutions instead
description: In the pilot workshop, the LLM unreliably produced fill-in-the-blank snippets, often returning complete code solutions instead
id: pilot-llm-unreliable-fill-in-blank
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: tseng-2026
    resource: "https://arxiv.org/abs/2607.06721"
    title: "Tseng, T., Seoror, L.H., Adda, J., Factor, M., Darabi, R., Matschke, K.R., Fu, T., Lin, A., Maram, A., Sinha, A. (2026). Flowcode: An AI-Powered Programming Environment for Scaffolding Iteration in Creative Computing Education. https://arxiv.org/abs/2607.06721"
    author: Tseng, T., Seoror, L.H., Adda, J., Factor, M., Darabi, R., Matschke, K.R., Fu, T., Lin, A., Maram, A., Sinha, A.
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# In the pilot workshop, the LLM unreliably produced fill-in-the-blank snippets, often returning complete code solutions instead

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` Code snippets generated during the pilot did not reliably use the fill-in-the-blank approach; one participant saw 24 of their prompts incorrectly return full code snippets, while two of seven never encountered the problem. [→ Tseng 2026](#tseng-2026)

## Evidence

### Tseng 2026

Tseng, T., Seoror, L.H., Adda, J., Factor, M., Darabi, R., Matschke, K.R., Fu, T., Lin, A., Maram, A., Sinha, A. (2026). Flowcode: An AI-Powered Programming Environment for Scaffolding Iteration in Creative Computing Education. https://arxiv.org/abs/2607.06721

`q2 · i?` · `design · r3`

Observation from the pilot workshop (n=7) interaction logs and screen recordings. The article reports the issue varied among participants and that "once the LLM incorrectly generated complete code for a specific user, it continued to do so in most subsequent responses throughout the workshop."

> "This behavior varied among partici- pants, with two of the seven participants never encountering the problem, whereas one participant saw 24 of their prompts incor- rectly return full code snippets."

## Discussion


## Related Claims
- [Participants used the Flowcode LLM across all stages of their design process, most frequently asking for code explanations](llm-use-across-design-stages.md) — related
- [Automatically updating the flowchart and injecting generated code into editors drew participants away from explanations and toward direct code editing](auto-updates-drew-users-from-explanations.md) — related
- [ChatGPT produced executed, grader-accepted submissions for all three fixed personalized Qiskit assignment instances in 150 of 150 sessions](chatgpt-completes-all-150-qiskit-homework-sessions.md) — related
