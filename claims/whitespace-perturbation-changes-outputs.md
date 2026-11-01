---
type: claim
title: Adding 0-2 leading or trailing spaces to a prompt generates very different LLM documents even with prompt settings unchanged
description: Adding 0-2 leading or trailing spaces to a prompt generates very different LLM documents even with prompt settings unchanged
id: whitespace-perturbation-changes-outputs
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 1
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Adding 0-2 leading or trailing spaces to a prompt generates very different LLM documents even with prompt settings unchanged

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` An appendix experiment demonstrates that adding only 0-2 leading or trailing spaces to the prompt produces very different generated documents, with no change in meaning. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q1 · i?` · `quant-synthesis · r2`

Illustrative experiment in Appendix A showing tokenization/formatting sensitivity beyond autoscoring. The article states "very different documents are generated from only adding 0-2 leading or trailing spaces in the prompt, even with prompt settings unchanged". Single demonstration; no statistical test reported.

> "we include another, experiment in Appendix A, where we demonstrate how very different documents are generated from only adding 0-2 leading or trailing spaces in the prompt, even with prompt settings unchanged."

## Discussion


## Related Claims
- [Systematic prompting of an LLM can generate cognitively activating formative feedback aligned with research-based scaffold types (demonstrated, not yet empirically validated)](leap-prompt-design-generates-cognitively-activating-feedback.md) — related
