---
type: claim
title: Example-first conditions outperformed problem-first conditions on an immediate circuit test
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: worked-example-problem-sequences
evidence_strength: low
sources:
  - id: van-gog-et-al-2011
    resource: "https://doi.org/10.1016/j.cedpsych.2010.10.004"
    title: "van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)"
    author: "van Gog, T., Kester, L., & Paas, F."
    q: 3
    i: "?"
    n: 96
    kind: causal
    rigour: "?"
---

# Example-first conditions outperformed problem-first conditions on an immediate circuit test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q3` · n=96

## Subclaims

`q3 i?` In this novice circuit experiment, WE and WE–PS outperformed PS and PS–WE on the immediate test and had lower reported training effort. Neither within-pair contrast was detected; equivalence was not tested.

## Evidence

### van Gog et al. 2011

van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)

`q3 · peer-reviewed experiment` · `i? · omnibus partial η² only; no pairwise standardized effect` · `n=96` · `causal · r?`

[Peer-reviewed author manuscript](https://research.ou.nl/ws/portalfiles/portal/1026339/Van%20Gog_%20Kester%20_%20Paas%20-%20CEDPSYCH%202010.pdf), Methods/Results and Table 1, manuscript pp. 10–16, 26. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004). Full method/result verification by the editing agent; not independent human verification.

103 Dutch secondary students were randomized within sessions; 96 were analyzed. Seven missing-test exclusions occurred in PS (4) and WE–PS (3). Prior knowledge was a covariate. Four paper tasks varied example/problem format; calculators and formula sheets were allowed, previous solutions unavailable. Two same-session test problems varied surface details or fault complexity; total score range was 0–8. One author scored blind to condition. Effort was self-reported on a nine-point scale.

Test ANCOVA: F(3,91)=9.00, partial η²=.23; training effort: F(3,91)=7.78, partial η²=.20. Bonferroni contrasts supported the stated ordering. These are omnibus effects, not pairwise standardized gains or individual probabilities. Randomization does not ensure exact baseline equivalence; differential exclusions and narrow, instruction-aligned tests constrain interpretation.

## Studies bearing on this claim

<!-- synthesis:start -->
*Should the example come before or after the practice problem?* This table gathers the studies behind this claim and the 2 narrower claims that bear on it: **3 distinct studies** (2 causal, 1 review), `q2`–`q3`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [van Gog et al. 2011](https://doi.org/10.1016/j.cedpsych.2010.10.004) | q3 · causal · r? | i? | this claim |
| [van Gog 2011](https://doi.org/10.1016/j.compedu.2011.03.019) | q3 · causal · r? | i? | [Identical example–problem pairs showed an early order advantage but no detected final-test](identical-example-problem-order-advantage-not-detected-at-final-test.md) (qualifies) |
| [Atkinson 2000](https://doi.org/10.3102/00346543070002181) | q2 · review · r3 | i? | [Alternating example-practice pairs produce faster and more accurate near-transfer solution](alternating-example-problem-pairs.md) (supports) |
<!-- synthesis:end -->

## Discussion

The comparison supports a bounded example-first choice for similar initial tasks. It does not test an adaptive fading policy, a mandatory alternation rule, delayed retention, live repair safety or open-ended creativity. Mental effort is an observed report; schema acquisition is an explanation, not a direct measurement. No learner-valued goal mechanism was measured.

Do not conflate example→problem pairs with completion problems: the latter omit solution steps within a task. Do not substitute this study's task count, timing or test threshold as universal requirements. A short diagnostic attempt before instruction is also distinct from a sustained problem-first learning design.

## Related Claims

- [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](worked-examples-with-practice-improve-transfer.md) — the general claim this finding bears on, with the studies behind it

- [Identical pairs qualify an example-first final-test advantage](identical-example-problem-order-advantage-not-detected-at-final-test.md)
- [Fading and principle prompts in probability learning](fading-and-principle-prompts-improve-probability-transfer.md)
