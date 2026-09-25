---
type: claim
title: Pretesting enhances learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: pretesting-enhances-learning
evidence_strength: weak
sources:
  - id: richland-kornell-and-kao-2009
    resource: "https://doi.org/10.1037/a0016496"
    title: "Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)"
    author: "Richland, L. E., Kornell, N., & Kao, L. S."
    q: 3
    i: 3
    n: 63 undergraduates (Experiment 1); 5 experiments, ns 59–158
  - id: kornell-hays-and-bjork-2009
    resource: "https://doi.org/10.1037/a0015729"
    title: "Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)"
    author: "Kornell, N., Hays, M. J., & Bjork, R. A."
    q: 3
    i: 2
    n: 25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32
---

# Pretesting enhances learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3` peer-reviewed experiment · `i2`–`i3`

Attempting to answer questions about material before it has been taught — even when those attempts fail — improves retention and transfer of that material relative to studying without a pretest. The claim covers pre-instruction testing on *not-yet-learned* material; it is distinct from retrieval practice on already-learned material.

## Subclaims

`q3 i3` Testing learners on to-be-read educational material before they read it (a "pretest," items answered essentially at floor) produces better retention of that material than giving equivalent extra study time, even though only pretest-failed items are analyzed. [→ Richland Kornell and Kao 2009](#richland-kornell-and-kao-2009)

`q3 i2` Unsuccessful attempts to retrieve an answer, when followed by feedback, enhance subsequent learning of that answer relative to simply studying the same material for an equal amount of time, both for fictional trivia facts and for weak word-associate pairs. [→ Kornell Hays and Bjork 2009](#kornell-hays-and-bjork-2009)

## Evidence

### Richland Kornell and Kao 2009

Richland, L. E., Kornell, N., & Kao, L. S. (2009). The pretesting effect: Do unsuccessful retrieval attempts enhance learning? *Journal of Experimental Psychology: Applied, 15*(3), 243–257. [doi:10.1037/a0016496](https://doi.org/10.1037/a0016496)

`q3 · peer-reviewed multi-experiment lab study` · `i3 · large effect, d=1.1 (Experiment 1)` · `n=63 undergraduates (Experiment 1); 5 experiments, ns 59–158`

Across five experiments, undergraduates read an expository essay on human vision. In the "test" condition they were asked questions about upcoming concepts *before* reading the passage (nearly all answered incorrectly or left blank at pretest); in the "extended study" condition they instead got proportionally more time to read. On a later test of the same material, the pretested group outperformed the extended-study group in every experiment — in Experiment 1, 75% vs. 56% correct, a large effect (d = 1.1) — even though the analysis excluded any item a participant had actually gotten right on the pretest, so the benefit cannot be attributed to successful retrieval. Later experiments ruled out mere attention-direction (emphasizing the same concepts with italics/bold in the study condition) as the explanation, and Experiment 5 found that simply reading the questions without attempting an answer produced a smaller benefit than actually attempting to answer them.

### Kornell Hays and Bjork 2009

Kornell, N., Hays, M. J., & Bjork, R. A. (2009). Unsuccessful retrieval attempts enhance subsequent learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 35*(4), 989–998. [doi:10.1037/a0015729](https://doi.org/10.1037/a0015729)

`q3 · peer-reviewed multi-experiment lab study` · `i2 · medium effect, d=0.58 (Experiment 1)` · `n=25 UCLA undergraduates (Experiment 1); 6 experiments, ns 20–32`

Six experiments tested whether failed retrieval attempts help or hurt later learning, using materials engineered so retrieval would fail: fictional trivia questions (Experiments 1–2, e.g. "What peace treaty ended the Calumet War?") and cue–weak-associate word pairs (Experiments 3–6, e.g. cue "whale," target "mammal"), with any rare correct guesses excluded from analysis. In the test condition participants attempted an answer before being shown it; in the read-only condition the question and answer were simply presented together for the same study time. On a later cued-recall test, the test condition beat the read-only condition in every experiment — in Experiment 1, 41% vs. 31% correct, t(24) = 2.97, p < .01, d = 0.58 — and in Experiment 6, initial wrong guesses ("commission errors") were recalled better than initially blank items, arguing against the idea that producing an incorrect answer is itself harmful.

## Discussion

**Mechanism.** Pretesting is typically explained through productive failure and search-set activation: an unsuccessful attempt to answer a question makes learners aware of gaps in their knowledge, activates related prior knowledge, and focuses attention on the to-be-learned answer during subsequent instruction. The error itself is not harmful — what matters is that the attempt creates a "search set" that the correct answer can then resolve. This connects to [Activation](../principles/activation.md) [+M] and to [Cognitive disequilibrium motivates conceptual change](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M].

**Boundary conditions.** The pretesting benefit appears strongest when the pretest questions are conceptually aligned with the subsequent instruction, when learners receive feedback or corrective instruction after the attempt, and when the material is meaningful rather than arbitrary. Pretests on entirely unrelated material, or pretests that consume so much time that instruction is curtailed, show weaker or no benefits [-W]. Low-stakes framing matters: pretests are diagnostic, not evaluative, and grading them can undermine the exploratory mindset that makes them effective [-W] — see [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S].

**Relation to retrieval practice.** Pretesting differs from standard [retrieval practice](../claims/retrieval-practice-improves-retention.md) [+S]: retrieval practice strengthens already-learned material, whereas pretesting operates on not-yet-learned material and works *despite* failure. Designers should not assume the two effects have identical moderators — in particular, the feedback-and-instruction phase is constitutive of the pretesting effect, not merely an adjunct.

**Design implications.** Practical deployments include opening a unit with two or three conceptually central questions learners cannot yet answer, using diagnostic "warm-up" quizzes in [flipped](../patterns/flipped-classroom.md) or blended settings, and framing pretests explicitly as low-stakes so that guessing is encouraged rather than penalized. Because the benefit depends on subsequent instruction resolving the search set, a pretest without timely, well-aligned instruction is likely wasted time [~M].

**Open questions.** The durability of pretesting benefits over long retention intervals, and their magnitude relative to equivalent time spent studying, remain actively debated in the literature. Until controlled studies are added to the Evidence section above, the strength and generality of this claim should be treated as provisional.

## Related Claims

- [Retrieval practice improves retention](retrieval-practice-improves-retention.md) — the closest cousin; pretesting extends testing effects to pre-instruction attempts
- [Activation improves learning](activation-improves-learning.md) — pretesting is a form of prior-knowledge activation that surfaces gaps
- [Cognitive disequilibrium motivates conceptual change](cognitive-disequilibrium-motivates-conceptual-change.md) — failed pretest attempts create the disequilibrium that instruction then resolves
- [Assessment for learning improves achievement](assessment-for-learning-improves-achievement.md) — pretests as low-stakes, formative rather than evaluative assessment
- [Productive failure improves learning](productive-failure-improves-learning.md) — the broader pattern that failed attempts before instruction can outperform instruction alone