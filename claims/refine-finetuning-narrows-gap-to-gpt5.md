---
type: claim
title: "Fine-tuning on interaction traces narrows an 8B model's gap to GPT-5 on interactive response quality except correctness"
description: "Fine-tuning on interaction traces narrows an 8B model's gap to GPT-5 on interactive response quality except correctness"
id: refine-finetuning-narrows-gap-to-gpt5
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: fares-fawzi-2026
    resource: "https://doi.org/10.1007/978-3-032-29744-0_27"
    title: "Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. [doi:10.1007/978-3-032-29744-0_27](https://doi.org/10.1007/978-3-032-29744-0_27)"
    author: Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: fares-fawzi-2026-2
    resource: "https://doi.org/10.1007/978-3-032-29744-0_27"
    title: "Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. [doi:10.1007/978-3-032-29744-0_27](https://doi.org/10.1007/978-3-032-29744-0_27)"
    author: Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fine-tuning on interaction traces narrows an 8B model's gap to GPT-5 on interactive response quality except correctness

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qwen3-8B REFINE is not significantly different from GPT-5 on relevance, actionability, or tool relevance, although a significant gap in correctness remains. [→ Fares Fawzi 2026](#fares-fawzi-2026)
`q2 i?` Fine-tuned REFINE reaches final answers in fewer reasoning–tool steps than the thinking baseline. [→ Fares Fawzi 2026 (2)](#fares-fawzi-2026-2)

## Evidence

### Fares Fawzi 2026

Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. [doi:10.1007/978-3-032-29744-0_27](https://doi.org/10.1007/978-3-032-29744-0_27)

`q2 · i?` · `design · r2`

Offline evaluation on a held-out test set of 192 student questions using a human-aligned Interactive Feedback Judge, with paired McNemar exact tests and Benjamini–Hochberg correction. No effect sizes are printed; only significance is reported.

> "Qwen 3-8B REFINE is not significantly different from GPT-5 on relevance, actionability, or tool relevance, although a significant gap in correctness remains."

### Fares Fawzi 2026 (2)

Fares Fawzi, Seyed Parsa Neshaei, Marta Knezevic, Tanya Nazaretsky, and Tanja Käser. (2026). REFINE: Real-world Exploration of Interactive Feedback and Student Behaviour. arXiv. [doi:10.1007/978-3-032-29744-0_27](https://doi.org/10.1007/978-3-032-29744-0_27)

`q2 · i?` · `design · r2`

Tool-use efficiency analysis on the same held-out test set: the fine-tuned model used 2.26 mean reasoning–tool steps versus 2.39 for the thinking baseline, and reduced the share of queries exceeding the nominal two-step trajectory (19.9% vs. 25.7%).

> "Qwen3-8B REFINE reached final answers in fewer reasoning–tool steps than the thinking baseline (2.26 vs. 2.39 mean steps; paired Wilcoxon p= 0.043)"

## Discussion


## Related Claims
- [Interactive feedback quality remains high when deployed in classroom and exam-preparation use](refine-deployment-quality-robust.md) — related
- [DPO training brings the pedagogical rubric performance of an 8B open-source LLM to the level of GPT-4o while improving over SFT and distillation-only training](dpo-matches-gpt4o-pedagogical-rubric.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — related
- [Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics](commercial-models-outperform-open-source-medgame-baseline.md) — related
