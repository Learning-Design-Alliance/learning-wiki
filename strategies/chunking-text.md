---
type: strategy
id: chunking-text
title: Chunking Text
description: Breaking continuous text into smaller, meaningfully organized units so working memory can process each unit before integrating them.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Chunking Text

> **Strategy** · [All strategies](index.md)

## Description
Chunking text means dividing continuous prose into smaller, coherent units — short paragraphs, headed sections, bulleted sequences, or step-by-step segments — so that each unit can be held and processed in working memory before being integrated into a larger understanding. Effective chunking is not arbitrary truncation: units are organized around meaning (one idea per segment), often signaled with headings, whitespace, or numbering, so learners can reconstruct the whole from the parts.

## Design Implications

Chunking works because working memory can hold only a small number of meaningful units at once; grouping information into larger, well-organized chunks reduces the load imposed by the same content [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]. The critical design decision is where boundaries fall — chunks should align with the conceptual structure of the material, not arbitrary length limits, or learners must spend effort reassembling fragments [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Headings and advance signals between chunks act as retrieval cues that support integration ([Advance Organizers](../elements/advance-organizers.md)).

### Context
#### Requirements
- Analysis of the text's conceptual structure so chunk boundaries match idea boundaries
- Signaling between chunks — headings, transitions, or numbered steps — that makes the overall structure visible ([Clear Structure Presentation](../principles/clear-structure-presentation.md))
- A way for learners to see the whole (an overview, map, or summary) so chunks are integrated, not encountered as disconnected fragments

#### Constraints
- Over-fragmentation destroys coherence: chopping text into tiny pieces forces learners to reconstruct relationships the original prose made explicit, increasing rather than reducing load [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [-M]
- Chunks presented without structural signaling can be encoded as isolated facts, harming integration and transfer [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~M]
- For skilled readers with high prior knowledge, heavy chunking can slow reading and feel patronizing; the benefit shrinks as expertise grows [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~W]

#### Implementation Variability
- **Segmented video and text**: pause points every 1–3 minutes with recall prompts, as in segmented instructional video research
- **Progressive disclosure**: reveal chunks on demand (accordion sections, "continue" buttons) so learners control pacing
- **Structural chunking**: reorganize rather than merely divide — convert dense prose into headed sections, tables, or numbered procedures ([Procedural Information](../elements/procedural-information.md))
- **Learner-generated chunking**: students mark their own segment boundaries while reading ([Annotating](../principles/annotating.md)), which builds structure awareness

### Target Learners
- Novices and readers with limited background knowledge, who lack the schemas to compress long passages into few chunks [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]
- Learners with working memory constraints or processing-speed challenges, for whom segment length is the binding factor
- Less necessary for expert readers, who chunk spontaneously using domain schemas [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [~W]

### Target Learning Goals
- Comprehension of complex expository or procedural text
- Retention of multi-step procedures and sequences
- Building accurate mental models of text structure ([Advance Organizers](../elements/advance-organizers.md))

### Instructions
1. Map the text's core ideas and their relationships before deciding on boundaries.
2. Divide the text so each chunk expresses one complete idea or one step, sized to be processed in a single reading pass.
3. Add a heading or signal to each chunk that states its role in the whole ([Clear Structure Presentation](../principles/clear-structure-presentation.md)).
4. Provide an overview or advance organizer showing how chunks fit together ([Advance Organizers](../elements/advance-organizers.md)).
5. Insert a brief activity between chunks — a recall prompt, question, or application task ([Practice](../elements/practice.md)) — to consolidate each unit before loading the next.
6. Fade chunking as learners gain expertise: move toward longer, denser passages so they develop independent text-handling stamina.

## Related Strategies
- [Segmenting](segmenting.md) — the multimedia analogue: breaking continuous animation or audio into learner-paced segments
- [Pre-reading Strategies](pre-reading_strategies.md) — chunking pairs with front-loading structure before reading begins
- [Text Marking](text_marking.md) — learners can chunk actively by marking boundaries and labeling sections themselves

## Examples
- **[Khan Academy](https://www.khanacademy.org)** — articles and transcripts are broken into short headed sections with inline practice between segments.
- **Duolingo** — lessons present target language in small chunked units of 3–5 items, sequenced so each unit builds on the last.
- **OpenStax textbooks** (e.g., *Psychology 2e*, https://openstax.org) — chapters divided into short modules with learning objectives, headings, and end-of-section review questions that close each chunk.

## Key Sources
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review, 63*(2), 81–97. [doi:10.1037/h0043158](https://doi.org/10.1037/h0043158)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296. [doi:10.1023/A:1022193728205](https://doi.org/10.1023/A:1022193728205)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Gobet, F., Lane, P. C. R., Croker, S., Cheng, P. C.-H., Jones, G., Oliver, I., & Pine, J. M. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences, 5*(6), 236–243. [doi:10.1007/978-1-4419-1428-6_1731)01662-4](https://doi.org/10.1007/978-1-4419-1428-6_1731)01662-4)