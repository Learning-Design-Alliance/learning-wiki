---
type: claim
title: "An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses"
description: "An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses"
id: llm-judge-audit-failure-modes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-03
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: clemente-garcía-hidalgo-2026
    resource: "https://doi.org/10.2196/106199"
    title: "Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199"
    author: Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# An exploratory LLM-judge audit labels knowledge gaps (39.1%) and reasoning errors (26.9%) as the most frequent failure modes among incorrect frontier-model responses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among 253 incorrect frontier-model responses, the Opus judge labeled 99 (39.1%) as knowledge gaps, 68 (26.9%) as reasoning errors, and 36 (14.2%) as fine-distractor errors. [→ Clemente García-Hidalgo 2026](#clemente-garcia-hidalgo-2026)

## Evidence

### Clemente García-Hidalgo 2026

Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199

`q2 · i?` · `associational · r2`

Exploratory LLM-judge audit applying a human-authored rubric to 253 incorrect frontier-model responses with usable explanations. "The Opus judge labeled 99 as knowledge gaps (n=_, 39.1%, bootstrap 95% CI 34-45), 68 as reasoning errors (n=_, 26.9%)".

> "The Opus judge labeled 99 as knowledge gaps (n=_, 39.1%, bootstrap 95% CI 34-45), 68 as reasoning errors (n=_, 26.9%), 36 as fine-distractor errors (n=_, 14.2%)"

## Discussion


## Related Claims
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [Validator false-negative cases reveal structural reasoning weaknesses, including answer-schema misinterpretation and internal inconsistency](code-gen-validator-fn-reasoning-weaknesses.md) — related
