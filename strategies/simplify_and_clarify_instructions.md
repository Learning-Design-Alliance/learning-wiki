---
type: strategy
title: Simplify and Clarify Instructions
description: Ensure formulations are short, easy to understand, and precise.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simplify and Clarify Instructions

## Description
Simplify and clarify instructions means writing or speaking task directions in short, syntactically simple, and unambiguous language so that working memory is spent on the task, not on decoding the directions. It involves one action per sentence, concrete verbs, explicit sequencing, and removal of idioms, hedging, and embedded clauses that do not carry instructional meaning.

## Design Implications

Instructional language competes with task content for limited working memory; convoluted directions impose extraneous load that degrades performance and completion [Extraneous cognitive load degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]. Simplified, well-structured directions are especially important at task boundaries — the moment learners must act independently — because confusion there produces off-task behavior, repeated help-seeking, or abandonment [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Clarity is not the same as brevity alone: instructions must remain *complete* — every step, criterion, and resource the learner needs — while omitting everything else.

### Context
#### Requirements
- A precise analysis of what the learner must actually do, so simplification does not delete necessary steps
- Consistent task verbs (e.g., always "click," never sometimes "select"/"hit"/"tap" for the same action)
- Sequenced, numbered steps when a task has more than two actions, one action per step ([Chunking](../principles/chunking.md))
- Plain-language vocabulary matched to learner proficiency ([Accessible Vocabulary & Syntax](../principles/accessible-vocabulary-syntax.md))

#### Constraints
- Over-simplification can omit qualifying details (conditions, exceptions, criteria), producing technically compliant but wrong work [-M]
- Simplified instructions do not compensate for a poorly designed or ambiguous task itself; unclear goals remain unclear however plainly stated [-M]
- For advanced learners, very granular step-by-step directions can be redundant and even irritating, reducing engagement [Guidance that helps novices can hinder more expert learners.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Written vs. spoken:** spoken instructions need shorter sentences and more repetition because they cannot be re-read
- **Multimedia:** pair simplified text with visuals or a worked demonstration rather than text alone [Multimedia messages that combine words and pictures improve learning.](../claims/multimedia-principle.md) [+S]
- **Layered instructions:** a one-line summary first, expandable detail beneath — supports both quick orientation and careful re-reading
- **Translated/simplified English:** for multilingual learners, controlled vocabulary and glossed terms rather than simplified content

### Target Learners
- Novices who lack the domain schemas to infer unstated steps from terse directions [Extraneous cognitive load degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+S]
- Multilingual learners and learners with language-processing or attention-related disabilities, for whom instruction clarity is an equity issue ([Accommodations](../elements/accommodations.md))
- Young learners whose working memory and reading capacity are still developing [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- Less granular phrasing suits experts, who find step-by-step direction redundant [Guidance that helps novices can hinder more expert learners.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural execution: correctly carrying out multi-step tasks, lab procedures, software workflows
- Independent task initiation: reducing help-seeking and off-task time at transitions
- Assessment validity: ensuring task responses measure the target skill rather than comprehension of the prompt

### Instructions
1. Draft the instruction, then audit it: one action per sentence, active voice, concrete verbs, no idioms or embedded clauses.
2. Break multi-step tasks into numbered chunks of at most 3–5 steps ([Chunking](../principles/chunking.md)).
3. State the goal and success criteria before the steps, so learners know what "done" looks like ([Clear Structure](../principles/clear-structure.md)).
4. Pair the text with a visual or a brief model of the finished task or process ([Advance Organizers](../elements/advance-organizers.md)).
5. Pilot the instructions with a learner and revise wherever they ask "what do I do here?" — confusion points are instruction defects, not learner defects.

## Related Strategies
- [Accessible Syntax](accessible_syntax.md) — the sentence-level craft underlying clear instructions
- [Activate Background Knowledge](activating_prior_knowledge.md) — pre-teaching vocabulary and context so instructions can stay lean
- [Modeling](../patterns/direct-instruction.md) — showing the task can substitute for some verbal instruction entirely

## Examples
- Instead of "Please retrieve your textbooks and turn to page 57," say "Get your books. Open to page 57."
- **Khan Academy** (https://www.khanacademy.org) — exercise prompts use short, consistent imperative sentences with a single visible action button, minimizing direction-decoding load.
- **Edmodo/Google Classroom assignment templates** — effective teachers post assignments as a numbered checklist ("1. Read… 2. Write… 3. Submit…") rather than a paragraph, so each step is independently checkable.
- **Plain language guidelines** (https://www.plainlanguage.gov) — U.S. federal standard for short sentences, common words, and reader-tested instructions, applicable directly to task directions.

## Key Sources
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction, 4*(4), 295–312. [doi:10.1016/0959-4752(94)90003-5](https://doi.org/10.1016/0959-4752(94)90003-5)