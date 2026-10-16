---
type: design
id: memdora-collaborative-deck-layer
title: Collaborative deck layer with live synchronization and independent per-follower scheduling
description: "Memdora's collaborative layer lets users publish decks publicly, to friends, or privately; published decks appear in a Discover feed where users follow them."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: ruiyang-zhang-2027
    resource: "https://arxiv.org/abs/2607.25096"
    title: "Ruiyang Zhang. (2027). Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition. Proceedings of ACM International Conference on Intelligent User Interfaces (IUI '27). https://arxiv.org/abs/2607.25096"
    author: Ruiyang Zhang
---

# Collaborative deck layer with live synchronization and independent per-follower scheduling

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Memdora's collaborative layer lets users publish decks publicly, to friends, or privately; published decks appear in a Discover feed where users follow them. When the deck owner adds, edits, or removes a card, "all followers' copies update instantly—no re-follow required", while "each follower maintains independent FSRS-6 scheduling state, learning at their own pace". The infrastructure uses a publish-subscribe model with server-side scheduling state.

## Design Implications

### Context
#### Requirements
- A publish-subscribe infrastructure with each follower maintaining independent scheduling state server-side
#### Constraints
- The collaborative deck features have not yet been evaluated in a formal educational setting; deployment may reveal unmet needs around teacher workflows and institutional authentication

### Target Learners
- students following a teacher's shared deck
- community deck followers

### Learning Goals
- shared vocabulary learning with teacher-curated content

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Ruiyang Zhang. (2027). Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition. Proceedings of ACM International Conference on Intelligent User Interfaces (IUI '27). https://arxiv.org/abs/2607.25096
