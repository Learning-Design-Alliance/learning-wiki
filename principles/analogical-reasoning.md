---
type: principle
id: analogical-reasoning
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
---

# Analogical Reasoning

> **Principle** · [All principles](index.md)
> **Evidence** · 7 claims (3 for, 4 mixed) · 14 studies (7 causal, 3 quant-synthesis, 3 review, 1 associational), `q2`–`q4` · 3 of 14 report an effect size · 1 claim rests on one study

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

- [Analogical Reasoning Improves Transfer](../claims/analogical-reasoning-improves-transfer.md) [+M]: a meta-analysis (`synthesis-experimental`) of 57 laboratory and classroom experiments (336 tests). Case-comparison activities produced greater learning than sequential, single-case or non-analogous case study, traditional instruction and controls, d = .50, 95% CI [.44, .56]. Benefits were larger when learners looked for similarities, when the principle came after the comparison, with perceptual content, and on immediate tests; the moderator sizes are not recorded (abstract only). Also, three `randomized` experiments with novice undergraduates learning negotiation (n = 334 in all). In Experiment 2, 48% of those who compared two cases on one page used the principle in a new negotiation, against 19% of those who studied the same cases separately. No standardised effect size is reported, and the claim page does not state the delay. Because both groups saw the same cases, the design isolates comparison itself. What this supports is mapping between two provided analogous cases, not an analogy to a familiar source domain. The pooled d mixes several kinds of comparison condition. Partly checked: 1 of 2 entries pass, the rest could not be confirmed (abstract). [Multiple contrasting cases support abstraction](../claims/comparing-contrasting-cases-improves-learning.md) [+M] rests on the same two entries and adds no study.
- [Comparing cases side by side improves learning and transfer by a moderate average amount, though in one algebra study it raised procedural knowledge and flexibility but not conceptual knowledge](../claims/comparing-contrasting-cases-improves-learning.md) [~M]: the same two studies, plus a `randomized` experiment with 70 seventh-graders learning to solve equations. Comparing alternative solution methods side by side raised procedural knowledge and procedural flexibility more than reflecting on the same methods one at a time, and conceptual knowledge no more. It is used here for that qualification. Comparison can change how learners use and choose methods without changing their `conceptual-understanding`. No effect size in the abstract read. Partly checked: 2 of 3 entries pass, the rest could not be confirmed (abstract).
- [Presenting multiple cases from different perspectives supports transfer in ill-structured domains](../claims/cognitive-flexibility-theory-multiple-cases.md) [~M]: a small `randomized` experiment (34 paid university volunteers, 17 per group after pooling two drill controls) on the social impact of technology. Revisiting short cases under several themes produced better transfer essays by the fourth session than computer drill (9.47 vs 7.24 on a 15-point scale), while the drill group scored higher on factual recall. The treatment bundled several features. It qualifies the relationship in two ways: multi-case work may trade recall for transfer, and the claim page notes that the meta-analysis's smaller delayed benefit cuts against the expectation that the advantage grows with delay. Not settled: the text available could not confirm the entries (abstract).
- [PAIR-C scaffolding shows mixed evidence for deep understanding and reduced misconceptions in emergent-phenomena instruction](../claims/pair-c-scaffolding-shows-mixed-evidence-for-emergent-phenomena-instruction.md) [~W]: a `controlled-nonrandom` pre/post study of 50 pre-service teachers learning natural selection with the same simulations. Explicitly contrasting emergent and sequential causal structure gave a significant advantage on `near-transfer` tasks. Deep understanding and misconception reduction only trended (p = .059, .060, .095). Neither group reached `far-transfer` to an unrelated emergent phenomenon, and persistence was not measured. It limits the relationship: contrasting structure within one domain did not by itself carry the structure to a new domain. The claim page reports the authors' suggestion that cross-domain analogical comparison may be needed, which is untested here. One study; not yet checked against its source.

Taken together: comparing provided analogous cases has `synthesis-experimental` and `randomized` support for learning and near transfer, mostly with novices and at short horizons. The gain may be procedural rather than conceptual. Far transfer across domains, delayed retention and analogies drawn from a familiar source domain are not established. Comparators (separate cases, drill, other activities) and outcomes (a negotiation, transfer essays, procedural items, near-transfer tasks) differ, so do not rank these results by effect label.

How far each may be carried: the comparison evidence supports steps 2–4 of the default design for cases learners are given. It does not show that a single explanatory analogy (water for current) helps, or that it is harmless. The cognitive-flexibility study is one bundled treatment in one ill-structured domain. The PAIR-C study is one domain and one population of adult pre-service teachers.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — not settled: the text available could not confirm the entries (abstract)
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~M] — not settled: the text available could not confirm the entries (abstract)

