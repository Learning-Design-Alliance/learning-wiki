---
type: strategy
id: customizable_display_of_information
title: Customizable Display of Information
description: Providing adjustable settings and accessible formats to accommodate individual needs and preferences.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Customizable Display of Information

> **Strategy** · [All strategies](index.md)

## Description
Customizable display of information means presenting content in digital formats whose appearance and modality learners can adjust — font size and type, spacing, color contrast, text-to-speech, captions, language, and layout. Rather than fixing a single presentation, the design exposes controls so each learner can configure the display to fit perceptual, linguistic, and working-memory constraints. This is a core UDL (Universal Design for Learning) representation strategy: the content stays constant while its rendering flexes.

## Design Implications

Adjusting display parameters changes how much working-memory capacity is consumed by perception and decoding, freeing resources for comprehension [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. For example, larger character spacing and shorter line lengths measurably improve reading speed and comprehension for readers with dyslexia, and e-reader displays that permit font manipulation outperform fixed paper for some of these readers (Schneps et al., 2013) [+M]. Pairing adjustable text with adjustable audio or visual rendering supports dual-channel processing [Dual coding improves recall.](../claims/dual-coding-improves-recall.md) [+S], but added visual decoration does not by itself aid learning [Decorative illustrations do not improve learning.](../claims/decorative-illustrations-do-not-improve-learning.md) [~S] — customization should serve legibility and modality access, not ornament.

### Context
#### Requirements
- Digital source materials (HTML/EPUB rather than scanned images) so settings actually propagate
- Built-in or platform-level controls: text size, font, spacing, contrast, captions, text-to-speech, translation
- Default settings that are already legible and accessible, so learners who never touch the controls are still served
- Brief guidance or defaults for learners who cannot judge which settings help them

#### Constraints
- Offering too many unexplained options creates decision overhead and extraneous load, particularly for novices [~M] — curated presets outperform raw control panels
- Customization cannot compensate for poorly structured content; if the underlying text is disorganized, no display setting fixes it
- Matching display to self-reported "learning style" preferences does not improve outcomes [X] — customize for measured needs (vision, decoding, language), not for style labels
- Print-locked materials (PDFs of scans, fixed-layout e-books) defeat customization entirely

#### Implementation Variability
- Learner-controlled settings (font, contrast, playback speed) vs. system-adaptive rendering (automatic reflow, responsive layout)
- Author-provided alternatives (captions, transcripts, alt text, simplified-language versions) vs. tool-provided transformations (text-to-speech, browser readers)
- Range from individual accommodations documented in a plan to universal defaults available to everyone

### Target Learners
- Learners with sensory disabilities (low vision, blindness, deafness, hearing loss), who depend on adjustable size, contrast, screen-reader compatibility, captions, and transcripts [+M]
- Learners with dyslexia or other decoding difficulties, who benefit from adjustable font, spacing, and text-to-speech (Rello & Baeza-Yates, 2013; Schneps et al., 2013) [+M]
- Second-language learners, who benefit from captions, adjustable reading speed, and translation options [+M]
- Older adults and learners using small screens or suboptimal environments — effectively most learners at some point

### Target Learning Goals
- Comprehension of text and multimedia content: removing decoding and perceptual barriers so the goal-level learning is reachable
- Vocabulary and language access: adjustable glossing, translation, and speech support
- Self-regulated learning: choosing and evaluating one's own display settings builds awareness of what conditions support one's work

### Instructions
1. Publish content in reflowable, accessible formats (HTML, EPUB, tagged PDF) rather than images of text.
2. Provide defaults that meet accessibility standards (sufficient contrast, readable base size, [Chunking](../principles/chunking.md) of long passages into navigable sections) [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S].
3. Expose a small set of high-value controls — text size, contrast, text-to-speech, captions, playback speed — with sensible presets; document formal [Accommodations](../elements/accommodations.md) separately for learners who need more.
4. Offer equivalent modalities (captions, transcripts, audio versions) so learners can shift channels rather than strain one [Dual coding improves recall.](../claims/dual-coding-improves-recall.md) [+S].
5. Briefly teach learners what the settings do and when to use them; check that chosen settings actually improve their reading and viewing, and adjust.

## Related Strategies
- [Chunking](../principles/chunking.md) — segmenting content complements display control; both reduce perceptual and memory load
- [Accessible syntax](accessible_syntax.md) — simplifying sentence structure addresses the same decoding barriers at the text level rather than the display level
- [Providing multiple means of representation](providing_multiple_means_of_representation.md) — customizable display is the delivery mechanism for this UDL principle

## Examples
- **[CAST UDL Guidelines](https://udlguidelines.cast.org)** — "Multiple Means of Representation" includes customizable display as a named checkpoint, with concrete options (text size, contrast, captions, text-to-speech).
- **[Bookshare](https://www.bookshare.org)** — accessible e-book library for readers with print disabilities; downloads in formats supporting large print, braille, and audio.
- **[Immersive Reader (Microsoft)](https://www.microsoft.com/en-us/education/products/immersive-reader)** — free tool embedded in Word, Teams, and Edge offering adjustable spacing, syllable highlighting, line focus, and read-aloud; widely used for dyslexia support.
- **[Khan Academy](https://www.khanacademy.org)** — video playback-speed control and multilingual subtitles and transcripts on lesson videos.

## Key Sources
- Rose, D. H., & Meyer, A. (2002). *Teaching every student in the digital age: Universal design for learning.* ASCD.
- Mayer, R. E. (2009). *Multimedia learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)
- Schneps, M. H., Thomson, J. M., Chen, C., Sonnert, G., & Pomplun, M. (2013). E-readers are more effective than paper for some with dyslexia. *PLoS ONE, 8*(9), e75634. [doi:10.1371/journal.pone.0075634](https://doi.org/10.1371/journal.pone.0075634)
- Rello, L., & Baeza-Yates, R. (2013). Good fonts for dyslexia. *Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '13).* ACM. [doi:10.1145/2513383.2513447](https://doi.org/10.1145/2513383.2513447)
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest, 9*(3), 105–119. [doi:10.1111/j.1539-6053.2009.01038.x](https://doi.org/10.1111/j.1539-6053.2009.01038.x)