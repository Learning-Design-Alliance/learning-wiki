---
type: claim
title: SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks
description: SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks
id: sped-adaptive-shifts-tutor-behavior-codebooks
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: unggi-lee-2026
    resource: "https://arxiv.org/abs/2605.30670"
    title: "Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670"
    author: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: unggi-lee-2026-2
    resource: "https://arxiv.org/abs/2605.30670"
    title: "Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670"
    author: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The DI We-Do move (lead) jumps from 9.1-14.3% in generic-prompted groups to 21.4-23.6% in SPED-prompted groups, with the I-Do modeling move shrinking by roughly a third. [→ Unggi Lee 2026](#unggi-lee-2026)
`q2 i?` Every disability-supporting EMT move multiplies in SPED-prompted variants (mand_model 2-5x, incidental 2-18x, expansion_recast up to 20x), and EMT affirmation rises from 22.1% in Base to 39.0% in SPED-adaptive. [→ Unggi Lee 2026 (2)](#unggi-lee-2026-2)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670

`q2 · i?` · `design · r2`

LLM-labeled turn-level Direct Instruction codebook analysis over N=11,103 tutor turns from the seven trained models, grouped as Base, Think, SPED-static, and SPED-adaptive. Reported with chi-square tests of independence (DI turn chi-square(15)=714.1, p<10-100, Cramer's V=0.146).

> "The We-Do move (lead) jumps from 9.1-14.3% across the generic-prompt groups (Base, Think∗) to 21.4-23.6% across the SPED-prompted groups (SPED-static∗, SPED-adaptive∗), and the I-Do procedure-modeling move (model) shrinks by roughly a third"

### Unggi Lee 2026 (2)

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670

`q2 · i?` · `design · r2`

Turn- and sentence-level Enhanced Milieu Teaching codebook analysis over N=60,745 sentences, reported with chi-square(18)=636.1, p<10-100, Cramer's V=0.138. Sentence-level EMT affirmation rises from 22.1% in Base to 39.0% in SPED-adaptive.

> "Every disability-supporting EMT move multiplies in the SPED-prompted variants relative to generic-prompted baselines:mand_model 2-5×, incidental 2-18×, expansion_recast up to 20×, time_delay∼ 3×, env_arrange 2×"

## Discussion


## Related Claims
- [The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline](special-r1-raises-persona-fit-and-sped-helpfulness.md) — related
- [Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback](tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) — related
- [LLM scaffolding level is associated with the student's next dialogue act, and the association persists within broad request categories](scaffolding-associated-with-next-student-move.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
- [Prompting a learning disability shifts feedback toward word- and sentence-level remediation, simplified vocabulary, and lowered expectations](learning-disability-feedback-lowered-expectations.md) — related
- [Iterative prompt refinement shifted a generative-AI tutor from tutorial-style explanation delivery toward dialogic Socratic support for K-12 beginners](prompt-refinement-shifts-genai-toward-socratic-support.md) — related
- [The AI's nonjudgmental conversational tone and adaptive prompting fostered risk-taking and productive struggle in a psychologically safe environment](nonjudgmental-ai-tone-risk-taking.md) — related
