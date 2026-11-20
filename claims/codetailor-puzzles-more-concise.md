---
type: claim
title: "CodeTailor's personalized Parsons puzzles contain significantly fewer movable blocks than fully movable puzzles built from the same solution"
description: "CodeTailor's personalized Parsons puzzles contain significantly fewer movable blocks than fully movable puzzles built from the same solution"
id: codetailor-puzzles-more-concise
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: xinying-hou-2024
    title: Xinying Hou 2024
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# CodeTailor's personalized Parsons puzzles contain significantly fewer movable blocks than fully movable puzzles built from the same solution

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Even after adding distractor blocks, CodeTailor puzzles had significantly fewer movable blocks than fully movable puzzles. [→ Xinying Hou 2024](#xinying-hou-2024)

## Evidence

### Xinying Hou 2024

Xinying Hou, Zihan Wu, Xu Wang, and Barbara J. Ericson. 2024. CodeTailor: LLM-Powered Personalized Parsons Puzzles for Engaging Support While Learning Programming. In Proceedings of the Eleventh ACM Conference on Learning @ Scale (L@S '24). https://doi.org/10.1145/3657604.3662032

`q2 · i?` · `causal · r1`

Technical evaluation comparing block counts for the two puzzle types generated from the same Stage 1 solutions across the 500 incorrect code inputs, using a Wilcoxon signed-rank test: "W = 13587.0, p < .001, CLES = 0.33".

> "even after adding distractor blocks, the CodeTailor Parsons puzzles, M (SD) = 6.3 (2.6), Median = 6.0, had significantly fewer movable blocks compared to the fully movable Parsons puzzles, M (SD) = 8.1 (3.0), Median = 8.0, W = 13587.0, p < .001, CLES = 0.33, across student incorrect code inputs."

## Discussion


## Related Claims
- [Novice programmers perceive CodeTailor's personalized Parsons puzzles as more engaging support than receiving a direct LLM-generated code solution](codetailor-more-engaging-than-ai-solution.md) — related
- [CodeTailor generates correct solutions closer to a student's incorrect code than a most common student solution](codetailor-solution-closeness-technical-eval.md) — related
- [Students applied more scaffolded practice elements independently on the posttest after using CodeTailor than after receiving an AI-generated solution](codetailor-higher-scaffolding-apply-rate.md) — related
- [Posttest programming scores did not differ significantly between CodeTailor support and receiving an AI-generated solution](codetailor-posttest-performance-null.md) — related
- [Most novice programmers (88%) preferred CodeTailor over receiving a direct AI-generated solution for learning](codetailor-preference-88-percent.md) — related
- [Five-option MCQs contain substantially more non-functioning distractors than three-option MCQs](five-option-mcq-more-non-functioning-distractors.md) — related
- [Two-distractor MCQs contain fewer item-writing flaws and more frequently have all distractors functional compared with three-distractor MCQs](two-distractor-items-fewer-flaws-more-functional.md) — related
