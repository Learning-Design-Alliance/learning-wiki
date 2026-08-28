---
okf_version: "0.2"
---

# Learning Design Wiki

<img src="branding/lazuli-wordmark-lapis.svg" alt="Lazuli" width="220">

A persistent, LLM-maintained knowledge base for learning design. Read [CLAUDE.md](CLAUDE.md) for the schema, page templates, and agent operating instructions.

---

## Knowledge Types

### [Principles](principles/index.md) (133)
Research-backed design commitments: what to do and why.

### [Elements](elements/index.md) (240)
Instructional building blocks — the components you compose into patterns.

### [Patterns](patterns/index.md) (77)
Reusable instructional designs at the lesson or unit level.

### [Strategies](strategies/index.md) (1629)
Concrete teaching activity recipes — specific, implementable approaches.

### [Theories](theories/index.md) (12)
Explanatory frameworks that ground principles and claims.

### [Claims](claims/index.md) (27)
Empirical claims with evidence ratings, sources, and competing views.

---

## Quick navigation

* [Ingest & edit log](log.md)
* [Schema & agent guide](CLAUDE.md)
* [Source manifest](https://github.com/Learning-Design-Alliance/learning-wiki/blob/main/sources/manifest.ndjson) — every source article reviewed, ingested or rejected (plain NDJSON, not a wiki page — browse on GitHub or grep it)

## How to use this wiki

**As an agent**: read `CLAUDE.md` first. Use `index.md` as your entry point, follow the markdown links in each page to traverse the graph, and use `grep` for targeted search.

**As a human**: browse the folder indexes above, or open the [docs site](https://learning-design-alliance.github.io/learning-wiki/). Evidence tags (**[+S]**, **[+M]**, **[~M]**, **[-W]**) indicate claim support strength. Pages marked `status: draft` are stubs; `review` pages need expert check; `stable` pages are reliable.
