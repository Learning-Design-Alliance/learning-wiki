---
type: claim
title: Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation
description: Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation
id: engagement-contract-ablation-reduces-pck-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: md-zabirul-islam-2026
    resource: "https://arxiv.org/abs/2606.20608"
    title: "Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608"
    author: Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Removing the engagement contract reduces judged engagement, adaptive scores, readability, and engagement-move counts in pedagogical video generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Disabling the engagement module reduces the LLM-judge engagement score from 5.00 to 1.20, the adaptive score from 4.80 to 3.40, and Flesch reading ease from 38.0 to 19.8, while analogy and retrieval-prompt counts fall to near zero. [→ Md Zabirul Islam 2026](#md-zabirul-islam-2026)

## Evidence

### Md Zabirul Islam 2026

Md Zabirul Islam, Md Motaleb Hossen Manik, and Ge Wang. (2026). CourseBlueprint: A Structured Pipeline for Adaptive Pedagogical Video Generation Grounded in Course Corpora. arXiv preprint. https://arxiv.org/abs/2606.20608

`q2 · i?` · `causal · r1`

Five-topic ablation (n=5 topics, one run each) comparing the full pipeline to a No-Engagement variant with scaffold and adaptive style held fixed; LLM-judge medians of three reps plus regex objective metrics. The article reports engagement falling "from 5.00 to 1.20" and analogies falling from 20.0 to 0.2 per video; no effect size is printed.

> "Disabling the engagement module reduces the engagement score from 5.00 to 1.20. The objective metrics show the same pattern: analogies fall from 20.0 to 0.2 per video, and retrieval prompts fall from 18.6 to 0.0 per video"

## Discussion


## Related Claims
- [Engagement removal lowers the adaptive score, indicating the engagement generator realizes persona-conditioned style choices in narration](engagement-realizes-adaptive-style-in-narration.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
