---
type: principle
id: analogical-reasoning
aliases: [metaphors-analogies]
title: Analogical Reasoning
description: "Comparing a new situation with a provided analogous case, prompted to find the shared relation and followed by the principle, is expected to help learners who do not yet see that structure transfer it to a near new case at a short horizon; analogies from a familiar source domain, far transfer and delayed effects are untested here."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
sources:
  - id: gentner-1983
    resource: "https://doi.org/10.1207/s15516709cog0702_3"
    title: "Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155-170"
    author: Gentner, D
  - id: richland-2007
    resource: "https://doi.org/10.1126/science.1142103"
    title: "Richland, L. E., Zur, O., & Holyoak, K. J. (2007). Cognitive supports for analogies in the mathematics classroom. *Science, 316*(5828), 1128-1129"
    author: "Richland, L. E., Zur, O., & Holyoak, K. J"
  - id: gentner-2017
    resource: "https://doi.org/10.1111/tops.12278"
    title: "Gentner, D., & Hoyos, C. (2017). Analogy and abstraction. *Topics in Cognitive Science, 9*(3), 672-693"
    author: "Gentner, D., & Hoyos, C"
  - id: richland-2015
    resource: "https://doi.org/10.1002/wcs.1336"
    title: "Richland, L. E., & Simms, N. (2015). Analogy, higher order thinking, and education. *Wiley Interdisciplinary Reviews: Cognitive Science, 6*(2), 177-192"
    author: "Richland, L. E., & Simms, N"
  - id: thibodeau-2017
    resource: "https://doi.org/10.1016/j.tics.2017.07.001"
    title: "Thibodeau, P. H., Hendricks, R. K., & Boroditsky, L. (2017). How linguistic metaphor scaffolds reasoning. *Trends in Cognitive Sciences, 21*(11), 852-863"
    author: "Thibodeau, P. H., Hendricks, R. K., & Boroditsky, L"
---

# Analogical Reasoning

> **Principle** · [All principles](index.md)
> **Evidence** · 16 claims (6 for, 10 mixed) · 23 studies (9 causal, 4 review, 4 qualitative, 3 quant-synthesis, 2 associational, 1 design), `q2`–`q4` · 3 of 23 report an effect size · 9 claims rest on one study

## Conditional relationship

This principle is about a learner who meets a new situation (a problem, a case, a concept) and does not yet see its relational structure. Their starting response might be treating the situation as wholly unfamiliar, answering from its surface features, or knowing a principle from one context without using it here. The expectation is that **mapping the relations of one situation onto another**, by comparing two or more analogous cases or by setting a familiar source beside the new target, helps them abstract the shared structure and use it on a new case (`near-transfer`). The expectation is strongest when learners are prompted to find what the situations share, the principle is made explicit after the comparison, and the test comes soon after. The target knowledge is a `principle` or a `procedure` whose structure can be shown in more than one surface form.

The wiki tests only part of this. Its evidence is about *comparing two or more provided cases* (`case-comparison`), mostly with `novice` learners and mostly on immediate or same-study tests. **No claim here tests the classic teaching analogy**, in which a teacher explains a new target through a familiar source domain (water flow for electric current, a solar system for an atom). It is also not shown what happens at `delayed-retention`, in `far-transfer` across domains, or when the source analogy is overextended. Whether the learner knows the source well, whether the two situations really share the relation, and whether the learner retrieves the source unprompted are conditions that must be established locally.

The [case-based learning pattern](../patterns/case-based-learning.md) already holds a converted policy for the case-comparison part: how to choose cases, compare them, and time the principle. This page owns the more general relationship, structural mapping between a familiar or provided source and a new target, and places case comparison inside it as the configuration with the best evidence. No pattern yet covers explanatory analogies from a familiar source domain.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal with its evidence status stated beside it. Most of it is untested as written.

