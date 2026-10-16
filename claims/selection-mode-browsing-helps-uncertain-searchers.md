---
type: claim
title: Browsing term lists (selection mode) helps searchers who do not know the exact query term
description: Browsing term lists (selection mode) helps searchers who do not know the exact query term
id: selection-mode-browsing-helps-uncertain-searchers
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: weak
sources:
  - id: epstein-1994
    resource: "https://eric.ed.gov/?id=ED462262"
    title: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262"
    author: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Browsing term lists (selection mode) helps searchers who do not know the exact query term

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Evidence quality** · No study behind this claim is a peer-reviewed article with a DOI: it rests on an ERIC document (a report, conference paper or thesis). It is kept because 2 design pages cite it; treat it as a lead to check, not an established finding.

## Subclaims
`q2 i?` Continuous scrolling through alphabetical term lists is valuable because users do not always know the exact query term or author name. [→ Epstein 1994](#epstein-1994)

## Evidence

### Epstein 1994

Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262

`q2 · i?` · `design · r2`

The authors' ergonomic analysis of the Entrez interface reports, from experience, that "selection mode" scrolling of alphabetical term lists is valuable because "users don't always know the exact query term or author name". No effect size is reported.

> "Experience shows that this scrolling ("selection mode") is a valuable feature of Entrez, since users don't always know the exact query term or author name."

## Studies bearing on this claim

<!-- synthesis:start -->
*Do retrieval tools that help users who cannot state the exact query (term browsing, query expansion, result summaries) improve what they find?* This table gathers the studies behind this claim and the 2 narrower claims that bear on it: **3 distinct studies** (2 design, 1 causal), `q2`, 0 of 3 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Epstein 1994 | q2 · design · r2 | i? | this claim |
| [Sidney Shapiro and Joshua Lindemann 2026](https://doi.org/10.48550/arxiv.2610.02510) | q2 · design · r2 | i? | [Post-deployment diagnostics attributed many remaining retrieval misses to query formulatio](retrieval-misses-attributed-to-query-formulation.md) (supports) |
| [Yifan Liu 2026](https://doi.org/10.48550/arxiv.2606.08936) | q2 · causal · r? | i? | [AI overviews in an academic search engine showed mixed effects: summaries may reduce menta](ai-overviews-mixed-effects-academic-search.md) (qualifies) |
<!-- synthesis:end -->

## Discussion


## Related Claims
- [Internet-based Entrez use grew dramatically in 1994 while CD-ROM subscriptions plateaued](internet-entrez-use-grew-cd-rom-plateaued.md) — related
- [Some users prefer a single-form Boolean query interface to the original Entrez interface](single-form-boolean-query-preferred-by-some-users.md) — related
- Some users prefer to search by people groups, contexts and institutions rather than by subject categories, and some will not explore complex structures or long lists — related
