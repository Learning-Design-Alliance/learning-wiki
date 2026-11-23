---
type: claim
title: The Cog+Con curriculum schedule (cognitive plus persona-based content ordering) achieves the best target-domain results, while the Interleaved schedule underperforms the other schedules
description: The Cog+Con curriculum schedule (cognitive plus persona-based content ordering) achieves the best target-domain results, while the Interleaved schedule underperforms the other schedules
id: cogcon-best-interleaved-underperforms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: nishit-neema-2025
    resource: "https://doi.org/10.48550/arXiv.2510.26336"
    title: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. [doi:10.48550/arXiv.2510.26336](https://doi.org/10.48550/arXiv.2510.26336)"
    author: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh"
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: nishit-neema-2025-2
    resource: "https://doi.org/10.48550/arXiv.2510.26336"
    title: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. [doi:10.48550/arXiv.2510.26336](https://doi.org/10.48550/arXiv.2510.26336)"
    author: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh"
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The Cog+Con curriculum schedule (cognitive plus persona-based content ordering) achieves the best target-domain results, while the Interleaved schedule underperforms the other schedules

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Among the four tested schedules, Cog+Con delivers the best overall target-domain performance for the 3B model (Macro t 0.4407 vs baseline 0.4108). [→ Nishit Neema 2025](#nishit-neema-2025)
`q2 i?` The Interleaved schedule underperforms the other curriculum schedules, with particularly large drops in mathematics and statistics. [→ Nishit Neema 2025 (2)](#nishit-neema-2025-2)

## Evidence

### Nishit Neema 2025

Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. [doi:10.48550/arXiv.2510.26336](https://doi.org/10.48550/arXiv.2510.26336)

`q2 · i?` · `causal · r1`

Comparison of four curriculum schedules in continual pretraining of Llama 3.2 3B (Table 1, Section 4.2). The article states Cog+Con "delivers the best overall performance"; Table 1 prints Macro t of 0.4407 for Cog+Con versus 0.4108 baseline.

> "Extending this with persona-based content progression inCog+Con delivers the best overall performance, indicating that curriculum design amplifies the benefits of synthetic corpora in continual pretraining."

### Nishit Neema 2025 (2)

Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. [doi:10.48550/arXiv.2510.26336](https://doi.org/10.48550/arXiv.2510.26336)

`q2 · i?` · `causal · r2`

Results section comparison showing the Interleaved schedule "underperforms relative to the other curriculum schedules"; Table 1 prints Interleaved Macro t of 0.4223. No effect size printed.

> "In contrast, theInterleavedschedule, which mixes book sections and QA pairs across domains within training stages, underperforms relative to the other curriculum schedules, with particularly large drops in mathematics and statistics."

## Discussion


## Related Claims
- Target-domain scores rose by more than 2.5 percentage points and non-target-domain scores by 0.4 points from pre-test to post-test after ACER knowledge infusion in the smaller Llama 3.2 1B model, in one uncontrolled pre-post study — related
- After ACER training, non-target MMLU domain scores rose by about 0.7 percentage points and general capabilities did not decline for the 3B model, in one uncontrolled pre-post study — related
- A balanced 1:1 ratio of in-domain synthetic data to general replay data yields the strongest results under the Cog+Con curriculum, with non-target performance dropping as replay proportion decreases — related
- Continual pretraining on ACER synthetic textbook corpora improves target-domain MMLU accuracy by approximately 3 percentage points macro-average, with the largest benefits in microeconomics and econometrics — related
- [Interleaving multiple graphical representations of fractions gave a qualified advantage over blocked practice, mainly on delayed conceptual transfer and for low-prior-knowledge students](interleaved-representations-better-learning.md) — related
- [Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories](interleaving-improves-inductive-learning.md) — related
