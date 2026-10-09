---
type: pattern
id: concept-attainment
title: Concept Attainment
description: "A reusable policy in which learners infer a concept's defining attributes by comparing labelled examples and non-examples, then classify new instances; expected to improve classification of new instances where the concept has identifiable attributes, the examples are chosen to contrast on them, guidance and a stated rule follow the induction, and learners can already interpret the instances."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
author: "Bruner, Goodnow, & Austin (1956)"
grain_size: lesson, unit
---

# Concept Attainment

> **Pattern** · [All patterns](index.md)
> **Evidence** · 10 claims (7 for, 3 mixed) · 18 studies (8 quant-synthesis, 7 causal, 2 review, 1 theoretical), `q1`–`q4` · 7 of 18 report an effect size · 3 claims rest on one study

## Description and scope

A reusable policy for teaching a `concept` by induction from labelled data: **labelled "yes" examples and "no" non-examples → learners state and test candidate attributes → near-miss non-examples that differ on one attribute → learners state the rule, and the conventional term and definition are given → learners classify new, unlabelled instances → the concept is used in a richer task**. The intended change is in classifying new instances, including borderline ones (`near-transfer`), and in stating the attributes that decide membership (`conceptual-understanding`).

It instantiates the [Analogical Reasoning principle](../principles/analogical-reasoning.md): comparing examples to find what they share, and contrasting them with non-examples to find what they lack, is a form of structural comparison, and that principle's evidence (comparison of provided cases, mostly with `novice` learners on immediate tests) is the nearest this pattern has. It also sits inside the [Inquiry-based Learning principle](../principles/inquiry-based-learning.md) as a small, tightly structured inquiry: learners investigate a question ("what makes these the yes items?") from data the designer supplies. That principle's boundary applies here directly: unsupported discovery of essential content learns less than explicit instruction, and guided forms do better. This page owns the narrower configuration, induction of one category from contrasted labelled instances, and does not restate either principle's model.

**No claim in this wiki tests concept attainment as such**, against definition-first teaching or anything else. The claims that bear on it are of four kinds: comparing provided cases against studying them separately; interleaving labelled exemplars of several categories against blocking them, measured on classifying new exemplars; guided against unguided discovery; and two 1966 conceptual arguments about when induction suits what is being taught. Each is carried to this pattern by extrapolation, and the page says how far. The response-dependent policy below is an **untested design proposal**; the sequence is the earlier page's, kept as the default, with each step's evidence status stated.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Before any data are shown, ask each learner to sort a few instances (some clear, one or two borderline) and say why. Record what attribute they use, whether they can perceive or read the instances at all, and their prior knowledge of the domain the instances come from. Preserve unknowns rather than labelling learners `novice`. |
| The concept | Whether it has identifiable defining attributes and a defensible boundary (well defined, like "prime number"), is a family-resemblance or prototype category, or is contested ("democracy"). Whether the instances are visual or perceptual, symbolic (equations, graphs), or verbal (sentences, word lists). How confusable it is with neighbouring concepts. |
| Context and activities | Setting (`classroom`, `online-self-paced`, `online-instructor-led`, `workplace-clinical`), `single-session` or `days-weeks`, how many concepts in the unit, group size, whether a teacher is present to answer "yes/no" and run the discussion, how labels and hypotheses are displayed. |
| Learner-valued goal | Ask what the learner wants to be able to do with the concept (recognise it at work, use the word correctly, pass a test, understand why it matters). Record disagreement with the designer objective. |
| Designer objective | Which of these is the target: classifying new instances, stating the defining attributes, using the conventional term, discriminating it from a named neighbouring concept, or the inductive process itself. Name the one the assessment will weigh. |
| Outcome | A classification test on new, unlabelled instances that includes near misses and instances from neighbouring concepts, scored apart from a written definition; immediate or `delayed`; and whether the concept must be recognised inside a richer task (`near-transfer`, `far-transfer`). |

A request to "use concept attainment for this unit" does not specify these. Ask what concept, what instances and what test before choosing the data set, its order or the number of concepts per lesson.