1. **Check the source before relying on it.** Confirm that learners can reason in the source domain (for example, predict what happens in the water system) before mapping it onto the target. Untested here; from the earlier page ("weak prior knowledge limits the benefit"). The comparison experiments below gave learners both cases to study, so they do not test analogies to a source learners are assumed to know.
2. **Choose a source and target that share a genuine relation, not only a resemblance.** Where possible, use at least two sources or cases that differ in surface detail and share the relation. Evidence: comparing analogous cases beats studying the same cases separately (see below). Using two cases rather than one source analogy is supported; how many is enough is not settled.
3. **Supply the source and prompt the mapping explicitly.** Ask what corresponds to what, and what is the same and why. Evidence: in the meta-analysis the benefit was larger when learners were asked to find similarities, and in the negotiation experiments more comparison support raised transfer.
4. **State the principle after the comparison**, connected to what learners found. Evidence: in the same meta-analysis the benefit was larger when the principle was given after the comparison. No dose or lag is set.
5. **Name where the analogy breaks down**, and have learners find a mismatch themselves. Untested here; from the earlier page. No claim in the wiki tests whether discussing the limits of an analogy prevents misconceptions.
6. **Judge the design on a new case with different surface features**, scored apart from recall and procedure use, and repeat it after a delay if the objective needs durable use. Evidence: immediate benefits were larger than delayed ones, and one study found comparison raised procedural knowledge but not conceptual knowledge (see below).

## Fitting the design to a situation

Ask for four facts when the brief omits them: **will learners compare two provided cases, or meet one explanatory analogy from a familiar source?**, **do they know the source well?**, **is the target near transfer within the domain or far transfer across domains?**, and **when will transfer be tested?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| The goal is using a principle on new cases | Give two or more cases that share the principle, side by side, with a prompt to say what is the same and why | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] |
| The plan states the principle and then gives examples | Have learners compare first and state the principle after, connected to what they found | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] (moderator in the meta-analysis) |
| Learners work alone (`online-self-paced`) | Show both cases on one screen and ask for a written description of their similarities; reading the same cases separately gave far less transfer | [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] |
| The goal is conceptual understanding in mathematics | After learners compare solution methods, explain why each method works; comparison raised procedural knowledge and flexibility, not conceptual knowledge | [Comparing cases: procedural gain, no conceptual gain in one algebra study](../claims/comparing-contrasting-cases-improves-learning.md) [~M] |
| The domain is ill structured | Revisit several cases under different themes and plan separate recall practice; transfer rose while factual recall favoured drill | [Multiple cases from different perspectives support transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M] |
| The test that matters is delayed | Repeat the comparison or retrieve the principle later; benefits were larger on immediate tests | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [~M] |
| Far transfer to another domain is the goal | Add a cross-domain comparison and a fresh case from the far domain; in one study contrasting causal structures gave near but not far transfer | [PAIR-C scaffolding: near-transfer gain, no far transfer](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~W] |
| The plan uses one explanatory analogy from a familiar source (water flow for current) | Check that learners can reason in the source first, ask them what corresponds to what, and name where the analogy breaks down | untested proposal; no claim in the wiki tests a single explanatory analogy |
| Analogies are generated by AI or personalised to learners' interests | Have learners check the mapping between source and target and name where it breaks; learners found such analogies memorable but flagged specific mismatches | [Students evaluate GenAI analogies by structural correspondence](../claims/students-audit-genai-analogy-structural-correspondence.md) [~W]; [Personalised analogies felt more engaging or memorable](../claims/personalized-analogies-more-engaging-memorable.md) [~W] |
| Learners are novices in the domain of the cases | Use comparison; the experiments recorded here used novice undergraduates (negotiation) and seventh graders (algebra). Supply both cases rather than relying on a source they are assumed to know | [Analogical reasoning improves transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]; [Comparing cases side by side improves learning and transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M] |

## Observation, state and explanation

What can be observed is a response to a particular task under stated conditions: a prediction, a solution, a named similarity, a principle stated or not, a transfer attempt with or without a hint. "Has abstracted the schema", "understands the source" and "was misled by the analogy" are inferred states. Record which source or cases were given, every comparison prompt and hint, and whether the learner was told that an earlier case was relevant. Recognising that a principle applies and being able to apply it are different performances.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Solves a new case when told "this is like the earlier ones", not without the hint | Principle abstracted but not retrieved spontaneously; principle tied to the earlier cases' surface; the hint itself gave away the method | Give matched new cases with and without the hint, and a case with the earlier surface but a different principle; see whether success follows the hint, the surface or the principle. |
| Names surface features when asked what two cases share | Too little knowledge of either case to see the relation; ambiguous prompt; cases differ on too many dimensions | Ask what would change the outcome of each case; re-run the comparison with cases aligned on surface and differing on one relation. |
| Uses the source analogy fluently but makes a wrong prediction in the target (for example, current "used up" in a bulb) | Attribute of the source carried over that does not map; misconception held before the analogy; source domain itself misunderstood | Ask for the same prediction in the source domain first, then ask which parts of the source correspond to which parts of the target. |
| Chooses and carries out methods better after comparison, explains the concept no better | Comparison supported method choice, not the concept; conceptual test misaligned with what was compared; too little time | Score procedural and conceptual items separately on matched content, and add an explanation item about why the method works. |
| Transfers to a near case in the same domain, not to an unrelated domain with the same structure | Structure recognised only within the taught domain; far task demands other knowledge; no cross-domain comparison was given | Give a cross-domain comparison prompt and then a fresh far case, and record whether the domain knowledge it needs is held. |

