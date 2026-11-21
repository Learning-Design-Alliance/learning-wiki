---
type: strategy
id: human-ai-complementarity-cps-labelling
title: Use AI models to auto-label semantically clearer CPS classes and leave complex labelling decisions to human experts
description: "The article proposes designing CPS diagnosis systems around human-AI complementarity, whereby \"classes that are semantically clearer than other classes are leveraging AI models for automated labelling and leave comple..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: kester-wong-2025
    resource: "https://arxiv.org/abs/2504.15093"
    title: "Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. https://arxiv.org/abs/2504.15093"
    author: Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova
---

# Use AI models to auto-label semantically clearer CPS classes and leave complex labelling decisions to human experts

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The article proposes designing CPS diagnosis systems around human-AI complementarity, whereby "classes that are semantically clearer than other classes are leveraging AI models for automated labelling and leave complex labelling decisions to human experts". This is motivated by the finding that several subskill and affect classes were well detected while other classes resisted even the best models, so a hybrid division of labelling labour can enhance productivity in CPS diagnosis.

## Design Implications

### Context
#### Requirements
- Automated labelling is applied to classes the article describes as semantically clearer than other classes, with complex labelling decisions reserved for human experts
#### Constraints
- The others were too complex for even the best models to detect

### Target Learners
- teachers and researchers coding CPS utterances of secondary school students

### Target Learning Goals
- accurate labelling of collaborative problem solving indicators and affect states

## Claims

- [Models made few or no predictions on underrepresented social-cognitive classes, though AudiBERT improved classification of the sparse AS3 affect state](../claims/audibert-improves-sparse-as3-classification.md) [+W]
- [AudiBERT improved classification of five specific social-cognitive CPS classes: SS1 sense-making, SS3 formulating a solution, SS5 reaching a solution, SS6 maintaining roles and responsibilities, and SC1 using scripting](../claims/audibert-improves-specific-social-cognitive-classes.md) [+W]
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](../claims/human-llm-agreement-gap-jaccard.md) [+W]

## Related Strategies

- [Design human-LLM collaborative systems in which LLMs assist diagnostic reasoning while human experts oversee complex decisions](human-llm-collaborative-diagnostic-reasoning-strategy.md)

## Examples
-

## Key Sources
- Kester Wong, Bin Wu, Sahan Bulathwela, and Mutlu Cukurova. (2025). Rethinking the Potential of Multimodality in Collaborative Problem Solving Diagnosis with Large Language Models. Proceedings of the 26th International Conference on Artificial Intelligence in Education. https://arxiv.org/abs/2504.15093
