---
type: claim
title: Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features
description: Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features
id: llm-pedagogical-features-drive-difficulty-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: matías-hoyl-2026
    resource: "https://doi.org/10.48550/arXiv.2602.00034"
    title: "Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)"
    author: Matías Hoyl
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the ablation study, the full model with LLM-derived pedagogical features reached a Pearson correlation of approximately 0.78 and Spearman of approximately 0.76, a marked improvement over models using only embeddings and traditional features. [→ Matías Hoyl 2026](#matias-hoyl-2026)

## Evidence

### Matías Hoyl 2026

Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)

`q2 · i?` · `design · r2`

Feature ablation study on the test set, four models sharing the same architecture and IRT framework; Table 4 prints Pearson 0.7791 and Spearman 0.7606 for the full model versus 0.6822 for embeddings only. No standardised effect size is printed for the difference between models, so impact is coded i? (no magnitude reported; not a null effect).

> "The most substantial gain in performance came with the addition of LLM-derived pedagogical features (Model 4, the Full Model). This model, which includes all feature types, reached a Pearson correlation of approximately 0.78 and a Spearman correlation of approximately 0.76."

## Discussion


## Related Claims
- [Traditional linguistic and structural question and option features add virtually no improvement once text embeddings are available](basic-features-minimal-impact-over-embeddings.md) — related
- [IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions](synthetic-responses-irt-difficulty-estimation.md) — related
- [LLM-extracted cognitive and linguistic features add predictive value beyond readily available item metadata (grade, domain, item type, word count)](llm-features-add-value-beyond-item-metadata.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
- [An expanded 67-feature model of P(J) gave only a minor correlation improvement over the original feature set in ASSISTments.](expanded-feature-set-minor-improvement.md) — related
