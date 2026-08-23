# Contributing to the Learning Design Wiki

This wiki is a persistent, LLM-maintained knowledge base — see [CLAUDE.md](CLAUDE.md) for the schema, page templates, and the [Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) it's built on. This file covers the *process* for getting a change merged.

## Automated checks

Every pull request runs `python3 scripts/lint.py` and `mkdocs build --strict` via GitHub Actions (`.github/workflows/validate.yml`). Both must pass before merge:

- `lint.py` checks broken cross-links, missing evidence strength / DOIs, principles with no linked claim, draft pages with no description, and `status: stable` pages missing a `verified` entry.
- `mkdocs build --strict` catches broken internal links and anchors that `lint.py` doesn't (e.g. anchor fragments that don't match a heading's actual generated id).

These catch mechanical problems — they don't tell you whether a claim is accurately described or a citation says what the page says it says. That's what review is for.

## Review policy

- **External contributions** (anyone without write access) require at least one maintainer approval before merge, in addition to passing checks.
- **Maintainers** may merge their own pull requests without a second approval when the change is infrastructure/tooling/mechanical (scripts, schema, formatting) and backed by passing automated checks — the checks are the review, in that case. This is configured as a bypass list on the branch's ruleset, not a blanket exemption from scrutiny.
- **Content changes** — a new or edited claim, a citation, an evidence tag, anything where the question is "does this accurately represent the source" — should still get an explicit second look, even from a maintainer, because `lint.py` and `mkdocs` can't check that. Once someone has actually done that check, record it:

  ```bash
  python3 scripts/log_revision.py <page> --by human:<id> --type status --desc "Reviewed for accuracy" --verify
  ```

  This appends a `verified: {by, at}` entry to the page (see "Trust tiers" in [CLAUDE.md](CLAUDE.md)) — distinct from `evidence_strength`, which describes the underlying research, not whether this page has been checked against it.

The short version: bypassing review is for changes where an automated check can tell you if something's wrong. For changes where only a human reading the source material can tell, get a human to actually read it, and record that they did.

## Making a change

1. Open a pull request against `main`.
2. Make sure `scripts/lint.py` passes locally before pushing — `python3 scripts/lint.py`.
3. For a new or updated page, follow the template for its type in [CLAUDE.md](CLAUDE.md).
4. See [README.md](README.md) for the `/ingest-article` skill, which automates turning a source article into wiki pages and opening a PR.
