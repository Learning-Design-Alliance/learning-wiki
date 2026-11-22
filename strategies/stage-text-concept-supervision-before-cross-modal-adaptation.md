---
type: strategy
id: stage-text-concept-supervision-before-cross-modal-adaptation
title: Stage educational-text concept supervision before cross-modal adaptation when adapting retrieval models to abstract curriculum queries
description: "A staged adaptation recipe for instructional retrieval systems: first structure the language space with example-concept pairs from educational texts (textbooks, teachers' handbooks), then transfer that concept-aware g..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: haiming-zhao-2026
    resource: "https://arxiv.org/abs/2610.00973"
    title: "Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. https://arxiv.org/abs/2610.00973"
    author: Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li
---

# Stage educational-text concept supervision before cross-modal adaptation when adapting retrieval models to abstract curriculum queries

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
A staged adaptation recipe for instructional retrieval systems: first structure the language space with example-concept pairs from educational texts (textbooks, teachers' handbooks), then transfer that concept-aware geometry to the visual domain with the visual encoder frozen, and only then jointly fine-tune both encoders with sparse visual concept supervision and textual replay. The article's ablations support the ordering: 'simply squeezing the description of a phenomenon and its conveyed concept into one single text item in a text-image pair is not the most effective,' and removing Stage 1 drops MAP@10 from 0.3848 to 0.2974.

## Design Implications

### Context
#### Requirements
- Access to educational texts supplying example-concept pairs; a sparse set of documentary segment-concept annotations; a pretrained two-tower vision-language model
#### Constraints
- The article motivates freezing the visual backbone in Stage 2 by cited evidence of severe gradient conflicts between vision and text under joint training; direct fine-tuning on sparse video-concept pairs alone 'provides little structure for why diverse visual segments and textual examples instantiate the same principle'

### Target Learners
- teachers searching science documentaries for instructional clips

### Target Learning Goals
- retrieving concrete visual examples of abstract curriculum concepts

### Affordances
- Concepts As Semantic Anchors Cdda

## Claims

- [CDDA achieves stronger pedagogically oriented concept retrieval than open or trainable multimodal baselines on a middle-school physics documentary benchmark](../claims/cdda-outperforms-baselines-concept-retrieval.md) [+W]
- [Concept adaptation preserves concrete image-description matching while improving image-concept decisions](../claims/cdda-preserves-concrete-alignment.md) [+W]
- [Visually heterogeneous curriculum concepts benefit most from concept-level alignment: CDDA retrieves 5 of 6 Force segments where multimodal baselines retrieve at most 2](../claims/heterogeneous-concepts-benefit-concept-alignment.md) [+W]
- [Stage 1 textual concept structuring is the main source of CDDA's retrieval gains; removing it degrades all reported metrics](../claims/stage1-text-structuring-drives-gains.md) [+W]
- [Text-only retrieval over subtitles remains weak for concept-to-example retrieval, suggesting subtitles alone miss visually expressed teaching evidence](../claims/text-only-subtitle-retrieval-weak.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Haiming Zhao, Tai Wang, Kun Zhang, Xicheng Peng, Zhiyang Li. (2026). Concept Driven Domain Adaptation: Finding an Abstract Needle in a Haystack. arXiv preprint. https://arxiv.org/abs/2610.00973
