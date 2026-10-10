---
type: claim
title: Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness
description: Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness
id: student-context-personalization-improves-tutor-metrics
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: udeshi-2026
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: udeshi-2026-2
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: udeshi-2026-3
    resource: "https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    title: "Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home"
    author: Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Providing an AFPM mastery estimate decreased tutor giving away the final answer by 55.16% ± 7.42%, increased behavioral engagement by 2.83% ± 1.73%, and decreased text complexity (reading level) by 5.59% ± 1.57%. [→ Udeshi 2026](#udeshi-2026)
`q2 i?` Providing AFPM levels of prerequisite skills with instructions to request review and give worked examples increased next-item correctness by 2.74% ± 2.46%. [→ Udeshi 2026 (2)](#udeshi-2026-2)
`q2 i?` Providing a problem attempt history summary increased next-item correctness by 3.37% ± 3.79% and behavioral engagement by 2.49% ± 2.69%. [→ Udeshi 2026 (3)](#udeshi-2026-3)

## Evidence

### Udeshi 2026

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment supplying an estimate of the user's mastery level on an AFPM scale (Unfamiliar, Attempted, Familiar, Proficient, Mastered) computed from practice history, with the tutor's only other instruction "Please tailor your tutoring style."

> "Tutor giving away final answer decreased by 55.16% ± 7.42% ● Behavioral engagement increased by 2.83% ± 1.73% ● Text complexity (reading level) decreased by 5.59% ± 1.57%"

### Udeshi 2026 (2)

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment providing the tutor with AFPM levels of all prerequisite skills and instructing it to ask students to review skills at attempted or familiar level and to provide a worked example, as illustrated in Table 2.

> "Next item correctness increased by 2.74% ± 2.46%"

### Udeshi 2026 (3)

Udeshi, T., Khazenzon, A., Khan, K., Breen, N., Corwin, R., DiGiano, C., Weatherholtz, K., Zaluski, M. (2026). Methodologies for Improving the Quality of AI Tutoring in K-12 Education. https://sites.google.com/khanacademy.org/aied2026supplementalmaterial/home

`q2 · i?` · `causal · r2`

Live experiment providing Khanmigo a summary of the student's attempt history for the exercise, including questions attempted in the last hour with correctness and counts prior to the last hour; the tutor was only instructed to tailor its tutoring based on the additional context.

> "Next-item-correctness increased by 3.37% ± 3.79% ● Behavioral engagement increased by 2.49% ± 2.69%"

## Discussion


## Related Claims
- [Limiting verbose Math Agent guidance sharply reduced answer giveaway but decreased cognitive engagement](math-agent-guidance-limit-tradeoff.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [LLMKT's predicted knowledge change curves on CoMTA are mixed across the 15 most frequent KCs, though overall they mostly resemble the power law of practice when dialogues have sufficient turns.](llmkt-knowledge-change-curves-show-mixed-trends-resembling-power-law-of-practice.md) — related
- [CLST's predicted mastery levels track response correctness and move similarly for related knowledge components](clst-mastery-tracks-correctness-and-related-kcs.md) — related
- [Most models struggle to engage with a student's prior debugging attempts even when the iteration history is provided](models-struggle-acknowledging-debugging-progression.md) — related
