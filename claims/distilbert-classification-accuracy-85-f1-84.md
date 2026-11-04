---
type: claim
title: The DistilBERT classification model achieves validation accuracy of .85 and F1 score of .84 on the essay scoring task
description: The DistilBERT classification model achieves validation accuracy of .85 and F1 score of .84 on the essay scoring task
id: distilbert-classification-accuracy-85-f1-84
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

# The DistilBERT classification model achieves validation accuracy of .85 and F1 score of .84 on the essay scoring task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In the validation data, the DistilBERT classification model achieves an accuracy of .85 and an F1 score of .84. [→ Debelak Rudolf 2026](#debelak-rudolf-2026)

## Evidence

### Debelak Rudolf 2026

Debelak Rudolf, Ziegler Matthias. (2026). Testing standards for AI-based scores in automated essay scoring. PLOS One. https://doi.org/10.1371/journal.pone.0354680

`q2 · i?` · `theoretical · r3`

Classification framing of the essay scoring task with a threshold of .5 to distinguish high and low quality essays. The article reports a loss of .27 in training data and .44 in validation data after three epochs, with validation 'accuracy of .85 and an F1 score of .84'.

> "In the validation data, we observed an accuracy of .85 and an F1 score of .84, which indicate a sufficiently high accuracy for the purposes of this illustration."

## Discussion


## Related Claims
- [The DistilBERT model shows indications of fairness violations when comparing human and AI scores across different topics](distilbert-fairness-violations-across-topics.md) — related
- [A DistilBERT essay-scoring model shows sufficiently high internal consistency with Spearman-Brown coefficients from .77 to .92](distilbert-internal-consistency-spearman-brown-77-92.md) — related
