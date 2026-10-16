---
type: claim
title: "Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations"
description: "Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations"
id: source-anchoring-reduces-hallucination-instruction-data
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: shwetha-singaravelu-2026
    resource: "https://doi.org/10.48550/arxiv.2607.23322"
    title: "Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)"
    author: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Source-anchored instruction pairs reduce hallucination: they achieve mean Teacher Fidelity 1.4 points higher than non-anchored pairs, and models trained on anchored subsets produce 23% fewer factual hallucinations

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Source-anchored pairs score higher on Teacher Fidelity and yield fewer factual hallucinations in held-out evaluations than non-anchored pairs. [→ Shwetha Singaravelu 2026](#shwetha-singaravelu-2026)

## Evidence

### Shwetha Singaravelu 2026

Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322 [doi:10.48550/arxiv.2607.23322](https://doi.org/10.48550/arxiv.2607.23322)

`q2 · i?` · `design · r2`

Data-quality analysis in Section 6.2 comparing source-anchored versus template-generated pairs without source anchoring, reporting mean TF scores of 7.8 versus 6.4 and a 23% reduction in factual hallucinations; no standardized effect size is printed.

> "source-anchored pairs achieve mean TF scores 1.4 points higher than non-anchored pairs (7.8 vs. 6.4), and fine-tuned models trained on source-anchored subsets produce 23% fewer factual hallucinations in held-out evaluations"

## Discussion


## Related Claims
- [Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality](non-monotonic-quality-volume-iks-instruct.md) — related
- LLM-assisted inductive qualitative coding carries risks of superficial themes, broad or redundant codes, and hallucinated interpretations, so LLMs should augment rather than replace human researchers — related
- [Poorly grounded GenAI self-study risks fabricated content and inferior learning relative to curated resources](genai-self-study-fabrication-curated-resources.md) — related
- [The verification threshold trades hallucination reduction against over-refusal, with the default tau of 0.20 providing the best balance](eduguard-verifier-threshold-sensitivity.md) — related
