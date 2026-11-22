---
type: claim
title: A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position
description: A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position
id: fine-tuned-8b-outperforms-70b-on-context-dependent-components
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ali-keramati-and-mark-warschauer-2026
    resource: "https://doi.org/10.48550/arXiv.2606.10327"
    title: "Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)"
    author: Ali Keramati and Mark Warschauer
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# A fine-tuned 8B model outperforms a zero-shot LLaMA-70B baseline on context-dependent components like Evidence and Conclusion, though the 70B excels on self-contained components like Position

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The Sequential 8B model significantly outperforms the LLaMA-70B zero-shot baseline on Evidence (65% vs. 49% F1) and Conclusion (87% vs. 60% F1), while the 70B model excels on self-contained components like Position. [→ Ali Keramati and Mark Warschauer 2026](#ali-keramati-and-mark-warschauer-2026)

## Evidence

### Ali Keramati and Mark Warschauer 2026

Ali Keramati and Mark Warschauer. (2026). The Order Matters: Sequential Fine-Tuning of LLaMA for Coherent Automated Essay Scoring. Published as a conference paper at ICLR 2026. [doi:10.48550/arXiv.2606.10327](https://doi.org/10.48550/arXiv.2606.10327)

`q2 · i?` · `causal · r2`

Benchmark comparison in the PERSUADE 2.0 experiments (Section 5.2, finding 5) between the fine-tuned Sequential 8B model and a general-purpose LLaMA-70B zero-shot baseline. The 8B model "significantly outperforms it on context-dependent components" with 65% vs. 49% F1 on Evidence and 87% vs. 60% F1 on Conclusion.

> "While the 70B model excels on self-contained components likePosition, ourSequential 8B model significantly outperforms it on context-dependent components likeEvidence(65% vs. 49% F1) andConclusion(87% vs. 60% F1)."

## Discussion


## Related Claims
- [Sequential curriculum fine-tuning yields the strongest overall AES performance, achieving the highest or tied-for-highest F1 on Claim, Evidence, and Conclusion](sequential-curriculum-strongest-aes-performance.md) — possibly the same claim (merge candidate)
- [LoRA fine-tuning a small LLM significantly improves answer correctness classification over prompted baselines, with the single-task model with rationale significantly outperforming Llama3 70B without rationale](mathedu-finetuning-improves-correctness-classification.md) — related
- [Sequentially fine-tuned models dramatically outperform independently fine-tuned models on scoring conclusions, implying conclusions require contextual representations from other essay parts](sequential-beats-independent-on-conclusion.md) — related
- [Fine-tuning substantially outperforms zero-shot prompting of the same open-source model for cross-rubric scoring, improving macro F1 from 0.222 to 0.353](fine-tuning-beats-zero-shot-prompting-same-model.md) — related