## Sequence and conditional policy

The default sequence is the earlier page's. Steps 1, 2 and 5 are untested here; steps 3, 4 and 6 have a neighbouring claim, carried by extrapolation.

1. **Check the concept and build the data set.** Use a concept with identifiable attributes; build clear "yes" examples, matched "no" non-examples, and near misses that differ from a "yes" on one attribute only; order them from unambiguous to borderline. If the concept is contested, either choose another approach or make exploring the boundary the explicit goal. Evidence status: untested; from the earlier page. [The task-type argument](../claims/task-type-moderates-induction-error-usefulness.md) [~W] (a 1966 conceptual analysis) holds that induction may suit concepts but not simple associations or response precision, and is "less than definitive" for rules and principles.
2. **Elicit, then show labelled data.** Collect each learner's starting sort (inputs, above). Present the first labelled items with a framing question ("what do all the 'yes' items share?") and, for learners new to the domain, an attribute checklist with two or three candidate attributes in play. Evidence status: untested; from the earlier page.
3. **Learners state and test hypotheses against each new item**; the teacher or the system answers only "yes" or "no"; competing hypotheses are written where all can see them. Prompt learners to say what the yes items share and how each no item differs. Evidence status: [comparing cases](../claims/comparing-contrasting-cases-improves-learning.md) [+M] found larger gains when learners were asked to find similarities. Those studies compared analogous cases, not examples with non-examples.
4. **Contrast near misses**, one attribute at a time, after the core rule is stable. Where the concept has confusable neighbours, mix their labelled instances rather than presenting each concept in a block. Evidence status: [interleaving labelled category exemplars](../claims/interleaving-improves-inductive-learning.md) [+M] helped classification of new exemplars for visual and mathematical material and reversed for word-based categories; one meta-analysis, read from its abstract.
5. **Name and define.** Learners state the rule in their own words; the teacher supplies the conventional term and canonical definition, and corrects the rule where the class has converged on a wrong one. Evidence status: untested; from the earlier page. The case-comparison meta-analysis found larger gains when the principle came after the comparison, which bears on the order but not on this pattern.
6. **Classify new, unlabelled instances, including borderline ones, with feedback**, then use the concept in a case or problem. If many learners still misclassify, explain the attributes directly rather than run another round of induction. Evidence status: [guided against unguided discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]: discovery with feedback, worked examples or scaffolding outperformed other instruction, while unassisted discovery learned less than explicit instruction.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learners fixate on a salient attribute that does not decide membership ("lives on land") | Show one "yes" item that lacks the salient attribute, or a "no" item that has it; ask whether their rule still holds. | If they revise, continue with near misses. If they keep the rule after the counter-item, they may not perceive the deciding attribute or may not read the item as intended: point to the attribute, or state it. Neither branch is tested. |
| Correct rule stated, but new borderline instances misclassified | Present two near misses that differ on one attribute; ask which attribute decides and why. | If they name the wrong attribute, add near-miss contrasts on that attribute. If they name the right one but misread the instance, the problem may be perceiving or reading the instances; give practice on reading them. One correct sort does not settle it. |
| Correct classification, no account of why | Ask for the attributes in their own words and one invented non-example. | If they cannot, the classification may rest on surface resemblance to the items shown; ask for self-made examples and non-examples before moving on. The comparison evidence suggests gains can be procedural without being conceptual. |
| No hypothesis offered after several items, or random guessing | Ask privately what they are looking at; check that they can identify the parts of an instance (the hair, the term, the axis). | If the instances are not readable, teach what the instances are first or switch to definition-first with examples. If they can read them but do not hypothesise, offer the attribute checklist. Proposed, untested. |
| A few learners announce the rule; others copy it | Collect written hypotheses before discussion; compare each learner's later classification of new items. | If the copiers misclassify, use private hypothesis writing and individual classification; do not read class agreement as each learner's concept. |

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether learners can already read the instances and the domain they come from.** Induction needs learners who can see the candidate attributes; unsupported discovery learned less than explicit instruction. If unstated, ask: given one instance, can they name its parts and say which features might matter?
- **What kind of material the instances are.** Interleaving labelled exemplars of confusable categories helped for paintings, photographs and mathematical tasks, and reversed for word-based categories. If unstated, ask: are the examples pictures, symbols or sentences, and which concept is it most often confused with?
- **Whether the target is a concept or a rule to apply.** Concepts are where induction is argued to fit; for a rule or procedure, a rule-then-examples order is the older recommendation. If unstated, ask: will learners be asked to recognise instances, or to carry out a procedure?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` in the domain (cannot yet name the parts of an instance) | Teach what the instances are first; keep two or three candidate attributes and give the checklist; use only clear exemplars until the rule is stable; give feedback on each classification and state the rule soon after the induction rather than waiting for the class to find it. | [Guided against unguided discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]; the meta-analysis does not break results down by prior knowledge |
| Learners are `advanced` or already use the concept | Skip the induction; give the definition and go straight to near misses and borderline cases, or ask them to generate the contrasting set. | Untested; from the earlier page |
| Learners are `child` (under 12) and the target is a procedure (e.g. a fair test) | Prefer direct instruction of the procedure with examples. Keep concept attainment for categories with visible attributes (animals, shapes). | [Guided against unguided discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]: 112 third- and fourth-graders learning the control-of-variables procedure; not a concept-attainment lesson |
| The concept's instances are visual or perceptual (artists' styles, rock types, skin lesions) with confusable neighbours, or verbal (word categories, sentence types such as metaphor) | Visual: after a short block of clear exemplars, mix labelled instances of the neighbouring concepts, and warn learners that practice will feel harder. Verbal: present each concept's examples together (blocked) before any mixing, keep near misses to one attribute and the labels visible. Test both on new instances. | [Interleaving labelled category exemplars](../claims/interleaving-improves-inductive-learning.md) [~M]: benefit for paintings, photographs and mathematical tasks, reversed for word-based categories; learners' ages and settings not reported on the claim page |
| The target is a rule or procedure, not a category | State the rule, give examples, then incomplete examples to complete; use contrasting cases to compare methods. | [Rule-example sequence](../claims/rule-example-sequence-efficient-rule-introduction.md) [~W] (a 1966 report of early programmed-instruction work, not a test); [the task-type argument](../claims/task-type-moderates-induction-error-usefulness.md) [~W] |
| The outcome is conceptual explanation, not only classification | Score explanation of the attributes separately from classification, and add a self-generated non-example task. | [Comparing cases](../claims/comparing-contrasting-cases-improves-learning.md) [~M]: with seventh-graders, comparing methods raised procedural knowledge and flexibility, not conceptual knowledge |
| `online-self-paced`, no teacher | The system gives the yes/no label after the learner commits a written hypothesis; show the hypothesis history beside the items; end with a classification set with feedback and a stated definition. | Untested proposal |
| `single-session` and many concepts in the unit | Use concept attainment for the one or two concepts learners most often confuse; teach the rest definition-first with examples and non-examples. | Untested; from the earlier page |
| High stakes, or assessment on new instances weeks later | Test on new, unlabelled instances including near misses and neighbouring concepts, at the delay that matters; do not use the practice items. | Untested proposal (the case-comparison benefit was smaller on delayed tests, which is a reason to test late, not evidence for this pattern) |
| Language of instruction is not the learners' first language, or learners have reading or access needs | Use visual or concrete instances alongside verbal ones, keep labels visible, and allow written or pointing responses so working memory is not spent on the attribute list. | Untested; from the earlier page |

Five rows rest on a claim (novice learners, children and procedures, visual against verbal material, rule against concept, and a conceptual outcome), and each is carried beyond the population or design its claim page reports, as its Basis cell says; the other five (advanced learners, online without a teacher, a single session with many concepts, high stakes, and language or access needs) are untested proposals or the earlier page's guidance.

## Choosing configurations from evidence

- **Comparison of cases.** [Comparing cases side by side improves learning and transfer by a moderate average amount, though in one algebra study it raised procedural knowledge and flexibility but not conceptual knowledge](../claims/comparing-contrasting-cases-improves-learning.md) [+M]: a meta-analysis of 57 experiments (336 tests) found case-comparison activities produced greater learning than single-case or sequential study, non-analogous cases, traditional instruction and controls (d = .50, 95% CI [.44, .56]), with larger gains when learners looked for similarities, when the principle came after the comparison, for perceptual content, and on immediate tests; the pooled estimate mixes comparison conditions. In a `randomized` experiment, 128 undergraduates who compared two negotiation cases on one page used the principle in a later negotiation more often than those who studied the same cases separately (48% vs 19%). In another, 70 seventh-graders comparing algebra solution methods side by side gained more procedural knowledge and flexibility, and no more conceptual knowledge, than those reflecting on the methods one at a time (abstract only). Partly checked: 2 of 3 entries pass. [Analogical Reasoning Improves Transfer](../claims/analogical-reasoning-improves-transfer.md) [+M] rests on the first two of these studies and adds none. None compares examples with non-examples; carry it to "prompted, side-by-side comparison of labelled items can help learners find what they share", no further.
- **Order of labelled exemplars across categories.** [Interleaving category examples improves inductive category learning for visual and mathematical materials, but not for expository texts or word categories](../claims/interleaving-improves-inductive-learning.md) [+M]: a multilevel meta-analysis of 59 studies (238 effect sizes) comparing interleaved with blocked presentation of category exemplars on classifying new exemplars, g = 0.42, 95% CI [0.34, 0.50]; largest for paintings (g = 0.67), smaller for photographs (g = 0.35) and mathematical tasks (g = 0.34), nonsignificant for expository texts, and reversed for word-based categories (g = −0.39); stronger where categories were similar to each other. Not settled: the abstract could not confirm the entry. It tests the order of positive exemplars of several categories, not non-examples of one concept or hypothesis testing, and it qualifies this page as much as it supports it: for verbal concepts the evidence favours blocking.
- **Guidance.** [Unassisted discovery produces less learning than explicit instruction, while discovery enhanced with guidance outperforms other instruction](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]: a meta-analysis of 164 studies found explicit instruction outperformed unassisted discovery (580 comparisons, d = 0.38 favouring explicit instruction), and discovery enhanced with feedback, worked examples, scaffolding or elicited explanations outperformed other instruction (360 comparisons, d = 0.30); with 112 third- and fourth-grade children, novices at the control-of-variables procedure, many more mastered it under direct instruction, and they did as well on a later transfer task as the few who discovered it; a narrative review argues the guidance advantage recedes only with enough prior knowledge. Partly checked: 1 of 3 entries passes. This is the boundary of the pattern: concept attainment with labels, a framing question, near misses, a stated definition and feedback is a guided form; the same data set left without them is not.
- **What induction suits.** [The task-type argument](../claims/task-type-moderates-induction-error-usefulness.md) [~W] and [the rule-example sequence](../claims/rule-example-sequence-efficient-rule-introduction.md) [~W] are both from one 1966 conceptual paper (coded `q1` and `q2`, `theoretical`): induction may suit concepts, not response precision or simple associations, and a rule-then-example sequence appeared efficient for introducing a new rule. They are arguments, not comparisons, and they measure nothing.

Do not rank concept attainment against definition-first teaching from these claims: none compares them, and none measures the time induction costs. Do not read class agreement on a rule, or fluent classification of the items already shown, as the concept attained. A precise abstention names the missing comparison (concept attainment against definition plus examples and non-examples, on classification of new instances at a stated horizon) and the local observation that would stand in for it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite which are not used as core evidence above. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before the 2026-10-02 rewrite. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M] — not settled: the text available could not confirm the entries (abstract); 1 judge failure(s) reviewed and dismissed
- [Activation improves learning.](../claims/activation-improves-learning.md) [+M] — partly checked: 2 of 3 entries pass, the rest could not be confirmed (abstract)
- [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Advance organizers improve learning.](../claims/advance-organizers-improve-learning.md) [+M] — partly checked: 1 of 3 entries pass, the rest could not be confirmed (abstract)

## Illustrative design instance and observation record

*Invented illustration, not a tested lesson.* Newly qualified care-home staff, adults working shifts, take a `online-self-paced` module on recognising stages of pressure injury from photographs, with no tutor available. The material is visual and the stages are easily confused, so the table changed the default: the module opens with a short check that learners can name the skin features in a photograph (it teaches them if not); shows a block of clear "yes" photographs of one stage with an attribute checklist of three features; asks the learner to type a rule before each label is revealed and keeps their rule history on screen; then mixes labelled photographs of the neighbouring stages, with near misses differing in one feature; gives the stage names and definitions; and ends with twelve new unlabelled photographs with feedback. A learner says she wants to know when to call the nurse; the designer's objective is correct staging. They agree to score staging and a "call or not" decision separately, and to repeat the new-photograph test four weeks later. The interleaving claim covers photographs of categories, not this population, setting or horizon; these are local choices to observe, not settled ones.

Record: **concept and its neighbours → instances and their order (blocked, mixed, near misses) → starting sort and stated reason → hypotheses offered, in order, and the item that changed each → labels and help given → rule stated and definition supplied → classification of new instances by item type (clear, near miss, neighbour) → candidate interpretations (attribute found, surface resemblance, cannot read the instances, copied rule) and their basis → reobservation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of concept mastery without a calibrated model.

## Elements and limits

[Non-examples](../elements/non-examples.md), [comparing cases](../elements/comparing-cases.md), [hypothesis testing](../elements/hypothesis-testing.md), [advance organizers](../elements/advance-organizers.md), [class discussion](../elements/class-discussion.md), [analogies](../elements/analogies.md), [articulation](../elements/articulation.md), [application](../elements/application.md), [feedback](../elements/feedback.md), [assessment](../elements/assessment.md) and [case studies](../elements/case-studies.md). Principles the pattern draws on: [Analogical Reasoning](../principles/analogical-reasoning.md), [Inquiry-based Learning](../principles/inquiry-based-learning.md), [Activation](../principles/activation.md), [Active Learning](../principles/active-learning.md), [Clear Structure](../principles/clear-structure.md) and [Chunking](../principles/chunking.md).

This pattern is scoped to inducing one concept with identifiable attributes from labelled, contrasted instances. Contested concepts, rules and procedures, and ill-structured categories of practice need other configurations ([direct instruction](direct-instruction.md), [case-based learning](case-based-learning.md)). The policy supports observation and design reasoning; whether concept attainment produces better classification of new instances than a definition with examples and non-examples, for which learners, at what time cost and at what horizon, remains to be tested.

## Related Patterns
- [Direct Instruction](direct-instruction.md) — the definition-first alternative; concept attainment trades efficiency for deeper attribute discrimination, and the two can be sequenced (attain, then consolidate explicitly)
- [Case-Based Learning](case-based-learning.md) — extends the same example-comparison logic to rich, ill-structured cases where the "concept" is a pattern of practice rather than a definable category
- [Anchored Instruction](anchored-instruction.md) — situates concept use in a realistic problem context after or alongside example-based induction
- [5E Learning Cycle](5e-learning-cycle.md) — shares the explain-after-explore ordering; concept attainment is a focused induction routine that can serve as the Explore/Explain pair

## Examples
- **Science — "mammal" in elementary school:** Teacher posts picture cards labeled yes (dog, whale, bat) and no (shark, penguin); students propose and discard attributes ("lives on land" fails on whale) until "warm-blooded, hair, milk" survives, then classify novel animals.
- **Mathematics — functions vs. non-functions:** Students sort tables, graphs, and mapping diagrams marked yes/no, hypothesizing the vertical-line test themselves before it is named; near-miss non-examples (a parabola tipped sideways) force the one-output rule.
- **Language arts — metaphor:** Students examine labeled sentences, isolating the attribute "comparison without 'like' or 'as'" against simile non-examples, then identify metaphors in an unannotated poem.
- **[Khan Academy](https://www.khanacademy.org) math practice:** Example/non-example sorting tasks in early algebra units let learners induce what makes an expression "like terms" before formal rules are stated.

## Key Sources
- Bruner, J. S., Goodnow, J. J., & Austin, G. A. (1956). *A study of thinking*. Wiley.
- Tennyson, R. D., & Cocchiarella, M. J. (1986). An empirically based instructional design theory for teaching concepts. *Review of Educational Research, 56*(1), 40–71. [doi:10.2307/1170286](https://doi.org/10.2307/1170286)
- Klahr, D., & Nigam, M. (2004). The equivalence of learning paths in early science instruction: Effects of direct instruction and discovery learning. *Psychological Science, 15*(10), 661–667. [doi:10.1111/j.0956-7976.2004.00737.x](https://doi.org/10.1111/j.0956-7976.2004.00737.x)
- Schwartz, D. L., & Bransford, J. D. (1998). A time for telling. *Cognition and Instruction, 16*(4), 475–522. [doi:10.1207/s1532690xci1604_4](https://doi.org/10.1207/s1532690xci1604_4)
- Merrill, M. D., & Tennyson, R. D. (1977). *Teaching concepts: An instructional design guide*. Educational Technology Publications.


<!-- deprecated 2026-10-02: superseded by the conditional model above; the body it replaced, kept verbatim.

## Description
Concept attainment is an inductive instructional pattern in which learners are shown carefully sequenced examples ("yes") and non-examples ("no") of a target concept and must infer its defining attributes themselves. Rather than receiving a definition first, learners generate and test hypotheses about what distinguishes exemplars from non-exemplars, then confirm their understanding by classifying novel instances. The pattern solves a persistent problem of definition-first teaching: learners can memorize a definition without grasping the concept's boundaries or its range of permissible variation.

## Implications

The pattern exploits the human capacity for inductive category learning: comparing contrasting cases forces attention to the attributes that vary between examples and those that remain constant [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S]. Hypothesis generation creates a productive gap between what learners expect and what the data show, motivating conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]. Because learners must hold candidate attributes in mind while evaluating each new example, the pattern depends on careful example sequencing and [chunking](../principles/chunking.md) of the attribute space to avoid overwhelming working memory.

### Context
#### Requirements
- A concept with identifiable defining attributes and a defensible boundary (not a fuzzy or contested concept)
- A pool of clear positive examples and matched negative examples, including "near misses" that differ on only one attribute
- A sequence that starts with unambiguous exemplars before introducing harder cases
- Time and structure for learners to state, test, and revise hypotheses aloud ([class discussion](../elements/class-discussion.md))

#### Constraints
- Inefficient for concepts learners could acquire faster from an explicit definition and worked examples; discovery of well-defined rules can be slower than direct explanation with no learning advantage [~M]
- Poorly chosen non-examples (too easy, or differing on irrelevant attributes) lead learners to infer wrong attributes [-M]
- Novices with minimal prior knowledge may fixate on salient but irrelevant features and build misconceptions that later need remediation [-M]
- Works poorly for concepts whose boundaries are genuinely contested (e.g., "democracy," "art") unless the goal is explicitly to explore those contested boundaries [~W]
- Hypothesis testing consumes class time; covering many concepts in a unit makes the pattern impractical at scale

#### Grain Size
Lesson — a single concept-attainment cycle fits one class period; a unit may cycle through several related concepts.

### Target Goals
- Acquisition of well-defined concepts and their defining attributes (e.g., "mammal," "prime number," "metaphor," "closed system")
- Discrimination skills: distinguishing exemplars from near-miss non-examples
- Hypothesis-testing and inductive reasoning as transferable processes
- Precise vocabulary attached to attributes learners have already isolated

### Target Learners
- Learners who have enough prior knowledge to generate plausible hypotheses but not enough to state the rule themselves [Activation improves learning.](../claims/activation-improves-learning.md) [+M]
- Learners prone to overgeneralizing from a single definition — the contrast set exposes boundary cases a definition hides
- Less suitable for complete novices, who lack the knowledge base for productive hypothesis generation [~M]

### Theory
#### Supporting
- [Information Processing Theory](../theories/information-processing-theory.md) — concept attainment is fundamentally a hypothesis-testing process operating within working-memory limits, which is why example sequencing matters
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) (Sweller) — well-structured example sets manage load; unstructured discovery imposes unnecessary search [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]
- [Constructivism](../theories/constructivism.md) — learners actively build category structure rather than receiving it; the pattern operationalizes guided induction

#### Contradicting / Qualifying
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — learners who already know the concept gain little from rediscovering it and may be slowed by the example sequence [~M]
- Direct instruction research (Klahr & Nigam) shows explicit explanation of a discovery strategy can outperform discovery itself for equivalent outcomes [~M]

### Claims
#### Supporting
- [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+S] — the yes/no example contrast is the engine of attribute isolation
- [Analogical reasoning improves transfer.](../claims/analogical-reasoning-improves-transfer.md) [+M] — comparing multiple exemplars supports schema abstraction that transfers to novel instances
- [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M] — non-examples that violate expectations drive refinement of the emerging concept
- [Advance organizers improve learning.](../claims/advance-organizers-improve-learning.md) [+M] — a framing question or attribute checklist can orient hypothesis generation without giving away the rule

#### Contradicting
- [Expertise reversal](../theories/expertise-reversal-effect.md) [~M] — for learners who already possess the concept, the inductive sequence adds load without adding structure

## Design

### Sequence
1. **Present focus and data** — Display labeled examples and non-examples, starting with clear exemplars; an [advance organizer](../elements/advance-organizers.md) frames the task ("What do all the 'yes' items share?")
2. **Hypothesize** — Learners state candidate attributes and test them against each new example; teacher responds only "yes" or "no," using [class discussion](../elements/class-discussion.md) to surface competing hypotheses
3. **Contrast near misses** — Introduce non-examples differing on a single attribute to sharpen the boundary; [analogies](../elements/analogies.md) can link the emerging concept to familiar categories
4. **Name and define** — Learners state the rule and essential attributes in their own words ([articulation](../elements/articulation.md)); the teacher supplies the conventional term and canonical definition
5. **Test on novel instances** — Learners classify new, unlabelled examples, including borderline cases ([application](../elements/application.md)); [feedback](../elements/assessment.md) confirms or corrects the attained concept
6. **Extend** — Apply the concept in [case studies](../elements/case-studies.md) or problem contexts where the concept must be recognized, not just defined

### Affordances
- [Activation](../principles/activation.md) — the hypothesis phase requires learners to retrieve and commit to prior knowledge before seeing confirmation, making existing schemas visible and revisable
- [Analogical Reasoning](../principles/analogical-reasoning.md) — comparing multiple exemplars is a structural analogy task; learners map shared relations across cases to abstract the concept
- [Active Learning](../principles/active-learning.md) — every learner generates, tests, and revises hypotheses rather than receiving a finished definition
- [Clear Structure](../principles/clear-structure.md) — the yes/no data set and phase sequence give the inductive work a predictable frame, preventing unstructured guessing

### Personalization

**Novices with no prior knowledge:** Begin with highly unambiguous exemplars and only two or three candidate attributes in play; provide an attribute checklist as an [advance organizer](../elements/advance-organizers.md). Delay near-miss non-examples until the core rule is stable.

**Learners with some background knowledge:** Start mid-sequence with harder, more ambiguous examples and require learners to generate their own non-examples — generating contrast cases deepens attribute analysis.

**Learners with anxiety or low confidence:** Allow private hypothesis-writing before public sharing, and normalize revised hypotheses ("wrong guesses are data"). Pair hypothesis generation so no learner's idea stands alone.

**Learners with diverse prior knowledge in the same cohort:** Assign roles in small groups — some generate hypotheses, others keep a running tally of which attributes survive each example — so every learner has an entry point into the same data set.

**Learners with language or learning differences:** Pair verbal examples with visual or concrete instances, keep the yes/no labels persistent and visible, and permit written hypothesis tracking so working memory is not spent holding the attribute list.


-->
