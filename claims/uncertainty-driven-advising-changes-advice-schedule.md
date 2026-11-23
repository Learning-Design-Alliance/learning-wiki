---
type: claim
title: Uncertainty-driven advice collection changes when advice is requested from the teacher, spreading requests across training rather than consuming the budget early
description: Uncertainty-driven advice collection changes when advice is requested from the teacher, spreading requests across training rather than consuming the budget early
id: uncertainty-driven-advising-changes-advice-schedule
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: sahir-2022
    resource: "https://doi.org/10.48550/arXiv.2204.07254"
    title: "Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)"
    author: Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: sahir-2022-2
    resource: "https://doi.org/10.48550/arXiv.2204.07254"
    title: "Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)"
    author: Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Uncertainty-driven advice collection changes when advice is requested from the teacher, spreading requests across training rather than consuming the budget early

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The proposed algorithms spread teacher advice requests erratically across environment steps, whereas AIR consumes most of the budget early due to higher model-of-teacher uncertainty. [→ Sahir 2022](#sahir-2022)
`q2 i?` A higher advice reuse rate does not necessarily correspond to better evaluation performance. [→ Sahir 2022 (2)](#sahir-2022-2)

## Evidence

### Sahir 2022

Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)

`q2 · i?` · `causal · r2`

Figure 4 analysis of advice taken and reused every 100 steps across all domains, described in the Results text. The proposed algorithms ask the teacher as and when needed; no effect size is printed.

> "The amount of advice taken (bottom row) for SUA and SUA-AIR is, in general, spread in an erratic fashion across the environment steps. AIR seeks to consume most of the training budget early on due to the higher uncertainty of the model of the teacher."

### Sahir 2022 (2)

Sahir, Ercüment İlhan, Srijita Das, Matthew E. Taylor. (2022). Methodical Advice Collection and Reuse in Deep Reinforcement Learning. Proc. of the Adaptive and Learning Agents Workshop (ALA 2022). [doi:10.48550/arXiv.2204.07254](https://doi.org/10.48550/arXiv.2204.07254)

`q2 · i?` · `causal · r2`

Figure 4 analysis in the Results section comparing advice reuse rates against evaluation performance. The article reports no necessary correspondence between reuse rate and performance; no effect size is printed.

> "The number of advice reused (top row) for AIR is higher than SUA and SUA-AIR in almost all steps. However, having a higher advice reuse rate does not necessarily correspond to a better evaluation performance."

## Discussion


## Related Claims
- [Advised deep RL students outperform a no-advising student during early training in Atari domains, except Q*bert where advising benefits appear later](action-advising-beats-no-advising-early-training-atari.md) — related
- [SUA-AIR does not statistically outperform the AIR baseline; adding dual uncertainties is inconclusive as an improvement](sua-air-not-significantly-better-than-air.md) — related
- [A warning message about potential AI mistakes increases seventh-graders' hint requests in a math intelligent tutoring system](ai-fallibility-warning-increases-help-seeking.md) — related
