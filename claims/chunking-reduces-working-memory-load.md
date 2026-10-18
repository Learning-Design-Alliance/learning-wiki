---
type: claim
title: Chunking reduces working memory load by grouping information into fewer, more meaningful units.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-04-06
sources:
  - id: miller-1956
    resource: "https://doi.org/10.1037/h0043158"
    title: "Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [https://doi.org/10.1037/h0043158](https://doi.org/10.1037/h0043158)"
    author: Miller, G. A.
    q: 2
    i: "?"
    n: N/A
    kind: review
    rigour: "?"
  - id: cowan-2001
    resource: "https://doi.org/10.1017/S0140525X01003922"
    title: "Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. [https://doi.org/10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922)"
    author: Cowan, N.
    q: 2
    i: "?"
    n: N/A
    kind: review
    rigour: "?"
  - id: thalmann-et-al-2019
    resource: "https://doi.org/10.1037/xlm0000578"
    title: "Thalmann, M., Souza, A. S., & Oberauer, K. (2019). How does chunking help working memory? *Journal of Experimental Psychology: Learning, Memory, and Cognition, 45*(1), 37–55. [https://doi.org/10.1037/xlm0000578](https://doi.org/10.1037/xlm0000578)"
    author: "Thalmann, M., Souza, A. S., & Oberauer, K."
    q: 3
    i: "?"
    n: unspecified
    kind: causal
    rigour: "?"
id: chunking-reduces-working-memory-load
evidence_strength: strong
---

# Chunking reduces working memory load by grouping information into fewer, more meaningful units.

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · 2 review `r?`, 1 causal `r?` · `q2`–`q3`

By recoding discrete elements into larger units they already know (chunks), people hold more in immediate memory. The evidence here is from list-recall experiments: it shows that a chunk frees memory for other material held at the same time, not that it frees resources for comprehension or problem solving, which no study on this page tests.

