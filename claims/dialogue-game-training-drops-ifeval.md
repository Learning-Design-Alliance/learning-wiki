---
type: claim
title: Post-training on dialogue games causes a substantial drop in instruction-following ability as measured by IFEval
description: Post-training on dialogue games causes a substantial drop in instruction-following ability as measured by IFEval
id: dialogue-game-training-drops-ifeval
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: horst-2025
    resource: "https://doi.org/10.18653/v1/2025.emnlp-main.1517"
    title: "Horst, N., Mazzaccara, D., Schmidt, A., Sullivan, M., Momentè, F., Franceschetti, L., Sadler, P., Hakimov, S., Testoni, A., Bernardi, R., Fernández, R., Koller, A., Lemon, O., Schlangen, D., Giulianelli, M., & Suglia, A. (2025). PLAYPEN: An Environment for Exploring Learning From Dialogue Game Feedback. arXiv. [doi:10.18653/v1/2025.emnlp-main.1517](https://doi.org/10.18653/v1/2025.emnlp-main.1517)"
    author: "Horst, N., Mazzaccara, D., Schmidt, A., Sullivan, M., Momentè, F., Franceschetti, L., Sadler, P., Hakimov, S., Testoni, A., Bernardi, R., Fernández, R., Koller, A., Lemon, O., Schlangen, D., Giulianelli, M., & Suglia, A."
    q: 2
    i: "?"
    kind: design
    rigour: "?"
---

# Post-training on dialogue games causes a substantial drop in instruction-following ability as measured by IFEval

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r?` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training on dialogue games produces a substantial drop in the ability to follow instructions as measured by IFEval, calling for instruction-following regimes more robust to interactive settings. [→ Horst 2025](#horst-2025)

## Evidence

### Horst 2025

Horst, N., Mazzaccara, D., Schmidt, A., Sullivan, M., Momentè, F., Franceschetti, L., Sadler, P., Hakimov, S., Testoni, A., Bernardi, R., Fernández, R., Koller, A., Lemon, O., Schlangen, D., Giulianelli, M., & Suglia, A. (2025). PLAYPEN: An Environment for Exploring Learning From Dialogue Game Feedback. arXiv. [doi:10.18653/v1/2025.emnlp-main.1517](https://doi.org/10.18653/v1/2025.emnlp-main.1517)

`q2 · i?` · `design · r?`

Non-interactive benchmark evaluation (Section 5.2) of post-trained models on IFEval. For Llama-3.1-8B, IFEval falls from 76.88 (Baseline) to 67.25 after SFT (CS), and for the 70B model from 85.16 to 79.38; the authors call for instruction-following training regimes that also handle multi-turn interactive tasks.

> "Another relevant finding from this evaluation is the substantial drop in the ability to follow instruc- tions, as measured by IFEval."

## Discussion


## Related Claims
- [Specializing models for K-12 education does not require a broad loss of general capability, with MMMU-Pro accuracy increasing at all three scales](omniedu-general-capability-retained-after-specialization.md) — reports the opposite
- [SFT on successful dialogue-game episodes improves in-domain gameplay but reduces out-of-domain generalisation](sft-overfits-dialogue-game-training.md) — related
