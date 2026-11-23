---
type: strategy
id: hybrid-llm-human-translation-strategy
title: Hybrid LLM translation with human-in-the-loop expert validation for onboarding documentation
description: "The article's translation workflow combines automated and human steps: a locally deployed LLM generates initial translations, a RAG glossary supplies terminology anchors, and native Chinese-speaking physicists validat..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: morris-2026
    resource: "https://arxiv.org/abs/2609.35830"
    title: "Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. https://arxiv.org/abs/2609.35830"
    author: Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X
---

# Hybrid LLM translation with human-in-the-loop expert validation for onboarding documentation

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (5 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article's translation workflow combines automated and human steps: a locally deployed LLM generates initial translations, a RAG glossary supplies terminology anchors, and native Chinese-speaking physicists validate and refine the output "to eliminate potential machine-generated hallucinations or errors". The strategy is meant to guarantee semantic accuracy while avoiding the labor cost of purely manual translation, without adding a bottleneck to content changes. It enabled the Mandarin Starterkit and a sibling workshop event in China.

## Design Implications

### Context
#### Requirements
- verified bilingual terminology glossary compiled and checked by bilingual collaboration members
- native-speaking domain experts for post-editing every document before it goes live
#### Constraints
- raw vanilla LLM output alone was unacceptable, with ~20% of sentences needing manual correction

### Target Learners
- LHCb collaborators reading onboarding documentation in Mandarin Chinese

### Target Learning Goals
- accessible onboarding of newcomers to LHCb software across language communities

## Claims

- [Roughly 22% of visits to the LHCb Starterkit website access at least one Chinese-language page](../claims/22-percent-visits-chinese-language-pages.md) [+W]
- [Qwen3.5-35B-A3B offered the best throughput and memory balance of three open-source LLMs benchmarked on consumer-grade hardware for translation](../claims/qwen-selected-optimal-throughput-memory-balance.md) [+W]
- [A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%](../claims/rag-llm-translation-accuracy-above-95-percent.md) [+W]
- [The Run 3 Starterkit receives about 30 visits per day, of which about 6.7 access at least one Chinese-language page](../claims/run3-starterkit-daily-visits-chinese-subset.md) [+W]
- [Retrieval-augmented generation grounding achieves near-perfect correctness compared to untuned LLM baseline](../claims/rag-grounding-near-perfect-correctness.md) [+W]
- [The systems established are extensible to other regions, with Brazil noted as a possible sibling-event site](../claims/sibling-workshop-extensibility-brazil.md) [~W]

## Related Strategies

- [Use independent expert physician review as a governance safeguard before deploying LLM-generated questions to learners](expert-physician-review-governance.md)
- [Expert-in-the-loop pipeline for generating and refining educational content with LLMs](expert-in-loop-llm-education-pipeline.md)
- [Four-step LLM-assisted workflow for producing attested ancient-language sentences](llm-postedit-attestation-workflow.md)

## Examples
-

## Key Sources
- Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. https://arxiv.org/abs/2609.35830. [doi:10.48550/arxiv.2609.35830](https://doi.org/10.48550/arxiv.2609.35830)
