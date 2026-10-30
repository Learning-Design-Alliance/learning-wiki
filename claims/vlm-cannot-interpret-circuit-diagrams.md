---
type: claim
title: State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems
description: State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems
id: vlm-cannot-interpret-circuit-diagrams
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: liangliang-chen-2025
    resource: "https://doi.org/10.1007/s40593-025-00501-w"
    title: "Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang. (2025). Benchmarking Large Language Models on Homework Assessment in Circuit Analysis. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00501-w"
    author: Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# State-of-the-art multimodal LLMs cannot reliably interpret circuit diagrams and therefore cannot independently solve circuit analysis problems

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o cannot interpret circuit diagrams reliably, hallucinating non-existing elements and giving dubious connection explanations, and consequently cannot solve provided circuit analysis problems whose statements include diagrams. [→ Liangliang Chen 2025](#liangliang-chen-2025)

## Evidence

### Liangliang Chen 2025

Liangliang Chen, Zhihao Qin, Yiming Guo, Jacqueline Rohde, Ying Zhang. (2025). Benchmarking Large Language Models on Homework Assessment in Circuit Analysis. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00501-w

`q2 · i?` · `design · r2`

Demonstration examples in the limitations section: when asked to list elements and connections in a circuit diagram, GPT-4o "mistakenly lists a non-existing resistor due to hallucinations," and a full solve attempt produced an incorrect answer.

> "This example demonstrates that GPT-4o cannot solve a provided circuit analysis problem, which is expected since GPT-4o cannot even understand the associated circuit diagram. However, we note that GPT-4o does recognize that KCL should be applied to different nodes."

## Discussion


## Related Claims
- [GPT-4o frequently makes characteristic errors in homework assessment, including failing to recognize unit and numeric equivalences, marking complete solutions incomplete, and mishandling alternative methods and notations](gpt4o-characteristic-assessment-error-types.md) — related
- [Current AI tutoring systems misinterpret complex STEM engineering diagrams, omitting edges, misclassifying component connections, and flattening hierarchical topologies](ai-systems-misinterpret-stem-diagrams.md) — a broader claim this one bears on
- [An LLM debugging assistant correctly interprets brief, informal natural-language prompts describing circuits](llm-handles-natural-language-circuit-prompts.md) — related
- [An LLM debugging assistant provides accurate, detailed descriptions of circuit components and their proper connections](llm-provides-accurate-hardware-information.md) — related
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — related
- [GPT-4o and Llama 3 70B significantly outperform GPT-3.5 Turbo across all five homework-assessment metrics in circuit analysis](gpt4o-llama3-outperform-gpt35-circuit-homework-assessment.md) — related
- [StructRAG achieves 89.3% question-level accuracy and 93.0% edge-level F1 on 1,650 STEM diagram questions, outperforming OCR+CV, GPT-4 graph-only, direct-image GPT-4o, and ablated variants](structrag-outperforms-baselines-stem-diagrams.md) — related
