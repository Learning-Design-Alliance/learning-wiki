---
type: claim
title: Multi-prompt training outperforms single-prompt only under extreme label scarcity; above 64 samples per prompt, single-prompt training yields better performance
description: Multi-prompt training outperforms single-prompt only under extreme label scarcity; above 64 samples per prompt, single-prompt training yields better performance
id: multi-prompt-vs-single-prompt-low-resource
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: hongseok-choi-2026
    resource: "https://doi.org/10.1109/ACCESS.2026.3718177"
    title: "Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177"
    author: Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang
    q: 3
    i: "?"
    kind: causal
    rigour: "?"
---

# Multi-prompt training outperforms single-prompt only under extreme label scarcity; above 64 samples per prompt, single-prompt training yields better performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` MP outperforms SP when training data are very limited (16 or 32 samples), but above 64 samples SP consistently yields better performance; at K = 128 MP is about 0.04 QWK points lower despite eight times more data. [→ Hongseok Choi 2026](#hongseok-choi-2026)

## Evidence

### Hongseok Choi 2026

Hongseok Choi, Serynn Kim, Wencke Liermann, Jin Seong, and Jin-Xia Huang. (2026). Enhancing Automated Essay Scoring With Three Techniques: Two-Stage Fine-Tuning, Score Alignment, and Self-Training. IEEE Access. https://doi.org/10.1109/ACCESS.2026.3718177

`q3 · i?` · `causal · r?`

Experiment on the effect of different prompt essays on ASAP++ (Fig. 4), comparing LoRA in the multi-prompt and single-prompt settings across training-sample sizes; the article reports essays from other prompts act as in-domain samples only in extremely low-resource settings.

> "We observe that MP outperforms SP when training data are very limited (e.g., 16 or 32 samples); however, above 64 samples, SP consistently yields better performance."

## Discussion


## Related Claims
- [Pre-training on synthetic data before fine-tuning on limited real data improves math operation classification accuracy, with the largest gains when real data is extremely limited](synthetic-pretraining-finetuning-limited-real-data.md) — related
- [Training NQG models on multiple datasets with different answer types improved performance over single-dataset training](multi-dataset-training-improves-nqg-answer-types.md) — related
