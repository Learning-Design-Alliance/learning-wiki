---
type: element
id: www-entrez-hypertext-retrieval-server
title: "WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases"
description: "WWW Entrez is a WWW server interface to NCBI's Entrez retrieval system, which provides \"an integrated view of portions of MEDLINE, and all publically available nucleotide and protein databases, including GenBank\"."
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

# WWW Entrez: a hypertext web interface to integrated molecular biology literature and sequence databases

> **Element** · [All elements](index.md)

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

## Related Elements
- 

## Examples
-

## Key Sources
- Epstein, Jonathan A., Kans, Jonathan A., & Schuler, Gregory D. (1994). WWW Entrez: A Hypertext Retrieval Tool for Molecular Biology. https://eric.ed.gov/?id=ED462262
