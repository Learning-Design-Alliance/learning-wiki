---
type: claim
title: In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task
description: In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task
id: sft-less-effective-than-prompting-for-feedback-generation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: adnan-labib-2026
    resource: "https://doi.org/10.48550/arxiv.2607.14524"
    title: "Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524 [doi:10.48550/arxiv.2607.14524](https://doi.org/10.48550/arxiv.2607.14524)"
    author: Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In one essay-feedback system, fine-tuned models produced no usable deep-level feedback output, so only directly prompted LLMs were evaluated; the authors suggest prompting may be more effective than supervised fine-tuning for this task

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Among directly prompted models, Claude 3.7 generated more fine-grained, pedagogically necessary comments (628) than LLaMA-3.3-70B (336) or GPT-4o (368), whose averages were below 10 comments per essay. [→ Adnan Labib 2026](#adnan-labib-2026)

## Evidence

### Adnan Labib 2026

Adnan Labib, Yixuan Huang, Jiahui Wu, John Maurice Gayed, Zheng Yuan, Qiao Wang. (2026). WrAFT: a Modularized Automated Writing Evaluation System for Argumentative Essays. arXiv preprint. https://arxiv.org/abs/2607.14524 [doi:10.48550/arxiv.2607.14524](https://doi.org/10.48550/arxiv.2607.14524)

`q2 · i?` · `design · r2`

In the preliminary check, neither fine-tuned model produced usable output (fine-tuned GPT-4o's output was truncated at the 8,000-token context window on every essay; fine-tuned LLaMA-3.3-70B's could not be parsed as valid JSON), so fine-tuned feedback was excluded from human evaluation and no like-for-like comparison of feedback quality was made; the authors conclude only that prompting "may even be more effective" than supervised fine-tuning. Preliminary check of directly prompted models' micro feedback sufficiency on the 40 test essays: a qualitative review of three randomly selected essays confirmed Claude 3.7's additional comments were more fine-grained and pedagogically necessary, so validation focused on Claude 3.7.

> "Of the 40 test essays, LLaMA-3.3-70B generated 336 comments and GPT-4o generated 368 comments, the averages of both were below 10. Claude 3.7, however, generated 628 comments."

## Discussion


## Related Claims
- [Supervised fine-tuning on real score–essay pairs substantially outperforms prompting for proficiency-conditioned writing simulation](sft-improves-proficiency-alignment-over-prompting.md) — reports the opposite
- [LLMs are more stable than supervised models across dataset shifts, though they do not surpass within-dataset fine-tuned performance](llms-more-stable-cross-dataset-than-supervised.md) — reports the opposite
- [Without fine-tuning, commercial frontier models outperform open-source LLMs on MedGame Bench structural validity and content metrics](commercial-models-outperform-open-source-medgame-baseline.md) — related
- [Directly prompted Claude 3.7 micro-level deep feedback was judged both necessary and effective in 94.69% of 630 comments](wraft-micro-feedback-95-percent-necessary-effective.md) — related
- [Directly prompted Claude 3.7 macro-level deep feedback was judged effective for 93.03% of 201 paragraph-level comments](wraft-macro-feedback-93-percent-effective.md) — related
- [Self-hosted open-weight LLMs offer privacy, reproducibility, and environmental advantages over commercial LLM interfaces in educational ITSs](self-hosted-llm-advantages-education.md) — related
- [Directly prompted GPT-4o surface-level corrective edits were judged necessary and effective in 96.14% of 2049 identified edits](wraft-surface-feedback-96-percent-precision.md) — related
- [Task-specific fine-tuning substantially improves open-source LLMs on MedGame Bench and narrows the gap with commercial models](fine-tuning-improves-open-source-llms-medgame-bench.md) — related
- [Fine-tuned 8B LLMs generate K-2 stories with difficulty-related metric scores statistically significantly different from (mostly better than) zero-shot GPT-4o and Llama 3.3 70B](finetuned-8b-llms-beat-zero-shot-large-models-on-difficulty-metrics.md) — reports the opposite
- [Rubric-grounded prompting alone provides limited proficiency control, aligning far better on content-oriented traits than on form-oriented traits](prompting-limited-uneven-proficiency-control-writing-simulation.md) — related
