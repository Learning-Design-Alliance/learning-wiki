---
type: claim
title: Shorter codebooks and shorter data excerpts yield higher initial LLM coding accuracy, and a smaller specialization gap between codebook and excerpt helps
description: Shorter codebooks and shorter data excerpts yield higher initial LLM coding accuracy, and a smaller specialization gap between codebook and excerpt helps
id: claim-llm-coding-accuracy-shorter-codebooks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jeongyeon-kim-and-john-mitchell-2026
    resource: "https://doi.org/10.48550/arxiv.2609.11109"
    title: "Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109 [doi:10.48550/arxiv.2609.11109](https://doi.org/10.48550/arxiv.2609.11109)"
    author: Jeongyeon Kim and John Mitchell
    q: 2
    i: 1
    kind: associational
    rigour: 2
  - id: jeongyeon-kim-and-john-mitchell-2026-2
    resource: "https://arxiv.org/abs/2609.11109"
    title: "Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109"
    author: Jeongyeon Kim and John Mitchell
    q: 2
    i: 2
    kind: design
    rigour: 2
  - id: jeongyeon-kim-and-john-mitchell-2026-3
    resource: "https://arxiv.org/abs/2609.11109"
    title: "Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109"
    author: Jeongyeon Kim and John Mitchell
    q: 2
    i: 1
    kind: associational
    rigour: 2
---

# Shorter codebooks and shorter data excerpts yield higher initial LLM coding accuracy, and a smaller specialization gap between codebook and excerpt helps

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2` · `i1`–`i2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i1` Lengthier codebooks negatively affect initial automated coding accuracy (effect size -0.287, p<0.0001). [→ Jeongyeon Kim and John Mitchell 2026](#jeongyeon-kim-and-john-mitchell-2026)
`q2 i2` Lengthier excerpts to be coded negatively affect initial coding accuracy (effect size -0.438, p<0.0001). [→ Jeongyeon Kim and John Mitchell 2026 (2)](#jeongyeon-kim-and-john-mitchell-2026-2)
`q2 i1` A smaller gap of degree of specialization between codebook and excerpt predicts higher initial coding accuracy (effect size -0.331 for the gap, p<0.0001). [→ Jeongyeon Kim and John Mitchell 2026 (3)](#jeongyeon-kim-and-john-mitchell-2026-3)

## Evidence

### Jeongyeon Kim and John Mitchell 2026

Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109 [doi:10.48550/arxiv.2609.11109](https://doi.org/10.48550/arxiv.2609.11109)

`q2 · i1` · `associational · r2`

Mixed-effects model analysis across four qualitative datasets (education, law, sociology, medicine) relating dataset characteristics to initial coding accuracy. The table reports codebook length at "(-11.702, -0.287)", i.e. p<0.0001 with effect size -0.287, stating "The shorter the codebook, the higher the initial accuracy of automated coding."

> "Length of Codebook < 0.0001 **** (-11.702, -0.287) The shorter the codebook, the higher the initial accuracy of automated coding."

### Jeongyeon Kim and John Mitchell 2026 (2)

Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109

`q2 · i2` · `design · r2`

Same mixed-effects analysis of dataset characteristics. The table reports excerpt length at "(-9.249, -0.438)", p<0.0001 with effect size -0.438, interpreting that concise data "contains less noise from extraneous details."

> "Length of Excerpt < 0.0001 **** (-9.249, -0.438) The shorter the excerpt to code, the higher the initial accuracy of automated coding."

### Jeongyeon Kim and John Mitchell 2026 (3)

Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109

`q2 · i1` · `associational · r2`

Same mixed-effects analysis, using a Word Difficulty Score based on COCA inverse word frequency to measure specialization. The gap metric reached "(-7.629, -0.331)", p<0.0001 with effect size -0.331; the article attributes the effect to failed text alignment between technical and lay language.

> "Gap of Degree of Specialization Between Codebook and Excerpt < 0.0001 **** (-7.629, -0.331) The smaller the gap of degree of specialization between codebook and excerpt to code, the higher the initial accuracy of automated coding."

## Discussion


## Related Claims
- [Cosine similarity has opposing effects on LLM coding accuracy: lower similarity within codebooks helps, higher similarity within excerpts helps](claim-opposing-cosine-similarity-codebook-excerpt.md) — related
