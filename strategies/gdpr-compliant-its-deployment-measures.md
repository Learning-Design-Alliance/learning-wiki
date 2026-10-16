---
type: strategy
id: gdpr-compliant-its-deployment-measures
title: Privacy-preserving deployment measures for an ITS under GDPR and EU AI Act
description: "To operate the ITS in a German university regulatory environment, the authors implemented layered privacy measures: strict separation of IP address logs from the ITS, pseudonymous usernames, no e-mail storage beyond r..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: alina-deriyeva-2025
    resource: "https://doi.org/10.1007/978-3-031-99261-2_16"
    title: "Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen. (2025). SCRIPT: Implementing an Intelligent Tutoring System for Programming in a German University Context. Artificial Intelligence in Education (Springer). https://doi.org/10.1007/978-3-031-99261-2_16"
    author: Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen
---

# Privacy-preserving deployment measures for an ITS under GDPR and EU AI Act

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To operate the ITS in a German university regulatory environment, the authors implemented layered privacy measures: strict separation of IP address logs from the ITS, pseudonymous usernames, no e-mail storage beyond registration, voluntary (non-mandatory) use, explicit fine-grained consent for keystroke-level research data recording, teacher exclusion from servers until after anonymization and grade finalization, and self-hosting of an LLama-70b model instead of commercial LLM interfaces to prepare for the EU AI Act.

## Design Implications

### Context
#### Requirements
- Explicit consent acquisition for research data recording
- Self-hosted or partner-hosted open-weight language models rather than commercial LLM interfaces
- Manual anonymization of data and finalized grades before teacher access to servers
#### Constraints
- Strict data privacy meant mandatory task submissions could not be implemented, so use had to remain entirely voluntary
- The precise implications of the EU AI Act for AI in education are not yet fully clear
- Fine-grained consent acquisition is described as a research topic in itself that is far from resolved

### Target Learners
- University students in EU/German higher education contexts

### Target Learning Goals
- Programming skill practice with legally and ethically compliant data handling

## Related Strategies

- [LA researchers and practitioners should adapt to changing regulations across jurisdictions, use regulatory sandboxes, and carefully consider data nature and privacy risks before cross-border data transfer](adapt-to-cross-jurisdiction-ai-regulation-sandboxes.md)
- [Four-step anonymization balancing disclosure risk and data utility](four-step-anonymization-engagement-data.md)
- [Secure enclaves for privacy-protecting researcher access to student-level data](secure-enclave-kinetic-data-access.md)

## Examples
-

## Key Sources
- Alina Deriyeva, Jesper Dannath, and Benjamin Paaßen. (2025). SCRIPT: Implementing an Intelligent Tutoring System for Programming in a German University Context. Artificial Intelligence in Education (Springer). https://doi.org/10.1007/978-3-031-99261-2_16
