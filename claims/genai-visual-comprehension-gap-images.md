---
type: claim
title: Generative AI excels at processing digital text but struggles with interpreting text from images
description: Generative AI excels at processing digital text but struggles with interpreting text from images
id: genai-visual-comprehension-gap-images
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: taira-k-2025
    resource: "https://doi.org/10.2196/67197"
    title: "Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197"
    author: Taira K, Itaya T, Yada S, Hiyama K, Hanada A.
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# Generative AI excels at processing digital text but struggles with interpreting text from images

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q1 i?` JPG's poor performance (26% median) highlights a limitation in visual comprehension of text from images. [→ Taira K 2025](#taira-k-2025)

## Evidence

### Taira K 2025

Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197

`q1 · i?` · `causal · r2`

The authors' interpretation of their benchmark result, reported in the discussion: "JPG’s poor performance highlights a significant limitation of generative AI" regarding text in images. This is an author-level explanation of the 26% median, not an independently tested mechanism.

> "JPG’s poor performance highlights a significant limitation of generative AI, which excels at processing digital text but struggles with interpreting text from images."

## Discussion


## Related Claims
- [ChatGPT-4's performance on the Japanese National Nursing Examination differs by attached file format, with JPG (26% median) far below text-based formats (87%-94% medians)](file-format-affects-chatgpt-nursing-exam-performance.md) — related
- [ChatGPT performs poorly on image-based data interpretation across DNA footprinting and BLI questions regardless of image detail](chatgpt-poor-image-inference-scientific-graphs.md) — related
- [All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions](llm-visual-question-decline-jneot.md) — a broader claim this one bears on
- [All evaluated models struggle with spatial reasoning and precise visual replication on Turtle Graphics tasks](vlms-struggle-spatial-reasoning-visual-precision.md) — related
