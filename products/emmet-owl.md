---
type: product
id: emmet-owl
title: EMMeT-OWL
description: "EMMeT-OWL is an OWL-encoded clinical knowledge base translated from Elsevier's Merged Medical Taxonomy and used by EMCQG to generate medical assessment questions."
product_kind: dataset
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# EMMeT-OWL

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
EMMeT-OWL is an OWL-encoded clinical knowledge base translated from Elsevier's Merged Medical Taxonomy and used by EMCQG to generate medical assessment questions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Mapping ontology rule consequent types onto Wh-type stem types (odd-one-out, T/F, synonym, definition, one-word)**: Each DL or SWRL rule is first transformed into an Instance Tree (ITree); traversal then selects a stem template based on the consequent's variable type. The article specifies, for example, that "If the consequent is a 'Type variable', then the odd one out question stem generated is 'Which among the following is not a 'Type Variable'?'", while a 'theEquivalentNameOf' antecedent yields a synonym stem, a single property/class antecedent yields a definition stem, and multiple class variables yield a one-word stem. This pattern makes the ontology's rule structure directly determine which cognitive-level stem type is produced. (Praveen Kumar et al. (2024))

### Claims
- [EMCQG generated more than 3 million distinct case-based questions for four physician specialities from the EMMeT ontology](../claims/emcqg-three-million-questions-four-specialities.md) [+W]

## Related Products and Programmes
-

## Key Sources
- J. Leo, G. Kurdi, N. Matentzoglu, B. Parsia, U. Sattler, S. Forge, G. Donato, W. Dowling. (2019). Ontology-Based Generation of Medical, Multi-term MCQs. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-018-00172-w
- Praveen Kumar, A., Nayak, A., Shenoy K., M., Chaitanya, & Ghosh, K. (2024). A Novel Framework for the Generation of Multiple Choice Question Stems Using Semantic and Machine-Learning Techniques. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00333-6
