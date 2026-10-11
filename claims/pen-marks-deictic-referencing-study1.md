---
type: claim
title: "Pen input supported deictic referencing: 85% of V1 queries contained at least one visible pen mark, and ease of referencing improved significantly over the baseline"
description: "Pen input supported deictic referencing: 85% of V1 queries contained at least one visible pen mark, and ease of referencing improved significantly over the baseline"
id: pen-marks-deictic-referencing-study1
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: penmark
    title: penmark
    q: 3
    i: "?"
    kind: design
    rigour: 3
  - id: ease-ref
    title: ease-ref
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Pen input supported deictic referencing: 85% of V1 queries contained at least one visible pen mark, and ease of referencing improved significantly over the baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r1`, 1 design `r3` · `q3`

## Subclaims
`q3 i?` In the V1 dataset, underlining (45%), circles (29%), boxes (9%) and braces (2%) dominated, and 85% of queries contained at least one visible mark. [→ penmark](#penmark)
`q3 i?` Ease of referencing specific elements was significantly higher for V1 than baseline (6.00 vs. 4.38, p=0.015). [→ ease-ref](#ease-ref)

## Evidence

### penmark

Jeongmin Rhee, Changhee Lee, Hyunwoo Kim, Kiroong Choe, Bohyoung Kim, Sungahn Ko, and Jinwook Seo. 2026. Penquiry: A Pen-based Interactive In-situ Q&A System Leveraging LLMs. https://arxiv.org/abs/2609.19870

`q3 · i?` · `design · r3`

Analysis of the 204 queries in the Penquiry V1 dataset from Study 1, classified using Marshall's annotation taxonomy; the authors state this "overwhelming reliance on visual deictic cues demonstrates that pen input effectively supports precise referencing behaviors."

> "Participants predominantly used four pen-mark types: underlining (45%), circles (29%), boxes (9%), and braces (2%) (Appendix A.3). Notably, 85% of queries contained at least one visible mark."

### ease-ref

Jeongmin Rhee, Changhee Lee, Hyunwoo Kim, Kiroong Choe, Bohyoung Kim, Sungahn Ko, and Jinwook Seo. 2026. Penquiry: A Pen-based Interactive In-situ Q&A System Leveraging LLMs. https://arxiv.org/abs/2609.19870

`q3 · i?` · `causal · r1`

Study 1 questionnaire item (N=16, within-subjects) on ease of referencing specific elements: V1 scored 6.00 versus baseline 4.38, p=0.015. Interview data (e.g., P16) indicated pointing avoided lengthy textual descriptions of graph regions.

> "Regarding the “Ease of referencing specific elements, ”PenquiryV1 showed a statistically significant improvement over the baseline (6.00 vs. 4.38, p = 0.015*), allowing participants to easily designate specific targets."

## Discussion


## Related Claims
- [Unmediated pen input introduced new pen-specific barriers: lack of visual feedback on referential intent and high interaction cost of handwriting complex queries](pen-specific-barriers-unmediated-ink.md) — related
- [In Study 1, learners preferred Penquiry V1 for part-scoped, specific-target and short questions, and favored the baseline for general topics and longer interpretive questions](penquiry-v1-question-type-preferences.md) — related
- [In Study 1, Penquiry V1 reduced physical demand and better maintained learning flow, and received higher TAM ratings, than a keyboard baseline](penquiry-v1-lower-physical-demand-higher-flow.md) — related
