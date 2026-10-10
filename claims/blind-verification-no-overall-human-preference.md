---
type: claim
title: Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically
description: Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically
id: blind-verification-no-overall-human-preference
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: liu-2026
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: 0
    kind: associational
    rigour: 2
  - id: liu-2026-2
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i0` negligible

## Subclaims
`q2 i0` Among decisive Human vs. LLM comparisons, an independent blind domain expert preferred human coding 51.5% and LLM coding 48.5% of the time, a statistically negligible deviation from chance. [→ Liu 2026](#liu-2026)
`q2 i?` Verification checks passed: no position bias was detected, and Human vs. Human pairs split nearly evenly across the three coders, confirming the task admits meaningful discrimination without favoring any coder. [→ Liu 2026 (2)](#liu-2026-2)

## Evidence

### Liu 2026

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i0` · `associational · r2`

Blind verification protocol: an expert with a doctorate in education, not involved in the original coding and unaware of source identity, judged 855 anonymized pairwise comparisons with position randomized. Of 855 comparisons, "the verifier expressed a decisive preference in 801 cases (93.7%)"; the human-preference effect versus 0.50 was "a negligible effect" (Cohen’s h = 0.029).

> "Among the 555 Human vs. LLM pairs, 515 received decisive preferences, with human coding preferred in 265 cases (51.5%) and LLM coding in 250 (48.5%). A binomial test yields p = 0.537, the 95% confidence interval for the human preference rate is [0.470, 0.559], and Cohen’s h relative to 0.50 is 0.029, a negligible effect."

### Liu 2026 (2)

Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890

`q2 · i?` · `associational · r2`

Baseline checks within the same blind verification protocol. Position of the two code sets was randomized and showed "No significant position bias" (p = 0.230), and Human vs. Human baseline pairs split nearly evenly across coders, so the aggregate null is not an artifact of presentation order or verifier favoritism.

> "No significant position bias was detected (Option A 47.8% vs. Option B 52.2% of decisive cases, p = 0.230). Among Human vs. Human pairs, decisive preferences split nearly evenly across the three coders (53.6%, 48.2%, 48.1%), confirming that the task admits meaningful discrimination without favoring any individual coder."

## Discussion


## Related Claims
- [Agreement metrics and expert quality judgments diverge in both directions: human consensus can encode shared conservative bias that the verifier rejects in favor of LLM coding](agreement-quality-divergence-human-consensus-bias.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — a narrower finding that bears on this claim
- [On codes requiring recognition of pedagogical intent not explicitly stated, LLMs over-apply and the blind verifier rejects their application in favor of human coding](intent-inference-codes-require-human-coders.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [CLARA annotations align with blinded educator judgments, with 0.81 pairwise agreement and highest-rated educational interpretability](clara-educator-agreement-interpretability.md) — related
- [CLARA achieves the highest agreement with blinded human developmental ranking judgments compared with readability and prompting baselines](clara-highest-human-ranking-agreement.md) — related
- [LLM and human written 7C analyses show no overall difference in behavioral alignment or evidence correspondence, but align less on Communication and Constructive dimensions](llm-7c-analytical-alignment-mixed.md) — related
- [Human raters' preferences align with the LLM judge on TutorBench (Pearson r = 0.82 across metric-level win rates)](human-llm-judge-preference-alignment-deeptutor.md) — related
- [On structured pedagogical-judgment items, all evaluated models share a systematic style-over-fit deviation, converging on the same non-reference option](llm-style-over-fit-uniform-deviation.md) — related
- [The cross-family LLM judge panel agrees with human domain experts on every judged axis, reaching the expert ceiling on answer-holding](educlaw-bench-judge-panel-human-validation.md) — related
