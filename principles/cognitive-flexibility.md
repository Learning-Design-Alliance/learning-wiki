---
type: principle
id: cognitive-flexibility
title: Cognitive Flexibility
description: "Revisiting the same concepts across several cases, perspectives or representations that differ in how the concept applies, with explicit prompts to compare them, is expected to help learners with some but rigid knowledge of an ill-structured domain transfer it to a new case at a short horizon; it may cost factual recall, novices may need a simpler start, and delayed effects are untested here."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: jacobson-1995
    resource: "https://doi.org/10.2190/4t1b-hbp0-3f7e-j4pn"
    title: "Jacobson, M. J., & Spiro, R. J. (1995). Hypertext learning environments, cognitive flexibility, and the transfer of complex knowledge: An empirical investigation. *Journal of Educational Computing Research, 12*(4), 301-333"
    author: "Jacobson, M. J., & Spiro, R. J"
---

# Cognitive Flexibility

> **Principle** · [All principles](index.md)
> **Evidence** · 8 claims (3 for, 5 mixed) · 14 studies (7 causal, 3 quant-synthesis, 2 review, 1 associational, 1 theoretical), `q2`–`q4` · 3 of 14 report an effect size · 4 claims rest on one study

## Conditional relationship

This principle is about a learner who already holds some knowledge of a domain in one form (one rule, one textbook case, one representation, one solution method) and must now use it in situations where it plays out differently. The starting response to look for is **rigid use**: applying the familiar rule or method to a case it does not fit, failing to recognise the concept when it appears in an unfamiliar form, or being able to state it but not adapt it. The expectation is that **revisiting the same concepts across several cases, perspectives or representations that differ in how the concept plays out, with explicit prompts to say what stays the same and what changes**, helps the learner assemble the knowledge afresh for a new situation. The outcome is `near-transfer` or `far-transfer` to a new case (an essay, a solution, a judgement), at short horizons in the evidence here. The target knowledge is a `principle`, a `concept` or a `complex-skill` whose application varies across situations; the theory's home is ill-structured domains such as medicine, law, policy and history.

The wiki tests only part of this. One small `randomized` experiment tests the bundled approach (revisiting short cases under several themes) against drill, with first- and second-year undergraduates, and finds better transfer essays by the fourth session and *worse* factual recall. The case-comparison evidence (a meta-analysis and experiments) tests comparing provided cases, not multiple perspectives or ill-structured domains as such, and its benefit was smaller at delay. **No claim here tests the expectation that the advantage grows at `delayed-retention`, how many cases are needed, or whether the approach suits `novice` learners**; the theory itself says novices may be overwhelmed, and one experiment on part-task practice supports simplifying first for them. Whether the learner's knowledge is in fact rigid, and whether the cases really differ in how the concept applies, must be established locally.

The converted sibling [Analogical Reasoning](analogical-reasoning.md) owns a narrower relationship: mapping the relations of one provided or familiar case onto a new one, with case comparison as its best-evidenced configuration. This page owns the more general one, holding the same knowledge in several forms so it can be reorganised, and places analogical case comparison inside it as one way to build that flexibility; multiple representations and multiple conceptual perspectives are the others. The [Cognitive Flexibility Theory](../theories/cognitive-flexibility-theory.md) page describes the theory and its criss-crossing design; it is not rewritten here. The [case-based learning pattern](../patterns/case-based-learning.md) holds a converted policy for teaching through cases.

"Cognitive flexibility" also names an executive function (switching between rules or sets), and the wiki's claims about training it in kindergarten and first grade (for example `cognitive-flexibility-training-increases-cognitive-flexibility-growth` and `embedded-cognitive-flexibility-no-overall-advantage-winter-kindergarten`) are about that construct. They do not test this page's relationship and are not used here.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal with its evidence status stated beside it. Most of it is untested as written.

