---
type: strategy
title: Dual Color Highlighting
description: Dual color highlighting is a text-to-speech feature that highlights the word being read aloud in one color while highlighting the containing sentence in another, synchronizing auditory and visual input during reading.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Dual Color Highlighting

## Description
Dual color highlighting is a feature within text-to-speech software that highlights the word currently being read aloud in one color (e.g., yellow) while highlighting the containing sentence in another color (e.g., blue). This creates a bimodal reading condition in which learners see and hear the text simultaneously, with the two-color scheme providing both word-level tracking and sentence-level context. It operationalizes multimedia learning principles by pairing spoken and written verbal input with visual attention cues [Combining spoken and written presentation affects recall and retention depending on modality conditions.](../claims/media-combinations-affect-recall-and-retention.md) [~M].

## Design Implications

Dual color highlighting reduces the working memory demand of visual tracking by externally guiding eye movements to the exact word being spoken, freeing capacity for comprehension [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. The sentence-level highlight supplies context that word-only highlighting lacks, supporting prosodic parsing and phrase-level meaning. Effectiveness depends on the emphasis directing attention to the right unit at the right time — the word highlight must track the audio precisely or the cue becomes misleading [Relevant emphasis directs learner attention to content.](../claims/relevancy-of-emphasis-directs-attention.md) [+M].

### Context
#### Requirements
- Text-to-speech software with synchronized dual-color highlighting (e.g., [Read&Write](https://www.texthelp.com/products/readwrite/), [ClaroRead](https://www.clarosoftware.com), [Voice Dream Reader](https://www.voicedream.com))
- Digital text in an accessible format; adjustable reading speed so audio and highlight remain synchronized
- Learner orientation to the color scheme: which color marks the word, which marks the sentence

#### Constraints
- Poorly synchronized highlighting disrupts rather than supports tracking; even small audio-visual lag forces learners to re-locate their place [-M]
- Learners with strong decoding skills may find the visual motion distracting and comprehension may drop relative to silent reading [~W]
- Bimodal (simultaneous spoken + written) presentation can produce redundancy effects for fluent readers, adding load rather than reducing it [~S]
- Effectiveness drops with low-quality text, dense layout, or small displays where sentence boundaries are hard to see

#### Implementation Variability
- Word-only vs. word-plus-sentence highlighting; some tools offer phrase or paragraph units
- Adjustable color contrast, font size, and reading speed; karaoke-style (word) highlighting is common in early-literacy apps
- Can be combined with [Annotating](../principles/annotating.md) so learners mark text while it is read aloud

### Target Learners
- Struggling readers and learners with dyslexia, who benefit from bimodal input and reduced tracking demand [Bimodal reading with talking computers improves comprehension for less skilled readers.](https://doi.org/10.1177/002221949602900305) [+M]
- Beginning readers building print-to-sound mapping and left-to-right tracking
- Learners with attention difficulties, where the moving highlight anchors visual attention
- Less beneficial for fluent readers, for whom synchronized text and audio can be redundant [~M]

### Target Learning Goals
- Decoding and word recognition: linking spoken and written word forms
- Reading fluency: modeling pacing and phrase boundaries via sentence highlighting
- Comprehension: freeing working memory from tracking so capacity goes to meaning-making

### Instructions
1. Select digital text and open it in text-to-speech software with dual color highlighting enabled.
2. Configure the color scheme and reading speed with the learner; confirm the word highlight tracks the audio accurately.
3. Model one read-through, pointing out that the word color shows "where we are" and the sentence color shows "what we're in."
4. Have the learner read along with the audio, following the highlights ([Practice](../elements/practice.md)).
5. Re-read the passage without audio, then discuss comprehension to check that understanding, not just tracking, improved.

## Related Strategies
- [Chunking](../principles/chunking.md) — sentence-level highlighting groups text into meaningful units, the same principle applied to reading units
- [Annotating](../principles/annotating.md) — highlighting is a system-driven form of text marking; learner-driven marking complements it
- [Audiobooks](../principles/audiobooks.md) — dual color highlighting adds synchronized visual tracking to audio-only reading

## Examples
- **[Read&Write (Texthelp)](https://www.texthelp.com/products/readwrite/)** — toolbar for docs and web with configurable dual-color highlighting; widely used in K-12 special education and UDL implementations.
- **[ClaroRead](https://www.clarosoftware.com)** — word and sentence highlighting with adjustable colors and speaking rate across Word, PDF, and browser text.
- **[Voice Dream Reader](https://www.voicedream.com)** — mobile reader offering karaoke-style word highlighting plus sentence highlighting for accessible reading.
- **[Learning Ally](https://learningally.org)** — audiobook platform for students with reading disabilities that synchronizes highlighted text with human-recorded audio.

## Key Sources
- Montali, J., & Lewandowski, L. (1996). Bimodal reading: Benefits of a talking computer for average and less skilled readers. *Journal of Learning Disabilities, 29*(3), 271–279. [doi:10.1177/002221949602900305](https://doi.org/10.1177/002221949602900305)
- Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)
- Takacs, Z. K., Swart, E. K., & Bus, A. G. (2015). Transfer and retention of transfer of multimedia features in multimedia learning. *Review of Educational Research, 85*(4), 581–620. [doi:10.3102/0034654314566171](https://doi.org/10.3102/0034654314566171)
- Paivio, A. (1986). *Mental Representations: A Dual Coding Approach*. Oxford University Press.