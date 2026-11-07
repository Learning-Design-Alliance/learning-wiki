---
type: claim
title: The optimal Critical Score Range for targeted double scoring depends on the configured costs of incorrect pass/fail decisions versus rating cost
description: The optimal Critical Score Range for targeted double scoring depends on the configured costs of incorrect pass/fail decisions versus rating cost
id: optimal-csr-depends-on-loss-cost-configuration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: fu-zhihui-2025
    resource: "https://doi.org/10.1080/10872981.2025.2467477"
    title: "Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan. (2025). Optimizing cost-effectiveness in remote objective structured clinical examinations through targeted double scoring methodologies. Medical Education Online. https://doi.org/10.1080/10872981.2025.2467477"
    author: Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The optimal Critical Score Range for targeted double scoring depends on the configured costs of incorrect pass/fail decisions versus rating cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under the decision-theoretic analysis, the loss-minimizing CSR was the null range when {LP,LF} equaled 40, the full range when it equaled 4,000, and intermediate ranges (e.g., 30–40 in CR; 13–15 or 0–20 in PE; 0–20 in FS) for other configurations. [→ Fu Zhihui 2025](#fu-zhihui-2025)

## Evidence

### Fu Zhihui 2025

Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan. (2025). Optimizing cost-effectiveness in remote objective structured clinical examinations through targeted double scoring methodologies. Medical Education Online. https://doi.org/10.1080/10872981.2025.2467477

`q2 · i?` · `design · r2`

Decision-theoretic analysis of the 550-examinee scoring data, comparing candidate CSRs via a loss function with c fixed at 40 and five {LP,LF} combinations. Intermediate "CSRs: 30–40 in the CR station" minimized loss for the middle configurations, per the article's trial-and-error loss comparison shown in Figure 5.

> "For other sets of {LP,LF}, the estimated expected loss was minimized for the following CSRs: 30–40 in the CR station, 13–15 or 0–20 in the PE station, and 0–20 in the FS station."

## Discussion


## Related Claims
- [Under high configured loss values ({LP,LF} = {4,000,4,000}), universal double scoring is optimal, while under low values ({40,40}) no double scoring minimizes expected loss](extreme-loss-values-flip-optimal-ds-decision.md) — possibly the same claim (merge candidate)
- [TDS outperformed the no-double-scoring baseline in the CR station under all loss configurations except {4,000,4,000}, in the PE station under two configurations, but in no configuration in the FS station](tds-beats-baseline-cr-pe-not-fs.md) — related
