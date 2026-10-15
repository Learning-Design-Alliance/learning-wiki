---
type: claim
title: LLM-generated erroneous code aligns with authentic student errors at levels that depend on model and prompting strategy, with Claude Sonnet 4 most consistently aligned
description: LLM-generated erroneous code aligns with authentic student errors at levels that depend on model and prompting strategy, with Claude Sonnet 4 most consistently aligned
id: llm-error-alignment-depends-on-model-and-prompting-strategy
status: review
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
    kind: causal
    rigour: 2
---

# LLM-generated erroneous code aligns with authentic student errors at levels that depend on model and prompting strategy, with Claude Sonnet 4 most consistently aligned

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Mean nearest edit distances to human submissions show LLMs can resemble student errors (best 16.35, Claude Sonnet 4 with Self-Refine), but GPT-5 and Gemini 2.5 Pro often exceed 80. [→ Ali Keramati 2026](#ali-keramati-2026)

## Evidence

### Ali Keramati 2026

Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113 [doi:10.48550/arxiv.2606.14113](https://doi.org/10.48550/arxiv.2606.14113)

`q2 · i?` · `causal · r2`

Two-stage structural alignment analysis comparing each LLM-generated error against 74,080 deduplicated human submissions via Jaccard retrieval and Zhang-Shasha tree edit distance. "Claude Sonnet 4 provides the most consistent alignment"; Grok Code Fast 1 achieved the absolute minimum (16.22) with Self-Refine but fluctuated above 30 under IO and CoT.

> "Claude Sonnet 4 provides the most consistent alignment: across all prompting strategies, its distances remain rela- tively low, with the best case (16.35 under Self-refine) be- ing the closest match to real student code among all con- ditions."

## Discussion


## Related Claims
- [Beam search-based self-refinement improves simulated solution alignment with predicted student behavior](beam-search-self-refinement-improves-solution-simulation.md) — related
- [Higher-struggling-level problems elicit more diverse but less student-like LLM-generated errors](higher-struggling-problems-elicit-more-diverse-less-student-like-errors.md) — related
- [LLMs across five models generate diverse erroneous Java code, with mean AST edit distances varying by model and prompting strategy](llms-generate-diverse-erroneous-java-code-varying-by-model-and-prompt.md) — related
- [Blinded expert annotators misclassified 83.7% of LLM-generated errors as human-written](blinded-annotators-misclassify-83-7-percent-of-llm-errors-as-human.md) — related
