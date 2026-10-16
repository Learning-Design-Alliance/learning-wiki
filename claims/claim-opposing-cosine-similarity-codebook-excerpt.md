---
type: claim
title: "Cosine similarity has opposing effects on LLM coding accuracy: lower similarity within codebooks helps, higher similarity within excerpts helps"
description: "Cosine similarity has opposing effects on LLM coding accuracy: lower similarity within codebooks helps, higher similarity within excerpts helps"
id: claim-opposing-cosine-similarity-codebook-excerpt
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jeongyeon-kim-and-john-mitchell-2026
    resource: "https://doi.org/10.48550/arxiv.2609.11109"
    title: "Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109 [doi:10.48550/arxiv.2609.11109](https://doi.org/10.48550/arxiv.2609.11109)"
    author: Jeongyeon Kim and John Mitchell
    q: 2
    i: 1
    kind: design
    rigour: 2
  - id: jeongyeon-kim-and-john-mitchell-2026-2
    resource: "https://arxiv.org/abs/2609.11109"
    title: "Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109"
    author: Jeongyeon Kim and John Mitchell
    q: 2
    i: 1
    kind: design
    rigour: 2
---

# Cosine similarity has opposing effects on LLM coding accuracy: lower similarity within codebooks helps, higher similarity within excerpts helps

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2` · `i1` small

## Subclaims
`q2 i1` Higher cosine similarity within the codebook negatively affects initial coding accuracy (effect size -0.276, p<0.0001). [→ Jeongyeon Kim and John Mitchell 2026](#jeongyeon-kim-and-john-mitchell-2026)
`q2 i1` Higher cosine similarity within the excerpt positively affects initial coding accuracy (effect size 0.189, p<0.0001). [→ Jeongyeon Kim and John Mitchell 2026 (2)](#jeongyeon-kim-and-john-mitchell-2026-2)

## Evidence

### Jeongyeon Kim and John Mitchell 2026

Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109 [doi:10.48550/arxiv.2609.11109](https://doi.org/10.48550/arxiv.2609.11109)

`q2 · i1` · `design · r2`

Mixed-effects analysis of dataset characteristics across the four datasets. The codebook-similarity row reports "(-11.738, -0.276)", p<0.0001 with effect size -0.276; the article interprets that varied codebook language aids contextual understanding of the code.

> "Cosine Similarity of Codebook < 0.0001 **** (-11.738, -0.276) The less similar the semantics of words in each codebook, the higher the initial accuracy of automated coding."

### Jeongyeon Kim and John Mitchell 2026 (2)

Jeongyeon Kim and John Mitchell. (2026). How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding. arXiv. https://arxiv.org/abs/2609.11109

`q2 · i1` · `design · r2`

Same mixed-effects analysis. The excerpt-similarity row reports "(7.372, 0.189)", p<0.0001 with effect size 0.189; the article concludes "coding accuracy improves when codebooks employ diverse language while the target data remains consistent."

> "Cosine Similarity of Excerpt < 0.0001 **** (7.372, 0.189) The more similar the semantics of words in excerpt to code, the higher the initial accuracy of automated coding."

## Discussion


## Related Claims
- [Shorter codebooks and shorter data excerpts yield higher initial LLM coding accuracy, and a smaller specialization gap between codebook and excerpt helps](claim-llm-coding-accuracy-shorter-codebooks.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
