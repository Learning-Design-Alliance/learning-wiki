---
type: claim
title: ChatGPT can perform worse when given more relevant evaluative information, suggesting a structural limitation in input integration
description: ChatGPT can perform worse when given more relevant evaluative information, suggesting a structural limitation in input integration
id: chatgpt-worse-with-more-information-structural-limitation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: mrityunjay-kumar-2025
    resource: "https://doi.org/10.48550/arXiv.2510.06997"
    title: "Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. [doi:10.48550/arXiv.2510.06997](https://doi.org/10.48550/arXiv.2510.06997)"
    author: Mrityunjay Kumar
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# ChatGPT can perform worse when given more relevant evaluative information, suggesting a structural limitation in input integration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Combining rubric and model solution (Prompt Type 4) did not outperform rubric alone, and the authors interpret this as a structural weakness in how the model processes evaluative tasks. [→ Mrityunjay Kumar 2025](#mrityunjay-kumar-2025)

## Evidence

### Mrityunjay Kumar 2025

Mrityunjay Kumar. (2025). The Limits of Goal-Setting Theory in LLM-Driven Assessment. arXiv. [doi:10.48550/arXiv.2510.06997](https://doi.org/10.48550/arXiv.2510.06997)

`q2 · i?` · `causal · r1`

Authors' interpretation of the controlled experiment results: "ChatGPT performs worse in some cases when given more information", which they attribute to the model treating each prompt in isolation and overfitting to surface cues rather than integrating multiple guidance sources.

> "ChatGPT performs worse in some cases when given more information, a counterintuitive and concerning outcome. This behaviour cannot be blamed on prompt wording or user error; it signals a structural weakness in how the model processes"

## Discussion


## Related Claims
- [Rubric-based GPT-4 prompting produced the strongest reflective assessment (80%), surpassing the top student submission (70%), though lacking personalization](chatgpt-reflective-assessment-strong-but-impersonal.md) — related
- [The advanced o1 Preview model did not consistently outperform GPT-4, underperforming V3 on descriptive tasks](o1-preview-no-consistent-advantage.md) — related
- [Despite generally accurate feedback, the LLM's scoring explanations could be unpredictable and prone to logical inconsistency, failing to award points even when citing the correct rubric directive](llm-logical-inconsistency-scoring-feedback.md) — related
