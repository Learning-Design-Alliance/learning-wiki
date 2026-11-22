---
type: claim
title: In cross-validated vocabulary-app review logs, memory models that use each item's sequence of past recall probabilities and review gaps predicted recall with about a third of half-life regression's error
description: On grouped data from 220 million review logs of a vocabulary app, recurrent-network memory models fed each item's history of outcomes, recall probabilities and review intervals predicted recall probability with a mean absolute error of 0.0307–0.0376, against 0.1070 for half-life regression and 0.0779 for a hand-built state model; the history of recall probabilities did most of the work.
id: review-history-features-cut-recall-prediction-error
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: su-et-al-2023
    resource: "https://doi.org/10.1109/TKDE.2023.3251721"
    title: "Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y. (2023). Optimizing spaced repetition schedule by capturing the dynamics of memory. *IEEE Transactions on Knowledge and Data Engineering, 35*(10), 10085–10097. [doi:10.1109/TKDE.2023.3251721](https://doi.org/10.1109/TKDE.2023.3251721)"
    author: "Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y."
    q: 2
    i: "?"
    n: 220 million review logs, grouped into 71,697 samples
    kind: associational
    rigour: 2
---

# In cross-validated vocabulary-app review logs, memory models that use each item's sequence of past recall probabilities and review gaps predicted recall with about a third of half-life regression's error

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · n=220 million review logs, grouped into 71,697 samples
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

This bears on what an adaptive review tool should record and feed its memory model: the order of past outcomes, how likely recall was at each past review, and the gaps between reviews, not only counts of successes and failures. Recall probability is the predicted chance of recalling an item at a review; half-life is the delay at which it falls to one half.

## Subclaims
`q2 i?` On 5×2-fold cross-validation, GRU-HLR (a recurrent network combined with half-life regression) predicted recall probability with a mean absolute error of 0.0307 and half-life with a symmetric percentage error of 18.88%, against 0.1070 and 76.65% for half-life regression, 0.0779 and 46.35% for the hand-built DHP-HLR model, and 0.3169 and 0.4535 for the fixed Pimsleur and Leitner schedules. [→ Su et al. 2023](#su-et-al-2023)

`q2 i?` In the ablation, adding the history of past recall probabilities (error 0.0309) or of past intervals (0.0328) to the outcome sequence alone (0.0376) reduced error, the recall-probability history more, and adding intervals on top of it changed little (0.0307). [→ Su et al. 2023](#su-et-al-2023)

`q2 i?` The half-life-regression models erred most for half-lives under 16 or over 129 days, and most models erred more above about 141 days, which the authors attribute to sparse data and to learners possibly reviewing outside the app over long gaps. [→ Su et al. 2023](#su-et-al-2023)

## Evidence

### Su et al. 2023

Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y. (2023). Optimizing spaced repetition schedule by capturing the dynamics of memory. *IEEE Transactions on Knowledge and Data Engineering, 35*(10), 10085–10097. [doi:10.1109/TKDE.2023.3251721](https://doi.org/10.1109/TKDE.2023.3251721)

`q2 · observational log data, cross-validated model comparison` · `i? · prediction errors, no standardised effect size` · `n=220 million review logs, grouped into 71,697 samples` · `associational · r2`

The authors collected 220 million review logs from MaiMemo, an app for memorising English vocabulary, and grouped them by word difficulty (ten levels, set by next-day recall after first learning) and review history into 71,697 samples, each with an observed recall rate and fitted half-life (section 5.1.1). They compared nine memory models (Table 4): GRU-HLR with and without the interval history and the recall-probability history, the hand-built DHP-HLR model, half-life regression with and without word identity, and the Pimsleur and Leitner schedules. 20% of the data tuned the network and the other 80% was evaluated by 5×2-fold cross-validation. Mean absolute error of recall probability was 0.0307 for full GRU-HLR, 0.0309 without intervals, 0.0328 without recall probabilities, 0.0376 without either, 0.0779 for DHP-HLR, 0.1070 for half-life regression, 0.1152 for it without word identity, 0.3169 for Pimsleur and 0.4535 for Leitner. The data are observational: the review gaps were those learners took in the app, and the paper does not report the learners' ages or other characteristics. Numbers were read from the authors' accepted manuscript; the published version is cited.

## Discussion

The comparison says which models describe one app's grouped logs best, for one kind of material, not how much a scheduler built on each changes what learners remember. The authors read the ablation as showing that how retrievable an item was at each past review carries the information the interval history carries, and more, since intervals were rounded to whole days. In the same article the hand-built DHP-HLR model's rules were refitted to these data (eqs. 18–19): after a successful recall, new half-life = old half-life × (e^3.25 · d^−0.386 · h^−0.147 · (1 − p)^0.821 + 1), and after a failure, new half-life = e^1.003 · d^−0.152 · h^0.264 · (1 − p)^−0.017. The authors read these, as in their conference version, as a spacing effect (a larger gain after recall at lower recall probability), a diminishing gain as half-life grows, smaller gains for harder words, and, after a failure, a weak effect of difficulty. The recurrent network and the hand-built model disagreed sharply on half-life after a failure at low recall probability (near 800 days against under 16), where data are sparse; the authors judged the hand-built model's value the more plausible. The conference paper on which this article extends (Ye, Su & Cao, 2022, doi:10.1145/3534678.3539081) used logs from the same app and is not independent evidence.

## Related Claims
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related: another log-data comparison of forgetting-curve models
- [The exponential forgetting curve model outperforms the power-law model on MAE and half-life correlation, while the power-law model performs slightly better on AUC](exponential-model-outperforms-power-law-mae-corh.md) — related
- [In a simulation built on vocabulary-app review logs, a cost-minimising review scheduler reached a target number of durable words in fewer days than other schedules under both a hand-built and a neural memory model](cost-minimizing-scheduler-advantage-holds-across-memory-models.md) — the scheduler built on these models
