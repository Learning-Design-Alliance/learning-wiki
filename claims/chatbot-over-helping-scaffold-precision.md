---
type: claim
title: The chatbot often provided more scaffold types than requested, and supplying classified question scope to the chatbot raised scaffold precision above .60
description: The chatbot often provided more scaffold types than requested, and supplying classified question scope to the chatbot raised scaffold precision above .60
id: chatbot-over-helping-scaffold-precision
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hyoungwook-jin-2026
    resource: "https://doi.org/10.48550/arxiv.2609.28918"
    title: "Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918 [doi:10.48550/arxiv.2609.28918](https://doi.org/10.48550/arxiv.2609.28918)"
    author: Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: hyoungwook-jin-2026-2
    resource: "https://arxiv.org/abs/2609.28918"
    title: "Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918"
    author: Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The chatbot often provided more scaffold types than requested, and supplying classified question scope to the chatbot raised scaffold precision above .60

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` In Study 1, scaffold precision was low: in approximately two-thirds of cases the chatbot provided more scaffold types than were asked. [→ Hyoungwook Jin 2026](#hyoungwook-jin-2026)
`q2 i?` Programmatically adjusting the system prompt with classified question scope substantially improved scaffold alignment to above .60 for Study 2. [→ Hyoungwook Jin 2026 (2)](#hyoungwook-jin-2026-2)

## Evidence

### Hyoungwook Jin 2026

Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918 [doi:10.48550/arxiv.2609.28918](https://doi.org/10.48550/arxiv.2609.28918)

`q2 · i?` · `causal · r2`

Technical evaluation of help-response alignment (coverage and precision) of the GPT-5.4-mini chatbot used in Study 1, using a human-annotated benchmark of 201, 142, and 165 chatbot responses across tasks. Total scaffold precision was .310 versus coverage .733.

> "In particular, scaffold pre- cision was low: in approximately two-thirds of cases, the chatbot provided more scaffold types than were asked."

### Hyoungwook Jin 2026 (2)

Hyoungwook Jin, Weirui Peng, Jieun Han, Q. Vera Liao, and Xu Wang. (2026). HelpCoach: Scaffolding Targeted AI Help-Seeking During Problem-Solving. arXiv. https://arxiv.org/abs/2609.28918

`q2 · i?` · `causal · r2`

For Study 2, the chatbot was supplied with the classified knowledge component and scaffold type of each student question and the system prompt was programmatically adjusted; Table 7 shows Study 2 total scaffold precision of .607 versus .310 in Study 1.

> "This approach substantially improved scaffold alignment to above .60, indicating that students would receive targeted help in most cases."

## Discussion


## Related Claims
- [Students rarely formulated questions specifying both knowledge component and scaffold type during chatbot problem-solving](students-rarely-ask-specific-questions.md) — related
- [Students' questions shift from broad to specific during Socratic AI tutoring, from about 10–15% specific in the first turn to all students asking specific questions by the final turn](question-specificity-rises-over-socratic-ai-dialogue.md) — related
- [Teachers sought to preserve student thinking and authorship by bounding chatbot answer-giving and maintaining teacher control over scope](teachers-preserve-student-thinking-bound-answer-giving.md) — a broader claim this one bears on
