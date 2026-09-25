---
type: claim
title: Spaced Retrieval Outperforms Restudy
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: spaced-retrieval-outperforms-restudy
evidence_strength: pending
sources:
  - id: latimier-et-al-2021
    resource: "https://doi.org/10.1007/s10648-020-09572-8"
    title: "Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)"
    author: "Latimier, A., Peyre, H., & Ramus, F."
    q: 4
    i: 2
    n: 39 effect sizes (subset 1)
---

# Spaced Retrieval Outperforms Restudy

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q4` pre-registered or meta-analytic · `i2` medium · n=39 effect sizes (subset 1)

Retrieving information from memory at spaced intervals produces stronger, longer-lasting retention than re-reading or restudying the same material. The claim concerns the *interaction* of spacing and retrieval — not either effect alone.

## Subclaims

`q4 i2` A meta-analysis of 29 studies finds that spacing out retrieval-practice episodes produces meaningfully better long-term retention than massing them, but the underlying studies compare spaced vs. massed retrieval practice rather than retrieval practice vs. restudy, so this evidence supports the spacing half of the claim more directly than the retrieval-vs-restudy half. [→ Latimier et al. 2021](#latimier-et-al-2021)

## Evidence

### Latimier et al. 2021

Latimier, A., Peyre, H., & Ramus, F. (2021). A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention. *Educational Psychology Review, 33*(3), 959–987. [doi:10.1007/s10648-020-09572-8](https://doi.org/10.1007/s10648-020-09572-8)

`q4 · meta-analysis (robust variance estimation over 29 studies)` · `i2 · medium effect, g=0.74` · `n=39 effect sizes (subset 1)`

Meta-analysis of 29 studies on spaced retrieval practice, split into two subsets to answer two questions. Subset 1 (39 aggregated effect sizes) tested whether spaced retrieval practice produces better final-retention memory than massed retrieval practice, and found a benefit for spacing (Hedges' g = 0.74). Subset 2 (54 effect sizes) tested whether an expanding spacing schedule beats a uniform one during retrieval practice and found no reliable difference (g = 0.034); the number of retrieval exposures per item moderated this null result. Note the comparator in subset 1 is *massed* retrieval practice, not passive restudy/re-reading — the meta-analysis establishes that spacing matters within retrieval practice, and does not itself contrast retrieval practice against restudy.

## Discussion

**Why the combination matters.** Spacing and retrieval are each powerful individually, but the claim here concerns their interaction: retrieval attempts spaced over time force effortful reconstruction of memory at successive points, which is theorized to strengthen retrieval routes more than passive restudy at either spaced or massed intervals. The mechanism is usually framed in terms of [information processing theory](../theories/information-processing-theory.md) — successful retrieval modifies the memory trace in ways restudy does not — and relates to working-memory constraints described in [chunking reduces working memory load](chunking-reduces-working-memory-load.md).

**Boundary conditions to expect.** The literature on this claim generally indicates the advantage depends on successful or near-successful retrieval: if learners cannot retrieve anything, a retrieval attempt may add little or even entrench errors [-M], and very long spacing intervals can make retrieval so difficult that it fails [-M]. Feedback after retrieval attempts is typically treated as a moderator — see [feedback improves learning](../claims/feedback-improves-learning.md) for the general case. These conditions should be documented here once evidence entries are added.

**Open questions.** Optimal spacing intervals relative to the retention interval, durability of the effect beyond laboratory materials, and how the effect interacts with learner expertise all remain to be specified with cited evidence on this page. The expertise question parallels the [expertise reversal effect](../theories/expertise-reversal-effect.md): retrieval demands that benefit novices may impose unnecessary load on advanced learners [~M], and the [cognitive overload degrades learning](cognitive-overload-degrades-learning.md) page describes the general failure mode when task difficulty exceeds available capacity.

**Design implication.** The one meta-analysis recorded above compares spaced with massed retrieval, not retrieval with restudy, so the "outperforms restudy" half of this claim still rests on the separate testing-effect literature. Practitioners should pair spaced retrieval with feedback and success rates high enough that retrieval attempts are effortful but achievable. In practice this means scheduling retrieval attempts at expanding or fixed intervals across sessions rather than within one sitting, keeping initial retrieval success rates moderate (learners should sometimes struggle but usually succeed), and correcting errors immediately after each attempt.

## Related Claims

- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — working-memory constraints shape how much can be successfully retrieved in one attempt
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — overly difficult retrieval attempts can exceed available capacity
- [Active learning improves exam performance](active-learning-improves-exam-performance.md) — retrieval practice is a form of active learning with direct assessment consequences
- [Feedback improves learning](../claims/feedback-improves-learning.md) — feedback after retrieval attempts is a key moderator of whether errors are corrected or entrenched
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — retrieval demands that help novices may become counterproductive for advanced learners