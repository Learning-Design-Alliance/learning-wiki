---
type: claim
title: Retrieval Practice Improves Transfer
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-practice-improves-transfer
evidence_strength: provisional
sources:
  - id: pan-rickard-2018
    resource: "https://doi.org/10.1037/bul0000151"
    title: "Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin, 144*(7), 710–756. [doi:10.1037/bul0000151](https://doi.org/10.1037/bul0000151)"
    author: "Pan, S. C., & Rickard, T. C."
    q: 4
    i: 2
    n: 122 experiments (192 effect sizes, N=10,382)
  - id: butler-2010
    resource: "https://doi.org/10.1037/a0019902"
    title: "Butler, A. C. (2010). Repeated testing produces superior transfer of learning relative to repeated studying. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 36*(5), 1118–1133. [doi:10.1037/a0019902](https://doi.org/10.1037/a0019902)"
    author: Butler, A. C.
    q: 3
    i: "?"
    n: 4 experiments
---

# Retrieval Practice Improves Transfer

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2` medium

Practicing retrieval of learned material (rather than rereading or restudying) improves learners' ability to apply that knowledge to new problems and contexts, not just to recall it verbatim.

## Subclaims

`q4 i2` Across 192 transfer effect sizes, practice testing produced transfer relative to non-testing re-exposure (d = 0.40), but the benefit is greatest for application/inference questions and changed test formats, weakest for rearranged items and untested material, and bias-corrected estimates often show no positive transfer when favourable moderators are absent. [→ Pan & Rickard 2018](#pan-rickard-2018)

`q3 i?` In four experiments with prose passages, repeated testing produced better one-week performance than repeated restudying on new inferential questions, both within the same knowledge domain and across different domains. [→ Butler 2010](#butler-2010)

## Evidence

### Pan & Rickard 2018

Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin, 144*(7), 710–756. [doi:10.1037/bul0000151](https://doi.org/10.1037/bul0000151)

`q4 · meta-analysis` · `i2 · medium effect, d=0.40` · `n=122 experiments (192 effect sizes, N=10,382)`

A random-effects meta-analysis of 67 published and unpublished articles spanning more than 40 years, comparing practice testing with a non-testing re-exposure control on transfer tests. Testing yielded transferable learning overall (d = 0.40, 95% CI [0.31, 0.50]), strongest across test formats, to application and inference questions, and to medical-diagnosis problems, and weakest to rearranged stimulus-response items, to untested material seen during study, and to worked-example problems. Response congruency, elaborated retrieval practice and initial test performance strongly moderated transfer. Publication-bias corrections (PET-PEESE and selection methods) left moderator effects largely intact but substantially reduced the intercept, often indicating no positive transfer when none of those moderators is present — a significant qualification of the unconditional claim.

### Butler 2010

Butler, A. C. (2010). Repeated testing produces superior transfer of learning relative to repeated studying. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 36*(5), 1118–1133. [doi:10.1037/a0019902](https://doi.org/10.1037/a0019902)

`q3 · peer-reviewed experiment` · `i? · no effect size in the abstract read` · `n=4 experiments`

Participants studied prose passages and then either repeatedly restudied them or took repeated tests on them. A week later the final test used the same questions (Experiment 1a), new inferential questions from the same knowledge domain (Experiments 1b and 2), or new inferential questions from different knowledge domains (Experiment 3). Repeated testing produced better retention and transfer than repeated studying in every case, indicating the benefit is not limited to the specific response practised.

## Discussion

**Scope of the claim.** The retrieval-practice literature distinguishes near transfer (applying knowledge to reworded or slightly varied problems) from far transfer (applying it to novel problem types or domains). The strongest documented benefits are for retention and near transfer; evidence for far transfer is thinner and more contested. Designers should treat "retrieval improves transfer" as most defensible when the transfer task shares structural features with the practiced material.

**Mechanism.** Retrieval is hypothesized to improve transfer because it forces learners to reconstruct knowledge and make it accessible under varied cues, rather than merely re-encountering it. Successful retrieval also consolidates memories and can reveal gaps that restudy conceals. This connects to [Spaced practice improves long-term retention](spaced-practice-improves-retention.md) — retrieval and spacing interact multiplicatively, with spaced retrieval producing the largest durable gains.

**Moderators and boundary conditions.** Retrieval practice benefits depend on successful retrieval: if learners fail to retrieve and receive no corrective feedback, the attempt can reinforce errors. Feedback after retrieval, and retrieval tasks that require some reconstruction (short answer, generation) rather than pure recognition, are generally associated with better outcomes — see [Feedback improves learning outcomes](feedback-improves-learning.md). As with [worked examples](../elements/demonstration.md), an expertise dimension likely applies — highly fluent learners may gain little from low-difficulty retrieval, consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md).

**Design implications.** To bias retrieval toward transfer rather than verbatim recall, vary the surface features of retrieval questions so learners must extract the underlying structure, and interleave retrieval across related topics rather than blocking by type. Pure recognition formats (multiple choice) are efficient for retention but provide weaker reconstruction demands than short-answer or generation formats. Successful retrieval also depends on material being within working-memory limits — see [Chunking reduces working memory load](chunking-reduces-working-memory-load.md).

**Open questions.** How retrieval practice supports transfer to genuinely novel problem structures, and how much task variability during retrieval is needed to produce flexible knowledge, remain active research questions. Until evidence entries are added, the strength of this specific transfer claim should be treated as provisional.

## Related Claims

- [Spaced practice improves long-term retention](spaced-practice-improves-retention.md) — spacing and retrieval interact; spaced retrieval is the strongest durable-learning combination
- [Testing improves retention of learned material](testing-effect-improves-retention.md) — the core testing effect on retention, of which transfer is an extension
- [Feedback improves learning outcomes](feedback-improves-learning.md) — feedback after retrieval attempts is a key moderator of retrieval benefits
- [Desirable difficulties enhance learning](desirable-difficulties-enhance-learning.md) — retrieval practice is the canonical desirable difficulty
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — successful retrieval depends on material being within working-memory limits