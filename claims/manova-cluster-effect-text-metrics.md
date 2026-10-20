---
type: claim
title: "Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)"
description: "Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)"
id: manova-cluster-effect-text-metrics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
sources:
  - id: teresa-luther-kate-belcher-joachim-kimmerle-detmar-meurers-ulrike-cress-2026
    resource: "https://doi.org/10.1007/s11412-026-09470-1"
    title: "Teresa Luther · Kate Belcher · Joachim Kimmerle · Detmar Meurers · Ulrike Cress (2026). Collaborative knowledge construction with generative AI: Exploring argumentative co-writing processes through n-gram and cluster analysis. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-026-09470-1"
    author: Teresa Luther · Kate Belcher · Joachim Kimmerle · Detmar Meurers · Ulrike Cress
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# Cluster membership showed a strong multivariate effect on standard text-similarity metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`

## Subclaims
`q3 i?` A MANOVA over BLEU, ROUGE-1/2/L, METEOR, and BERTScore revealed that clusters differed reliably in surface-level textual similarity. [→ Teresa Luther · Kate Belcher · Joachim Kimmerle · Detmar Meurers · Ulrike Cress 2026](#teresa-luther-kate-belcher-joachim-kimmerle-detmar-meurers-ulrike-cress-2026)

## Evidence

### Teresa Luther · Kate Belcher · Joachim Kimmerle · Detmar Meurers · Ulrike Cress 2026

Teresa Luther · Kate Belcher · Joachim Kimmerle · Detmar Meurers · Ulrike Cress (2026). Collaborative knowledge construction with generative AI: Exploring argumentative co-writing processes through n-gram and cluster analysis. Intern. J. Comput.-Support. Collab. Learn. https://doi.org/10.1007/s11412-026-09470-1

`q3 · i?` · `associational · r2`

Omnibus MANOVA treating the six benchmark scores as joint dependent variables to validate the n-gram clustering; a "strong multivariate effect of cluster membership" was found. Descriptively, Clusters 1 and 3 had higher BLEU, ROUGE, and BERTScore means than Cluster 2.

> "The analysis revealed a strong multivariate effect of cluster membership on the combined set of metrics (Pillai's trace = 0.85, F(12, 248) = 15.31, p < 0.001), indicating that clusters differed reliably in surface-level textual similarity as captured by n-gram overlap."

## Discussion


## Related Claims
- [Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models](higher-bit-quantisation-preserves-semantic-structure-pidgin-llm.md) — related
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](lora-improves-reference-answer-similarity-control-systems.md) — related
- [Base-model size effects persist after LoRA adaptation: the 7B model gained more on ROUGE-2 and ROUGE-L, yet 3B-r16 outperformed 7B-r4 on ROUGE-L and BERTScore-F1](model-size-and-lora-rank-joint-effects.md) — related
- [BLEU-4 scored zero on all 179 mathematical-proof responses, which the authors interpret as a property of n-gram metrics rather than system failure](bleu4-zero-mathematical-proofs-metric-limitation.md) — related
- [Per-topic performance varied: NP-completeness scored highest ROUGE-1 F1 (0.1285), sorting algorithms highest pedagogical quality (0.8250), and recurrence relations lowest pedagogical quality (0.6629)](algorag-topic-specific-performance-variation.md) — related
- [AI-supported argumentative writing yields three distinct uptake clusters (text reproducers, text integrators, text reconstructors) based on recurring n-gram overlap](three-uptake-clusters-human-ai-cowriting.md) — a broader claim this one bears on
- [Multivariate analysis confirmed a significant overall group effect, and all outcome variables correlated positively in both groups](ai-ibi-multivariate-group-effect-positive-correlations.md) — related
- [Personalized responses remain semantically grounded in the shared knowledge base while varying in surface-level expression and structure](semantic-grounding-with-surface-variation.md) — related
- [Text reproducers copied nearly all of their final text from ChatGPT with long verbatim sequences, while text integrators showed fragment-level micro-uptake](text-reproducers-near-verbatim-copying.md) — related
- [Textbook format choice produces a significant multivariate difference in university students' motivation and self-regulated learning scores](textbook-format-manova-omnibus-difference.md) — related
