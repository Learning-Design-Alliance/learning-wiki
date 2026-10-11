---
type: claim
title: "Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026"
description: "Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026"
id: tactutor-guardrail-flags-improve-accept-leak
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: dongjie-yang-2026
    resource: "https://arxiv.org/abs/2608.03952"
    title: "Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952"
    author: Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Post-training improves TACTutor's auxiliary guardrail flags on TACTBench: accept rate rises from 0.603 to 0.872 and leak-or-overhelp falls from 0.346 to 0.026

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the same 78 diagnostic contexts, TACTutor's accept rate increases from 0.603 to 0.872 and its leak-or-overhelp rate falls from 0.346 to 0.026 relative to the backbone. [→ Dongjie Yang 2026](#dongjie-yang-2026)

## Evidence

### Dongjie Yang 2026

Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, and Zixin Chen. (2026). TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring. https://arxiv.org/abs/2608.03952

`q2 · i?` · `design · r2`

Auxiliary judge-flag rates on the TACTBench diagnostic runs (Appendix Table 6), reported as guardrails separate from TACT_Overall. The article states accept rate increases "from 0.603 to 0.872" and leak-or-overhelp falls "from 0.346 to0.026"; no significance test is printed.

> "This post-training raisesTACT_Overallfrom0.629forthebackboneto0.832;the auxiliary flags also improve, with accept rate increasing from 0.603 to 0.872 and leak-or-overhelp falling from 0.346 to0.026."

## Discussion


## Related Claims
- [Taxonomy-guided post-training raises TACTutor's TACT_Overall on TACTBench from 0.629 (backbone) to 0.832, the highest among evaluated models](tactutor-raises-tactbench-overall-0-629-to-0-832.md) — related
- [In a blinded study with 50 learners, TACTutor receives the highest overall mean rating (5.54/7) and is rated above its backbone across all four teaching-behavior dimensions (+0.39 overall)](tactutor-highest-blinded-learner-rating-5-54.md) — related
- [TACTutor shows no degradation relative to its Qwen backbone on external educational benchmarks, with scores rising on MRBench, TutorBench, LongTutor, and DeepTutor](tactutor-no-degradation-external-benchmarks.md) — related
