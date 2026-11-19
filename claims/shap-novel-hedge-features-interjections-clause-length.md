---
type: claim
title: SHAP analysis identified novel features of hedge classes, including interjections associated with Apologizers and clause length as a class indicator
description: SHAP analysis identified novel features of hedge classes, including interjections associated with Apologizers and clause length as a class indicator
id: shap-novel-hedge-features-interjections-clause-length
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
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

# SHAP analysis identified novel features of hedge classes, including interjections associated with Apologizers and clause length as a class indicator

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SHAP explanation of the best model revealed features not identified in the hedges literature: informal words/interjections like ah and oh associated with Apologizers, POS n-grams important for all classes, and clause length patterns distinguishing classes. [→ Yann Raphalen 2022](#yann-raphalen-2022)

## Evidence

### Yann Raphalen 2022

Yann Raphalen, Chloé Clavel, Justine Cassell. (2022). "You might think about slightly revising the title": Identifying Hedges in Peer-tutoring Interactions. [doi:10.18653/v1/2022.acl-long.153](https://doi.org/10.18653/v1/2022.acl-long.153)

`q2 · i?` · `design · r2`

SHAP (TreeSHAP) explanation analysis of the LightGBM model with all features on the peer-tutoring corpus. The article also reports that "a clause shorter than the mean is weakly associated with directness (n=17) while a longer clause suggests that it contains a Subjectivizer (n=6)."

> "SHAP highlights the importance of novel features whose function was not identified in the hedges literature: (i) what LIWC classifies as informal words but that are mostly interjections like ah and oh are strongly associated with Apologizer, as are disfluencies (n=12);"

## Discussion


## Related Claims
- [Best hedge-detection performance (F1 79.0) came from LightGBM using nearly all feature groups](lightgbm-all-features-best-f1-79.md) — related
- [Rule-based classifier labels and expected lexical markers (I, sorry, just, would) rank among the most important SHAP features for hedge classes](rule-based-labels-top-shap-features.md) — related
