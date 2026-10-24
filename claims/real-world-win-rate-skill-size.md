---
type: claim
title: On real-world data, the proposed method maintains high win rates as the number of skills increases, performing strongly on ACE and MSE
description: On real-world data, the proposed method maintains high win rates as the number of skills increases, performing strongly on ACE and MSE
id: real-world-win-rate-skill-size
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ryosuke-nagai-2026
    resource: "https://doi.org/10.48550/arxiv.2606.20611"
    title: "Ryosuke Nagai, Kyohei Atarashi, Koh Takeuchi, Jill-Jênn Vie, and Hisashi Kashima. (2026). Estimating Learners' Skill Acquisition Without Temporal Information. https://arxiv.org/abs/2606.20611 [doi:10.48550/arxiv.2606.20611](https://doi.org/10.48550/arxiv.2606.20611)"
    author: Ryosuke Nagai, Kyohei Atarashi, Koh Takeuchi, Jill-Jênn Vie, and Hisashi Kashima
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On real-world data, the proposed method maintains high win rates as the number of skills increases, performing strongly on ACE and MSE

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Consistent with synthetic experiments, the proposed method maintains high win rates against baselines as the number of skills increases, with consistent strength on ACE and MSE. [→ Ryosuke Nagai 2026](#ryosuke-nagai-2026)

## Evidence

### Ryosuke Nagai 2026

Ryosuke Nagai, Kyohei Atarashi, Koh Takeuchi, Jill-Jênn Vie, and Hisashi Kashima. (2026). Estimating Learners' Skill Acquisition Without Temporal Information. https://arxiv.org/abs/2606.20611 [doi:10.48550/arxiv.2606.20611](https://doi.org/10.48550/arxiv.2606.20611)

`q2 · i?` · `design · r2`

Figure-based numerical result on the ASSISTments real-world data (15 skills), reporting win rates versus skill size. The article attributes this to "better calibration and lower prediction error under higher-dimensional skill settings."

> "Figure 5 shows that the proposed method maintains high win rates against baselines as the number of skills increases. In particular, it consistently performs strongly on ACE and MSE"

## Discussion


## Related Claims
- [On the ASSISTments real-world benchmark, the proposed method achieves the best performance across all metrics, significantly outperforming all baselines](assistments-real-world-best-all-metrics.md) — related
- [The proposed method's advantage grows or holds as the skill space expands and under higher noise rates in synthetic experiments](robustness-to-skill-size-and-noise-synthetic.md) — related
- [The proposed snapshot-based method consistently outperforms baselines on synthetic next-skill prediction across all metrics except accuracy](synthetic-next-skill-prediction-outperforms-baselines.md) — related
