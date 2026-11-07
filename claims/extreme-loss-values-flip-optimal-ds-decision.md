---
type: claim
title: "Under high configured loss values ({LP,LF} = {4,000,4,000}), universal double scoring is optimal, while under low values ({40,40}) no double scoring minimizes expected loss"
description: "Under high configured loss values ({LP,LF} = {4,000,4,000}), universal double scoring is optimal, while under low values ({40,40}) no double scoring minimizes expected loss"
id: extreme-loss-values-flip-optimal-ds-decision
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
  - id: fu-zhihui-2025-2
    resource: "https://doi.org/10.1080/10872981.2025.2467477"
    title: "Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan. (2025). Optimizing cost-effectiveness in remote objective structured clinical examinations through targeted double scoring methodologies. Medical Education Online. https://doi.org/10.1080/10872981.2025.2467477"
    author: Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Under high configured loss values ({LP,LF} = {4,000,4,000}), universal double scoring is optimal, while under low values ({40,40}) no double scoring minimizes expected loss

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` When {LP,LF} equaled {40,40}, the null CSR minimized expected loss (no double scoring optimal); when LP and LF were set at 4,000, expected loss reached its minimum of 40 for full-range CSRs (0–60 in CR, 0–20 in PE and FS), making all double scoring optimal. [→ Fu Zhihui 2025](#fu-zhihui-2025)
`q2 i?` Summed minimum costs across the three stations were 29.82, 117.16, 104.15, 96.87, and 120 for the five {LP,LF} combinations in order. [→ Fu Zhihui 2025](#fu-zhihui-2025)

## Evidence

### Fu Zhihui 2025

Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan. (2025). Optimizing cost-effectiveness in remote objective structured clinical examinations through targeted double scoring methodologies. Medical Education Online. https://doi.org/10.1080/10872981.2025.2467477

`q2 · i?` · `design · r2`

Decision-theoretic loss comparison over candidate CSRs in the 550-examinee dataset. At the high-loss extreme, "the loss incurred from incorrect pass/fail decisions exceeded the cost of Double Scoring", making full-range double scoring optimal; at {40,40} the null CSR was optimal because incorrect decisions were cheaper than double scoring.

> "When LP and LF were set at 4,000, the loss incurred from incorrect pass/fail decisions exceeded the cost of Double Scoring (DS), rendering such incorrect decisions nearly unacceptable."

### Fu Zhihui 2025 (2)

Fu Zhihui, Wu Yuhong, Xu Lingling, Cai Fen, Liu Ren, Jiang Zhehan. (2025). Optimizing cost-effectiveness in remote objective structured clinical examinations through targeted double scoring methodologies. Medical Education Online. https://doi.org/10.1080/10872981.2025.2467477

`q2 · i?` · `design · r2`

Station-level minimum expected losses from the same decision-theoretic analysis. The five {LP,LF} configurations yielded the printed per-station minimum costs, e.g., "in CR station, minimum costs were 7.13, 38.69, 24.15, 16.87, and 40", summing to 29.82, 117.16, 104.15, 96.87, and 120 across stations.

> "Setting {LP,LF} values to {40, 40}, {800, 200}, {400, 400}, {200, 800}, and {4,000, 4,000} correspondingly yielded minimum costs as follows: (1) in CR station, minimum costs were 7.13, 38.69, 24.15, 16.87, and 40; (2) in PE station, minimum costs were 10.25, 38.47, 40, 40, and 40; (3) in FS station, minimum costs were 12.44, 40, 40, 40, and 40."

## Discussion


## Related Claims
- [The optimal Critical Score Range for targeted double scoring depends on the configured costs of incorrect pass/fail decisions versus rating cost](optimal-csr-depends-on-loss-cost-configuration.md) — possibly the same claim (merge candidate)
- [TDS outperformed the no-double-scoring baseline in the CR station under all loss configurations except {4,000,4,000}, in the PE station under two configurations, but in no configuration in the FS station](tds-beats-baseline-cr-pe-not-fs.md) — related
