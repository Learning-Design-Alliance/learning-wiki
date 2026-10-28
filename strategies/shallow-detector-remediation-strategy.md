---
type: strategy
id: shallow-detector-remediation-strategy
title: Use shallow-learning detectors to route students to conceptual-grounding remediation and real-time metacognitive feedback
description: The article proposes two uses for a shallow-learning detector in remediation.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: gowda-2013
    resource: "https://doi.org/10.1007/s40593-013-0006-4"
    title: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4"
    author: "Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M"
---

# Use shallow-learning detectors to route students to conceptual-grounding remediation and real-time metacognitive feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article proposes two uses for a shallow-learning detector in remediation. First, identified students "can be tracked towards activities that improve their conceptual grounding, perhaps then returning to procedural practice to solidify the conceptual gains made". Second, the software can respond to specific behaviors in real time: "if a student fails to pause and self-explain after seeking a hint, the software can provide meta-cognitive feedback on that decision". A gaming student can be given exercises covering material bypassed by gaming, asked to reflect on why the answer is correct, or given an explanation.

## Design Implications

### Context
#### Requirements
- A validated detector of shallow learning integrated into the learning software, plus interventions shown to help students acquire robust learning
#### Constraints
- Traditional student modeling methods fail to provide remediation to these students because they have mastered the tutor's skills; building this remediation into the Genetics Tutor is described as future work

### Target Learners
- students in intelligent tutoring systems who have mastered tutor skills but lack robust learning

### Target Learning Goals
- building conceptual understanding on top of procedural skill; supporting transfer and preparation for future learning

### Affordances
- Shallow Learning Operational Definition

## Claims

- [K* models outperform step regression for detecting transfer-shallowness, with no-interactions and interaction models each best on different metrics](../claims/kstar-beats-step-regression-transfer-shallow.md) [+W]
- [K* detectors identify no-PFL-shallow learners with cross-validated A′ of 0.790 and kappa 0.55](../claims/kstar-detects-no-pfl-shallow-learning.md) [+W]
- [K* detectors identify no-transfer-shallow learners at student-level cross-validated A′ of 0.766–0.791](../claims/kstar-detects-no-transfer-shallow-learning.md) [+W]
- [Shallowness detectors transfer between the transfer-shallow and PFL-shallow constructs with minimal A′ degradation](../claims/shallow-detectors-portable-across-constructs.md) [+W]
- [Shallow learners show slower responses and higher certainty of slip, suggesting struggle rather than fast guessing](../claims/shallow-learners-slow-struggling-not-guessing.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Gowda, S. M., Baker, R. S., Corbett, A. T., & Rossi, L. M. (2013). Towards Automatically Detecting Whether Student Learning is Shallow. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-013-0006-4
