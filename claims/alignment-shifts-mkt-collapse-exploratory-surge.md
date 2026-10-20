---
type: claim
title: GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output
description: GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output
id: alignment-shifts-mkt-collapse-exploratory-surge
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: codebook-shift-1
    resource: "https://doi.org/10.48550/arxiv.2605.30666"
    title: codebook-shift-1
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Under GRPO alignment, the MKT sentence rate collapses from 18.1% to 6.5% (a 64% relative drop), Interaction nearly triples (4.4% to 12.3%), and PIU climbs from 20.0% to 28.7%. [→ codebook-shift-1](#codebook-shift-1)

## Evidence

### codebook-shift-1

Shim Jaechang and Unggi Lee. 2026. The Tutoring Effectiveness Index: Predicting LLM Math Tutor Quality from Four Conversation Signals. In Proceedings of The 35th ACM International Conference on Information and Knowledge Management (CIKM '26). https://arxiv.org/abs/2605.30666 [doi:10.48550/arxiv.2605.30666](https://doi.org/10.48550/arxiv.2605.30666)

`q2 · i?` · `causal · r1`

Codebook category distribution (Table 8, sentence-multilabel %, four-category view) over 119,009 tutor sentences labelled by GPT-4o-mini at temperature 0: "the aligned model’s MKT rate collapses from18.1%to6 .5%". TEI@4 selection on the base leaves all four category rates within 1.7pp of Greedy. No effect size printed.

> "the aligned model’s MKT rate collapses from18.1%to6 .5%(a64%relative drop) while its Inter- action rate nearly triples (4.4%to12 .3%) and its PIU rate climbs"

## Discussion


## Related Claims
- [GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)](grpo-pedagogical-alignment-tax-lowers-learning.md) — related
- [For material students have prior knowledge of (work-energy theorem), tutorial effectiveness depends significantly on teaching quality, with the ideal Socratic implementation best](instructor-quality-matters-with-prior-knowledge.md) — related
- [SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks](sped-adaptive-shifts-tutor-behavior-codebooks.md) — related
- [Reinforcement learning with a learned alignment reward substantially improves question-concept alignment after supervised fine-tuning, while answerability remains high throughout training](alignment-rl-improves-concept-alignment.md) — related
- [GRPO alignment without the directness reward raises Socratic scaffolding effectiveness from 0.300 to 0.633 and cuts keyword leakage from 26.7% to 13.3% on held-out questions](grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) — related
- [Iterative prompt refinement shifted a generative-AI tutor from tutorial-style explanation delivery toward dialogic Socratic support for K-12 beginners](prompt-refinement-shifts-genai-toward-socratic-support.md) — related
