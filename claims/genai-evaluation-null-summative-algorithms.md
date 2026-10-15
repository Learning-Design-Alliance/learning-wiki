---
type: claim
title: Evaluating GenAI-generated solutions produced no significant differences on midterm scores, final exam scores, course percentages, or normalized exam change relative to solving problems directly
description: Evaluating GenAI-generated solutions produced no significant differences on midterm scores, final exam scores, course percentages, or normalized exam change relative to solving problems directly
id: genai-evaluation-null-summative-algorithms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ethan-dickey-2026
    resource: "https://doi.org/10.48550/arxiv.2607.27586"
    title: "Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586 [doi:10.48550/arxiv.2607.27586](https://doi.org/10.48550/arxiv.2607.27586)"
    author: Ethan Dickey, Marios Mertzanidis, Alexandros Psomas
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: ethan-dickey-2026-2
    resource: "https://arxiv.org/abs/2607.27586"
    title: "Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586"
    author: Ethan Dickey, Marios Mertzanidis, Alexandros Psomas
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Evaluating GenAI-generated solutions produced no significant differences on midterm scores, final exam scores, course percentages, or normalized exam change relative to solving problems directly

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q3`

## Subclaims
`q3 i?` In a randomized crossover algorithms course (N=220), midterm scores did not differ significantly between the solving and GenAI-evaluation groups (t(218)=-0.58, p=.56, d=-0.08). [→ Ethan Dickey 2026](#ethan-dickey-2026)
`q3 i?` Final exam scores (t(218)=-0.39, p=.70, d=-0.05), normalized change (d=0.03), overall course percentages (d=0.13), and letter-grade distributions (Cramer's V=.07) were all statistically indistinguishable between groups. [→ Ethan Dickey 2026 (2)](#ethan-dickey-2026-2)

## Evidence

### Ethan Dickey 2026

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586 [doi:10.48550/arxiv.2607.27586](https://doi.org/10.48550/arxiv.2607.27586)

`q3 · i?` · `causal · r2`

Randomized A/B crossover study in a junior-level algorithms course; independent-samples t-tests after assumption checks. Midterm showed "a negligible effect size (Cohen's𝑑=− 0.08)" with CI [-4.8, 2.6], indicating no significant group difference.

> "Midterm examination scores did not differ significantly between groups,𝑡( 218)=− 0.58,𝑝=. 56, with a 95% CI of[−4.8, 2.6] points and a negligible effect size (Cohen's𝑑=− 0.08)."

### Ethan Dickey 2026 (2)

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586

`q3 · i?` · `causal · r2`

Final exam (maximum 113) comparison in the same crossover study; the article also reports no significant differences for normalized change (d=0.03), course percentages (d=0.13), and letter grades (chi-squared p=.38, Cramer's V=.07).

> "Final examination scores likewise showed no significant difference,𝑡( 218)=− 0.39, 𝑝=.70, 95% CI[−5.4,3.6]points,𝑑=−0.05."

## Discussion


## Related Claims
- [Prior GenAI-solution evaluation showed no significant benefit on exam problems structurally aligned with the homework, with the midterm comparison inconclusive due to a floor effect](genai-aligned-exam-null-floor-effect.md) — a narrower finding that bears on this claim
- [Midterm self-efficacy (comfort and confidence) did not differ between conditions after three assignments, though both varied significantly across algorithmic topics](genai-condition-no-self-efficacy-difference.md) — related
- [Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams](genai-homework-advantage-no-transfer.md) — related
- [The instructor's own final exam showed the same direction of advantage on the intact randomized sample, with no difference on the pre-treatment midterm](instructor-final-confirms-tutor-advantage-direction.md) — reports the opposite
