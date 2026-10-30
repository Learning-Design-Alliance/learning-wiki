---
type: claim
title: "A DoX-based pre-filtering step reduces the Intelligent Explanation Generator's asymptotic time complexity from quadratic to linear in the size of the text collection"
description: "A DoX-based pre-filtering step reduces the Intelligent Explanation Generator's asymptotic time complexity from quadratic to linear in the size of the text collection"
id: dox-prefiltering-reduces-complexity-to-linear
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: sovrano-francesco-2024
    resource: "https://doi.org/10.1007/s40593-024-00399-w"
    title: "Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w"
    author: Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# A DoX-based pre-filtering step reduces the Intelligent Explanation Generator's asymptotic time complexity from quadratic to linear in the size of the text collection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly
> **Design limits** · Sovrano Francesco 2024: no comparison group (read from the study by two models, 2026-10-27)

## Subclaims
`q1 i?` Selecting questions from only the highest-DoX paragraphs converts the question count into a constant, reducing complexity from O(|S|²) to O(|S|). [→ Sovrano Francesco 2024](#sovrano-francesco-2024)

## Evidence

### Sovrano Francesco 2024

Sovrano Francesco, Ashley Kevin, Brusilovsky Peter Leonid, Vitali Fabio. (2024). How to Improve the Explanatory Power of an Intelligent Textbook: a Case Study in Legal Writing. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00399-w

`q1 · i?` · `causal · r2`

Analytical derivation under the article's model: without step 1, selecting the questions best answered by the corpus has complexity O(|Qc|·|S|), which in the worst case is quadratic, O(|S|²). The derivation is the article's own complexity argument, not an empirical measurement.

> "Hence, considering that computing the DoX of |S| snippets of text has an asymptotic time complexity equal to O(|S|), it follows that step 1 reduces the complexity of the Intelligent Explanation Generator to O(|S|)."

## Discussion


## Related Claims
- [Explanations generated from generic questions were rated significantly better than those generated from random questions, supporting the hypothesis that question selection strategy matters](generic-questions-beat-random-questions-explanations.md) — related
- [Special-issue evidence: a knowledge-graph-enriched legal-writing textbook led to better learning outcomes than baselines, and aggregated emoji annotations helped teachers identify challenging text](special-issue-textbook-enhancements-outcomes.md) — related
