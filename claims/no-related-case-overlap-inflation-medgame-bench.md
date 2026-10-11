---
type: claim
title: Related-case overlap between MedGame Bench train and test splits shows no significant performance difference
description: Related-case overlap between MedGame Bench train and test splits shows no significant performance difference
id: no-related-case-overlap-inflation-medgame-bench
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: qian-wu-2026
    resource: "https://arxiv.org/abs/2607.21570"
    title: "Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570"
    author: Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Related-case overlap between MedGame Bench train and test splits shows no significant performance difference

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Test cases with and without similar patient variants in the training split showed no significant performance difference (p > 0.05); equivalence was not tested. [→ Qian Wu 2026](#qian-wu-2026)

## Evidence

### Qian Wu 2026

Qian Wu, Xinrong Zhou, Zizhan Ma, Kai Chen, Zheyao Gao, Xun Lin, Hongqiu Wu, Longfei Gou, Yixiao Liu, Ann Sin Nga Lau, Qi Dou. (2026). MedGame: Storytelling Gamification Empowered by Large Language Models for Medical Education. arXiv preprint. https://arxiv.org/abs/2607.21570

`q2 · i?` · `design · r2`

Secondary analysis tracking high-similarity patient variants across the benchmark split (409 of 1,000 test cases had a similar variant in train). The article reports no significant difference and "no evidence of score inflation from related cases"; no effect size printed.

> "Test cases with and without similar patient variants in the training split show no significant perfor- mance difference (p >0.05; Appendix E.4), pro- vidingno evidence of score inflation from related cases."

## Discussion


## Related Claims
- [Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models](fine-tuning-improves-open-source-llms-medgame-bench.md) — related
- [Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics](commercial-models-outperform-open-source-medgame-baseline.md) — related
