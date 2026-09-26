---
type: claim
title: Annotating improves learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: annotating-improves-learning
evidence_strength:
sources:
  - id: ponce-et-al-2022
    resource: "https://doi.org/10.1007/s10648-021-09654-1"
    title: "Ponce, H. R., Mayer, R. E., & Méndez, E. E. (2022). Effects of learner-generated highlighting and instructor-provided highlighting on learning from text: A meta-analysis. *Educational Psychology Review, 34*(2), 989–1024. [doi:10.1007/s10648-021-09654-1](https://doi.org/10.1007/s10648-021-09654-1)"
    author: "Ponce, H. R., Mayer, R. E., & Méndez, E. E."
    q: 4
    i: 1
    n: 36 articles (85 effect sizes)
  - id: dunlosky-et-al-2013
    resource: "https://doi.org/10.1177/1529100612453266"
    title: "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)"
    author: "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T."
    q: 3
    i: "?"
    n: 10 techniques reviewed
---

# Annotating improves learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i1` small

Learners who actively mark up texts — highlighting, underlining, margin notes, and other generative annotations — tend to process material more deeply than passive readers. The scope of this claim covers learner-generated annotations on text and multimedia, not instructor-supplied annotations.

## Subclaims

`q4 i1` Asking learners to highlight or underline important material while reading improves memory for the text (average effect size 0.36) but not comprehension (0.20), and helps college students but not school students; this covers highlighting only, not elaborative margin notes. [→ Ponce et al. 2022](#ponce-et-al-2022)

`q3 i?` A review of ten common study techniques rated highlighting and underlining as low utility, which qualifies any general claim that unguided marking of text improves learning. [→ Dunlosky et al. 2013](#dunlosky-et-al-2013)

## Evidence

### Ponce et al. 2022

Ponce, H. R., Mayer, R. E., & Méndez, E. E. (2022). Effects of learner-generated highlighting and instructor-provided highlighting on learning from text: A meta-analysis. *Educational Psychology Review, 34*(2), 989–1024. [doi:10.1007/s10648-021-09654-1](https://doi.org/10.1007/s10648-021-09654-1)

`q4 · meta-analysis` · `i1 · small effect, 0.36 on memory; 0.20 on comprehension` · `n=36 articles (85 effect sizes)`

A meta-analysis of experiments, published between 1938 and 2019, in which college or K-12 students read an academic text either with or without being asked to highlight important material (or with or without the important material already highlighted by the instructor), and then took memory or comprehension tests. When learners did the [highlighting](../elements/text-underlining-and-annotating.md) themselves, memory improved (average effect size 0.36) but comprehension did not (0.20). The benefit held for college students (0.39) but not for school students (0.24). Highlighting supplied by the instructor did better, improving both memory and comprehension (0.44 each). Read from the abstract only. The study covers highlighting and underlining, not other kinds of annotation such as written margin notes.

### Dunlosky et al. 2013

Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques: Promising directions from cognitive and educational psychology. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)

`q3 · narrative review of experimental literature` · `i? · no pooled effect size reported` · `n=10 techniques reviewed`

A long review that asks, for each of ten study techniques, whether its benefits hold up across different learning conditions, types of student, materials and tests. Highlighting (or underlining) was one of five techniques rated low utility, along with summarization, the keyword mnemonic, imagery use for text learning and rereading. Practice testing and distributed practice were rated high utility. This counts against the claim for unguided highlighting in particular. It does not test more elaborative annotation. Read from the Crossref-deposited abstract only.

## Discussion

**Mechanism.** Annotating is a generative activity: it forces selection of important information and connection of it to prior knowledge, consistent with generative theories of learning. It also produces an external record that supports later review and retrieval practice. Annotation quality likely matters more than quantity — superficial highlighting without elaboration can create an illusion of fluency, and re-reading highlighted text is among the weaker study strategies in the learning-techniques literature.

**Moderators to establish.** Open questions include whether benefits depend on learner expertise (novices may highlight the wrong things), whether structured prompts or annotation schemes (e.g., genre-based or rhetorical annotation) outperform free-form marking, and whether benefits persist on delayed tests rather than immediate ones. Studies are needed across domains, media (print vs. digital annotation), and age groups before a strength rating can be assigned.

**Boundary conditions.** Annotation may impose extraneous load when the text is already dense or the learner lacks the background to judge relevance; in such cases, guided or scaffolded annotation is likely preferable to unguided marking. This parallels the expertise-reversal pattern documented for other scaffolds: support that helps novices can become redundant for advanced learners — see [Expertise reversal effect](../theories/expertise-reversal-effect.md). Relatedly, [cognitive load management](../principles/cognitive-load-management.md) suggests annotation tasks should be matched to text difficulty and learner background.

**Design implications.** Because unguided marking is unreliable, designers should pair annotation tasks with training in what to mark (e.g., modeling expert annotation), require elaborative annotations (summaries, questions, connections) rather than mere highlighting, and build in opportunities to revisit and use annotations for retrieval rather than re-reading. Structured annotation tasks fit naturally within [active learning](../principles/active-learning.md) sequences and can serve as an [activation step](activation-improves-learning.md) before discussion or problem-solving. They also align with [dual coding](../theories/dual-coding-theory.md) when annotations combine verbal notes with visual marks.

**Status.** No evidence entries have been ingested for this claim yet. Until controlled or meta-analytic evidence is added, treat this as a plausible but unrated claim: the generative-processing rationale is well grounded in theory, but the empirical support — particularly for unguided highlighting — is contested in the study-strategies literature.

## Related Claims

- [Activation improves learning](activation-improves-learning.md) — annotation activates prior knowledge during reading
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — annotation segments text into manageable units
- [Annotating](../principles/annotating.md) — the underlying design principle this claim supports
- [Von Restorff effect text marking](../theories/von-restorff-effect-text-marking.md) — distinctive marking makes annotated items more memorable
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — scaffolds that help novices can burden advanced learners, including annotation guidance
- [Cognitive load reduction improves learning](cognitive-load-reduction-improves-learning.md) — annotation must not add extraneous load on dense texts
- [Relevancy of emphasized text directs attention and influences test performance](relevancy-of-emphasis-directs-attention.md) — related
- [Highlighting shows low utility for improving learning outcomes](highlighting-low-utility.md) — reports the opposite
- [Experimenter-generated underlining is as effective as student-generated underlining for test performance](experimenter-underlining-effective-as-student-underlining.md) — related
- [Strong acquisition tasks explicating the organization produce better internalization than weak tasks asking only for a structured summary](strong-acquisition-tasks-improve-internalization.md) — related