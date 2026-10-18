---
type: strategy
id: infstm-catchall-default-code-strategy
title: Use a default catch-all code (InfStm?) to flag uncodable messages for manual checking
description: When the DAC filter finds no discourse marker in a message, it assigns the InfStm?
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
sources:
  - id: erkens-2008
    resource: "https://doi.org/10.1007/s11412-008-9052-6"
    title: "Erkens, G., & Janssen, J. (2008). Automatic coding of dialogue acts in collaboration protocols. Computer-Supported Collaborative Learning, 3, 447-470. https://doi.org/10.1007/s11412-008-9052-6"
    author: "Erkens, G., & Janssen, J"
---

# Use a default catch-all code (InfStm?) to flag uncodable messages for manual checking

## Description
When the DAC filter finds no discourse marker in a message, it assigns the InfStm? code as a default catch-all, marking the message for manual checking rather than risking a wrong automatic code. The article states "If the system does not find a discourse marker in a message, the message is coded by the label InfStm? as a default catch-all." This means "the researcher still has to check and code some parts of the protocol (about 10%)", but the job is simplified because large parts are already coded and uncoded parts are easy to find.

## Design Implications

### Context
#### Requirements
- A researcher must review and manually code the flagged InfStm? messages after automatic coding
#### Constraints
- The catch-all does not guarantee the DAC filter makes no other mistakes; disagreements not flagged as InfStm? remain unnoticed unless the protocol is checked

### Target Learners
- researchers coding collaboration protocols from CSCL studies

### Target Learning Goals
- reliable and efficient coding of communicative functions in collaboration protocols

## Related Strategies
- 

## Examples
-

## Key Sources
- Erkens, G., & Janssen, J. (2008). Automatic coding of dialogue acts in collaboration protocols. Computer-Supported Collaborative Learning, 3, 447-470. https://doi.org/10.1007/s11412-008-9052-6
