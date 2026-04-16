---
name: wiki-enrich
description: Enrich ld-wiki stub pages for learning design concepts. Use when asked to enrich, fill in, develop, or create wiki pages for principles, elements, patterns, strategies, theories, or claims.
compatibility: Requires access to ld-wiki directory. Uses Google Search for real-world examples and sources.
---

# Wiki Enrich Skill

Enriches stub pages in the ld-wiki learning design knowledge base.

## Quick Start

1. **Read stub**: Find and read the page to enrich.
2. **Read exemplar**: Check [references/exemplars.md](references/exemplars.md) for the correct model.
3. **Research**: Use Google Search for 3-5 peer-reviewed sources (APA + DOI). For the Examples section, find and confirm real URLs for any publicly accessible product, platform, or program.
4. **Draft**: Match exemplar density and voice. Use double-bracket `[[wikilinks]]`. Verify each wikilink slug exists by checking the relevant folder's `index.md` before writing it.
5. **Evidence**: Apply tags from [references/evidence-tags.md](references/evidence-tags.md).
6. **Finalize**: Update `index.md` in the folder and append to `log.md`.

## Key Rules

- **Wikilinks**: Always use `[[folder/slug]]` or `[[folder/slug|Name]]`. Double brackets are mandatory. Confirm slugs exist in the wiki before using them.
- **Evidence Tags**: Link tags to claims: `[[claims/slug]] [+M]`.
- **Sources**: Use real DOIs. In the Examples section, use markdown `[Name](URL)` links for publicly accessible products and programs — search for the URL if you don't know it. Only omit a link if the example has no public URL.
- **Constraints**: Use `[-]` or `[~]` tags for constraints.
- **Missing pages**: If you reference a theory, element, or principle that has no wiki page yet, create a minimal stub (frontmatter + `# Title` only, `status: draft`) in the correct folder and add it to that folder's `index.md`.

## Batch enrichment

When asked to enrich multiple pages of a type:
1. List all `status: draft` pages in the folder.
2. Confirm count with user.
3. Process one at a time.
4. Create stubs for new wikilinks.
5. Update `index.md` once at the end.

See [references/operating-guide.md](references/operating-guide.md) for full schemas.
