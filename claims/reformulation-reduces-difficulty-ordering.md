---
type: claim
title: Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended
description: Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended
id: reformulation-reduces-difficulty-ordering
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: justin-chih-yao-chen-2026
    resource: "https://doi.org/10.48550/arXiv.2604.04767"
    title: "Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)"
    author: Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Reformulating hard open-ended problems into MCQ or cloze formats reduces empirical difficulty, with a consistent ordering MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Zero-shot accuracy on pass@64=0 problems rises from strictly 0.0 on open-ended questions to 33.8% with 4-choice MCQ reformulation, above the 25% random baseline. [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)
`q2 i?` Reformulations induce a consistent empirical difficulty ordering: MCQ4 ≤ MCQ10 ≤ Cloze ≤ Open-ended. [→ Justin Chih-Yao Chen 2026](#justin-chih-yao-chen-2026)

## Evidence

### Justin Chih-Yao Chen 2026

Justin Chih-Yao Chen, Archiki Prasad, Zaid Khan, Joykirat Singh, Runchu Tian, Elias Stengel-Eskin, Mohit Bansal. (2026). Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems. Preprint. Under review. [doi:10.48550/arXiv.2604.04767](https://doi.org/10.48550/arXiv.2604.04767)

`q2 · i?` · `causal · r2`

Zero-shot evaluation of Qwen on the reformulated hard dataset D'hard (problems sampled only where pass@64=0), reported in Section 3.1 and Figure 2(a). The 4-choice reformulation "achieves 33.8% accuracy, well above the 25% random baseline" while the original open-ended baseline is strictly 0.0.

> "For instance, the 4-choice MCQ reformulation achieves 33.8% accuracy, well above the 25% random baseline. Similar trends hold for the 10-choice and cloze formats. We also observe that task reformulations induce a consistent ordering of empirical difficulty: MCQ4 ≤MCQ 10 ≤Cloze≤Open-ended."

## Discussion


## Related Claims
- Cog-DRIFT outperforms GRPO and guided-exploration baselines, unlocking gains on originally unsolvable problems (+10.11% Qwen, +8.64% Llama on BigMath-Hard) — related
- [An instance-level adaptive curriculum that promotes problems upon reaching 50% accuracy improves sample efficiency and prevents performance plateaus](instance-level-curriculum-sample-efficiency.md) — related
- [Exposure to a diverse mixture of reformulations is critical for transfer; single-format training does not improve over no training](reformulation-diversity-critical.md) — related
- [Learning from reformulated problems transfers back to original open-ended hard problems, and more generative formats transfer better](reformulation-transfers-back-to-open-ended.md) — related
- [In one German secondary-school chemistry test, multiple-choice single-select items were less difficult than open-ended items, and delayed perceived task difficulty ratings related more strongly to relative item difficulty for open-ended items](answer-format-availability-affects-difficulty-and-ratings.md) — a broader claim this one bears on
- [Structured open-ended formats such as the MEQ tend to underperform well-written multiple-choice items in testing higher-order cognitive skills, and converge on multiple-choice as their reliability increases](meq-underperforms-mcq-higher-order.md) — related
- [Well-constructed context-rich multiple-choice items can assess five of Bloom's six cognitive levels, so the question's phrasing rather than the response format determines the cognitive level tested](context-rich-mcq-higher-order.md) — related
