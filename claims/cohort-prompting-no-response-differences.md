---
type: claim
title: Prompting ChatGPT to respond as-if from different cohorts yields no differences in FCI response distributions
description: Prompting ChatGPT to respond as-if from different cohorts yields no differences in FCI response distributions
id: cohort-prompting-no-response-differences
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: fabian-kieser-2023
    resource: "https://doi.org/10.1103/physrevphyseducres.19.020150"
    title: "Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)"
    author: Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompting ChatGPT to respond as-if from different cohorts yields no differences in FCI response distributions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prompting ChatGPT to answer the FCI as a 10th-grade school student versus an engineering student produced no statistically significant differences between the three cohorts' correct-response distributions. [→ Fabian Kieser 2023](#fabian-kieser-2023)

## Evidence

### Fabian Kieser 2023

Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)

`q2 · i?` · `design · r2`

Kruskal-Wallis rank test comparing correct-response distributions of ChatGPT responses prompted as school students (N=8), as engineering students (N=18), and unprompted responses: "H=1.79, p=0.409, η2=-0.01". No effect size of meaningful magnitude was printed; equivalence was not tested.

> "The Kruskal-Wallis test yields a value for potential group differences of H=1.79, p=0.409, η2=-0.01. Essentially, no differences were found between the aggregated correct response distributions for the three cohorts."

## Discussion


## Related Claims
- [Prompting ChatGPT with specific physics preconceptions introduces much response variance that approximates real student FCI distributions](preconception-prompting-yields-variance.md) — related
- [On MedQA, GPT-5.4-mini's accuracy increases monotonically with prompt sophistication across semantically equivalent questions, with generated Low Literacy prompt variants scoring significantly below Prompt Engineer variants](prompt-privilege-monotonic-accuracy-gap-medqa.md) — related
