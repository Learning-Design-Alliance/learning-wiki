---
type: claim
title: AI grades more leniently than teaching assistants and clusters rubric item grades more strongly, indicating holistic rather than differentiated grading
description: AI grades more leniently than teaching assistants and clusters rubric item grades more strongly, indicating holistic rather than differentiated grading
id: ai-grades-leniently-and-holistically
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: gerd-kortemeyer-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.020144"
    title: "Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)"
    author: Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: gerd-kortemeyer-2024-2
    resource: "https://doi.org/10.1103/physrevphyseducres.20.020144"
    title: "Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)"
    author: Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AI grades more leniently than teaching assistants and clusters rubric item grades more strongly, indicating holistic rather than differentiated grading

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Despite prompts enforcing strict grading, the AI grades more leniently than TAs. [→ Gerd Kortemeyer 2024](#gerd-kortemeyer-2024)
`q2 i?` AI grades cluster together much more strongly than TA grades, suggesting the AI grades holistically with limited ability to differentiate between correct and incorrect solution steps. [→ Gerd Kortemeyer 2024 (2)](#gerd-kortemeyer-2024-2)

## Evidence

### Gerd Kortemeyer 2024

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Observed across grading workflows on the 252-exam corpus. The R²=0.84 achieved with verbose synthetic answers in an earlier study could not be reproduced with authentic handwritten data.

> "in spite of the prompts in Figs. 10–12 attempting to enforce strict grading, the AI grades more leniently than TAs"

### Gerd Kortemeyer 2024 (2)

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Fruchterman-Reingold analysis of Spearman correlations between rubric items (WF1, Problem 1). AI rubric item grades are strongly inter-correlated unlike TA grades; summative totals are nonetheless more closely aligned than individual items.

> "the AI-grades cluster together much more strongly than those of the TAs, which could be explained by the TAs being able to grade the items independently, while the AI tends to grade holistically with only limited ability to differentiate between one step of a solution being correct and another one incorrect"

## Discussion


## Related Claims
- [AI-assigned total scores on a handwritten chemistry exam align strongly with TA-assigned totals (R2 = 0.91), while per-problem agreement is lower (R2 = 0.61–0.85)](ai-total-scores-align-with-ta-grades-chemistry-exam.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — a broader claim this one bears on
- [Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances](rubric-granularity-affects-ai-grading-reliability.md) — related
