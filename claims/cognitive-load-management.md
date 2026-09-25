---
type: claim
title: Cognitive Load Management
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: cognitive-load-management
evidence_strength:
sources:
  - id: rey-et-al-2019
    resource: "https://doi.org/10.1007/s10648-018-9456-4"
    title: "Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S. (2019). A meta-analysis of the segmenting effect. *Educational Psychology Review, 31*(2), 389–419. [doi:10.1007/s10648-018-9456-4](https://doi.org/10.1007/s10648-018-9456-4)"
    author: "Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S."
    q: 4
    i: "?"
    n: 56 investigations (88 pairwise comparisons)
  - id: barbieri-et-al-2023
    resource: "https://doi.org/10.1007/s10648-023-09745-1"
    title: "Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). A meta-analysis of the worked examples effect on mathematics performance. *Educational Psychology Review, 35*(1), 11. [doi:10.1007/s10648-023-09745-1](https://doi.org/10.1007/s10648-023-09745-1)"
    author: "Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K."
    q: 4
    i: 2
    n: 55 studies (43 articles, 181 effect sizes)
---

# Cognitive Load Management

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q4` pre-registered or meta-analytic · `i2` medium

Managing intrinsic, extraneous, and germane cognitive load — by controlling element interactivity, removing unnecessary processing demands, and scaffolding complex content — protects limited working-memory capacity and improves learning outcomes.

## Subclaims

`q4 i?` Breaking multimedia instruction into learner-paced or system-paced segments, a way of managing intrinsic load, improves retention and transfer by small to medium amounts and lowers overall rated cognitive load. It also lengthens learning time, and learners with high prior knowledge gained more on retention than learners with low prior knowledge. [→ Rey et al. 2019](#rey-et-al-2019)

`q4 i2` Worked examples, the standard technique for cutting unnecessary problem-solving search, give a medium average benefit on mathematics performance from elementary school through postsecondary. The benefit is smaller when the examples come with self-explanation prompts, so the germane-load add-on did not help here. [→ Barbieri et al. 2023](#barbieri-et-al-2023)

## Evidence

### Rey et al. 2019

Rey, G. D., Beege, M., Nebel, S., Wirzberger, M., Schmitt, T. H., & Schneider, S. (2019). A meta-analysis of the segmenting effect. *Educational Psychology Review, 31*(2), 389–419. [doi:10.1007/s10648-018-9456-4](https://doi.org/10.1007/s10648-018-9456-4)

`q4 · meta-analysis` · `i? · described as small to medium; the abstract gives no pooled d` · `n=56 investigations (88 pairwise comparisons)`

This meta-analysis pooled 56 investigations (88 pairwise comparisons) that compared multimedia instruction split into meaningful segments with the same material presented as one continuous unit. Segmenting had small to medium positive effects on retention and transfer. It also reduced overall cognitive load and increased learning time, and the same four effects held when the system, not the learner, set the pace. Contrary to what the expertise reversal effect would predict, learners with high prior knowledge benefited more on retention than learners with little or none. That finding qualifies the idea that load-reducing support always matters most for novices.

### Barbieri et al. 2023

Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). A meta-analysis of the worked examples effect on mathematics performance. *Educational Psychology Review, 35*(1), 11. [doi:10.1007/s10648-023-09745-1](https://doi.org/10.1007/s10648-023-09745-1)

`q4 · meta-analysis (robust variance estimation)` · `i2 · medium effect, g=0.48` · `n=55 studies (43 articles, 181 effect sizes)`

The authors screened 8,033 abstracts and kept 55 experimental and quasi-experimental studies (181 effect sizes) of [worked examples](worked-examples-reduce-novice-search.md) in mathematics, from elementary grades to postsecondary. The average effect on mathematics performance was medium (g = 0.48). It held whether the examples were used for initial skill acquisition or for practice, and correct examples alone worked better than incorrect examples or a mix of the two. Adding self-explanation prompts produced a negative effect compared with worked examples without them. This cuts against the assumption that layering a germane-load activity onto a load-reducing scaffold always adds value.

## Discussion

Cognitive load management is the practical application of [Cognitive Load Theory](../theories/cognitive-load-theory.md): because working memory can hold only a small number of interacting elements, instruction that exceeds this capacity degrades learning — see [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md). Designers manage load in three ways: reducing **intrinsic** load by sequencing and segmenting complex material (chunking, part-whole progression), reducing **extraneous** load by eliminating redundant or poorly integrated presentation (see [Cognitive Load Reduction](../principles/cognitive-load-reduction.md) and [Cognitive Load Reduction Improves Learning](cognitive-load-reduction-improves-learning.md)), and optimizing **germane** load by directing freed capacity toward schema-building activities such as self-explanation and practice.

Key moderators shape when load management helps. The [expertise reversal effect](../theories/expertise-reversal-effect.md) means scaffolds that reduce load for novices (worked examples, high guidance) can become redundant and even harmful for advanced learners, so support must fade as competence grows — see [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md). Prior knowledge activation reduces intrinsic load by providing schemas to which new elements can be attached — see [Activation](activation.md). Offloading sub-skills to automaticity frees capacity for higher-order processing, as with [Automatic word recognition frees resources for comprehension](automatic-word-recognition-frees-resources-for-comprehension.md).

Boundary conditions deserve explicit design attention. Over-reduction of load can backfire: instruction that is too easy or too supportive removes the productive effort that drives schema construction, connecting to the broader finding that desirable difficulties can outperform smoothed-out instruction for durable learning. Load management therefore targets *unnecessary* load, not all effort. Segmenting and sequencing also interact with learner control — learners who skip segments or fail to pace themselves may not receive the intended load reduction.

Open questions include how to measure load reliably in real classrooms (subjective rating scales vs. physiological measures) and how load management interacts with motivation — reducing difficulty too far can undermine engagement and desirable difficulties.

## Related Claims

- [Cognitive Load Reduction Improves Learning](cognitive-load-reduction-improves-learning.md) — the core claim that reducing extraneous load improves outcomes
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — the failure condition this practice guards against
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — a primary mechanism for managing intrinsic load
- [Automatic word recognition frees resources for comprehension](automatic-word-recognition-frees-resources-for-comprehension.md) — automaticity offloads capacity for higher-order learning
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — a canonical load-management technique for novice learners
- [Worked examples can become redundant or counterproductive for advanced learners.](worked-examples-expertise-reversal.md) — the expertise reversal boundary condition on load-reducing scaffolds
- [Activation improves learning](activation-improves-learning.md) — activated prior knowledge supplies schemas that lower intrinsic load