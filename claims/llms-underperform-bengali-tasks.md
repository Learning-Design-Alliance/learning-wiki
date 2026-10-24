---
type: claim
title: General-purpose large language models perform substantially worse on Bengali downstream tasks than on equivalent English tasks, with gaps consistent with data-volume explanations
description: General-purpose large language models perform substantially worse on Bengali downstream tasks than on equivalent English tasks, with gaps consistent with data-volume explanations
id: llms-underperform-bengali-tasks
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: avijit-roy-2026
    resource: "https://doi.org/10.48550/arxiv.2608.12278"
    title: "Avijit Roy, Proma Roy. (2026). Structural Silence: When AI Infrastructure Fails Speakers of Underrepresented Languages — A Case Study in Bengali, the Digital Divide, and the Hidden Cost of English-Centric Design. arXiv preprint. https://arxiv.org/abs/2608.12278 [doi:10.48550/arxiv.2608.12278](https://doi.org/10.48550/arxiv.2608.12278)"
    author: Avijit Roy, Proma Roy
    q: 2
    i: "?"
    kind: review
    rigour: 2
---

# General-purpose large language models perform substantially worse on Bengali downstream tasks than on equivalent English tasks, with gaps consistent with data-volume explanations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Benchmark evaluations including BenLLM-Eval and a 2025 evaluation of ten open-source LLMs show Bengali performance lower across model families than equivalent English performance. [→ Avijit Roy 2026](#avijit-roy-2026)

## Evidence

### Avijit Roy 2026

Avijit Roy, Proma Roy. (2026). Structural Silence: When AI Infrastructure Fails Speakers of Underrepresented Languages — A Case Study in Bengali, the Digital Divide, and the Hidden Cost of English-Centric Design. arXiv preprint. https://arxiv.org/abs/2608.12278 [doi:10.48550/arxiv.2608.12278](https://doi.org/10.48550/arxiv.2608.12278)

`q2 · i?` · `review · r2`

Review of published benchmark evaluations (BenLLM-Eval, Kabir et al. 2024; Bhowmik et al. 2025, a ten-model Bengali/English comparison). The review reports consistent performance gaps relative to English equivalents; no effect sizes are printed in this article.

> "A 2025 evaluation of ten open-source LLMs across Bengali and English benchmarks likewise showed that Bengali performance was lower across model families, particularly for smaller models like Mistral, and that the gaps correlated with tokenization efficiency and model scale."

## Discussion


## Related Claims

- [Bengali's alphasyllabary script incurs a tokenization penalty: elevated token fertility fragments linguistic units and compounds the training data deficit](bengali-tokenization-penalty-fertility.md) — related
- [Individual internet penetration in rural Bangladesh (36.5%) is about half the urban rate (71.4%), which one case-study preprint argues puts cloud-dependent AI tools out of reach for rural learners](rural-urban-connectivity-exclusion-bangladesh.md)
