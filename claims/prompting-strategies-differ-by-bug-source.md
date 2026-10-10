---
type: claim
title: "Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies"
description: "Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies"
id: prompting-strategies-differ-by-bug-source
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rq2-strategies
    title: rq2-strategies
    q: 3
    i: "?"
    kind: qualitative
    rigour: 2
---

# Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · qualitative `r2` · `q3`

## Subclaims
`q3 i?` Natural bug states are dominated by specification-oriented strategies (Update signature 30.6%, Extend task 27.8% in n:first), while injected bug states show more guidance and restatement-oriented strategies (Provide guidance 33.0% in i:any). [→ rq2-strategies](#rq2-strategies)

## Evidence

### rq2-strategies

Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667

`q3 · i?` · `qualitative · r2`

Qualitative coding of 204 sampled prompts using a single-label coding scheme with Krippendorff's α = 0.87. The codebook includes eight strategy categories from Task reframe to Meta. Distribution differs by bug source across n:first, n:any, i:first, and i:any groups.

> "Natural bug states are dominated by specification-oriented strategies, while injected bug states show more guidance and restatement-oriented strategies."

## Discussion


## Related Claims
- [Immediate success rates are higher after injected bugs than after natural bugs](higher-immediate-success-after-injected-bugs.md) — related
- [Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks](injected-bugs-eliciting-direct-edits-natural-bugs-reprompting.md) — related
- [Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs](smaller-edits-after-injected-bugs.md) — related
- [Students report code understanding, debugging, and AI-limitation awareness as primary learning benefits of buggy GenAI programming tasks](student-reflections-buggy-genai-learning-benefits.md) — related
