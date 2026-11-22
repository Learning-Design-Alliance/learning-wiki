---
type: claim
title: AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content
description: AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content
id: ai-hints-aligned-exam-performance-only
aliases: [ai-hints-associated-exam2-performance]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: malikova-z-2026
    resource: "https://doi.org/10.3389/feduc.2026.1964629"
    title: "Malikova Z, Ualikhanova B, Turmambekov T, Rakhashev B and Berdaliyev D (2026). Artificial intelligence in university physics education: a systematic review of empirical studies. Front. Educ. 11:1964629. https://doi.org/10.3389/feduc.2026.1964629"
    author: Malikova Z, Ualikhanova B, Turmambekov T, Rakhashev B and Berdaliyev D
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: yifan-lu-2025
    resource: "https://doi.org/10.1103/v93w-ytyc"
    title: "Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko. (2025). Incentivizing supplemental math assignments and using AI-generated hints is associated with improved exam performance. arXiv. Originally published 2024. [doi:10.1103/v93w-ytyc](https://doi.org/10.1103/v93w-ytyc)"
    author: Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: yifan-lu-2025-2
    resource: "https://doi.org/10.1103/v93w-ytyc"
    title: "Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko. (2025). Incentivizing supplemental math assignments and using AI-generated hints is associated with improved exam performance. arXiv. Originally published 2024. [doi:10.1103/v93w-ytyc](https://doi.org/10.1103/v93w-ytyc)"
    author: Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies (3 entries) · 1 causal `r2`, 1 associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims

`q2 i?` In Lu et al. (2025), AI-hint use during homework was significantly associated with exam performance only for items closely matching homework content (b = 0.40, p = .004); no significant association was observed for other items. [→ Malikova Z 2026](#malikova-z-2026)

`q2 i?` There is a statistically significant association between Exam 2 score and AI hints usage, the exam most aligned with homework (ISI = 0.4). [→ Yifan Lu 2025](#yifan-lu-2025)

`q2 i?` No significant association between AI hints usage and exam performance was found for Exams 1 and 3, possibly due to low relevance between those exams and the homework questions. [→ Yifan Lu 2025 (2)](#yifan-lu-2025-2)

## Evidence

### Malikova Z 2026

Malikova Z, Ualikhanova B, Turmambekov T, Rakhashev B and Berdaliyev D (2026). Artificial intelligence in university physics education: a systematic review of empirical studies. Front. Educ. 11:1964629. https://doi.org/10.3389/feduc.2026.1964629

`q2 · i?` · `associational · r1`

The review reports this non-randomized study of 382 students in two sections of a calculus-based introductory mechanics course; Table 5 lists the reported indicator "b = 0.40, p = .004" for aligned exam performance.

> "However, the association was statistically significant only when the examination questions closely matched the homework content; no significant association was observed for other examination items."

### Yifan Lu 2025

Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko. (2025). Incentivizing supplemental math assignments and using AI-generated hints is associated with improved exam performance. arXiv. Originally published 2024. [doi:10.1103/v93w-ytyc](https://doi.org/10.1103/v93w-ytyc)

`q2 · i?` · `causal · r2`

OLS regression on Exam 2 z-scores (Table VIII) shows an AI hints usage coefficient of 0.40 (p = 0.004); Fig. 6 plots Exam 2 score versus FCI score separated by hint use, suggesting larger benefit for less-prepared students.

> "We found a statistically significant association between Exam 2 score and AI hints usage, as demonstrated in Fig. 6 and Tab. VIII. Interestingly, the linear fit result in Fig. 6 suggests that AI-generated hints might benefit students who are less prepared to a larger extent."

### Yifan Lu 2025 (2)

Yifan Lu, K. Supriya, Shanna Shaked, Elizabeth H. Simmons, and Alexander Kusenko. (2025). Incentivizing supplemental math assignments and using AI-generated hints is associated with improved exam performance. arXiv. Originally published 2024. [doi:10.1103/v93w-ytyc](https://doi.org/10.1103/v93w-ytyc)

`q2 · i?` · `causal · r2`

Regressions for Exams 1 and 3 (Tables VII and III) show non-significant AI hints usage coefficients (p = 0.337 and p = 0.240); the article attributes this to low Isomorphism Index between those exams and homework questions.

> "However, we did not find a significant association between student exam performance and AI hints usage for Exams 1 and 3, possibly due to the low relevance between these exams and the homework questions, as indicated from the ISI in Tab. I."

## Discussion



## Related Claims

- [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](chatgpt-hints-significant-gains-versus-control.md) — the general claim this finding bears on, with the studies behind it
- [Unguarded answer-giving AI harmed unaided exam performance while a guarded version of the same model erased the harm (Bastani et al., 2025, as reported)](gpt4-access-harms-learning-after-withdrawal.md) — related
- [A wrong response preceding a help request is associated with a higher predicted probability of a correct end-of-unit response than the request alone](wrong-then-request-joint-effect-higher.md) — related
- [A scaffolded AI Study Coach produced no assignment-performance or concept-inventory advantage over unrestricted AI use in a master's programming course pilot](scaffolded-coach-no-assignment-performance-advantage.md) — related
- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](persistence-costs-concentrated-among-direct-solution-users.md) — related
- [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface](gpt-tutor-improves-practice-more-than-gpt-base.md) — related
- [Successful students showed significantly higher engagement action counts in in-unit assignments, while struggling students requested more hints, answers and explanations.](struggling-students-request-more-hints-answers-explanations.md) — related
- [Completing supplemental math material 1 (vectors) is associated with better exam performance, and the association grows with the material's relevance to exam content](vectors-material-completion-better-exam-performance.md) — related
- [In Experiment 1, compulsory GAI-powered personalized recommendation with heuristic hints significantly improved physics performance for low-achieving students (d = 0.673)](gai-hints-improve-low-achievers-compulsory-recommendation.md) — related
