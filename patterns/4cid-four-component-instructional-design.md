---
type: pattern
status: review
last_edited: 2026-04-07
edited_by: Codex
author: Jeroen J. G. van Merrienboer
grain_size: unit
---

# 4C/ID (Four-Component Instructional Design)

## Description
4C/ID is a design pattern for teaching complex skills by organizing instruction around four coordinated components: whole learning tasks, supportive information, procedural information, and part-task practice. The pattern is designed for skills that require learners to integrate knowledge, strategy, and procedure rather than master isolated facts. Its central move is to keep the whole task visible while still managing difficulty through sequencing, scaffolding, and selective automation of subskills.

The pattern is strongest when learners need transfer to authentic performance. It is not mainly a content-delivery model. It is a design approach for building sequences in which learners perform meaningful tasks, receive just enough support, and gradually work with more variability and complexity over time.

## Implications

### Context
#### Requirements
- **Complex performance goals**: Best used when the target involves coordination of multiple skills in realistic tasks.
- **A sequence of whole tasks**: Tasks should progress from simpler to more complex while preserving meaningful structure.
- **Supportive and procedural information**: Learners need conceptual guidance before or around the task and just-in-time directions during performance.
- **Selective part-task practice**: Routine elements can be isolated when automation is necessary and the whole task would overload absolute novices.
#### Constraints
- **Design intensity**: 4C/ID requires careful sequencing, task-class design, and support planning.
- **Weak fit for simple recall**: It is excessive for instruction focused mainly on memorization or single-step procedures.
- **Scaffolding quality matters**: Poorly timed support can either overload learners or over-support them.
- **Whole-task complexity can swamp novices**: Designers still need to manage intrinsic load deliberately.
#### Grain Size
- Unit
- Course
- Training sequence

### Target Goals
- **Complex skill acquisition**: Building integrated performance rather than detached subskills.
- **Transfer**: Preparing learners for real or realistic practice conditions.
- **Strategic and procedural coordination**: Combining conceptual understanding with fluent execution.

### Target Learners
- **Adult and professional learners**: Strong fit for workforce, technical, medical, and higher education contexts.
- **Learners preparing for authentic performance**: Best when the outcome is application in practice, not only classroom recall.
- **Novices in complex domains**: Particularly useful when complexity must be managed without losing sight of the whole task.

### Theory
#### Supporting
- Cognitive load theory — complex performance should be sequenced so intrinsic load is manageable and extraneous load stays low.
- Whole-task instructional design traditions — authentic coordinated performance supports transfer better than isolated training alone.
- Scaffolding and fading perspectives — supports should be gradually withdrawn as learners gain control.
#### Contradicting / Qualifying
- Not all skills require full 4C/ID treatment; some can be learned more efficiently through simpler explicit instruction sequences.
- Part-task work is a support inside the pattern, not the organizing center.

### Claims
#### Supporting
- [[claims/whole-task-performance-improves-transfer]] [+S]
- [[claims/part-task-practice-reduces-load-for-novices]] [+M]
- [[claims/contingent-scaffolding-improves-learning]] [+M]
#### Contradicting
- [[claims/worked-examples-expertise-reversal]] [~M]

## Design

### Sequence
1. Present a whole task at an entry level learners can attempt.
2. Provide supportive information that helps learners understand the task class and relevant strategies.
3. Deliver procedural information just in time during task performance.
4. Add part-task practice for routine subskills that need automation.
5. Increase task variability and complexity while fading supports.

### Elements Used
- [[elements/whole-task-performance|Whole-task Performance]]
- [[elements/part-task-practice|Part-task Practice]]
- [[elements/problem-presentation|Problem Presentation]]
- [[elements/assessment|Assessment]]

### Affordances
- [[principles/guided-practice|Guided Practice]]
- [[principles/problem-based-learning|Problem-based Learning]]
- [[principles/competency-based-learning-assessment|Competency-Based Learning & Assessment]]
- [[principles/worked-examples|Worked Examples]]

### Personalization
- Task complexity can be adjusted by changing constraints, support, and variability.
- Procedural supports can be faded at different rates for different learners.
- Part-task practice can be targeted only to the subskills a learner has not yet automated.

## Related Patterns
- [[patterns/problem-based-learning-pbl|Problem-Based Learning (PBL)]]
- [[patterns/cognitive-load-reduction-clt-scaffolding-approach|Cognitive Load Reduction (CLT Scaffolding Approach)]]

## Examples
- Clinical training programs that move from simpler to more complex patient cases while fading support.
- Technical workforce training where learners perform increasingly realistic troubleshooting tasks.
- Professional education sequences that combine authentic tasks, coaching, and targeted subskill drills.

## Impact
- Strong fit for complex-skill domains where transfer matters more than short-term task ease.
- Helps preserve authentic performance demands while still protecting novices from overload.

## Key Sources
- van Merrienboer, J. J. G. (1997). *Training complex cognitive skills*. Educational Technology Publications.
- van Merrienboer, J. J. G., Kester, L., & Paas, F. (2006). Teaching complex rather than simple tasks: Balancing intrinsic and germane load to enhance transfer of learning. *Applied Cognitive Psychology, 20*(3), 343-352. [https://doi.org/10.1002/acp.1250](https://doi.org/10.1002/acp.1250)
- van Merrienboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge.
