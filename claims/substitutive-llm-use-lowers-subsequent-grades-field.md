---
type: claim
title: In the field study, substitutive LLM use (submitting ChatGPT-like solutions) significantly decreases grades on subsequent questions
description: In the field study, substitutive LLM use (submitting ChatGPT-like solutions) significantly decreases grades on subsequent questions
id: substitutive-llm-use-lowers-subsequent-grades-field
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: matthias-lehmann-2024
    resource: "https://doi.org/10.48550/arXiv.2409.09047"
    title: "Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)"
    author: Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In the field study, substitutive LLM use (submitting ChatGPT-like solutions) significantly decreases grades on subsequent questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under instrumental-variable fixed effects, cumulative ChatGPT similarity negatively and significantly predicts the grade on the current question. [→ Matthias Lehmann 2024](#matthias-lehmann-2024)

## Evidence

### Matthias Lehmann 2024

Matthias Lehmann, Philipp B. Cornelius, and Fabian J. Sting. (2024). AI Meets the Classroom: When Do Large Language Models Harm Learning? arXiv preprint. [doi:10.48550/arXiv.2409.09047](https://doi.org/10.48550/arXiv.2409.09047)

`q2 · i?` · `causal · r2`

Panel field study of two graduate Python courses (113 students, 6,594 observations) using ChatGPT outages as instruments for substitutive LLM use. In the FE2SLS second stage, cumulative ChatGPT similarity remains negative and significant (p = 0.002): "their grade on all subsequent questions decreases by 0.06".

> "If students submit code that is identical to a ChatGPT-generated solution, their grade for the current question does not change, but their grade on all subsequent questions decreases by 0.06."

## Discussion


## Related Claims
- [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 access in high-school mathematics raised assisted practice performance but left students worse off after withdrawal](gpt4-access-harms-learning-after-withdrawal.md) — related
