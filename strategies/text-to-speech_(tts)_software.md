---
type: strategy
title: Text-to-Speech (TTS) Software
description: Text-to-speech (TTS) software converts written text into spoken audio, providing an alternative access route to digital and printed content.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Text-to-Speech (TTS) Software

## Description
Text-to-speech (TTS) software converts written text into synthesized spoken audio, allowing learners to listen to digital or scanned text rather than — or alongside — reading it. Modern implementations offer adjustable reading rate, voice selection, word-level highlighting that synchronizes audio with text, and integration with browsers, documents, and dedicated reading platforms. TTS is both an [accommodation](../elements/accommodations.md) for learners with reading difficulties and a universal design feature that benefits a broad range of learners.

## Design Implications

TTS bypasses decoding bottlenecks so learners can devote working memory to comprehension rather than word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+S]. A meta-analysis of read-aloud tools for students with reading disabilities found moderate positive effects on comprehension, with stronger effects when TTS was used as an accommodation during instruction than as a substitute for reading instruction itself [Wood et al., 2018](https://doi.org/10.1177/0022219416688446) [+M]. Synchronized highlighting (audio plus visual text) supports dual-channel processing consistent with multimedia learning principles [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

### Context
#### Requirements
- Digital text or accurate OCR conversion of printed material; poor scans degrade synthesis quality and comprehension
- Adjustable speech rate and voice options so learners can match listening speed to comprehension capacity
- For struggling readers, pairing with explicit decoding instruction — TTS supplements rather than replaces it
- Synchronized text highlighting where possible, to anchor attention to the words being spoken

#### Constraints
- TTS does not build decoding skills; over-reliance can displace the practice struggling readers need to develop word recognition [-M]
- Benefits shrink for proficient readers, for whom listening is often slower than reading and adds no comprehension advantage [~M]
- Comprehension from audio alone drops for complex expository text and for learners with limited vocabulary, since speech is transient and cannot be easily re-inspected [-W]
- Poorly paced or robotic narration increases extraneous cognitive load, particularly for novices [~M]

#### Implementation Variability
- **Accommodation mode**: TTS on assessments or assignments for learners with documented reading disabilities, decoupling content access from decoding ability
- **Bimodal reading**: audio with synchronized highlighting, which supports word-reading development better than audio alone [+W]
- **Universal access**: available to all learners in a [Universal Design for Learning](https://udlguidelines.cast.org) environment for preference-based use
- **Writing support**: TTS read-back of the learner's own drafts to support revision and error detection [+W]

### Target Learners
- Students with reading disabilities, dyslexia, or slow decoding [Wood et al., 2018](https://doi.org/10.1177/0022219416688446) [+M]
- English language learners, who can connect written and spoken forms of unfamiliar words [+W]
- Learners with visual impairments or print-related fatigue
- Less beneficial for strong readers with adequate time, who gain little and may prefer silent reading [~M]

### Target Learning Goals
- Content-area comprehension: accessing grade-level material despite decoding difficulty
- Vocabulary development: hearing pronunciation of new words in context
- Self-regulated revision: evaluating one's own writing by ear

### Instructions
1. Verify the text is digital and accurately converted (OCR quality check for scanned material).
2. Configure rate, voice, and highlighting to the learner's preference; teach the learner to adjust these independently.
3. Model bimodal use — following highlighted text while listening — before independent use.
4. Pair TTS with comprehension supports such as [Chunking](../principles/chunking.md) of text into sections and [Annotating](../principles/annotating.md) during listening.
5. Review periodically whether TTS remains an access tool or is displacing needed decoding practice.

## Related Strategies
- [Audiobooks](audiobooks.md) — the pre-recorded counterpart; human narration offers prosody TTS lacks, while TTS offers any-text flexibility
- [Accommodating Processing Speed Challenges](accommodating_processing_speed_challenges.md) — TTS rate adjustment is a direct lever for pacing
- [Accessible Syntax](accessible_syntax.md) — simplifying text complements TTS by reducing the comprehension burden of complex sentences

## Examples
- **[Learning Ally](https://learningally.org)** and **[Bookshare](https://www.bookshare.org)** — accessible libraries serving students with print disabilities, combining human-narrated and TTS audio with synchronized text.
- **[Microsoft Immersive Reader](https://www.microsoft.com/education/products/immersive-reader)** — free TTS with syllable splitting, picture dictionary, and line focus, embedded across Office and Teams.
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar-based TTS with highlighting, widely used as a UDL accommodation in K–12 and higher education.
- **Kurzweil 3000** — long-standing TTS platform for students with dyslexia, combining read-aloud with study-skill tools.

## Key Sources
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73–84. [doi:10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- CAST. (2018). *Universal Design for Learning Guidelines version 2.2*. [https://udlguidelines.cast.org](https://udlguidelines.cast.org)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)