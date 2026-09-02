---
type: strategy
id: chunking_directions
title: Chunking Directions
description: Breaking down directions into smaller, more manageable sections to support sustained attention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Chunking Directions

> **Strategy** · [All strategies](index.md)

## Description
Chunking directions means delivering multi-step instructions in short, sequenced segments — one step or small cluster at a time — rather than as a single long block. Each chunk is completed (or rehearsed) before the next is presented, keeping the amount of information learners must hold in mind at any moment within working memory limits.

## Design Implications

Working memory can hold only a few elements at once, and lengthy instruction strings routinely exceed that capacity, especially for novices and learners with attentional difficulties [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. Sequencing directions so that each chunk is used immediately converts storage demands into just-in-time processing, freeing capacity for the task itself. Chunking works best when each segment is a meaningful unit — a coherent action or sub-goal — not an arbitrary fragment [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M].

### Context
#### Requirements
- A task analysis identifying the natural sub-steps and their dependencies
- Clear stopping points or checkpoints where learners act on the chunk before receiving the next
- Concise, parallel phrasing within each chunk ([Accessible Vocabulary & Syntax](../principles/accessible-vocabulary-syntax.md)); numbered steps or visual icons help learners track position in the sequence
- A way for learners to re-access a chunk (posted card, slide, LMS step) without asking, since re-reading is common

#### Constraints
- Fragmenting directions into steps that are not meaningful units adds switching overhead and can *increase* load rather than reduce it [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M]
- Learners who need to see the whole task structure to plan or monitor their work may be disoriented by step-by-step delivery; providing an advance overview of the full sequence mitigates this
- Over-chunking can produce dependence on external prompts, undermining learners' ability to internalize procedures for independent performance
- Does not address underlying attention or working-memory limitations; it manages them during instruction but does not build capacity

#### Implementation Variability
- **Whole-then-parts:** show the complete direction set once as an overview, then re-present each chunk at the point of use — supports planning while managing load
- **Learner-paced chunks:** post all chunks and let learners reveal or advance through them at their own rate (e.g., step-by-step LMS modules, task cards)
- **Faded chunking:** begin with one chunk at a time, then deliver progressively larger clusters as learners internalize routines, transferring memory demands back to the learner
- **Peer-mediated chunks:** pairs read a chunk, restate it in their own words, then execute — adding [Self-Explanation](../claims/self-explanation-improves-conceptual-understanding.md) [+M] benefit

### Target Learners
- Novices, who lack schemas for compressing multi-step procedures into fewer memory elements [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- Learners with attention difficulties or limited working memory, for whom long instruction strings reliably exceed capacity
- Young learners and second-language learners processing unfamiliar vocabulary alongside task demands
- Less necessary for experts, who chunk automatically and may find step-by-step delivery slow and patronizing [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural fluency: accurately executing multi-step routines (lab protocols, software workflows, craft processes)
- Executive-function support: completing tasks that exceed current self-management capacity
- Reduced error rates on tasks where a missed step invalidates the outcome

### Instructions
1. Analyze the task and identify meaningful sub-steps; group steps into chunks of roughly 1–3 actions aligned to natural sub-goals ([Cognitive Load Management](../principles/cognitive-load-management.md)).
2. Open with a brief overview of the whole task so learners know where they are heading ([Advance Organizers](../elements/advance-organizers.md)).
3. Present the first chunk in clear, numbered language; check that learners can restate it before they begin ([Practice](../elements/practice.md)).
4. Provide a visible stopping point and a way to re-access the current chunk.
5. Deliver the next chunk only at the point of need; fade chunk size as learners demonstrate they can hold and sequence steps independently.

## Related Strategies
- [Task Analysis](../strategies/task-analysis.md) — the prerequisite for identifying meaningful chunks
- [Modeling Multi-Step Processes](../strategies/modeling-multi-step-processes.md) — demonstrating the chunked sequence before learners attempt it

## Examples
- **Elementary classroom routines:** a teacher gives a three-part art task as "First, fold your paper in half and wait" — then releases each subsequent step only when all students reach the checkpoint.
- **Lab instruction:** chemistry curricula such as [ChemCollective](https://chemcollective.org) present virtual lab procedures step-by-step, with each step's instructions visible only for the current stage.
- **Software onboarding:** tools like [Notion](https://www.notion.so) and Duolingo deliver setup or lesson flows one screen at a time, with a progress indicator showing position in the sequence.

## Key Sources
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [doi:10.1037/h0043158](https://doi.org/10.1037/h0043158)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Gagné, R. M., Briggs, L. J., & Wager, W. W. (1992). *Principles of Instructional Design* (4th ed.). Harcourt Brace Jovanovich.

