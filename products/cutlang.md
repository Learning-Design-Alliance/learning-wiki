---
type: product
id: cutlang
title: CutLang
description: CutLang is a domain-specific declarative language and interpreter for describing and running collider-physics analyses without writing or compiling analysis code.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
---

# CutLang

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
CutLang is a domain-specific declarative language and interpreter for describing and running collider-physics analyses without writing or compiling analysis code.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Analysis Description Language: decoupling physics content from technical operations in collider analyses**: An analysis description language is "a domain-speciﬁc and declarative language designed to describe the physics content of a collider analysis in a standard and unambiguous way". The concept addresses the problem that in general-purpose frameworks based on C++ or Python, physics content and technical operations are intertwined, making research involvement difficult for beginning students. When the physics algorithm description is fully separated from software frameworks, any framework capable of interpreting the language can perform the analysis. CutLang is the concrete realization of this idea used in the school. (A. Adıgüzel et al. (2021))
- **Use an analysis description language to lower the entry barrier so students with no prior programming experience can perform real data analyses**: The article concludes that using an Analysis Description Language "greatly lowers the barrier of entry, making actual data analysis accessible even to students with no prior programming experience". Because ADL syntax is simple, human-readable, and requires no code writing or compilation, introductory-level HEP data analysis becomes appropriate for undergraduates once computer and programming technicalities are surmounted. The authors also recommend integrating such an analysis into regular particle physics courses, as it offers a concrete task those courses sorely miss. (A. Adıgüzel et al. (2021))

### Claims
- [Student teams in the 2020 school reproduced assigned ATLAS and CMS analyses with CutLang, with 5 of 8 teams producing final discriminant histograms and 2 performing fits](../claims/cutlang-school-teams-reproduce-lhc-analyses.md) [+M]
- [Nine months after the school, most responding students reported comfort with key concepts and 87% agreed they could prepare a simple CutLang ADL file](../claims/cutlang-school-knowledge-retention-nine-months.md) [+M]
- [Instructors' oral evaluations at final presentations indicated junior and senior undergraduates could access HEP data analysis](../claims/cutlang-school-oral-evaluations-accessibility.md) [+W]

## Related Products and Programmes
-

## Key Sources
- A. Adıgüzel, O. Çakır, Ü. Kaya, V. E. Özcan, S. Öztürk, S. Sekmen, İ. Türk Çakır, G. Ünel. (2021). CutLang as an Analysis Description Language for Introducing Students to Analyses in Particle Physics. arXiv:2008.12034v2 [hep-ph]. https://arxiv.org/abs/2008.12034
