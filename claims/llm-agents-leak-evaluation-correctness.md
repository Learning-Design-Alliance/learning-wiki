---
type: claim
title: LLM agents leak evaluation of answer correctness through praise, word choice, reply length, and pacing, which stops student reasoning
description: LLM agents leak evaluation of answer correctness through praise, word choice, reply length, and pacing, which stops student reasoning
id: llm-agents-leak-evaluation-correctness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: byungmoon-cho-2026
    resource: "https://doi.org/10.48550/arXiv.2610.22949"
    title: "Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)"
    author: Byungmoon Cho
    q: 1
    i: "?"
    kind: design
    rigour: 3
---

# LLM agents leak evaluation of answer correctness through praise, word choice, reply length, and pacing, which stops student reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` LLM agents tend to reveal whether an answer was right through praise, word choice, reply length, and pacing, and a student who infers this stops reasoning. [→ Byungmoon Cho 2026](#byungmoon-cho-2026)

## Evidence

### Byungmoon Cho 2026

Byungmoon Cho. (2026). Designing an AI Agent That Does Not Tutor: Design Rules for Socratic Probing in Introductory Physics. [doi:10.48550/arXiv.2610.22949](https://doi.org/10.48550/arXiv.2610.22949)

`q1 · i?` · `design · r3`

The article's design analysis, grounded in eight agent versions and more than 40 scripted simulation runs, identifies evaluation leakage: "praise, word choice, reply length, and pacing reveal whether an answer was right". No effect size is reported; this is a design observation, not a tested human result.

> "LLM agents tend to leak evaluation: praise, word choice, reply length, and pacing reveal whether an answer was right, and a student who knows stops reasoning."

## Discussion


## Related Claims
- [Banning forbidden praise phrases increased praise, while a positive indistinguishability principle eliminated it in bait tests](banned-phrase-lists-increase-praise.md) — related
- [A deployed reflection agent followed its prompt's countable rules but broke its dispositional rules about manner](agent-followed-countable-not-dispositional-rules.md) — related
- [The AutoFeedback multi-agent system significantly outperforms a single GenAI agent by reducing over-praise and over-inference in generated feedback](autofeedback-multi-agent-reduces-over-praise-over-inference.md) — related
- [The agent's praise was indiscriminate affirmation: validation followed about half of participant turns regardless of what the participant said](indiscriminate-affirmation-reflection-agent.md) — related
