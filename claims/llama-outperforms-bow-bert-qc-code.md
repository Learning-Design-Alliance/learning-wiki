---
type: claim
title: Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code
description: Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code
id: llama-outperforms-bow-bert-qc-code
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: rebeckah-k-fussell-2025
    resource: "https://doi.org/10.1103/physrevphyseducres.21.010128"
    title: "Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)"
    author: Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Fine-tuned LLaMA models outperform bag of words and BERT across performance metrics for the QC code

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The two trained LLaMA models performed better than bag of words and BERT across AUC, accuracy, and balanced accuracy for the QC code, approaching but not exceeding human inter-rater balanced accuracy. [→ Rebeckah K. Fussell 2025](#rebeckah-k-fussell-2025)

## Evidence

### Rebeckah K. Fussell 2025

Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)

`q2 · i?` · `causal · r2`

Performance comparison of five model types on the QC code, averaged over five training trials applied to 22 hold-out lab notes, reported in Results with Fig. 2. The article states the two trained LLaMA models "performed better than bag of words and BERT across all three metrics".

> "The two trained LLaMA models performed better than bag of words and BERT across all three metrics, making use of the greater computing power dedicated to training."

## Discussion


## Related Claims
- [Few-shot LLaMA significantly underperforms even the traditional bag of words approach for skill classification](few-shot-llama-underperforms-trained-models.md) — related
- [Adding a prompt to fine-tuned LLaMA yields performance similar to unprompted fine-tuned LLaMA](prompted-llama-similar-to-unprompted.md) — related
