---
type: claim
title: Retrieval Fails Without Encoding
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: retrieval-fails-without-encoding
evidence_strength:
sources:
  - id: kornell-et-al-2009
    resource: "https://doi.org/10.1037/a0015729"
    title: "Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)"
    author: "Kornell, N., Hays, M. J., & Bjork, R. A."
    q: 3
    i: 2
    n: 25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32
  - id: richland-et-al-2009
    resource: "https://doi.org/10.1037/a0016496"
    title: "Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)"
    author: "Richland, L. E., Kornell, N., & Kao, L. S."
    q: 3
    i: 3
    n: 63 undergraduates (Experiment 1); 5 experiments, ns 59–158
---

# Retrieval Fails Without Encoding

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3` peer-reviewed experiment · `i2`–`i3`

Retrieval practice strengthens memory only for material that was first encoded into long-term memory; if learners never formed a usable memory representation, attempting retrieval produces little or no benefit.

## Subclaims

`q3 i2` Failed retrieval attempts on material with no existing memory trace (fictional trivia questions with no true answer) still improved later recall relative to passive re-reading, but only because every trial ended with the correct answer being shown — the retrieval attempt itself created nothing until that subsequent encoding step occurred. [→ Kornell et al. 2009](#kornell-et-al-2009)

`q3 i3` Testing readers on passage content *before* they had read it ("pretesting") produced better retention than giving equivalent extra study time, but again every pretest was immediately followed by reading the full passage — the unsuccessful retrieval attempt enhanced encoding of the answer that followed it, rather than substituting for encoding. [→ Richland et al. 2009](#richland-et-al-2009)

## Evidence

### Kornell et al. 2009

Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)

`q3 · peer-reviewed multi-experiment lab study` · `i2 · medium effect, d=0.58 (Experiment 1)` · `n=25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32`

Experiment 1: 25 UCLA undergraduates were given fictional trivia questions (invented facts with no true answer, so every "test" trial was guaranteed to be unsuccessful) either in a test condition (attempt to recall before the answer was shown) or a read-only condition (question and answer shown together). Final cued recall was significantly higher for items from the test condition (M=.41) than the read-only condition (M=.31), t(24)=2.97, p<.01, d=0.58. The authors' own reading of this is that the failed attempt enhanced the encoding that occurred when the answer was subsequently presented — the design never tested retrieval with no answer ever supplied, so the result speaks to what retrieval attempts do *to* a following encoding opportunity, not to retrieval practiced in its absence.

### Richland et al. 2009

Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)

`q3 · peer-reviewed multi-experiment lab study` · `i3 · large effect, d=1.1 (Experiment 1)` · `n=63 undergraduates (Experiment 1); 5 experiments, ns 59–158`

Across five experiments, participants read an expository essay about vision. In the "test" condition they were asked about concepts embedded in the essay *before* reading it (guaranteeing an unsuccessful retrieval attempt, since they had not yet encountered the material); in the "extended study" condition they instead got more time to read. Post-test performance on the pretested concepts was better than on the extended-study concepts in every experiment, even analyzing only items the pretest failed to elicit. The pretest was always followed by reading the full passage, so — as in Kornell et al. (2009) — the unsuccessful attempt is shown to enhance the encoding that immediately followed it, not to produce learning by itself.

## Discussion

**Mechanism.** Retrieval practice works by strengthening and making accessible existing memory traces. If the trace is weak, incomplete, or never formed — because the learner skimmed, was distracted, or experienced cognitive overload during initial instruction — retrieval attempts have nothing to consolidate. This places a sequencing constraint on design: meaningful encoding activities (worked examples, explanation, elaboration) must precede or accompany retrieval, not be replaced by it. Where instruction itself exceeds working memory capacity, the resulting trace is too fragile for retrieval to strengthen — see [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) [-S] and [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) [+S].

**Boundary conditions.** The claim does not mean retrieval is useless for novices. Successful retrieval of even partially encoded material can itself serve as a restudy event, and feedback after failed retrieval can support encoding [+M]. The failure mode is retrieval *without* feedback or *before* any exposure — e.g., quizzing students on content never taught, or using pre-tests as the sole instructional event [~M]. Designers should therefore treat retrieval as a consolidation phase layered on top of [worked examples](../elements/demonstration.md) and explicit instruction, not as a substitute for them.

**Design implications.** Sequence instruction encode-first: [worked examples](../elements/demonstration.md), [advance organizers](../elements/advance-organizers.md), or [activation](../elements/activation.md) of prior knowledge before the first retrieval attempt; ensure feedback follows every retrieval attempt, especially failed ones; and treat pre-tests as [activation](activation-improves-learning.md) devices rather than as the sole instructional event. Retrieval-based formats such as [quizzing](../elements/practice.md) and [flashcards](../elements/practice.md) should be scheduled after, not instead of, initial instruction.

**Open questions.** The precise threshold of encoding strength at which retrieval becomes beneficial, and whether failed retrieval followed by feedback outperforms restudy for entirely novel material, remain contested in the literature. This page needs primary evidence entries before its strength rating can be set.

## Related Claims

- [Retrieval practice improves long-term retention.](retrieval-practice-improves-retention.md) — the core testing-effect claim this page bounds
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — overloaded working memory during instruction prevents encoding in the first place
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — a primary cause of encoding failure
- [Activation improves learning.](activation-improves-learning.md) — activating prior knowledge supports initial encoding before retrieval is attempted
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — an encoding-first alternative to premature problem-solving or retrieval
- [Advance organizers improve learning.](advance-organizers-improve-learning.md) — a structure-building device that supports the encoding retrieval depends on