---
type: claim
title: "A surface-feature classifier recovers the keyed answer at 34.4%, almost entirely attributable to a longest-option heuristic rather than broad surface leakage"
description: "A surface-feature classifier recovers the keyed answer at 34.4%, almost entirely attributable to a longest-option heuristic rather than broad surface leakage"
id: surface-feature-classifier-longest-option-artifact
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: clemente-garcía-hidalgo-2026
    resource: "https://doi.org/10.2196/106199"
    title: "Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199"
    author: Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: clemente-garcía-hidalgo-2026-2
    resource: "https://doi.org/10.2196/106199"
    title: "Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199"
    author: Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A surface-feature classifier recovers the keyed answer at 34.4%, almost entirely attributable to a longest-option heuristic rather than broad surface leakage

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` A leave-one-examination-out cross-validated surface-feature classifier recovered the keyed answer at 34.4% (289/839), while a longest-option heuristic alone recovered it at 34.6% (290/839), indicating the signal is a length-dominated item-writing artifact. [→ Clemente García-Hidalgo 2026](#clemente-garcia-hidalgo-2026)

## Evidence

### Clemente García-Hidalgo 2026

Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199

`q3 · i?` · `associational · r2`

Surface-feature prediction analysis using an L2-regularized logistic classifier with 11 features, cross-validated leave-one-examination-out on 839 items. "recovered the keyed answer at 34.4% (289/839, 95% CI 31.3-37.7) against a 25% chance baseline".

> "A surface-feature classifier with no medical knowledge, cross-validated leave-one-examination-out, recovered the keyed answer at 34.4% (289/839, 95% CI 31.3-37.7) against a 25% chance baseline"

### Clemente García-Hidalgo 2026 (2)

Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199

`q3 · i?` · `associational · r2`

Comparison of the classifier against a simple longest-option rule on the same 839 items. "a longest-option heuristic applied alone, with no classifier at all, recovers the key at 34.6% (290/839), matching or exceeding the classifier", indicating the signal is item-format-intrinsic.

> "a longest-option heuristic applied alone, with no classifier at all, recovers the key at 34.6% (290/839), matching or exceeding the classifier"

## Discussion


## Related Claims
- [Frontier LLMs achieve near-ceiling accuracy on all four 2026 Spanish specialty-access examinations, with the strongest configuration at 94.8% pooled accuracy](frontier-llm-near-ceiling-accuracy-spanish-specialty-exams.md) — related
- [The simulated-respondent approach recovers the guessing parameter c at correlation 0.48, far above regression baselines, suggesting it captures genuine response behavior](simulated-respondents-recover-guessing-parameter-048.md) — related
