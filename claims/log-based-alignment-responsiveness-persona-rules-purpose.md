---
type: claim
title: "Log-based evaluation showed chatbot alignment was stronger for responsiveness (88.9%) and persona (81.5%) than for rules (70.4%) and purpose (59.3%)"
description: "Log-based evaluation showed chatbot alignment was stronger for responsiveness (88.9%) and persona (81.5%) than for rules (70.4%) and purpose (59.3%)"
id: log-based-alignment-responsiveness-persona-rules-purpose
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: riahi-2026
    resource: "https://doi.org/10.48550/arxiv.2609.29993"
    title: "Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V. (2026). Will It Teach as Intended? How Teachers Configure Educational AI Chatbots. https://arxiv.org/abs/2609.29993 [doi:10.48550/arxiv.2609.29993](https://doi.org/10.48550/arxiv.2609.29993)"
    author: "Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: riahi-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.29993"
    title: "Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V. (2026). Will It Teach as Intended? How Teachers Configure Educational AI Chatbots. https://arxiv.org/abs/2609.29993. [doi:10.48550/arxiv.2609.29993](https://doi.org/10.48550/arxiv.2609.29993)"
    author: "Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Log-based evaluation showed chatbot alignment was stronger for responsiveness (88.9%) and persona (81.5%) than for rules (70.4%) and purpose (59.3%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Bot-level evaluation of 27 unique chatbots across four criteria found responsiveness was the strongest dimension (88.9% pass, Avg = 3.67) and purpose alignment the weakest (59.3% pass, Avg = 3.00). [→ Riahi 2026](#riahi-2026)
`q2 i?` A chatbot could generate a reasonable response without consistently reflecting the instructional goal or intended function defined by the teacher. [→ Riahi 2026 (2)](#riahi-2026-2)

## Evidence

### Riahi 2026

Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V. (2026). Will It Teach as Intended? How Teachers Configure Educational AI Chatbots. https://arxiv.org/abs/2609.29993 [doi:10.48550/arxiv.2609.29993](https://doi.org/10.48550/arxiv.2609.29993)

`q2 · i?` · `design · r2`

Log-based evaluation of 27 unique chatbot configurations using a four-criterion rubric (Responsiveness, Purpose, Rules, Persona) rated on a four-point ordinal scale and collapsed to pass/fail. Full dataset comprised 1,160 criterion-level evaluations.

> "Responsiveness was the strongest dimension (88.9%, Avg = 3.67), indicating that most bots were able to produce relevant and usable responses when users interacted with them."

### Riahi 2026 (2)

Riahi, B., Ozturk, D., Guth, A., Li, J., Singh, D. P., Tian, X., Chiu, J., Lytle, N., Barnes, T., & Cateté, V. (2026). Will It Teach as Intended? How Teachers Configure Educational AI Chatbots. https://arxiv.org/abs/2609.29993. [doi:10.48550/arxiv.2609.29993](https://doi.org/10.48550/arxiv.2609.29993)

`q2 · i?` · `design · r2`

Bot-level evaluation found purpose alignment weakest, followed by rule adherence (70.4%, Avg = 3.26) and persona (81.5%, Avg = 3.48), suggesting a gap between general conversational performance and fidelity to teacher-defined configurations.

> "Purpose showed the lowest alignment, with a 59.3% pass rate and the lowest average score (Avg = 3.00)."

## Discussion


## Related Claims
- [Teachers used the Purpose field primarily for instructional goals and content focus while Rules specified pedagogical behavior, guardrails, and learner-specific adaptations](purpose-field-goals-rules-field-pedagogical-behavior.md) — related
- [Instructors authoring AI tutoring chatbots in a MOOC almost never systematically tested their bots before deploying them to students](teachers-rarely-test-ai-tutor-bots-before-publication.md) — related
