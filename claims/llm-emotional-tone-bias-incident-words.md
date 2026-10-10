---
type: claim
title: "A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only"
description: "A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only"
id: llm-emotional-tone-bias-incident-words
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
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

# A general-purpose LLM assessing team emails' emotional tone was biased toward interpreting messages as anxiety-related only

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When experimenting with categorizing teams' email emotional tone, the general LLM almost always interpreted messages as exhibiting only anxiety-related emotions, likely due to the prevalence of incident words in the dataset. [→ V. Švábenský 2026](#v-svabensky-2026)

## Evidence

### V. Švábenský 2026

V. Švábenský, J. Vykopal, S. Leelaluk, P. Čeleda, F. Okubo, A. Shimada. (2026). Assessment in Team Problem-Solving Exercises in Computing Education. Proceedings of the 56th IEEE Frontiers in Education Conference (FIE '26). https://arxiv.org/abs/2607.19209

`q2 · i?` · `design · r2`

Exploratory experiment (RQ2) in which the authors asked the LLM to categorize the emotional tone of teams' TTX emails; the authors attribute the bias to incident vocabulary and conclude valid results require framing assessment within the TTX context or a domain-specific model such as CyLLM.

> "However, the general LLM was biased to almost always interpret messages as exhibiting only anxiety-related emotions. Most likely, this stemmed from the prevalence of incident words (e.g., "cyber attack" or "data loss") in the dataset."

## Discussion


## Related Claims
- [GPT-4o's rubric-guided grading of team communication disagreed with instructors at near-chance levels (55% RMSE), while GPT-5.2 improved but remained insufficiently aligned (35%)](llm-communication-grading-insufficient-alignment-ttx.md) — related
- [Perceptions of feedback characteristics vary between researcher and teacher coders, with agreement shaped by professional background](coder-background-varies-feedback-interpretation.md) — related
- [Fully inductive LLM codebook development risks importing unexamined sensitizing concepts, such as folk theories and scientific misconceptions, from the model's training data](llm-inductive-coding-sensitizing-concept-risk.md) — a broader claim this one bears on
- [Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions](llm-selection-bias-against-option-d.md) — related
