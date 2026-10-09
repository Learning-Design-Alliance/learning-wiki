---
type: claim
title: Pretesting enhances learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: pretesting-enhances-learning
aliases: [pretesting-improves-retention, retrieval-fails-without-encoding]
evidence_strength: weak
sources:
  - id: richland-kornell-and-kao-2009
    resource: "https://doi.org/10.1037/a0016496"
    title: "Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)"
    author: "Richland, L. E., Kornell, N., & Kao, L. S."
    q: 3
    i: 3
    n: 63 undergraduates (Experiment 1); 5 experiments, ns 59–158
    kind: causal
    rigour: "?"
  - id: kornell-hays-and-bjork-2009
    resource: "https://doi.org/10.1037/a0015729"
    title: "Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)"
    author: "Kornell, N., Hays, M. J., & Bjork, R. A."
    q: 3
    i: 2
    n: 25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32
    kind: causal
    rigour: 1
---

# Pretesting enhances learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1` · `q3` · `i2`–`i3`

Attempting to answer questions about material before it has been taught — even when those attempts fail — improves later retention of that material relative to studying for the same time without a pretest, provided the attempt is followed by the answer or the instruction. The two multi-experiment laboratory studies recorded here (undergraduates; expository text, fictional trivia and word pairs) test retention, not transfer.
<!-- deprecated wording (2026-10-05, overstated its evidence): ...improves retention and transfer of that material relative to studying without a pretest. --> The claim covers pre-instruction testing on *not-yet-learned* material; it is distinct from retrieval practice on already-learned material.

## Subclaims

