---
type: design
id: acer-curriculum-schedule-taxonomy
title: "Four curriculum schedules for incorporating synthetic book corpora into continual pretraining: Flat, Cognitive, Cognitive+Content, and Interleaved"
description: "The article experiments with \"four curriculum schedules for incorporating synthetic book corpus into continual pretraining\": Flat (all books, easy QA, and hard QA presented together without ordering), Cognitive (books..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: nishit-neema-2025
    resource: "https://arxiv.org/abs/2510.26336"
    title: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. https://arxiv.org/abs/2510.26336"
    author: "Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh"
---

# Four curriculum schedules for incorporating synthetic book corpora into continual pretraining: Flat, Cognitive, Cognitive+Content, and Interleaved

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article experiments with "four curriculum schedules for incorporating synthetic book corpus into continual pretraining": Flat (all books, easy QA, and hard QA presented together without ordering), Cognitive (books then easy QA then hard QA, with domains and personas mixed randomly within stages), Cognitive+Content (which "extends the cognitive schedule by introducing content-based ordering: High school, Undergraduate, Graduate, Researcher"), and Interleaved (chapter-section-level interleaving across domains while preserving persona order within each category). This taxonomy aligns learning along both a cognitive-difficulty dimension and a content/persona dimension, and the schedules are ablated against a Flat baseline to test whether structured ordering improves domain knowledge infusion.

## Design Implications

### Context
#### Requirements
- A synthetic corpus divided into books, easy QA, and hard QA subsets, generated across multiple persona levels
- A general replay data source mixed with the in-domain corpus
#### Constraints
- The Interleaved schedule underperformed in this continual-pretraining setting, with large drops in mathematics and statistics

### Target Learners
- Large language models undergoing continual pretraining

### Learning Goals
- Progressive acquisition of domain knowledge along cognitive difficulty and audience-level dimensions

### Claims
- [Cogcon Best Interleaved Underperforms](../claims/cogcon-best-interleaved-underperforms.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. https://arxiv.org/abs/2510.26336
