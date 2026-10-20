---
type: claim
title: "Student-AI conversations under teacher-authored prompts largely stay on the intended task (71% fully on-track; fewer than 1% substantially off-track)"
description: "Student-AI conversations under teacher-authored prompts largely stay on the intended task (71% fully on-track; fewer than 1% substantially off-track)"
id: teacher-prompts-keep-conversations-on-track
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: alex-liu-2026
    resource: "https://doi.org/10.48550/arxiv.2604.16738"
    title: "Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738 [doi:10.48550/arxiv.2604.16738](https://doi.org/10.48550/arxiv.2604.16738)"
    author: Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alex-liu-2026-2
    resource: "https://arxiv.org/abs/2604.16738"
    title: "Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738"
    author: Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Student-AI conversations under teacher-authored prompts largely stay on the intended task (71% fully on-track; fewer than 1% substantially off-track)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` 71.0% of conversations remained fully on-track toward teacher-specified objectives and only 0.5% deviated substantially. [→ Alex Liu 2026](#alex-liu-2026)
`q2 i?` Among deviating conversations, the most common patterns were shortcut/answer-seeking behavior (15.1%) and off-topic exchanges (13.1%). [→ Alex Liu 2026 (2)](#alex-liu-2026-2)

## Evidence

### Alex Liu 2026

Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738 [doi:10.48550/arxiv.2604.16738](https://doi.org/10.48550/arxiv.2604.16738)

`q2 · i?` · `design · r2`

LLM-coded conversation-level task alignment across the pilot's student-AI conversations, with human validation on a stratified subset reaching 87% agreement on high-stakes codes. The article reports "71.0% of conversations remained fully on-track" and 0.5% substantially off-track.

> "71.0% of conversations remained fully on-trackmoving toward teacher-specified objectives, with an additional 28.3% partially on-track (some deviation but substantial relevant engagement). Only 0.5% of conversations deviated substantially from the topics stated in the teacher prompt"

### Alex Liu 2026 (2)

Alex Liu, Min Sun, Lief Esbenshade, Victor Tian, Zachary Zhang, and Kevin He. (2026). Teacher-Authored Prompts for Configuring StudentAI Dialogue: K12 Classroom Implementation. https://arxiv.org/abs/2604.16738

`q2 · i?` · `design · r2`

Secondary descriptive analysis of conversations exhibiting some deviation. The article reports shortcut/answer-seeking at 15.1% of all conversations, off-topic exchanges at 13.1%, and copy-paste-like inputs at 6.9%.

> "the most common patterns wereshortcut/answer-seeking behavior(15.1% of all conversations) andoff-topic exchanges(13.1%). Copy-paste-like inputs, which potentially indicating students submitting work for the AI to complete, appeared in 6.9% of conversations."

## Discussion


## Related Claims
- [Prompting alone could not keep the gpt-3.5-turbo model on-topic, while the text-davinci-002 engine stayed on-topic in the deployed chatbot](gpt35-turbo-off-topic-prompting-insufficient.md) — related
- [Teachers authoring student-AI dialogue prompts predominantly write highly specific tasks targeting higher-order thinking (92% at DOK 2–3)](teachers-author-specific-higher-order-ai-prompts.md) — related
