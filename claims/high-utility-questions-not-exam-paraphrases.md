---
type: claim
title: "High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions"
description: "High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions"
id: high-utility-questions-not-exam-paraphrases
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: dong-ho-lee-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: dong-ho-lee-2026-2
    resource: "https://doi.org/10.18653/2026.findings-emnlp.97"
    title: "Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)"
    author: Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Utility correlates weakly positively with semantic similarity to the most similar exam question (0.25) and nearly zero with ROUGE (0.04), suggesting high-utility questions are not simple paraphrases of exam questions. [→ Dong-Ho Lee 2026](#dong-ho-lee-2026)
`q2 i?` Utility correlates weakly positively with Bloom's taxonomy cognitive depth (correlation of 0.12). [→ Dong-Ho Lee 2026 (2)](#dong-ho-lee-2026-2)

## Evidence

### Dong-Ho Lee 2026

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i?` · `associational · r1`

Correlational analysis computing embedding cosine similarity (text-embedding-3-small) and ROUGE overlap between generated questions and exam questions in the same chapter. The printed correlations are "0.25" for semantic similarity and "nearly zero at 0.04" for ROUGE; no standardized effect size is printed beyond these raw correlations, so the impact is uncoded. The authors conclude high-utility questions "are not simple paraphrases of exam questions".

> "The correlation between utility and semantic similarity is 0.25 (p <0.001 ), indicating a weak positive relationship, while the correlation with ROUGE is nearly zero at 0.04 (p <0.01)."

### Dong-Ho Lee 2026 (2)

Dong-Ho Lee, Hyundong Cho, Jonathan May, Jay Pujara. (2026). Which Questions Improve Learning the Most? Utility Estimation of Questions with LM-based Simulations. arXiv. Originally published 2025. [doi:10.18653/2026.findings-emnlp.97](https://doi.org/10.18653/2026.findings-emnlp.97)

`q2 · i?` · `associational · r1`

Correlational analysis annotating exam questions with Bloom's taxonomy categories via an LM and correlating cognitive depth with utility on generated training-set questions. The printed correlation is 0.12 with p <0.001, described as a weak positive relationship; no standardized effect size is printed, so the impact is uncoded.

> "Using Bloom's taxonomy as a cognitive depth scale (Likert 1-6), the correlation between utility and cognitive depth is 0.12 (p <0.001 ), indicating a weak positive relationship."

## Discussion


## Related Claims
- [Automatic text-similarity metrics do not correlate with manual evaluation for Socratic utterance generation](automatic-metrics-uncorrelated-socratic-manual-eval.md) — related
- [Exam cognitive level, question type, and content coverage were similar across control and reading-quiz terms, ruling out reduced exam rigor](exam-rigor-similar-across-quiz-and-control-terms.md) — related
- [Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.](sft-ineffective-reference-metrics-unreliable.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [Simulation-computed utility is moderately positively correlated with usefulness as perceived by human evaluators, without reducing interestingness](utility-moderately-correlates-human-perceived-usefulness.md) — related
- [Question utility is only weakly correlated with salience and not significantly correlated with expected information gain](utility-uncorrelated-with-salience-and-eig.md) — related
