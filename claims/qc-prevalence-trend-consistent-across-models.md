---
type: claim
title: All three trained models measure a similar trend in QC skill prevalence across lab units, with L1b highest and L1a fewest
description: All three trained models measure a similar trend in QC skill prevalence across lab units, with L1b highest and L1a fewest
id: qc-prevalence-trend-consistent-across-models
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
    kind: design
    rigour: 2
---

# All three trained models measure a similar trend in QC skill prevalence across lab units, with L1b highest and L1a fewest

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Bag of words, BERT, and LLaMA all agree that the second lab session L1b has the highest prevalence of QC-coded sentences and L1a the fewest, telling a story of scaffolding that prompts then fades the skill. [→ Rebeckah K. Fussell 2025](#rebeckah-k-fussell-2025)

## Evidence

### Rebeckah K. Fussell 2025

Rebeckah K. Fussell, Megan Flynn, Anil Damle, Michael F.J. Fox, and N. G. Holmes. (2025). Comparing Large Language Models for supervised analysis of students’ lab notes. [doi:10.1103/physrevphyseducres.21.010128](https://doi.org/10.1103/physrevphyseducres.21.010128)

`q2 · i?` · `design · r2`

Outcomes analysis applying three trained models to 468 lab notes, reported as barcharts in Fig. 4a with statistical and systematic uncertainty. The article interprets the pattern as scaffolding in L1b prompting more QC engagement, which drops when scaffolding is removed.

> "For example, all models agree that the second lab session, L1b, has the highest prevalence (average fraction) of sentences with the QC code and L1a has the fewest."

## Discussion


## Related Claims
- [Absolute prevalence estimates differ across models and generally do not agree within uncertainties, despite similar trends](model-prevalence-estimates-differ-within-uncertainties.md) — related
- [For the PI code, all three models measure a similar low, stable prevalence across sessions, with the single-session L2 unit lowest](pi-prevalence-trend-l2-lowest.md) — related
