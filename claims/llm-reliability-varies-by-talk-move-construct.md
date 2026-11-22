---
type: claim
title: "LLM reliability on instructional moves varies by construct: stronger on explicit, structurally constrained moves and weaker on socially and metacognitively demanding ones"
description: "LLM reliability on instructional moves varies by construct: stronger on explicit, structurally constrained moves and weaker on socially and metacognitively demanding ones"
id: llm-reliability-varies-by-talk-move-construct
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kirk-vanacore-and-rené-f-kizilcec-2026
    resource: "https://doi.org/10.1145/3774398.3811605"
    title: "Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)"
    author: Kirk Vanacore and René F. Kizilcec
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM reliability on instructional moves varies by construct: stronger on explicit, structurally constrained moves and weaker on socially and metacognitively demanding ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Models reached moderate to substantial per-code reliability on Getting Students to Relate to Another's Ideas, Restating, and Pressing for Accuracy, but poor or fair reliability on Keeping Everyone Together, Revoicing, and Pressing for Reasoning. [→ Kirk Vanacore and René F. Kizilcec 2026](#kirk-vanacore-and-rene-f-kizilcec-2026)

## Evidence

### Kirk Vanacore and René F. Kizilcec 2026

Kirk Vanacore and René F. Kizilcec. (2026). How well do Large Language Models Recognize Instructional Moves? Establishing Baselines for Foundation Models in Educational Discourse. Originally published 2025. [doi:10.1145/3774398.3811605](https://doi.org/10.1145/3774398.3811605)

`q2 · i?` · `causal · r2`

Construct-specific analysis of the benchmark experiment, shown per-code in Fig. 1 and Appendix A tables. The article reports this per-code κ contrast across the six Talk Moves; no standardized effect size is printed.

> "Models reached moderate to substantial reliability onGetting Students to Relate to Another’s Ideas,Restating, andPressing for Accuracy, whereas reli- ability mostly remained poor or fair forKeeping Everyone Together,Revoic- ing, andPressing for Reasoning."

## Discussion


## Related Claims
- [Construct-specific verification models outperform a generalist model on difficult instructional constructs, recovering signal for Getting Students to Relate (F1 0.46 vs. generalist 0.15)](construct-specific-verifiers-improve-detection.md) — related
- [Systems Thinking Practices is the hardest CT construct to code reliably for both human raters and the LLM, requiring more explicitly operationalized rubrics](stp-low-reliability-complex-construct.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [A multimodal LLM achieves moderate-to-substantial agreement with human consensus on well-defined CT practices but lower agreement on multi-component constructs like Physics Correctness and Systems Thinking](llm-human-agreement-ct-practices.md) — related
- [Models struggle more in pedagogically demanding low-proficiency and low-resource contexts, with smaller models varying more across contexts](l2-bench-context-performance-low-resource.md) — related
