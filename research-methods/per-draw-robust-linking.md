---
type: research-method
id: per-draw-robust-linking
title: Per-draw robust linking
description: The linking step maps each independently calibrated period to a common reference metric by minimizing a response-count-weighted pseudo-Huber (robust Haebara) discrepancy between expected-score curves on anchor items.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Per-draw robust linking

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The linking step maps each independently calibrated period to a common reference metric by minimizing a response-count-weighted pseudo-Huber (robust Haebara) discrepancy between expected-score curves on anchor items. Following Baldwin (2011), the criterion is minimized separately for each posterior draw rather than once at the posterior mean; the article states that "Applying it draw-wise propagates the linking uncertainty, together with its dependence on the item parameters, into the linked posteriors." Weighting anchors by response count lets better-estimated items contribute more to the link, approximating concurrent calibration.

## Accounts
<!-- How each source describes or uses the method -->
- **Per-draw robust linking: solving a response-count-weighted robust Haebara criterion separately for each posterior draw propagates linking uncertainty into the linked posteriors**: The linking step maps each independently calibrated period to a common reference metric by minimizing a response-count-weighted pseudo-Huber (robust Haebara) discrepancy between expected-score curves on anchor items. Following Baldwin (2011), the criterion is minimized separately for each posterior draw rather than once at the posterior mean; the article states that "Applying it draw-wise propagates the linking uncertainty, together with its dependence on the item parameters, into the linked posteriors." Weighting anchors by response count lets better-estimated items contribute more to the link, approximating concurrent calibration. (Paul A. Jewsbury et al. (2026))

### Claims
- [Consensus calibration closely reproduces pooled-benchmark item-parameter means and standard deviations on an operational assessment](../claims/consensus-posterior-agrees-with-pooled-benchmark.md) [+M]

## Related Research Methods
-

## Key Sources
- Paul A. Jewsbury and Steven W. Nydick and Manqian Liao and Siyuan (Marco) Chen. (2026). Bayesian Consensus Calibration of Continuously Evolving IRT Item Banks. https://arxiv.org/abs/2609.13590v1
