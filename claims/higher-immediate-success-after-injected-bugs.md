---
type: claim
title: Immediate success rates are higher after injected bugs than after natural bugs
description: Immediate success rates are higher after injected bugs than after natural bugs
id: higher-immediate-success-after-injected-bugs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rq1-success
    title: rq1-success
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Immediate success rates are higher after injected bugs than after natural bugs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`

## Subclaims
`q3 i?` Immediate success for any action is 89.92% for i:first vs 51.16% for n:first, with the same contrast holding within prompt and edit actions. [→ rq1-success](#rq1-success)

## Evidence

### rq1-success

Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667

`q3 · i?` · `associational · r2`

Log analysis of student sessions in the Prompt Programming platform. Immediate success is defined counterfactually for prompt actions using the injection audit, and by reaching a passing result through edit-and-run attempts for edit actions. Injected bugs show "success for any action is" substantially higher.

> "In the 'first turn' summaries, success for any action is89 .92%fori:firstvs.51 .16%forn:first; the same contrast holds within prompt actions (87.74%vs.43 .30%) and edit actions (92.22%vs.63 .33%)."

## Discussion


## Related Claims
- [Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs](smaller-edits-after-injected-bugs.md) — related
- [Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks](injected-bugs-eliciting-direct-edits-natural-bugs-reprompting.md) — related
- [Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies](prompting-strategies-differ-by-bug-source.md) — related
