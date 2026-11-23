---
type: claim
title: SFT on successful dialogue-game episodes improves in-domain gameplay but reduces out-of-domain generalisation
description: SFT on successful dialogue-game episodes improves in-domain gameplay but reduces out-of-domain generalisation
id: sft-overfits-dialogue-game-training
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
    kind: causal
    rigour: "?"
---

# SFT on successful dialogue-game episodes improves in-domain gameplay but reduces out-of-domain generalisation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training with SFT on successful episodes improves in-domain performance but reduces generalisation, with a decrease in all dimensions of performance on out-of-domain games. [→ Horst 2025](#horst-2025)

## Evidence

### Horst 2025

Horst, N., Mazzaccara, D., Schmidt, A., Sullivan, M., Momentè, F., Franceschetti, L., Sadler, P., Hakimov, S., Testoni, A., Bernardi, R., Fernández, R., Koller, A., Lemon, O., Schlangen, D., Giulianelli, M., & Suglia, A. (2025). PLAYPEN: An Environment for Exploring Learning From Dialogue Game Feedback. arXiv. [doi:10.18653/v1/2025.emnlp-main.1517](https://doi.org/10.18653/v1/2025.emnlp-main.1517)

`q2 · i?` · `causal · r?`

Results section reporting clemscore evaluations of Llama-3.1-8B, Llama-3.1-70B and Qwen-2-7B post-trained with SFT on filtered successful clembench episodes. In-domain clemscore for Llama-3.1-8B rises from 19.39 to 40.11 while out-of-domain falls from 24.58 to 22.53; the authors note this "aligns with prior observations that SFT tends to overfit to the training distribution".

> "Training with SFT on successful episodes improves in-domain performance but reduces generalisation, with a decrease in all dimensions of performance on out-of-domain games."

## Discussion


## Related Claims
- DPO variants improve in-domain gameplay over the baseline but fail to outperform the best SFT model and degrade out-of-domain games — related
- GRPO applied to the base model gives consistent clemscore gains on both in-domain and out-of-domain games without degrading other skills — related
- Scaling the backbone to Llama-3.1-70B nearly doubles clemscore, with diminishing SFT returns in-domain — related
- [Post-training on dialogue games causes a substantial drop in instruction-following ability as measured by IFEval](dialogue-game-training-drops-ifeval.md) — related
