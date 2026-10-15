---
type: claim
title: On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00
description: On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00
id: three-seed-retrieval-sanity-check-perfect
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: sahil-al-farib-2026
    resource: "https://doi.org/10.48550/arxiv.2608.03161"
    title: "Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan. (2026). Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning. https://arxiv.org/abs/2608.03161 [doi:10.48550/arxiv.2608.03161](https://doi.org/10.48550/arxiv.2608.03161)"
    author: Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On a preliminary three-question retrieval sanity check, all seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All three seed questions achieved top-1 and top-3 hits on their gold concepts with mean top-5 recall of 1.00, but the article explicitly frames this as a sanity check, not a benchmark. [→ Sahil Al Farib 2026](#sahil-al-farib-2026)

## Evidence

### Sahil Al Farib 2026

Sahil Al Farib, Momota Ahsana Meem, Sheikh Redwanul Islam, and Md. Tanvir Raihan. (2026). Evidence-Grounded Multimodal Knowledge Graph Construction for Multi-Lecture Educational Reasoning. https://arxiv.org/abs/2608.03161 [doi:10.48550/arxiv.2608.03161](https://doi.org/10.48550/arxiv.2608.03161)

`q2 · i?` · `design · r2`

Numerical retrieval evaluation reported in the Results section over only three seed questions; Table VI lists top-1, top-3, and R@5 of 1.00 for each question. The article calls retrieval "a sanity check, not a final benchmark."

> "All three seed questions placed their target concept first and within the top three, with mean top-5 recall of 1.00 (Table VI)"

## Discussion


## Related Claims
- [Across three neural-network lectures, evidence and confidence checks retained 1,022 of 1,155 raw concept mentions (88.48%) and 312 of 400 raw relationship mentions (78.00%), yielding 172 canonical concepts and 282 graph relationships with 90.38% endpoint coverage](evidence-grounded-kg-extraction-yield-three-lectures.md) — related
- [Generated answers sometimes added correct background knowledge not explicitly supported by retrieved evidence, an unsupported-answer behavior the authors flag as requiring faithfulness evaluation](answers-add-unsupported-background-knowledge.md) — related
- [Fine-tuned SLMs retrieve the correct concept within a top-K shortlist but have limited top-1 accuracy](slm-topk-shortlist-limited-top1-accuracy.md) — related
