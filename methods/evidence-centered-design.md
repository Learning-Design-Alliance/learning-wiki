---
type: method
id: evidence-centered-design
title: Evidence-Centered Design
description: A design method for assessment that works backwards from the claim you want to make — name the competency, then the observable behaviour that would be evidence for it, then the task that elicits that behaviour.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-03
sources:
  - id: mislevy-2003
    resource: "https://doi.org/10.1207/s15366359mea0101_02"
    title: "Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003). Focus article: On the structure of educational assessments. Measurement: Interdisciplinary Research and Perspectives, 1(1), 3-62."
    author: "Mislevy, R. J., Steinberg, L. S., & Almond, R. G."
  - id: plass-et-al-2011
    resource: "https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning"
    title: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). Learning mechanics and assessment mechanics for games for learning (G4LI White Paper #01/2011, v0.1). Games for Learning Institute."
    author: "Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K."
---

# Evidence-Centered Design

> **Design Method** · [All design methods](index.md)

## Description
Most assessments are built forwards: someone writes tasks that feel like the subject, learners do them, and the scores are then interpreted as evidence of something. Evidence-centered design (ECD) inverts that order. It is a formal method for assessment design that begins with the claim you intend to make about a learner and works back to the task that would license it, so that the interpretation is designed in rather than argued for afterwards.

Mislevy, Steinberg and Almond (2003) frame it as three questions, each answered by a model:

- **What should be assessed?** — the **student model** (also called the competency model): the constructs of interest, described as changes in skills, knowledge, identity, values and epistemology.
- **What learner behaviours would reveal those constructs?** — the **evidence model**: the salient features of learner behaviour, plus the rules for scoring those features and for interpreting the scores.
- **What tasks and activities would elicit those behaviours?** — the **task model**: the description of what the learner will actually be asked to do.

The order is the method. A task model written without an evidence model produces activities nobody can score defensibly; an evidence model without a student model scores behaviour that stands for nothing in particular.

ECD earns its formality in settings where the assessment is not a test — simulations, portfolios, [epistemic games](../patterns/epistemic-games.md), and instrumented learning environments generally. This wiki's [Assessment Mechanic](../elements/assessment-mechanic.md) is one such case, and the G4LI account of it is where this page's framing comes from: Plass and colleagues take ECD as the first criterion an assessment mechanic must satisfy, deriving from it both the requirement that a task make the learner's steps explicit and the requirement that the statistical model represent the dependencies between in-game items, since items encountered in sequence in one environment cannot be assumed independent (Rupp, Gushta, Mislevy, & Shaffer, 2010).

## Design Implications

### Context
#### Requirements
- **A competency worth naming.** ECD's cost is only repaid when the student model says something more specific than "understands the unit"; a vague construct produces an evidence model that cannot discriminate.
- **Behaviour that can actually be observed.** The evidence model is a bridge between a construct and a record, and it fails at the record end as easily as at the construct end. In an instrumented environment this becomes a hard constraint on task design: the task has to be capturable by the instrumentation.
- **Measurement expertise, or access to it.** The evidence model is a psychometric artefact — scoring rules, and a statistical model that represents dependencies between tasks. The source is explicit that these test-theoretical concerns are part of the method, not a downstream concern.
- **Iteration between the models.** The task model is constrained by what the evidence model can score, and the evidence model by what the student model claims; a first pass at any one of them usually revises the others.

#### Constraints
- **Heavy for small stakes.** A quiz at the end of a lesson does not need three models. ECD is for assessments whose interpretations will be relied on — placement, certification, adaptive systems, research.
- **The student model can encode a contestable theory of the domain.** Naming what counts as competence is a substantive claim about the subject, and ECD makes it explicit rather than making it correct. Making it explicit is the benefit; it does not settle the argument.
- **Confounds are the standing failure mode.** A task can elicit the target behaviour *and* several others — see the confounds catalogued on [Assessment Mechanic](../elements/assessment-mechanic.md), where load, differential scaffolding, motor demands, unrelated content knowledge and emotion each turn score variation into something other than the construct.
- **Logs are not evidence on their own.** An instrumented environment produces an enormous record of behaviour, and without an evidence model saying which features are salient and how they score, that record is data waiting for a story.

#### Implementation Variability
- **In conventional assessment** — the three models sit behind item specifications and a scoring rubric, and the method mostly disciplines an existing practice.
- **In simulations and games** — the task model becomes an [Assessment Mechanic](../elements/assessment-mechanic.md), and the evidence model has to work over event logs rather than responses. Rupp et al. (2010) develop this case for epistemic games specifically.
- **Extended with observation** — the G4LI summary notes that supplementing log data of game events and user behaviour with observational data extends the ECD model and yields more valid assessments, particularly of state and trait variables.
- **Embedded vs. stealth** — whether the learner is aware the task is assessing them is a design choice made at the task-model level, and the two variants have different validity risks.

### Target Learners
- Designers building an assessment whose interpretation will carry weight, rather than a check for understanding
- Designers instrumenting a simulation, game or learning environment, where the volume of available behaviour makes "what counts as evidence" the binding question
- Teams where measurement and design expertise sit with different people, and the three models are the interface between them

### Target Learning Goals
- Constructs that are not directly observable — reasoning, strategy, self-regulation, professional judgement
- Process as well as outcome: ECD's evidence model is where "how the learner got there" becomes scoreable
- Diagnostic distinctions: designing a task so that a failure attributable to two different causes cannot look identical in the record

### Instructions
1. **Write the student/competency model.** Name the constructs — skills, knowledge, identity, values, epistemology — at a grain size that a decision would actually turn on. If two levels of the construct would lead to the same action, they do not need separating.
2. **Write the evidence model.** For each construct, state the salient features of learner behaviour that would count as evidence, the rules for scoring those features, and how the scores are to be interpreted. This is the step most assessment design skips.
3. **Choose the statistical model.** Decide how the scored features combine, and represent the dependencies between them explicitly — assessments delivered inside one environment routinely violate the independence assumption a naive model would make.
4. **Write the task model.** Describe the tasks and activities that will elicit the behaviour the evidence model needs. Require the learner to make their steps explicit rather than only to produce answers, and allow repeated exposure to similar problems so the behaviour is observed more than once.
5. **Audit the task for confounds.** For each task, ask what *else* could produce a low score: unrelated knowledge, motor demand, exploration luck, processing speed, emotional response. Each one found is either designed out or added to the model as a variable.
6. **Check the task is instrumentable.** Confirm the behaviour the evidence model needs is actually captured by whatever will record it, before the task is built rather than after.
7. **Iterate.** Take what the task model forced you to change back to the evidence and student models, and repeat until the three describe one assessment.

## Related Methods
- [Cognitive Task Analysis](cognitive-task-analysis.md) — a way to populate the student model for judgement-heavy domains, where what competence consists of is exactly what the expert cannot articulate
- [Backward Design](backward-design.md) — the same working-backwards logic applied to a whole unit; ECD is the assessment-shaped case, and the two compose naturally
- [Task Analysis](task-analysis.md) — decomposition that feeds the task model
- [Standards Crosswalk](standards-crosswalk.md) — where the constructs in a student model have to answer to an external framework

## Examples
- [Assessment Mechanic](../elements/assessment-mechanic.md) — ECD's task model, realised as a repeated in-game activity
- [Epistemic Games](../patterns/epistemic-games.md) — the pattern Rupp, Gushta, Mislevy and Shaffer (2010) developed ECD's game-based form against
- [Formative Assessment](../elements/formative-assessment.md) — where an evidence model is usually implicit, and where making it explicit is the cheapest available improvement
- [Performance-based Assessment](../elements/performance-based-assessment.md) — assessment through doing, which is where the gap between "the learner did well" and "the learner knows X" is widest

## Key Sources
- Mislevy, R. J., Steinberg, L. S., & Almond, R. G. (2003). Focus article: On the structure of educational assessments. *Measurement: Interdisciplinary Research and Perspectives, 1*(1), 3–62. [doi:10.1207/s15366359mea0101_02](https://doi.org/10.1207/s15366359mea0101_02)
- Rupp, A. A., Gushta, M., Mislevy, R. J., & Shaffer, D. W. (2010). Evidence-centered design of epistemic games: Measurement principles for complex learning environments. *Journal of Technology, Learning, and Assessment, 8*(4).
- Plass, J. L., Homer, B. D., Kinzer, C., Frye, J., & Perlin, K. (2011). *Learning mechanics and assessment mechanics for games for learning* (G4LI White Paper #01/2011, Version 0.1). Games for Learning Institute. [researchgate.net/publication/272815253](https://www.researchgate.net/publication/272815253_Learning_Mechanics_and_Assessment_Mechanics_for_Games_for_Learning)
- Shute, V. J. (2010). *Innovative assessment for the 21st century: Supporting educational needs*. Springer.

<!-- Provenance, and the reason this page is status: draft rather than review. The account
     of ECD's three models here follows Plass et al. (2011)'s summary of Mislevy, Steinberg
     & Almond (2003) — the wording of the three questions, the "skills, knowledge, identity,
     values and epistemology" phrasing (which Plass et al. take from Rupp et al., 2010), and
     the dependency point are all as that white paper states them. The Mislevy primary is
     cited and its DOI was resolved against Crossref on 2026-09-03 (verified via
     scripts/resolve_doi_conflicts.classify_doi, registry title form retained), but it has
     NOT been read for this page. A reader with the 60-page focus article in hand should
     expect to correct and considerably deepen the three-model description; nothing here was
     inferred beyond what the secondary source states. Rupp et al. is in the Journal of
     Technology, Learning, and Assessment, which Crossref does not index; per CLAUDE.md that
     absence is not evidence of fabrication and no DOI was invented for it. -->
