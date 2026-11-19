---
type: claim
title: Rule-based classifier labels and expected lexical markers (I, sorry, just, would) rank among the most important SHAP features for hedge classes
description: Rule-based classifier labels and expected lexical markers (I, sorry, just, would) rank among the most important SHAP features for hedge classes
id: rule-based-labels-top-shap-features
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: yann-raphalen-2022
    resource: "https://doi.org/10.18653/v1/2022.acl-long.153"
    title: "Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). \"You might think about slightly revising the title\": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)"
    author: Yann Raphalen, Chloé Clavel, Justine Cassell
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Rule-based classifier labels and expected lexical markers (I, sorry, just, would) rank among the most important SHAP features for hedge classes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The rule-based label was among the top features for three of four classes, and top unigrams (Oh, Sorry, just, Would, I) confirmed prior literature on hedge-class characterization. [→ Yann Raphalen 2022](#yann-raphalen-2022)

## Evidence

### Yann Raphalen 2022

Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)

`q2 · i?` · `design · r2`

SHAP analysis of the LightGBM model on the peer-tutoring corpus. The article states unigrams "(Oh, Sorry, just, Would, and I) are also present in the 5 top-ranked features", confirming prior characterizations of the classes.

> "The most important features seem to be the rule-based labels, which appear in at least the fourth position for three classes (see Table 6), and in the first position for Propositional Hedges and Not hedged classes."

## Discussion


## Related Claims
- [Adding n-gram features significantly improved the hedge classifier, but tutoring moves and nonverbal features did not](ngrams-help-tutoring-moves-nonverbal-do-not.md) — related
- [SHAP analysis identified novel features of hedge classes, including interjections associated with Apologizers and clause length as a class indicator](shap-novel-hedge-features-interjections-clause-length.md) — related
