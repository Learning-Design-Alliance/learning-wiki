---
type: claim
title: "iRULER's LLM-as-a-judge scoring showed high intra-model reliability and moderate-to-substantial agreement with expert ratings on the ICNALE dataset"
description: "iRULER's LLM-as-a-judge scoring showed high intra-model reliability and moderate-to-substantial agreement with expert ratings on the ICNALE dataset"
id: iruler-scoring-reliability-expert-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: jingwen-bai-2026
    title: Jingwen Bai 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: jingwen-bai-2026-2
    title: Jingwen Bai 2026 (2)
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# iRULER's LLM-as-a-judge scoring showed high intra-model reliability and moderate-to-substantial agreement with expert ratings on the ICNALE dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1`–`r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across five scoring runs per essay, all criteria achieved Krippendorff's α ≥ .82 and the total score α = .95. [→ Jingwen Bai 2026](#jingwen-bai-2026)
`q2 i?` Expert-LLM agreement reached QWK = .68 on the 0–100 total score, with per-criterion QWK from .52 (Content) to .66 (Language Use). [→ Jingwen Bai 2026 (2)](#jingwen-bai-2026-2)

## Evidence

### Jingwen Bai 2026

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q2 · i?` · `causal · r1`

Intra-model reliability analysis on the ICNALE Edited Essays dataset (640 essays of 200–300 words from ESL students), running gpt-4.1 with temperature 0 five times per essay and treating the runs as five raters.

> "all criteria achieve𝛼≥. 82, and the total score reaches𝛼=. 95, with SDs of 0.06–0.11 on four criteria and 1.7 on the 0–100 total score."

### Jingwen Bai 2026 (2)

Jingwen Bai, Wei Soon Cheong, Philippe Muller, and Brian Y Lim. 2026. iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision. Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems (CHI '26). https://doi.org/10.1145/3772318.3790539

`q2 · i?` · `causal · r2`

Expert-LLM agreement analysis averaging the five runs per essay and computing Quadratic Weighted Kappa against ICNALE expert scores; the article states agreement is moderate to substantial and that iRULER is not intended to replace human experts.

> "𝑄𝑊𝐾=. 68on the 0–100 total score, with per-criterion QWK ranging from .52 (Content) to .66 (Language Use), comparable to recent LLM-based AES systems and typical human–human agreement on fine-grained writing scores"

## Discussion


## Related Claims
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Inter-run reliability of LLM performance on the EBHS examination was consistently high, with an overall mean Cohen's κ of 0.821 and no model falling below moderate agreement.](llm-ebhs-inter-run-reliability-high-kappa-0821.md) — related
