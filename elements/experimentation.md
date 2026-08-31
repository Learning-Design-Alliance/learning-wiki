---
type: element
title: Experimentation
description: Learners form predictions, manipulate variables, and test hypotheses against observed outcomes rather than receiving conclusions directly.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Experimentation

## Description
Experimentation asks learners to pose a question or prediction, systematically vary conditions, observe outcomes, and revise their understanding based on evidence. It functions as both a learning activity and a model of scientific reasoning: the learner generates a hypothesis, gathers data, and confronts discrepancies between expectation and result.

## Design Implications

Experimentation supports learning by making learners active generators and testers of ideas rather than passive recipients [Active learning improves exam performance relative to lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. Its effectiveness depends heavily on structure: unguided "discovery" tends to overload working memory and leave misconceptions intact, whereas experimentation with prompts, predictions, and feedback produces robust gains [Unguided discovery is less effective than guided instruction.](../claims/unguided-discovery-less-effective-than-guided-instruction.md) [-S]. Requiring explicit predictions before observing outcomes is the highest-leverage design move — prediction creates a commitment that evidence can confirm or violate, and violated expectations drive conceptual change [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M].

### Context
#### Requirements
- A manipulable system or dataset where variables can be isolated and outcomes observed (simulation, lab, dataset, or worked domain)
- A prompt for explicit prediction or hypothesis *before* the outcome is revealed
- Timely, interpretable feedback linking the outcome back to the hypothesis
- Scaffolds for the reasoning cycle itself: question → predict → test → interpret → revise ([Articulation](articulation.md) prompts or structured lab reports)

#### Constraints
- Unguided experimentation with minimal scaffolding produces poor outcomes for novices, who tend to run unsystematic trials and confirm prior beliefs [Unguided discovery is less effective than guided instruction.](../claims/unguided-discovery-less-effective-than-guided-instruction.md) [-S]
- Learners often exhibit confirmation bias — testing cases they expect to succeed rather than disconfirming ones — unless prompted to consider alternative hypotheses [~M]
- In domains with high element interactivity, the overhead of managing the experiment itself can crowd out the target learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Slow feedback loops (multi-day labs) weaken the prediction–outcome link; simulations with immediate feedback preserve it

### Target Learners
- Learners with some prior knowledge who can generate a plausible first hypothesis; pure novices need a model or worked case first
- Learners holding misconceptions — the prediction–violation cycle is one of the most reliable ways to surface and confront them [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]
- Less effective as a first exposure for complete novices, who lack the knowledge to interpret outcomes meaningfully

### Target Learning Goals
- Conceptual change: replacing intuitive but incorrect models with evidence-consistent ones
- Scientific inquiry skills: variable control, hypothesis generation, evidence evaluation
- Transfer: reasoning from principles rather than recalling procedures [Analogical reasoning improves transfer when learners compare cases.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]

### Affordances
- [Active Learning](../principles/active-learning.md) — experimentation enacts this principle by requiring learners to generate and commit to ideas rather than receive them, producing the retrieval and decision-making that strengthen encoding
- [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md) — a failed prediction creates exactly the expectation–evidence conflict that motivates schema revision
- [Autonomy](../principles/autonomy.md) — letting learners choose what to vary and investigate supports intrinsic motivation, provided the choice space is bounded [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+M]
- [Cognitive Load Management](../principles/cognitive-load-management.md) — well-designed simulations and structured lab templates offload procedural overhead so working memory is spent on the hypothesis–evidence relationship

## Related Elements
- [Application](application-of-knowledge.md) — experimentation is application with a hypothesis-testing structure layered on top
- [Articulation](articulation.md) — learners must state predictions and interpretations for the cycle to produce conceptual change
- [Assessment](assessment.md) — experimental artifacts (lab reports, revised hypotheses) provide authentic evidence of reasoning
- [Case Studies](case-studies.md) — published cases can serve as "experiments others ran," useful when live manipulation is impractical
- [Analogies](analogies.md) — comparing multiple experimental outcomes supports abstraction of the underlying principle

## Patterns That Use This Element
- [5E Learning Cycle](../patterns/5e-learning-cycle.md) — the "Explore" and "Explain" phases center on structured experimentation before formal explanation
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — the exploration phase, where learners test strategies in the target domain
- [Collaborative Inquiry](../patterns/collaborative-inquiry.md) — groups jointly pose and test questions, distributing the reasoning load

## Examples

**[PhET Interactive Simulations](https://phet.colorado.edu)** — University of Colorado physics/chemistry simulations designed around variable manipulation and immediate feedback; research-validated for conceptual gains when paired with prediction prompts.

**[Concord Consortium](https://concord.org)** — Technology-enhanced science curricula (e.g., *SmartGraphs*, *Molecular Workbench*) embedding prediction-then-test cycles with embedded assessment.

**[WISE (Web-Based Inquiry Science Environment)](https://wise.berkeley.edu)** — Scaffolds the full inquiry cycle — prediction, data collection, reflection — with embedded notes and stepwise guidance.

**[BSCS 5E instructional model](https://bscs.org/bscs-5e-instructional-model)** — Published curriculum framework sequencing engagement, exploration, explanation, elaboration, and evaluation; the exploration phase is structured experimentation.

## Key Sources
- Klahr, D., & Dunbar, K. (1988). Dual space search during scientific reasoning. *Cognitive Science, 12*(1), 1–48. [doi:10.1207/s15516709cog1201_1](https://doi.org/10.1207/s15516709cog1201_1)
- Alfieri, L., Brooks, P. J., Aldrich, N. J., & Tenenbaum, H. R. (2011). Does discovery-based instruction enhance learning? A meta-analysis of the evidence. *Journal of Educational Psychology, 103*(1), 1–18. [doi:10.1037/a0021017](https://doi.org/10.1037/a0021017)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Hmelo-Silver, C. E., Duncan, R. G., & Chinn, C. A. (2007). Scaffolding and achievement in problem-based and inquiry learning: A response to Kirschner, Sweller, and Clark (2006). *Educational Psychologist, 42*(2), 99–107. [doi:10.1080/00461520701263368](https://doi.org/10.1080/00461520701263368)
- Kuhn, D. (2007). Is direct instruction an answer to the right question? *Educational Psychologist, 42*(2), 109–113. [doi:10.1080/00461520701263376](https://doi.org/10.1080/00461520701263376)