---
type: design
id: buk-content-qa-units
title: "Basic Units of Knowledge (BUKs): Content and Q&A lesson building blocks"
description: BUKs are the atomic chunks of knowledge delivered in lessons, each referring to a single Medical_Concept via the refers_to_concept property.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-08
sources:
  - id: michalowski-martin-2021
    resource: "https://doi.org/10.3390/ijerph18147355"
    title: "Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor. (2021). A Health eLearning Ontology and Procedural Reasoning Approach for Developing Personalized Courses to Teach Patients about Their Medical Condition and Treatment. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph18147355"
    author: "Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor"
---

# Basic Units of Knowledge (BUKs): Content and Q&A lesson building blocks

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
BUKs are the atomic chunks of knowledge delivered in lessons, each referring to a single Medical_Concept via the refers_to_concept property. The article defines two types: "The first is a Content BUK, which delivers definitions of clinical concepts using different modalities. The second is a Q&A (Question and Answer) BUK, which is delivered in the form of multiple-choice questions." BUKs carry properties for VARK learning style, required comprehension level (low, medium, or high), and a simplified two-level Bloom taxonomy, and are specialized by themes such as dosage, side effects, and diet restrictions.

## Design Implications

### Context
#### Requirements
- BUKs are fixed and need to be developed in advance for different comprehension levels
#### Constraints
- Q&A BUKs are available only in A or R modes, while Content BUKs can be presented in any of the VARK modes

### Target Learners
- patients with varying comprehension levels and VARK learning styles

### Learning Goals
- condition and treatment knowledge at lower-order and higher-order Bloom levels

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Michalowski Martin, Wilk Szymon, Michalowski Wojtek, O'Sullivan Dympna, Bonaccio Silvia, Parimbelli Enea, Carrier Marc, Le Gal Grégoire, Kingwell Stephen, Peleg Mor. (2021). A Health eLearning Ontology and Procedural Reasoning Approach for Developing Personalized Courses to Teach Patients about Their Medical Condition and Treatment. International Journal of Environmental Research and Public Health. https://doi.org/10.3390/ijerph18147355
