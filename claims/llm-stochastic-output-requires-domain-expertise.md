---
type: claim
title: LLM output can be misleading or erroneous because a stochastic element in text generation sometimes selects less likely continuations, so it requires continuous supervision and critical evaluation by domain experts.
description: LLM output can be misleading or erroneous because a stochastic element in text generation sometimes selects less likely continuations, so it requires continuous supervision and critical evaluation by domain experts.
id: llm-stochastic-output-requires-domain-expertise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: huber-2024
    resource: "https://doi.org/10.1007/s10648-024-09868-z"
    title: "Huber, S. E., Kiili, K., Nebel, S., Ryan, R. M., Sailer, M., & Ninaus, M. (2024). Leveraging the Potential of Large Language Models in Education Through Playful and Game-Based Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09868-z"
    author: "Huber, S. E., Kiili, K., Nebel, S., Ryan, R. M., Sailer, M., & Ninaus, M."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 2
---

# LLM output can be misleading or erroneous because a stochastic element in text generation sometimes selects less likely continuations, so it requires continuous supervision and critical evaluation by domain experts.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because present LLMs sometimes choose a less likely continuation rather than the most likely one, their output can be misleading or erroneous and requires continuous supervision and critical evaluation. [→ Huber 2024](#huber-2024)

## Evidence

### Huber 2024

Huber, S. E., Kiili, K., Nebel, S., Ryan, R. M., Sailer, M., & Ninaus, M. (2024). Leveraging the Potential of Large Language Models in Education Through Playful and Game-Based Learning. Educational Psychology Review. https://doi.org/10.1007/s10648-024-09868-z

`q1 · i?` · `theoretical · r2`

Theoretical argument in this perspective piece: the authors explain that LLMs compute likely continuations of prompts and that the stochastic selection of "a less likely continuation" is why output can be misleading or erroneous. No empirical data are reported.

> "An important ingredient in the computation is the fact that not always the most likely, but sometimes a less likely continuation is chosen."

## Discussion


## Related Claims
- [Optimizing prompts can vastly improve the accuracy of LLM outputs, but critical evaluation of the resulting outputs still requires domain expertise.](prompt-optimization-improves-accuracy-expertise-still-needed.md) — possibly the same claim (merge candidate)
- [Surface validation can function while substantive validation fails: most participants detected flawed AI recommendations yet continued following them](surface-validation-works-substantive-validation-fails.md) — related
- [Students' critical examination of AI-generated outputs increased across learning cycles, though unevenly, with some participants continuing to seek confirmation from AI](critical-evaluation-of-ai-outputs-increased-unevenly.md) — related
- [Students perceived the teacher’s modeling with contrasting cases as a turning point that repositioned them as active gatekeepers of AI-generated content](contrasting-cases-gatekeeper-repositioning.md) — related
- [GenAI feedback limitations require students to exercise evaluative judgement](genai-limitations-require-evaluative-judgement.md) — a broader claim this one bears on
- [Students' top two concerns about educational LLM use are output quality (fabricated or misleading content, 53 mentions) and the verification burden (34 mentions)](students-top-concerns-output-quality-verification-burden.md) — related
- [A structured mixture-of-experts candidate improved some corrections on fixed-evidence cases but introduced new factual and continuity regressions, so activation was held](moe-candidate-mixed-fidelity-result.md) — a narrower finding that bears on this claim
- [Attachment to LLMs exhibits cruel optimism: desired efficiency collides with the vigilance and expertise students do not yet possess](cruel-optimism-of-llms-in-education.md) — related
- [Anthropomorphic language about AIED tools misleads people into overestimating what the tools can do](anthropomorphic-language-misleads-about-aied.md) — related
