---
type: claim
title: Stated confidence discriminates correct from incorrect responses (GPT-5.2 AUROC approximately 0.87 to 0.90), though most configurations are net underconfident
description: Stated confidence discriminates correct from incorrect responses (GPT-5.2 AUROC approximately 0.87 to 0.90), though most configurations are net underconfident
id: llm-confidence-discriminates-correctness
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

# Stated confidence discriminates correct from incorrect responses (GPT-5.2 AUROC approximately 0.87 to 0.90), though most configurations are net underconfident

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Stated confidence distinguished correct from incorrect responses within the panel (GPT-5.2 AUROC approximately 0.87 to 0.90), with 10 of 12 configurations net underconfident and ECE ranging from 0.030 to 0.075. [→ Clemente García-Hidalgo 2026](#clemente-garcia-hidalgo-2026)

## Evidence

### Clemente García-Hidalgo 2026

Clemente García-Hidalgo, Manuel Carpio-Salmerón, Pau Benito, Carlos Carazo-Casas, Beatriz Carratalá, Jaime Campos Pavón. (2026). Construct Validity of Frontier Large Language Models on 4 Spanish Health Professions Specialty-Access Examinations (MIR, EIR, PIR, and FIR): Cross-Sectional Benchmarking and Psychometric Study. JMIR Medical Education. https://doi.org/10.2196/106199

`q3 · i?` · `associational · r2`

Calibration analysis of stated certainty (1-100) across the 12-configuration panel. "Stated confidence distinguished correct from incorrect responses within the panel (GPT-5.2 AUROC approximately 0.87 to 0.90)", with 10 of 12 configurations net underconfident.

> "Stated confidence distinguished correct from incorrect responses within the panel (GPT-5.2 AUROC approximately 0.87 to 0.90). The highest AUROC was 0.90 for GPT-5.2 high with the expert prompt, with a 27.6-point difference in mean confidence between correct and incorrect answers"

## Discussion


## Learner Variables
- [Metacognition](../learner-variables/metacognition.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Frontier LLMs achieve near-ceiling accuracy on all four 2026 Spanish specialty-access examinations, with the strongest configuration at 94.8% pooled accuracy](frontier-llm-near-ceiling-accuracy-spanish-specialty-exams.md) — related
- [Latent (token-probability) confidence is the weakest single-source confidence signal for LLM-based ASAG, with the lowest AUROC and worst calibration](latent-confidence-weakest-asag.md) — related
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](hybrid-aleatoric-best-calibration-asag.md) — related
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](hybrid-confidence-highest-auroc-selective-asag.md) — related
- [The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct](peer-grading-confidence-estimates-conservative.md) — related
- [Rejecting the 40% lowest-confidence predictions with the hybrid confidence measure raises grading accuracy from 0.704 to approximately 0.900](rejection-04-accuracy-gain-hybrid-confidence.md) — related
