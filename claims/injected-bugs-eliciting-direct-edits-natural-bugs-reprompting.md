---
type: claim
title: Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks
description: Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks
id: injected-bugs-eliciting-direct-edits-natural-bugs-reprompting
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rq1-actions
    title: rq1-actions
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`

## Subclaims
`q3 i?` Students are more likely to edit code directly after injected bugs (67.57% i:first vs 45.42% n:first) and more likely to reprompt after natural bugs (51.71% n:first vs 31.46% i:first). [→ rq1-actions](#rq1-actions)

## Evidence

### rq1-actions

Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667

`q3 · i?` · `causal · r1`

Classroom log analysis of 2,636 sessions from 917 CS1 students using a prompt-based programming platform with a bug injection pipeline. Pooled first-turn summaries show a clear shift by bug source in follow-up action choice, with "edit actions are more common" after injected bugs.

> "Students are more likely to choose prompting inn:firstthan in i:first(51 .71%vs.31 .46%), while edit actions are more common in i:firstthan inn:first(67 .57%vs.45 .42%)."

## Discussion


## Related Claims
- [Immediate success rates are higher after injected bugs than after natural bugs](higher-immediate-success-after-injected-bugs.md) — related
- [Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs](smaller-edits-after-injected-bugs.md) — related
- [Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies](prompting-strategies-differ-by-bug-source.md) — related
- [Students report code understanding, debugging, and AI-limitation awareness as primary learning benefits of buggy GenAI programming tasks](student-reflections-buggy-genai-learning-benefits.md) — related
