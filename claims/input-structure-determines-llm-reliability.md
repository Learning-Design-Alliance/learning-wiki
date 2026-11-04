---
type: claim
title: LLM clinical reasoning performance is highly sensitive to input structure, with prompt structure a critical determinant of reliable behavior independent of model architecture
description: LLM clinical reasoning performance is highly sensitive to input structure, with prompt structure a critical determinant of reliable behavior independent of model architecture
id: input-structure-determines-llm-reliability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: vinson-2026
    resource: "https://doi.org/10.1038/s41598-026-48326-4"
    title: "Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4"
    author: "Vinson, J., Caronia, C., & Savargaonkar, R."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LLM clinical reasoning performance is highly sensitive to input structure, with prompt structure a critical determinant of reliable behavior independent of model architecture

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` LLM clinical reasoning performance is highly sensitive to input structure; prompt structure rather than model selection alone is a critical determinant of reliable LLM behavior. [→ Vinson 2026](#vinson-2026)

## Evidence

### Vinson 2026

Vinson, J., Caronia, C., & Savargaonkar, R. (2026). Input structure–driven instability and convergence in large language model clinical reasoning: a formative study using pediatric residency–level MCQs. Scientific Reports. https://doi.org/10.1038/s41598-026-48326-4

`q2 · i?` · `causal · r1`

Cross-sectional comparative study manipulating delivery format while holding question content constant across six LLMs on 77 validated pediatric MCQs. The article reports that "LLM clinical reasoning performance is highly sensitive to input structure" and that structured batch delivery improved reproducibility independent of model architecture.

> "LLM clinical reasoning performance is highly sensitive to input structure. Reducing contextual load through structured batch delivery improves reproducibility and minimizes inter-model variability, independent of model architecture."

## Discussion


## Related Claims
- [Batch delivery of ten questions converges LLM accuracy to 83%–88% with no statistically significant inter-model differences](batch-delivery-convergence-83-88.md) — a narrower finding that bears on this claim
- [Sequential delivery in batches of ten substantially reduces performance dispersion and instability across evaluated LLMs compared with simultaneous delivery](batch-delivery-reduces-instability.md) — a narrower finding that bears on this claim
- [There is no universal optimal injection position for the collaborative prior; effectiveness is an architecture-sensitive design choice](injection-strategy-architecture-sensitive.md) — related
- [Phase VI AI-enabled systems face six documented challenges: explainability, hallucination risk, prompt sensitivity, computational cost, validation complexity, and limited large-scale evidence](phase-vi-ai-systems-six-challenges.md) — related
- [LoRA fine-tuning hyperparameters are not model-agnostic: increasing rank above 64 destroyed LLaMA's feedback generation while Gemma remained robust](lora-rank-sensitivity-architecture-dependent.md) — related
