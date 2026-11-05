---
type: strategy
id: pre-segment-and-pre-feed-domain-materials-strategy
title: Pre-segment domain materials at moderate granularity and pre-feed them to LLMs to reduce cognitive load and improve answer accuracy
description: A fine-tuning-free teaching strategy in which educators divide lengthy specialised materials into moderate-sized text segments and supply them to a chatbot before questioning.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: lei-yung-hsu-2025
    resource: "https://doi.org/10.1080/10872981.2025.2602788"
    title: "Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788"
    author: Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju
---

# Pre-segment domain materials at moderate granularity and pre-feed them to LLMs to reduce cognitive load and improve answer accuracy

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 3 studies (2 causal, 1 review), `q2`–`q3` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
A fine-tuning-free teaching strategy in which educators divide lengthy specialised materials into moderate-sized text segments and supply them to a chatbot before questioning. The authors recommend that "educators can pre-segment domain materials and 'pre-feed' structured content to models like ChatGPT to reduce cognitive load, and yield more accurate responses". They stress the recommendation is procedural, not numerical: segment at moderate granularity, then tune segment length on the target task.

## Design Implications

### Context
#### Requirements
- Access to a chatbot interface accepting file uploads; materials must exist as text; segment length should be tuned on the target task
#### Constraints
- Tested only on plastic surgery questions from a single textbook with token lengths between 4,000 and 20,000; cannot process image-based or graphical information

### Target Learners
- medical trainees in specialised fields
- educators and clinicians without advanced technical skills

### Target Learning Goals
- accurate AI-assisted answering of specialised domain questions
- scalable access to domain-specific feedback

### Affordances
- [Clt Analogy For Llm Attention Limits](../theories/cognitive-load-theory.md)

## Claims

- [Under 6,000-token segmentation, GPT-4.1 accuracy did not differ significantly across Bloom's taxonomy cognitive levels](../claims/no-bloom-level-accuracy-differences-under-token-splitting.md) [~W]
- [6,000-token segmentation outperformed both larger 20,000-token segments and unsegmented full-chapter input on specialised exam accuracy](../claims/six-thousand-token-segments-outperform-large-and-full-chapter-inputs.md) [+W]
- [Segmenting domain content into moderate token chunks significantly improves GPT-4.1 accuracy on specialised medical board questions compared with no prior content input](../claims/token-splitting-improves-gpt41-specialised-exam-accuracy.md) [+W]
- [Segmentation Benefits Shrink With Expertise](../claims/segmentation-benefits-shrink-with-expertise.md) [~W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Lei Yung-Hsu, Chen Chien-Chung, Shen Ching-Ju. (2025). Token-splitting improves GPT-4.1 performance on plastic surgery exams: implications for AI-Assisted medical education. Medical Education Online. https://doi.org/10.1080/10872981.2025.2602788
