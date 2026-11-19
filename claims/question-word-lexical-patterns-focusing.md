---
type: claim
title: "The question words \"why\", \"how do\", and \"what else\" correlate positively with focusing labels while \"when\" correlates negatively on the FILTERED set"
description: "The question words \"why\", \"how do\", and \"what else\" correlate positively with focusing labels while \"when\" correlates negatively on the FILTERED set"
id: question-word-lexical-patterns-focusing
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: sterling-alic-2022
    resource: "https://doi.org/10.18653/v1/2022.bea-1.27"
    title: "Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)"
    author: Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The question words "why", "how do", and "what else" correlate positively with focusing labels while "when" correlates negatively on the FILTERED set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Indicators of open-ended questions ("why", "how do", "what else") correlate significantly positively with focusing, whereas "when" correlates negatively, and other question words show no significant correlation. [→ Sterling Alic 2022](#sterling-alic-2022)

## Evidence

### Sterling Alic 2022

Sterling Alic, Dorottya Demszky, Zid Mancenido, Jing Liu, Heather Hill, Dan Jurafsky. (2022). Computationally Identifying Funneling and Focusing Questions in Classroom Discourse. [doi:10.18653/v1/2022.bea-1.27](https://doi.org/10.18653/v1/2022.bea-1.27)

`q2 · i?` · `design · r2`

Correlational analysis of lexical count features against human labels on the FILTERED set. The text also reports "when" has a negative correlation with focusing, indicating teachers use it when expecting a normative answer.

> "we see a signiﬁcant positive correlation between the use of “why”, “how do”, and “what else” on theFILTERED set, conﬁrming our hypotheses that indicators of open-ended questions are also indicators of focusing."

## Discussion


## Related Claims
- [The unsupervised forwards-range measure correlates negatively with human labels on the UNFILTERED set (ρ = -.130) and positively on the FILTERED set (ρ = .159)](forwards-range-unsupervised-correlations.md) — related
- [A supervised RoBERTa model fine-tuned on the annotated dataset reaches a Spearman correlation of .761 with human expert labels for funneling and focusing questions on the UNFILTERED set](roberta-funneling-focusing-correlation-761.md) — related
