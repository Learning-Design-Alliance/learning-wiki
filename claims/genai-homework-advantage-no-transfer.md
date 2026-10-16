---
type: claim
title: Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams
description: Students received significantly higher homework scores during GenAI-evaluation periods, but this advantage did not transfer to downstream exams
id: genai-homework-advantage-no-transfer
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: ethan-dickey-2026
    resource: "https://doi.org/10.48550/arxiv.2607.27586"
    title: "Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586 [doi:10.48550/arxiv.2607.27586](https://doi.org/10.48550/arxiv.2607.27586)"
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

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586 [doi:10.48550/arxiv.2607.27586](https://doi.org/10.48550/arxiv.2607.27586)

`q3 · i1` · `causal · r2`

Within-student change scores in homework performance across course halves in the crossover study; Group A showed M=18±25 vs Group B 9±23 on GenAI questions, "a small effect size (Cohen's𝑑=.39)".

> "For the GenAI-graded problems, the Mann–Whitney test indicated a statistically significant difference between groups (𝑈= 7,046,𝑝=. 035), with a small effect size (𝑟=. 14). A confirmatory independent-samples 𝑡-test yielded a consistent result,𝑡( 218)= 2.90,𝑝=. 004, with a small effect size (Cohen's𝑑=.39)."

### Ethan Dickey 2026 (2)

Ethan Dickey, Marios Mertzanidis, Alexandros Psomas. (2026). Is Solving Better Than Evaluating GenAI Solutions? https://arxiv.org/abs/2607.27586

`q3 · i1` · `causal · r2`

Identical non-GenAI homework items also differed significantly across halves (r=.15), so the article concludes this pattern means homework-level differences should not be read as direct evidence of a learning effect from the GenAI activity.

> "For the student-solved (non-GenAI) problems, the Mann–Whitney test likewise indicated a statistically significant difference between groups (𝑈= 7,119,𝑝=. 024), with a small effect size ( 𝑟=.15)."

## Studies bearing on this claim

<!-- synthesis:start -->
*Do gains learners make with generative AI on coursework show up on midterm and final exams taken without it?* This table gathers the studies behind this claim and the 8 narrower claims that bear on it: **5 distinct studies** (3 associational, 2 causal), `q2`–`q3`, 2 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Ethan Dickey 2026](https://doi.org/10.48550/arxiv.2607.27586) | q3 · causal · r2 | i1; i? | this claim; [Evaluating GenAI-generated solutions produced no significant differences on midterm scores](genai-evaluation-null-summative-algorithms.md) (supports); [Prior GenAI-solution evaluation showed no significant benefit on exam problems structurall](genai-aligned-exam-null-floor-effect.md) (supports) |
| [Minju Park 2026](https://doi.org/10.48550/arxiv.2605.04534) | q2 · associational · r1 | i2; i? | [Students who used LLMs on assignments scored significantly lower than non-users on the fir](llm-users-lower-midterm1-score-gap-narrowed.md) (supports); [Among LLM users, Low-Reliance students (use in under half of submissions) consistently out](low-reliance-outperformed-high-reliance-midterms.md) (supports) |
| [David Racovan 2026](https://doi.org/10.48550/arxiv.2609.36073) | q2 · associational · r1 | i? | [Flagged Spring 2026 students scored lower on all three exams than non-flagged peers, with ](flagged-students-lower-exam-scores-dose-response.md) (supports); [Average homework H-scores correlate negatively with proctored exam performance, with the c](h-score-negative-exam-correlation-strengthening.md) (supports) |
| [Shuang Geng 2026](https://doi.org/10.48550/arxiv.2607.28710) | q2 · associational · r1 | i? | [At baseline, mechanics-specific AI use was inversely related to course performance, but th](baseline-mechanics-ai-use-inversely-related-performance.md) (supports) |
| [Xinming Yang 2025](https://doi.org/10.48550/arxiv.2508.05979) | q2 · causal · r1 | i? | [Learning-by-teaching an LLM improved assignment and project performance versus historical ](learning-by-teaching-llm-improves-assignments-projects.md) (supports) |
<!-- synthesis:end -->

## Discussion

## Related Claims

- [AI-supported instruction has a moderate positive effect on student achievement in STEM education (g = 0.670 under a random effects model)](ai-instruction-stem-moderate-positive-effect.md) — the general claim this finding bears on, with the studies behind it

- [Timely feedback on homework increases learning, and computer platforms providing immediate feedback help teachers adapt](timely-feedback-improves-homework-learning.md) — the general claim this finding bears on, with the studies behind it
- [Evaluating GenAI-generated solutions produced no significant differences on midterm scores, final exam scores, course percentages, or normalized exam change relative to solving problems directly](genai-evaluation-null-summative-algorithms.md) — related
- [Prior GenAI-solution evaluation showed no significant benefit on exam problems structurally aligned with the homework, with the midterm comparison inconclusive due to a floor effect](genai-aligned-exam-null-floor-effect.md) — a narrower finding that bears on this claim
- [Falsifiable hypothesis: unrestricted AI use on deep-processing tasks will produce a product–process dissociation—higher-rated assignments but lower unaided delayed transfer](h3-product-process-dissociation-hypothesis.md) — a broader claim this one bears on
- [Most students reported no change in study habits, but students who adapted their study strategies rated GenAI-evaluation assignments as significantly more helpful](study-habit-adapters-rate-genai-grading-helpful.md) — related
- [Unrestricted ChatGPT access yields better practice performance but significantly worse exam scores](gpt4-access-harms-learning-after-withdrawal.md) — related
- [No significant group differences in knowledge gain or knowledge transfer despite ChatGPT's task-performance advantage](no-knowledge-gain-transfer-difference-genai.md) — related
