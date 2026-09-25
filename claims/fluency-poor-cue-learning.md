---
type: claim
title: Fluency is a poor cue for actual learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: fluency-poor-cue-learning
evidence_strength: moderate
sources:
  - id: carpenter-et-al-2013
    resource: "https://doi.org/10.3758/s13423-013-0442-z"
    title: "Carpenter, S. K., Wilford, M. M., Kornell, N., & Mullaney, K. M. (2013). Appearances can be deceiving: Instructor fluency increases perceptions of learning without increasing actual learning. *Psychonomic Bulletin & Review, 20*(6), 1350–1356. [doi:10.3758/s13423-013-0442-z](https://doi.org/10.3758/s13423-013-0442-z)"
    author: "Carpenter, S. K., Wilford, M. M., Kornell, N., & Mullaney, K. M."
    q: 3
    i: "?"
    n: not stated in the abstract read
  - id: rhodes-castel-2008
    resource: "https://doi.org/10.1037/a0013684"
    title: "Rhodes, M. G., & Castel, A. D. (2008). Memory predictions are influenced by perceptual information: Evidence for metacognitive illusions. *Journal of Experimental Psychology: General, 137*(4), 615–625. [doi:10.1037/a0013684](https://doi.org/10.1037/a0013684)"
    author: "Rhodes, M. G., & Castel, A. D."
    q: 3
    i: "?"
    n: not stated in the abstract read
---

# Fluency is a poor cue for actual learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3` peer-reviewed experiment

Learners often judge how well they have learned something by how easy and fluent it feels to process — but this subjective fluency frequently diverges from actual retention and transfer. The claim concerns fluency *as a metacognitive cue* (judgments of learning), not fluency as a design goal.

## Subclaims

`q3 i?` Undergraduates who watched a fluent instructor predicted they had learned more than those who watched a disfluent one, but recalled no more. Their study time did not change either, so this study shows the illusion misleading self-assessment and does not show it redirecting later study. [→ Carpenter et al. 2013](#carpenter-et-al-2013)

`q3 i?` Words shown in a larger font received higher judgments of learning but were recalled no better. The bias survived repeated study-test cycles and an explicit warning, and it disappeared when the large-font words were made harder to read, which points to encoding fluency as the cause. [→ Rhodes & Castel 2008](#rhodes-castel-2008)

## Evidence

### Carpenter et al. 2013

Carpenter, S. K., Wilford, M. M., Kornell, N., & Mullaney, K. M. (2013). Appearances can be deceiving: Instructor fluency increases perceptions of learning without increasing actual learning. *Psychonomic Bulletin & Review, 20*(6), 1350–1356. [doi:10.3758/s13423-013-0442-z](https://doi.org/10.3758/s13423-013-0442-z)

`q3 · peer-reviewed experiment (two experiments)` · `i? · no effect size in the abstract read` · `n=not stated in the abstract read`

Participants watched one of two short videos of an instructor explaining a science concept. In one video the instructor spoke fluently, stood upright and kept eye contact. In the other, the same instructor slumped, looked away and read haltingly from notes. Perceived learning was significantly higher after the fluent lecture (Experiment 1), and the fluent instructor was rated as more prepared and effective in both experiments. However, lecture fluency did not significantly change how much was learned, and when participants were given the script to study (Experiment 2), their study time did not differ significantly either. This supports the miscalibration half of the claim but not the "misdirects further study" half.

### Rhodes & Castel 2008

Rhodes, M. G., & Castel, A. D. (2008). Memory predictions are influenced by perceptual information: Evidence for metacognitive illusions. *Journal of Experimental Psychology: General, 137*(4), 615–625. [doi:10.1037/a0013684](https://doi.org/10.1037/a0013684)

`q3 · peer-reviewed experiments (multi-experiment laboratory series)` · `i? · no effect size in the abstract read` · `n=not stated in the abstract read`

Participants studied words printed in different font sizes for a free-recall test and made a judgment of learning (JOL) for each word. Larger fonts received higher JOLs, but font size had little relationship to recall. The bias was weaker when more valid cues, such as associative strength, were available. It persisted across several study-test sessions, with a forgetting scale, and after participants were explicitly warned that font size has little effect on memory. Making large-font words harder to read eliminated the effect, which the authors attribute to encoding fluency. The materials were word lists in the laboratory, not classroom content.

## Discussion

**Why fluency misleads.** Fluent processing (legible fonts, repeated rereading, massed practice, well-matched examples) feels like learning, yet conditions that boost in-the-moment fluency often produce *worse* long-term retention than conditions that feel effortful. This is the core of the distinction between performance during instruction and durable learning: desirable difficulties such as [spaced practice](../principles/spaced-practice.md), [retrieval practice](../principles/retrieval-practice.md), and [interleaving](../strategies/interleaving.md) reduce fluency while improving retention [+S], whereas fluent strategies like rereading and massing inflate confidence without durable gains [-S].

**Metacognitive consequences.** Because learners use fluency as a cue when making judgments of learning, they tend to prefer ineffective strategies (rereading, cramming) and to terminate study too early on fluent material [-M]. Instructional designs that make learning *feel* smooth — heavily scaffolded [worked examples](../elements/demonstration.md) never faded, continuous success without retrieval demands — risk producing confident learners with fragile knowledge [~M]. Designers should treat learner reports of ease as a diagnostic warning sign rather than a success signal, and should build in retrieval-based checks that bypass fluency-based self-assessment.

**Boundary conditions.** Fluency is not always deceptive: for very novice learners, reduced extraneous load genuinely does support learning (see [Cognitive load reduction](../principles/cognitive-load-reduction.md)) [+S], and fluency gained through genuine [automaticity](../elements/automaticity.md) in component skills is functional [+S]. The claim targets fluency *as a metacognitive cue for judging learning*, not fluency as a design goal per se. Open questions include how to train learners to discount fluency cues and under what conditions fluency and actual learning dissociate least.

**Design implications.** Practical countermeasures follow directly from the dissociation between felt ease and durable learning: replace self-ratings of confidence with low-stakes retrieval tests; introduce spacing and interleaving even when learners report them as harder [~S]; and frame effortful practice as a sign of learning rather than a signal of failure, since learners who misread disfluency as incompetence often abandon effective strategies [-M].

**Relation to assessment design.** The dissociation also undermines learner-selected study sequences: learners gravitate toward material they can process fluently, which compounds the problem by concentrating effort where it is least needed [-M]. [Assessment for learning](../principles/assessment-for-learning.md) and [adaptive learning](../principles/adaptive-learning.md) approaches that force retrieval and adjust difficulty externally sidestep fluency-based self-selection [+M].

## Related Claims

- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — genuine load reduction can raise fluency without guaranteeing durable learning
- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) — the flip side: disfluency from overload does harm, so effort is not uniformly desirable
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — scaffolding that keeps learning fluent becomes counterproductive as expertise grows
- [Automatic word recognition frees resources for comprehension](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) — a case where fluency is functional rather than deceptive
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) — retrieval-based checks bypass fluency-based self-assessment
- [Cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) — a boundary condition where reduced load genuinely helps novices