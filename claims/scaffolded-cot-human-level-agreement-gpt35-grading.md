---
type: claim
title: "Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters"
description: "Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters"
id: scaffolded-cot-human-level-agreement-gpt35-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-11-21
recheck_by: 2027
sources:
  - id: zhongzhou-chen-and-tong-wan-2024
    resource: "https://doi.org/10.1119/perc.2024.pr.chen"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhongzhou-chen-and-tong-wan-2024-2
    resource: "https://doi.org/10.1119/perc.2024.pr.chen"
    title: "Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)"
    author: Zhongzhou Chen and Tong Wan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Scaffolded COT prompting brings GPT-3.5 grading agreement with human raters to 70%-80%, comparable to agreement between two human raters

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`
> **Currency** · newest study 2024 · checked against its sources 2026-11-21 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The level of agreement between the scaffolded-COT AI grader and human raters reaches 70%-80% by percent agreement, comparable to the level of agreement between two human raters (75%). [→ Zhongzhou Chen and Tong Wan 2024 (2)](#zhongzhou-chen-and-tong-wan-2024-2)
`q2 i?` AI-human agreement under scaffolded COT is 20%-30% higher in grading accuracy than under conventional (naive) COT prompting. [→ Zhongzhou Chen and Tong Wan 2024 (2)](#zhongzhou-chen-and-tong-wan-2024-2)

## Evidence

### Zhongzhou Chen and Tong Wan 2024

Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)

`q2 · i?` · `design · r2`

Evaluation of GPT-3.5 Turbo grading of 40 incorrect-answer explanations from 94 exam responses, using percent agreement, mean simple matching distance, and quadratic weighted kappa against two human raters. Table I reports Pagree of 83% vs rater 1 and 70% vs rater 2 for scaffolded COT, versus 55%/50% for naive COT and a human-human baseline of 75%; SMD values were 0.08 and 0.11 for scaffolded COT versus 0.21/0.22 for naive COT, and QWK improved from 0.68 to 0.84 (rater 1) and from 0.58 to 0.66 (rater 2).

> "It is worth noting that the level of agreement measured by Pagree between Scaffolded COT and the human graders are comparable to the level of agreement between the human raters, between 70% - 80%"

### Zhongzhou Chen and Tong Wan 2024 (2)

Zhongzhou Chen and Tong Wan. (2024). Achieving Human Level Partial Credit Grading of Written Responses to Physics Conceptual Question using GPT-3.5 with Only Prompt Engineering. [doi:10.1119/perc.2024.pr.chen](https://doi.org/10.1119/perc.2024.pr.chen)

`q2 · i?` · `causal · r1`

The authors' own summary of the Table I comparison across the three prompt versions: percent agreement rose from 55%/50% (naive COT) to 83%/70% (scaffolded COT) against the two human raters, a difference the article characterizes as "20% - 30% higher than conventional COT".

> "the grading accuracy of GPT-3.5 using scaffolded COT is 20% - 30% higher than conventional COT"

## Discussion


## Related Claims
- [Preliminary re-testing found scaffolded COT unstable across runs while GPT-4o in chat mode reliably reached about 75% agreement using Detailed-Rubric COT](gpt4o-chat-mode-detailed-rubric-reliability.md) — related
- [Prompt refinement significantly improves GPT-3.5 agreement with human rater 1 but not, statistically, with rater 2](scaffolded-cot-significance-by-rater.md) — related
- [Out-of-the-box LLMs agree with human essay grades far less than human raters agree with each other](llm-essay-scoring-weak-human-agreement.md) — reports the opposite
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [Human inter-rater agreement for FRISCO essay scoring was reliable, with mean kappa 0.78–0.84 and percentage of agreement above 75% in all six dimensions](frisco-rater-agreement-reliable.md) — related
- [GPT-4 achieved almost perfect inter-rater reliability with faculty after three iterations of rubric engineering on three of four medical school OEQ questions](gpt4-almost-perfect-irr-after-rubric-engineering.md) — related
- [GPT-4o self-consistency mode grading of physics explanations reaches agreement with human graders almost identical to the agreement between the human graders themselves](gpt4o-self-consistency-human-level-grading-agreement.md) — related
- [GPT-4o grades students' written explanations on EMCS conceptual physics questions with accuracy comparable to a human grader (0-3% discrepancy, mean Cohen's kappa 0.77)](gpt4o-grades-written-physics-explanations-comparable-to-human-graders.md) — related
- [An LLM grader using a four-level explanation-quality rubric achieved substantial agreement with human consensus scores (quadratic-weighted κ=0.78).](llm-grader-substantial-agreement-human-consensus.md) — related
- [The GPT-4o mini event classifier agrees with domain experts at almost-perfect pairwise levels (κ = 0.841–0.855), reducing multi-rater Fleiss κ only marginally (0.682 to 0.624)](llm-event-classifier-expert-agreement.md) — related
