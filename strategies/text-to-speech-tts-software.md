---
type: strategy
id: text-to-speech-tts-software
aliases: [text-to-speech-tts, text-to-speech_software]
title: Text-to-Speech (TTS) Software
description: Text-to-speech (TTS) software converts written text into spoken audio, providing an alternative access route to digital and printed content.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Text-to-Speech (TTS) Software

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 1 mixed, 1 against) · 6 studies (3 review, 2 causal, 1 theoretical), `q1`–`q3` · 0 of 6 report an effect size · 1 claim rests on one study

## Description
Text-to-speech (TTS) software converts written text into synthesized spoken audio, allowing learners to listen to digital or scanned text rather than — or alongside — reading it. Modern implementations offer adjustable reading rate, voice selection, word-level highlighting that synchronizes audio with text, and integration with browsers, documents, and dedicated reading platforms. TTS is both an [accommodation](../elements/accommodations.md) for learners with reading difficulties and a universal design feature that benefits a broad range of learners.

## Design Implications

TTS bypasses decoding bottlenecks so learners can devote working memory to comprehension rather than word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+M]. A meta-analysis of read-aloud tools for students with reading disabilities found moderate positive effects on comprehension, with stronger effects when TTS was used as an accommodation during instruction than as a substitute for reading instruction itself Wood et al., 2018. Synchronized highlighting (audio plus visual text) supports dual-channel processing consistent with multimedia learning principles [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

### Context
#### Requirements
- Digital text or accurate OCR conversion of printed material; poor scans degrade synthesis quality and comprehension
- Adjustable speech rate and voice options so learners can match listening speed to comprehension capacity
- For struggling readers, pairing with explicit decoding instruction — TTS supplements rather than replaces it
- Synchronized text highlighting where possible, to anchor attention to the words being spoken
- Digital text in an accessible format (HTML, EPUB, tagged PDF) so the synthesizer can parse reading order and structure
- Adjustable speech rate and voice options; learners differ widely in preferred pace
- Highlighting of the word or sentence being spoken, to bind audio and visual input
- For assessment use, a clear policy on whether TTS is permitted and whether it is read-aloud accommodation or a universal tool
- Digital text in a compatible format (or OCR for scanned print); compatible operating system and assistive technology stack (e.g., screen magnification)
- Headphones for classroom use to avoid disturbing peers
- Learner training: voice speed, highlighting, and dictionary features require explicit [demonstration](../elements/demonstration.md) and guided [application](../elements/application.md) before independent use
- A decision framework for when TTS is appropriate (access need) versus when decoding practice is the instructional goal

#### Constraints
- TTS does not build decoding skills; over-reliance can displace the practice struggling readers need to develop word recognition [-M]
- Benefits shrink for proficient readers, for whom listening is often slower than reading and adds no comprehension advantage [~M]
- Comprehension from audio alone drops for complex expository text and for learners with limited vocabulary, since speech is transient and cannot be easily re-inspected [-W]
- Poorly paced or robotic narration increases extraneous cognitive load, particularly for novices [~M]
- Synthetic speech degrades comprehension of complex syntax, homographs, and technical vocabulary compared with human narration [-W]
- Listening alone yields poorer recall of expository text than reading for skilled readers, because auditory input is transient and harder to review [~M]
- Poorly tagged documents produce garbled reading order, adding rather than reducing load [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [-W]
- Synthesized speech mispronounces irregular words, homographs, and technical vocabulary, which can distort meaning in domains with precise terminology [~M]
- Listening imposes its own working-memory demands; long passages at high speed degrade comprehension, so pacing and [chunking](../principles/chunking.md) of text matter [-W]

#### Implementation Variability
- **Accommodation mode**: TTS on assessments or assignments for learners with documented reading disabilities, decoupling content access from decoding ability
- **Bimodal reading**: audio with synchronized highlighting, which supports word-reading development better than audio alone [+W]
- **Universal access**: available to all learners in a [Universal Design for Learning](https://udlguidelines.cast.org) environment for preference-based use
- **Writing support**: TTS read-back of the learner's own drafts to support revision and error detection [+W]
- **Word-level highlighting with audio** (Read&Write, Voice Dream Reader) — supports tracking and phoneme-grapheme mapping
- **Full-document audio** ([audiobooks](../elements/audiobooks.md), Learning Ally) — access to grade-level content beyond current decoding skill
- **Screen readers** (JAWS, NVDA, VoiceOver) — full non-visual access, requiring document accessibility standards (WCAG)
- **Embedded courseware narration** — TTS as a universal option in LMS content and assessments
- **As an accommodation:** individual learners with dyslexia or visual impairment use TTS for all text access, often with extended-time equivalents on assessments
- **As a proofreading tool:** writers listen to their own drafts to catch errors that visual reading misses
- **As a UDL option:** TTS offered universally so no learner is singled out; built-in tools (Microsoft Immersive Reader, Apple Speak Screen) lower adoption cost
- **Layered supports:** TTS combined with highlighting, masking, and picture dictionaries (e.g., Read&Write) rather than bare audio output

### Target Learners
- Students with reading disabilities, dyslexia, or slow decoding Wood et al., 2018
- English language learners, who can connect written and spoken forms of unfamiliar words [+W]
- Learners with visual impairments or print-related fatigue
- Less beneficial for strong readers with adequate time, who gain little and may prefer silent reading [~M]
- Learners with dyslexia, low vision, or blindness, for whom TTS is often essential access [~S]
- Struggling decoders whose listening comprehension exceeds their reading comprehension — TTS lets them work at grade level while decoding develops
- English language learners using audio support to map spoken and written forms [~W]
- Skilled readers benefit least; for them TTS is mainly a convenience or preference [~M]
- Students with dyslexia, decoding deficits, or visual impairments — the group with the strongest evidence base [+M]
- English learners, who benefit from hearing pronunciation while following highlighted text [~W]
- Proficient readers gain little from verbatim narration and may be slowed by it [-M]

### Target Learning Goals
- Content-area comprehension: accessing grade-level material despite decoding difficulty
- Vocabulary development: hearing pronunciation of new words in context
- Self-regulated revision: evaluating one's own writing by ear
- Comprehension of complex texts when decoding is a barrier
- Content-area knowledge acquisition (science, social studies) independent of reading level
- Fluency development when TTS models are used for read-along rather than read-for
- Access to content knowledge when decoding is not the instructional target
- Proofreading and revision in writing instruction
- Development of independent learning behaviors and self-advocacy in assistive technology use

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
- Audiobook-supported reading — TTS at book scale, pairing human-narrated audio with print
- Read-aloud accommodation — TTS applied to assessment conditions
- Highlighting and text marking — complements TTS by adding a visual processing layer to spoken input
- Audiobooks — a pre-recorded alternative serving the same access function with human narration
- Multisensory presentation — TTS as one channel in a multimodal design
- Universal Design for Learning — TTS as a standard multiple-means-of-representation option

## Examples
- **[Learning Ally](https://learningally.org)** and **[Bookshare](https://www.bookshare.org)** — accessible libraries serving students with print disabilities, combining human-narrated and TTS audio with synchronized text.
- **[Microsoft Immersive Reader](https://www.microsoft.com/education/products/immersive-reader)** — free TTS with syllable splitting, picture dictionary, and line focus, embedded across Office and Teams.
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar-based TTS with highlighting, widely used as a UDL accommodation in K–12 and higher education.
- **Kurzweil 3000** — long-standing TTS platform for students with dyslexia, combining read-aloud with study-skill tools.
- **[Read&Write](https://www.texthelp.com/products/readwrite/)** (Texthelp) — toolbar with word-level highlighting, dictionary, and adjustable voices, widely used in K–12 for dyslexia support.
- **[Learning Ally](https://www.learningally.org)** — human-narrated audiobooks with synced text highlighting for students with print disabilities.
- **[Voice Dream Reader](https://www.voicedream.com)** — mobile app combining TTS with synchronized highlighting and configurable voices.
- **NVDA ([nvaccess.org](https://www.nvaccess.org))** — free open-source screen reader providing full non-visual access to digital content.
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar-based TTS with highlighting, picture dictionaries, and screen-masking, widely documented in K–12 classrooms for students with reading difficulties.
- **[Microsoft Immersive Reader](https://www.microsoft.com/en-us/education/products/learning-tools)** — free TTS with syllabification, parts-of-speech coloring, and line focus, built into Word, Edge, and Teams.
- **[NaturalReader](https://www.naturalreaders.com)** and **[ClaroRead](https://www.clarosoftware.com)** — standalone TTS with MP3 export for portable listening.
- **Built-in system tools** — Apple VoiceOver and Speak Screen, Microsoft Narrator — provide zero-cost TTS for basic access needs.

## Key Sources
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73–84. [doi:10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- CAST. (2018). *Universal Design for Learning Guidelines version 2.2*. [https://udlguidelines.cast.org](https://udlguidelines.cast.org)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Rose, D. H., & Meyer, A. (2002). *Teaching every student in the digital age: Universal design for learning.* ASCD.
- Perfetti, C. A., & Stafura, J. (2014). Word knowledge in a theory of reading comprehension. *Scientific Studies of Reading, 18*(1), 22–37. [doi:10.1080/10888438.2013.827687](https://doi.org/10.1080/10888438.2013.827687)
- Moreno, R., & Mayer, R. (2007). Interactive multimodal learning environments. *Educational Psychology Review, 19*(3), 309–326. [doi:10.1007/s10648-007-9047-2](https://doi.org/10.1007/s10648-007-9047-2)
- Dalton, B., & Strangman, N. (2006). Improving struggling readers' comprehension through scaffolded hypertexts and other technology supports. *Journal of Special Education Technology, 21*(1), 5–21.

<!-- merged 2026-10-13 from strategies/text-to-speech-tts ("Text-to-Speech (TTS)"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Text-to-Speech (TTS)

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (1 for, 1 mixed, 1 against) · 6 studies (3 review, 2 causal, 1 theoretical), `q1`–`q3` · 0 of 6 report an effect size · 1 claim rests on one study

## Description
Text-to-speech (TTS) converts written text into synthesized spoken audio, allowing learners to listen to digital text rather than — or alongside — reading it. It is implemented through screen readers (JAWS, NVDA), literacy support tools ([Read&Write](https://www.texthelp.com/products/readwrite/), [Learning Ally](https://www.learningally.org)), built-in OS features, and audio narration embedded in courseware. TTS serves both as an [accommodation](../elements/accommodations.md) for learners with print disabilities and as a universal design option for any learner who benefits from hearing text.

## Design Implications

TTS reduces the decoding burden so that working memory resources can be directed toward comprehension rather than word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+M]. For learners with dyslexia or visual impairment, this access benefit is well established; for fluent readers, listening to text while reading it can support attention and engagement, though benefits shrink as reading skill increases [~M]. Combining spoken and written presentation of the *same* text can aid recall, but presenting redundant narration with identical on-screen text can also add extraneous load if learners cannot control pacing [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

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
- **Full-document audio** ([audiobooks](../elements/audiobooks.md), Learning Ally) — access to grade-level content beyond current decoding skill
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
-->

<!-- merged 2026-10-13 from strategies/text-to-speech_software ("Text-to-Speech Software"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Text-to-Speech Software

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 3 studies (1 causal, 1 review, 1 theoretical), `q1`–`q3` · 0 of 3 report an effect size · 1 claim rests on one study

## Description
Text-to-speech (TTS) software converts written text into synthesized speech, allowing learners to listen to digital text rather than — or in addition to — reading it visually. Modern TTS tools read web pages, PDFs, and word-processor documents, often with synchronized word- or sentence-level highlighting, adjustable voice speed, and OCR integration for scanned print. In learning design, TTS functions primarily as an [accommodation](../elements/accommodations.md) that removes decoding barriers, and secondarily as a multimodal presentation option that pairs auditory and visual input.

## Design Implications

TTS is best understood as an access intervention, not a reading intervention: it lets learners with weak decoding reach grade-level content, but it does not by itself build decoding skill. Meta-analytic evidence shows read-aloud tools improve comprehension for students with reading disabilities, with effects strongest when TTS is used to bypass decoding rather than as a universal substitute for reading instruction [Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities?](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+M]. For general learners, adding narration to on-screen text can support learning when the two channels carry complementary load, but simply duplicating identical text in both channels yields little benefit [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

### Context
#### Requirements
- Digital text in a compatible format (or OCR for scanned print); compatible operating system and assistive technology stack (e.g., screen magnification)
- Headphones for classroom use to avoid disturbing peers
- Learner training: voice speed, highlighting, and dictionary features require explicit [demonstration](../elements/demonstration.md) and guided [application](../elements/application.md) before independent use
- A decision framework for when TTS is appropriate (access need) versus when decoding practice is the instructional goal

#### Constraints
- Over-reliance can displace the decoding practice struggling readers need; automatic word recognition is a trainable skill that TTS bypasses rather than builds [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [-M]
- Synthesized speech mispronounces irregular words, homographs, and technical vocabulary, which can distort meaning in domains with precise terminology [~M]
- Narrating text verbatim in both visual and auditory channels adds redundant load without improving learning for proficient readers [Media combinations affect recall and retention.](../claims/media-combinations-affect-recall-and-retention.md) [-M]
- Listening imposes its own working-memory demands; long passages at high speed degrade comprehension, so pacing and [chunking](../principles/chunking.md) of text matter [-W]

#### Implementation Variability
- **As an accommodation:** individual learners with dyslexia or visual impairment use TTS for all text access, often with extended-time equivalents on assessments
- **As a proofreading tool:** writers listen to their own drafts to catch errors that visual reading misses
- **As a UDL option:** TTS offered universally so no learner is singled out; built-in tools (Microsoft Immersive Reader, Apple Speak Screen) lower adoption cost
- **Layered supports:** TTS combined with highlighting, masking, and picture dictionaries (e.g., Read&Write) rather than bare audio output

### Target Learners
- Students with dyslexia, decoding deficits, or visual impairments — the group with the strongest evidence base [+M]
- English learners, who benefit from hearing pronunciation while following highlighted text [~W]
- Proficient readers gain little from verbatim narration and may be slowed by it [-M]

### Target Learning Goals
- Access to content knowledge when decoding is not the instructional target
- Proofreading and revision in writing instruction
- Development of independent learning behaviors and self-advocacy in assistive technology use

### Instructions
1. Assess the learner's decoding profile to determine whether TTS serves as an [accommodation](../elements/accommodations.md) or whether targeted phonics instruction should take priority
2. [Demonstrate](../elements/demonstration.md) the tool explicitly: adjusting speed, using highlighting, and employing the dictionary or screenshot-reading features
3. Provide guided [application](../elements/application.md) on short, high-interest texts before independent use
4. Establish a listening routine — segment text, pause to summarize, and re-listen to difficult passages rather than passively streaming audio
5. Review usage periodically and fade TTS for tasks where independent decoding is the goal

## Related Strategies
- Audiobooks — a pre-recorded alternative serving the same access function with human narration
- Multisensory presentation — TTS as one channel in a multimodal design
- Universal Design for Learning — TTS as a standard multiple-means-of-representation option

## Examples
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar-based TTS with highlighting, picture dictionaries, and screen-masking, widely documented in K–12 classrooms for students with reading difficulties.
- **[Microsoft Immersive Reader](https://www.microsoft.com/en-us/education/products/learning-tools)** — free TTS with syllabification, parts-of-speech coloring, and line focus, built into Word, Edge, and Teams.
- **[NaturalReader](https://www.naturalreaders.com)** and **[ClaroRead](https://www.clarosoftware.com)** — standalone TTS with MP3 export for portable listening.
- **Built-in system tools** — Apple VoiceOver and Speak Screen, Microsoft Narrator — provide zero-cost TTS for basic access needs.

## Key Sources
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73–84. [doi:10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the science of instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Moreno, R., & Mayer, R. (2007). Interactive multimodal learning environments. *Educational Psychology Review, 19*(3), 309–326. [doi:10.1007/s10648-007-9047-2](https://doi.org/10.1007/s10648-007-9047-2)
- Dalton, B., & Strangman, N. (2006). Improving struggling readers' comprehension through scaffolded hypertexts and other technology supports. *Journal of Special Education Technology, 21*(1), 5–21.
-->
