---
type: claim
title: "Model accuracy depends strongly on the concept inventory, with BEMA (66.7%) and TUG-K (64.4%) averages higher than QMVI (44.4%) and FTGOT (35.1%)"
description: "Model accuracy depends strongly on the concept inventory, with BEMA (66.7%) and TUG-K (64.4%) averages higher than QMVI (44.4%) and FTGOT (35.1%)"
id: mllm-accuracy-varies-by-concept-inventory
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: giulia-polverini-and-bor-gregorcic-2025
    resource: "https://doi.org/10.1088/1361-6404/ae03f8"
    title: "Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)"
    author: Giulia Polverini and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model accuracy depends strongly on the concept inventory, with BEMA (66.7%) and TUG-K (64.4%) averages higher than QMVI (44.4%) and FTGOT (35.1%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Average performance across all tested models was higher on BEMA and TUG-K than on QMVI and FTGOT, with FTGOT hardest even for top models. [→ Giulia Polverini and Bor Gregorcic 2025](#giulia-polverini-and-bor-gregorcic-2025)

## Evidence

### Giulia Polverini and Bor Gregorcic 2025

Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)

`q2 · i?` · `design · r2`

Aggregated benchmark results across the 15 models show "The average performance across all tested models on BEMA (66.7%) and TUG-K (64.4%) was higher than on QMVI (44.4%) and FTGOT (35.1%)"; per-model gaps between highest and lowest inventory ranged 30–50 points.

> "The average performance across all tested models on BEMA (66.7%) and TUG-K (64.4%) was higher than on QMVI (44.4%) and FTGOT (35.1%)."

## Discussion


## Related Claims
- [GPT-4o averages 71.1% on English physics concept inventories, with individual inventory scores ranging from 27% to 97%](gpt4o-english-inventory-average-71-percent.md) — a broader claim this one bears on
- [Average effect sizes by concept inventory ranged from 1.248 (CINS) to 0.052 (CCI), with the two physics inventories relatively large](lasso-effect-size-varies-by-concept-inventory.md) — related
- [The best-performing MLLMs already outperform post-instruction university student averages on the four tested concept inventories](top-mllms-exceed-post-instruction-student-averages.md) — related
