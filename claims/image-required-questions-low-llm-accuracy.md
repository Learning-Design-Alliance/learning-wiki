---
type: claim
title: "GPT-4o accuracy on image-required FCI questions (36–38%) is substantially weaker than on text-only and image-optional questions (97–100%)"
description: "GPT-4o accuracy on image-required FCI questions (36–38%) is substantially weaker than on text-only and image-optional questions (97–100%)"
id: image-required-questions-low-llm-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: marina-babayeva-2025
    resource: "https://doi.org/10.21203/rs.3.rs-7410179/v1"
    title: "Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)"
    author: Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o accuracy on image-required FCI questions (36–38%) is substantially weaker than on text-only and image-optional questions (97–100%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across translated, back-translated, and English versions, text-only and image-optional questions were solved at 97–100% accuracy while image-required questions dropped to 36–38% for GPT-4o and 56% for GPT-o1. [→ Marina Babayeva 2025](#marina-babayeva-2025)

## Evidence

### Marina Babayeva 2025

Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)

`q2 · i?` · `design · r2`

Performance breakdown by the study's own question categories (10 text-only, 9 image-optional, 11 image-required) across all language versions and English baselines in Table 2. The authors call this "a significant discrepancy between the model's proficiency in solving text versus image problems."

> "While text-only and image-optional questions were solved with high accuracy (97–100%), performance on image-required questions was considerably lower. For example, GPT-4o's accuracy on image-required questions hovered around 36–38%, whereas GPT-o1 showed improved visual reasoning at 56%."

## Discussion


## Related Claims
- [GPT-4o scores 75% on LLM-translated FCI versions across 53 languages, 76% on back-translations, and 77% in English, with GPT-o1 reaching 84% in English](fci-gpt4o-translation-overall-accuracy.md) — related
- [GPT-4o answered only 59% of pre-test questions correctly, with accuracy dropping sharply as the number of images per question increased](gpt4o-fci-accuracy-drops-with-images.md) — related
- [ChatGPT's accuracy on image-based MCQs ranged from 13.1% to 100% across studies, and it performed significantly worse on open-ended questions than on MCQs](image-mcq-and-open-ended-question-performance.md) — related
- [GPT-4o performs far worse on items requiring image interpretation (49%) than on text-only items (81%)](gpt4o-required-image-items-weaker.md) — a broader claim this one bears on
