---
type: claim
title: All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions
description: All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions
id: llm-visual-question-decline-jneot
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: saita-kazuya-2026
    resource: "https://doi.org/10.1186/s12909-025-08542-4"
    title: "Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4"
    author: Saita Kazuya, Mine Yuichi, Amano Satoru
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: saita-kazuya-2026-2
    resource: "https://doi.org/10.1186/s12909-025-08542-4"
    title: "Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4"
    author: Saita Kazuya, Mine Yuichi, Amano Satoru
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: saita-kazuya-2026-3
    resource: "https://doi.org/10.1186/s12909-025-08542-4"
    title: "Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4"
    author: Saita Kazuya, Mine Yuichi, Amano Satoru
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Correct response rates on visually-based questions (50.0-68.2%) fall well below text-only rates (86.4-93.8%) across all four models. [→ Saita Kazuya 2026](#saita-kazuya-2026)

## Evidence

### Saita Kazuya 2026

Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4

`q2 · i?` · `design · r2`

Benchmarking of the full 199-item 60th JNEOT against official answer keys; text-only correct response rates were "Gemini 2.5 answered 93.8% of the items correctly, OpenAI o3 91.5%, GPT-4.5 87.0%, and Claude 3.7 86.4%".

> "When the input was text-only, the correct response rate was high for all models (Tables 2 and 3): Gemini 2.5 answered 93.8% of the items correctly, OpenAI o3 91.5%, GPT-4.5 87.0%, and Claude 3.7 86.4%."

### Saita Kazuya 2026 (2)

Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4

`q2 · i?` · `associational · r2`

Descriptive comparison of the same benchmark's visually-based subscores in the Results section: "a general decrease of 23-36% points when image interpretation was required". No standardized effect size is printed.

> "The figures show a general decrease of 23-36% points when image interpretation was required."

### Saita Kazuya 2026 (3)

Saita Kazuya, Mine Yuichi, Amano Satoru. (2026). What the performance of multimodal LLMs on a national licensing exam teaches us about occupational therapy education. BMC Medical Education. https://doi.org/10.1186/s12909-025-08542-4

`q2 · i?` · `associational · r2`

The authors' summary of the format effect: "accuracy on visual-based questions decreased by 26-36% compared to text-based questions across all models". Only percentage-point declines are reported; no standardized effect size is printed.

> "Performance declined significantly when visual information processing was required; accuracy on visual-based questions decreased by 26-36% compared to text-based questions across all models."

## Discussion


## Related Claims
- [Gemini 2.5 significantly outperformed GPT-4.5 and Claude 3.7 on overall JNEOT accuracy, with Gemini 2.5 highest at 91.0%](gemini-outperformed-gpt45-claude37-jneot.md) — related
- [No significant inter-model differences in accuracy on visually-based JNEOT questions](no-intermodel-differences-visual-questions.md) — related
- [Ten JNEOT questions were answered incorrectly by all four LLMs, six of them visually-based](ten-questions-incorrect-by-all-llms.md) — related
- [LLM errors on multimodal physics problems fall into four categories, with visual processing errors most prevalent, and error type distribution does not differ significantly across models](four-category-llm-multimodal-error-taxonomy.md) — related
- [The Multimodal Interference Effect: mapping visual representations to physical concepts degrades LLM performance even on non-visual problem aspects](multimodal-interference-effect-llms.md) — related
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — reports the opposite
