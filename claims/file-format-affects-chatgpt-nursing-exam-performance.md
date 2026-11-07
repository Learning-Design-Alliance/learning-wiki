---
type: claim
title: "ChatGPT-4's performance on the Japanese National Nursing Examination differs by attached file format, with JPG (26% median) far below text-based formats (87%-94% medians)"
description: "ChatGPT-4's performance on the Japanese National Nursing Examination differs by attached file format, with JPG (26% median) far below text-based formats (87%-94% medians)"
id: file-format-affects-chatgpt-nursing-exam-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: taira-k-2025
    resource: "https://doi.org/10.2196/67197"
    title: "Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197"
    author: Taira K, Itaya T, Yada S, Hiyama K, Hanada A.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: taira-k-2025-2
    resource: "https://doi.org/10.2196/67197"
    title: "Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197"
    author: Taira K, Itaya T, Yada S, Hiyama K, Hanada A.
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# ChatGPT-4's performance on the Japanese National Nursing Examination differs by attached file format, with JPG (26% median) far below text-based formats (87%-94% medians)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Median percentages of correct answers ranged from 26% with JPG attachment to 94% with PDF, with PROMPT-ONLY at 92%, TEXT at 92%, and DOCX at 87%. [→ Taira K 2025](#taira-k-2025)
`q2 i?` Differences between attached formats were statistically significant in all pairs (P<.01) except PROMPT-ONLY versus TEXT and PROMPT-ONLY versus DOCX. [→ Taira K 2025 (2)](#taira-k-2025-2)

## Evidence

### Taira K 2025

Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197

`q2 · i?` · `causal · r2`

Benchmark evaluation of the unmodified gpt-4-1106-preview model on the 2023 Japanese National Nursing Examination, with each of five file formats processed for 100 iterations. The results section reports the printed medians, including "94% (IQR 94%‐96%)" for PDF and "26% (IQR 20%‐30%)" for JPG.

> "The median percentages of correct answers were 92% (IQR 64%‐94%), 92% (IQR 92%‐94%), 94% (IQR 94%‐96%), 87% (IQR 86%‐90%), and 26% (IQR 20%‐30%) for PROMPT-ONLY, TEXT, PDF, DOCX, and JPG formats, respectively."

### Taira K 2025 (2)

Taira K, Itaya T, Yada S, Hiyama K, Hanada A. (2025). Impact of Attached File Formats on the Performance of ChatGPT-4 on the Japanese National Nursing Examination: Evaluation Study. JMIR Nursing. https://doi.org/10.2196/67197

`q2 · i?` · `causal · r2`

Kruskal-Wallis test with Dann-Bonferroni post hoc comparisons across the five format conditions in the same 100-iteration-per-format evaluation. The study reports "statistically significant in all pairs (P<.01)" except the two named pairs.

> "The differences between the attached formats were statistically significant in all pairs (P<.01) except for the PROMPT-ONLY versus TEXT and PROMPT-ONLY versus DOCX pairs (Figure 1)."

## Discussion


## Related Claims
- [Generative AI excels at processing digital text but struggles with interpreting text from images](genai-visual-comprehension-gap-images.md) — related
- [All four multimodal LLMs show a marked decrease in correct response rates on visually-based versus text-only JNEOT questions](llm-visual-question-decline-jneot.md) — related
- [The PROMPT-ONLY format showed more variable performance than TEXT, PDF, and DOCX formats in ChatGPT-4's examination responses](prompt-only-format-more-variable.md) — a narrower finding that bears on this claim
- [ChatGPT models achieve a pooled accuracy of 70.1% on national health licensing examinations](chatgpt-pooled-accuracy-70-percent-licensing-exams.md) — a broader claim this one bears on
