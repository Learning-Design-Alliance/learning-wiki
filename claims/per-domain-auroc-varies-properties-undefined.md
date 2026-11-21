---
type: claim
title: Classification performance varies across the seven sensemaking domains, and no AUROC could be reported for the properties domain because its positive examples were too rare
description: Classification performance varies across the seven sensemaking domains, and no AUROC could be reported for the properties domain because its positive examples were too rare
id: per-domain-auroc-varies-properties-undefined
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: gili-2025
    resource: "https://doi.org/10.1103/v6gw-lv4c"
    title: "Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)"
    author: Gili, Heuton, Shah, Hammer, and Hughes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Classification performance varies across the seven sensemaking domains, and no AUROC could be reported for the properties domain because its positive examples were too rare

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All three models detect object evidence well, but AUROC for the properties domain is undefined because no positive examples appeared in the test set. [→ Gili 2025](#gili-2025)

## Evidence

### Gili 2025

Gili, Heuton, Shah, Hammer, and Hughes. (2025). Combining physics education and machine learning research to measure evidence of students' mechanistic sensemaking. arXiv. [doi:10.1103/v6gw-lv4c](https://doi.org/10.1103/v6gw-lv4c)

`q2 · i?` · `design · r2`

Per-domain test evaluation shown in Fig. 3 with bootstrapped intervals. The article states the properties domain had extremely large class imbalance and no positive test examples, so "we cannot report AUROC results" for that domain; more positive examples are said to be necessary.

> "One major limitation in the results is that we cannot report AUROC results for yes/no criteria labels in the properties domain in Fig. 3."

## Discussion


## Related Claims
- [A fine-tuned BERT encoder achieves the best agreement with human coding (AUROC 0.916) among three encoder variants on held-out student responses to the same four problems](bert-finetuned-best-auroc-sensemaking.md) — related