These are proposals, untested with learners. A probe can shift confidence between explanations; it does not identify a cause, and probing itself teaches (a hinted transfer item is also a comparison).

## Evidence and qualifications

The claims below share their strongest entries. Alfieri et al.'s meta-analysis and Gentner et al.'s negotiation experiments sit under several titles, so **count studies, not claims**: five distinct studies stand behind the four core claims.

- [Analogical Reasoning Improves Transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+M]: a meta-analysis (`synthesis-experimental`) of 57 laboratory and classroom experiments (336 tests). Case-comparison activities produced greater learning than sequential, single-case or non-analogous case study, traditional instruction and controls, d = .50, 95% CI [.44, .56]. Benefits were larger when learners looked for similarities, when the principle came after the comparison, with perceptual content, and on immediate tests; the moderator sizes are not recorded (abstract only). Also, three `randomized` experiments with novice undergraduates learning negotiation (n = 334 in all). In Experiment 2, 48% of those who compared two cases on one page used the principle in a new negotiation, against 19% of those who studied the same cases separately. No standardised effect size is reported, and the claim page does not state the delay. Because both groups saw the same cases, the design isolates comparison itself. What this supports is mapping between two provided analogous cases, not an analogy to a familiar source domain. The pooled d mixes several kinds of comparison condition. Partly checked: 1 of 2 entries pass, the rest could not be confirmed (abstract). [Multiple contrasting cases support abstraction](../claims/comparing-contrasting-cases-improves-learning.md) [+M] rests on the same two entries and adds no study.
- [Comparing cases side by side improves learning and transfer by a moderate average amount, though in one algebra study it raised procedural knowledge and flexibility but not conceptual knowledge](../claims/comparing-contrasting-cases-improves-learning.md) [~M]: the same two studies, plus a `randomized` experiment with 70 seventh-graders learning to solve equations. Comparing alternative solution methods side by side raised procedural knowledge and procedural flexibility more than reflecting on the same methods one at a time, and conceptual knowledge no more. It is used here for that qualification. Comparison can change how learners use and choose methods without changing their `conceptual-understanding`. No effect size in the abstract read. Partly checked: 2 of 3 entries pass, the rest could not be confirmed (abstract).
- [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M]: a small `randomized` experiment (34 paid university volunteers, 17 per group after pooling two drill controls) on the social impact of technology. Revisiting short cases under several themes produced better transfer essays by the fourth session than computer drill (9.47 vs 7.24 on a 15-point scale), while the drill group scored higher on factual recall. The treatment bundled several features. It qualifies the relationship in two ways: multi-case work may trade recall for transfer, and the claim page notes that the meta-analysis's smaller delayed benefit cuts against the expectation that the advantage grows with delay. Not settled: the text available could not confirm the entries (abstract).
- [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~W]: a `controlled-nonrandom` pre/post study of 50 pre-service teachers learning natural selection with the same simulations. Explicitly contrasting emergent and sequential causal structure gave a significant advantage on `near-transfer` tasks. Deep understanding and misconception reduction only trended (p = .059, .060, .095). Neither group reached `far-transfer` to an unrelated emergent phenomenon, and persistence was not measured. It limits the relationship: contrasting structure within one domain did not by itself carry the structure to a new domain. The claim page reports the authors' suggestion that cross-domain analogical comparison may be needed, which is untested here. One study; not yet checked against its source.