`q3 i3` Testing learners on to-be-read educational material before they read it (a "pretest," items answered essentially at floor) produces better retention of that material than giving equivalent extra study time, even though only pretest-failed items are analyzed. [→ Richland Kornell and Kao 2009](#richland-kornell-and-kao-2009)

`q3 i2` Unsuccessful attempts to retrieve an answer, when followed by feedback, enhance subsequent learning of that answer relative to simply studying the same material for an equal amount of time, both for fictional trivia facts and for weak word-associate pairs. [→ Kornell Hays and Bjork 2009](#kornell-hays-and-bjork-2009)

`q3 i2` Failed retrieval attempts on material with no existing memory trace (fictional trivia questions with no true answer) still improved later recall relative to reading the question and answer together for the same time; every trial ended with the correct answer shown, and no condition without the answer was tested, so the study shows the attempt enhancing the encoding that followed it and does not show what an attempt does without one. [→ Kornell et al. 2009](#kornell-hays-and-bjork-2009)
<!-- deprecated (2026-10-05, overstated its evidence): Failed retrieval attempts on material with no existing memory trace (fictional trivia questions with no true answer) still improved later recall relative to passive re-reading, but only because every trial ended with the correct answer being shown — the retrieval attempt itself created nothing until that subsequent encoding step occurred. [→ Kornell et al. 2009](#kornell-hays-and-bjork-2009) -->

`q3 i3` Testing readers on passage content *before* they had read it ("pretesting") produced better retention than giving equivalent extra study time; every pretest was followed by reading the full passage, so the study shows the unsuccessful attempt enhancing the reading that followed it, and does not test a pretest without that reading. [→ Richland et al. 2009](#richland-kornell-and-kao-2009)
<!-- deprecated (2026-10-05, overstated its evidence): Testing readers on passage content *before* they had read it ("pretesting") produced better retention than giving equivalent extra study time, but again every pretest was immediately followed by reading the full passage — the unsuccessful retrieval attempt enhanced encoding of the answer that followed it, rather than substituting for encoding. -->

## Evidence

### Richland Kornell and Kao 2009

Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)

`q3 · peer-reviewed multi-experiment lab study` · `i3 · large effect, d=1.1 (Experiment 1)` · `n=63 undergraduates (Experiment 1); 5 experiments, ns 59–158` · `causal · r?`

Across five experiments, undergraduates read an expository essay on human vision. In the "test" condition they were asked questions about upcoming concepts *before* reading the passage (nearly all answered incorrectly or left blank at pretest); in the "extended study" condition they instead got proportionally more time to read. On a later test of the same material, the pretested group outperformed the extended-study group in every experiment — in Experiment 1, 75% vs. 56% correct, a large effect (d = 1.1) — even though the analysis excluded any item a participant had actually gotten right on the pretest, so the benefit cannot be attributed to successful retrieval. Later experiments ruled out mere attention-direction (emphasizing the same concepts with italics/bold in the study condition) as the explanation, and Experiment 5 found that simply reading the questions without attempting an answer produced a smaller benefit than actually attempting to answer them.

<!-- merged 2026-10-05: a second write-up of this study, kept verbatim. It came from retrieval-fails-without-encoding; same citation, DOI (Crossref: "The pretesting effect: Do unsuccessful retrieval attempts enhance learning?", Richland 2009) and codes as the entry above.
### Richland et al. 2009

Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)

`q3 · peer-reviewed multi-experiment lab study` · `i3 · large effect, d=1.1 (Experiment 1)` · `n=63 undergraduates (Experiment 1); 5 experiments, ns 59–158` · `causal · r?`

Across five experiments, participants read an expository essay about vision. In the "test" condition they were asked about concepts embedded in the essay *before* reading it (guaranteeing an unsuccessful retrieval attempt, since they had not yet encountered the material); in the "extended study" condition they instead got more time to read. Post-test performance on the pretested concepts was better than on the extended-study concepts in every experiment, even analyzing only items the pretest failed to elicit. The pretest was always followed by reading the full passage, so — as in Kornell et al. (2009) — the unsuccessful attempt is shown to enhance the encoding that immediately followed it, not to produce learning by itself.
-->

### Kornell Hays and Bjork 2009

Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)

`q3 · peer-reviewed multi-experiment lab study` · `i2 · medium effect, d=0.58 (Experiment 1)` · `n=25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32` · `causal · r1`

Six experiments tested whether failed retrieval attempts help or hurt later learning, using materials engineered so retrieval would fail: fictional trivia questions (Experiments 1–2, e.g. "What peace treaty ended the Calumet War?") and cue–weak-associate word pairs (Experiments 3–6, e.g. cue "whale," target "mammal"), with any rare correct guesses excluded from analysis. In the test condition participants attempted an answer before being shown it; in the read-only condition the question and answer were simply presented together for the same study time. On a later cued-recall test, the test condition beat the read-only condition in every experiment — in Experiment 1, 41% vs. 31% correct, t(24) = 2.97, p < .01, d = 0.58 — and in Experiment 6, initial wrong guesses ("commission errors") were recalled better than initially blank items, arguing against the idea that producing an incorrect answer is itself harmful.

<!-- merged 2026-10-05: a second write-up of this study, kept verbatim. It came from retrieval-fails-without-encoding; same citation, DOI (Crossref: "Unsuccessful retrieval attempts enhance subsequent learning.", Kornell 2009) and codes as the entry above.
### Kornell et al. 2009

Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)

`q3 · peer-reviewed multi-experiment lab study` · `i2 · medium effect, d=0.58 (Experiment 1)` · `n=25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32` · `causal · r1`

Experiment 1: 25 UCLA undergraduates were given fictional trivia questions (invented facts with no true answer, so every "test" trial was guaranteed to be unsuccessful) either in a test condition (attempt to recall before the answer was shown) or a read-only condition (question and answer shown together). Final cued recall was significantly higher for items from the test condition (M=.41) than the read-only condition (M=.31), t(24)=2.97, p<.01, d=0.58. The authors' own reading of this is that the failed attempt enhanced the encoding that occurred when the answer was subsequently presented — the design never tested retrieval with no answer ever supplied, so the result speaks to what retrieval attempts do *to* a following encoding opportunity, not to retrieval practiced in its absence.
-->

## Discussion

**Mechanism.** Pretesting is typically explained through productive failure and search-set activation: an unsuccessful attempt to answer a question makes learners aware of gaps in their knowledge, activates related prior knowledge, and focuses attention on the to-be-learned answer during subsequent instruction. The error itself is not harmful — what matters is that the attempt creates a "search set" that the correct answer can then resolve. This connects to [Activation](../principles/activation.md) [+M] and to [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M].

**Boundary conditions.** The pretesting benefit appears strongest when the pretest questions are conceptually aligned with the subsequent instruction, when learners receive feedback or corrective instruction after the attempt, and when the material is meaningful rather than arbitrary. Pretests on entirely unrelated material, or pretests that consume so much time that instruction is curtailed, show weaker or no benefits [-W]. Low-stakes framing matters: pretests are diagnostic, not evaluative, and grading them can undermine the exploratory mindset that makes them effective [-W] — see [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S].

**Relation to retrieval practice.** Pretesting differs from standard [retrieval practice](../claims/retrieval-practice-improves-retention.md) [+S]: retrieval practice strengthens already-learned material, whereas pretesting operates on not-yet-learned material and works *despite* failure. Designers should not assume the two effects have identical moderators — in particular, the feedback-and-instruction phase is constitutive of the pretesting effect, not merely an adjunct.

**Design implications.** Practical deployments include opening a unit with two or three conceptually central questions learners cannot yet answer, using diagnostic "warm-up" quizzes in [flipped](../patterns/flipped-classroom.md) or blended settings, and framing pretests explicitly as low-stakes so that guessing is encouraged rather than penalized. Because the benefit depends on subsequent instruction resolving the search set, a pretest without timely, well-aligned instruction is likely wasted time [~M].

**Open questions.** The durability of pretesting benefits over long retention intervals, and their magnitude relative to equivalent time spent studying, remain actively debated in the literature. Two multi-experiment laboratory studies are recorded above (Richland et al. 2009, five experiments with expository text; Kornell et al. 2009, six with trivia and word pairs), both with undergraduates and short retention intervals; classroom studies, long delays and transfer are not yet recorded.
<!-- deprecated (2026-10-05, stale): Until controlled studies are added to the Evidence section above, the strength and generality of this claim should be treated as provisional. -->

*Merged from “Pretesting Improves Retention” (pretesting-improves-retention):* **The pretesting (prequestioning) effect.** Failed retrieval attempts before instruction appear to prime learners to encode the corrective information presented afterward. The dominant explanations are search-set activation — the pretest activates related prior knowledge and narrows what learners look for in the to-be-learned material — and productive failure, in which the experience of not knowing creates a gap that subsequent instruction fills. Both accounts predict that the pretest need not be answered correctly to confer a benefit, which distinguishes pretesting from [activation](../principles/activation.md) aimed only at surfacing prior knowledge.

**Scope and moderators.** The effect has been reported most consistently for verbal, fact-like material (word pairs, trivia, expository text) and for relatively short retention intervals. Whether pretesting benefits transfer or complex-skill learning, and whether gains persist over long delays, remain open questions. Feedback after the pretest is likely important: without corrective information, a failed guess may entrench errors rather than prime correction — a boundary condition shared with claims about when [retrieval practice](../strategies/retrieval_practice.md) helps and when errors persist.

**Practical form.** Pretests should be low- or no-stakes, brief, and on the same content as the upcoming instruction. They pair naturally with [retrieval practice](../strategies/retrieval_practice.md) during and after instruction, forming a test–study–test cycle. In classroom settings, brief prequestions embedded at the start of a lesson or online module are the lowest-cost implementation.

**Constraints.** Pretesting gains shrink or vanish when the pretest targets content unrelated to the subsequent instruction [-M], when no corrective feedback or instruction follows the failed attempt [-M], and possibly when learners lack enough prior knowledge to generate even plausible guesses [~W]. High-stakes pretests can also induce anxiety and discourage the productive guessing the effect depends on [-W].

**Single-family limitation.** The page documents two peer-reviewed laboratory studies from overlapping authors (Kornell is on both), so the evidence here is one research programme's; independent replications are not yet recorded.
<!-- deprecated (2026-10-05, stale): **Single-family limitation.** Until peer-reviewed studies are added to Evidence, this claim should be treated as emerging: the effect is well known in the literature but this page does not yet document its evidentiary basis. -->

*Merged from “Retrieval Fails Without Encoding” (retrieval-fails-without-encoding):* (That page's title overstated its evidence: its two studies, now the entries above, show unsuccessful retrieval attempts *followed by the answer* enhancing learning; neither tests retrieval with no encoding at all. The paragraphs below are its argument, not findings of those studies.) **Mechanism.** Retrieval practice works by strengthening and making accessible existing memory traces. If the trace is weak, incomplete, or never formed — because the learner skimmed, was distracted, or experienced cognitive overload during initial instruction — retrieval attempts have nothing to consolidate. This places a sequencing constraint on design: meaningful encoding activities (worked examples, explanation, elaboration) must precede or accompany retrieval, not be replaced by it. Where instruction itself exceeds working memory capacity, the resulting trace is too fragile for retrieval to strengthen — see [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) [-S] and [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) [+S].

**Boundary conditions.** The claim does not mean retrieval is useless for novices. Successful retrieval of even partially encoded material can itself serve as a restudy event, and feedback after failed retrieval can support encoding [+M]. The failure mode is retrieval *without* feedback or *before* any exposure — e.g., quizzing students on content never taught, or using pre-tests as the sole instructional event [~M]. Designers should therefore treat retrieval as a consolidation phase layered on top of [worked examples](../elements/demonstration.md) and explicit instruction, not as a substitute for them.

**Design implications.** Sequence instruction encode-first: [worked examples](../elements/demonstration.md), [advance organizers](../elements/advance-organizers.md), or [activation](../elements/activation.md) of prior knowledge before the first retrieval attempt; ensure feedback follows every retrieval attempt, especially failed ones; and treat pre-tests as [activation](activation-improves-learning.md) devices rather than as the sole instructional event. Retrieval-based formats such as [quizzing](../elements/practice.md) and [flashcards](../elements/practice.md) should be scheduled after, not instead of, initial instruction.

**Open questions.** The precise threshold of encoding strength at which retrieval becomes beneficial remains contested. For entirely novel material, Kornell et al. (2009) found failed retrieval followed by the answer beat equal-time reading (fictional trivia, d = 0.58 in Experiment 1), though in the laboratory and over short intervals.
<!-- deprecated (2026-10-05, stale): The precise threshold of encoding strength at which retrieval becomes beneficial, and whether failed retrieval followed by feedback outperforms restudy for entirely novel material, remain contested in the literature. This page needs primary evidence entries before its strength rating can be set. -->

## Related Claims

- [Retrieval practice improves retention](retrieval-practice-improves-retention.md) — the closest cousin; pretesting extends testing effects to pre-instruction attempts
- [Activation improves learning](activation-improves-learning.md) — pretesting is a form of prior-knowledge activation that surfaces gaps
- [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](cognitive-disequilibrium-motivates-conceptual-change.md) — failed pretest attempts create the disequilibrium that instruction then resolves
- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — pretests as low-stakes, formative rather than evaluative assessment
- [Productive failure improves learning](productive-failure-improves-conceptual-learning.md) — the broader pattern that failed attempts before instruction can outperform instruction alone
- [Retrieval practice](../strategies/retrieval_practice.md) — the strategy page covering test–study–test cycles
- [Pre-tests reduced adult learners' persistence in a MOOC, though they improved post-test scores among those who completed it](pretesting-can-harm-motivation.md) — related
- [Feedback Enhances Retrieval Practice](feedback-enhances-retrieval-practice.md) — related
- [Retrieval Failure Reduces Benefit](retrieval-failure-reduces-benefit.md) — related
- [Question prompts improve learning](question-prompts-improve-learning.md) — related
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — overloaded working memory during instruction prevents encoding in the first place
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — a primary cause of encoding failure
- [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) — an encoding-first alternative to premature problem-solving or retrieval
- [Advance organizers improve learning.](advance-organizers-improve-learning.md) — a structure-building device that supports the encoding retrieval depends on
- [Retrieval practice effects on mediator-cued final tests have been positive, but Coppens et al. (2016) concluded the true effect may be only about 0.10 to 0.20](mediator-cued-final-test-effects-of-retrieval-practice-may-be-small.md) — related
- [Two-part collaborative assessment, individual then group answering, transforms summative testing into a learning experience and may reduce test anxiety](two-part-collaborative-assessment-learning-experience.md) — related