1. **Name the throughline first.** Write down the one to three concepts that will recur across every case, so variation does not become fragmentation. Untested; from the earlier page ("learners still need a coherent throughline").
2. **For learners new to the domain, start with one clear case or one representation and the parts of the task separately; add variability once they can complete the simple version unaided.** Evidence: part-task practice helped novices on a high-interactivity task before the whole task (see below). That study did not vary cases, so it supports simplifying first, not a particular point at which to add variety. If learners cannot complete the simple version unaided, do not add cases yet: give a worked example or a part task instead.
3. **Choose several short cases in which the same concept plays out differently**, not cases that only look different. Revisit each case under more than one theme or question rather than covering it once. Evidence: the criss-crossing experiment used short cases reread under different combinations of themes, and its transfer advantage appeared by the fourth session (see below). No number of cases or sessions is established; the earlier page and the theory page give none either.
4. **Prompt the comparison explicitly**: "What stays the same across these cases? What changes, and why does the rule apply differently here?" Put the cases side by side, and state the principle after learners have compared them. Evidence: in the case-comparison meta-analysis, benefits were larger when learners were asked to find similarities and when the principle came after the comparison.
5. **Add a second representation (a diagram, a simulation, a formula) only with instruction in how the representations connect**, and check that learners can read each one. Evidence: multiple representations helped in one undergraduate physics field study, and a review finds the benefit depends on learners' skill at connecting representations.
6. **Have learners explain why the familiar rule cannot be applied mechanically to a new case.** Untested for this relationship; from the earlier page, which cited the self-explanation claim (under Further evidence below).
7. **Keep fact learning separate, and judge the design on a new case.** Practise the facts the objective needs by recall; assess flexibility with an unfamiliar case scored apart from recall, and repeat it after a delay if the objective needs durable use. Evidence: the criss-crossing group transferred better and recalled facts worse than the drill group.

## Fitting the design to a situation

The three facts that most change the decision:

