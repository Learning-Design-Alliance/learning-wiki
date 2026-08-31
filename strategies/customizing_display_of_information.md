---
type: strategy
title: Customizing Display of Information
description: Customizing the display of information involves modifying the appearance of digital content to reduce reading effort and improve comprehension.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Customizing Display of Information

> **Strategy** · [All strategies](index.md)

## Description
Customizing the display of information means modifying how digital content appears — text size, font, line spacing, margins, color themes, and justification — to reduce reading effort and improve comprehension. Browser reading modes and e-reading apps strip away page clutter and let each reader tailor the visual presentation to their own needs, rather than forcing every learner through an identical interface.

## Design Implications

Reading is a visual task constrained by working memory; poorly formatted displays (long line lengths, tight spacing, justified text with uneven word gaps, decorative clutter) impose extraneous load that competes with comprehension [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [+M]. Customization shifts control of that load to the learner, which is especially valuable when visual processing demands vary widely across readers. The goal is not aesthetic preference but reducing the perceptual and parsing effort between the eye and the meaning.

### Context
#### Requirements
- Digital text in a reflowable, customizable format (HTML, EPUB) rather than fixed layout
- A reader or app exposing display controls (font, size, spacing, theme, margins)
- Guidance on *which* settings help, since learners rarely discover optimal configurations on their own

#### Constraints
- Fixed-layout formats (PDF, scanned images) resist resizing and reflowing, making customization impossible [-M]
- Over-customization can create new problems: exotic fonts, high-contrast color schemes, or frequent layout changes add visual novelty that must be processed [Decorative illustrations do not improve learning.](../claims/decorative-illustrations-do-not-improve-learning.md) [~M]
- Effects on comprehension for typically developing readers are modest; the strongest benefits accrue to readers with specific visual or decoding difficulties [~M]
- Customization options vary across platforms, so instructions tied to one tool may not transfer

#### Implementation Variability
- Reader modes (Safari Reader, Immersive Reader) apply curated defaults; full control (e-readers, browser extensions) lets users tune each parameter
- Can be learner-initiated (teaching students to adjust their own settings) or instructor-initiated (publishing accessible, reflowable course materials)
- Pairs with content-side simplification: [Chunking](../principles/chunking.md) and [Clear Structure](../principles/clear-structure-presentation.md) address the same extraneous-load problem at the content level

### Target Learners
- Readers with dyslexia, low vision, or visual processing difficulties, who benefit most from adjustable font, spacing, and contrast [~M]
- Learners with attention deficits, for whom distraction-free reading views reduce competing stimuli
- All readers benefit from reflowable text on small screens; effects are smaller for proficient readers of standard displays

### Target Learning Goals
- Improving reading fluency and endurance for text-heavy learning goals
- Reducing extraneous cognitive load so working memory is available for the content itself [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]
- Accessibility and equitable access to the same content across diverse learners

### Instructions
1. Ensure source content is in a reflowable format (HTML or EPUB), not fixed PDF
2. Teach learners to locate display controls in their reading tool (font, size, spacing, theme, margins)
3. Recommend evidence-informed starting points: larger sans-serif fonts, generous line spacing, left-aligned (not justified) text, moderate line length
4. Use a distraction-free reading mode to strip ads and navigation clutter
5. Encourage learners to treat settings as personal and adjustable per task — pair with [Accommodations](../elements/accommodations.md) where a formal need exists

## Related Strategies
- Chunking and segmenting content — the content-side complement to display-side customization; both reduce extraneous load
- Providing accessible source formats — customization is only possible when materials are published reflowably

## Related Elements
- [Chunking](../principles/chunking.md) — breaking content into digestible units; display customization controls how those units are visually presented
- [Accommodations](../elements/accommodations.md) — display customization is a low-cost, universally available accommodation for documented reading needs
- [Advance Organizers](../elements/advance-organizers.md) — structural cues that survive reflow and help readers navigate customized layouts

## Examples
- **[Microsoft Immersive Reader](https://www.microsoft.com/en-us/learning-tools/immersive-reader)** — built into Edge, Word, and Teams; adjustable text size, spacing, syllable highlighting, and line focus for readers with dyslexia.
- **Safari Reader / Firefox Reader View** — one-click stripping of page clutter with font and theme controls.
- **[CAST Clusive](https://clusive.cast.org)** — a free reader from CAST's Center on Inclusive Software for Learning that lets students adjust text display and scaffolds strategy use.
- **Kindle and Apple Books** — font, spacing, margin, and justification controls on reflowable EPUB content.

## Key Sources
- Rello, L., & Baeza-Yates, R. (2013). Good fonts for dyslexia. *Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '13)*. [doi:10.1145/2513383.2513447](https://doi.org/10.1145/2513383.2513447)
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Sweller, J., Ayres, P., & Kalyuga, S. (2011). *Cognitive Load Theory*. Springer. [doi:10.1007/978-1-4419-8126-4](https://doi.org/10.1007/978-1-4419-8126-4)
- Mayer, R. E. (2009). *Multimedia Learning* (2nd ed.). Cambridge University Press. [doi:10.1017/CBO9780511811678](https://doi.org/10.1017/CBO9780511811678)