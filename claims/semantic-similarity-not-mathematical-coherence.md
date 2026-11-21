---
type: claim
title: Semantic similarity between predicted and true misconceptions does not guarantee mathematical coherence
description: Semantic similarity between predicted and true misconceptions does not guarantee mathematical coherence
id: semantic-similarity-not-mathematical-coherence
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: joshua-mitton-2026
    resource: "https://doi.org/10.1145/3774398.3811609"
    title: "Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)"
    author: Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Semantic similarity between predicted and true misconceptions does not guarantee mathematical coherence

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Predicted misconceptions can match the actual misconception stylistically while differing fundamentally in underlying mathematical reasoning, implying different pedagogical interventions. [→ Joshua Mitton 2026](#joshua-mitton-2026)

## Evidence

### Joshua Mitton 2026

Joshua Mitton, Prarthana Bhattacharyya, Digory Smith, Thomas Christie, Ralph Abboud, and Simon Woodhead. (2026). Misconception Diagnosis From Student-Tutor Dialogue: Generate, Retrieve, Rerank. arXiv preprint. [doi:10.1145/3774398.3811609](https://doi.org/10.1145/3774398.3811609)

`q2 · i?` · `design · r2`

Discussion §6.3 qualitative analysis (Tables 2 and 5) of Claude Sonnet 4.5 predictions that match stylistically but are mathematically incoherent, e.g. an estimation error predicted where the actual error concerns division by decimals. No effect size is printed.

> "A model can identify misconceptions that are stylistically similar, i.e., sharing vocabulary or mathematical domain, but they may fundamentally differ in their underlying mathematical reasoning."

## Discussion


## Related Claims
- [Behavioral similarity between LLMs and learners does not guarantee mechanistic similarity](llm-behavioral-similarity-not-mechanistic-similarity.md) — a broader claim this one bears on
- [Equal accuracy on fraction comparison items can mask fundamentally different misconceptions](fraction-accuracy-masks-distinct-misconceptions.md) — related
