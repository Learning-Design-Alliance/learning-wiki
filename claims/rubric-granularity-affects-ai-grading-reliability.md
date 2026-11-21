---
type: claim
title: Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances
description: Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances
id: rubric-granularity-affects-ai-grading-reliability
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

# Fine-grained rubric grading of entire problems exceeds LLM bookkeeping capabilities, while parts-based grading is more reliable but misses nuances

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Fine-grained rubric grading for a complete problem is beyond GPT-4-32k's bookkeeping capabilities, producing frequent grading failures. [→ Gerd Kortemeyer 2024](#gerd-kortemeyer-2024)
`q2 i?` The LLM was much better equipped to keep track of four or five problem parts than of 22 rubric items, and necessary regrades dramatically decreased with parts-based grading. [→ Gerd Kortemeyer 2024 (2)](#gerd-kortemeyer-2024-2)

## Evidence

### Gerd Kortemeyer 2024

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Results from Workflow 1 (rubric-based grading of 252 exams with 22 rubric items for Problem 1). Very frequent failures to produce complete grading output within available point ranges made WF1 nonviable.

> "The low agreement between TAs and AI on individual rubric items, as well as the very frequent failures to provide a complete grading output with points within the available range, indicates that fine-grained rubric grading for a complete problem is beyond GPT-4-32k's "bookkeeping" capabilities."

### Gerd Kortemeyer 2024 (2)

Gerd Kortemeyer, Julian Nöhl, Daria Onishchuk. (2024). Grading Assistance for a Handwritten Thermodynamics Exam using Artificial Intelligence: An Exploratory Study. [doi:10.1103/physrevphyseducres.20.020144](https://doi.org/10.1103/physrevphyseducres.20.020144)

`q2 · i?` · `design · r2`

Results from Workflow 2 (parts-based grading). Switching from 22 rubric items to 4–5 problem parts dramatically decreased regrades. Standard deviations of average grades were lower than in WF1.

> "Initial tests on Problem 1 showed that the LLM was much better equipped to keep track of four or five problem parts than of 22 rubric items, and the number of necessary regrades dramatically decreased"

## Discussion


## Related Claims
- [AI grades more leniently than teaching assistants and clusters rubric item grades more strongly, indicating holistic rather than differentiated grading](ai-grades-leniently-and-holistically.md) — related
- [In a 252-student thermodynamics exam grading study, LLMs struggled with numerical tasks such as counting and addition but were beneficial for grading free-form exam responses](llm-grading-freeform-strengths.md) — related
- [Grading prompt granularity significantly impacts automated grading success: fine-grained rubrics on entire problems caused bookkeeping mistakes, while subdividing problems with a comprehensive sample solution proved more reliable](rubric-granularity-affects-automated-grading.md) — possibly the same claim (merge candidate)
- [Rubric-based and parts-based grading workflows outperform problem-based grading, possibly because GPT-4-32k cannot reliably add numbers](wf1-wf2-outperform-wf3-grading.md) — a broader claim this one bears on
- [LLMs show discoverability bias: they accurately identify only high-quality open-ended biology responses and miss nuanced misconceptions](llm-discoverability-bias-open-ended-biology-assessment.md) — related
- [GPT-4 scoring errors clustered on multiple possible answers, unrecognized vocabulary, and missed incorrect or missing answers, while faculty were overly generous graders](gpt4-faculty-error-patterns-oeq-scoring.md) — related
- [Prompt composition shifts LLM grading bias: rubric-only prompts yield stricter grading, examples-only prompts more lenient grading, and combining both produces the best results](rubric-examples-prompt-variant-balances-grading-bias.md) — related
