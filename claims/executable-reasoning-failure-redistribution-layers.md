---
type: claim
title: Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations
description: Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations
id: executable-reasoning-failure-redistribution-layers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sagnik-nath-2026
    resource: "https://doi.org/10.1007/978-3-032-30860-3_11"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: sagnik-nath-2026-2
    resource: "https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    title: "Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv"
    author: Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Code-augmented interaction redistributes failures into protocol, execution, and mathematical layers, with Gemini 2.5 Pro failing mostly through protocol violations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Under the code-augmented condition, failures separate into protocol violations, execution failures, and mathematically incorrect computations, and models differ markedly in where they fail. [→ Sagnik Nath 2026](#sagnik-nath-2026)
`q2 i?` Gemini 2.5 Pro exhibits a failure profile dominated by protocol violations rather than execution or mathematical failures under executable reasoning. [→ Sagnik Nath 2026 (2)](#sagnik-nath-2026-2)

## Evidence

### Sagnik Nath 2026

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv [doi:10.1007/978-3-032-30860-3_11](https://doi.org/10.1007/978-3-032-30860-3_11)

`q2 · i?` · `causal · r2`

Model-level failure disaggregation for the code-augmented condition (Fig. 5). The article reports "Models differ markedly in where they fail", with distinctions invisible in baseline evaluation becoming explicit when reasoning is externalized as code.

> "Models differ markedly in where they fail. Some frequently violate protocol con- straints, others generate executable code that fails at runtime, and others execute suc- cessfully but compute incorrect results."

### Sagnik Nath 2026 (2)

Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv

`q2 · i?` · `causal · r2`

Code-augmented failure analysis (Fig. 5): the article reports Gemini 2.5 Pro's majority of errors arise from protocol violations, and that the model "often produces correct or near -correct reasoning content" that "fails to comply with the strict output contract".

> "This suggests that the model often produces correct or near -correct reasoning content that nonetheless fails to comply with the strict output contract required for executable interaction."

## Discussion


## Related Claims

- [Code-augmented interaction consistently increases median and tail latency, and costs per correct answer typically increase, with Gemini 2.5 Pro a notable outlier](code-augmented-latency-cost-increases.md) — related
- [LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions](llm-representational-sensitivity-equivalent-math-forms.md) — related
- [In the MM-04 workflow case, similar-looking model activity has different evidential validity: GPT-5.5 closes the evidence-to-action loop while GLM-5.1 leaves the assigned deck unchanged and Gemini-3.1-Pro misses required numeric or visual evidence](mm04-workflow-boundary-failures.md) — related
- [Representation gaps are nontrivial for all models, and code-based interaction can amplify representational specialization rather than stabilizing performance](representation-gaps-model-specific-code-amplification.md) — related
- [The memory layer recorded 889 failure, verification, correction, or protocol-proxy events (9.26 per active day), making governance part of the operating environment](governance-889-events-ger-9-26.md)
