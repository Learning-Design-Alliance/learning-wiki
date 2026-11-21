---
type: claim
title: SimCSE-trained sequence embeddings outperform mean-pooled pretrained-encoder baselines on action content prediction and action sequence reconstruction
description: SimCSE-trained sequence embeddings outperform mean-pooled pretrained-encoder baselines on action content prediction and action sequence reconstruction
id: simcse-sequence-embeddings-beat-mean-pooling-probes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: siddhartha-pradhan-2026
    resource: "https://doi.org/10.48550/arXiv.2604.08693"
    title: "Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar. (2026). Towards Generalizable Representations of Mathematical Solution Strategies. arXiv. [doi:10.48550/arXiv.2604.08693](https://doi.org/10.48550/arXiv.2604.08693)"
    author: Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SimCSE-trained sequence embeddings outperform mean-pooled pretrained-encoder baselines on action content prediction and action sequence reconstruction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The SimCSE encoder with MathBERT-mamut state embeddings achieved the highest action content scores (86.1% Micro-F1, 21.8% Macro-F1) and best reconstruction (2.06 perplexity, 77.0% token accuracy). [→ Siddhartha Pradhan 2026](#siddhartha-pradhan-2026)

## Evidence

### Siddhartha Pradhan 2026

Siddhartha Pradhan, Ethan Prihar, and Erin Ottmar. (2026). Towards Generalizable Representations of Mathematical Solution Strategies. arXiv. [doi:10.48550/arXiv.2604.08693](https://doi.org/10.48550/arXiv.2604.08693)

`q2 · i?` · `design · r2`

Probe evaluation (MLP classifiers and an LSTM reconstruction probe) trained on sequence embeddings from 36 model configurations, compared against mean-pooled frozen-encoder baselines (Table 2). The best configuration reached "86.1% Micro-F1 and 21.8% Macro-F1" on action content and "2.06 perplexity and 77.0% token-level accuracy" on reconstruction.

> "our encoder with sequence embeddings derived from MathBERT-mamut achieved the highest scores on the action content task (86.1% Micro-F1 and 21.8% Macro-F1), and action sequence reconstruction (2.06 perplexity and 77.0% token-level accuracy)."

## Discussion


## Related Claims
- [After PPO optimization, auxiliary feedback semantic similarity (SimCSE) reaches 81.3% and 79.3% for the two policy models, higher than evaluated pretrained baselines](races-auxiliary-feedback-simcse-gains.md) — related
