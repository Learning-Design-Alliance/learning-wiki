---
type: claim
title: Higher-struggling-level problems elicit more diverse but less student-like LLM-generated errors
description: Higher-struggling-level problems elicit more diverse but less student-like LLM-generated errors
id: higher-struggling-problems-elicit-more-diverse-less-student-like-errors
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ali-keramati-2026
    resource: "https://doi.org/10.48550/arxiv.2606.14113"
    title: "Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113 [doi:10.48550/arxiv.2606.14113](https://doi.org/10.48550/arxiv.2606.14113)"
    author: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ali-keramati-2026-2
    resource: "https://arxiv.org/abs/2606.14113"
    title: "Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113"
    author: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Higher-struggling-level problems elicit more diverse but less student-like LLM-generated errors

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Mean edit distances among LLM submissions increased substantially from low- to medium-struggling problems and remained high at high-struggling problems, indicating harder problems elicit more heterogeneous erroneous outputs. [→ Ali Keramati 2026](#ali-keramati-2026)
`q2 i?` As struggling level increases, mean nearest edit distance to human code also increases, indicating LLMs find it harder to reproduce student-like logical errors on higher-struggle problems. [→ Ali Keramati 2026 (2)](#ali-keramati-2026-2)

## Evidence

### Ali Keramati 2026

Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113 [doi:10.48550/arxiv.2606.14113](https://doi.org/10.48550/arxiv.2606.14113)

`q2 · i?` · `design · r2`

Figure-based comparison of diversity across three struggling levels (Low avg. 1,187 submissions, Medium avg. 2,049, High avg. 4,125). Example: Gemini 2.5 Pro (CoT) rose from 62.34 (low) to 82.89 (medium) and stayed high at 74.59 (high).

> "mean edit distances among LLM submissions increased substan- tially from low- to medium-struggling problems, and re- mained high at high-struggling problems for most models"

### Ali Keramati 2026 (2)

Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113

`q2 · i?` · `design · r2`

Figure 4 analysis of simulated-human alignment across struggling levels. Claude Sonnet 4 was most stable with slightly longer distances as struggle increased; GPT-5 and Gemini 2.5 Pro showed substantial increases at medium and high levels.

> "as the level of struggle increases, the mean near- est edit distance also increases, indicating that LLMs find it harder to reproduce student-like logical errors on higher- struggle problems"

## Discussion


## Related Claims
- [LLM-generated erroneous code aligns with authentic student errors at levels that depend on model and prompting strategy, with Claude Sonnet 4 most consistently aligned](llm-error-alignment-depends-on-model-and-prompting-strategy.md) — related
- [LLMs across five models generate diverse erroneous Java code, with mean AST edit distances varying by model and prompting strategy](llms-generate-diverse-erroneous-java-code-varying-by-model-and-prompt.md) — related
