---
type: strategy
id: maze-cloze-assessments
title: Maze Cloze Assessments
description: A maze cloze assessment replaces every nth word of a passage with three choices, measuring sentence-level comprehension quickly and objectively.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Maze Cloze Assessments

> **Strategy** · [All strategies](index.md)

## Description
A maze cloze assessment presents a passage in which every 5th–7th word is replaced by a set of three choices — one correct, one semantically plausible distractor, one unrelated distractor. Students circle or click the word that best completes each sentence. Unlike traditional cloze (which requires free recall of the deleted word), the maze format is objectively scorable and yields a rapid estimate of reading comprehension and monitoring.

## Design Implications

Maze tasks convert comprehension into a series of local sentence-level decisions, making them fast to administer and machine-scorable while still requiring integration of syntax and meaning [~M]. Because distractors can be engineered to be grammatically correct but semantically wrong, the format can isolate whether students are reading for meaning rather than relying on surface cues [~M]. Performance is sensitive to comprehension monitoring: students who reread and check fit reject the plausible-but-wrong distractor more often [~M].

### Context
#### Requirements
- A passage at an appropriate readability level, with deletions at fixed intervals (typically every 5th–7th word)
- Three options per deletion: correct answer, semantic distractor, unrelated distractor
- A scoring convention (raw correct, or correct minus incorrect to discourage guessing)
- Passages long enough to yield reliable scores (typically 3 minutes of reading or more)

#### Constraints
- Measures local, sentence-level comprehension far more than global inference or text-structure understanding [~M] — a student can score well while missing the passage's main idea
- Fixed-interval deletion can remove words that carry disproportionate meaning load, distorting difficulty [~W]
- Guessing inflates scores substantially relative to open cloze; three options give a 33% chance floor [~M]
- Poorly constructed distractors (too obviously wrong) reduce the task to vocabulary matching rather than comprehension [~M]
- Less informative for students with decoding difficulties, where word recognition, not comprehension, drives performance [~M]

#### Implementation Variability
- **Progressive maze** (as in PEA/PALS): difficulty increases across passages, allowing the same instrument to track growth across a wide ability range
- **Curriculum-based maze**: passages drawn from actual course texts, aligning the measure with instruction
- **Digital adaptive mazes**: item difficulty adjusts to responses in real time
- **Distractor type manipulation**: using only semantic distractors turns the task into a purer measure of meaning-making; using grammatical distractors adds syntactic sensitivity

### Target Learners
- Elementary and middle-grade readers, where maze is a validated screening tool for comprehension risk [~M]
- English learners, with caution — distractor performance can reflect vocabulary knowledge rather than comprehension [~M]
- Less appropriate as a diagnostic for advanced readers, where ceiling effects compress scores [~M]

### Target Learning Goals
- Screening and progress monitoring of reading comprehension
- Formative diagnosis of comprehension monitoring (do students check that words fit the meaning?)
- Not suitable for assessing higher-order goals such as inference, critique, or synthesis

### Instructions
1. Select or write a passage at the target readability level; verify no deleted word is unguessable from local context alone.
2. Replace every nth word (typically 5th–7th) with three choices; construct the semantic distractor first, then the unrelated distractor.
3. Pilot the items and discard any where the distractor is chosen almost as often as the key (poor discrimination) or almost never (obvious distractor).
4. Administer with a time limit (commonly 2–3 minutes) and score correct minus incorrect to penalize guessing.
5. Pair results with a richer measure — e.g., [Retrieval Practice](retrieval-practice.md)-style recall prompts or retelling — before drawing instructional conclusions, since maze scores underrepresent global comprehension [~M].

## Related Strategies
- [Cloze Procedure](cloze-procedure.md) — the open-ended parent format; harder to score, more demanding of production
- [Curriculum-Based Measurement](curriculum-based-measurement.md) — the broader family of brief, repeatable progress measures into which maze fits
- [Formative Assessment](formative-assessment.md) — the instructional stance maze data should serve

## Examples
- **PEA Maze (Progressive Achievement Assessment)** — used in the PALS reading intervention research (Fuchs et al.), a maze with increasing difficulty levels administered every two weeks to monitor comprehension growth.
- **DIBELS 8th Edition Maze** (https://dibels.uoregon.edu) — a benchmark screening maze for grades 2–8 with national norms.
- **FastBridge earlyReading/CBMreading maze tasks** (https://www.fastbridge.org) — digital maze screening integrated with adaptive reporting.

## Key Sources
- Guthrie, J. T., Seifert, M., Burnham, N. A., & Caplan, R. I. (1974). The maze technique to assess, monitor reading comprehension. *The Reading Teacher, 28*(2), 161–168.
- Fuchs, D., Fuchs, L. S., Mathes, P. G., & Simmons, D. C. (1997). Peer-assisted learning strategies: Making classrooms more responsive to diversity. *American Educational Research Journal, 34*(1), 174–206. [doi:10.3102/00028312034001174](https://doi.org/10.3102/00028312034001174)
- Fuchs, L. S., & Fuchs, D. (2004). Determining adequate yearly progress from kindergarten through grade 6 with curriculum-based measurement. *Assessment for Effective Intervention, 29*(4), 25–37. [doi:10.1177/073724770402900405](https://doi.org/10.1177/073724770402900405)
- O'Connor, R. E., Bell, K. M., Harty, K. R., Larkin, L. K., Sackor, S. M., & Zigmond, N. (2002). Teaching reading to poor readers in the intermediate grades: A comparison of text difficulty. *Journal of Educational Psychology, 94*(3), 474–485. [doi:10.1037/0022-0663.94.3.474](https://doi.org/10.1037/0022-0663.94.3.474)