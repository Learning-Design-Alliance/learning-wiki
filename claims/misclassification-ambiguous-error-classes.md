---
type: claim
title: Most frequent mis-classifications by the BERT + Action method involve ambiguous or overlapping error classes, suggesting an upper limit on dataset performance
description: Most frequent mis-classifications by the BERT + Action method involve ambiguous or overlapping error classes, suggesting an upper limit on dataset performance
id: misclassification-ambiguous-error-classes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: mcnichols-2023
    resource: "https://doi.org/10.1007/978-3-031-36272-9_30"
    title: "McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)"
    author: "McNichols, H., Zhang, M., & Lan, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: mcnichols-2023-2
    resource: "https://doi.org/10.1007/978-3-031-36272-9_30"
    title: "McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)"
    author: "McNichols, H., Zhang, M., & Lan, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Most frequent mis-classifications by the BERT + Action method involve ambiguous or overlapping error classes, suggesting an upper limit on dataset performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` REVERSED SIDES is mis-classified as WRONG OPERATION 41% of the time and the reverse 18% of the time, reflecting genuinely ambiguous student intent. [→ McNichols 2023](#mcnichols-2023)
`q2 i?` Mis-classifications also occur between classes differing only in specificity, e.g. FORGOT NEGATIVE mis-classified as WRONG OPERATION 23.6% of the time. [→ McNichols 2023 (2)](#mcnichols-2023-2)

## Evidence

### McNichols 2023

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `design · r2`

Qualitative error analysis of the best method (BERT + Action) on one cross-validation fold, shown as a mis-classification heatmap (Fig. 3). Both REVERSED SIDES and WRONG OPERATION can be appropriate for a response like y = −3, and true student intent is unknown. No effect size is printed.

> "The most frequent mis-classiﬁcation is between error class #4 and # 8 (RE- VERSED SIDES and WRONG OPERATION respectively). Class #4, 41% of the time, is incorrectly classiﬁed as class #8. 18% of the time the reve rse mis- classiﬁcation occurs."

### McNichols 2023 (2)

McNichols, H., Zhang, M., & Lan, A. (2023). Algebra Error Classification with Large Language Models. [doi:10.1007/978-3-031-36272-9_30](https://doi.org/10.1007/978-3-031-36272-9_30)

`q2 · i?` · `design · r2`

From the same qualitative analysis: a sign error in addition/subtraction can be explained as an incorrect operation, making one class more specific than the other. Similar confusions occur 13.2% of the time from class #15 to #18 and 11% from class #3 to #13.

> "For example, class #12 (FORGOT NEGATIVE) is 23.6% of the time mis-classiﬁed as class #8 (WRONG OPERATION)."

## Discussion


## Related Claims
- [Retrained BERT relies on high-impact nouns, verbs, and adjectives for correct predictions, but this reliance is muted on the AF dataset](lime-pos-reliance-varies-by-dataset.md) — related
