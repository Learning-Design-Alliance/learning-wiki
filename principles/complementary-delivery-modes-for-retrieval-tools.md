---
type: principle
id: complementary-delivery-modes-for-retrieval-tools
title: Offer multiple delivery modes of a retrieval resource to complement different user needs
description: "The article concludes that the CD-ROM, client/server, and WWW implementations of Entrez \"complement, rather than compete with one another\": WWW Entrez suits users who prefer a single software tool and can accept slowe..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: epstein-1994
    resource: "https://eric.ed.gov/?id=ED462262"
    title: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262"
    author: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D"
---

# Offer multiple delivery modes of a retrieval resource to complement different user needs

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 for) · 1 study, `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article concludes that the CD-ROM, client/server, and WWW implementations of Entrez "complement, rather than compete with one another": WWW Entrez suits users who prefer a single software tool and can accept slower performance, while Network Entrez is critical for high performance and custom applications. Maintaining alternate implementations also provides a fallback when one service fails for a user.

## Design Implications

### Context
#### Requirements
- Each mode must be maintained against its own constraints, e.g. CD-ROM capacity limits and WWW statelessness overhead.
#### Constraints
- WWW Entrez is useful only for users who can accept slower performance; Network Entrez requires local administrator support at each site.

### Target Learners
- molecular biologists

### Target Learning Objectives
- access to integrated biological literature and sequence data

### Claims

- [Internet Entrez Use Grew Cd Rom Plateaued](../claims/internet-entrez-use-grew-cd-rom-plateaued.md) [+M]
- [Some users prefer a single-form Boolean query interface to the original Entrez interface](../claims/single-form-boolean-query-preferred-by-some-users.md) [+W]
- [Browsing term lists (selection mode) helps searchers who do not know the exact query term](../claims/selection-mode-browsing-helps-uncertain-searchers.md) [+W]

## Related Principles

- [Design retrieval tools for easy, accurate, and complete access to rapidly growing knowledge](easy-accurate-complete-access-motivates-retrieval-design.md)

## Examples

- [WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases](../elements/www-entrez-hypertext-retrieval-server.md)

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262
