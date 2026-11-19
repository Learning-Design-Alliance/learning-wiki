---
type: claim
title: "PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T"
description: "PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T"
id: pjsd-captures-uptake-phenomena-switchboard
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: dorottya-demszky-2021
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On Switchboard dialog-act-labeled pairs, PJSD predicts significantly higher scores than %-IN-T for all five uptake phenomena, especially answers, reformulations, collaborative completions and acknowledgments. [→ Dorottya Demszky 2021](#dorottya-demszky-2021)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `design · r2`

Large-scale comparison on Switchboard utterance pairs labeled via SWBD-DAMSL tags for five uptake phenomena: median score differences (δ) between quantile-transformed PJSD and %-IN-T were tested per phenomenon, with significance at p<0.001 for answers, reformulation, collaborative completion and acknowledgment, and a small but significant δ for repetition.

> "The results (Figure 2) show that PJSD predicts signiﬁcantly higher scores than %-IN-T for all phe-nomena, especially for answers, reformulations, collaborative completions and acknowledgments."

## Discussion


## Related Claims
- [Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set](elaboration-prompts-pjsd-advantage.md) — related
- [PJSD correlates significantly with educational outcomes across three datasets, while %-IN-T fails in the written one-on-one tutoring setting](pjsd-correlates-educational-outcomes-three-datasets.md) — related
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](pjsd-outperforms-repetition-baseline-uptake.md) — related
- [Supervised models outperform the unsupervised uptake measures by less than .08 correlation, indicating their competitiveness](supervised-models-competitiveness-uptake.md) — related
