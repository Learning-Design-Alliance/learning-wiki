---
type: strategy
title: Just In Time Learning
description: Delivering instruction at the moment learners need it to complete a task, rather than in advance of it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Just In Time Learning

> **Strategy** · [All strategies](index.md)

## Description
Just In Time (JIT) learning defers instruction until the point of need: learners attempt a task first, and content, hints, or mini-lessons are delivered when a gap becomes apparent. The approach trades comprehensive front-loaded instruction for on-demand support embedded in the task context, so new information arrives with immediate relevance and an immediate opportunity to apply it.

## Design Implications

JIT delivery exploits the fact that information encountered at the moment of application is better encoded and more likely to transfer than the same information delivered abstractly in advance [Activation of relevant prior knowledge at the point of need improves learning.](../claims/activation-improves-learning.md) [+M]. It also manages cognitive load by withholding material until learners have a schema to attach it to, reducing the burden of holding unused content in working memory [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. However, JIT is not unguided discovery: learners left to search for needed information without structure waste limited working memory resources [Minimal guidance is less effective than guided instruction for novices.](../claims/cognitive-overload-degrades-learning.md) [~S]. Effective JIT systems anticipate need points and deliver support proactively at those moments rather than requiring learners to find it themselves.

### Context
#### Requirements
- A well-structured task or problem that creates authentic need points where specific knowledge becomes necessary
- Modular, small-grain content assets (short explanations, hints, demos) that can be surfaced independently
- A mechanism for detecting need — learner request, error detection, or instructor diagnosis ([Assessment](../elements/assessment.md), [Check-In](../elements/check-in.md))
- Rapid feedback loops so the just-delivered content is applied immediately ([Practice](../elements/practice.md))

#### Constraints
- Pure learner-initiated "pull" models fail for novices, who do not know what they do not know and cannot formulate useful queries [Minimal guidance is less effective than guided instruction for novices.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Fragmenting content into micro-units can prevent learners from building an integrated schema of the whole domain; some advance framing is still needed [Advance organizers improve learning.](../claims/advance-organizers-improve-learning.md) [~M]
- Poorly timed support — delivered after frustration or after the task is complete — loses most of its benefit
- High-stakes or safety-critical skills require systematic coverage in advance; JIT alone leaves dangerous gaps

#### Implementation Variability
- **Just-in-Time Teaching (JiTT)**: learners complete pre-class warm-up questions; the instructor adapts that day's instruction to the misconceptions revealed [Novak et al., 1999]
- **Embedded performance support**: help panels, tooltips, and contextual documentation inside software (e.g., Salesforce in-app guidance, WalkMe)
- **Adaptive sequencing**: platforms like [Khan Academy](https://www.khanacademy.org) and [Duolingo](https://www.duolingo.com) surface review and new content based on error patterns [Adaptive learning improves outcomes.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- **Workshop-on-demand**: instruction scheduled in response to demonstrated need in project-based or workplace settings

### Target Learners
- Adult and workplace learners with immediate performance goals, who are highly motivated by relevance [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+M]
- Intermediate learners who have enough prior knowledge to recognize when they need help
- Novices need more scaffolding and proactive (system-initiated) JIT support rather than open-ended search [Minimal guidance is less effective than guided instruction for novices.](../claims/cognitive-overload-degrades-learning.md) [-S]

### Target Learning Goals
- Procedural and tool-based skills where knowledge is needed at specific task moments
- Troubleshooting, diagnosis, and applied problem solving
- Less suited to foundational conceptual frameworks, which benefit from systematic, sequenced instruction

### Instructions
1. Design or select an authentic task that learners can begin with existing knowledge ([Case Studies](../elements/case-studies.md), [Anchored Instruction](../elements/anchored-instruction.md))
2. Map the task's need points — the moments where specific knowledge or procedures become necessary
3. Prepare modular support assets for each need point: brief explanations, [Demonstrations](../elements/demonstration.md), worked examples, or hints ([Scaffolding](../elements/scaffolding.md))
4. Establish a trigger mechanism — learner request, error detection, or instructor review of warm-up responses ([Assessment](../elements/assessment.md))
5. Deliver support at the need point and require immediate application ([Practice](../elements/practice.md))
6. Provide an advance organizer or overview so learners retain a map of the whole domain even though details arrive on demand [Advance organizers improve learning.](../claims/advance-organizers-improve-learning.md) [+M]
7. Schedule spaced follow-up so just-learned content is revisited and retained [Spaced practice improves retention.](../claims/spaced-practice-improves-retention.md) [+S]

## Related Strategies
- [Scaffolding](../elements/scaffolding.md) — JIT support is scaffolding delivered at need points; both require fading as competence grows
- [Adaptive Learning](../principles/adaptive-learning.md) — automates the diagnosis-and-deliver loop at scale
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — expert hints and coaching during task performance are a JIT mechanism
- [Blended Learning](../patterns/blended-learning.md) — JiTT is a common blended design, with online warm-ups driving face-to-face instruction

## Examples
- **Just-in-Time Teaching (JiTT)** ([https://www.jitt.org](http://www.jitt.org)) — web-based pre-class questions on physics or biology; instructors adjust lecture content to the misconceptions students reveal hours before class [Novak et al., 1999]
- **[Khan Academy](https://www.khanacademy.org)** — hints and step-by-step solution reveals triggered when a learner stalls on an exercise
- **[WalkMe](https://www.walkme.com)** and **[Salesforce In-App Guidance](https://www.salesforce.com)** — contextual walkthroughs surfaced inside enterprise software at the exact workflow step where users typically fail
- **Microsoft Learn** ([https://learn.microsoft.com](https://learn.microsoft.com)) — modular docs and sandboxes structured so developers pull only the content needed for the task at hand

## Key Sources
- Novak, G. M., Patterson, E. T., Gavrin, A. D., & Christian, W. (1999). *Just-in-Time Teaching: Blending Active Learning with Web Instruction*. Prentice Hall.
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)