Taken together: comparing provided analogous cases has `synthesis-experimental` and `randomized` support for learning and near transfer, mostly with novices and at short horizons. The gain may be procedural rather than conceptual. Far transfer across domains, delayed retention and analogies drawn from a familiar source domain are not established. Comparators (separate cases, drill, other activities) and outcomes (a negotiation, transfer essays, procedural items, near-transfer tasks) differ, so do not rank these results by effect label.

How far each may be carried: the comparison evidence supports steps 2–4 of the default design for cases learners are given. It does not show that a single explanatory analogy (water for current) helps, or that it is harmless. The cognitive-flexibility study is one bundled treatment in one ill-structured domain. The PAIR-C study is one domain and one population of adult pre-service teachers.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/analogical-reasoning.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does comparing analogous cases improve transfer more than studying cases one at a time? [Analogical Reasoning Improves Transfer](../claims/comparing-contrasting-cases-improves-learning.md) [+S]: 5 distinct studies.
- Does teaching through realistic cases, by itself, raise learning? [Case-based learning improves exam performance](../claims/case-based-learning-improves-exam-performance.md) [~S]: 4 distinct studies.
- How do learners receive an explanatory analogy from a familiar source domain? [Most participants described interest-personalized GenAI analogies as more engaging or memorable than generic technical explanations](../claims/personalized-analogies-more-engaging-memorable.md) [~M]: 2 distinct studies.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — not settled: the text available could not confirm the entries (abstract)
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Students avoided metaphorical visualizations they perceived as childish or insufficiently rigorous, signaling disciplinary legitimacy concerns even when the tools could help them](../claims/legitimacy-disciplinary-identity-resistance.md) [~W]
- [Students without prior programming experience anchor more heavily in code and engage minimally with metaphor views compared to students with prior experience](../claims/prior-experience-shapes-view-engagement.md) [~M]
- [Collaborative metaphor workshops helped higher education staff and students make sense of GenAI and raised their awareness of its ethical dimensions](../claims/metaphor-workshops-support-genai-sensemaking.md) [+W]
- [Concrete, outcome-oriented eco-feedback visualizations with real-world analogies are rated more favorably than abstract metrics](../claims/concrete-eco-feedback-visualizations-preferred-over-abstract.md) [+W]
- [Qualities metaphors depicted GenAI as unknowable, unreliable and unbounded, with participants unsettled by its opacity](../claims/qualities-metaphors-genai-unknowable-unreliable.md) [~W]
- [Role metaphors positioned GenAI as helper, learning partner, and friend/foe, with a high proportion combining friend and foe](../claims/role-metaphors-genai-frenemy-ambivalence.md) [+W]
- [Students who compared a climate model with non-climate analog models during productive failure scored significantly higher on far across domain transfer than students who used only the climate model](../claims/two-models-comparison-far-across-domain-transfer.md) [+M] — attached 2026-10-23 from Jacobson et al. (2020), which proposed "Scaffold comparison of two contrasting-domain models during productive failure exploration to foster far across domain transfer"; tests this page's relationship.

## Objective and learner-valued goal

The designer's objective names the relation to be abstracted, the kind of new case it should be used on (near or far, prompted or unprompted), and the horizon. Elicit separately what the learner wants from it. Agreement, divergence and uncertainty are observations.

For example, an apprentice electrician may want to be able to tell which circuit in a house will trip a breaker. The designer's objective is a working model of current, voltage and resistance, taught through a water-flow analogy and compared circuits. A learner who can retell the water analogy, or who solves the compared circuits, has met neither aim yet. Probe with an unfamiliar circuit, unprompted, and ask for a prediction the analogy would get wrong if it were overextended. Record both aims, so that fluency with the analogy is not read as the capability the learner came for.

## What would revise this model?

The model should weaken if well-controlled comparisons with comparable learners find no transfer advantage for comparing analogous cases over studying them separately, or find that the advantage disappears at the delay the objective needs. If analogies from a familiar source domain are tested and are found to leave misconceptions that a direct explanation would not, step 1's check and step 5's limits become requirements, not options, or the analogy should be dropped. If comparison keeps changing procedures but not concepts, keep that distinction rather than calling both understanding. If far transfer needs cross-domain comparison, as one study's authors suggest, that is a separate configuration to test. Do not protect the model by calling every transfer failure a retrieval failure or a lack of prior knowledge.

Recognising that a source applies, mapping it correctly, using the principle on a near case, using it in another domain, and remembering it later are separate claims. The present evidence does not establish how many cases to use, how similar they should be, or whether analogies a learner generates for themselves help or hurt.