## Objective and learner-valued goal

The designer's objective names the relation to be abstracted, the kind of new case it should be used on (near or far, prompted or unprompted), and the horizon. Elicit separately what the learner wants from it. Agreement, divergence and uncertainty are observations.

For example, an apprentice electrician may want to be able to tell which circuit in a house will trip a breaker. The designer's objective is a working model of current, voltage and resistance, taught through a water-flow analogy and compared circuits. A learner who can retell the water analogy, or who solves the compared circuits, has met neither aim yet. Probe with an unfamiliar circuit, unprompted, and ask for a prediction the analogy would get wrong if it were overextended. Record both aims, so that fluency with the analogy is not read as the capability the learner came for.

## What would revise this model?

The model should weaken if well-controlled comparisons with comparable learners find no transfer advantage for comparing analogous cases over studying them separately, or find that the advantage disappears at the delay the objective needs. If analogies from a familiar source domain are tested and are found to leave misconceptions that a direct explanation would not, step 1's check and step 5's limits become requirements, not options, or the analogy should be dropped. If comparison keeps changing procedures but not concepts, keep that distinction rather than calling both understanding. If far transfer needs cross-domain comparison, as one study's authors suggest, that is a separate configuration to test. Do not protect the model by calling every transfer failure a retrieval failure or a lack of prior knowledge.

Recognising that a source applies, mapping it correctly, using the principle on a near case, using it in another domain, and remembering it later are separate claims. The present evidence does not establish how many cases to use, how similar they should be, or whether analogies a learner generates for themselves help or hurt.

## Related Principles
- [Metaphors & Analogies](metaphors-analogies.md) — analogical reasoning is one of the strongest structured forms of analogy use in teaching
- [Activation](activation.md) — analogies often work by activating prior knowledge before introducing a new concept
- [Constructivist Learning](constructivism.md) — analogies help learners build new understanding out of familiar structures

## Examples

### Illustrative

**[Analogies](../elements/analogies.md)** — A teacher explains electric current through a water-flow analogy, then explicitly identifies where the analogy helps and where it breaks down.

**[Metaphors](../elements/metaphors.md)** — Learners compare the structure of an atom to a solar system model, then critique the limits of the comparison so the metaphor does not harden into misconception.

**Comparing parallel cases** — In math or science, learners study two situations with different surface details but the same underlying relationship, then explain the shared structure before solving a new transfer problem.

## Key Sources
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155-170. [https://doi.org/10.1207/s15516709cog0702_3](https://doi.org/10.1207/s15516709cog0702_3)
- Richland, L. E., Zur, O., & Holyoak, K. J. (2007). Cognitive supports for analogies in the mathematics classroom. *Science, 316*(5828), 1128-1129. [https://doi.org/10.1126/science.1142103](https://doi.org/10.1126/science.1142103)

<!-- deprecated 2026-10-02: superseded by the conditional model above; the previous body is kept verbatim.

## Description
Analogical reasoning is the principle of using relational similarity between a familiar case and a new case to support understanding, inference, and transfer. It is useful when the surface details differ but the underlying structure is similar enough to guide thinking.

## Implications

Analogical reasoning is most valuable when learners need help seeing a new concept through the structure of something they already understand. The principle works best when the analogy highlights deep relational similarity rather than superficial resemblance alone, because a coherent mapping can reduce interpretive burden and help learners organize new information [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]. In instruction, that means the teacher or task must help learners map the source and target explicitly, notice where the analogy is helpful, and identify where it breaks down; analogies become even stronger when learners explain why the mapping works [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Poor analogies do not merely fail to help; they can actively mislead by inviting false transfer from surface features, though even confident misreadings can become productive if the mismatch is made explicit and corrected [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~M].

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
- [Metaphors & Analogies](metaphors-analogies.md) — provides the broader family of instructional moves that analogical reasoning belongs to
- [Information Processing Theory](../theories/information-processing-theory.md) — analogies can reduce interpretive burden by linking new content to existing schema

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — analogies support construction of meaning, but only if learners actively interpret and test the mapping rather than accept it uncritically

### Claims
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — analogies can support chunking and organization when the relational mapping is coherent
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — analogies become stronger when learners explain why the mapping works
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~M] — analogies that trigger confident but incorrect predictions can still be instructionally useful if the mismatch is corrected explicitly
-->
