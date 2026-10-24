---
type: claim
title: Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models
description: Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models
id: higher-bit-quantisation-preserves-semantic-structure-pidgin-llm
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: nwogo-2026
    resource: "https://doi.org/10.48550/arxiv.2608.15738"
    title: "Nwogo, E. U., Ihianle, I. K., Machado, P., Bird, J. J., Lotfi, A., Shuaib, A. A., Akinwumi, I. I., & Oluranti, J. (2026). An AI-Based Adaptive Learning Platform for Multilingual and Low-Resource Educational Contexts: A Case Study on Nigeria. arXiv. https://arxiv.org/abs/2608.15738 [doi:10.48550/arxiv.2608.15738](https://doi.org/10.48550/arxiv.2608.15738)"
    author: "Nwogo, E. U., Ihianle, I. K., Machado, P., Bird, J. J., Lotfi, A., Shuaib, A. A., Akinwumi, I. I., & Oluranti, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Among the fine-tuned quantised models, LLM-Q8 achieved the highest ROUGE-L (0.3120) and BERTScore (0.8590), indicating better structural coherence and semantic preservation than lower-bit models. [→ Nwogo 2026](#nwogo-2026)

## Evidence

### Nwogo 2026

Nwogo, E. U., Ihianle, I. K., Machado, P., Bird, J. J., Lotfi, A., Shuaib, A. A., Akinwumi, I. I., & Oluranti, J. (2026). An AI-Based Adaptive Learning Platform for Multilingual and Low-Resource Educational Contexts: A Case Study on Nigeria. arXiv. https://arxiv.org/abs/2608.15738 [doi:10.48550/arxiv.2608.15738](https://doi.org/10.48550/arxiv.2608.15738)

`q2 · i?` · `design · r2`

Automatic semantic evaluation of three fine-tuned, quantised LLMs (Q4, Q5, Q8) on 14 science prompts with gpt-4o outputs as references. LLM-Q8 "achieved the highest ROUGE-L score (0.3120)" and the highest BERTScore (0.8590) in Table 1; BLEU was uniformly low (0.0120–0.0121).

> "However, higher-bit quantisation (LLM-Q8) achieved the highest ROUGE-L score (0.3120), suggesting that in- creased numerical precision better preserves structural co- herence and sentence-level flow."

## Discussion


## Related Claims
- [The OpenAI gpt-4o reference model outperformed all quantised models on human-rated coherence, fluency, relevance and cultural appropriateness, serving as an upper benchmark](gpt-4o-reference-outperformed-quantised-models-human-ratings.md) — related
- [Native speakers rated outputs of LLMs fine-tuned on Nigerian Pidgin English as understandable and context-aware, though no non-fine-tuned baseline was evaluated](pidgin-fine-tuning-improves-linguistic-alignment.md) — related
- [A 4-bit quantized 27B local Teacher LLM generated knowledge in the required format, suggesting accessible-resource implementations may be feasible](quantized-local-teacher-llm-feasible.md) — related
- [Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)](manova-cluster-effect-text-metrics.md) — related
- [Hallucination rate increases under 4-bit quantization and is substantially mitigated by quantization-aware fine-tuning](quantization-raises-hallucination-rate-finetuning-mitigates.md) — related
