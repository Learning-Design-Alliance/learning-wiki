---
type: claim
title: In the simulations, replacing the similarity-weighted influence term with a simple average of group opinions lowers final performance and speeds up consensus, and removes the diversity-driven performance collapse
description: In the simulations, replacing the similarity-weighted influence term with a simple average of group opinions lowers final performance and speeds up consensus, and removes the diversity-driven performance collapse
id: simulation-weighted-influence-term-outperforms-simple-average
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: jibeom-seo-2025
    resource: "https://doi.org/10.1016/j.physa.2025.130670"
    title: "Jibeom Seo, Beom Jun Kim. (2025). Opinion dynamics model of collaborative learning. [doi:10.1016/j.physa.2025.130670](https://doi.org/10.1016/j.physa.2025.130670)"
    author: Jibeom Seo, Beom Jun Kim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In the simulations, replacing the similarity-weighted influence term with a simple average of group opinions lowers final performance and speeds up consensus, and removes the diversity-driven performance collapse

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When the first term of the group-influence vector is formulated as a simple sum of member opinions, final performance decreases, consensus occurs more quickly, and the nonlinear phase transition with initial diversity disappears. [→ Jibeom Seo 2025](#jibeom-seo-2025)

## Evidence

### Jibeom Seo 2025

Jibeom Seo, Beom Jun Kim. (2025). Opinion dynamics model of collaborative learning. [doi:10.1016/j.physa.2025.130670](https://doi.org/10.1016/j.physa.2025.130670)

`q2 · i?` · `design · r2`

Model-ablation simulation comparing the original similarity-weighted influence term with a simple-average formulation. The article reports that with the simple average "the final performance decreases and opinion consensus occurs more quickly compared to our original model."

> "we found that when the first term is instead formulated as P j ⃗Sj (representing that students simply adopt the average opinions of their group members), the final performance decreases and opinion consensus occurs more quickly compared to our original model."

## Discussion


## Related Claims
- [In the model's simulations, group performance increases through discussion even when no group member initially knows the correct answer, provided initial opinions sufficiently differ](simulation-group-discussion-improves-performance-diverse-initial-opinions.md) — related
- [In the simulations, final group performance depends more on initial opinion diversity than on initial group performance, with a threshold diversity of about 0.5 above which final performance is high regardless of initial score](simulation-initial-diversity-beats-initial-performance-threshold-0-5.md) — related
