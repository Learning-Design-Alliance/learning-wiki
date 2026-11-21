---
type: claim
title: Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.
description: Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.
id: sft-ineffective-reference-metrics-unreliable
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: alexander-scarlatos-2024
    resource: "https://doi.org/10.1007/978-3-031-64302-6_20"
    title: "Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)"
    author: Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: alexander-scarlatos-2024-2
    resource: "https://doi.org/10.1007/978-3-031-64302-6_20"
    title: "Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)"
    author: Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Supervised fine-tuning does not outperform zero-shot prompting on rubric score for math feedback generation, and ROUGE-L and BERTScore are unreliable estimates of feedback quality.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` SFT does not outperform Zero-Shot on rubric score, showing the standard fine-tuning setup is not effective for feedback generation. [→ Alexander Scarlatos 2024](#alexander-scarlatos-2024)
`q2 i?` ROUGE-L and BERTScore are unreliable estimates of feedback quality since they are highest on SFT, which copies the style of the gold feedback most closely. [→ Alexander Scarlatos 2024 (2)](#alexander-scarlatos-2024-2)

## Evidence

### Alexander Scarlatos 2024

Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)

`q2 · i?` · `design · r2`

Quantitative comparison in §4.3 (Table 2) of Llama 2 variants on the Eedi test set scored by GPT-4; SFT and Zero-Shot both score 0.49 overall. No effect size or significance test is printed.

> "Surprisi ngly, SFT does not outperform Zero-Shot on score, which shows that the standar d ﬁne-tuning setup is not eﬀective for feedback generation."

### Alexander Scarlatos 2024 (2)

Alexander Scarlatos, Digory Smith, Simon Woodhead, and Andrew Lan. (2024). Improving the Validity of Automatically Generated Feedback via Reinforcement Learning. Published in AIED 2024. [doi:10.1007/978-3-031-64302-6_20](https://doi.org/10.1007/978-3-031-64302-6_20)

`q2 · i?` · `design · r2`

Same §4.3 evaluation using human-written feedback as reference; SFT attains the highest ROUGE-L (0.29) and BERTScore (0.61) despite a low rubric score of 0.49. No effect size is printed.

> "We can also see that ROUGE-L and BERTScore are unreliable estimates of feedback quality sin ce they are highest on SFT, primarily because it copies the style of the gold feed back the closest."

## Discussion


## Related Claims
- [DPO training on GPT-4 rubric annotations with mismatched feedback significantly improves the correctness and alignment of Llama 2-generated math feedback compared to zero-shot and SFT baselines.](dpo-score-mismatch-improves-math-feedback.md) — related
- [In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task](sft-less-effective-than-prompting-for-feedback-generation.md) — related
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — reports the opposite
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [DPO consistently outperforms supervised fine-tuning (SFT) for Socratic question generation with Llama 2](dpo-outperforms-sft-socratic-questions.md) — related
- [Higher-bit quantisation (8-bit) better preserves structural coherence and semantic alignment in a Pidgin-fine-tuned LLM, achieving the highest ROUGE-L (0.3120) and BERTScore (0.8590) among the quantised models](higher-bit-quantisation-preserves-semantic-structure-pidgin-llm.md) — related
- [Zero-shot prompting collapses proficiency variation toward an idealized high-scoring student population, while SFT and GRPO match the human score and length distributions](prompting-collapses-proficiency-variation-toward-idealized-students.md) — related
- [DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training](dpo-matches-gpt4o-pedagogical-rubric.md) — related
- [High-utility questions are weakly related to exam-question similarity and Bloom's cognitive depth, suggesting they are not paraphrases of exam questions](high-utility-questions-not-exam-paraphrases.md) — related
