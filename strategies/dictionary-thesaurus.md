---
type: strategy
id: dictionary-thesaurus
title: "Dictionary & Thesaurus"
description: Incorporating web dictionaries and thesauruses into vocabulary lessons allows learners to quickly search and understand unfamiliar words.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Dictionary & Thesaurus

> **Strategy** · [All strategies](index.md)

## Description
Incorporating web dictionaries and thesauruses into vocabulary lessons allows learners to quickly search and understand unfamiliar words. When learners look up challenging words while reading, they monitor their comprehension and activate cognitive processes that support increased recall and consolidation to long-term memory. Features such as voice search, audio pronunciation, and embedded quizzes can further support vocabulary building and practice.

## Design Implications

Dictionary and thesaurus use converts word-learning from passive guessing into an active, self-directed lookup cycle, but the learning payoff depends on how the retrieved definition is processed. Definitions alone are weak vehicles for word knowledge — dictionary definitions are often written in a compressed register that learners misread, and a single encounter with a definition rarely produces durable learning [~M]. Retention improves substantially when lookups are followed by elaborative processing: connecting the word to prior knowledge, generating an example sentence, or encountering the word repeatedly across varied contexts [+M]. Because each lookup interrupts reading and consumes working memory, the strategy works best when lookups are selective (targeting high-value, unfamiliar words) rather than exhaustive.

### Context
#### Requirements
- Access to web dictionaries and thesauruses, such as the [Merriam-Webster Dictionary app](https://www.merriam-webster.com), [Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com), or [Dictionary.com](https://www.dictionary.com)
- Learner skill in interpreting dictionary entries (part of speech, multiple senses, example sentences), which itself may need explicit instruction
- A mechanism for recording and revisiting looked-up words — a personal glossary, [Annotating](../principles/annotating.md) workflow, or spaced-review deck — since a single lookup rarely produces durable learning [~M]

#### Constraints
- Requires learners to actively search for and look up words, which may be time-consuming; excessive lookups during reading disrupt comprehension of the passage as a whole [~M]
- Reliance on dictionary definitions may not always provide sufficient context for understanding; definitions frequently use abstract superordinate terms that are themselves unfamiliar to the learner [~M]
- Thesaurus use without guidance produces word substitutions that are semantically wrong (synonyms are rarely interchangeable), which can degrade writing quality [-M]
- Learners with weak decoding or spelling skills may struggle to locate words in a dictionary at all, making the tool inaccessible without voice search or embedded lookup support [-W]

#### Implementation Variability
- **Embedded vs. standalone lookup:** e-reader tap-to-define features (e.g., Kindle's built-in dictionary) lower the interruption cost compared with switching to a separate app, increasing lookup frequency but sometimes reducing deliberate processing
- **Teacher-selected vs. learner-selected words:** pre-teaching a curated set of high-utility words before reading complements, and often outperforms, purely learner-driven lookup for the highest-impact vocabulary [~M]
- **Multimedia entries:** audio pronunciation and illustrated entries support learners who cannot yet decode the headword reliably
- **Thesaurus as generation task:** asking learners to choose among candidate synonyms and justify the choice turns the thesaurus into a discrimination exercise rather than a substitution shortcut

### Target Learners
- Intermediate readers who can decode fluently but encounter unknown vocabulary; for beginning readers, lookup demands can overwhelm comprehension [~M]
- Second-language learners, for whom learner-oriented dictionaries (with controlled defining vocabulary and corpus-based example sentences) are markedly more usable than native-speaker dictionaries [+M]
- Learners with strong self-regulation who can judge which words are worth looking up; younger or less metacognitively skilled learners need guidance on when to look up versus infer from context [~W]

### Target Learning Goals
- Vocabulary acquisition: building word meanings and the network of synonyms and contrasts captured in a thesaurus
- Reading comprehension: resolving word-level obstacles to passage understanding and monitoring comprehension breakdowns
- Self-directed learning: developing the habit and skill of independent reference use

### Instructions
1. Pre-teach a small set of high-utility words from the upcoming text so lookups during reading stay selective ([Advance Organizers](../elements/advance-organizers.md)).
2. During reading, have learners flag unfamiliar words rather than immediately looking up each one; after reading, they select the words most critical to understanding and look those up.
3. Require an elaborative step after each lookup: write a personal definition, an original sentence, or a synonym contrast ([Annotating](../principles/annotating.md)).
4. Use the thesaurus as a comparison task — choose between candidate synonyms and justify the choice — rather than as a substitution source.
5. Revisit recorded words in spaced review or embedded quizzes ([Practice](../elements/practice.md)), since repeated, spaced encounters drive retention [+M].
6. Assess by reviewing learners' personal glossaries and scoring definitions for accuracy and depth of elaboration.

## Related Strategies
- [Annotating](../principles/annotating.md) — recording looked-up words in the margins or a glossary is the annotation habit that makes lookups durable
- [Activating Prior Knowledge](../strategies/activating_prior_knowledge.md) — connecting a new word's definition to known concepts and experiences is what converts a lookup into learning
- [Chunking](../principles/chunking.md) — grouping looked-up words into semantic clusters (e.g., by the thesaurus's synonym sets) reduces the memory load of vocabulary study

## Related Elements
- [Practice](../elements/practice.md) — spaced retrieval of looked-up words is what consolidates them
- [Analogies](../elements/analogies.md) — relating a new word to a familiar concept deepens the definition beyond the dictionary entry
- [Assessment](../elements/assessment.md) — glossary review and vocabulary quizzes provide evidence of word learning

## Examples
- **[Merriam-Webster Dictionary app](https://www.merriam-webster.com)** — voice search, audio pronunciation, word-of-the-day, and built-in vocabulary quizzes for self-assessment.
- **[Oxford Learner's Dictionaries](https://www.oxfordlearnersdictionaries.com)** — learner-oriented entries with a controlled defining vocabulary (the Oxford 3000), corpus-based example sentences, and pronunciation audio, designed specifically for second-language users.
- **Amazon Kindle tap-to-define** — embedded dictionary lookup in e-readers; the Vocabulary Builder feature automatically collects looked-up words into flashcards for review, closing the loop between lookup and spaced practice.
- **Frayer Model routine** — after a dictionary lookup, learners complete a four-quadrant graphic organizer (definition, characteristics, examples, non-examples), forcing elaboration beyond the retrieved definition.

## Key Sources
- Swanborn, M. S. L., & de Glopper, K. (1999). Incidental word learning while reading: A meta-analysis. *Review of Educational Research, 69*(3), 261–285. [doi:10.3102/00346543069003261](https://doi.org/10.3102/00346543069003261)
- Nation, I. S. P. (2001). *Learning vocabulary in another language*. Cambridge University Press. [doi:10.1017/CBO9781139524759](https://doi.org/10.1017/CBO9781139524759)
- Beck, I. L., McKeown, M. G., & Kucan, L. (2013). *Bringing words to life: Robust vocabulary instruction* (2nd ed.). Guilford Press.
- Nagy, W. E., & Scott, J. A. (2000). Vocabulary processes. In M. L. Kamil et al. (Eds.), *Handbook of reading research* (Vol. 3, pp. 269–284). Erlbaum.