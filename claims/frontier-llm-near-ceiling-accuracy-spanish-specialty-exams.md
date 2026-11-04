---
type: claim
title: "Frontier LLMs achieve near-ceiling accuracy on all four 2026 Spanish specialty-access examinations, with the strongest configuration at 94.8% pooled accuracy"
description: "Frontier LLMs achieve near-ceiling accuracy on all four 2026 Spanish specialty-access examinations, with the strongest configuration at 94.8% pooled accuracy"
id: frontier-llm-near-ceiling-accuracy-spanish-specialty-exams
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
---

# Frontier LLMs achieve near-ceiling accuracy on all four 2026 Spanish specialty-access examinations, with the strongest configuration at 94.8% pooled accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` GPT-5.2 high (neutral) achieved 94.8% pooled accuracy (795/839) across MIR, EIR, PIR, and FIR examinations, with all 12 configurations answering 668 of 828 paired items correctly (80.7%). [→ Clemente García-Hidalgo 2026](#clemente-garcia-hidalgo-2026)

## Evidence

### Clemente García-Hidalgo 2026

Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199

`q3 · i?` · `associational · r2`

Cross-sectional benchmarking of 12 LLM configurations on 839 valid items from the January 2026 Spanish specialty-access examinations. The strongest configuration was GPT-5.2 high (neutral) at "94.8% (795/839, 95% CI 93.0%-96.1%)", with all configurations answering 668 of 828 paired items correctly (80.7%).

> "Pooling under full-coverage configurations (Table 2), the strongest configuration was GPT-5.2 high (neutral) at 94.8% (795/839, 95% CI 93.0%-96.1%)"

## Discussion


## Related Claims
- [Stated confidence discriminates correct from incorrect responses (GPT-5.2 AUROC approximately 0.87 to 0.90), though most configurations are net underconfident](llm-confidence-discriminates-correctness.md) — related
- [A surface-feature classifier recovers the keyed answer at 34.4%, almost entirely attributable to a longest-option heuristic rather than broad surface leakage](surface-feature-classifier-longest-option-artifact.md) — related
- [Human and machine item facility correlate moderately (Spearman ρ=0.40), lower than predicted by a uniform-advantage simulation (0.63)](human-machine-item-facility-correlation-moderate.md) — related
- [Image-associated items show lower model accuracy both when images are supplied (OR 0.33) and when withheld (OR 0.11)](image-items-lower-model-accuracy.md) — related
