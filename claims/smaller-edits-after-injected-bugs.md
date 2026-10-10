---
type: claim
title: Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs
description: Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs
id: smaller-edits-after-injected-bugs
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rq2-edit-distance
    title: rq2-edit-distance
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Students make smaller code changes and fewer edit-and-run attempts after injected bugs than after natural bugs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`

## Subclaims
`q3 i?` Edit distance is lower for i:first than n:first (median 4 vs 24, mean 21.96 vs 93.92), and edit-and-run counts follow the same trend (first turn: 1.51 vs 2.15). [→ rq2-edit-distance](#rq2-edit-distance)

## Evidence

### rq2-edit-distance

Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667

`q3 · i?` · `causal · r1`

Log analysis measuring repair effort using mean absolute Levenshtein distance from initial buggy output to final edited version, and mean number of edit-and-run submissions. Results suggest "students treat injected bugs as localized repair tasks."

> "edit distance is lower fori:firstthann:first(median4vs.24, mean21 .96vs.93 .92), and the same trend holds for 'any turn' (median4vs.35, mean25.18vs.121 .02fori:anyvs.n:any)."

## Discussion


## Related Claims
- [Immediate success rates are higher after injected bugs than after natural bugs](higher-immediate-success-after-injected-bugs.md) — related
- [Injected bugs prompt more direct code edits while natural bugs prompt more reprompting in prompt-based programming tasks](injected-bugs-eliciting-direct-edits-natural-bugs-reprompting.md) — related
- [Prompting strategies differ by bug source: natural bugs elicit specification-oriented strategies while injected bugs elicit guidance-oriented strategies](prompting-strategies-differ-by-bug-source.md) — related
- [Students report code understanding, debugging, and AI-limitation awareness as primary learning benefits of buggy GenAI programming tasks](student-reflections-buggy-genai-learning-benefits.md) — related
