#!/usr/bin/env python3
"""
ingest_extractions.py — Convert a completed eval_harness.py run's per-article
extraction JSON into real OKF wiki pages (principles/elements/patterns/
strategies/theories/claims), following CLAUDE.md's page templates and ingest
process (steps 3-7 of "Ingest" in CLAUDE.md): write new pages, regenerate
indexes, and log each one via log_revision.py.

The extraction JSON schema (see scripts/eval/validator.py, the deterministic
half of this project's quality checks) is a deliberately FLATTENED version of
the full page templates — prompts.py's own docstring says as much: it's
condensed so a smaller open-weight model can follow it without tool use.
This script renders exactly what that schema captures into the right
template SHAPE; any template section the schema doesn't cover (e.g. a
Pattern's Sequence/Personalization, a Strategy's Instructions) is left as
the same blank `- ` placeholder bullet CLAUDE.md's own templates use for an
unfilled section — never invented content.

Only creates NEW pages. If a contribution's slug collides with an existing
wiki page, it's skipped with a warning rather than attempted as an automated
merge — CLAUDE.md's "never delete content on update" merge step needs real
editorial judgment this script doesn't have; that page is left for a human
(or a future, smarter merge pass) to reconcile by hand.

Only ingests a record whose structural validation PASSED. A record with
warnings still passes (warnings are normal for a freshly-drafted page — e.g.
missing a target_learners entry) and IS ingested; only a hard structural
error (validator.py's error_count > 0) excludes it, since that means the
model's JSON itself broke the output contract somewhere in that article's
extraction — coarser than ideal (one bad contribution excludes its article's
other, otherwise-fine contributions too) but the safe default for something
headed straight into the wiki via an automated PR.

Usage:
    python3 scripts/ingest_extractions.py --run-id <run_id> --model <model-dirname> \
        [--by <actor>] [--dry-run]

<model-dirname> is the folder under eval/runs/<run-id>/ (see
eval_harness.py's safe_model_dirname()) — e.g. for "google/gemma-4-26b-a4b-it"
that's "google_gemma-4-26b-a4b-it".
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok
from eval import discover_articles

WIKI_ROOT = Path(__file__).parent.parent
EVAL_ROOT = WIKI_ROOT / "eval"
RUNS_DIR = EVAL_ROOT / "runs"
TODAY = date.today().isoformat()

TYPE_TO_FOLDER = {
    "claim": "claims",
    "principle": "principles",
    "element": "elements",
    "pattern": "patterns",
    "strategy": "strategies",
    "theory": "theories",
    "learner-variable": "learner-variables",
}

# Matches okf_lib's own citation-year convention: "(2020)" or "(2020a)".
_YEAR_RE = re.compile(r"\((\d{4}[a-z]?)\)")
_URL_RE = re.compile(r"(https?://[^\s)]+)")


def _one_sentence(text: str, fallback: str) -> str:
    text = (text or "").strip()
    if not text:
        return fallback
    # First sentence only, for a frontmatter `description` — keep it short
    # per OKF's "one-sentence summary" convention rather than dumping the
    # whole description paragraph into frontmatter.
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    sentence = m.group(1) if m else text
    return sentence if len(sentence) <= 220 else sentence[:217].rstrip() + "..."


def _citation_id_author_year(citation: str) -> tuple[str, str | None, str | None]:
    """(slug_id, lead_author_or_None, year_or_None) from a free-text citation string."""
    citation = (citation or "").strip()
    if not citation:
        return "source", None, None
    ym = _YEAR_RE.search(citation)
    if not ym:
        return ok.slugify(" ".join(citation.split()[:5])) or "source", None, None
    year = ym.group(1)
    prefix = citation[: ym.start()].strip().rstrip(".")
    lead_author = prefix.split(",")[0].strip() if prefix else None
    sid = ok.slugify(f"{lead_author}-{year}") if lead_author else ok.slugify(f"source-{year}")
    return sid or "source", (prefix or None), year


def _citation_url(citation: str) -> str | None:
    m = _URL_RE.search(citation or "")
    return m.group(1) if m else None


def _page_link(slug: str, folder: str, from_folder: str) -> str:
    label = slug.replace("-", " ").title()
    return f"[{label}]({ok.to_relative(f'/{folder}/{slug}.md', from_folder)})"


def _bullets(items, formatter=lambda x: str(x)) -> str:
    items = [i for i in (items or []) if i]
    if not items:
        return "- "
    return "\n".join(f"- {formatter(i)}" for i in items)


def _render_claim(contrib: dict, actor: str, slug: str) -> tuple[dict, str]:
    title = (contrib.get("title") or "").strip()
    evidence = [e for e in (contrib.get("evidence") or []) if isinstance(e, dict)]
    subclaims = [s for s in (contrib.get("subclaims") or []) if isinstance(s, dict)]

    anchor_slug = {}   # raw JSON anchor -> heading slug used in the rendered page
    anchor_label = {}  # raw JSON anchor -> human-readable heading label
    used_headings = {}  # base heading slug -> how many evidence entries have used it so far
    ev_blocks = []
    sources = []

    for ev in evidence:
        raw_anchor = str(ev.get("anchor") or "")
        citation = (ev.get("citation") or "").strip()
        sid, author, year = _citation_id_author_year(citation)
        base_label = f"{author.split(',')[0]} {year}".strip() if author and year else (raw_anchor or sid)
        base_label = base_label or sid
        base_slug = ok.slugify(base_label) or sid
        # A study reporting more than one finding is common (e.g. two ANOVA
        # results cited as two separate evidence entries) — without this,
        # both entries collapse onto the SAME "### Author Year" heading and
        # the SAME frontmatter sources[] id, which is wrong twice over: the
        # subclaim -> evidence anchor links become ambiguous, and OKF's
        # sources[] entries are supposed to be unique per id.
        seen = used_headings.get(base_slug, 0)
        used_headings[base_slug] = seen + 1
        if seen:
            heading_slug, label = f"{base_slug}-{seen + 1}", f"{base_label} ({seen + 1})"
        else:
            heading_slug, label = base_slug, base_label
        anchor_slug[raw_anchor] = heading_slug
        anchor_label[raw_anchor] = label

        quality, impact = ev.get("quality"), ev.get("impact")
        codes = " · ".join(x for x in (
            f"q{quality}" if isinstance(quality, int) else None,
            f"i{impact}" if isinstance(impact, int) else None,
        ) if x)
        desc = (ev.get("description") or "").strip()
        quote = (ev.get("source_quote") or "").strip()
        quote_block = f'\n\n> "{quote}"' if quote else ""
        ev_blocks.append(f"### {label}\n\n{citation}\n\n`{codes}`\n\n{desc}{quote_block}\n")

        url = _citation_url(citation)
        source_entry = {"id": heading_slug}
        if url:
            source_entry["resource"] = url
        if citation:
            source_entry["title"] = citation
        if author:
            source_entry["author"] = author
        sources.append(source_entry)

    sc_lines = []
    for sc in subclaims:
        q, i = sc.get("q"), sc.get("i")
        text = (sc.get("text") or "").strip()
        ref = str(sc.get("evidence_ref") or "")
        heading_slug = anchor_slug.get(ref)
        codes = " ".join(x for x in (
            f"q{q}" if isinstance(q, int) else None,
            f"i{i}" if isinstance(i, int) else None,
        ) if x)
        link = f" [→ {anchor_label.get(ref, ref)}](#{heading_slug})" if heading_slug else ""
        sc_lines.append(f"`{codes}` {text}{link}".strip())

    related = [r for r in (contrib.get("related_claims") or []) if isinstance(r, str)]

    body = f"""
