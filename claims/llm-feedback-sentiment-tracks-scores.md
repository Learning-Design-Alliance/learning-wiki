---
type: claim
title: "LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise"
description: "LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise"
id: llm-feedback-sentiment-tracks-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jerin-george-mathew-2026
    resource: "https://arxiv.org/abs/2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714"
    author: Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Essays receiving low LLM scores are associated with high proportions of negative trait mentions, while higher-scored essays receive increasingly positive feedback, though the relationship varies in strength across traits and datasets. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714

`q2 · i?` · `associational · r2`

Aspect-based sentiment analysis (DeBERTa-v3 ABSA, confidence above 0.9) of trait-specific praise and criticism in LLM feedback, aggregated by assigned score for DREsS and ASAP Task 1 (Figures 11 and 12). Positive mentions frequently exceeded 80-100% for high-scoring essays on DREsS.

> "essays receiving low scores are typically associated with a high proportion of negative mentions across traits, while essays receiving higher scores contain increasingly positive feedback."

## Discussion


## Related Claims
- [SHAP analysis shows praise mentions raise LLM-assigned scores while criticism mentions lower them](shap-praise-raises-criticism-lowers-llm-scores.md) — possibly the same claim (merge candidate)
- [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) — related
- [LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts](marked-students-praise-withholding-bias.md) — related
- [Motivation prompts shift feedback tone: unmotivated students receive enthusiastic, collaborative encouragement while motivated students receive direct, higher-level critique](motivation-prompt-enthusiasm-pedagogy.md) — related
- [Gender prompts shift feedback stance: female students receive affective, first-person, empathy-oriented feedback while male students receive objective, task-oriented critique](gender-prompt-emotional-connection-pedagogy.md) — related
