---
type: element
id: worked-examples
title: Worked Examples
description: Worked examples are the element in which learners study complete or partial solutions before attempting similar problems independently.
status: review
generated:
  by: codex/unspecified
  at: 2026-04-08
---

# Worked Examples

> **Element** · [All elements](index.md)
> **Evidence** · 14 claims (10 for, 4 mixed) · 19 studies (11 causal, 4 quant-synthesis, 2 review, 1 associational, 1 theoretical), `q2`–`q4` · 3 of 19 report an effect size · 5 claims rest on one study

## Description
Worked examples are the element in which learners study complete or partial solutions before attempting similar problems independently.

## Design Implications

### Context
#### Requirements
- **A solved model of performance**
- **Prompts that surface why steps were taken**
#### Constraints
- **Benefits fade as expertise grows**

### Target Learning Goals
- Reduce novice search burden and support schema formation.

### Affordances
- [Worked Examples](../principles/worked-examples.md)
- [Scaffolding](../principles/scaffolding.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Sequencing worked examples with practice problems improves learning for novices](../claims/worked-example-problem-sequences.md) [+W]
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+W]
- [Example-problem sequences reduce cognitive load and improve learning outcomes.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+W]
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-examples-example-problem-sequences.md) [+W]
- [Worked examples improve mathematics performance, especially for novices.](../claims/worked-examples-improve-math-performance.md) [+M]
- [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+M]
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S]
- [Expertise Reversal Guidance Hurts Experts](../claims/expertise-reversal-guidance-hurts-experts.md) [~S]
- [Productive Failure Improves Conceptual Learning](../claims/productive-failure-improves-conceptual-learning.md) [~S]
- [Lower-prior-knowledge learners scored higher on an algebra posttest after full-worked than completion-worked examples, while higher-prior-knowledge learners' non-significant advantage ran the other way](../claims/lower-prior-knowledge-learners-score-higher-with-full-than-completion-worked-examples.md) [~M]
- [Self Explanation Prompts Improve Learning From Worked Examples](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- [Erroneous examples improve conceptual understanding by forcing comparison with correct models.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+S]
- [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [+S]

## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### Should novices start with a worked example or with a problem?
- **Default:** start with a worked example. In one randomised experiment with 96 secondary-school novices in circuit troubleshooting, sequences that began with an example (examples only, or example–problem pairs) beat sequences that began with a problem on the post-test and cost less mental effort — [Sequencing worked examples with practice problems improves learning for novices](../claims/worked-example-problem-sequences.md) [+M]; in algebra, novices who studied examples instead of solving conventional problems later solved same-structure problems faster and with fewer errors — [Worked examples improve mathematics performance, especially for novices.](../claims/worked-examples-improve-math-performance.md) [+S], [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- **Changes when:** the goal is conceptual understanding or transfer, the learners are past the early primary grades, and the problem phase follows productive-failure design (multiple solutions, group work, instruction that builds on students' attempts) → problem solving first, then instruction. Across 53 studies this beat instruction first on conceptual knowledge and transfer (g = 0.36), with no difference on procedural knowledge (g = −0.03), and reversed for second to fifth graders and domain-general skills — [Productive Failure Improves Conceptual Learning](../claims/productive-failure-improves-conceptual-learning.md) [~S]
- **Tested with:** secondary and university students in algebra and electrical-circuit troubleshooting (worked examples); a meta-analysis of mostly mathematics and science comparisons (productive failure).
- **Not settled:** no study in the wiki sets worked examples directly against a productive-failure sequence, and the productive-failure comparisons are against instruction first, not against studying examples. Whether a problem followed by an example helps more than problems alone is also unclear: the two wiki pages on van Gog et al. (2011) disagree, one saying all example-based conditions beat problems only, the other that problem–example pairs did not differ from problems only.

### Are examples enough on their own, or must they be paired with practice?
- **Default:** follow examples with structurally similar problems and move learners toward solving on their own — [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+M]
- **Changes when:** the target is problems of a different structure → examples alone did not carry over. Sweller and Cooper's gains held only for problems identical in structure to the examples, and the authors argue general rules take practice across a wider range of problems — [Worked examples improve mathematics performance, especially for novices.](../claims/worked-examples-improve-math-performance.md) [~S]
- **Tested with:** secondary-school novices in circuit troubleshooting; school and university students in algebra.
- **Not settled:** the claim page's title says pairing beats examples alone, but its evidence compares example-based sequences with problems only, and the fuller page on the same experiment found examples only and example–problem pairs did not differ on the post-test. The number of examples per problem, and how many pairs a topic needs, have no wiki evidence.

### When and how should the examples be withdrawn?
- **Default:** fade steps out of the example: full worked examples, then completion problems, then independent problems. In Renkl et al. (2002, n = 71), removing worked steps gradually gave better learning and less mental effort than full problem solving or a block of examples followed by a block of problems — [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]
- **Changes when:** learners already hold the schema → reduce or drop full examples, since guidance that helps novices loses its advantage and in several paradigms reverses once learners have domain schemas — [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~S], [Expertise Reversal Guidance Hurts Experts](../claims/expertise-reversal-guidance-hurts-experts.md) [~S]
- **Tested with:** university and secondary students in well-structured domains; electrical trainees reading circuit diagrams (Kalyuga et al. 1998).
- **Not settled:** how fast to fade, and how to tell that a learner has passed the point where examples stop helping. The expertise-reversal pages rest on reviews and abstracts and report no effect sizes, and they note that expertise is specific to each topic, so a learner may need examples again in the next one.

### Full worked examples or completion problems?
- **Default:** for learners with little prior knowledge, give full worked examples. In one factorial study of college students solving simultaneous equations, lower-prior-knowledge learners scored higher after full-worked than completion-worked examples (t(1,26) = 1.98, p = .05) — [Lower-prior-knowledge learners scored higher on an algebra posttest after full-worked than completion-worked examples, while higher-prior-knowledge learners' non-significant advantage ran the other way](../claims/lower-prior-knowledge-learners-score-higher-with-full-than-completion-worked-examples.md) [~M]
- **Changes when:** learners have more prior knowledge → completion examples had a higher mean in the same study (11.19 against 10.00), but the difference was not significant (p = .22), so this is a direction, not a finding — same claim [~M]
- **Tested with:** one study, college students, algebra.
- **Not settled:** one small study with a borderline result; no effect size is printed and equivalence was not tested.

### Should learners be prompted to explain the steps to themselves?
- **Default:** yes. Across 69 effect sizes from 64 reports, self-explanation prompts improved learning by g = .55, across task types, subjects and levels of education — [Self Explanation Prompts Improve Learning From Worked Examples](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- **Changes when:** the outcome is classroom or delayed performance in mathematics → the benefit is much less established than for immediate, lab-style tests, and it was stronger when learners were scaffolded toward high-quality explanations — same claim [~S]
- **Tested with:** meta-analyses spanning school and university levels; mathematics for the Rittle-Johnson et al. synthesis; eighth graders reading a science text (Chi et al. 1994).
- **Not settled:** the evidence is for self-explanation in general, not with worked examples specifically, as the claim page says; which prompt format works best is not settled there.

### Should the examples include errors, or be compared side by side?
- **Default:** have learners compare correct and incorrect worked solutions and explain the errors. Middle-schoolers who compared correct and erroneous decimal examples did better than those who studied correct examples only, especially on transfer — [Erroneous examples improve conceptual understanding by forcing comparison with correct models.](../claims/erroneous-examples-build-conceptual-knowledge.md) [+S]; more broadly, comparing two or more cases side by side beat studying them one at a time (d = .50 across 57 experiments), with larger gains when learners look for similarities and the principle comes after the comparison — [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [+S]
- **Changes when:** the goal is conceptual knowledge from comparing solution methods → seventh graders who compared algebra methods side by side gained procedural knowledge and flexibility but no more conceptual knowledge than those who studied them one at a time — [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [~S]
- **Tested with:** middle-school decimals and algebra; undergraduates learning negotiation; a meta-analysis of laboratory and classroom experiments.
- **Not settled:** whether erroneous examples suit learners with no prior knowledge. The claim page says they work best with some prior knowledge, but cites no study for that, and neither entry reports an effect size.

## Related Elements
- [Demonstration](demonstration.md)
- [Fading](fading.md)

## Key Sources
- van Gog, T., & Rummel, N. (2010). Example-based learning. *Educational Psychology Review, 22*(2), 155-174.
