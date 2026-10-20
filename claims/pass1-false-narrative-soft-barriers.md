---
type: claim
title: "Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures"
description: "Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures"
id: pass1-false-narrative-soft-barriers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: pass1-analysis
    title: pass1-analysis
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Pass@1 is not a sufficient success metric for soft barriers because it conflates successful barriers with model generation failures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` A drop in Pass@1 under intervention does not necessarily mean the barrier failed, since both successful barriers and model failures reduce Pass@1 with opposite meanings. [→ pass1-analysis](#pass1-analysis)

## Evidence

### pass1-analysis

Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, and Tegawendé F. Bissyandé. 2026. Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming. Proceedings of the 41st IEEE/ACM International Conference on Automated Software Engineering (ASE '26). https://doi.org/10.1145/3832783.3834554

`q2 · i?` · `causal · r1`

Analysis of the same automated outputs under the handoff lens, reported in Section 4. The paper notes "Claude with invisible characters on MBPP has very low Pass@1 under intervention, yet its CPR is 0.997", showing Pass@1 alone misreads barrier success as failure.

> "Claude with invisible characters on MBPP has very low Pass@1 under intervention, yet its CPR is 0.997."

## Discussion


## Related Claims
- [Incorporating example problems does not necessarily improve LLM teaching and can degrade it via a shift to example-specific error correction](example-problems-degrade-llm-teaching.md) — related
- [Differences in student pass-rate distributions between test splits explain the smaller INSIDE-over-SFT improvement on test_NP](pass-rate-distribution-explains-split-gap.md) — related
- [Output-level Unicode soft barriers can achieve high copy-paste resistance, but effectiveness is highly model- and task-dependent](soft-barriers-cpr-model-task-dependent.md) — related
- [In an exploratory pilot, a soft barrier shifted participants from direct copying toward editing, understanding, and iterative resubmission without preventing task completion](soft-barrier-shifts-users-toward-editing.md) — related