## Subclaims
`q2 i?` Recoding input into larger chunks lets people stretch the limit on how much information they can hold in immediate memory, a limit Miller found clustering around seven items while withholding judgment on what the recurring seven means. [→ Miller 1956](#miller-1956)
`q2 i?` More recent estimates put the limit closer to three to five chunks for novel material, tightening rather than overturning Miller's estimate. [→ Cowan 2001](#cowan-2001)
`q3 i?` In four list-recall experiments, chunking improved recall of other, unchunked items held at the same time, and chunks early in a list freed capacity for material encoded after them; the benefit depended on chunk size when chunks shared elements, so capacity is not a fixed number of chunks. [→ Thalmann et al. 2019](#thalmann-et-al-2019)

## Evidence

Primary evidence link: https://doi.org/10.1037/h0043158

### Miller 1956

Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [https://doi.org/10.1037/h0043158](https://doi.org/10.1037/h0043158)

`q2 · narrative review of absolute-judgment and immediate-memory experiments (abstract only)` · `i? · no effect size; a review` · `n=N/A` · `review · r?`

Miller reviews experiments on the limits of absolute judgment and of immediate memory, notes that both kinds of limit cluster around seven, and explicitly withholds judgment on whether the recurring seven means anything. His positive proposal is that organising input into chunks, recoding it into fewer and larger units, lets people break or stretch that bottleneck on how much they can remember. The popular reading that working memory holds "7 ± 2 chunks" goes further than the paper does; Cowan (2001) below later put the limit for novel material nearer four.

### Cowan 2001

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. [https://doi.org/10.1017/S0140525X01003922](https://doi.org/10.1017/S0140525X01003922)

`q2 · narrative review: theoretical target article` · `i? · the abstract prints no effect size; the full text may` · `n=N/A` · `review · r?`

A systematic reconsideration of Miller's estimate, arguing that once rehearsal and long-term-memory support are controlled for, the pure capacity limit for novel material is closer to four chunks than seven. The practical consequence for instructional design is that the usable working-memory budget is smaller than Miller's figure suggests, making chunking more important rather than less.

### Thalmann et al. 2019

Thalmann, M., Souza, A. S., & Oberauer, K. (2019). How does chunking help working memory? *Journal of Experimental Psychology: Learning, Memory, and Cognition, 45*(1), 37–55. [https://doi.org/10.1037/xlm0000578](https://doi.org/10.1037/xlm0000578)

`q3 · peer-reviewed experiment` · `i? · the abstract prints no effect size; the full text may` · `n=unspecified` · `causal · r?`

Four experiments on how chunks help working memory. Chunking improved recall not only of the chunked items but of other, unchunked information held at the same time, which the authors read as chunking reducing load. The benefit was independent of chunk size only when chunks were made of unique elements; with overlapping elements, larger chunks helped less, and this held under articulatory suppression, so capacity is not limited to a fixed number of chunks. Chunks early in a list improved recall of later material; chunks at the end did not. The authors conclude that a chunk is retrieved from long-term memory as one compact representation, which frees capacity for material encoded afterwards. The tasks were serial recall of lists; the abstract reports no learning or higher-order outcome (abstract read 2026-10-15).

## Studies bearing on this claim

<!-- synthesis:start -->
*How large should a unit be, and does grouping static material help?* This table gathers the studies behind this claim and the 3 narrower claims that bear on it: **5 distinct studies** (3 causal, 2 review), `q1`–`q3`, 1 of 5 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Miller 1956](https://doi.org/10.1037/h0043158) | q2 · review · r? | i? | this claim |
| [Cowan 2001](https://doi.org/10.1017/s0140525x01003922) | q2 · review · r? | i? | this claim |
| [Thalmann et al. 2019](https://doi.org/10.1037/xlm0000578) | q3 · causal · r? | i? | this claim |
| Furukawa 1978 | q2 · causal · r1 | i1; i? | [Short chunking study outlines produce higher test performance than long chunking study out](short-cso-improves-test-performance.md) (supports); [High CPC students outperform low CPC students only on the delayed posttest under the chunk](cpc-difference-delayed-posttest-only.md) (qualifies) |
| Do 2024 | q1 · causal · r1 | i? | [Deliberate practice can expand short-term memory capacity beyond the conventional seven-it](deliberate-practice-expands-memory-capacity.md) (qualifies) |
<!-- synthesis:end -->

## Discussion
Chunking efficiency is highly dependent on prior knowledge; an expert can form much larger and more meaningful chunks than a novice in the same domain. The chunk must be *meaningful to that learner* — an arbitrary grouping of unrelated items does not reduce load, because each element still has to be held separately.

The clearest demonstration is chess expertise: master players recall real board positions almost perfectly by chunking them into familiar patterns, but show no advantage over novices for randomly arranged pieces, which is evidence that the benefit comes from stored patterns rather than any larger raw capacity (Gobet et al., 2001 — citation carried over from a duplicate page and not yet DOI-verified).

This has a direct design consequence: chunking imposed from outside only helps while the learner cannot yet chunk unaided. Once they can, the same segmented presentation becomes redundant and slows them down, which is the expertise-reversal effect linked below.

**What this does not show.** Many design pages cite this claim for segmenting instruction or grouping content so learners can think about it. No study on this page measures learning, comprehension or problem solving after material was chunked for learners; the experiments measure recall of lists. Carrying the finding to instruction is an extrapolation, and the narrower claims in the table above (Furukawa 1978) are the nearest instructional tests.

## Related Claims

- [Minimal guidance is less effective for novices than explicit instruction](minimal-guidance-less-effective-for-novices.md) — the general claim this finding bears on, with the studies behind it
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](expertise-reversal-effect.md)
- [Clear Structure Improves Learning](clear-structure-improves-learning.md) — related
- [Cognitive Overload Degrades Learning](cognitive-overload-degrades-learning.md) — related
- [Deliberate practice can expand short-term memory capacity beyond the conventional seven-item limit](deliberate-practice-expands-memory-capacity.md) — related
- [Normal adults typically can keep in mind only about 3 or 4 items, a limit replicated across many methods](adult-working-memory-limit-3-4-chunks.md) — related
- [Collaborative learning distributes cognitive load across multiple working memories, aiding learning of high-load tasks](collaborative-learning-collective-working-memory-advantage.md) — related
- [Two subsets of rational-number CCS items demand working memory capacities of 4 or 5 units respectively](rational-number-item-subsets-capacity-demands.md) — related
- [Children's understanding of whole number advances by one developmental level per additional unit of working memory capacity](whole-number-ccs-one-level-per-wm-unit.md) — related
