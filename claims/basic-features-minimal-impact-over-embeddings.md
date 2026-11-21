---
type: claim
title: Traditional linguistic and structural question and option features add virtually no improvement once text embeddings are available
description: Traditional linguistic and structural question and option features add virtually no improvement once text embeddings are available
id: basic-features-minimal-impact-over-embeddings
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

# Traditional linguistic and structural question and option features add virtually no improvement once text embeddings are available

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding question-text features (Model 2) offered virtually no improvement in difficulty correlation, and adding option features (Model 3) slightly decreased Pearson correlation to around 0.68 while Spearman remained largely unchanged. [→ Matías Hoyl 2026](#matias-hoyl-2026)

## Evidence

### Matías Hoyl 2026

Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. [doi:10.48550/arXiv.2602.00034](https://doi.org/10.48550/arXiv.2602.00034)

`q2 · i?` · `design · r2`

Feature ablation study, Models 2 and 3 versus Model 1: Table 4 prints Pearson 0.6842 and 0.6758 versus 0.6822 for embeddings only, with Spearman around 0.70. No effect size for the difference is printed, so impact is coded i? (no magnitude reported; not a null effect); the decrease in Model 3 is descriptive.

> "Adding traditional linguistic and structural features derived from the question text (Model 2) offered virtually no improvement in difficulty correlation."

## Discussion


## Related Claims
- [Adding LLM-extracted pedagogical features raises difficulty-prediction correlation from about 0.68 to about 0.78 over embeddings and traditional features](llm-pedagogical-features-drive-difficulty-gain.md) — related
- [Combining semantic and process features yields the best difficulty prediction; semantic embeddings alone trail the full model by 7.4–12.1 macro-F1 points on SAT Math](full-representation-beats-semantic-only-ablation.md) — related
