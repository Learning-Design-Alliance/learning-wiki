---
type: claim
title: A DistilBERT essay-scoring model shows sufficiently high internal consistency with Spearman-Brown coefficients from .77 to .92
description: A DistilBERT essay-scoring model shows sufficiently high internal consistency with Spearman-Brown coefficients from .77 to .92
id: distilbert-internal-consistency-spearman-brown-77-92
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: debelak-rudolf-2026
    resource: "https://doi.org/10.1371/journal.pone.0354680"
    title: "Debelak Rudolf, Ziegler Matthias. (2026). Testing standards for AI-based scores in automated essay scoring. PLOS One. https://doi.org/10.1371/journal.pone.0354680"
    author: Debelak Rudolf, Ziegler Matthias
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# A DistilBERT essay-scoring model shows sufficiently high internal consistency with Spearman-Brown coefficients from .77 to .92

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The DistilBERT model applied to the Hewlett Foundation dataset achieves internal consistency with Spearman-Brown coefficients in the range .77 to .92. [→ Debelak Rudolf 2026](#debelak-rudolf-2026)

## Evidence

### Debelak Rudolf 2026

Debelak Rudolf, Ziegler Matthias. (2026). Testing standards for AI-based scores in automated essay scoring. PLOS One. https://doi.org/10.1371/journal.pone.0354680

`q2 · i?` · `theoretical · r3`

Empirical illustration using the Hewlett Foundation Kaggle automated essay scoring dataset with a DistilBERT model. The article reports Spearman-Brown coefficients 'in the range from .77 to .92' as evidence of internal consistency via split-half text partitioning.

> "By applying the proposed framework to an evaluation based on a DistilBERT model, we find the model to be robust with sufficiently high internal consistency (Spearman-Brown coefficients in the range from .77 to .92)."

## Discussion


## Related Claims
- [The DistilBERT model shows indications of fairness violations when comparing human and AI scores across different topics](distilbert-fairness-violations-across-topics.md) — related
- [The DistilBERT classification model achieves validation accuracy of .85 and F1 score of .84 on the essay scoring task](distilbert-classification-accuracy-85-f1-84.md) — related
- [Split-half analysis supports the internal consistency of the Turkish-adapted tool (Spearman–Brown = 0.800, Guttman = 0.796)](turkish-clt-tool-split-half-spearman-brown-0800.md) — related
