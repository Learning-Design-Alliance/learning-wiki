---
type: claim
title: Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs
description: Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs
id: minor-position-bias-and-partial-guessing-in-small-llms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: markos-stamatakis-2026
    resource: "https://doi.org/10.48550/arxiv.2606.15919"
    title: "Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)"
    author: Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Smaller local LLMs show a minor position bias toward option ordering and partially guessing-like error variation, but accuracy remains relatively stable across permutations and repeated sampling runs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rotating MCQ option positions slightly affects Mistral-7B and DeepSeek-R1 scores, and repeated sampling runs show slight score variation, with accuracy and fully-correct answers remaining relatively stable. [→ Markos Stamatakis 2026](#markos-stamatakis-2026)

## Evidence

### Markos Stamatakis 2026

Markos Stamatakis, Omkar Gavali, Joshua Berger, Christian Wartena, Anett Hoppe, and Ralph Ewerth. (2026). Are LLM-based Chatbots Good Enough to Support Computer Science Students in Multiple-Choice Exercises? https://arxiv.org/abs/2606.15919 [doi:10.48550/arxiv.2606.15919](https://doi.org/10.48550/arxiv.2606.15919)

`q2 · i?` · `causal · r2`

Stability evaluation (Table 3, Sec. 4): four cyclic option permutations per question and 10 repeated runs with default sampling for the two local models. The article reports a "minor position bias for both models" and error-similarity variation hinting at partial guessing; descriptive percentages only.

> "varying the order of the options slightly affects the score, indicating a minor position bias for both models."

## Discussion


## Related Claims
- [GPT-4o and GPT-5.2 achieve higher accuracy and more fully correct answers on university IVDA multiple-choice questions than the smaller Mistral-7B and DeepSeek-R1 models](gpt-models-outperform-smaller-llms-on-ivda-mcqs.md) — related
- [LLM difficulty predictions for fraction items are less stable across repeated runs than for the overall item set](llm-fraction-predictions-run-to-run-instability.md) — related
- [Some LLMs exhibit a selection bias against selecting option D on multiple-choice pedagogy questions](llm-selection-bias-against-option-d.md) — related
- [The benchmark procedure is stable under stochastic decoding, with a maximum accuracy standard deviation of 0.43% over 20 repeated runs](cdpk-benchmark-stability-0-43-percent-sd.md) — related
- [Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%](its-dialogue-models-brittleness-perturbations.md) — related
- [Cumulative meta-analysis shows reported GenAI productivity effects remained stable over time (stabilizing at g = 0.331) despite rapid advancement of underlying foundation models.](cumulative-productivity-effects-stable-over-time.md) — related
- [Model and prompt choice account for only a small share of misalignment error, which concentrates in transcript-conditioned higher-order interactions](variance-decomposition-model-prompt-weak-levers.md) — related
- [Model and student error patterns on IVDA MCQs show limited question-level consistency but comparable difficulty distributions for easiest and hardest questions](limited-model-student-question-level-alignment.md) — related
