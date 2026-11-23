---
type: claim
title: "GATA agents rarely examine the cookbook, so they usually do not learn the game's goal"
description: "GATA agents rarely examine the cookbook, so they usually do not learn the game's goal"
id: gata-rarely-examines-cookbook
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: mathieu-tuli-2022
    resource: "https://doi.org/10.52202/068431-1413"
    title: "Mathieu Tuli, Andrew C. Li, Pashootan Vaezipoor, Toryn Q. Klassen, Scott Sanner, Sheila A. McIlraith. (2022). Learning to Follow Instructions in Text-Based Games. 36th Conference on Neural Information Processing Systems (NeurIPS 2022). [doi:10.52202/068431-1413](https://doi.org/10.52202/068431-1413)"
    author: Mathieu Tuli, Andrew C. Li, Pashootan Vaezipoor, Toryn Q. Klassen, Scott Sanner, Sheila A. McIlraith
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GATA agents rarely examine the cookbook, so they usually do not learn the game's goal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Mathieu Tuli 2022: no comparison group (read from the study by two models, 2026-11-23)

## Subclaims
`q2 i?` Across levels 1 and 2 and both training-set sizes, the cookbook was examined in at most 3 of 20 testing games (15%). [→ Mathieu Tuli 2022](#mathieu-tuli-2022)

## Evidence

### Mathieu Tuli 2022

Mathieu Tuli, Andrew C. Li, Pashootan Vaezipoor, Toryn Q. Klassen, Scott Sanner, Sheila A. McIlraith. (2022). Learning to Follow Instructions in Text-Based Games. 36th Conference on Neural Information Processing Systems (NeurIPS 2022). [doi:10.52202/068431-1413](https://doi.org/10.52202/068431-1413)

`q2 · i?` · `causal · r2`

RL experiments in the TextWorld Cooking domain with GATA across four settings (levels 1 and 2, 20- and 100-game training sets); the article reports the cookbook "was the cookbook examined more than 15% of the time" in none of them, i.e. 3/20 testing games at most.

> "We tested a GATA agent on levels 1 and 2 in the Cooking domain, after training on either the 20-game or 100-game training set, and found that in none of those settings was the cookbook examined more than 15% of the time (3/20 testing games)."

## Discussion


## Related Claims
- Forcing GATA to examine the cookbook does not improve its performance — related
- GATA performance in TextWorld Cooking is largely unaffected by the presence or absence of instructions — related
- LTL-GATA outperforms GATA baselines and achieves high task-completion success rates across Cooking levels — related
- LTL progression is critical to LTL-GATA's performance; removing it causes a large drop below baseline performance — related
