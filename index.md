---
okf_version: "0.2"
---

# Learning Design Wiki

A persistent, LLM-maintained knowledge base for learning design. Read [CLAUDE.md](CLAUDE.md) for the schema, page templates, and agent operating instructions.

## Read this first

- **Models wrote this wiki, and no person has yet checked any page.** Every page's *Page metadata* panel shows its trust tier; today all of them read *unverified*. Treat a page as a well-sourced lead, and check the cited study before relying on a detail.
- **Most claims rest on one study.** A claim page reports what one or a few studies found, in the conditions they ran. Where several studies bear on one question, a table on the claim page lists them one row each; nothing is averaged into a verdict.
- **Every study carries codes.** `q1`–`q4` is the design tier (q4: a pre-registered trial or well-powered meta-analysis; q1: a case study or argument). `i1`–`i3` is the size of a printed effect (small, medium, large); `i?` means the source printed none, which is not the same as no effect. `causal · r2` names the kind of evidence and how well it was done for its kind (r1–r3). The [evidence report](evidence.md) shows the state of it all.
- **Markers on design pages** say how a claim bears on the page: `+` supports, `~` depends on conditions, `-` counts against, and `S`/`M`/`W` how strong, capped by the claim's recorded evidence.
- **Principle and pattern pages say what is tested and what is not.** A design marked *Default design, while the relationship is untested* is a labelled proposal, not a finding.
- **Found an error?** Open an issue on [GitHub](https://github.com/Learning-Design-Alliance/learning-wiki/issues) with the page and the source.

---

## Knowledge Types

### [Principles](principles/index.md) (170)
Research-backed design commitments: what to do and why.

### [Elements](elements/index.md) (1057)
Instructional building blocks — the components you compose into patterns.

### [Patterns](patterns/index.md) (54)
Reusable instructional designs at the lesson or unit level.

### [Designs](designs/index.md) (1045)
Designs for a particular setting, course, population or product: what a design uses the general patterns for. A pattern is general across contexts; a design is not.

### [Products & Programmes](products/index.md) (1950)
Named products and programmes others adopt: software and platforms, curricula, assessments and instruments, datasets, and branded programmes and initiatives, each with its own frameworks and the evidence about it. A design is one setting's.

### [Strategies](strategies/index.md) (6797)
Concrete teaching activity recipes — specific, implementable approaches.

### [Design Processes](processes/index.md) (18)
How a course gets designed — whole-process models a designer works through, rather than anything a learner meets.

### [Design Methods](methods/index.md) (37)
The practices a design process is made of — analysis, elicitation, mapping and evaluation work done on the design, not in the classroom.

### [Research Methods](research-methods/index.md) (653)
Methods for studying learning and evaluating education that are specific to it or especially useful in it. General social-science methods are not listed.

### [Theories](theories/index.md) (1360)
Explanatory frameworks that ground principles and claims.

### [Learner Variables](learner-variables/index.md) (75)
Canonical learner characteristics claims report findings about — one page per variable, so the same concept does not fragment across differently-worded tags.

### [Claims](claims/index.md) (27710)
Empirical claims with evidence ratings, sources, and competing views.

---

## Quick navigation

* [Ingest & edit log](https://github.com/Learning-Design-Alliance/learning-wiki/blob/main/log.md) (current month; earlier months in `log/`)
* [Schema & agent guide](CLAUDE.md)

## How to use this wiki

**As an agent**: read `CLAUDE.md` first. Use `index.md` as your entry point, follow the markdown links in each page to traverse the graph, and use `grep` for targeted search.

**As a human**: browse the folder indexes above, or search from the box at the top of every page (on GitHub, read the wiki at [wiki.learningdesignalliance.org](https://wiki.learningdesignalliance.org/)). Evidence tags (**[+S]**, **[+M]**, **[~M]**, **[-W]**) indicate claim support strength. Pages marked `status: draft` are stubs or unreviewed; `review` pages have content that needs an expert's check.
