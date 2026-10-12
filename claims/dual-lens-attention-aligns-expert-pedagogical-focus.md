---
type: claim
title: "Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps"
description: "Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps"
id: dual-lens-attention-aligns-expert-pedagogical-focus
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: li-2025
    resource: "https://doi.org/10.3390/info16100882"
    title: "Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882"
    author: Li, Y.; Yang, H.; Fang, Q.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Dual-Lens attention aligns with expert pedagogical focus, allocating most weight to Bloom's taxonomy verbs and problem-solving steps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Attention weight analysis shows strong alignment with pedagogical elements, allocating 73% of weights to Bloom's taxonomy verbs and problem-solving steps in mathematics cases, though one failure case placed 28% weight on emotional cues. [→ Li 2025](#li-2025)

## Evidence

### Li 2025

Li, Y.; Yang, H.; Fang, Q. (2025). Towards Trustworthy and Explainable-by-Design Large Language Models for Automated Teacher Assessment. Information 2025, 16, 882. https://doi.org/10.3390/info16100882

`q2 · i?` · `design · r2`

Interpretability analysis (§5.7, Table 12) of attention weight distributions by pedagogical component; Bloom's verbs receive "73% of weights" against an expert benchmark of 75.4%, while emotional cues receive 28.4% versus an expert benchmark of 15.2%.

> "Attention weight analysis reveals strong alignment with pedagogical elements, allocating 73% of weights to Bloom's taxonomy verbs and problem-solving steps in mathematics instruction cases."

## Discussion


## Related Claims
- [The selected-questions-verbs prompting strategy yields the strongest LLM Bloom classification, reaching weighted F1 up to 0.84](selected-questions-verbs-best-prompt.md) — related
- [In-context examples improve LLM Bloom classification: three-shot and ten-shot prompting outperform zero-shot across datasets](in-context-examples-improve-bloom-classification.md) — related
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
