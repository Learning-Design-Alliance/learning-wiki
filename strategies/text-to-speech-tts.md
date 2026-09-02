---
type: strategy
id: text-to-speech-tts
title: Text-to-Speech (TTS)
description: Text-to-speech (TTS) technology converts written text into spoken words, enhancing accessibility and comprehension for individuals with dyslexia, visual impairments, or other learning differences.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Text-to-Speech (TTS)

> **Strategy** · [All strategies](index.md)

## Description
Text-to-speech (TTS) converts written text into synthesized spoken audio, allowing learners to listen to digital text rather than — or alongside — reading it. It is implemented through screen readers (JAWS, NVDA), literacy support tools ([Read&Write](https://www.texthelp.com/products/readwrite/), [Learning Ally](https://www.learningally.org)), built-in OS features, and audio narration embedded in courseware. TTS serves both as an [accommodation](../elements/accommodations.md) for learners with print disabilities and as a universal design option for any learner who benefits from hearing text.

## Design Implications

TTS reduces the decoding burden so that working memory resources can be directed toward comprehension rather than word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+S]. For learners with dyslexia or visual impairment, this access benefit is well established; for fluent readers, listening to text while reading it can support attention and engagement, though benefits shrink as reading skill increases [~M]. Combining spoken and written presentation of the *same* text can aid recall, but presenting redundant narration with identical on-screen text can also add extraneous load if learners cannot control pacing [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

### Context
#### Requirements
- Digital text in an accessible format (HTML, EPUB, tagged PDF) so the synthesizer can parse reading order and structure
- Adjustable speech rate and voice options; learners differ widely in preferred pace
- Highlighting of the word or sentence being spoken, to bind audio and visual input
- For assessment use, a clear policy on whether TTS is permitted and whether it is read-aloud accommodation or a universal tool

#### Constraints
- For learners still building decoding skills, TTS can bypass the practice needed for automatic word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [-M] — over-reliance may slow reading development if listening replaces decoding practice entirely
- Synthetic speech degrades comprehension of complex syntax, homographs, and technical vocabulary compared with human narration [-W]
- Listening alone yields poorer recall of expository text than reading for skilled readers, because auditory input is transient and harder to review [~M]
- Poorly tagged documents produce garbled reading order, adding rather than reducing load [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [-W]

#### Implementation Variability
- **Word-level highlighting with audio** (Read&Write, Voice Dream Reader) — supports tracking and phoneme-grapheme mapping
- **Full-document audio** ([audiobooks](../principles/audiobooks.md), Learning Ally) — access to grade-level content beyond current decoding skill
- **Screen readers** (JAWS, NVDA, VoiceOver) — full non-visual access, requiring document accessibility standards (WCAG)
- **Embedded courseware narration** — TTS as a universal option in LMS content and assessments

### Target Learners
- Learners with dyslexia, low vision, or blindness, for whom TTS is often essential access [~S]
- Struggling decoders whose listening comprehension exceeds their reading comprehension — TTS lets them work at grade level while decoding develops
- English language learners using audio support to map spoken and written forms [~W]
- Skilled readers benefit least; for them TTS is mainly a convenience or preference [~M]

### Target Learning Goals
- Comprehension of complex texts when decoding is a barrier
- Content-area knowledge acquisition (science, social studies) independent of reading level
- Fluency development when TTS models are used for read-along rather than read-for

### Instructions
1. Verify the source content is accessible: proper heading structure, reading order, alt text — otherwise the synthesizer output is unusable.
2. Select a tool matched to the goal: word-level highlighting for decoding support ([Accommodations](../elements/accommodations.md)), full-document audio for content access.
3. Let the learner control speech rate, voice, and whether to listen, read, or read along — learner control is central to effective use.
4. Pair listening with comprehension activity (annotation, summarizing) so audio input is processed actively rather than passively.
5. Review periodically whether TTS remains needed or whether it should be faded as decoding improves.

## Related Strategies
- Audiobook-supported reading — TTS at book scale, pairing human-narrated audio with print
- Read-aloud accommodation — TTS applied to assessment conditions
- Highlighting and text marking — complements TTS by adding a visual processing layer to spoken input

## Examples
- **[Read&Write](https://www.texthelp.com/products/readwrite/)** (Texthelp) — toolbar with word-level highlighting, dictionary, and adjustable voices, widely used in K–12 for dyslexia support.
- **[Learning Ally](https://www.learningally.org)** — human-narrated audiobooks with synced text highlighting for students with print disabilities.
- **[Voice Dream Reader](https://www.voicedream.com)** — mobile app combining TTS with synchronized highlighting and configurable voices.
- **NVDA ([nvaccess.org](https://www.nvaccess.org))** — free open-source screen reader providing full non-visual access to digital content.

## Key Sources
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73–84. [doi:10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
- Rose, D. H., & Meyer, A. (2002). *Teaching every student in the digital age: Universal design for learning.* ASCD.
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Perfetti, C. A., & Stafura, J. (2014). Word knowledge in a theory of reading comprehension. *Scientific Studies of Reading, 18*(1), 22–37. [doi:10.1080/10888438.2013.827687](https://doi.org/10.1080/10888438.2013.827687)