# Authoring principles and patterns as observation and design objects

A **principle** states a conditional relationship between a learner's inferred state, an activity under stated conditions, and subsequent observations. A **pattern** expresses a reusable configuration or policy for choosing activities and interpreting responses. A particular lesson, course or study procedure is a **design instance**; its details should not silently become universal pattern requirements.

## Exemplar pairs

- [Worked Examples principle](principles/worked-examples.md) and [pattern](patterns/worked-examples.md): initial support, independent performance and representation changes.
- [Spaced Learning principle](principles/spaced-learning.md) and [pattern](patterns/spaced-learning.md): total spacing, schedule shape and delayed outcome.
- [Formative Assessment principle](principles/formative-assessment.md) and [pattern](patterns/formative-assessment.md): evidence interpretation, contingent action and reobservation.

Ten more pairs follow the same format (2026-10-01): [cooperative learning](principles/cooperative-learning.md) / [pattern](patterns/cooperative-learning.md), [direct instruction](principles/direct-instruction.md) / [pattern](patterns/direct-instruction.md), [mastery learning](principles/mastery-learning.md) / [pattern](patterns/mastery-learning.md), [multimedia learning](principles/multimedia-learning.md) / [pattern](patterns/multimedia-learning.md), [problem-based learning](principles/problem-based-learning.md) / [pattern](patterns/problem-based-learning.md), [self-regulated learning](principles/self-regulated-learning.md) / [pattern](patterns/self-regulated-learning.md), [peer discussion](principles/peer-discussion.md) / [peer instruction](patterns/peer-instruction.md), [scaffolding and fading](principles/scaffolding-and-fading.md) / [cognitive apprenticeship](patterns/cognitive-apprenticeship.md), [cognitive load](principles/cognitive-load-theory.md) / [4C/ID](patterns/4cid-four-component-instructional-design.md), and [retrieval practice](principles/retrieval-practice.md) / [team-based learning](patterns/team-based-learning.md). Conversion wave 1 (2026-10-02, `eval/page-triage/wave-1.md`) converted single pages: the principles [cognitive-load management](principles/cognitive-load-management.md), [annotating](principles/annotating.md), [check-ins](principles/check-ins.md), [chunking](principles/chunking.md), [assessment for learning](principles/assessment-for-learning.md), [active learning](principles/active-learning.md), [clear structure](principles/clear-structure.md), [collaborative learning](principles/collaborative-learning.md), [building empathy](principles/building-empathy.md), [accessible vocabulary and syntax](principles/accessible-vocabulary-syntax.md), [authentic audiences and purposes](principles/authentic-audiences-purposes.md), [activation](principles/activation.md) and [scaffolding](principles/scaffolding.md), and the patterns [case-based learning](patterns/case-based-learning.md) and [think-pair-share](patterns/think-pair-share.md). Each keeps the page's previous body in a `<!-- deprecated -->` block and every claim it cited, in the model or under Further evidence.

These are authoring exemplars with explicit evidence limits. Their proposed diagnostic branches require learner testing; textual completeness does not establish effectiveness.

## Required affordances

| Affordance | What the page helps a reader do |
|---|---|
| Initial state | Elicit a task-specific response under recorded conditions; distinguish observation from inferred state and retain uncertainty. |
| Transition | Use a response and its interpretation to select a conditional next activity, preserving intervention configuration. Label untested branches. |
| Target | Specify capability, representative instrument, locally chosen criterion and horizon, or elicit them when missing. |
| Expectation | Follow a direct claim link to a bounded comparison; state what it does and does not predict. |
| Diagnosis | Separate at least two explanations of the same response using observations that could discriminate them. |
| Significance | Ask what the learner values, distinguish it from the designer objective, and use agreement or divergence in design. |

Each affordance is one of the shared dimensions in [`evidence-dimensions.json`](evidence-dimensions.json), where its controlled values live and where it meets the same dimension's name in a coded evidence cell and in an effect's comparison record: initial state is `learner-state`, target is `goal` and `outcome`, transition is `design-variable`, expectation is `effect` and `assignment`, significance is `valued-goal`, and diagnosis is `diagnosis`. Use those values where a page names a learner's expertise, a knowledge type, a setting or an outcome, so a page, an evidence map and a benchmark check about the same thing say it the same way.

A general page need not provide a universal test score or schedule. It must show how the relevant local information will be established. A useful abstention identifies the missing observation or unsupported comparison and its consequence for the decision.

## Evidence boundaries

For each used claim, preserve provenance and grain, exact treatment and comparator, learner/context characteristics, assignment and baseline comparability, outcome alignment and independence, score-range constraints, assessment horizon, uncertainty and source verification status. Record unknowns. A nonsignificant difference does not establish equivalence. A program-level average does not forecast an individual's response, and an aligned measure can also be closely tied to the intervention.

Keep raw magnitude alongside a justified interpretation rather than ranking unlike studies. Distinguish study-observed effects from mechanism hypotheses, transported implications and proposed local designs.

## Review with two briefs

Use a brief with an observed learner response, context, designer objective and learner goal, and another that withholds the starting response, target details and goal. The first should produce a bounded decision; the second should produce useful elicitation rather than invented specificity. Check the principle and pattern separately and check their reciprocal links. Then ask another reader to apply them to a new brief. Document improvement in decisions, observations collected and unsupported claims avoided; adding headings alone is insufficient.
