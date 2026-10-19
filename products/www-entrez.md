---
type: product
id: www-entrez
title: WWW Entrez
description: WWW Entrez is an NCBI-developed World Wide Web interface for searching and linking MEDLINE and public nucleotide and protein sequence databases.
product_kind: software
status: review
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: epstein-1994
    resource: "https://eric.ed.gov/?id=ED462262"
    title: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262"
    author: "Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D"
---

# WWW Entrez

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
WWW Entrez is an NCBI-developed World Wide Web interface for searching and linking MEDLINE and public nucleotide and protein sequence databases.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims
- [Some users prefer a single-form Boolean query interface to the original Entrez interface](../claims/single-form-boolean-query-preferred-by-some-users.md) [+W]
- [Browsing term lists (selection mode) helps searchers who do not know the exact query term](../claims/selection-mode-browsing-helps-uncertain-searchers.md) [+W]
- [Internet-based Entrez use grew dramatically in 1994 while CD-ROM subscriptions plateaued](../claims/internet-entrez-use-grew-cd-rom-plateaued.md) [+W]
- [Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor](../claims/retrieval-misses-attributed-to-query-formulation.md) [~W]

## Related Products and Programmes
-

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262

<!-- merged 2026-10-10 from elements/www-entrez-hypertext-retrieval-server ("WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
WWW Entrez is a WWW server interface to NCBI's Entrez retrieval system, which provides "an integrated view of portions of MEDLINE, and all publically available nucleotide and protein databases, including GenBank". It was built from Bourne shell scripts and a C search engine (entrcmd) layered on the NCBI toolbox, supports Boolean queries with inter-database linking and intra-database neighboring, and offers both FORMS-based and non-FORMS interfaces. It serves vt100-class users and links to external web data sources.

## Design Implications

### Context
#### Requirements
- Requires a WWW browser; the entrcmd engine runs only on a UNIX host, though it is layered on the portable NCBI toolbox.
#### Constraints
- Inherently slower than Network Entrez due to shell scripts, statelessness requiring database re-initialization per URL, and transfer of formatted data.
- Display of a large document in an on-demand fashion is impossible; the document must be fetched in its entirety.

### Target Learners
- molecular biologists
- higher education researchers

### Target Learning Goals
- retrieval of biological literature and sequence data to support experimental work

### Claims
<!- - Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] - ->
- [Some users prefer a single-form Boolean query interface to the original Entrez interface](../claims/single-form-boolean-query-preferred-by-some-users.md) [+W]
- [Browsing term lists (selection mode) helps searchers who do not know the exact query term](../claims/selection-mode-browsing-helps-uncertain-searchers.md) [+W]

## Related Elements
- 

## Examples
-

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262
-->

<!-- merged 2026-10-19 from principles/easy-accurate-complete-access-motivates-retrieval-design ("Design retrieval tools for easy, accurate, and complete access to rapidly growing knowledge"), a narrower page folded into its canonical page (fragment step): its body as it stood. Its bullets this page lacked were added above.

# Design retrieval tools for easy, accurate, and complete access to rapidly growing knowledge

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article motivates Entrez by the explosive growth of information molecular biologists must access: the literature adds about 6,000 peer-reviewed articles per month and sequence databases double in size every 20 months. It concludes that "Biologists need a retrieval tool which offers easy, accurate and complete access to this type of information", which drove the design of integrated, linked, and neighboring-based retrieval.

## Design Implications

### Context
#### Requirements
- Pre-computed relationships (BLAST sequence similarity, statistical text neighboring) to support linking within and across databases.
#### Constraints
- 

### Target Learners
- molecular biologists

### Target Learning Objectives
- locating relevant literature and sequence data efficiently

### Claims

- [Internet-based Entrez use grew dramatically in 1994 while CD-ROM subscriptions plateaued](../claims/internet-entrez-use-grew-cd-rom-plateaued.md) [+W]
- [Browsing term lists (selection mode) helps searchers who do not know the exact query term](../claims/selection-mode-browsing-helps-uncertain-searchers.md) [+W]
- [Some users prefer a single-form Boolean query interface to the original Entrez interface](../claims/single-form-boolean-query-preferred-by-some-users.md) [+W]
- [Post-deployment diagnostics attributed many remaining retrieval misses to query formulation, with bounded expansion recovering eleven of 24 original queries without lowering the relevance floor](../claims/retrieval-misses-attributed-to-query-formulation.md) [~W]

## The evidence by question

- *Do retrieval tools that help users who cannot state the exact query (term browsing, query expansion, result summaries) improve what they find?* [Browsing term lists (selection mode) helps searchers who do not know the exact query term](../claims/selection-mode-browsing-helps-uncertain-searchers.md) [+W]

## Related Principles

- [Offer multiple delivery modes of a retrieval resource to complement different user needs](www-entrez.md)

## Examples

- [WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases](../products/www-entrez.md)

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262
-->

<!-- merged 2026-10-19 from principles/complementary-delivery-modes-for-retrieval-tools ("Offer multiple delivery modes of a retrieval resource to complement different user needs"), a narrower page folded into its canonical page (fragment step): its body as it stood. Its bullets this page lacked were added above.

# Offer multiple delivery modes of a retrieval resource to complement different user needs

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

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

- [Design retrieval tools for easy, accurate, and complete access to rapidly growing knowledge](../products/www-entrez.md)

## Examples

- [WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases](../products/www-entrez.md)
- [Offer student success courses in varied content, timing, and delivery modes matched to student needs rather than a one-size-fits-all model](../strategies/varied-delivery-modes-student-success-courses.md)

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262
-->
