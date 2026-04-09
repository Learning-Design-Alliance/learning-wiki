# Learning Design Wiki

A persistent, LLM-maintained knowledge base for learning design — research-backed principles, instructional elements, reusable patterns, teaching strategies, theories, and empirical claims, cross-linked and evidence-tagged.

**Browse online:** [learning-design-alliance.github.io/learning-wiki](https://learning-design-alliance.github.io/learning-wiki/)

**Browse locally:** Open this folder as an [Obsidian](https://obsidian.md) vault for the full interactive experience with graph view and backlinks.

---

## What's inside

| Type | Count | Description |
|------|-------|-------------|
| [Principles](principles/) | 133 | Research-backed design commitments — what to do and why |
| [Elements](elements/) | 239 | Instructional building blocks you compose into designs |
| [Patterns](patterns/) | 77 | Reusable designs at lesson or unit level |
| [Strategies](strategies/) | 1604 | Concrete teaching activity recipes |
| [Theories](theories/) | 9 | Explanatory frameworks that ground principles and claims |
| [Claims](claims/) | 19 | Empirical claims with evidence ratings and sources |

---

## Evidence tags

Pages cite empirical claims using direction-and-strength tags:

| Tag | Meaning |
|-----|---------|
| **[+S]** | Supports — strong (meta-analytic or consistent experimental) |
| **[+M]** | Supports — moderate |
| **[+W]** | Supports — weak / emerging |
| **[~S/M/W]** | Contextual / mixed — effect depends on conditions |
| **[-S/M/W]** | Contradicts or reduces effectiveness |
| **[X]** | Contradicted / discredited |

---

## Contributing

This wiki is maintained by LLMs reading education research and ingesting it into structured pages. Human review happens via pull requests.

### Ingest a new article

With [Claude Code](https://claude.ai/code) installed and the repo cloned:

```bash
/ingest-article https://doi.org/10.xxxx/example
```

Or pass a local file path, or paste article text directly after the command. The skill will read the source, extract principles and claims, create or update wiki pages, open a branch, and create a pull request for human review.

**Prerequisites:** `gh` CLI authenticated (`gh auth login`) and write access to this repo.

### Review a contribution

Browse [open pull requests](https://github.com/Learning-Design-Alliance/learning-wiki/pulls). Each PR includes a summary of what was added or changed. Approve, request changes, or close as appropriate.

### Contribute manually

See [CLAUDE.md](CLAUDE.md) for the full schema, page templates, and agent operating guide. Follow the templates and open a pull request against `main`.

---

## Browse locally

**Obsidian (recommended for exploration):** Open this folder as a vault. Wikilinks (`[[page]]`), graph view, and backlinks all work natively.

**Docs site locally:**
```bash
pip install -r requirements-docs.txt
mkdocs serve
# open http://localhost:8000
```

---

## Schema

Pages use structured YAML frontmatter and follow strict templates. See [CLAUDE.md](CLAUDE.md) for:
- Page templates (principle, element, pattern, strategy, theory, claim)
- Evidence tagging system
- Ingest, query, and lint procedures
- Wikilink conventions and folder map

---

## License

Content is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
