# Canonical SLA theory hubs — task for an in-session agent

The wiki's theory pages are framed one source at a time ("Swain's output hypothesis with three
functions", "Krashen's five hypotheses as principles for bilingual programs"). A course designer
looking for *the* output hypothesis finds three fragments and no page that says what the theory
claims, what tests it, and where it fails. A hub is that page. It does not replace the fragments:
they stay, and the hub links them.

## What a hub is

`theories/<slug>.md`, in the Theory template from CLAUDE.md (frontmatter `type: theory`, the H1 equal
to `title:`, the banner `> **Theory** · [All theories](index.md)` under the H1), with:

- **Description**: what the theory proposes and its mechanism, in 2–4 short paragraphs, written
  **only from what the fetched articles say about it** (the passages you read in
  `eval/corpus/cache/<id>.txt`), not from memory. Where the articles disagree about it, say so.
- **Implications**: Context / Target Learners / Target Learning Objectives, for adult learners
  where the sources speak to it. Keep it to what the sources support.
- **Claims**: wiki claim pages that test or bear on the theory, each as
  `[claim title](../claims/<slug>.md) [marker]`. The marker's polarity is how the claim bears on the
  theory (`+` supports, `~` depends on conditions, `-` against). Its strength may never exceed the
  claim's own recorded evidence: S only when the claim has 2+ distinct studies and one at q3+, M
  when it has a study at q2+, else W (`scripts/link_pages.py`'s `strength_cap` is the rule). Read
  each claim page before linking it; link only claims that actually bear on this theory.
- **Related Theories**: the source-framed variants of this theory and neighbouring theories, as
  `[title](slug.md)` links.
- **Examples**: strategies, elements, patterns or principles in the wiki that apply the theory, only
  where the page itself names or plainly enacts it.
- **Key Sources**: the theory's primary works, **each resolved against Crossref**
  (`https://api.crossref.org/works/<doi>?mailto=contact@learningdesignalliance.org`, or a Crossref
  bibliographic query for a work you do not have a DOI for) with author, year and title agreeing. Take
  the citation from how the fetched articles cite the work, then check it. A book with no DOI is
  cited as the articles cite it, with no DOI. Never write a DOI you have not resolved to that work.
- An HTML comment right after the banner:
  `<!-- Hub page (2026-09-30). The Description is compiled from the fetched articles that discuss this
  theory: <ids>. The primary works in Key Sources were verified against Crossref but not read. -->`
- `status: draft` (the description is secondhand), `generated: {by: claude/unspecified, at: 2026-09-30}`,
  and a one-sentence `description:`.

Then, on each source-framed variant page the hub links, add one bullet under its
`## Related Theories` (create the heading before `## Examples` or `## Key Sources` if missing):
`- [<hub title>](<hub-slug>.md) — the canonical page for this theory`. Change nothing else on it.

## Rules

- Check the slug does not exist (`ls theories/<slug>.md`), and search for an existing canonical page
  first (`grep -il "<name>" theories/*.md`). If one exists and is canonical, improve that page instead
  of adding a hub, and say so.
- Never touch claim pages, never add `verified:`, never commit or push; another session commits.
- Do not edit `index.md` files; run nothing but `python3 scripts/lint.py` at the end (must be 0 for
  your pages; report anything else).
- Report: each hub written (slug, how many claims linked and with which markers, key sources and how
  each was verified), each variant page touched, and anything you could not establish.
