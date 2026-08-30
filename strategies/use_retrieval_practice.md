---
type: strategy
title: Use Retrieval Practice
description: Learners actively recall information from memory rather than re-reading or re-watching it, strengthening retention and transfer.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Use Retrieval Practice

## Description
Retrieval practice asks learners to pull information out of memory — via free recall, short-answer questions, flashcards, or low-stakes quizzing — instead of passively reviewing material. The act of successful retrieval strengthens the memory trace and makes it more accessible in future contexts, a phenomenon known as the testing effect. It is carried out by replacing or supplementing review activities with recall attempts, typically followed by feedback.

## Design Implications

Retrieval practice produces substantially larger and more durable learning gains than restudying across ages, subjects, and formats [Roediger & Karpicke's classroom experiments showed testing outperformed repeated study on delayed tests.](https://doi.org/10.1111/j.1467-9280.2006.01693.x) [+S]. Its effectiveness depends on retrieval being effortful but successful: learners must genuinely attempt recall, not recognize answers. Feedback after retrieval corrects errors and supports learning of unretrieved material, but retrieval with feedback outperforms feedback alone.

### Context
#### Requirements
- Recall prompts that require learners to generate answers, not merely recognize them (multiple-choice is weaker than free recall but still superior to restudy)
- Feedback or answer-checking so errors are corrected rather than reinforced ([Feedback](../elements/feedback.md))
- Sufficient delay between study and retrieval — immediate recall after reading adds little; spaced retrieval drives the effect
- Low-stakes framing so retrieval functions as learning, not evaluation

#### Constraints
- Retrieval of poorly encoded material fails and can reinforce errors when learners confidently retrieve wrong answers without feedback [-M]
- Repeated retrieval of the same item in one session yields diminishing returns; spacing is what sustains gains [~S]
- High-stakes framing converts retrieval into test anxiety, which can impair recall for anxious learners [~M]
- Very difficult retrieval (failure without prompt) can produce little benefit and frustrate novices [~M]

#### Implementation Variability
- Free recall ("brain dump"), cued recall, short answer, flashcards (e.g., [Anki](https://apps.ankiweb.net)), low-stakes classroom quizzing, or retrieval embedded in application tasks
- Pre-questions before instruction (pretesting effect) as a variant that primes learning even when learners answer incorrectly
- Cumulative quizzing, where each quiz samples from all prior material, combines retrieval with spacing

### Target Learners
- Effective across age ranges, from elementary students to medical residents and adult professionals [+S]
- Learners with some initial encoding of the material; complete novices need an initial study phase before retrieval becomes productive [~M]
- Learners with poor metacognitive calibration benefit especially, because retrieval exposes the gap between perceived and actual knowledge

### Target Learning Goals
- Long-term retention of facts, concepts, and procedures
- Transfer: retrieval practice enhances application to new questions better than restudy [+M]
- Metacognitive accuracy: calibrating judgments of learning to actual knowledge state

### Instructions
1. Present or assign the material to be learned, ensuring initial encoding ([Advance Organizers](../elements/advance-organizers.md) can structure this).
2. After a short delay, pose recall prompts — free recall, short answer, or flashcards — rather than asking learners to reread ([Practice](../elements/practice.md)).
3. Provide feedback promptly, especially for incorrect or omitted answers ([Feedback](../elements/feedback.md)).
4. Space subsequent retrieval attempts across days or weeks, increasing the interval as items are mastered.
5. Keep retrieval low-stakes and cumulative so learners treat errors as information, not failure.

## Related Strategies
- [Use Spaced Practice](use_spaced_practice.md) — spacing multiplies the durability of each retrieval attempt
- [Use Worked Examples](use_worked_examples.md) — an alternative for novices before they are ready for effortful retrieval
- [Interleave Practice Types](interleave_practice_types.md) — interleaving forces retrieval of the correct strategy, not just the answer

## Examples
- **[Retrieval Practice Guide](https://www.retrievalpractice.org)** (Agarwal & Bain) — classroom resources translating testing-effect research into routines like "brain dumps" and "two things" exit tickets.
- **[Anki](https://apps.ankiweb.net)** — spaced-repetition flashcard software implementing expanding retrieval schedules; widely used in medical education.
- **[Khan Academy](https://www.khanacademy.org)** — mastery quizzes after each video force retrieval before learners advance.
- **Roediger & Karpicke (2006)** — students who practiced recalling a passage remembered far more a week later than students who reread it four times, despite rereaders predicting the opposite.

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Roediger, H. L., Putnam, A. L., & Smith, M. A. (2011). Ten benefits of testing and their applications to educational practice. In *Psychology and the Real World* (pp. 178–191). Worth Publishers.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Agarwal, P. K., & Bain, P. M. (2019). *Powerful Teaching: Unleash the Science of Learning*. Jossey-Bass.
- Karpicke, J. D., & Blunt, J. R. (2011). Retrieval practice produces more learning than elaborative studying with concept mapping. *Science, 331*(6018), 772–775. [doi:10.1126/science.1199327](https://doi.org/10.1126/science.1199327)