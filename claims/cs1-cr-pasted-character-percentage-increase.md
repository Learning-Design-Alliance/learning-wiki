---
type: claim
title: "The percentage of pasted characters in coding assignments rose significantly from 61.0% in Fall 2024 to 68.1% in CS1-CR"
description: "The percentage of pasted characters in coding assignments rose significantly from 61.0% in Fall 2024 to 68.1% in CS1-CR"
id: cs1-cr-pasted-character-percentage-increase
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: peter-fowles-2026
    resource: "https://arxiv.org/abs/2605.21374"
    title: "Peter Fowles, Erik Falor, Sulove Bhattarai, John Edwards, and Seth Poulsen. (2026). Combating Harms of Generative AI in CS1 with Code Review Interviews and a Flipped Classroom. https://arxiv.org/abs/2605.21374"
    author: Peter Fowles, Erik Falor, Sulove Bhattarai, John Edwards, and Seth Poulsen
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The percentage of pasted characters in coding assignments rose significantly from 61.0% in Fall 2024 to 68.1% in CS1-CR

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Submission-level percentage of characters pasted relative to total characters input increased significantly between Fall 2024 and CS1-CR (Mann-Whitney U = 85517, p < 0.0001), which the authors attribute to increased AI usage. [→ Peter Fowles 2026](#peter-fowles-2026)

## Evidence

### Peter Fowles 2026

Peter Fowles, Erik Falor, Sulove Bhattarai, John Edwards, and Seth Poulsen. (2026). Combating Harms of Generative AI in CS1 with Code Review Interviews and a Flipped Classroom. https://arxiv.org/abs/2605.21374

`q2 · i?` · `causal · r1`

Keystroke-log analysis over eight identical assignments from Fall 2024 and CS1-CR using the ShowYourWork plugin in PyCharm. The percentage of characters pasted "increased from61 .0%in Fa24 to68 .1%in CS1-CR", significant by Mann-Whitney U test; no effect size is printed.

> "increased from61 .0%in Fa24 to68 .1%in CS1-CR. A Mann-Whitney U test on the two distributions of submission-level percentages shows that this increase is significant(𝑈= 85517, 𝑝< 0.0001)"

## Discussion


## Related Claims
- [Paste event counts stayed roughly constant while pasted characters rose, indicating students pasted larger blocks of AI-generated code](cs1-cr-paste-events-unchanged-larger-blocks.md) — related
- [Student effort on assignments, measured by time-on-task and keystrokes, showed no evidence of decrease when AI use was allowed](cs1-cr-effort-unchanged-despite-ai.md) — related
- [CS1-CR students reported overwhelmingly positive sentiment toward code reviews, with 65% agreeing they helped avoid over-reliance on AI and 90% reporting increased motivation to understand their code](cs1-cr-positive-sentiment-code-reviews.md) — related
- [Random assignment to AI access produces a strong first stage: about 70 percent of treated students use AI, most often to explain concepts](genai-first-stage-usage-patterns.md) — related
