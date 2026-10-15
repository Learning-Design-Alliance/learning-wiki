---
type: design
id: hybrid-query-resolution-platform-internship-onboarding
title: Hybrid query-resolution platform routing queries across AI assistant, peer layer, curated FAQ corpus and administrator escalation
description: "A deployed support platform for a large online internship programme that routes each raised query across four paths: an AI chatbot answering only from a curated FAQ corpus, a peer layer where any participant may answe..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: gupta-2026
    resource: "https://arxiv.org/abs/2609.38967"
    title: "Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967"
    author: Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S
---

# Hybrid query-resolution platform routing queries across AI assistant, peer layer, curated FAQ corpus and administrator escalation

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
A deployed support platform for a large online internship programme that routes each raised query across four paths: an AI chatbot answering only from a curated FAQ corpus, a peer layer where any participant may answer, administrator handling, and a scripted facility. The article states that "The platform routes a raised query first to the AI chatbot, which answers only from a curated corpus of verified FAQ entries, a deliberate restriction that prevents unverified procedural guidance". Peer answers pass through administrator acceptance and senior-administrator final approval before release, and the corpus was revised daily so rule or schedule changes were reflected the same day.

## Design Implications

### Context
#### Requirements
- A curated corpus of verified FAQ entries that is revised daily so procedural changes are reflected the same day
- Administrator acceptance and senior-administrator approval of peer answers before release to the asker
#### Constraints
- The AI assistant answers only from the curated corpus and cannot report an individual participant's current status
- The study covers a single programme across nine weeks of onboarding, with volume peaking in week 3 and tapering after, so it describes an onboarding period rather than a steady state

### Target Learners
- Participants in a large-scale online internship programme during staggered-cohort onboarding

### Learning Goals
- Resolving operational onboarding queries (eligibility, documentation, scheduling, status of pending submissions) with short turnaround without a dedicated mentor per student

### Claims
- [Status Enquiries Pending Submissions Assistant 1 3 Percent](../claims/status-enquiries-pending-submissions-assistant-1-3-percent.md) [+M]
- [Peer Answering Fast 70 Percent Within One Hour](../claims/peer-answering-fast-70-percent-within-one-hour.md) [+M]
- [Corpus Coverage 8 Percent Person Resolved Queries](../claims/corpus-coverage-8-percent-person-resolved-queries.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967. [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)
