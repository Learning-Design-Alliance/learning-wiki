---
type: claim
title: "LM-based simulated expert evaluations replicate the Expertise Reversal Effect: low-expertise learners benefit more from worked examples than practice, with no such difference among high-expertise learners"
description: "LM-based simulated expert evaluations replicate the Expertise Reversal Effect: low-expertise learners benefit more from worked examples than practice, with no such difference among high-expertise learners"
id: see-replicates-expertise-reversal-effect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
source_checked: 2026-11-20
sources:
  - id: joy-he-yueya-2024
    resource: "https://doi.org/10.48550/arXiv.2403.02795"
    title: "Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)"
    author: Joy He-Yueya, Noah D. Goodman, Emma Brunskill
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# LM-based simulated expert evaluations replicate the Expertise Reversal Effect: low-expertise learners benefit more from worked examples than practice, with no such difference among high-expertise learners

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person

## Subclaims
`q2 i?` According to GPT-3.5 simulated expert evaluations over 120 student personas, the worked-example group significantly outperforms the practice group on the post-test among low-expertise learners, while high-expertise learners show similar outcomes under both instruction types. [→ Joy He-Yueya 2024](#joy-he-yueya-2024)

## Evidence

### Joy He-Yueya 2024

Joy He-Yueya, Noah D. Goodman, Emma Brunskill. (2024). Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint. [doi:10.48550/arXiv.2403.02795](https://doi.org/10.48550/arXiv.2403.02795)

`q2 · i?` · `causal · r1`

Simulated expert evaluations (SEEs) with gpt-3.5-turbo-16k as evaluator over 120 student personas in a systems-of-equations domain, following the design of Kalyuga and Sweller's coordinate geometry experiment. The article reports the significant worked-example advantage for low-expertise learners and its absence for high-expertise learners (Figure 4).

> "Among low-expertise learners, the worked-example group significantly outperforms the practice group on the post-test. This performance difference is not observed among high-expertise learners, where both practice and worked-example groups show similar outcomes."

## Discussion


## Learner Variables
- [Prior Knowledge](../learner-variables/prior-knowledge.md) — moderator: an instructional effect differs with it

## Related Claims
- [LM judgments are internally consistent: SEEs designed to replicate the Variability Effect also replicate the Expertise Reversal Effect](see-judgments-consistent-across-replications.md) — possibly the same claim (merge candidate)
- [LM-based simulated expert evaluations replicate the Variability Effect: high variability enhances performance in worked-example conditions but has no effect in practice conditions](see-replicates-variability-effect.md) — related
- [Element interactivity and expertise reversal effects: cognitive load effects diminish and may reverse as expertise increases because known elements chunk into single elements](expertise-reversal-effect-element-interactivity.md) — a broader claim this one bears on
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](expertise-reversal-effect.md) — a broader claim this one bears on
- [Expertise reversal: cognitive load effects for novices decrease, disappear, and can reverse as expertise increases](expertise-reversal-effect-compound.md) — a broader claim this one bears on
- [Segmentation Benefits Shrink With Expertise](segmentation-benefits-shrink-with-expertise.md) — related
- [Design guidelines beneficial for novice learners can be ineffective or even detrimental when applied to experts (expertise reversal)](expertise-reversal-interactivity-guidelines.md) — a broader claim this one bears on
- [Reviews report that the split-attention benefit for novices reverses into a redundancy effect for more experienced learners: Kalyuga et al. (2003) cite Kalyuga et al. (1998) and Yeung et al. (1998), and Ginns (2006) cites Kalyuga et al. (1998)](expertise-reversal-split-attention-redundancy-review.md) — related
