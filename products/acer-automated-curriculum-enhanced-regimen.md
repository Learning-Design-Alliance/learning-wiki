---
type: product
id: acer-automated-curriculum-enhanced-regimen
title: ACER (Automated Curriculum-Enhanced Regimen)
description: A multi-stage pipeline proposed by Nishit Neema et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
---

# ACER (Automated Curriculum-Enhanced Regimen)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A multi-stage pipeline proposed by Nishit Neema et al. for generating curriculum-aligned synthetic textbook corpora and Bloom-guided question–answer pairs to infuse domain knowledge into continually pretrained large language models.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ACER: a multi-stage pipeline for synthesizing curriculum-aligned textbook corpora and Bloom's-taxonomy-guided QA pairs for domain knowledge infusion**: ACER (Automated Curriculum-Enhanced Regimen) is "a multi-stage pipeline designed to transform high-level learning goals into a structured synthetic training corpus". It proceeds through domain detailing (domain name, intent, and target-audience metadata yielding a domain description, core subtopics, and 6-8 key questions aligned with Bloom's taxonomy), outline generation of a hierarchical table of contents, section-level synthetic textbook content generation, and two-stage QA generation whose difficulty "gradually escalates, following a cognitive progression from comprehension to interpretation, analysis, and application". Four persona versions (high school, undergraduate, graduate, researcher) of each textbook encode educational progression. (Nishit Neema et al. (2025))

### Claims
- [The Cog+Con curriculum schedule (cognitive plus persona-based content ordering) achieves the best target-domain results, while the Interleaved schedule underperforms the other schedules](../claims/cogcon-best-interleaved-underperforms.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Nishit Neema, Srinjoy Mukherjee, Sapan Shah, Gokul Ramakrishnan & Ganesh Venkatesh. (2025). From Amateur to Master: Infusing Knowledge into LLMs via Automated Curriculum Learning. arXiv preprint. https://arxiv.org/abs/2510.26336
