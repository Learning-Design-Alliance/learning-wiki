---
type: claim
title: "Learning techniques have much smaller effects on deep learning and far transfer than on surface learning and near transfer"
description: "Effects were d = 0.60 on surface outcomes (1,473 effects) against 0.26 on deep outcomes (109 effects), and 0.61 on near transfer against 0.39 on far transfer; most studies measured surface or factual outcomes."
id: learning-techniques-smaller-effects-on-deep-learning-and-far-transfer
status: draft
generated:
  by: claude/unspecified
  at: 2026-10-13
evidence_strength: moderate
sources:
  - id: donoghue-hattie-2021
    resource: "https://doi.org/10.3389/feduc.2021.581216"
    title: "Donoghue, G. M., & Hattie, J. A. C. (2021). A Meta-Analysis of Ten Learning Techniques. *Frontiers in Education, 6*, 581216. [doi:10.3389/feduc.2021.581216](https://doi.org/10.3389/feduc.2021.581216)"
    author: "Donoghue, G. M., & Hattie, J. A. C."
    q: 3
    i: 1
    n: 242 studies
    kind: quant-synthesis
    rigour: "?"
---

# Learning techniques have much smaller effects on deep learning and far transfer than on surface learning and near transfer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q3` · `i1` small · n=242 studies

Whether the ten learning techniques Dunlosky et al. (2013) reviewed help with deep, relational learning and transfer, or mainly with surface recall.

## Subclaims

`q3 i1` Effects were d = 0.60 on surface outcomes (1,473 effects) against 0.26 on deep outcomes (109 effects), and 0.61 on near transfer against 0.39 on far transfer; most studies measured surface or factual outcomes. [→ Donoghue & Hattie 2021](#donoghue-hattie-2021)

## Evidence

### Donoghue & Hattie 2021

Donoghue, G. M., & Hattie, J. A. C. (2021). A Meta-Analysis of Ten Learning Techniques. *Frontiers in Education, 6*, 581216. [doi:10.3389/feduc.2021.581216](https://doi.org/10.3389/feduc.2021.581216)

`q3 · meta-analysis (moderator analysis, 1,619 effects)` · `i1 · small effect on deep outcomes, d = 0.26 (0.60 surface); far transfer d = 0.39` · `n=242 studies` · `quant-synthesis · r?`

The authors coded each outcome for depth (surface, content-specific, against deep, more generalisable) and for transfer distance. Effects on surface outcomes were d = 0.60 (1,473 effects) and on deep outcomes d = 0.26 (109 effects). Near-transfer effects were d = 0.61 and far-transfer effects d = 0.39. They name the dominance of surface and factual outcomes as the review's major limitation.

> "The effects were higher for Surface (d = 0.60, SE = 0.021, N = 1,473) than for Deep processing (d = 0.26, SE = 0.064, N = 109)."

## Studies bearing on this claim

<!-- synthesis:start -->
*Does instruction that raises near transfer also raise far transfer to a different domain or form?* This table gathers the studies behind this claim and the 4 narrower claims that bear on it: **5 distinct studies** (3 causal, 1 quant-synthesis, 1 review), `q2`–`q3`, 1 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Donoghue & Hattie 2021](https://doi.org/10.3389/feduc.2021.581216) | q3 · quant-synthesis · r? | i1 · small effect on deep outcomes, d = 0.26 (0.60 surface); far transfer d = 0.39 | this claim |
| Reisslein 2004 | q2 · causal · r2 | i? | [In one 51-learner experiment on help formats in computer-based electrical engineering inst](far-transfer-floor-effect-and-equal-time.md) (supports) |
| Miwa et al. 2017 | q2 · causal · r1 | i? | [Test-score increases occurred only for identical and near-transfer problems; no increases ](germane-load-gains-limited-to-identical-and-near-transfer-problems.md) (supports) |
| Kelly McNeil 2026 | q2 · review · r2 | i? | [The review reports that simulation games support near transfer of knowledge but evidence f](simulation-near-transfer-robust-far-transfer-weak.md) (supports) |
| [Dunlosky 2013](https://doi.org/10.1177/1529100612453266) | q2 · causal · r? | i? | [Self-explanation effects hold on far-transfer but not near-transfer questions in a geometr](self-explanation-far-transfer-geometry-classroom.md) (counts against) |
<!-- synthesis:end -->

## Discussion

A course aiming at understanding or transfer cannot take the headline effects of these techniques at face value. Only 109 of 1,619 effects measured deep outcomes, so the evidence for deep learning is thin rather than negative.

## Related Claims

- [Retrieval Practice Improves Transfer](retrieval-practice-improves-transfer.md) — the general claim this finding bears on, with the studies behind it

- [Across ten learning techniques, distributed practice and practice testing have the largest effects and underlining and summarization the smallest](ten-learning-techniques-ranked-distributed-practice-and-practice-testing-highest.md) — related
