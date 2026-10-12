---
type: claim
title: Students whose tutors have access to Tutor CoPilot are 4 percentage points more likely to master lesson topics (pass exit tickets) in live K-12 math tutoring
description: Students whose tutors have access to Tutor CoPilot are 4 percentage points more likely to master lesson topics (pass exit tickets) in live K-12 math tutoring
id: tutor-copilot-raises-exit-ticket-mastery-4pp
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: strong
sources:
  - id: rose-e-wang-2025
    resource: "https://arxiv.org/abs/2410.03017"
    title: "Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017"
    author: Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky
    q: 4
    i: "?"
    kind: causal
    rigour: 2
  - id: rose-e-wang-2025-2
    resource: "https://arxiv.org/abs/2410.03017"
    title: "Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017"
    author: Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky
    q: 4
    i: "?"
    kind: causal
    rigour: 3
  - id: rose-e-wang-2025-3
    resource: "https://arxiv.org/abs/2410.03017"
    title: "Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017"
    author: Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky
    q: 4
    i: "?"
    kind: causal
    rigour: 3
---

# Students whose tutors have access to Tutor CoPilot are 4 percentage points more likely to master lesson topics (pass exit tickets) in live K-12 math tutoring

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2`–`r3` · `q4`

## Subclaims
`q4 i?` In a preregistered intent-to-treat analysis of the RCT, students working with treatment tutors were 4 p.p. more likely to pass exit tickets (62%→66%, p<0.01). [→ Rose E. Wang 2025](#rose-e-wang-2025)
`q4 i?` Students were 2 p.p. more likely to attempt the exit ticket (p<0.1) and, conditional on attempting, 3 p.p. more likely to pass it (p<0.01). [→ Rose E. Wang 2025 (2)](#rose-e-wang-2025-2)
`q4 i?` In a 2SLS analysis of tutors who actually used the tool, students were 14 p.p. more likely to pass exit tickets (p<0.01). [→ Rose E. Wang 2025 (3)](#rose-e-wang-2025-3)

## Evidence

### Rose E. Wang 2025

Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017

`q4 · i?` · `causal · r2`

Preregistered intent-to-treat regression from the randomized controlled trial (900 tutors initially assigned; 4,136 sessions), with student covariates and school-by-grade fixed effects. The article reports a significant positive treatment effect: "4 percentage points (p.p.) more likely to pass their exit tickets (p< 0.01". No standardized effect size is printed.

> "Students working with treatment tutors were 4 percentage points (p.p.) more likely to pass their exit tickets (p< 0.01, 62%→ 66% student passing rate from control to treatment)."

### Rose E. Wang 2025 (2)

Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017

`q4 · i?` · `causal · r3`

Same ITT analysis, secondary session-level measures from Table 2. Attempting the exit ticket was marginal (p<0.1); conditional passing was significant (p<0.01). The article prints no standardized effect size for either measure, so impact is null.

> "We also found that students were 2 p.p. more likely to attempt the exit ticket (p< 0.1), and conditional on their attempt, they were 3 p.p. more likely to pass the exit ticket (p< 0.01)."

### Rose E. Wang 2025 (3)

Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017

`q4 · i?` · `causal · r3`

Two-stage least squares analysis disentangling actual use from mere access, reported in a Results-section footnote. Students of tutors who used the tool were "14 p.p. more likely to pass their exit tickets (p< 0.01". No standardized effect size is printed.

> "Appendix H reports results on the tutors using Tutor CoPilot, rather than just having access to it, where students were 14 p.p. more likely to pass their exit tickets (p< 0.01)."

## Discussion


## Related Claims
- [Tutor Copilot No Significant Effects Secondary Outcomes](tutor-copilot-no-significant-effects-secondary-outcomes.md)
- [Tutor Copilot Benefits Concentrated Among Lower Rated Tutors](tutor-copilot-benefits-concentrated-among-lower-rated-tutors.md)
- [Tutors with Tutor CoPilot access use more understanding-fostering strategies (e.g., prompting students to explain) and rely less on giving away answers than control tutors](tutor-copilot-shifts-tutors-toward-understanding-fostering-strategies.md) — related
- [In a large-scale RCT, real-time LLM-generated pedagogical suggestions for human tutors raised student knowledge-component mastery by 4 percentage points on average, with larger effects for lower-performing or less-experienced tutors](llm-suggestions-human-tutors-mastery-gain.md) — possibly the same claim (merge candidate)
- [Situational-level real-time AI guidance for tutors raised students' topic mastery, especially for students of lower-rated tutors](situational-tutoring-guidance-raises-topic-mastery.md) — possibly the same claim (merge candidate)
- [Tutors perceive Tutor CoPilot as helpful for on-the-spot explanations but flag suggestions that are not grade-level appropriate and 'too smart'](tutors-perceive-tutor-copilot-helpful-but-grade-level-issues.md) — related
