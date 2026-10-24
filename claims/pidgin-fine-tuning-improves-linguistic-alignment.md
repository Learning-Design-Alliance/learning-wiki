---
type: claim
title: "Native speakers rated outputs of LLMs fine-tuned on Nigerian Pidgin English as understandable and context-aware, though no non-fine-tuned baseline was evaluated"
description: "Native speakers rated outputs of LLMs fine-tuned on Nigerian Pidgin English as understandable and context-aware, though no non-fine-tuned baseline was evaluated"
id: pidgin-fine-tuning-improves-linguistic-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
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

# Native speakers rated outputs of LLMs fine-tuned on Nigerian Pidgin English as understandable and context-aware, though no non-fine-tuned baseline was evaluated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` Bilingual English–Pidgin speakers consistently rated outputs from the fine-tuned models as understandable and context-aware. The authors read this as improved linguistic alignment relative to non-adapted baselines, but the evaluation compared only three quantisation levels of the fine-tuned model with a GPT-4o reference (which rated highest), with no non-fine-tuned version of the model, so it cannot show that fine-tuning caused the improvement. [→ Nwogo 2026](#nwogo-2026)

## Evidence

### Nwogo 2026

Nwogo, E. U., Ihianle, I. K., Machado, P., Bird, J. J., Lotfi, A., Shuaib, A. A., Akinwumi, I. I., & Oluranti, J. (2026). An AI-Based Adaptive Learning Platform for Multilingual and Low-Resource Educational Contexts: A Case Study on Nigeria. arXiv. https://arxiv.org/abs/2608.15738 [doi:10.48550/arxiv.2608.15738](https://doi.org/10.48550/arxiv.2608.15738)

`q2 · i?` · `design · r2`

Human-centred cultural and linguistic evaluation: a structured survey was distributed to 50 native Nigerian Pidgin speakers via Google Forms, "yielding 18 valid responses", who rated fluency, coherence, relevance and cultural appropriateness on a five-point Likert scale. Responses to 14 prompts came from the fine-tuned model at three quantisation levels (Q4, Q5, Q8) and from OpenAI GPT-4o as a reference; no non-fine-tuned model was rated, so the comparison in the authors' sentence below was not tested.

> "Across responses, participants consistently rated outputs from the fine-tuned models as understandable and context- aware, confirming that fine-tuning on Nigerian Pidgin data improves linguistic alignment relative to non-adapted base- lines."

## Discussion


## Related Claims
- [Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models](higher-bit-quantisation-preserves-semantic-structure-pidgin-llm.md) — related
- [Prompting experiments show LLMs perform badly at generating non-US national standard varieties and conflate Nigerian English with Nigerian Pidgin](llms-perform-badly-non-us-standard-varieties.md) — related
- [Automated grading systems may produce systematically inequitable outcomes for international and non-Western students](automated-grading-bias-non-native-english.md) — related
- [Current LLMs reproduce linguistic hierarchies by being built on dominant standard English varieties, producing a monolithic English that ignores regional variation](llms-reproduce-linguistic-hierarchies-monolithic-english.md) — related
- [The OpenAI gpt-4o reference model outperformed all quantised models on human-rated coherence, fluency, relevance and cultural appropriateness, serving as an upper benchmark](gpt-4o-reference-outperformed-quantised-models-human-ratings.md) — related
- [In the fine-tuning experiments, increasing base model size up to 32B parameters improved performance, and larger LLMs consistently outperformed smaller MLMs](model-size-and-llm-vs-mlm-performance-vocabulary-difficulty.md) — related