## Related Principles
- [Activation](activation.md) — analogies often work by activating prior knowledge before introducing a new concept
- [Constructivist Learning](cognitive-activation.md) — analogies help learners build new understanding out of familiar structures
- [Creating Visual Representations](dual-coding.md) — analogies often become more useful when represented visually.
- [Graphic Organizers](graphic-organizers.md) — organizers can help learners map which parts of an analogy align and where it breaks.
- [Inquiry-based Learning](inquiry-based-learning.md) — learners can generate and test analogies while exploring new concepts.

## Examples

- **Math analogies**: A teacher uses balance-scale imagery to explain equation solving and then asks learners to test where the analogy holds.
- **Science metaphors**: Learners compare electrical flow to water flow, then identify the limits of the comparison.
- **Writing identity metaphors**: Learners use metaphor to describe their writing process and reflect on how that framing shapes revision habits.
- **Digital literacy comparisons**: Learners use familiar physical systems to reason about files, networks, or information flow.
- [A model of twelve divergent thinking activities organised along two dimensions of remoteness and abstractness](../designs/twelve-activity-model-remoteness-abstractness.md)
- [Hybrid productive failure with analogical comparison: schema abstraction through comparing contrasting models](../designs/hybrid-pf-analogical-comparison-schema-abstraction.md)

### Illustrative

**[Analogies](../elements/analogies.md)** — A teacher explains electric current through a water-flow analogy, then explicitly identifies where the analogy helps and where it breaks down.

**[Metaphors](../elements/metaphors.md)** — Learners compare the structure of an atom to a solar system model, then critique the limits of the comparison so the metaphor does not harden into misconception.

**Comparing parallel cases** — In math or science, learners study two situations with different surface details but the same underlying relationship, then explain the shared structure before solving a new transfer problem.

