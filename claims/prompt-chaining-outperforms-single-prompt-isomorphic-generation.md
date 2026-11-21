---
type: claim
title: Prompt-chaining produces higher quality and more consistent isomorphic physics problems than single-prompt or simple-prompt generation
description: Prompt-chaining produces higher quality and more consistent isomorphic physics problems than single-prompt or simple-prompt generation
id: prompt-chaining-outperforms-single-prompt-isomorphic-generation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: zhongzhou-chen-2025
    resource: "https://doi.org/10.48550/arXiv.2508.14755"
    title: "Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)"
    author: Zhongzhou Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhongzhou-chen-2025-2
    resource: "https://doi.org/10.48550/arXiv.2508.14755"
    title: "Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)"
    author: Zhongzhou Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: zhongzhou-chen-2025-3
    resource: "https://doi.org/10.48550/arXiv.2508.14755"
    title: "Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)"
    author: Zhongzhou Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompt-chaining produces higher quality and more consistent isomorphic physics problems than single-prompt or simple-prompt generation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under a single-prompt condition, all 10 generated versions neglected the instruction to generate numerical values for variables despite explicit instruction. [→ Zhongzhou Chen 2025](#zhongzhou-chen-2025)
`q2 i?` Under a simple-prompt condition, ChatGPT hallucinated the answer without initiating python tool-use, and most of the problem answers were incorrect. [→ Zhongzhou Chen 2025 (2)](#zhongzhou-chen-2025-2)
`q2 i?` Under the one-prompt condition for the diagram bank, the LLM generated only 7 scenarios and 13 combinations instead of the intended 10 scenarios and 26 combinations, and produced diagrams with an underground trajectory. [→ Zhongzhou Chen 2025 (3)](#zhongzhou-chen-2025-3)

## Evidence

### Zhongzhou Chen 2025

Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)

`q2 · i?` · `design · r2`

Comparison test reported in the Results section: a single prompt containing the same information as the chain was used for problem bank 1, and the article reports that "All 10 versions generated had no numerical values associated with them."

> "The most significant shortfall of the single prompt output is that it completely neglected the instruction for generating numerical values for variables despite explicit instruction. All 10 versions generated had no numerical values associated with them."

### Zhongzhou Chen 2025 (2)

Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)

`q2 · i?` · `design · r2`

Simple-prompt test case for problem bank 1, designed to mimic a naive instructor approach; the article reports ChatGPT "hallucinated the answer without initiating python tool -use" and that most answers were incorrect.

> "The main issue with this generation is that the correct answer should be 1 48.6 kg, ChatGPT simply hallucinated the answer without initiating python tool -use. Most of the problem answers were incorrect."

### Zhongzhou Chen 2025 (3)

Zhongzhou Chen. (2025). Reliable generation of isomorphic physics problems using Generative AI with prompt-chaining and tool use. [doi:10.48550/arXiv.2508.14755](https://doi.org/10.48550/arXiv.2508.14755)

`q2 · i?` · `design · r2`

One-prompt condition for problem bank 2, shown in Figure 2; diagrams had one trajectory underground and one invisible, and the article states instruction-following was "significantly compromised" under this condition.

> "the LLM somehow generated only 7 scenarios and 13 combinations, instead of the 10 scenarios and 26 combinations intended."

## Discussion


## Related Claims
- [Storing intermediate outputs in table format increases the reliability of passing information between prompts in a chain](data-table-intermediate-storage-prompt-chain-reliability.md) — related
- [GenAI services can be used to verify the quality of generated isomorphic problems, identifying and correcting erroneous items](genai-verification-of-generated-item-quality.md) — related
