---
type: strategy
id: word-prediction-software
title: Word Prediction Software
description: Software that suggests words as a learner types, reducing spelling and transcription demands so composing effort can go to ideas and structure.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Word Prediction Software

> **Strategy** · [All strategies](index.md)

## Description
Word prediction software displays a list of likely next words as a learner types, typically triggered by the first one or two letters. The learner selects a predicted word rather than typing it in full, which reduces spelling demands, keystrokes, and the working-memory burden of holding a word in mind while transcribing it. Most modern tools combine prediction with text-to-speech feedback, custom dictionaries, and topic-specific vocabulary.

## Design Implications

Word prediction functions as an [accommodation](../elements/accommodations.md) that offloads low-level transcription so working memory is available for planning and composing [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Because transcription fluency is a bottleneck for struggling writers, freeing it can improve both writing volume and quality [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+M]. The trade-off is that scanning and evaluating prediction lists imposes its own cognitive load; poorly tuned prediction can interrupt the flow of composition [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M].

### Context
#### Requirements
- A prediction engine tuned to the learner's vocabulary and topic (custom dictionaries, topic word lists)
- Prediction lists short enough to scan quickly (typically 3–6 items) with keyboard or single-switch selection
- Text-to-speech readback so learners can verify that the selected word is the intended one
- Explicit instruction in how to use the tool — learners who ignore predictions gain little

#### Constraints
- Prediction interrupts composition for fluent spellers and fast typists; for them it slows writing rather than helping [-M]
- Learners must be able to recognize the correct word in the list; prediction does not help if the target word is not already in the learner's receptive vocabulary [-M]
- Heavy reliance on prediction without spelling instruction can leave underlying encoding skills underdeveloped [~W]
- Poorly matched prediction (wrong frequency, wrong topic) adds scanning and decision costs that exceed the keystrokes saved [~M]

#### Implementation Variability
- Phonetic prediction: suggests words matching the learner's invented spellings (e.g., typing "fone" surfaces "phone")
- Topic-specific dictionaries loaded per assignment to raise hit rates in content-area writing
- Combined tools pairing prediction with speech recognition for learners whose oral language exceeds their written output
- Abbreviation expansion as a lower-cost alternative for recurring phrases

### Target Learners
- Students with dyslexia, dysgraphia, or other spelling-related disabilities, for whom transcription is the primary writing bottleneck [+M]
- Students with physical disabilities who benefit from reduced keystrokes [+M]
- Emergent writers and English learners, where recognition-based selection supports vocabulary use [~W]
- Fluent spellers and fast typists, who gain little and may be slowed [-M]

### Target Learning Goals
- Written expression: increasing length, fluency, and organization of compositions
- Spelling accuracy in produced text (distinct from spelling knowledge)
- Writing stamina and willingness to revise, by lowering the cost of producing text

### Instructions
1. Assess the learner's transcription bottleneck: confirm that spelling/keystroke demands, not idea generation, are the limiting factor.
2. Configure the tool — set prediction list length, enable phonetic matching, and load topic dictionaries for the current assignment.
3. Model tool use explicitly: demonstrate scanning the list, listening to readback, and selecting, using a [think-aloud](../strategies/think-aloud_modeling.md) approach.
4. Pair the tool with [practice](../elements/practice.md) on authentic writing tasks so prediction becomes automatic rather than attention-demanding.
5. Fade support as fluency develops — reduce prediction frequency or move to abbreviation expansion — and continue targeted spelling instruction alongside.

## Related Strategies
- [Text-to-Speech](../principles/text-to-speech.md) — complementary readback that lets learners verify predicted words
- [Speech-to-Text](../principles/speech-to-text.md) — alternative transcription accommodation for learners with stronger oral than written language
- [Scaffolded Writing Frames](../strategies/sentence-frames.md) — addresses planning and structure rather than transcription

## Examples
- **Co:Writer (Don Johnston)** — widely used in special education; offers phonetic prediction and topic dictionaries; [https://learningtools.donjohnston.com/product/cowriter/](https://learningtools.donjohnston.com/product/cowriter/)
- **Clicker (Crick Software)** — word prediction plus grids for elementary writers; [https://www.cricksoft.com/us/clicker](https://www.cricksoft.com/us/clicker)
- **Read&Write (Texthelp)** — prediction bundled with literacy supports in mainstream classrooms; [https://www.texthelp.com/products/read-and-write/](https://www.texthelp.com/products/read-and-write/)
- **iOS/Android built-in keyboards** — consumer-grade prediction now standard, though not configurable for instructional purposes

## Key Sources
- MacArthur, C. A. (2009). Reflections on research on writing and technology for struggling writers. *Learning Disabilities Research & Practice, 24*(2), 93–102. [doi:10.1111/j.1540-5826.2009.00283.x](https://doi.org/10.1111/j.1540-5826.2009.00283.x)
- Evmenova, A. S., Graff, H. J., Jerome, M. K., & Behrmann, M. M. (2010). Word prediction programs with phonetic spelling support: Performance comparisons and impact on journal writing for students with writing difficulties. *Journal of Special Education Technology, 25*(4), 33–48.
- Graham, S., & Perin, D. (2007). A meta-analysis of writing instruction for adolescent students. *Journal of Educational Psychology, 99*(3), 445–476. [doi:10.1037/0022-0663.99.3.445](https://doi.org/10.1037/0022-0663.99.3.445)
- Berninger, V. W., & Winn, W. D. (2006). Implications of advancements in brain research and technology for writing development, writing instruction, and educational evolution. In C. A. MacArthur, S. Graham, & J. Fitzgerald (Eds.), *Handbook of Writing Research* (pp. 96–114). Guilford Press.