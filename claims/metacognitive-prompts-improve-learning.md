---
type: claim
title: Metacognitive prompts improve learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: metacognitive-prompts-improve-learning
evidence_strength:
sources:
  - id: guo-2022
    resource: "https://doi.org/10.1111/jcal.12650"
    title: "Guo, L. (2022). Using metacognitive prompts to enhance self‐regulated learning and learning outcomes: A meta‐analysis of experimental studies in computer‐based learning environments. *Journal of Computer Assisted Learning, 38*(3), 811–832. [doi:10.1111/jcal.12650](https://doi.org/10.1111/jcal.12650)"
    author: Guo, L.
    q: 4
    i: 2
    n: unreported in abstract (full text access-gated; k not stated)
    kind: quant-synthesis
    rigour: "?"
  - id: wong-et-al-2019
    resource: "https://doi.org/10.1080/10447318.2018.1543084"
    title: "Wong, J., Baars, M., Davis, D., Van Der Zee, T., Houben, G.-J., & Paas, F. (2019). Supporting Self-Regulated Learning in Online Learning Environments and MOOCs: A Systematic Review. *International Journal of Human–Computer Interaction, 35*(4–5), 356–373. [doi:10.1080/10447318.2018.1543084](https://doi.org/10.1080/10447318.2018.1543084)"
    author: "Wong, J., Baars, M., Davis, D., Van Der Zee, T., Houben, G.-J., & Paas, F."
    q: 3
    i: "?"
    n: 35 studies
    kind: review
    rigour: 2
---

# Metacognitive prompts improve learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 quant-synthesis `r?`, 1 review `r2` · `q3`–`q4` · `i2` medium

Prompts that direct learners' attention to planning, monitoring, and evaluating their own thinking can improve learning outcomes, particularly when embedded in structured learning tasks.

## Subclaims

