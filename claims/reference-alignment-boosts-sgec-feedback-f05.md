---
type: claim
title: "Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality"
description: "Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-c..."
id: reference-alignment-boosts-sgec-feedback-f05
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: mengjie-qian-2026
    resource: "https://doi.org/10.2139/ssrn.6588326"
    title: "Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)"
    author: Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Strong GEC reference alignment yields the highest feedback F0.5 (43.69 on LNG, 45.96 on S&I), a 6.4% and 7.8% relative improvement, and is the first approach enabling an end-to-end SGEC system to surpass the partial-cascaded baseline in feedback quality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Training with Strong aligned GEC references achieves F0.5 of 43.69 on LNG and 45.96 on S&I, relative improvements of 6.4% and 7.8% over unaligned references, outperforming both Orig and Mild references in feedback F0.5. [→ Mengjie Qian 2026](#mengjie-qian-2026)

## Evidence

### Mengjie Qian 2026

Mengjie Qian, Rao Ma, Stefano Bannò, Mark J.F. Gales, Kate M. Knill. (2026). End-to-End Spoken Grammatical Error Correction. arXiv. Originally published 2025. [doi:10.2139/ssrn.6588326](https://doi.org/10.2139/ssrn.6588326)

`q2 · i?` · `design · r2`

Feedback evaluation of reference alignment variants for Whispergec+pt large-v2 (Table 6, Section 5.4). The Strong alignment "yields the highest overall scores, with F0.5 reaching 43.69 on LNG and 45.96 on S&I" against Orig F0.5 of 41.08 and 42.62.

> "Strong GEC yields the highest overall scores, with F0.5 reaching 43.69 on LNG and 45.96 on S&I, corresponding to a relative improvement of 6.4% and 7.8%, respectively."

## Discussion


## Related Claims
- [Averaged two-sided edit-confidence filtering combined with Strong reference alignment achieves the best feedback F0.5 (44.73 on LNG, 46.94 on S&I), relative gains of 2.4% and 2.1% over the unfiltered baseline](edit-confidence-filtering-improves-feedback-f05.md) — related
- [Prompt-conditioned end-to-end SGEC, conditioning on a fluent transcription during training and inference, improves WER modestly and raises feedback Precision by 3.54 on LNG and 3.69 on S&I over the non-prompted model](prompt-conditioned-sgec-improves-feedback-precision.md) — related
