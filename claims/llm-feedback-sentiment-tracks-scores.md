---
type: claim
title: "LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise"
description: "LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise"
id: llm-feedback-sentiment-tracks-scores
aliases: [shap-praise-raises-criticism-lowers-llm-scores]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: jerin-george-mathew-2026
    resource: "https://doi.org/10.48550/arxiv.2603.23714"
    title: "Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)"
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

`q2 i?` In proxy XGBoost models predicting LLM scores from trait-specific praise and criticism counts, praise-related features produce positive SHAP values and criticism-related features negative ones. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `associational · r2`

Aspect-based sentiment analysis (DeBERTa-v3 ABSA, confidence above 0.9) of trait-specific praise and criticism in LLM feedback, aggregated by assigned score for DREsS and ASAP Task 1 (Figures 11 and 12). Positive mentions frequently exceeded 80-100% for high-scoring essays on DREsS.

> "essays receiving low scores are typically associated with a high proportion of negative mentions across traits, while essays receiving higher scores contain increasingly positive feedback."

<!-- merged 2026-10-13 from shap-praise-raises-criticism-lowers-llm-scores: that page's entry for this study, which differed from the one above, kept verbatim.
### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714

`q2 · i?` · `associational · r2`

XGBoost proxy models trained per dataset and LLM on counts of positive and negative trait mentions, with SHAP used to estimate feature contributions (Figure 13 for Llama models on ASAP Task 7). Similar trends were reported for GPT models and other datasets in an appendix.

> "These results suggest that LLM-assigned scores are coherent with the evaluative signals expressed in their feedback: praise-related mentions increase predicted scores, whereas criticism-related mentions decrease them."
-->

## Discussion



## Related Claims

- [Different LLMs rely on different subsets of rubric traits when assigning essay scores](llms-weight-rubric-traits-differently.md) — related
- [LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts](marked-students-praise-withholding-bias.md) — related
- [Motivation prompts shift feedback tone: unmotivated students receive enthusiastic, collaborative encouragement while motivated students receive direct, higher-level critique](motivation-prompt-enthusiasm-pedagogy.md) — related
- [Gender prompts shift feedback stance: female students receive affective, first-person, empathy-oriented feedback while male students receive objective, task-oriented critique](gender-prompt-emotional-connection-pedagogy.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
