---
type: claim
title: Understanding-focused prompts predict higher learning gains, and clarity amplifies the benefits of development and understanding prompts
description: Understanding-focused prompts predict higher learning gains, and clarity amplifies the benefits of development and understanding prompts
id: understanding-clarity-prompts-predict-learning-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: brender-2025
    resource: "https://doi.org/10.1007/978-3-032-03870-8_7"
    title: "Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)"
    author: Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E.
    q: 3
    i: 0
    kind: causal
    rigour: 2
  - id: brender-2025-2
    resource: "https://doi.org/10.1007/978-3-032-03870-8_7"
    title: "Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)"
    author: Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E.
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: brender-2025-3
    resource: "https://doi.org/10.1007/978-3-032-03870-8_7"
    title: "Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)"
    author: Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Understanding-focused prompts predict higher learning gains, and clarity amplifies the benefits of development and understanding prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q3` · `i0`–`i3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Brender 2025 (2): no comparison group (read from the study by two models, 2026-11-21)

## Subclaims
`q3 i0` A larger proportion of Understanding prompts is a significant positive predictor of learning gain (β = 0.23, p = 0.017). [→ Brender 2025](#brender-2025)
`q3 i3` Clear development prompts (Clarity × Development, β = 0.77, p < .001) and clear understanding prompts (Clarity × Understanding, β = 0.75, p < .001) contribute to learning gains. [→ Brender 2025 (2)](#brender-2025-2)
`q3 i?` A significant negative interaction between Understanding and Granularity (β = −0.36, p = .022) suggests overly detailed prompts may dampen learning benefits. [→ Brender 2025 (3)](#brender-2025-3)

## Evidence

### Brender 2025

Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)

`q3 · i0` · `causal · r2`

Stepwise and multiple linear regression on session 3 data (54 observations) predicting normalized learning gain from prompt types and attributes; the printed standardized coefficient for Understanding prompts is β = 0.23, a small effect, within the model retaining all variables (R2 = .45, adjusted R2 = .35, F(8, 45) = 2.06, p < 0.01).

> "The results show that a larger proportion of Understanding prompts is a significant positive predictor ( β = 0 .23, p = 0 .017, p < 0.05) of learning gain."

### Brender 2025 (2)

Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)

`q3 · i3` · `causal · r2`

Same session 3 regression model: the printed interaction coefficients are large (β = 0.77 and β = 0.75, both p < .001); the authors interpret that higher Clarity amplifies the positive relationships of Development and Understanding with learning gains.

> "having development prompts that are clear (interaction between Clarity and Development, β = 0.77, p < .001) and clear prompts that seek to improve students' understanding (interaction effect between Clarity and Understanding, β = 0.75, p < .001) contribute to learning."

### Brender 2025 (3)

Brender, J., El-Hamamsy, L., Uittenhove, K., Mondada, F., Bumbacher, E. (2025). Structured Prompts, Better Outcomes? Exploring the Effects of a Structured Interface with ChatGPT in a Graduate Robotics Course. [doi:10.1007/978-3-032-03870-8_7](https://doi.org/10.1007/978-3-032-03870-8_7)

`q3 · i?` · `causal · r2`

Same regression model; no significant interaction was found between Development and Granularity (β = −0.29, p = .29). The session 2 model retaining only Clarity was not significant (F(1, 56) = 2.06, p = .15, R2 = .036).

> "A significant negative interaction between Understanding and Granularity (β = −0.36, p = .022) suggests that overly detailed prompts may dampen the benefits of learning."

## Discussion


## Related Claims
- [Higher proportion of student-generated text in prompts is marginally associated with learning gains, and the structured interface increased self-written input only while in use](self-generated-prompt-input-marginal-learning-association.md) — related
- [A structured prompting interface produced no significant differences in learning or performance compared with free ChatGPT use in graduate robotics labs](structured-prompting-interface-no-learning-performance-difference.md) — related
- [Higher compliance with MetaTutor's review-notes prompt is associated with larger proportional learning gains](review-notes-compliance-predicts-learning-gains.md) — related
- [Higher compliance with MetaTutor's suggest-subgoal prompt is associated with larger proportional learning gains](suggest-subgoal-compliance-predicts-learning-gains.md) — related
- [Higher compliance with MetaTutor's revise-summary prompt is associated with larger proportional learning gains](revise-summary-compliance-predicts-learning-gains.md) — related
- [Form-focused instruction combined with prompts is more effective than FFI combined with recasts or no feedback, especially on written tasks](ffi-with-prompts-beats-recasts-for-gender.md) — related
