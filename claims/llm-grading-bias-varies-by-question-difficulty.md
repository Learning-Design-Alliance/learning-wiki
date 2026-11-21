---
type: claim
title: "LLM grading bias relative to TAs varies with question difficulty: near-zero on trivial and easy questions, mildly stringent on medium, and more generous than TAs on hard questions"
description: "LLM grading bias relative to TAs varies with question difficulty: near-zero on trivial and easy questions, mildly stringent on medium, and more generous than TAs on hard questions"
id: llm-grading-bias-varies-by-question-difficulty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: pavlin-g-poliˇcar-2025
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: pavlin-g-poliˇcar-2025-2
    resource: "https://doi.org/10.1093/bioinformatics/btaf196"
    title: "Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)"
    author: Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM grading bias relative to TAs varies with question difficulty: near-zero on trivial and easy questions, mildly stringent on medium, and more generous than TAs on hard questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across difficulty categories, models showed low negative bias on medium-difficulty questions but were significantly more generous than TAs on difficult questions. [→ Pavlin G. Poliˇcar 2025](#pavlin-g-policar-2025)
`q2 i?` Llama-8B was a distinct exception on hard questions, over-grading about 45% and correctly grading only 50% of submissions. [→ Pavlin G. Poliˇcar 2025 (2)](#pavlin-g-policar-2025-2)

## Evidence

### Pavlin G. Poliˇcar 2025

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Analysis of average grading differences against TA grades across five difficulty categories from trivial to open-ended. Models showed 'low levels of negative bias' on medium questions, while on difficult questions 'most models are significantly more generous than TAs.'

> "For medium-difficulty questions, the models appear to show low levels of negative bias, while the opposite is true for difficult questions, where most models are significantly more generous than TAs."

### Pavlin G. Poliˇcar 2025 (2)

Pavlin G. Poliˇcar, Martin Špendl, Tomaž Curk, Blaž Zupan. (2025). Automated Assignment Grading with Large Language Models: Insights from a Bioinformatics Course. [doi:10.1093/bioinformatics/btaf196](https://doi.org/10.1093/bioinformatics/btaf196)

`q2 · i?` · `causal · r2`

Performance analysis of the smallest model on hard questions: Llama-8B 'over graded about 45% of submissions and under graded about 5% of submissions, correctly grading only 50% of submissions,' leading the authors to deem it unsuitable as a classroom grader.

> "for hard questions, Llama-8B over graded about 45% of submissions and under graded about 5% of submissions, correctly grading only 50% of submissions"

## Discussion


## Related Claims
- [In a real classroom, all six evaluated LLMs except Llama-8B graded student text answers with classification accuracy between 85% and 90% against TA gold-standard grades](llm-graders-match-ta-grading-accuracy.md) — related
- [LLMs systematically underestimate fraction items whose difficulty is driven by misconceptions (the \"Easy Trap\")](easy-trap-fraction-items-underestimated-by-llms.md) — related
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — related
