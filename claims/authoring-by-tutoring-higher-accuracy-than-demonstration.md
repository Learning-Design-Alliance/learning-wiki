---
type: claim
title: Authoring by Tutoring yields a more accurate expert model than Authoring by Demonstration while maintaining the same level of completeness
description: Authoring by Tutoring yields a more accurate expert model than Authoring by Demonstration while maintaining the same level of completeness
id: authoring-by-tutoring-higher-accuracy-than-demonstration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2015
sources:
  - id: matsuda-2015
    resource: "https://doi.org/10.1007/s40593-014-0020-1"
    title: "Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1"
    author: "Matsuda, N., Cohen, W. W., & Koedinger, K. R."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: matsuda-2015-2
    resource: "https://doi.org/10.1007/s40593-014-0020-1"
    title: "Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1"
    author: "Matsuda, N., Cohen, W. W., & Koedinger, K. R."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Authoring by Tutoring yields a more accurate expert model than Authoring by Demonstration while maintaining the same level of completeness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The expert model generated with Authoring by Tutoring achieves a higher average problem score (0.80) than Authoring by Demonstration (0.62), a statistically significant difference. [→ Matsuda 2015](#matsuda-2015)
`q2 i?` Recall scores, reflecting completeness, did not differ significantly between the two authoring strategies. [→ Matsuda 2015 (2)](#matsuda-2015-2)

## Evidence

### Matsuda 2015

Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1

`q2 · i?` · `causal · r2`

Simulation study comparing Authoring by Tutoring and Authoring by Demonstration, both simulated with Cognitive Tutor technology. The tutoring condition produced a higher average problem score (0.80 vs. 0.62), with a statistically significant difference, t(69)=7.94, p<0.001.

> "After training on 20 problems, the average problem score for Authoring by Tutoring was 0.80, and 0.62 for Authoring by Demonstration. The difference was statistically significant, t(69)=7.94, p<0.001."

### Matsuda 2015 (2)

Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1

`q2 · i?` · `causal · r2`

In the same simulation study, recall scores showed no statistically significant difference between strategies at the end of training, t(49)=1.50, p=0.13, indicating comparable completeness.

> "At the beginning, Authoring by Tutoring showed slightly inferior performance on the recall score, but at the end, the difference was not statistically significant; t(49)=1.50, p=0.13."

## Discussion


## Related Claims
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [Explicit negative feedback on incorrect production applications drives the accuracy advantage of Authoring by Tutoring](negative-feedback-drives-tutoring-accuracy-advantage.md) — related
