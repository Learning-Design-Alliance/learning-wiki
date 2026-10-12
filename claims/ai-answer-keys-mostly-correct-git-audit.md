---
type: claim
title: "A git-history audit found 96.3% of AI-generated answer-key question blocks needed no post-release semantic repair"
description: "A git-history audit found 96.3% of AI-generated answer-key question blocks needed no post-release semantic repair"
id: ai-answer-keys-mostly-correct-git-audit
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: jin-guo-liu-2026
    resource: "https://arxiv.org/abs/2606.23315"
    title: "Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang. (2026). Test-Driven, AI-Assisted Learning: Replacing Lectures with Weekly Closed-Book Tests. https://arxiv.org/abs/2606.23315"
    author: Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A git-history audit found 96.3% of AI-generated answer-key question blocks needed no post-release semantic repair

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Of 273 distinct answer-key question blocks, 263 (96.3%) had no post-release repair across subsequent commits. [→ Jin-Guo Liu 2026](#jin-guo-liu-2026)

## Evidence

### Jin-Guo Liu 2026

Jin-Guo Liu, Shang-Qi Lu, Xin-Ran Shi, Long-Li Zheng, Wei Wang. (2026). Test-Driven, AI-Assisted Learning: Replacing Lectures with Weekly Closed-Book Tests. https://arxiv.org/abs/2606.23315

`q2 · i?` · `design · r2`

Descriptive git-history audit of the repository's test and validation files, counting "273 distinct answer-key question blocks" and 10 semantic repairs. The authors call it operational evidence, not a controlled benchmark; no effect size printed.

> "Subsequent commits contained 10 semantic repairs (proof logic, missing conditions, theorem references, or analysis), leaving 263 of 273 blocks (96.3%) with no post-release repair."

## Discussion


## Related Claims
- [In a ten-request live textbook audit, citation integrity coexisted with substantive error: every citation resolved to its source, yet answers included retrieval misses and contradictions](citation-integrity-coexists-with-error.md) — related
- [Evidence tracing links 96 of 114 generated claims to source chunks, but three claims with retrieval scores of 0.50 or below show retrieval similarity alone is insufficient](evidence-tracing-114-claims-retrieval-limit.md) — related
