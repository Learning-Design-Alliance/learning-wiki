---
type: product
id: mutse
title: MuTSE
description: MuTSE is a web application developed by Rares-Alexandru Roșcan et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
---

# MuTSE

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
MuTSE is a web application developed by Rares-Alexandru Roșcan et al. for comparing and manually or automatically evaluating LLM-generated text simplifications against learner proficiency targets.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Tiered semantic alignment engine with hierarchical embedding fallback and linearity bias heuristic**: MuTSE's Semantic Alignment Engine visually maps original sentences to their simplified counterparts using a three-tier cascade: a 384-dimensional multilingual transformer embedding (paraphrase-multilingual-MiniLM-L12-v2), a hybrid TF-IDF fallback with word- and character-level n-grams, and a tertiary positional fallback. A linearity factor λ penalizes positionally distant alignments via Score(i,j) = CosineSim − |Pos_rel(i) − Pos_rel(j)| × λ, adjustable in real time between 0 and 2 with a default of 0.5. The article describes the linearity bias as "a structural regularizer, effectively offsetting the reduced discriminative capacity inherent to heavily compressed embedding models." (Rares-Alexandru Roșcan et al. (2026))
- **Evaluation-agnostic annotation framework with user-defined dimensions, arbitrary rating scales, and weighted aggregation**: MuTSE operates as an evaluation-agnostic framework with zero predefined metrics: evaluators build custom assessment criteria from scratch in the Settings module, define arbitrary numerical rating scales from binary (1-to-2) up to continuous 100-point sliders, and assign relative impact weights from 0.1 to 10.0. The system normalizes and aggregates manual inputs to compute a weighted overall performance percentage for each generated column. The article motivates this by noting "a pervasive lack of standardization and extreme diversity in evaluation methodologies and terminology across the field." (Rares-Alexandru Roșcan et al. (2026))

### Claims

- [Asynchronous concurrent execution bounds overall latency to approximately the slowest individual model's inference time](../claims/async-concurrency-latency-bounded-by-slowest-model.md) [+W]
- [The linearity bias heuristic enables robust alignment with low-dimensional embeddings on standard CPUs, lowering computational prerequisites](../claims/linearity-bias-lowers-computational-prerequisites.md) [+W]

## Related Products and Programmes
-

## Key Sources
- Rares-Alexandru Roșcan, Gabriel Petre, Adrian-Marius Dumitran, Angela-Liliana Dumitran. (2026). MuTSE: A Human-in-the-Loop Multi-use Text Simplification Evaluator. arXiv. https://arxiv.org/abs/2604.08947
