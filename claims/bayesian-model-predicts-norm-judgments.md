---
type: claim
title: "A Bayesian inference model positively predicted participants' judgmental posterior probabilities in Experiment 1, outperforming a frequency-tracking baseline under a rigorous test"
description: "A Bayesian inference model positively predicted participants' judgmental posterior probabilities in Experiment 1, outperforming a frequency-tracking baseline under a rigorous test"
id: bayesian-model-predicts-norm-judgments
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: duan-2026
    resource: "https://doi.org/10.1038/s41539-026-00405-x"
    title: "Duan, J., Guo, X., Zheng, L. & Yin, J. (2026). A Bayesian perspective on observers' inference of group norms. npj Science of Learning. https://doi.org/10.1038/s41539-026-00405-x"
    author: "Duan, J., Guo, X., Zheng, L. & Yin, J."
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# A Bayesian inference model positively predicted participants' judgmental posterior probabilities in Experiment 1, outperforming a frequency-tracking baseline under a rigorous test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Model-derived posterior probabilities positively predicted participants' judgmental posterior probabilities, indicating consistency with Bayesian updating. [→ Duan 2026](#duan-2026)
`q2 i?` Under a more rigorous test adding experimental condition as a random variable, the frequency-tracking model no longer positively predicted responses while the Bayesian model did. [→ Duan 2026](#duan-2026)

## Evidence

### Duan 2026

Duan, J., Guo, X., Zheng, L. & Yin, J. (2026). A Bayesian perspective on observers' inference of group norms. npj Science of Learning. https://doi.org/10.1038/s41539-026-00405-x

`q2 · i?` · `causal · r1`

Bayesian hierarchical linear regression with a random effect per participant on Experiment 1 data (N = 32) showed the reported positive prediction. The frequency-tracking baseline also predicted judgments (β = 0.48) but produced only coarse clustered estimates; with condition as a random variable it failed (Pr (β > 0) = 78.20%) while the Bayesian model continued to predict (Pr (β > 0) = 96.80%).

> "the model-derived posterior probabilities positively predict the participants’ judgmental posterior probabilities, β = 0.69, 95% CrI = [0.29, 1.15], Pr (β > 0) = 100.00%, δt = 8.31."

## Discussion


## Related Claims
- [The Bayesian inference model also positively predicted judgments in Experiment 2 with deviant behaviors present, and the frequency-tracking model failed the rigorous test](bayesian-model-predicts-judgments-with-deviant-behaviors.md) — a narrower finding that bears on this claim
- [In Experiment 2, norm inference remained consistent with Bayesian updating in the presence of deviant behaviors, though 25% norm-consistent behavior pushed posteriors below 0.5](norm-inference-robust-to-deviant-behaviors.md) — related
- [In Experiment 1, posterior probabilities of norm existence increased with the number of norm-consistent behaviors while priors did not differ across conditions](posterior-probabilities-increase-with-norm-consistent-behaviors.md) — related
- [In Experiment 3, norm and desire posterior probabilities followed distinct patterns, and the Independent Effect model best predicted judgments, indicating norm inference is independent of desire inference](norm-inference-independent-of-desire-inference.md) — related
- [Updating degrees of norm-related belief (DKL) increased with the number of norm-consistent behaviors in Experiment 1](dkl-updating-increases-norm-consistent-behaviors.md) — related
