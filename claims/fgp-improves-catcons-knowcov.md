---
type: claim
title: Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain
description: Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain
id: fgp-improves-catcons-knowcov
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: catcons-gain
    title: catcons-gain
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: knowcov-gain
    title: knowcov-gain
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Fine-grained prompting improves Bloom-level category consistency and knowledge coverage of generated questions in the computer science domain

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r2`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` Under FGP, Qwen2.5-7B improves CatCons by 18.20 points and Spark Max by 10.89 points in the computer science domain. [→ catcons-gain](#catcons-gain)
`q2 i?` Under FGP, LLaMA-3-8B achieves the largest knowledge-coverage gain (21.38 points) in the computer science domain. [→ knowcov-gain](#knowcov-gain)

## Evidence

### catcons-gain

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `design · r2`

Automated evaluation of category consistency after usability filtering, reported in the RQ2 results for the computer science domain comparing CoT and FGP. Qwen2.5-7B "achieves an 18.20-point improvement in CatCons".

> "In the computer science domain,Qwen2.5-7Bachieves an 18.20-point improvement in CatCons, andSpark Maximproves by 10.89 points."

### knowcov-gain

Xiaolong Wang, Zhe Zhao, Song Lai, Chaoli Zhang, Zijie Geng, Yu Tong, Ye Wei, and Qingsong Wen. 2026. From Memorization to Creation: Evaluating the Cognitive Depth of LLM-Generated Educational Questions. Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.1 (KDD '26). https://doi.org/10.1145/3770854.3785686

`q2 · i?` · `causal · r2`

Knowledge-coverage analysis in the same RQ2 computer science comparison. LLaMA-3-8B "achieves the largest gain (21.38 points)", followed by GLM-4-9B and InternLM3-8B with 7.37 and 13.30 points.

> "Regarding KnowCov,LLaMA-3-8B achieves the largest gain (21.38 points), followed byGLM-4-9Band InternLM3-8B, which improve by 7.37 and 13.30 points, respectively."

## Discussion

## Related Claims

- [LLMs show a directional asymmetry in educational control: they reliably increase cognitive demand but struggle to lower it](llm-upward-cognitive-shift-asymmetry.md) — the general claim this finding bears on, with the studies behind it
- [Fine-grained prompting substantially improves question uniqueness and usability of LLM-generated educational questions compared with Chain-of-Thought prompting](fgp-improves-question-uniqueness-usability.md) — related
- [Cognitive leap is the most prevalent deviation pattern of LLM-generated questions, and fine-grained prompting amplifies upward shifts while suppressing cognitive regression](cogleap-dominant-fgp-suppresses-regression.md) — related
- [Under Chain-of-Thought prompting, higher Bloom-level classification accuracy correlates with lower category consistency in generated questions](negative-correlation-classification-catcons.md) — related
- [The Bloom-driven framework generalizes to social-science questions, with automated rubrics agreeing strongly with experts on usability but only modestly on Bloom level](social-science-generalization-human-agreement.md) — related
- [LLMs exhibit an inherent abstraction bias, consistently generating questions at higher-than-intended cognitive levels regardless of prompting strategy](llm-abstraction-bias-higher-order-overproduction.md) — related
- [Higher knowledge-identification accuracy is associated with improved knowledge coverage in LLM-generated questions under Chain-of-Thought prompting](positive-correlation-identification-coverage.md) — related
