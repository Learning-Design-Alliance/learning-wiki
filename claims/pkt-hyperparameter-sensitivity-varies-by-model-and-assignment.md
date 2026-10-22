---
type: claim
title: Hyperparameter sensitivity in PKT is an inherent characteristic of programming interaction data, varying across models and across assignments within the same model
description: Hyperparameter sensitivity in PKT is an inherent characteristic of programming interaction data, varying across models and across assignments within the same model
id: pkt-hyperparameter-sensitivity-varies-by-model-and-assignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jaewook-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Hyperparameter sensitivity in PKT is an inherent characteristic of programming interaction data, varying across models and across assignments within the same model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Optimal hyperparameter configurations vary across PKT models and across assignments within the same model, and this variability is observed consistently across both DKT and PKT models. [→ Jaewook Kim 2026](#jaewook-kim-2026)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)

`q2 · i?` · `causal · r2`

Analysis of hyperparameter sensitivity for Code-DKT and ECKT (Section 3.3) on CodeWorkout. The authors state that "hyperparameter sensitivity is an inherent characteristic of programming interaction data rather than a byproduct of architectural complexity".

> "We observe that optimal configurations vary not only across different PKT models, but also across assignments within the same model."

## Discussion


## Related Claims
- [Task-specific hyperparameter optimization substantially raises baseline DKT performance, indicating prior DKT-vs-PKT gaps partly reflect insufficient baseline tuning](task-specific-hyperparameter-tuning-raises-dkt-baseline.md) — related
- [MBP-KT performance is optimal with sliding-window size N between 2 and 4 and is not sensitive to pattern-set length K (variation within 2%)](mbp-kt-hyperparameter-sensitivity-n-k.md) — reports the opposite
- [Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets](longer-sequence-length-no-consistent-pkt-gain.md) — related
- DynEmb's response-prediction AUC is stable over a wide range of question-embedding dimensionalities — reports the opposite
- OptimNN is insensitive to optimizer learning rate and network hyperparameters, unlike plain SGD on BKT — reports the opposite
- DKT's input/output representation significantly affects performance, with KC inputs and item outputs working best on most datasets — related
- [There is no universal optimal injection position for the collaborative prior; effectiveness is an architecture-sensitive design choice](injection-strategy-architecture-sensitive.md) — a narrower finding that bears on this claim
- [ProPRL is sensitive to learning rate but comparatively insensitive to its structural hyperparameters, with propagation depth around 5 capturing most multi-hop benefit](proprl-hyperparameter-sensitivity.md) — related
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — related
- [Students' strategy use is partly context-specific and partly individual-bound, varying across courses yet consistent over courses](strategy-use-context-specific-and-individual-bound.md) — related
