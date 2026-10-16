---
type: design
id: blind-turing-test-legal-exam-evaluation-protocol
title: Blind Turing-test evaluation protocol for LLM legal exam papers
description: An evaluation design in which LLM-generated and human exam papers are formatted identically and anonymously assessed by expert examiners using official criteria.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: germana-bertoli-2025
    resource: "https://github.com/SSIGPRO/LLMs-in-legal-professions"
    title: "Germana Bertoli, Ilaria Amelia Caggiano, Francesca Lagioia, Riccardo Rovatti, Giovanni Sartor, Emiliano Troisi. (2025). What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries. https://github.com/SSIGPRO/LLMs-in-legal-professions"
    author: Germana Bertoli, Ilaria Amelia Caggiano, Francesca Lagioia, Riccardo Rovatti, Giovanni Sartor, Emiliano Troisi
---

# Blind Turing-test evaluation protocol for LLM legal exam papers

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
An evaluation design in which LLM-generated and human exam papers are formatted identically and anonymously assessed by expert examiners using official criteria. Three domain experts who had served on national board committees each evaluated five uniformly formatted papers with no indication of authorship. "we employed highly skilled professionals with direct experience in national boards as evaluators, through a 'Turing Test' approach, capturing qualitative nuances, often missed by automated metrics." The human benchmark was the highest-scoring candidate's real exam paper, digitised via OCR and manually verified.

## Design Implications

### Context
#### Requirements
- Expert evaluators with direct national-board examination experience
- Uniform formatting making LLM and human papers visually indistinguishable
- Official assessment grids from the Italian Ministry of Justice
#### Constraints
- Limited number of exam papers and a small pool of three expert evaluators, constraining statistical generalisation
- LLMs had internet access while human candidates were restricted to limited legal materials
- Situated within the Italian legal system

### Target Learners
- legal professional candidates
- AI-in-law researchers

### Learning Goals
- assessing LLM legal competence under authentic professional examination conditions

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Germana Bertoli, Ilaria Amelia Caggiano, Francesca Lagioia, Riccardo Rovatti, Giovanni Sartor, Emiliano Troisi. (2025). What out-of-the-box LLMs can(t) do in law? A Turing test in Italian exams for lawyers, judges and notaries. https://github.com/SSIGPRO/LLMs-in-legal-professions
