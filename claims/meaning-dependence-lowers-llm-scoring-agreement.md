---
type: claim
title: Meaning-dependent (reading) short-answer items reliably lower LLM agreement with human raters compared with more fact-based science items
description: Meaning-dependent (reading) short-answer items reliably lower LLM agreement with human raters compared with more fact-based science items
id: meaning-dependence-lowers-llm-scoring-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Meaning-dependent (reading) short-answer items reliably lower LLM agreement with human raters compared with more fact-based science items

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across meta-analytic specifications, items requiring semantic interpretation show a systematic negative effect on LLM-human QWK agreement (posterior mean ≈ -0.21 on Fisher-z scale). [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q2 · i?` · `quant-synthesis · r2`

Meta-regression of 890 QWK observations across a systematic review of LLM short-answer scoring studies, with multiway random effects. The read indicator is "negative across specifications, including the Bayesian model (posterior mean≈−0.21 on Fisher-z scale)". No standardized effect size beyond the Fisher-z coefficient is printed.

> "The read indicator is negative across specifications, including the Bayesian model (posterior mean≈−0.21 on Fisher-z scale). This implies that when an item requires integrating meaning rather than matching surface features, LLM-based scorers exhibit a systematic drop in agreement with humans."

## Discussion


## Related Claims
- [Human-perceived item difficulty (human-human QWK) does not reliably predict LLM scoring difficulty on the same items](human-difficulty-does-not-predict-llm-difficulty.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Course Context Raised an LLM Grader's Agreement on Terse Answers and Lowered It on Long Ones](course-context-helps-sparse-items-and-dilutes-rich-ones.md) — related
