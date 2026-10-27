---
type: claim
title: LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays
description: LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays
id: llm-overrate-short-essays-overpenalize-errors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Compared to humans, LLMs assign higher scores to short or underdeveloped essays that address the prompt, and assign lower scores to well-developed essays containing minor grammatical or spelling errors. [→ Jerin George Mathew 2026](#jerin-george-mathew-2026)

## Evidence

### Jerin George Mathew 2026

Jerin George Mathew, Sumayya Taher, Anindita Kundu, Denilson Barbosa. (2026). LLMs Do Not Grade Essays Like Humans. https://arxiv.org/abs/2603.23714 [doi:10.48550/arxiv.2603.23714](https://doi.org/10.48550/arxiv.2603.23714)

`q2 · i?` · `associational · r2`

Manual inspection of essays with large LLM-human score differences plus essay-feature analysis (Figures 9, 10): essay length increased substantially with human scores while readability stayed stable, and all maximum-score essays contained LanguageTool-detected errors, most commonly spelling.

> "Compared to humans, LLMs tend to overrate short or underdeveloped essays that address the prompt, and to over-penalize minor language errors in otherwise well-developed essays, suggesting they take a more literal approach to grading according to humans."

## Discussion

## Related Claims

- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — the general claim this finding bears on, with the studies behind it
- [Both fine-tuned models show regression toward the mean in score-wise bias, and error rises monotonically above score 3.0, with high scores hardest to predict](score-wise-bias-regression-to-mean-awe.md) — related
- [AI scoring consistency approaches or exceeds 90% for most rubric items, but spelling is replaced by a deterministic LanguageTool-based approach achieving 68% accuracy with 100% consistency](ai-consistency-high-except-spelling-languagetool-replacement.md) — related
- [Small input perturbations such as minor spelling errors can reduce state-of-the-art dialogue and assessment model accuracy by over 30%](its-dialogue-models-brittleness-perturbations.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — reports the opposite
- [LLM feedback sentiment tracks assigned scores: low scores come with more criticism, high scores with more praise](llm-feedback-sentiment-tracks-scores.md) — related
- [Prompt quality and detailed scoring rubrics significantly influence the accuracy and consistency of LLM-generated grades](prompt-rubric-quality-drives-llm-grading.md) — related
- [Wise-crowd content models for summary assessment correlate well with an educational rubric, manually and via two automated NLP methods](wise-crowd-content-model-summary-assessment.md) — related
