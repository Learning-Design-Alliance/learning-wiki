---
type: claim
title: "Prompting learners to self-explain, one generative strategy, improves learning by a moderate average amount; other generative activities are not tested by the evidence recorded here"
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: generative-processing-improves-learning
aliases: [generative-learning-improves-retention, generative-learning-improves-comprehension]
evidence_strength:
sources:
  - id: bisra-et-al-2018
    resource: "https://doi.org/10.1007/s10648-018-9434-x"
    title: "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing Self-Explanation: a Meta-Analysis. *Educational Psychology Review, 30*(3), 703–725. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)"
    author: "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H."
    q: 4
    i: 2
    n: 69 effect sizes (64 research reports)
    kind: quant-synthesis
    rigour: "?"
---

# Prompting learners to self-explain, one generative strategy, improves learning by a moderate average amount; other generative activities are not tested by the evidence recorded here

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r?` · `q4` · `i2` medium · n=69 effect sizes (64 research reports)
<!-- deprecated title (2026-10-05, overstated its evidence): Generative processing improves learning -->

Generative processing means learners actively construct connections between new material and their prior knowledge, by summarizing, self-explaining, mapping or generating answers. The one entry recorded, a meta-analysis of 64 reports (Bisra et al. 2018), tests self-explanation prompts only, and finds a moderate average benefit (g = 0.55) over conditions without them; whether summarizing, mapping or generating answers do the same is not shown here. <!-- deprecated (2026-10-05, overstated its evidence): Learners who actively construct connections between new material and their prior knowledge — by summarizing, self-explaining, mapping, or generating answers — learn more than learners who passively receive the same material. --> The claim concerns the *act of generation itself*; comparisons must control for study time, since generative activities typically take longer than passive study.

## Subclaims

`q4 i2` Prompting learners to self-explain — a canonical generative strategy that forces selecting, organizing, and integrating information — produces a moderate learning benefit over passive study or problem-solving without such prompts, across a wide range of instructional conditions. [→ Bisra et al. 2018](#bisra-et-al-2018)

## Evidence

### Bisra et al. 2018

Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing Self-Explanation: a Meta-Analysis. *Educational Psychology Review, 30*(3), 703–725. [doi:10.1007/s10648-018-9434-x](https://doi.org/10.1007/s10648-018-9434-x)

`q4 · meta-analysis (random-effects model)` · `i2 · medium effect, g=0.55` · `n=69 effect sizes (64 research reports)` · `quant-synthesis · r?`

A meta-analysis of studies that induced self-explanation — a generative strategy in which learners produce inferences about causal connections or conceptual relationships in to-be-learned material — while studying text, worked examples, or solving problems, compared with matched conditions without self-explanation prompts. Pooling 69 effect sizes from 64 research reports with a random-effects model, the authors found an overall weighted mean effect of Hedges' *g* = 0.55 favoring self-explanation. The benefit held across 20 coded moderators (task type, subject area, level of education, type of inducement, treatment duration), leading the authors to describe self-explanation prompts as "a potentially powerful intervention across a range of instructional conditions."

## Discussion

**Mechanism.** Generative processing is the productive engagement hypothesized by [cognitive load theory](../theories/cognitive-load-theory.md) and generative models of comprehension: learners select relevant information, organize it into a coherent structure, and integrate it with prior knowledge. Activities that prompt this work — self-explanation, summarizing, concept mapping, drawing, generating examples — are predicted to outperform passive study of identical content because they force construction rather than recognition. This claim is the umbrella under which several more specific claims on this wiki sit: [annotating](annotating-improves-learning.md), [activation](activation-improves-learning.md), and [active learning](active-learning-improves-exam-performance.md) can all be read as particular instantiations of generative processing.

**Moderators and boundary conditions.** The benefit depends on the learner actually generating, not just being given the opportunity to. Learners with low prior knowledge may lack the schema to generate useful connections, so generation can impose extraneous load rather than germane load — a pattern consistent with the [expertise reversal effect](../theories/expertise-reversal-effect.md). Poorly designed generation tasks (e.g., copying, or generating before any input is understood) can also backfire. Quality of the generated product, time on task, and alignment between the generation task and the criterion test all plausibly moderate the effect; these need to be established by evidence before strong design prescriptions follow. A recurring confound in this literature is time on task: generative activities typically take longer than passive study, so comparisons must control for study time to isolate the effect of generation itself.

**Relation to load management.** Generation is not free: it consumes working memory resources. It therefore pairs naturally with [chunking](chunking-reduces-working-memory-load.md) and other load-management measures — the claim is that generative effort pays off only when the material itself does not overwhelm the learner, as captured by [cognitive overload degrades learning](cognitive-overload-degrades-learning.md). Designers should treat generative tasks as an investment of limited capacity, sequenced after basic comprehension of the input rather than instead of it.

**Open questions.** Which generation activities are most efficient per unit of time, how generation interacts with [worked examples](../elements/demonstration.md) and fading, and how effects scale from lab tasks to classroom curricula all remain to be documented on this page. One entry is recorded, a meta-analysis of self-explanation prompts; for other generative activities, this page is a framing claim whose specific instantiations carry their own evidence (summarizing, for instance, did worse than rereading in one multi-document study: [summarization](summarization-improves-learning.md)). <!-- deprecated (2026-10-05, stale): Until evidence entries are added, this page should be treated as a framing claim whose specific instantiations carry their own evidence. -->

*Merged from “Generative Learning Improves Retention” (generative-learning-improves-retention):* **Mechanism.** Generative activities are hypothesized to work by forcing learners to construct relations between new material and prior knowledge, rather than reproducing surface text. This aligns with the broader account in [Cognitive Load Theory](../theories/cognitive-load-theory.md): generation imposes effortful processing that supports schema construction, but only when the extra load is germane rather than extraneous — see [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md).

**Moderators and boundary conditions.** Generation is not uniformly beneficial. Learners need sufficient prior knowledge to generate accurate products; when they lack it, generative tasks can produce errors or flounder, and providing structure (prompts, sentence starters, worked models) becomes necessary. The activity must also actually require transforming meaning — copying, highlighting, or verbatim note-taking look generative but do not produce the same benefit. Task–learner fit matters: the same prompt that helps one learner may be redundant or overwhelming for another, echoing the expertise-reversal pattern documented in the [expertise reversal effect](../theories/expertise-reversal-effect.md).

**Retention versus transfer.** The folded page's claim concerned retention. Generative strategies are often expected to support transfer and inference as well, but the meta-analysis recorded above measured self-explanation, one generative strategy, so the strength of that expectation for other strategies is not established here; retention benefits are typically the better-established outcome in this literature.

**Open questions.** Most of the evidence base compares generation against passive control conditions; fewer studies test which generative activity is best for a given material type, or how benefits persist over delay intervals versus immediate tests. The recorded evidence covers self-explanation only, so confidence in the broader claim about generative strategies should stay moderate.

*Merged from “Generative Learning Improves Comprehension” (generative-learning-improves-comprehension):* **Mechanism.** Generative activities are hypothesized to work by forcing learners to select relevant information, organize it into a coherent structure, and relate it to prior knowledge — the three processes in generative models of comprehension (Fiorella & Mayer's selecting–organizing–integrating framework). This aligns with the broader principle that [active learning](../principles/active-learning.md) outperforms passive reception [+M], and with [activation](../principles/activation.md) of prior knowledge as a precondition for meaningful integration [+M].

**Not all generation is equal.** The benefit depends on the quality of the generative process. Copying text verbatim or underlining involves little transformation and yields little gain [~M], whereas activities that require constructing relations — such as [self-explaining](../elements/articulation.md), concept mapping, or [annotating](../principles/annotating.md) — impose the selection–organization–integration cycle that drives comprehension [+M]. Fiorella and Mayer distinguish "summarizing" and "mapping" (organizing strategies) from "self-explaining" and "teaching" (integrating strategies); both families outperform passive study, but through different process routes.

**Moderators and boundary conditions.** Generation is effortful; learners with limited prior knowledge or high working-memory demands may benefit from more scaffolded generative tasks, consistent with [cognitive load theory](../theories/cognitive-load-theory.md) [~M]. Learners also tend to prefer rereading over generating, even though rereading is less effective — so designers should not treat learner preference as a guide [-W]. The benefit is strongest for measures of comprehension and transfer rather than verbatim recall [+M].

**Open questions.** Which generative strategy is optimal for a given domain, learner profile, and outcome measure remains unsettled; comparative studies often find small differences among well-chosen strategies, suggesting that any activity that reliably triggers the underlying processes captures most of the benefit. Studies still need to be added to the Evidence section before this claim can carry an evidence-strength rating.

## Related Claims

- [Active learning improves exam performance.](active-learning-improves-exam-performance.md) — active engagement in class produces better outcomes than lecture alone
- [Activation improves learning.](activation-improves-learning.md) — activating prior knowledge supports integration of new material
- [Annotating improves learning.](annotating-improves-learning.md) — annotation is a concrete generative activity during reading
- [Chunking reduces working memory load.](chunking-reduces-working-memory-load.md) — managing load is a precondition for productive generative effort
- [Cognitive overload degrades learning.](cognitive-overload-degrades-learning.md) — generation helps only when working memory is not overwhelmed
- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](self-explanation-improves-conceptual-understanding.md) — related
- [Elaborative Encoding Improves Retention](elaborative-encoding-improves-retention.md) — related
- [Students who generate their own research question are apt to be more invested and more engaged](ur-student-generated-question-engagement.md) — related
- [Students with more controlled interaction patterns in iSTART-2 generated higher-quality self-explanations than students with more random patterns](controlled-interaction-patterns-higher-self-explanation-quality.md) — a narrower finding that bears on this claim
- [Learners' beliefs about a medium and its processing demands influence the mental effort they invest in processing it](learner-beliefs-influence-mental-effort-media-processing.md) — related
- [Task-essentialness and productive use of new words in goal-directed activity may positively affect vocabulary learning and retention](task-essentialness-goal-directed-vocabulary-retention.md) — a narrower finding that bears on this claim
- [Answering history explanation questions often requires causal inferences because causal relationships are frequently left implicit in textbooks](causal-links-implicit-in-history-textbooks.md) — related
- [Learner-constructed graphic organizers are not shown to outperform provided ones: the one direct test, with college readers, favoured provided organizers on transfer](learner-constructed-graphic-organizers-outperform-provided.md) — related
- [Knowledge gained by self-analysis is more likely to produce constructive change in teaching than insights given by an observer](self-analysis-knowledge-drives-teacher-change.md) — related
- [Different evidence types differ in how strongly they can support claims about effectiveness](evidence-types-differ-support-strength.md) — related
