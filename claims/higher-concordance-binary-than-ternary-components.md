---
type: claim
title: Concordance between LLM and human ratings is generally, not uniformly, higher for binary rubric components than for ternary components
description: Concordance between LLM and human ratings is generally, not uniformly, higher for binary rubric components than for ternary components
id: higher-concordance-binary-than-ternary-components
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-05
recheck_by: 2029
sources:
  - id: stadler-p-2026
    resource: "https://doi.org/10.2196/94666"
    title: "Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666"
    author: Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Concordance between LLM and human ratings is generally, not uniformly, higher for binary rubric components than for ternary components

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-05 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Concordance was generally higher for the binary rubric components (person and factual accuracy) than for the ternary components, with exceptions for particular model and prompting configurations. [→ Stadler P 2026](#stadler-p-2026)

## Evidence

### Stadler P 2026

Stadler P, Bucichowski P, Holzhausen Y, Hege I, Peters H, Kaminski J. (2026). Test-Retest Reliability of Large Language Models and Their Concordance With Human Experts in Rubric-Based Scoring of Clinical Summary Statements: Experimental Comparative Study. JMIR Medical Education. https://doi.org/10.2196/94666

`q2 · i?` · `causal · r2`

Four LLMs were each run under 4 prompting strategies (16 model × prompting conditions) to rate 122 summary statements. Agreement with the expert ratings (Gwet AC1 for binary components, AC2 for ternary ones) was generally higher for the binary components (person, factual accuracy) than for the ternary ones (semantic qualifiers, transformation, narrowing, global); the results section says the binary components "usually showed the highest agreement". The pattern is not uniform: Mistral 7B under zero-shot prompting reached AC2=0.876 on semantic qualifiers while its person rating collapsed to near chance (AC1=0.037), and Mistral Large scored only AC1=0.530 on factual accuracy under few-shot prompting. The authors note the difference may partly reflect the distribution of ratings in the human reference set.

> "Concordance was higher for the binary rubric components (person and factual accuracy) than for the ternary components."

## Discussion


## Related Claims
- [Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs](few-shot-cot-best-concordance-human-experts.md) — related
- [Extreme deviations and invalid outputs from LLM raters are rare but more frequent in ternary components and the smaller local model](rare-extreme-deviations-invalid-outputs.md) — a narrower finding that bears on this claim
- [Model choice, prompting configuration, and rubric component all significantly affect LLM-human agreement, with significant interactions](mixed-effects-model-significant-main-and-interaction-effects.md) — a broader claim this one bears on
