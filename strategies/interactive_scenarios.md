---
type: strategy
id: interactive_scenarios
title: Interactive Scenarios
description: Simulated environments or branching situations that place learners in realistic decision-making roles mirroring real-world challenges.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
sources:
  - id: sitzmann-2011
    resource: "https://doi.org/10.1111/j.1744-6570.2011.01190.x"
    title: "Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation games. *Personnel Psychology, 64*(2), 489–528"
    author: "Sitzmann, T."
  - id: clark-2016
    resource: "https://doi.org/10.1002/9781119239086"
    title: "Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley"
    author: "Clark, R. C., & Mayer, R. E."
  - id: merrill-2002
    resource: "https://doi.org/10.1007/BF02505024"
    title: "Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development, 50*(3), 43–59"
    author: "Merrill, M. D."
  - id: cook-2011
    resource: "https://doi.org/10.1001/jama.2011.1234"
    title: "Cook, D. A., et al. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988"
    author: "Cook, D. A., et al."
---

# Interactive Scenarios

> **Strategy** · [All strategies](index.md)

## Description
Interactive scenarios place learners inside simulated, realistic situations where they must make decisions and experience the consequences. Branching narratives, simulations, and role-based dilemmas require active choice rather than passive reception, with feedback and consequences delivered in response to learner decisions.

## Design Implications

Interactive scenarios work because they require learners to apply knowledge to authentic problems rather than merely recognize it — the core of Merrill's first principles, where learning is promoted when learners engage in task-centered application [Merrill's first principles of instruction.](https://doi.org/10.1007/BF02505024) [+M]. Meta-analytic evidence shows simulation-based instruction outperforms passive comparison conditions on declarative knowledge, procedural knowledge, and retention, with the largest gains when scenarios are paired with explicit debriefing [Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation games. *Personnel Psychology, 64*(2), 489–528](https://doi.org/10.1111/j.1744-6570.2011.01190.x) [+S]. In health professions education, technology-enhanced simulation is associated with large positive effects on learning outcomes compared with no instruction [Cook, D. A., et al. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988](https://doi.org/10.1001/jama.2011.1234) [+S]. The scenario itself is not sufficient — the debriefing and feedback structure around it carries much of the learning benefit.

### Context
#### Requirements
- Authentic decision points with meaningful, consequential branches — not cosmetic interactivity
- Feedback tied to learner choices, ideally at the task and process level rather than generic praise [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- A debriefing or reflection phase where learners examine why their choices succeeded or failed
- Realistic fidelity in the dimensions that matter for the target decision-making (not necessarily maximal visual realism)

#### Constraints
- High production cost and long development cycles; poorly resourced scenarios often reduce to linear content with decorative clicking
- Excessive entertainment features can depress learning outcomes relative to simpler versions of the same content [Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation games. *Personnel Psychology, 64*(2), 489–528](https://doi.org/10.1111/j.1744-6570.2011.01190.x) [~M]
- Novices can be overwhelmed by full-complexity scenarios; simplifying early scenarios and increasing complexity gradually manages this [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- Without debriefing, learners may encode plausible-but-wrong decision paths as valid experience
- Less efficient for well-structured factual or procedural content where worked examples or direct instruction achieve the outcome at lower cost

#### Implementation Variability
- **Branching narratives** (e.g., Twine, Articulate Storyline, Harvard Business School simulations): text- or media-based decision trees with consequence feedback
- **High-fidelity simulation** (e.g., medical mannequin labs, flight simulators): physical realism for high-stakes procedural skills
- **Role-play and live scenarios**: human-run simulations such as moot courts, crisis negotiation exercises, or standardized patient encounters
- **Case-based interactive scenarios**: [Case Studies](../elements/case-studies.md) with embedded decision points, bridging toward full [Case-Based Learning](../patterns/case-based-learning.md)

### Target Learners
- Intermediate learners who have enough prior knowledge to make meaningful decisions but need to integrate it under realistic conditions [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- Professionals in high-stakes domains (medicine, aviation, emergency response) where errors must be practiced safely [Cook, D. A., et al. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988](https://doi.org/10.1001/jama.2011.1234) [+S]
- Novices benefit only when scenario complexity is reduced or scaffolded; full-complexity scenarios can exceed working memory capacity [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]

### Target Learning Goals
- Decision-making and judgment: choosing among plausible options under uncertainty
- Procedural integration: applying component skills in realistic sequences
- Transfer: bridging classroom knowledge to authentic contexts [Merrill's first principles of instruction.](https://doi.org/10.1007/BF02505024) [+M]
- Consequence understanding: seeing how early choices propagate through a situation

### Instructions
1. Define the target decision(s) the scenario must exercise, and the criteria for good choices.
2. Build a realistic situation with 2–4 consequential decision points; keep early scenarios simpler and add complexity as competence grows ([Scaffolding](../elements/scaffolding.md), [Fading](../elements/fading.md)).
3. Embed feedback in the consequences themselves, supplemented by process-level explanations of *why* a choice worked or failed [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
4. Allow safe failure — let learners experience poor outcomes and recover, which supports engagement and conceptual change [Productive failure improves conceptual learning.](../claims/productive-failure-improves-conceptual-learning.md) [+M].
5. Follow with structured debriefing: compare learner choices against expert reasoning, possibly via a [Think-Aloud](../elements/think-aloud.md) expert walkthrough of the same scenario.
6. Assess transfer with a new scenario or [Application](../elements/application.md) task, not by replaying the trained one.

## Related Strategies
- Case-based discussion — the non-interactive ancestor; scenarios add decision-making to case analysis
- Simulation debriefing protocols (e.g., PEARLS) — the structured reflection that converts scenario experience into learning

## Examples
- **[Harvard Business Publishing Simulations](https://www.harvardbusiness.org/)** — business simulations (e.g., the Change Management simulation) where learners make sequential strategic decisions and see organizational consequences unfold.
- **[Open Learning Initiative (Carnegie Mellon)](https://oli.cmu.edu)** — course units embed interactive scenario exercises with immediate feedback within otherwise expository online courses.
- **Medical simulation centers** — standardized patient encounters and mannequin-based scenarios followed by facilitated debriefing, the best-evidenced large-scale use of the strategy [Cook, D. A., et al. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988](https://doi.org/10.1001/jama.2011.1234) [+S].
- **[Twine](https://twinery.org)** — a low-cost authoring tool widely used for branching-narrative scenarios in humanities and ethics teaching.

## Key Sources
- Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation games. *Personnel Psychology, 64*(2), 489–528. [doi:10.1111/j.1744-6570.2011.01190.x](https://doi.org/10.1111/j.1744-6570.2011.01190.x)
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Barsuk, J. H. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988. [doi:10.1001/jama.2011.1234](https://doi.org/10.1001/jama.2011.1234)
- Merrill, M. D. (2002). First principles of instruction. *Educational Technology Research and Development, 50*(3), 43–59. [doi:10.1007/BF02505024](https://doi.org/10.1007/BF02505024)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)