`q4 i2` A meta-analysis of experimental studies in computer-based learning environments finds that metacognitive prompts (planning/monitoring/evaluation cues) produce a medium-sized improvement in learning outcomes relative to no-prompt control conditions, and a larger improvement in self-regulated-learning activity itself. [→ Guo 2022](#guo-2022)

`q3 i?` A systematic review of 35 studies of self-regulated-learning support in online learning environments judged prompting (14 studies) an effective way to enhance SRL strategies and learning performance, but reported no pooled effect, found that effectiveness varied with how prompts were implemented and with learners' prior knowledge, and did not examine publication bias. [→ Wong et al. 2019](#wong-et-al-2019)

## Evidence

### Guo 2022

Guo, L. (2022). Using metacognitive prompts to enhance self‐regulated learning and learning outcomes: A meta‐analysis of experimental studies in computer‐based learning environments. *Journal of Computer Assisted Learning, 38*(3), 811–832. [doi:10.1111/jcal.12650](https://doi.org/10.1111/jcal.12650)

`q4 · meta-analysis of experimental studies` · `i2 · medium effect, g=0.40, 95% CI [0.31, 0.49]` · `n=unreported in abstract (full text access-gated; k not stated)` · `quant-synthesis · r?`

A random-effects meta-analysis of experimental studies conducted in computer-based learning environments (CBLEs) tested whether prompting learners to plan, monitor, and evaluate their own thinking during a task improves outcomes relative to unprompted control conditions. Metacognitive prompts significantly raised both self-regulated-learning activity (Hedges' g = 0.50, 95% CI [0.37, 0.63]) and learning outcomes (g = 0.40, 95% CI [0.31, 0.49]) compared to control. Moderator analyses found the effect varied with three features of the prompts themselves: whether they were paired with feedback, how task-specific they were, and whether they adapted to the individual learner — directly supporting this page's "prompt specificity" and "support fading/adaptability" moderator notes in the Discussion section below. The authors frame task-specific, individually adaptive prompting (with feedback) as the design implication for CBLEs.

### Wong et al. 2019

Wong, J., Baars, M., Davis, D., Van Der Zee, T., Houben, G.-J., & Paas, F. (2019). Supporting Self-Regulated Learning in Online Learning Environments and MOOCs: A Systematic Review. *International Journal of Human–Computer Interaction, 35*(4–5), 356–373. [doi:10.1080/10447318.2018.1543084](https://doi.org/10.1080/10447318.2018.1543084)

`q3 · systematic review, narrative synthesis, no pooled estimate` · `i? · no pooled effect size reported` · `n=35 studies` · `review · r2`

A systematic review of 35 studies of approaches to support self-regulated learning in online learning environments (23 of them at undergraduate level; searched April 2016), grouped by approach: 14 on prompts, 10 on integrated support systems, 2 on feedback, 4 on prompts combined with feedback. The prompting studies found more SRL activity (planning, goal specification, monitoring, evaluation) and better transfer, factual and problem-solving performance in several studies, but the authors say effectiveness "cannot be simply defined by one effect size" because prompts differed in form, intention, specificity and timing. In one study reviewed, lower-prior-knowledge learners benefited from prompts only once they had been trained to use them. Read in full (open access, Erasmus University repository).

> "The evidence indicates that prompting is an effective way to enhance SRL and learning performance. However, the results should be interpreted with caution as publication bias was not examined."

## Discussion

**Scope and mechanism.** Metacognitive prompts are typically short questions or cues (e.g., "What is your goal for this step?", "Does this answer make sense?") inserted into a task, worked example, or collaborative activity. They are expected to work by triggering self-regulatory processes that learners would not otherwise initiate spontaneously — see [Self-regulated learning](../theories/self-regulated-learning.md). The claim as stated is deliberately broad: prompts vary widely in content (planning vs. monitoring vs. evaluation), timing, and delivery, and the evidence base has not yet been entered on this page, so no effect direction is currently asserted with a tag. Until evidence entries are added, this page should be treated as a scoped hypothesis with plausible moderators, not a validated claim.

**Likely moderators.** Several boundary conditions are plausible on general grounds and should be tested once evidence entries are added:

- *Expertise.* Novices are the most plausible beneficiaries, because they rarely engage in self-explanation or self-monitoring unprompted; for advanced learners, prompts may be redundant and consume working-memory capacity — consistent with the expertise-reversal pattern described in [Cognitive load theory](../theories/cognitive-load-theory.md) and [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md).
- *Prompt specificity.* Generic prompts ("think about your learning") are less likely to help than task-specific prompts tied to the current step of the task. This parallels the distinction between generic and domain-specific guidance in [Advance organizers improve learning](advance-organizers-improve-learning.md).
- *Timing and load.* Prompts delivered during demanding problem-solving may interrupt productive processing rather than support it; prompts placed at natural pauses (before, between, or after tasks) are less likely to interfere with the load-management concerns captured in [Chunking reduces working memory load](chunking-reduces-working-memory-load.md).
- *Support fading.* Sustained benefits plausibly depend on gradually removing prompts as learners internalize the strategies; permanent prompting risks dependence rather than strategy acquisition — the same fading logic that governs [Worked examples can become redundant or counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md).

**Open questions.** Whether effects persist after prompts are removed (i.e., whether learners internalize the strategies), whether effects transfer beyond the prompted task, and how prompt benefits interact with [Activation](activation-improves-learning.md) of prior knowledge all remain to be established from the evidence base. A further open question is whether prompted reflection must be overt (written or spoken) to be effective, or whether covert cueing suffices — a distinction that matters for designs like [Learner highlighting of text gives a small memory benefit but no reliable comprehension benefit, and evidence on other forms of annotation is not yet recorded here](annotating-improves-learning.md) and [3-2-1 reflection](../strategies/3-2-1_reflection.md).

**Online environments (Wong et al. 2019).** The online-learning review supports the direction of this claim but qualifies it: prompt effects depended on implementation and on learners' prior knowledge, and in the study it describes, lower-prior-knowledge learners needed training before prompts helped them. It pooled no effect, so it adds a second source for the direction, not for the size.

## Related Claims

- [Learner highlighting of text gives a small memory benefit but no reliable comprehension benefit, and evidence on other forms of annotation is not yet recorded here](annotating-improves-learning.md) — annotation is a concrete strategy that externalizes the monitoring processes metacognitive prompts target
- [Activation improves learning](activation-improves-learning.md) — prompts that activate prior knowledge are a closely related cueing mechanism
- [Cognitive overload degrades learning](cognitive-overload-degrades-learning.md) — added prompts can themselves impose load if poorly timed
- [Chunking reduces working memory load](chunking-reduces-working-memory-load.md) — relevant to when prompts fit within available working-memory capacity
- [Self-regulated learning](../theories/self-regulated-learning.md) — the theoretical framework in which metacognitive prompting sits
- [Reflective Practice Improves Outcomes When Structured](reflective-practice-improves-outcomes-when-structured.md) — related
- [Scaffolding improves learning](scaffolding-improves-learning.md) — related
- [Self Monitoring Comprehension Improves Learning](self-monitoring-comprehension-improves-learning.md) — related
- [Students showed deficiencies in maintaining and monitoring their reading plan within the three-element view of metacognition](students-deficient-monitoring-maintaining-plan.md) — related