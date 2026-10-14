---
type: claim
title: Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams
description: Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams
id: genai-homework-advantage-no-transfer
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: ethan-dickey-2026
    resource: "https://arxiv.org/abs/2607.27586"
    title: "Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586"
    author: Ethan Dickey, Marios Mertzanidis, Alexandros Psomas
    q: 3
    i: 1
    kind: causal
    rigour: 2
  - id: ethan-dickey-2026-2
    resource: "https://arxiv.org/abs/2607.27586"
    title: "Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586"
    author: Ethan Dickey, Marios Mertzanidis, Alexandros Psomas
    q: 3
    i: 1
    kind: causal
    rigour: 2
---

# Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i1` small

## Subclaims
`q3 i1` Within-student difference scores on the GenAI-graded problem differed significantly between groups (Mann-Whitney U=7,046, p=.035, r=.14; t(218)=2.90, p=.004, d=.39). [→ Ethan Dickey 2026](#ethan-dickey-2026)
`q3 i1` A parallel significant difference appeared on identical student-solved problems (U=7,119, p=.024, r=.15), which the authors attribute to time-varying factors rather than the intervention. [→ Ethan Dickey 2026 (2)](#ethan-dickey-2026-2)

## Evidence

### Ethan Dickey 2026

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586

`q3 · i1` · `causal · r2`

Within-student change scores in homework performance across course halves in the crossover study; Group A showed M=18±25 vs Group B 9±23 on GenAI questions, "a small effect size (Cohen's𝑑=.39)".

> "For the GenAI-graded problems, the Mann–Whitney test indicated a statistically significant difference between groups (𝑈= 7,046,𝑝=. 035), with a small effect size (𝑟=. 14). A confirmatory independent-samples 𝑡-test yielded a consistent result,𝑡( 218)= 2.90,𝑝=. 004, with a small effect size (Cohen's𝑑=.39)."

### Ethan Dickey 2026 (2)

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586

`q3 · i1` · `causal · r2`

Identical non-GenAI homework items also differed significantly across halves (r=.15), so the article concludes this pattern means homework-level differences should not be read as direct evidence of a learning effect from the GenAI activity.

> "For the student-solved (non-GenAI) problems, the Mann–Whitney test likewise indicated a statistically significant difference between groups (𝑈= 7,119,𝑝=. 024), with a small effect size ( 𝑟=.15)."

## Discussion


## Related Claims
- [Evaluating GenAI-generated solutions produced no significant differences on midterm scores, final exam scores, course percentages, or normalized exam change relative to solving problems directly](genai-evaluation-null-summative-algorithms.md) — related
- [Prior GenAI-solution evaluation showed no significant benefit on exam problems structurally aligned with the homework, with the midterm comparison inconclusive due to a floor effect](genai-aligned-exam-null-floor-effect.md) — a narrower finding that bears on this claim
- [Falsifiable hypothesis: unrestricted AI use on deep-processing tasks will produce a product–process dissociation—higher-rated assignments but lower unaided delayed transfer](h3-product-process-dissociation-hypothesis.md) — a broader claim this one bears on
- [Most students reported no change in study habits, but students who adapted their study strategies rated GenAI-evaluation assignments as significantly more helpful](study-habit-adapters-rate-genai-grading-helpful.md) — related
- [Unrestricted ChatGPT access yields better practice performance but significantly worse exam scores](gpt4-access-harms-learning-after-withdrawal.md) — related
