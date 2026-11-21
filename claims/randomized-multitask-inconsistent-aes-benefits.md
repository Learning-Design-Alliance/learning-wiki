---
type: claim
title: Randomized multi-task fine-tuning shows inconsistent benefits, achieving the best Position F1 but performing poorly on Lead
description: Randomized multi-task fine-tuning shows inconsistent benefits, achieving the best Position F1 but performing poorly on Lead
id: randomized-multitask-inconsistent-aes-benefits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ali-keramati-and-mark-warschauer-2026
    resource: "https://doi.org/10.48550/arXiv.2606.10327"
    title: "Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)"
    author: Ali Keramati and Mark Warschauer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Randomized multi-task fine-tuning shows inconsistent benefits, achieving the best Position F1 but performing poorly on Lead

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Randomized (multi-task) model unexpectedly achieves the best F1-score on Position (57%) but performs exceptionally poorly on Lead (7% F1). [→ Ali Keramati and Mark Warschauer 2026](#ali-keramati-and-mark-warschauer-2026)

## Evidence

### Ali Keramati and Mark Warschauer 2026

Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)

`q2 · i?` · `causal · r1`

Results for the Randomized multi-task fine-tuning condition in the PERSUADE 2.0 experiments (Section 5.2, finding 4). The shuffled multi-task model achieved the best Position F1 at 57% but only 7% F1 on Lead, which the authors describe as inconsistent.

> "It unexpectedly achieves the best F1-score onPosition(57%) but performs exceptionally poorly onLead(7% F1). This inconsistency suggests that while jointly learning shared features is beneficial, it is less robust than a structured curriculum."

## Discussion


## Related Claims
- [Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion](sequential-curriculum-strongest-aes-performance.md) — related
- [Frontier LLMs achieve the best balance between detecting misconceptions in correct-answer cases and not over-flagging correct students, while fine-tuned local models achieve under 58% TM recall](frontier-llms-best-balance-tm-detection.md) — related
