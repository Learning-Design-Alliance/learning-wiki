---
type: claim
title: Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness
description: Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness
id: supervised-models-competitiveness-uptake
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: dorottya-demszky-2021
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Supervised BERT-base (ρ=.618) and RoBERTa-base (ρ=.561) outperform the unsupervised PJSD measure (ρ=.540) by less than .08. [→ Dorottya Demszky 2021](#dorottya-demszky-2021)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `associational · r2`

Appendix experiment: BERT-base and RoBERTa-base were fine-tuned on an 80/20 split of the annotated data with z-scored rater judgments as labels, achieving ρ=.618 and ρ=.561 versus PJSD's .540; the authors report the gap as less than .08 and note BERT unexpectedly beat RoBERTa.

> "The supervised models outperform our unsupervised models by less than.08, indicating the competitiveness of our unsupervised methods. Interestingly, we also ﬁnd that BERT outperforms RoBERTa, a gap that per-sisted despite tuning the number of training epochs."

## Discussion


## Related Claims
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](pjsd-captures-uptake-phenomena-switchboard.md) — related
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](pjsd-outperforms-repetition-baseline-uptake.md) — related
- [Domain adaptation through unsupervised pretraining gave mixed results: it slightly improved RoBERTa but degraded the Longformer for both Content and Wording](domain-adaptation-mixed-roberta-helped-longformer-hurt.md) — related