# {title}

## Subclaims
{chr(10).join(sc_lines) if sc_lines else '- '}

## Evidence

{chr(10).join(ev_blocks)}
## Discussion


## Related Claims
{_bullets(related, lambda s: _page_link(s, "claims", "claims"))}
"""

    fm = {
        "type": "claim",
        "title": title,
        "description": _one_sentence(title, "Untitled claim"),
        # The slug, not a CL-xxxxxxxx code. A claim's identity is the name a
        # design document cites it by (research:<claim-slug>); a truncated
        # 8-character hash was neither stable nor unique — six such ids were
        # already shared by two pages each. See scripts/page_identity.py.
        "id": slug,
        "status": "draft",
        "generated": {"by": actor, "at": TODAY},
        "evidence_strength": contrib.get("evidence_strength"),
        "sources": sources,
    }
    return fm, body.strip() + "\n"


# Section-heading layout per non-claim type, matching each type's exact
# CLAUDE.md template. Every type shares the same underlying JSON fields
# (validator.py's _validate_other() is one shared check for all five) — only
# the heading wording/nesting differs page to page.
_OTHER_LAYOUT = {
    "principle": {
        "target_goals_heading": "Target Learning Objectives",
        "related_heading": "Related Principles",
        "claims_heading": "Claims",
    },
    "element": {
        "target_goals_heading": "Target Learning Goals",
        "related_heading": "Related Elements",
        "claims_heading": None,  # elements link theory via "Affordances", not a Claims section
    },
    "pattern": {
        "target_goals_heading": "Target Goals",
        "related_heading": "Related Patterns",
        "claims_heading": "Claims",
    },
    "strategy": {
        "target_goals_heading": "Target Learning Goals",
        "related_heading": "Related Strategies",
        "claims_heading": None,
    },
    "theory": {
        "target_goals_heading": "Target Learning Objectives",
        "related_heading": "Related Theories",
        "claims_heading": "Claims",
    },
    "learner-variable": {
        # Same shape as theory — both are canonical concept pages that
        # claims link into as evidence, rather than prescriptive design
        # constructs like principle/pattern/strategy.
        "target_goals_heading": "Target Learning Objectives",
        "related_heading": "Related Learner Variables",
        "claims_heading": "Claims",
    },
}


def _render_other(contrib: dict, ctype: str, actor: str, slug: str) -> tuple[dict, str]:
    folder = TYPE_TO_FOLDER[ctype]
    layout = _OTHER_LAYOUT[ctype]
    title = (contrib.get("title") or "").strip()
    description = (contrib.get("description") or "").strip()

    requirements = _bullets(contrib.get("requirements"))
    constraints = _bullets(contrib.get("constraints"))
    target_learners = _bullets(contrib.get("target_learners"))
    target_goals = _bullets(contrib.get("target_learning_goals"))

    claims_cited = [c for c in (contrib.get("claims_cited") or []) if isinstance(c, dict) and c.get("slug")]

    def _claim_line(c):
        tag = c.get("tag", "")
        link = _page_link(c["slug"], "claims", folder)
        return f"{link} [{tag}]" if tag else link

    claims_block = _bullets(claims_cited, _claim_line)

    related = [r for r in (contrib.get("related") or []) if isinstance(r, str)]
    related_block = _bullets(related, lambda s: _page_link(s, folder, folder))

    theory_supporting = [t for t in (contrib.get("theory_supporting") or []) if isinstance(t, str)]
    theory_block = _bullets(theory_supporting, lambda s: _page_link(s, "theories", folder))

    key_sources = [s for s in (contrib.get("key_sources") or []) if isinstance(s, str) and s.strip()]
    key_sources_block = "\n".join(f"- {s}" for s in key_sources) if key_sources else "- "
    sources = []
    for src in key_sources:
        sid, author, _ = _citation_id_author_year(src)
        entry = {"id": sid, "title": src}
        url = _citation_url(src)
        if url:
            entry["resource"] = url
        if author:
            entry["author"] = author
        sources.append(entry)

    claims_section = ""
    if layout["claims_heading"]:
        claims_section = f"""
