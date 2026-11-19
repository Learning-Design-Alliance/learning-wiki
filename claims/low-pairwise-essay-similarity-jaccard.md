---
type: claim
title: Pairwise essay similarity was low across the whole sample, with a median Jaccard similarity index of 0.002
description: Pairwise essay similarity was low across the whole sample, with a median Jaccard similarity index of 0.002
id: low-pairwise-essay-similarity-jaccard
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
sources:
  - id: željana-bašić-2023
    resource: "https://doi.org/10.35542/osf.io/n5m7s"
    title: "Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)"
    author: Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Pairwise essay similarity was low across the whole sample, with a median Jaccard similarity index of 0.002

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Željana Bašić 2023: no comparison group (read from the study by two models, 2026-11-19)

## Subclaims
`q2 i?` Pairwise comparison of all essays using the Jaccard similarity index showed low similarity overall, with a median of 0.002 and a range of 0 to 0.054. [→ Željana Bašić 2023](#zeljana-basic-2023)

## Evidence

### Željana Bašić 2023

Željana Bašić, Ana Banovac, Ivana Kružić, Ivan Jerković. (2023). Better by You, better than Me? ChatGPT-3 as writing assistance in students' essays. University Department of Forensic Sciences, University of Split. [doi:10.35542/osf.io/n5m7s](https://doi.org/10.35542/osf.io/n5m7s)

`q2 · i?` · `causal · r1`

Pairwise document similarity was computed in R Studio with the Textreuse package for all 18 essays. The article reports "a median value of the Jaccard similarity index of 0.002 (0 – 0.054)"; no effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "The text similarity in the overall sample was low  (Supplementary table 1) , with a median value of the Jaccard similarity index of 0.002 (0 – 0.054)."

## Discussion


## Related Claims
- [LLMs and instructors agree broadly on where feedback belongs but diverge on exact sentence spans, with span overlap strongly goal-dependent and LLMs highlighting more of each essay](llm-instructor-span-overlap-goal-dependent.md) — related
- [Cooccurrence network analysis found that students' AI-ethics thinking changed from fragmented clusters at pretest to integrated networks at posttest in one single-group pre-post study](cooccurrence-network-structural-transformation.md) — related
