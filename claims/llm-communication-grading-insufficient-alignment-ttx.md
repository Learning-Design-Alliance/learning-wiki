---
type: claim
title: "GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)"
description: "GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)"
id: llm-communication-grading-insufficient-alignment-ttx
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: v-švábenský-2026
    resource: "https://arxiv.org/abs/2607.19209"
    title: "V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209"
    author: V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-4o's disagreement with human-assigned communication grades was 55%, essentially matching chance, and although GPT-5.2 reduced error to 35%, the LLM assessments were not sufficiently aligned with instructor judgment in the cyber TTX context. [→ V. Švábenský 2026](#v-svabensky-2026)

## Evidence

### V. Švábenský 2026

V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209

`q2 · i?` · `design · r2`

Evaluation (RQ1) of LLM grading of teams' incident-response emails against instructor communication scores on a 0-2 rubric scale for 23 teams; instructor-instructor RMSE was 0.32 (16%), GPT-4o averaged 1.10 (55%), and GPT-5.2 averaged 0.71 (35%) across the two TTXs.

> "However, since the GPT-4o's disagreement with the human-assigned grades was 55%, the output essentially matched chance. Even though the LLM was guided by a clear prompt based on the standardized rubric criteria [55], it often yielded surprising results"

## Discussion


## Related Claims
- [Clustering of TTX activity logs aligns with instructor-assigned milestone scores and outperforms the random-grouping baseline in both exercises](clustering-ttx-team-assessment-aligns-instructor-scores.md) — related
- [Expert former math teachers rated GPT-4o's dialogue annotations very highly for student correctness and moderate-to-high for knowledge components, with volatile inter-rater reliability.](expert-teachers-rate-gpt-4o-dialogue-annotations-as-largely-accurate.md) — related
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](turn-level-convergence-gpt-4o-mini.md) — related
- [A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only](llm-emotional-tone-bias-incident-words.md) — related
- [Structured developmental annotation (CLARA) achieves stronger alignment with developmental references than readability-based and direct prompting baselines](clara-outperforms-readability-and-prompting-baselines.md) — related
