---
type: strategy
id: attention-checks-probe-reflective-engagement
title: Use injected attention checks as behavioral probes of reflective engagement with AI suggestions
description: "The article recommends injecting a controlled number of deliberately misleading suggestions, semantically inconsistent with the student's immediate coding goal, to detect whether students critically evaluate AI code s..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: jessica-hutchison-2026
    resource: "https://doi.org/10.1145/3803400.3809394"
    title: "Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394"
    author: Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil
---

# Use injected attention checks as behavioral probes of reflective engagement with AI suggestions

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends injecting a controlled number of deliberately misleading suggestions, semantically inconsistent with the student's immediate coding goal, to detect whether students critically evaluate AI code suggestions rather than defaulting to fast thinking. Accepting an attention-check suggestion counts as a fail; rejecting it counts as a pass. The authors suggest future work could shift attention checks "from a passive metric toward a feedback mechanism" with real-time or summative feedback.

## Design Implications

### Context
#### Requirements
- Suggestions must be semantically inconsistent with the student's immediate coding goal rather than simply incorrect, since they could still produce functional code through later corrections
- Participants must not be informed of the manipulation in advance, as awareness would undermine its purpose
#### Constraints
- Deterministic injected attention checks do not fully replicate spontaneous AI hallucinations in real-world coding
- In this study attention checks served as a behavioral probe, not a feedback mechanism

### Target Learners
- CS1 / introductory programming students using AI code completion tools

### Target Learning Goals
- Critical evaluation and reflective engagement with AI-generated code suggestions

## Related Strategies
- 

## Examples
-

## Key Sources
- Jessica Hutchison, Ian Tyler Applebaum, Kenneth Angelikas, Kush Rakesh Patel, Phuoc Nguyen, Antonio Lazaro, Nicholas Rucinski, Rahad Arman Nabid, and Stephen MacNeil. (2026). To Tab or Not to Tab: Measuring Critical Engagement in AI Code Completion Tools Using Behavioral Signals and Attention Checks. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education (ITiCSE 2026). https://doi.org/10.1145/3803400.3809394
