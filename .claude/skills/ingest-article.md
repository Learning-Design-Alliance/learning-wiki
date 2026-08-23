---
description: Read an education research article (URL, file path, or pasted text) and ingest it into the Learning Design Wiki — creating structured pages for claims, principles, elements, patterns, strategies, and/or theories — then open a pull request for human review.
---

You are ingesting education research into the Learning Design Wiki. Follow these steps exactly. Do not skip steps or batch them up — complete each one before moving on.

## Input

The article source is: $ARGS

- If it looks like a URL, fetch the full text with WebFetch.
- If it looks like a file path, read it with the Read tool.
- If it is pasted text, use it directly.

If no source is provided, ask the user to supply a URL, file path, or the article text.

---

## Step 1 — Read the schema

Read `CLAUDE.md` in full before doing anything else. Pay attention to:
- Page templates for each type (principle, element, pattern, strategy, theory, claim)
- Evidence tags ([+S], [+M], [+W], [~], [-], [X]) and when to use each
- Claim page structure: frontmatter, subclaims, evidence entries, discussion
- Evidence quality tiers (q1–q4) and impact magnitude (i0–i3)
- Cross-link conventions (`[Display Name](slug.md)` same folder, `[Display Name](../folder/slug.md)` a different folder)
- Status values (draft / review / stable)

---

## Step 2 — Extract article metadata

From the article, record:
- **Title**
- **Authors** (Last, First. format)
- **Year**
- **Journal / publisher**
- **DOI or URL**
- **Abstract / main argument** (2–4 sentences)

---

## Step 3 — Identify contributions

Read the article carefully and list what it contributes to the wiki. For each contribution, classify it by type:

- **Claim** — an empirical finding with a measurable effect (requires evidence entry)
- **Principle** — a design recommendation ("do X because Y")
- **Element** — an instructional component described or evaluated (e.g., "retrieval practice", "elaborative interrogation")
- **Pattern** — a reusable instructional design at lesson/unit level
- **Strategy** — a specific, implementable teaching activity recipe
- **Theory** — an explanatory framework named and substantively described

Most papers will primarily contribute **claims** and may also reinforce existing **principles** or **elements**. Be conservative: only create a new page if the article provides meaningful content for it. Cite don't hallucinate — only extract what is actually in the article.

---

## Step 4 — Check existing pages

For each contribution:
1. Search `index.md` for a matching page by name or slug.
2. If uncertain, `grep` the relevant folder for close matches.
3. Classify each as: **new page** (create) or **existing page** (update).

Do not create a new page if a close match exists — update instead.

---

## Step 5 — Create a git branch

Before writing any files:

```bash
git checkout main
git pull
```

Generate a slug from the first author's last name and year: `<lastname>-<year>` (e.g., `roediger-2011`). If the title is more descriptive, use a short title slug (e.g., `spacing-effect-meta-analysis-2019`).

```bash
git checkout -b ingest/<slug>
```

---

## Step 6 — Write claim pages

For each empirical claim the article supports, create or update a claim page in `claims/`.

**New claim slug format:** `<brief-topic>-<mechanism-or-direction>` (e.g., `retrieval-practice-improves-long-term-retention`). Keep it under 60 characters.

Follow the claim template from CLAUDE.md exactly:
- `id:` — use format `CL-<slug-prefix>` (e.g., `CL-rp-1`)
- `evidence_strength:` — strong / moderate / weak / mixed
- Write subclaims: one sentence each, prefixed with `q? i?`, linked to the evidence entry with `[→ Author Year](#author-year)`
- Write the evidence entry: full APA citation with DOI link, quality/impact/n codes with plain-language explanations, then 2–4 sentence description in plain language
- Link any instructional elements mentioned to wiki pages using `[display name](../elements/slug.md)`

---

## Step 7 — Create or update other pages

For each principle, element, pattern, strategy, or theory the article contributes to:

**If updating an existing page:**
- Add the new claim link to the `### Claims` section with the correct evidence tag
- Add the source to `## Key Sources`
- Do not delete or overwrite existing content — add to it
- Update the page's `generated` field (or run `python3 scripts/log_revision.py <page> --by <actor> --type content --desc "..."`, which does this and appends to `log.md` in one step)

**If creating a new page:**
- Use the template from CLAUDE.md for that page type
- Set `status: draft`
- Set `generated: { by: <actor>, at: <today> }`
- Fill in only what the article actually supports — leave optional sections empty rather than inventing content
- Link the relevant claim(s) in the Claims section with evidence tags

---

## Step 8 — Cross-link

For each new page:
1. Identify 2–5 closely related pages already in the wiki (search index.md and grep).
2. Add markdown links (`[Title](../folder/slug.md)`) in the `## Related Principles` / `## Related Elements` / `## Related Claims` section of the new page.
3. Add a reciprocal link on those existing pages pointing back to the new page (append to the relevant section).

---

## Step 9 — Update index.md

For each new page created:
- Run `python3 scripts/build_indexes.py` to regenerate `index.md` and every per-folder index from disk state

---

## Step 10 — Append to log.md

Add one entry per page created or updated:

```
* **Ingest**: [page name](/folder/page.md) — [source title, DOI]
```

under today's `## YYYY-MM-DD` heading (or run `python3 scripts/log_revision.py <page> --by <actor> --type ingest --desc "[source title, DOI]"`, which appends this and updates the page's `generated` field together).

---

## Step 11 — Commit

Stage only the files you created or modified (not bulk `git add .`):

```bash
git add claims/<new-claim>.md
git add principles/<updated>.md   # etc.
git add index.md
git add log.md
git commit -m "Ingest: <Article Title> (<Year>)

Created: <list new pages>
Updated: <list updated pages>

Source: <DOI or URL>"
```

---

## Step 12 — Push and open a pull request

```bash
git push -u origin ingest/<slug>
```

Then create the PR:

```bash
gh pr create \
  --title "Ingest: <Article Title> (<Year>)" \
  --body "$(cat <<'EOF'
## Source

**<Author(s)> (<Year>). <Title>. <Journal>.**
DOI/URL: <doi-or-url>

## Summary

<2–3 sentence plain-language summary of what the article contributes to the wiki.>

## Pages created

<Bulleted list of new pages with their slugs and types.>

## Pages updated

<Bulleted list of existing pages that received new claims or sources.>

## Review checklist

- [ ] Claim evidence entries accurately represent the study design and findings
- [ ] Evidence quality (q) and impact (i) scores are appropriate
- [ ] Evidence tags ([+S], [+M], etc.) on principle/element pages match claim direction
- [ ] New pages follow the correct template structure
- [ ] Wikilinks resolve to real pages
- [ ] index.md counts are correct
EOF
)"
```

---

## Notes

- **Be conservative.** A paper that mentions a concept in passing does not warrant a new page. The article must substantively describe, test, or theorize about something to justify a page.
- **One claim per finding.** If an article reports multiple experiments, create separate subclaims within one claim page rather than multiple claim pages, unless the findings are genuinely distinct constructs.
- **Never hallucinate citations.** Only include studies in evidence entries if they are actually cited in the article you are ingesting.
- **Preserve existing content.** When updating a page, append — never overwrite. Move superseded content to an HTML comment block (`<!-- deprecated -->`).
- **If `gh` is not authenticated**, complete Steps 1–11 then tell the user to run `gh auth login` and provide the exact `gh pr create` command to run manually.
