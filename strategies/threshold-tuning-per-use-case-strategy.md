---
type: strategy
id: threshold-tuning-per-use-case-strategy
title: Tune the mind wandering detection threshold to the deployment setting, and choose thresholds by use case (recall for research, precision for interventions)
description: The article recommends systematically testing classification thresholds (0.1 to 0.9) rather than defaulting to 0.5, especially when base rates differ between training and deployment datasets.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: bühler-2025
    resource: "https://doi.org/10.1007/s40593-024-00412-2"
    title: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2"
    author: "Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E"
---

# Tune the mind wandering detection threshold to the deployment setting, and choose thresholds by use case (recall for research, precision for interventions)

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends systematically testing classification thresholds (0.1 to 0.9) rather than defaulting to 0.5, especially when base rates differ between training and deployment datasets. It states that adjusting the threshold "depending on its application, can improve the effectiveness of these predictions, especially in cross-dataset prediction", favoring high recall for research on materials and high precision when interventions should not disturb attentive learners.

## Design Implications

### Context
#### Requirements
- Access to the model's probability outputs so cutoffs can be adjusted
- Knowledge of the deployment setting's mind wandering base rate
#### Constraints
- Focusing on F1 scores can lead to an imbalance between recall and precision of the mind wandering class

### Target Learners
- online learners in ITSs and MOOCs

### Target Learning Goals
- accurate detection of mind wandering to trigger targeted attentional interventions

## Claims

- [Optimizing the classification threshold improves cross-dataset mind wandering detection, raising person-level correlation from 0.48 to 0.8](../claims/threshold-optimization-improves-cross-dataset-detection.md) [+M]

## Related Strategies

- [Select the variant-generation prompting protocol by deployment threat profile: zero-shot or structured CoT for construct fidelity, few-shot or dimension-preserving generation for surface separation](threat-profile-keyed-generation-protocol.md)

## Examples
-

## Key Sources
- Bühler, B., Bozkir, E., Goldberg, P., Sümer, Ö., D'Mello, S., Gerjets, P., Trautwein, U., Kasneci, E. (2025). From the Lab to the Wild: Examining Generalizability of Video-based Mind Wandering Detection. Int J Artif Intell Educ 35, 823–857. https://doi.org/10.1007/s40593-024-00412-2