- **How rigid or how thin the learner's current knowledge is.** A learner who has nothing to be rigid about needs a first, simple version (step 2); a learner applying a rule mechanically needs varied cases (step 3). If unstated, ask: can they complete a standard case of this kind unaided, and what do they do with a case where the usual rule does not fit?
- **Whether the domain really varies across situations.** In a well-structured procedure with one right method, varied cases add load for little gain (the theory and the earlier page both say so; no claim here tests it). If unstated, ask: do experts in this field disagree about cases, or apply the same rule differently in different settings?
- **What the assessment rewards.** The one direct test found a trade-off: better transfer, worse factual recall. If the stakes sit on recall, the design must protect recall separately. If unstated, ask: what will the learner be judged on, a new case, or what they remember?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Expertise `novice` in the domain, high element interactivity | Start with one case and part tasks; add the second and third case only after the simple version is completed unaided; prompt the named dimension of comparison. | [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]; population not reported on the claim page |
| Expertise `intermediate` or `advanced`, an ill-structured domain (clinical reasoning, law, policy) | Use criss-crossing: revisit each concept in several short cases under different themes across sessions; drop the step-by-step part tasks. | [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]; tested with first- and second-year undergraduates, untested with professionals |
| Age `child` (under 12) | Use two cases at a time, side by side, with the one dimension that differs named by the teacher; no free navigation among cases. | untested proposal; no claim here tests this relationship with children |
| Age `adolescent`, goal a mathematics `procedure` | Have learners compare alternative solution methods side by side; expect gains in choosing methods, and add a separate item asking why each method works. | [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [~M]; tested with seventh-graders, procedural flexibility rose, conceptual knowledge did not |
| Goal `verbal-association` (facts, terms), or recall-weighted high-stakes assessment | Do not make criss-crossing the main activity; give facts their own retrieval practice, and use varied cases only for the transfer part of the objective. | [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M]: the drill group recalled more facts |
| Goal a STEM `concept` taught through representations | Add a second representation (sketch, simulation) beside the formula, with tasks that connect them; monitor reported load and representational skill. | [Multiple representations improve learning](../claims/multiple-representations-improve-learning.md) [~M]; one undergraduate physics field study and a review; benefit depends on representational competence |
| Setting `online-self-paced` or hypertext | Give a guided route through the cases (a theme per pass) rather than free browsing, and build the comparison prompts into the pages. | [Students in the flexible hypertext-based course design scored higher on achievement tests (76%) than students in the direct online course design (59%)](../claims/cft-hypertext-design-higher-achievement-scores.md) [~W]: groups studied different software, so it does not isolate the design; navigation burden is untested, from the theory page |
| Duration `single-session` | Use two or three contrasting cases with a similarities prompt and the principle stated after; test on a new case the same day. If the course allows, revisit the cases later under a new theme. | [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [+M]: comparison helped in single experiments, more at immediate tests |
| Duration `days-weeks` or `term-plus` | Return to the same concepts in each session through new cases and new themes; schedule a delayed transfer case. | [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]: the advantage appeared by the fourth session; delayed benefit untested |
| Constraint: cases in a second language, or heavy reading load | Keep cases short, give them in accessible language, and present the comparison as a table learners fill in, so reading demand does not swamp comparison. | untested proposal |

Eight of the ten rows rest on a claim, each only as far as its tested population and setting; the rows for children and for reading load are untested proposals.

## Observation, state and explanation

What can be observed is a response to a particular case under stated conditions: which rule or method the learner applied, whether they noticed that the case differed, what they said changed and what stayed the same, whether a hint was needed. "Rigid knowledge", "flexible understanding" and "oversimplified schema" are inferred states. Record which cases and representations the learner had already met, every prompt and hint, and whether the test case shares surface features with a taught one.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Applies the familiar rule to a case it does not fit | Knowledge held as one rigid schema; did not notice the case differs; noticed but has no alternative to apply | Ask what is different about this case before asking for a solution; give a matched case where the difference is made salient and see whether the choice changes. |
| Solves taught cases well, fails a new case in the same domain | Learned the cases, not the concept; new case needs knowledge not taught; test case harder in ways unrelated to flexibility | Give a new case with the taught surface and a different principle, and one with a new surface and the taught principle; score which one fails. |
| Lists differences between cases but cannot say what stays the same | Surface comparison only; too little knowledge of the concept to see it; prompt asked for differences | Ask for the shared idea explicitly, then for a prediction in a third case; compare with a learner given the principle after the comparison. |
| Recalls facts poorly after several case sessions, writes good case analyses | Time moved from facts to cases; facts not needed for the analyses; analysis uses general reasoning rather than domain knowledge | Score fact items and case items separately; check whether the case analyses use the facts the objective requires. |
| Overwhelmed by several cases or representations: stops, picks one at random | Working memory exceeded; cannot read one of the representations; unclear what the comparison is for | Reduce to two cases or one representation and repeat; ask the learner to read each representation alone; give the comparison question before the cases. |

These are proposals, untested with learners. A probe can shift confidence between explanations; it does not identify a cause, and probing itself is practice (a "what is different here" prompt is also a comparison prompt).

## Evidence and qualifications

The Alfieri et al. case-comparison meta-analysis stands under two of these titles, so **count studies, not claims**: nine distinct studies stand behind the six core claims.

- [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M]: the one direct test of the bundled approach. A small `randomized` experiment (34 paid university volunteers, first- and second-year, 17 per group after pooling two drill controls) on the social impact of technology. Rereading short cases under different combinations of themes ("thematic criss-crossing hypertext") produced better problem-solving transfer essays by the fourth session than computer drill (9.47 vs 7.24 on a 15-point scale), holding after adjustment for verbal ability and extra study time; the drill group scored higher on factual recall. No standardised effect size is reported. The treatment bundled several features, so it does not show which one mattered. The claim's second entry is the case-comparison meta-analysis below, which does not isolate ill-structured domains or multiple perspectives and found a smaller benefit at delay, against the theory's prediction. Not settled: the text available could not confirm the entries (abstract).
- [Comparing Contrasting Cases Improves Learning](../claims/comparing-contrasting-cases-improves-learning.md) [~M]: a meta-analysis (`synthesis-experimental`) of 57 experiments (336 tests): case comparison beat single, sequential or non-analogous case study, traditional instruction and controls, d = .50, 95% CI [.44, .56], with larger benefits when learners looked for similarities, when the principle came after the comparison, with perceptual content, and at immediate tests. Also a `randomized` experiment with 128 undergraduates learning negotiation (48% vs 19% used the principle in a new negotiation after comparing two cases on one page versus studying them separately), and a `randomized` experiment with 70 seventh-graders in which comparing algebra solution methods side by side raised procedural knowledge and **procedural flexibility** but not conceptual knowledge. It supports comparison as a mechanism for flexibility and qualifies it: the flexibility gained may be in choosing methods, not in understanding them. Partly checked: 2 of 3 entries pass, the rest could not be confirmed (abstract).
- [Encoding variability across varied example contexts produces decontextualization supporting transfer (review reports DiVesta and Peverly)](../claims/encoding-variability-decontextualization-transfer.md) [+W]: a `review` reporting, second-hand, an experiment that varied the contexts in which a concept was learned and measured recognition of new instances in another context (`far-transfer`). The claim page gives no sample, effect size or comparator detail. It supports the idea that varied contexts help knowledge detach from its first context, and no more. Not yet checked against its sources.
- [Multiple representations improve learning](../claims/multiple-representations-improve-learning.md) [~M]: a `controlled-nonrandom` field study (81 first-year university physics students) in which sketching and simulation tasks beside the formula raised a vector-field test score (d = 0.40) and raised reported cognitive load; and a narrative `review` concluding that a second type of visual representation helps only when learners can connect representations. It bears on the "more than one representation" half of the principle and limits it: more forms are not automatically better. Not settled: the text available could not confirm the entries (abstract).
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]: an experiment in which novices on a task with high element interactivity did better when first given isolated parts before the integrated task. The claim page reports no sample size or effect size. It limits the relationship for novices: simplify first, then add complexity and variety. It does not test varied cases. Not yet checked against its sources.
- [Students in the flexible hypertext-based course design scored higher on achievement tests (76%) than students in the direct online course design (59%)](../claims/cft-hypertext-design-higher-achievement-scores.md) [~W]: a `controlled-nonrandom` comparison of two intact groups of 73 students in a Moodle course. The flexible-hypertext group studied Adobe Flash and the direct-design group Adobe Illustrator, so content and design are confounded; no significance test or effect size is printed. It is listed because it is the wiki's other test of a cognitive-flexibility design, and it cannot separate the design from the subject taught. Not yet checked against its sources.

Taken together: revisiting concepts through varied, compared cases has `randomized` and `synthesis-experimental` support for transfer at short horizons, mostly with undergraduates; the one direct test of the bundled approach is small and traded recall for transfer. The flexibility gained may be procedural rather than conceptual, multiple representations help only when learners can connect them, and novices may need a simpler start. Delayed transfer, professional learners, children, and the number of cases are not established. Comparators (drill, separate cases, traditional tasks, a different course) and outcomes (essays, negotiations, algebra items, a physics test) differ, so do not rank these results by effect label.

How far each may be carried: the criss-crossing experiment supports steps 3 and 7 of the default design for undergraduates in one ill-structured topic. The comparison evidence supports step 4 for provided cases. The part-task study supports step 2's "simplify first" for novices, not when to add variety. The hypertext study supports nothing on its own.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [A training-design argument, not tested by any study recorded here, holds that practising whole complex tasks improves transfer of complex skills](../claims/whole-task-performance-improves-transfer.md) [~M] — checked by the judge: all 1 entries pass (abstract)
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — not settled: the text available could not confirm the entries (abstract)

## Objective and learner-valued goal

The designer's objective names the concept that should travel, the kinds of new case it should be used on (near or far, with or without a hint), what counts as adapting it well, and the horizon. Elicit separately what the learner wants from it. Agreement, divergence and uncertainty are observations.

For example, a second-year law student may want to pass a doctrinal exam that rewards stating rules precisely, while the designer's objective is to apply a negligence standard to fact patterns that differ from the leading cases. Criss-crossing cases serves the designer's aim and, on the one direct test, may cost some recall the student values. Record both aims, give the rule statements their own practice, and show the student a new fact pattern where the stated rule alone gives the wrong answer, so the value of the case work is visible rather than asserted.

## What would revise this model?

The model should weaken if well-controlled comparisons with comparable learners find no transfer advantage for revisiting concepts across varied, compared cases over studying the same material once in one form, or find the advantage gone at the delay the objective needs. If the advantage is consistently procedural (choosing methods) and never conceptual, keep that distinction rather than calling both flexibility. If novices given varied cases from the start do as well as those given a simple start, step 2 should be dropped; if they do worse, it becomes a requirement. If the recall cost seen in the one direct test persists and matters to the objective, the design needs separate fact practice by default. Do not protect the model by calling every transfer failure a sign that the cases were not varied enough.

Noticing that a case differs, saying what changes, choosing an appropriate method, applying a concept in a new case, doing so in another domain, and remembering it later are separate claims. The present evidence does not establish how many cases or perspectives to use, how different they should be, or whether multiple perspectives add anything beyond case comparison.

## Related Principles
- [Perspective-Taking](perspective-taking.md) — multiple viewpoints often drive the need for flexible interpretation
- [Constructivist Learning](constructivism.md) — cognitive flexibility assumes knowledge is actively reorganized, not merely stored
- [Cognitive Disequilibrium](cognitive-disequilibrium.md) — contradiction and instability can sometimes trigger the need for more flexible models

## Examples

### Illustrative

**[Cognitive Flexibility Theory](../theories/cognitive-flexibility-theory.md)** — Learners revisit concepts across multiple cases, perspectives, and representations instead of mastering one linear explanation.

**Cross-case comparison in medicine or law** — Students compare superficially similar cases with different underlying structures, then explain why the same rule cannot be applied mechanically.

**Multiple-solution-method analysis** — Learners study several valid approaches to the same problem and articulate what each method reveals or obscures.

## Key Sources
- Spiro, R. J., Feltovich, P. J., Jacobson, M. J., & Coulson, R. L. (1991). Cognitive flexibility, constructivism, and hypertext. *Educational Technology, 31*(5), 24-33.
- Jacobson, M. J., & Spiro, R. J. (1995). Hypertext learning environments, cognitive flexibility, and the transfer of complex knowledge: An empirical investigation. *Journal of Educational Computing Research, 12*(4), 301-333. [https://doi.org/10.2190/4t1b-hbp0-3f7e-j4pn](https://doi.org/10.2190/4t1b-hbp0-3f7e-j4pn)

<!-- deprecated 2026-10-02: superseded by the conditional model above; the previous body is kept verbatim.

## Description
Cognitive flexibility is the principle of helping learners represent, interpret, and apply knowledge in more than one way rather than locking it into a single rigid schema. It is useful when domains are complex, case-based, or open to multiple valid perspectives.

## Implications

Cognitive flexibility matters most in ill-structured domains where oversimplified rules break down and learners must adapt understanding across contexts. The principle does not reject structure; it resists premature rigidity. Learners need repeated exposure to varied cases, perspectives, and representations so they can reorganize knowledge instead of merely retrieving one memorized version, which is one reason contextualized whole-task experience can support flexible transfer better than isolated drills [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~S]. The challenge is pacing. Too much variability too early can overwhelm novices [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M], while too little variability can leave learners with brittle knowledge that fails outside the original example. Explanation across cases and perspectives is one of the strongest ways to make flexibility visible and learnable [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S].

### Context
#### Requirements
- **Multiple representations, cases, or viewpoints** — flexibility develops when learners see a concept behaving differently across contexts
- **Tasks that require adapting understanding across contexts** — learners need to compare, reframe, and transfer rather than reproduce one routine response
#### Constraints
- **Too much variability can overwhelm novices without support**
- **Learners still need a coherent throughline** — flexibility is not fragmentation or randomness
- **Complex domains are a better fit than tightly procedural ones**

### Target Learners
- Learners in medicine, law, design, policy, writing, and other ill-structured or case-based domains
- Learners who must interpret ambiguity rather than apply a single fixed rule
- Learners moving from foundational understanding toward adaptive transfer

### Target Learning Objectives
- Improve transfer, adaptive reasoning, and the ability to reframe knowledge
- Help learners avoid overgeneralizing from one case or representation
- Build the capacity to reorganize knowledge under shifting conditions

### Theory
#### Supporting
- [Cognitive Flexibility Theory](../theories/cognitive-flexibility-theory.md) — the most direct pattern-level expression of this principle
- [Perspective-Taking](perspective-taking.md) — shifting viewpoint is one of the mechanisms by which flexibility develops
- [Constructivism](../theories/constructivism.md) — knowledge is reorganized through active interpretation across contexts

#### Contradicting / Qualifying
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — variability and nonlinearity need to be calibrated to learner readiness

### Claims
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~S] — flexible transfer is stronger when learners encounter knowledge in integrated, contextualized use
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — explanation across cases and perspectives can deepen flexible understanding
- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M] — novices may still need staged simplification before they can benefit from high variability
-->
