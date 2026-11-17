---
type: claim
title: "Duplicate rows in the ASSISTments dataset artificially boosted DKT's reported performance; removing them negates the claimed gains"
description: "Duplicate rows in the ASSISTments dataset artificially boosted DKT's reported performance; removing them negates the claimed gains"
id: duplicate-rows-negate-dkt-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: kevin-h-wilson-2016
    resource: "https://doi.org/10.48550/arXiv.1604.02336"
    title: "Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)"
    author: Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Duplicate rows in the ASSISTments dataset artificially boosted DKT's reported performance; removing them negates the claimed gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Duplicate rows arising when a single interaction is aligned with multiple skills gave models processing all skills simultaneously access to ground truth, and DKT's performance gains over prior results disappeared once duplicates were removed. [→ Kevin H. Wilson 2016](#kevin-h-wilson-2016)

## Evidence

### Kevin H. Wilson 2016

Kevin H. Wilson, Yan Karklin, Bojian Han, Chaitanya Ekanadham. (2016). Back to the basics: Bayesian extensions of IRT outperform neural networks for proficiency estimation. arXiv:1604.02336v2 [cs.AI]. [doi:10.48550/arXiv.1604.02336](https://doi.org/10.48550/arXiv.1604.02336)

`q2 · i?` · `design · r2`

Re-analysis of the ASSISTments skill-builder dataset (346,740 interactions, 4,097 users). Duplicate rows account for approximately 25% of rows; the authors reproduced the previously reported AUC of 0.86 only when duplicates were left in the raw data.

> "Indeed, we observed that the performance gains of DKT are negated when these duplicates are removed (see Section 5)."

## Discussion


## Related Claims
- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](pkt-attention-softmax-dimension-causal-flaw.md) — related
