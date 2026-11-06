---
type: claim
title: CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks
description: CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks
id: cot-few-shot-efficient-alternative
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: altermatt-fernando-r-2025
    resource: "https://doi.org/10.1186/s12909-025-07250-3"
    title: "Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3"
    author: Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J.
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# CoT + few-shot prompting delivers high accuracy with minimal computational overhead, offering an efficient alternative to multi-agent frameworks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The CoT + few-shot configuration reached 87.67% accuracy (SD = 0.12%) with a single API call and about 1.74 seconds per query. [→ Altermatt Fernando R. 2025](#altermatt-fernando-r-2025)

## Evidence

### Altermatt Fernando R. 2025

Altermatt Fernando R., Neyem Andres, Sumonte Nicolas, Mendoza Marcelo, Villagran Ignacio, Lacassie Hector J. (2025). Performance of single-agent and multi-agent language models in Spanish language medical competency exams. BMC Medical Education. https://doi.org/10.1186/s12909-025-07250-3

`q2 · i?` · `causal · r1`

Results from the same automated EUNACOM evaluation (Table 1) show CoT + few-shot at 87.67% ± 0.12% with 1.00 API call and 1.74 s, versus MDAGENTS at 21.14 API calls and 192.44 s. The article calls it "an optimal balance between performance and efficiency".

> "CoT + few-shot combined strong accuracy (87.67%, SD = 0.12%) with minimal computational overhead, representing an optimal balance between performance and efficiency."

## Discussion


## Related Claims
- [Multi-agent strategies incur substantially higher computational costs than single-agent methods on EUNACOM evaluation](multiagent-computational-cost-tradeoff.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [In-context learning did not consistently improve LLM annotation reliability over zero-shot prompting for engagement coding](icl-no-better-than-zero-shot-engagement-coding.md) — related
- [Few-shot chain-of-thought prompting outperforms zero-shot prompting for detecting teacher questions](few-shot-cot-outperforms-zero-shot-question-detection.md) — related
- [GPT-4 outperforms GPT-3.5-turbo in a single-lesson question-detection test](gpt4-outperforms-gpt35-single-lesson.md) — related
- [Few-shot LLM approaches outperform standalone supervised ML approaches, yet hand-crafted rules remain relevant](few-shot-llm-outperforms-ml-hcr-relevant.md) — related
- [Chain-of-thought prompting yields higher-quality GenAI feedback on argumentative essays than Zero-shot prompting and teacher feedback](cot-prompting-higher-feedback-quality-than-zero-shot-and-teacher.md) — related
- [Few-shot with chain-of-thought prompting achieves the best concordance with human expert ratings for all tested LLMs](few-shot-cot-best-concordance-human-experts.md) — related
- [MDAGENTS achieves the highest accuracy on Spanish-language EUNACOM questions, outperforming all other evaluated strategies](mdagents-highest-accuracy-eunacom.md) — related
