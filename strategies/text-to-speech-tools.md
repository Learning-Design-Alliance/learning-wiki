---
type: strategy
title: Text To Speech Tools
description: Software that converts written text into synthesized spoken audio, allowing learners to listen to digital text rather than — or alongside — reading it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Text To Speech Tools

> **Strategy** · [All strategies](index.md)

## Description
Text-to-speech (TTS) tools render digital text as synthesized speech, typically with word-level highlighting that tracks the narration. They are used both as an [accommodation](../elements/accommodations.md) for learners with reading difficulties and as a universal design option that lets learners switch between reading and listening modes.

## Design Implications

TTS offloads decoding work so that limited working-memory resources can be directed toward comprehension rather than word recognition [Automatic word recognition frees resources for comprehension.](../claims/automatic-word-recognition-frees-resources-for-comprehension.md) [+M]. For learners whose decoding is slow or effortful, listening removes a bottleneck that otherwise degrades understanding [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+M]. For fluent readers, however, TTS adds little and can interfere: reading and listening simultaneously can create redundancy effects when the audio merely duplicates the on-screen text [Clark, R. C., & Mayer, R. E. (2016)](https://doi.org/10.1002/9781119239086) [~M].

### Context
#### Requirements
- Digital, machine-readable text (screen-reader-compatible documents, EPUB, or tagged PDFs)
- Adjustable speech rate and voice; word- or sentence-level highlighting to support tracking
- A clear purpose: decoding support, comprehension support, proofreading, or fatigue management — not simply "audio because we can"

#### Constraints
- Redundant narration of on-screen text can hurt learning for fluent readers, consistent with the redundancy principle [Clark, R. C., & Mayer, R. E. (2016)](https://doi.org/10.1002/9781119239086) [-M]
- Synthetic speech at default rates can impair comprehension for learners with auditory processing difficulties; rate must be adjustable [~M]
- Over-reliance can reduce print exposure and practice for learners who still need to build decoding skill; TTS should supplement, not replace, reading instruction for beginning readers [-W]
- Poorly structured source documents (untagged PDFs, image-based scans) produce garbled output that adds cognitive load rather than reducing it

#### Implementation Variability
- **Decoding accommodation:** full text read aloud for students with dyslexia or low vision (e.g., built into [Kurzweil 3000](https://www.kurzweil3000.com) or [Read&Write](https://www.texthelp.com/products/readwrite/))
- **Bimodal reading:** audio with synchronized highlighting, which research on supported reading suggests can benefit struggling readers more than audio alone [+W]
- **Self-monitoring aid:** fluent writers use TTS to hear their own drafts, catching errors that silent reading misses [+W]
- **Universal option:** offered via [Choice Boards](../elements/choice-boards.md) so all learners can select modality by context and fatigue

### Target Learners
- Learners with dyslexia, low vision, or other print disabilities, for whom TTS is a well-established accommodation [+M]
- English language learners, who can pair audio input with text to support phonological mapping [+W]
- Beginning readers should use TTS selectively — it supports access to age-appropriate content but does not build decoding skill on its own [-W]

### Target Learning Goals
- Comprehension of content-area text where the goal is knowledge acquisition, not reading practice
- Access to grade-level material despite below-grade decoding
- Revision and proofreading of written work

### Instructions
1. Verify the source material is digitally accessible (tagged headings, real text, not scanned images).
2. Set the purpose with learners: decoding support, comprehension, or revision — and select bimodal highlighting or audio-only accordingly.
3. Adjust speech rate and voice to the individual learner; default rates are often too fast.
4. Pair TTS access with comprehension supports such as [Annotating](../principles/annotating.md) or [Advance Organizers](../elements/advance-organizers.md), since listening alone does not guarantee engagement.
5. Review periodically: fade TTS for decoding practice where the goal is reading growth, and retain it for content access where it is not.

## Related Strategies
- [Accommodating Processing Speed Challenges](accommodating_processing_speed_challenges.md) — TTS is a primary tool for learners who process print slowly
- [Audiobooks](../principles/audiobooks.md) — the pre-recorded counterpart; TTS generalizes it to any text

## Examples
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar-based TTS with word highlighting, dictionary, and translation, widely deployed in K–12 and higher education.
- **[Kurzweil 3000](https://www.kurzweil3000.com)** — TTS with study-skill tools (highlighting, notes) designed for learners with dyslexia and other print disabilities.
- **[Immersive Reader (Microsoft)](https://www.microsoft.com/en-us/education/products/immersive-reader)** — free TTS with syllabification, picture dictionary, and adjustable spacing, embedded across Office and Teams.
- **[Bookshare](https://www.bookshare.org)** — accessible e-book library whose titles are read via TTS or braille for readers with print disabilities.

## Key Sources
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the science of instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. *Journal of Learning Disabilities, 51*(1), 73–84. [doi:10.1177/0022219416688170](https://doi.org/10.1177/0022219416688170)
- Rose, D. H., & Meyer, A. (2002). *Teaching every student in the digital age: Universal design for learning.* ASCD.
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive load theory.* Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)