## Key Sources
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155-170. [https://doi.org/10.1207/s15516709cog0702_3](https://doi.org/10.1207/s15516709cog0702_3)
- Richland, L. E., Zur, O., & Holyoak, K. J. (2007). Cognitive supports for analogies in the mathematics classroom. *Science, 316*(5828), 1128-1129. [https://doi.org/10.1126/science.1142103](https://doi.org/10.1126/science.1142103)
- Gentner, D., & Hoyos, C. (2017). Analogy and abstraction. *Topics in Cognitive Science, 9*(3), 672-693. [https://doi.org/10.1111/tops.12278](https://doi.org/10.1111/tops.12278)
- Richland, L. E., & Simms, N. (2015). Analogy, higher order thinking, and education. *Wiley Interdisciplinary Reviews: Cognitive Science, 6*(2), 177-192. [https://doi.org/10.1002/wcs.1336](https://doi.org/10.1002/wcs.1336)
- Thibodeau, P. H., Hendricks, R. K., & Boroditsky, L. (2017). How linguistic metaphor scaffolds reasoning. *Trends in Cognitive Sciences, 21*(11), 852-863. [https://doi.org/10.1016/j.tics.2017.07.001](https://doi.org/10.1016/j.tics.2017.07.001)

<!-- deprecated 2026-10-02: superseded by the conditional model above; the previous body is kept verbatim.

## Description
Analogical reasoning is the principle of using relational similarity between a familiar case and a new case to support understanding, inference, and transfer. It is useful when the surface details differ but the underlying structure is similar enough to guide thinking.

## Implications

Analogical reasoning is most valuable when learners need help seeing a new concept through the structure of something they already understand. The principle works best when the analogy highlights deep relational similarity rather than superficial resemblance alone, because a coherent mapping can reduce interpretive burden and help learners organize new information [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]. In instruction, that means the teacher or task must help learners map the source and target explicitly, notice where the analogy is helpful, and identify where it breaks down; analogies become even stronger when learners explain why the mapping works [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Poor analogies do not merely fail to help; they can actively mislead by inviting false transfer from surface features, though even confident misreadings can become productive if the mismatch is made explicit and corrected [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [~M].

### Context
#### Requirements
- **A familiar source domain and a target domain with meaningful structural overlap** — the analogy has to preserve a genuine relation, not just a catchy comparison
- **Prompts that make the shared relation explicit** — learners often need help seeing how the source maps onto the target
- **Discussion of where the analogy breaks down** — instructional analogies are strongest when their limits are named
#### Constraints
- **Surface-feature matches can mislead learners if the deep structure differs**
- **Overextended analogies can create misconceptions**
- **Weak prior knowledge limits the benefit** — if learners do not understand the source domain, the analogy cannot do much explanatory work

### Target Learners
- Learners encountering abstract, invisible, or complex concepts for the first time
- Learners who benefit from conceptual bridges between familiar and unfamiliar domains
- Novices who need support recognizing structural similarity across contexts

### Target Learning Objectives
- Improve conceptual understanding, transfer, and relational reasoning
- Help learners recognize underlying structure rather than relying only on surface cues
- Support explanation and prediction in new domains through structured comparison

### Theory
#### Supporting
- Structure-mapping perspectives on analogy — analogical reasoning works when relational correspondences are preserved across domains
- [Metaphors & Analogies](analogical-reasoning.md) — provides the broader family of instructional moves that analogical reasoning belongs to
- [Information Processing Theory](../theories/information-processing-theory.md) — analogies can reduce interpretive burden by linking new content to existing schema

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — analogies support construction of meaning, but only if learners actively interpret and test the mapping rather than accept it uncritically

### Claims

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — analogies can support chunking and organization when the relational mapping is coherent
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — analogies become stronger when learners explain why the mapping works
- [High-confidence errors are more likely than low-confidence errors to be corrected on a later test after feedback.](../claims/high-confidence-errors-improve-retention.md) [~M] — analogies that trigger confident but incorrect predictions can still be instructionally useful if the mismatch is corrected explicitly
-->
- [Undergraduate computing students evaluate GenAI analogies by structural correspondence between source and target domain, flagging specific mapping breakdowns rather than judging holistically](../claims/students-audit-genai-analogy-structural-correspondence.md) [~W]

<!-- merged 2026-10-15 from principles/metaphors-analogies ("Metaphors & Analogies"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Metaphors & Analogies

> **Principle** · [All principles](index.md)
> **Evidence** · 10 claims (5 for, 5 mixed) · 14 studies (5 qualitative, 2 causal, 2 quant-synthesis, 2 review, 2 associational, 1 design), `q2`–`q4` · 1 of 14 report an effect size · 7 claims rest on one study

## Description
Metaphors and analogies help learners understand unfamiliar ideas by mapping them onto more familiar experiences, systems, or images. Their instructional power lies in comparative structure: they can make abstract concepts more concrete, reveal patterns, and help learners reason about relationships they might otherwise miss. Used carefully, they support explanation, transfer, and conceptual flexibility. Used carelessly, they can oversimplify or mislead.

## Implications
Metaphors and analogies work because they let learners reason from a known structure toward an unfamiliar one. A good analogy can reduce the effort of building a concept from scratch and make abstract relationships easier to grasp [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S], especially when learners explain the mapping in their own words [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. The design caution is that analogies are only partial bridges: unless instructors explicitly mark where the comparison fits and where it breaks, learners may overextend the metaphor and build durable misconceptions.

### Context
#### Requirements
- **A well-chosen source analogy**: The familiar comparison has to map meaningfully onto the target concept, not just sound catchy.
- **Explicit mapping**: Instructors should name what carries over from the analogy and what does not.
- **Support for interpretation**: Learners often need prompts to explain the analogy in their own words or test its limits.
- **Alignment to the learning goal**: Analogies work best when the goal involves conceptual structure, pattern recognition, or abstraction.
#### Constraints
- **Misleading carryover**: Learners may overextend the analogy to places where it no longer fits.
- **Surface similarity traps**: A comparison that shares only superficial features can create durable misconceptions.
- **Cultural mismatch**: An analogy can fail if the supposedly familiar source domain is not actually familiar to the learners.
- **Overreliance**: Learners still need formal language and direct explanation, not only figurative framing.

### Target Learners
- **Learners encountering abstract ideas**: Strong fit for conceptual, disciplinary, or symbolic content that needs a bridge from the known to the unknown.
- **Learners building higher-order reasoning**: Analogies support comparison, transfer, and flexible interpretation.
- **Learners with strong prior knowledge in another domain**: The strategy works when existing knowledge can become a scaffold.
- **Writers and explainers**: Metaphor can support identity-building, communication, and explanatory power as well as comprehension.

### Target Learning Objectives
- **Conceptual understanding**: Building an initial model of an abstract or unfamiliar idea.
- **Transfer and pattern recognition**: Seeing structural similarity across situations or domains.
- **Flexible thinking**: Reframing a problem or concept through a new lens.
- **Communication and explanation**: Expressing difficult ideas in more memorable and interpretable ways.

### Theory
#### Supporting
- Information processing views — analogies reduce the burden of inventing structure from scratch by connecting to existing schemas.
- Dual-coding-related perspectives — metaphor and analogy often become stronger when supported with image, gesture, or diagram as well as words.
- Structure-mapping traditions in cognitive science — analogy supports reasoning by aligning relational patterns across domains.
#### Contradicting / Qualifying
- Analogies do not replace precise disciplinary explanation.
- Learners may need help separating productive metaphor from literal truth, especially in science, mathematics, and policy topics.

### Claims

- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — analogies teach more when learners explain how the source and target actually map
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — a strong analogy can reduce interpretive burden by giving learners a familiar structure to think with
- [Students avoided metaphorical visualizations they perceived as childish or insufficiently rigorous, signaling disciplinary legitimacy concerns even when the tools could help them](../claims/legitimacy-disciplinary-identity-resistance.md) [~W]
- [Most participants described interest-personalized GenAI analogies as more engaging or memorable than generic technical explanations](../claims/personalized-analogies-more-engaging-memorable.md) [+W]
- [Students without prior programming experience anchor more heavily in code and engage minimally with metaphor views compared to students with prior experience](../claims/prior-experience-shapes-view-engagement.md) [~M]
- [Undergraduate computing students evaluate GenAI analogies by structural correspondence between source and target domain, flagging specific mapping breakdowns rather than judging holistically](../claims/students-audit-genai-analogy-structural-correspondence.md) [~W]
- [Collaborative metaphor workshops helped higher education staff and students make sense of GenAI and raised their awareness of its ethical dimensions](../claims/metaphor-workshops-support-genai-sensemaking.md) [+W]
- [Concrete, outcome-oriented eco-feedback visualizations with real-world analogies are rated more favorably than abstract metrics](../claims/concrete-eco-feedback-visualizations-preferred-over-abstract.md) [+W]
- [Qualities metaphors depicted GenAI as unknowable, unreliable and unbounded, with participants unsettled by its opacity](../claims/qualities-metaphors-genai-unknowable-unreliable.md) [~W]
- [Role metaphors positioned GenAI as helper, learning partner, and friend/foe, with a high proportion combining friend and foe](../claims/role-metaphors-genai-frenemy-ambivalence.md) [+W]

## Related Principles
- [Creating Visual Representations](dual-coding.md) — analogies often become more useful when represented visually.
- [Graphic Organizers](graphic-organizers.md) — organizers can help learners map which parts of an analogy align and where it breaks.
- [Explaining Their Thinking](cognitive-activation.md) — asking learners to explain an analogy surfaces whether the mapping is actually understood.
- [Inquiry-based Learning](inquiry-based-learning.md) — learners can generate and test analogies while exploring new concepts.

## Examples
- **Math analogies**: A teacher uses balance-scale imagery to explain equation solving and then asks learners to test where the analogy holds.
- **Science metaphors**: Learners compare electrical flow to water flow, then identify the limits of the comparison.
- **Writing identity metaphors**: Learners use metaphor to describe their writing process and reflect on how that framing shapes revision habits.
- **Digital literacy comparisons**: Learners use familiar physical systems to reason about files, networks, or information flow.

## Key Sources
- Gentner, D., & Hoyos, C. (2017). Analogy and abstraction. *Topics in Cognitive Science, 9*(3), 672-693. [https://doi.org/10.1111/tops.12278](https://doi.org/10.1111/tops.12278)
- Richland, L. E., & Simms, N. (2015). Analogy, higher order thinking, and education. *Wiley Interdisciplinary Reviews: Cognitive Science, 6*(2), 177-192. [https://doi.org/10.1002/wcs.1336](https://doi.org/10.1002/wcs.1336)
- Thibodeau, P. H., Hendricks, R. K., & Boroditsky, L. (2017). How linguistic metaphor scaffolds reasoning. *Trends in Cognitive Sciences, 21*(11), 852-863. [https://doi.org/10.1016/j.tics.2017.07.001](https://doi.org/10.1016/j.tics.2017.07.001)
-->
