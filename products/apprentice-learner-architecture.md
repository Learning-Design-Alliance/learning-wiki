---
type: product
id: apprentice-learner-architecture
title: Apprentice Learner Architecture
description: A domain-general architecture and authoring framework by MacLellan and Koedinger for creating teachable-agent tutors with learner models that can be trained across diverse instructional domains.
product_kind: framework
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
---

# Apprentice Learner Architecture

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A domain-general architecture and authoring framework by MacLellan and Koedinger for creating teachable-agent tutors with learner models that can be trained across diverse instructional domains.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Apprentice Learner Architecture for domain-general tutor authoring (MacLellan & Koedinger)**: One of the four accepted special-issue papers. MacLellan and Koedinger "offer a more technical and generalized treatment of the teachable agent approach using their Apprentice Learner Architecture", covering "diverse tutoring domains including fraction arithmetic, learning chinese characters, correct a/an/the usage, block tower stability, rule induction, stoichiometry, and equations". The editorial places it with Matsuda's work as adaptive authoring of adaptive content. (Andrew M. Olney et al. (2021))
- **Decision Tree model: a non-incremental apprentice learner model within the Apprentice Learner Architecture**: The Decision Tree model is one of two apprentice learner models built within the Apprentice Learner Architecture. It uses a non-incremental decision tree learner for when-learning, meaning it reprocesses all experienced training examples each time it updates its learned classifier. Like the Trestle model, it draws on the same small set of prior knowledge (six operators and three types of relational knowledge) to support expert model authoring. The model was used to author a novel experimental design tutor and evaluated across seven additional tutoring domains. (Christopher J. MacLellan et al. (2022))
- **Trestle model: an incremental apprentice learner model within the Apprentice Learner Architecture**: The Trestle model is the second apprentice learner model built within the Apprentice Learner Architecture. It uses Trestle, an incremental concept learning algorithm based on psychological studies of how humans learn concepts, for when-learning. Incremental algorithms efficiently update their classification tree in response to each new datum without reprocessing all previous training examples. Like the Decision Tree model, it draws on the same small set of prior knowledge (six operators and three types of relational knowledge). (Christopher J. MacLellan et al. (2022))
- **Apprentice learner models enable non-programmers to author tutors for complex domains where existing approaches struggle**: Apprentice learner models provide a means for non-programmers to build expert models by training computational agents through demonstrations and feedback, similar to how human apprentices learn. Domain experts train models by providing examples and feedback, and these models translate instruction into expert models that can power tutoring systems. This approach generalizes from training, unlike Example-Tracing which does not perform any generalization, making it viable for domains where demonstrating all correct solutions is impractical. (Christopher J. MacLellan et al. (2022))

### Claims
- [Apprentice learner models support efficient tutor authoring, more efficient than Example-Tracing with mass production](../claims/apprentice-learner-models-efficient-authoring.md) [+M]
- [Apprentice learner models are domain-general: they learn expert models across eight tutor domains without specialized domain knowledge](../claims/apprentice-learner-models-domain-general.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Andrew M. Olney, Stephen B. Gilbert, Kelly Rivers. (2021). Preface to the Special Issue on Creating and Improving Adaptive Learning: Smart Authoring Tools and Processes. International Journal of Artificial Intelligence in Education (2022) 32:1–3. https://doi.org/10.1007/s40593-021-00277-9
- Christopher J. MacLellan & Kenneth R. Koedinger. (2022). Domain-General Tutor Authoring with Apprentice Learner Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00214-2
