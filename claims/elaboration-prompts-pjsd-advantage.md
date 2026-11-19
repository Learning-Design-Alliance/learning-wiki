---
type: claim
title: "Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set"
description: "Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set"
id: elaboration-prompts-pjsd-advantage
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
    kind: design
    rigour: 2
  - id: dorottya-demszky-2021-2
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Elaboration prompts are significantly enriched among examples where PJSD outperforms %-IN-T, but other phenomena show no significant difference in that set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Elaboration prompts occur significantly more often (odds ratio 4.25, p<0.05) in examples where PJSD outperforms %-IN-T. [→ Dorottya Demszky 2021](#dorottya-demszky-2021)
`q2 i?` No significant difference between the two sets in reformulations, collaborative completions and answers, possibly due to the small sample (n=67). [→ Dorottya Demszky 2021 (2)](#dorottya-demszky-2021-2)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `design · r2`

Manual labeling of teacher utterances in the residual-based set where PJSD outperforms %-IN-T versus the reverse set: examples with residual differences 1.5 SD above the mean were labeled for four phenomena, and elaboration prompts showed an odds ratio of 4.25 (p<0.05, Fisher exact test).

> "As Table 5 shows, elaboration prompts, which are exemplars of high uptake in teaching (Nystrand et al., 1997) are signiﬁcantly more likely to occur in this set"

### Dorottya Demszky 2021 (2)

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `design · r2`

Null result from the same manual labeling analysis: the occurrence of reformulations, collaborative completions and answers did not differ significantly between the PJSD-favoring and %-IN-T-favoring sets, which the authors attribute to the small sample size (n=67); equivalence was not tested.

> "We do not ﬁnd a signiﬁ- cant difference in the occurrence of reformulations, collaborative completions and answers between the two sets, possibly due to the small sample size (n=67)."

## Discussion


## Related Claims
- [PJSD captures uptake phenomena beyond repetition — answers, reformulations, collaborative completions and acknowledgments — better than %-IN-T](pjsd-captures-uptake-phenomena-switchboard.md) — related
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](pjsd-outperforms-repetition-baseline-uptake.md) — related
