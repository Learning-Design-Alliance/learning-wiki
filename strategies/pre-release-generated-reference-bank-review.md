---
type: strategy
id: pre-release-generated-reference-bank-review
title: Generate and validate a pilot reference bank before releasing an assignment to reveal convergence or ambiguity and decide what evidence the assessment should elicit
description: Before students see an assignment, the instructor generates solutions from the exact handout and starter code, evaluates every output with the instructor tests, and inspects convergence per task.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: runlong-ye-2026
    resource: "https://arxiv.org/abs/2610.00863"
    title: "Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863"
    author: Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut
---

# Generate and validate a pilot reference bank before releasing an assignment to reveal convergence or ambiguity and decide what evidence the assessment should elicit

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Before students see an assignment, the instructor generates solutions from the exact handout and starter code, evaluates every output with the instructor tests, and inspects convergence per task. The article states this "profile shows where an assignment channels solutions toward one form and where repeatedly generated failures expose ambiguity, giving the instructor a chance to revise the task before students encounter it." The observed batch cost of about 5 US cents per attempt suggests a 100-attempt pilot costs about US$5, though the article does not establish that one hundred attempts suffice for every task.

## Design Implications

### Context
#### Requirements
- Generation must use the exact handout and starter code students will receive, and every output must be evaluated with the instructor tests before release.
#### Constraints
- The article's results do not establish that one hundred attempts are sufficient for every task; low matching alone does not mean an assignment elicits richer reasoning, as Lab 10 shows.

### Target Learners
- CS1 introductory programming students

### Target Learning Goals
- Eliciting reasoning, testing, and intermediate work on programming assignments

## Claims

- [Solutions from different LLM providers converged broadly on most CS1 labs, with cross-LLM MOSS match rates of about 88% pooled across labs but only 13.18–22.11% on Lab 10](../claims/cross-llm-convergence-task-dependent.md) [+W]
- [On tightly specified functions, LLMs converged on a few exact AST forms (1–14 per 1,000 files) while an open-ended function remained diverse, and source was associated with exact form for all five functions](../claims/exact-ast-form-convergence-constrained-functions.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Runlong Ye, Jing Fan, Angela Zavaleta Bernuy, Oscar Karnalim, Paul Denny, Juho Leinonen, and Michael Liut. (2026). Correctness, Convergence, and AI-Generated Code Detection: A Longitudinal Study of Student and Large Language Model Code in Introductory Programming. https://arxiv.org/abs/2610.00863