### {layout['claims_heading']}
{claims_block}
"""
    else:
        # Elements/strategies fold theory-supported claims under Affordances
        # (element) or leave it implicit (strategy) per their own templates —
        # still surface anything the model tied to a theory, don't drop it.
        if theory_supporting:
            claims_section = f"""
### Affordances
{theory_block}
"""

    body = f"""
# {title}

## Description
{description}

## Design Implications

### Context
#### Requirements
{requirements}
#### Constraints
{constraints}

### Target Learners
{target_learners}

### {layout['target_goals_heading']}
{target_goals}
{claims_section}
## Related {layout['related_heading'].replace('Related ', '')}
{related_block}

## Examples
-

## Key Sources
{key_sources_block}
"""

    fm = {
        "type": ctype,
        # Identity from birth for the kinds a design document points at, so a
        # freshly ingested element resolves without a backfill pass. Strategies
        # and theories are reached through the reverse index, never named.
        **({"id": slug} if folder in ("elements", "principles", "patterns",
                                      "learner-variables") else {}),
        "title": title,
        "description": _one_sentence(description, title or "Untitled"),
        "status": "draft",
        "generated": {"by": actor, "at": TODAY},
        "sources": sources,
    }
    return fm, body.strip() + "\n"


def render_page(contrib: dict, actor: str) -> tuple[str, str, dict, str] | None:
    """Returns (folder, slug, frontmatter_dict, body_markdown) or None if the
    contribution is too malformed to render at all (shouldn't happen for a
    record that already passed structural validation, but defend anyway)."""
    ctype = contrib.get("type")
    slug = contrib.get("slug")
    if ctype not in TYPE_TO_FOLDER or not slug:
        return None
    folder = TYPE_TO_FOLDER[ctype]
    if ctype == "claim":
        fm, body = _render_claim(contrib, actor, slug)
    else:
        fm, body = _render_other(contrib, ctype, actor, slug)
    return folder, slug, fm, body


def ingest_record(record: dict, actor: str, dry_run: bool) -> list:
    """Returns a list of (folder, slug) pages actually written (or that
    WOULD be written, in dry-run mode)."""
    written = []
    validation = record.get("validation") or {}
    if not validation.get("passed"):
        return written
    parsed = record.get("parsed") or {}
    contributions = parsed.get("contributions") or []

    for contrib in contributions:
        if not isinstance(contrib, dict):
            continue
        rendered = render_page(contrib, actor)
        if rendered is None:
            print(f"  [SKIP] {record['article_id']}: unrenderable contribution "
                  f"(type={contrib.get('type')!r}, slug={contrib.get('slug')!r})", file=sys.stderr)
            continue
        folder, slug, fm, body = rendered
        page_path = WIKI_ROOT / folder / f"{slug}.md"
        if page_path.exists():
            print(f"  [SKIP] {folder}/{slug}.md already exists — not auto-merging, "
                  f"leave for manual review", file=sys.stderr)
            continue

        text = ok.dump_frontmatter(fm) + "\n" + body
        if dry_run:
            print(f"  [DRY-RUN] would write {folder}/{slug}.md")
        else:
            (WIKI_ROOT / folder).mkdir(exist_ok=True)
            page_path.write_text(text, encoding="utf-8")
            print(f"  [OK] wrote {folder}/{slug}.md")
        written.append((folder, slug, record["article_id"], record["article_title"]))

    return written


def gate_citations(pages: list) -> dict:
    """Run the citation gate over the pages a source just wrote.

    Gate 3. Gates 1 and 2 — structural validation and the enrichment-time
    Crossref check — already existed, but nothing connected either to the
    manifest, so `sources/manifest.ndjson` recorded "ingested" for a source
    whose pages carried a DOI resolving to the wrong paper. Structural
    validity is the weakest of the three checks and the one least likely to
    catch what actually goes wrong.

    Returns {"checked", "crossref_reachable", "removed", "flagged"}.

    The two failure kinds are kept apart on purpose. A Crossref lookup that
    could not complete is an outage, not a finding — recording it as a citation
    issue would fill the manifest with noise during any network blip and, worse,
    make a clean ingest during an outage indistinguishable from a dirty one.
    So outage lines set crossref_reachable: false, and only genuine findings —
    a DOI on two papers, invented journal metadata, an invented title — become
    `flagged`. This is the same distinction that keeps classify_doi from
    treating "error" as "wrong paper"."""
    import io, contextlib
    try:
        import enrich
    except Exception as e:                       # pragma: no cover - import guard
        return {"checked": False, "error": f"gate unavailable: {e}"}

    # Lines the gate prints that mean "could not check", not "found a problem".
    OUTAGE = ("resolve failed", "citation unchecked", "check skipped", "skipped:")
    FINDING = ("[citation metadata]", "[citation title]", "[DOI collision]")

    removed, flagged, ran, reachable = [], [], False, True
    for rel in pages:
        path = WIKI_ROOT / rel
        if not path.exists():
            continue
        buf = io.StringIO()
        try:
            # verify_page_citations reports collisions, fabricated journal
            # metadata and invented titles on stderr, and returns the DOIs it
            # actually stripped. Both matter: a strip is a defect it fixed, a
            # report is one it found and left for a human.
            with contextlib.redirect_stderr(buf):
                dropped = enrich.verify_page_citations(path, apply=True)
            ran = True
        except Exception as e:
            flagged.append(f"{rel}: gate error: {e}")
            continue
        for d in dropped:
            removed.append(f"{rel}: {d['doi']} ({d.get('status')})")
        for line in buf.getvalue().splitlines():
            s = line.strip()
            if any(o in s for o in OUTAGE):
                reachable = False
            elif s.startswith(FINDING):
                flagged.append(s)
    return {"checked": ran, "crossref_reachable": reachable,
            "removed": removed, "flagged": flagged}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-id", required=True, help="eval/runs/<run-id> to ingest from")
    parser.add_argument("--model", required=True, help="Model dirname under eval/runs/<run-id>/ (safe_model_dirname form)")
    parser.add_argument("--by", default="claude/unspecified", help="Actor for generated.by / log_revision.py --by")
    parser.add_argument("--dry-run", action="store_true", help="Report what would be written without touching the wiki")
    args = parser.parse_args()

    model_dir = RUNS_DIR / args.run_id / args.model
    if not model_dir.is_dir():
        print(f"[ERROR] {model_dir} not found. Run eval_harness.py's `run` command first, "
              f"or check --run-id/--model.", file=sys.stderr)
        sys.exit(1)

    result_files = sorted(model_dir.glob("*.json"))
    if not result_files:
        print(f"[ERROR] No result files in {model_dir}.", file=sys.stderr)
        sys.exit(1)

    print(f"Ingesting {len(result_files)} extraction record(s) from {model_dir}"
          f"{' (dry run)' if args.dry_run else ''}...\n")

    all_written = []
    article_registry_entries = {}  # article_id -> {outcome, run_id, model, pages} for the
                                    # processed-articles registry (see discover_articles.py) —
                                    # covers EVERY article this run touched, not just ingested
                                    # ones, so a validation-failure isn't re-generated later either.
    n_skipped_validation = 0
    for path in result_files:
        record = json.loads(path.read_text(encoding="utf-8"))
        article_id = record["article_id"]
        validation = record.get("validation") or {}
        if not validation.get("passed"):
            n_skipped_validation += 1
            print(f"  [SKIP] {article_id}: structural validation did not pass "
                  f"({validation.get('error_count', '?')} error(s)) — not ingesting any of "
                  f"this article's contributions", file=sys.stderr)
            reason = None
            if not args.dry_run:
                if validation.get("parse_error"):
                    reason = f"parse error: {validation['parse_error']}"
                elif not validation.get("n_contributions"):
                    reason = "no extractable contributions (out of scope or no learning-design content found)"
                else:
                    reason = f"{validation.get('error_count', '?')} structural validation error(s)"
                ok.append_manifest_entry(
                    source_id=article_id,
                    title=record.get("article_title", ""),
                    status="rejected",
                    reason=reason,
                )
            # article_registry_entries feeds discover_articles.record_processed_articles()
            # below (eval/corpus/processed_articles.json) — a separate, scraper-specific
            # mechanism from the sources/manifest.ndjson append above: the manifest is a
            # general append-only audit log (any pipeline, human-browsable on GitHub), this
            # registry tracks `attempts` so a validation_failed article gets a bounded number
            # of retries across future discovery batches instead of the manifest's flat
            # "rejected" verdict treating it as permanent. Both stay populated in dry-run mode
            # (matching pre-merge behavior) since the enclosing `if args.dry_run: return`
            # below means neither ever actually gets persisted to disk in that case.
            article_registry_entries[article_id] = {
                "outcome": "validation_failed", "run_id": args.run_id, "model": args.model,
                "pages": [], "reason": reason,
            }
            continue
        print(f"[{article_id}] {record.get('article_title', '')}")
        written = ingest_record(record, args.by, args.dry_run)
        all_written.extend(written)
        if written and not args.dry_run:
            page_paths = [f"{folder}/{slug}.md" for folder, slug, *_ in written]
            citations = gate_citations(page_paths)
            if citations["removed"]:
                print(f"  [citations] stripped {len(citations['removed'])} unverifiable "
                      f"DOI(s) from this source's pages", file=sys.stderr)
            if citations["flagged"]:
                print(f"  [citations] {len(citations['flagged'])} citation issue(s) "
                      f"recorded in the manifest for review", file=sys.stderr)
            if not citations["checked"]:
                print(f"  [citations] gate could not run — manifest records this ingest "
                      f"as unverified", file=sys.stderr)
            ok.append_manifest_entry(
                source_id=article_id,
                title=record.get("article_title", ""),
                status="ingested",
                pages=page_paths,
                citations=citations,
            )
        article_registry_entries[article_id] = {
            "outcome": "ingested" if written else "no_new_pages",
            "run_id": args.run_id, "model": args.model,
            "pages": [f"{folder}/{slug}.md" for folder, slug, _, _ in written],
        }

    print(f"\n{len(all_written)} page(s) {'would be ' if args.dry_run else ''}written, "
          f"{n_skipped_validation} article(s) skipped (failed structural validation).")

    if args.dry_run:
        return

    if all_written:
        print("\nRegenerating index.md files...")
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "build_indexes.py")], check=True, cwd=WIKI_ROOT)

        print("Logging each new page (revision card + log.md)...")
        for folder, slug, article_id, article_title in all_written:
            subprocess.run([
                sys.executable, str(WIKI_ROOT / "scripts" / "log_revision.py"),
                f"{folder}/{slug}.md",
                "--by", args.by,
                "--type", "ingest",
                "--desc", f"Ingested from {article_id} ({article_title}) via eval_harness.py + ingest_extractions.py",
            ], check=True, cwd=WIKI_ROOT)

    if article_registry_entries:
        discover_articles.record_processed_articles(article_registry_entries)
        print(f"\nRecorded {len(article_registry_entries)} article outcome(s) in "
              f"eval/corpus/processed_articles.json — future discovery batches will exclude these ids.")

    print(f"\nDone. {len(all_written)} new page(s), indexes regenerated, log.md updated.")
    print("Review the diff before committing — this is draft-quality, machine-ingested content "
          "(status: draft, no `verified` entry) per CLAUDE.md's trust-tier convention.")


if __name__ == "__main__":
    main()
