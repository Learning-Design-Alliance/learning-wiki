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
_URL_RE = re.compile(r"(https?://(?:[^\s()<>]|\([^\s()]*\)|<[^\s()<>]*>)+)")  # balanced parens are part of a DOI; see okf_lib.LINK_URL



def _impact_code(obj: dict, key: str) -> str | None:
    """`i2` for a coded magnitude, `i?` for an explicit null (the article prints
    no effect size, so someone looked and could not say), nothing when the key
    is absent. The `?` is the corpus's existing spelling for that state, and
    okf_lib.parse_evidence_codes and sync_evidence_codes already carry it."""
    if key not in obj:
        return None
    value = obj[key]
    if value is None:
        return "i?"
    return f"i{value}" if isinstance(value, int) and not isinstance(value, bool) else None

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


def _evidence_headings(evidence: list) -> list[dict]:
    """The `### Author Year` heading each evidence entry renders under, in order.

    One function, used by the claim renderer AND by the observation record, so
    the anchor a record names is by construction the heading the page carries.
    A study reporting more than one finding is common (e.g. two ANOVA results
    cited as two separate evidence entries). Without the suffixing below, both
    entries collapse onto the SAME heading and the SAME frontmatter sources[]
    id, which is wrong twice over: the subclaim -> evidence anchor links become
    ambiguous, and OKF's sources[] entries are supposed to be unique per id."""
    used_headings = {}  # base heading slug -> how many evidence entries have used it so far
    out = []
    for ev in evidence:
        raw_anchor = str(ev.get("anchor") or "")
        citation = (ev.get("citation") or "").strip()
        sid, author, year = _citation_id_author_year(citation)
        base_label = f"{author.split(',')[0]} {year}".strip() if author and year else (raw_anchor or sid)
        base_label = base_label or sid
        base_slug = ok.slugify(base_label) or sid
        seen = used_headings.get(base_slug, 0)
        used_headings[base_slug] = seen + 1
        if seen:
            heading_slug, label = f"{base_slug}-{seen + 1}", f"{base_label} ({seen + 1})"
        else:
            heading_slug, label = base_slug, base_label
        out.append({"ev": ev, "raw_anchor": raw_anchor, "citation": citation, "author": author,
                    "sid": sid, "heading_slug": heading_slug, "label": label})
    return out


def _render_claim(contrib: dict, actor: str, slug: str) -> tuple[dict, str]:
    title = (contrib.get("title") or "").strip()
    evidence = [e for e in (contrib.get("evidence") or []) if isinstance(e, dict)]
    subclaims = [s for s in (contrib.get("subclaims") or []) if isinstance(s, dict)]

    anchor_slug = {}   # raw JSON anchor -> heading slug used in the rendered page
    anchor_label = {}  # raw JSON anchor -> human-readable heading label
    ev_blocks = []
    sources = []

    for h in _evidence_headings(evidence):
        ev, raw_anchor, citation, author = h["ev"], h["raw_anchor"], h["citation"], h["author"]
        heading_slug, label = h["heading_slug"], h["label"]
        anchor_slug[raw_anchor] = heading_slug
        anchor_label[raw_anchor] = label

        quality = ev.get("quality")
        codes = " · ".join(x for x in (
            f"q{quality}" if isinstance(quality, int) else None,
            _impact_code(ev, "impact"),
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
        q = sc.get("q")
        text = (sc.get("text") or "").strip()
        ref = str(sc.get("evidence_ref") or "")
        heading_slug = anchor_slug.get(ref)
        codes = " ".join(x for x in (
            f"q{q}" if isinstance(q, int) else None,
            _impact_code(sc, "i"),
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
                                      "learner-variables", "strategies") else {}),
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


CACHE_DIR = WIKI_ROOT / "eval" / "corpus" / "cache"


def _quote_key(text: str) -> str:
    """Letters and digits only, after NFKC: PDF text breaks words across lines
    ("mem- ory") and uses ligatures, and a verbatim copy of it must still match.
    A paraphrase fails, because it changes the letters. Same normalisation as
    scripts/eval/pre_extractor_test.py's quote audit."""
    import unicodedata
    return re.sub(r"[^0-9a-z]+", "", unicodedata.normalize("NFKC", text or "").lower())


def drop_unfound_quotes(parsed: dict, article_id: str) -> list:
    """Remove every evidence entry whose source_quote is not in the article.

    The extraction prompt requires each quote to be copied verbatim, and the
    validator cannot check that without the article. In the pre-extractor test
    2% of GLM's quotes and 1% of headless Opus's were not in the article, so
    this gate is what keeps a fabricated quote off a page. A subclaim pointing
    at a removed entry goes with it; a claim left with no evidence is dropped
    whole. Returns one note per removal. With no cached text the gate cannot
    run, and it says so rather than passing everything silently."""
    path = CACHE_DIR / f"{article_id}.txt"
    if not path.exists():
        return [f"quote check skipped: no cached text at {path.relative_to(WIKI_ROOT)}"]
    article = _quote_key(path.read_text(encoding="utf-8"))
    notes = []
    kept = []
    for c in parsed.get("contributions") or []:
        if not isinstance(c, dict) or c.get("type") != "claim":
            kept.append(c)
            continue
        good, gone = [], set()
        for e in c.get("evidence") or []:
            q = e.get("source_quote") if isinstance(e, dict) else None
            if q and _quote_key(q) not in article:
                gone.add(e.get("anchor"))
                notes.append(f"{c.get('slug')}: dropped evidence {e.get('anchor')!r}, quote not in article: {q[:80]!r}")
            else:
                good.append(e)
        c["evidence"] = good
        c["subclaims"] = [sc for sc in c.get("subclaims") or []
                          if not (isinstance(sc, dict) and sc.get("evidence_ref") in gone)]
        if good and c["subclaims"]:
            kept.append(c)
        else:
            notes.append(f"{c.get('slug')}: claim dropped, no evidence with a verifiable quote left")
    parsed["contributions"] = kept
    return notes


def ingest_record(record: dict, actor: str, dry_run: bool) -> list:
    """Returns a list of (folder, slug) pages actually written (or that
    WOULD be written, in dry-run mode)."""
    written = []
    validation = record.get("validation") or {}
    if not validation.get("passed"):
        return written
    parsed = record.get("parsed") or {}
    for note in drop_unfound_quotes(parsed, record["article_id"]):
        print(f"  [QUOTE] {record['article_id']}: {note}", file=sys.stderr)
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


def build_study_record(record: dict, written: list, actor: str,
                       removed_dois: list | None = None) -> tuple[str | None, dict | None, list]:
    """(key, observation record, problems) from an extraction's `study_record`.

    The record is built from the extraction and then held to exactly the same
    validator as a hand-written one (observation_lib.validate_record, with the
    live claim/anchor index), so the pipeline cannot write a record the store
    would refuse. Nothing here fills a field the extraction left empty:
    `study.doi` is never set (absent = not established), provenance says an
    unverified pipeline wrote it, and an observation's claim edge is kept only
    when it names a `bearing` — never defaulted, because a record read as
    `supports` because nobody said otherwise is a fabrication.

    The anchor is set only when the claim page was written by THIS run, so it
    points at the evidence entry this same extraction produced. For a claim
    page that already existed, the edge is kept without an anchor: the record
    names the proposition, and writing it into that page's argument stays an
    editorial act (CLAUDE.md: do not automate epistemic promotion)."""
    import observation_lib as ol

    parsed = record.get("parsed") or {}
    sr = parsed.get("study_record")
    if not isinstance(sr, dict):
        return None, None, []
    problems = []
    contributions = [c for c in (parsed.get("contributions") or []) if isinstance(c, dict)]
    claims = {c.get("slug"): c for c in contributions if c.get("type") == "claim" and c.get("slug")}
    written_claims = {slug for folder, slug, *_ in written if folder == "claims"}

    # The source: the one L0b citation string every evidence entry carries.
    citation = next((ev.get("citation") for c in claims.values()
                     for ev in (c.get("evidence") or []) if isinstance(ev, dict) and ev.get("citation")),
                    None)
    if not citation:
        return None, None, ["no evidence citation to name the source by"]
    # gate_citations reports each removal as "<page>: <doi> (<status>)".
    dois = {m.group(1) for r in (removed_dois or [])
            for m in [re.search(r"(10\.\d{4,9}/[^\s()]+)", str(r))] if m}
    for doi in dois:
        # The citation gate stripped this DOI from the pages because it
        # resolved to the wrong paper; the record must not carry it back in.
        citation = re.sub(rf"\s*\[?(?:doi:)?\s*(?:https?://(?:dx\.)?doi\.org/)?{re.escape(doi)}\]?(?:\([^)]*\))?",
                          "", citation, flags=re.I).strip()
    sid, _, _ = _citation_id_author_year(citation)
    key = ol.ascii_key(sid)

    appears, observations = [], []
    for o in sr.get("observations") or []:
        if not isinstance(o, dict):
            continue
        o = dict(o)
        claim, ref, bearing = o.pop("claim", None), o.pop("evidence_ref", None), o.pop("bearing", None)
        observations.append(o)
        if not claim:
            continue
        if bearing not in ol.BEARINGS:
            problems.append(f"observation {o.get('id')!r}: claim edge to {claim!r} dropped — "
                            f"bearing {bearing!r} is not one of {sorted(ol.BEARINGS)}")
            continue
        edge = {"claim": claim, "bearing": bearing}
        if claim in written_claims and claim in claims:
            heads = {h["raw_anchor"]: h["heading_slug"]
                     for h in _evidence_headings([e for e in (claims[claim].get("evidence") or [])
                                                  if isinstance(e, dict)])}
            if ref in heads:
                edge["anchor"] = heads[ref]
        elif not (WIKI_ROOT / "claims" / f"{claim}.md").exists():
            problems.append(f"observation {o.get('id')!r}: claim edge dropped — claims/{claim}.md "
                            f"was not written and does not exist")
            continue
        if edge not in appears:
            appears.append(edge)

    rec = {
        "schema_version": ol.SCHEMA_VERSION,
        "study": {"key": key, "citation": citation, "design": sr.get("design")},
        "provenance": {
            "source_type": "research",
            "extracted_by": actor,
            "extracted_at": date.today().isoformat(),
            "extraction_method": f"ingest-pipeline-{record.get('prompt_version') or 'unknown'}"
                                 f" ({record.get('model') or 'unknown model'})",
            "verification": "unverified",
        },
    }
    if sr.get("synthesis") is not None:
        rec["study"]["synthesis"] = sr["synthesis"]
    if appears:
        rec["appears_in"] = appears
    rec["evidence_base"] = sr.get("evidence_base")
    rec["comparisons"] = sr.get("comparisons") or []
    rec["observations"] = observations

    issues = ol.validate_record(rec, key, ol.claim_evidence_anchors())
    return key, rec, problems + list(issues)


def ingest_study_record(record: dict, written: list, actor: str, dry_run: bool,
                        removed_dois: list | None = None) -> str | None:
    """Write observations/<key>.yaml when the extraction's study_record is
    valid. Returns the bundle-relative path written (or that would be), else
    None. Never overwrites: a study key that already has a record is either the
    same study, recorded more carefully by hand, or a namesake — and a pipeline
    cannot tell which, so it reports and stops."""
    import yaml

    key, rec, problems = build_study_record(record, written, actor, removed_dois)
    aid = record.get("article_id")
    if rec is None:
        if problems:
            print(f"  [observations] {aid}: no record — {problems[0]}", file=sys.stderr)
        return None
    blocking = [p for p in problems if "claim edge" not in p]
    for p in problems:
        if p not in blocking:
            print(f"  [observations] {aid}: {p}", file=sys.stderr)
    if blocking:
        print(f"  [observations] {aid}: record for {key!r} NOT written, "
              f"{len(blocking)} validation issue(s):", file=sys.stderr)
        for p in blocking[:8]:
            print(f"      {p}", file=sys.stderr)
        return None
    rel = f"observations/{key}.yaml"
    path = WIKI_ROOT / rel
    if path.exists():
        print(f"  [observations] {aid}: {rel} already exists — not overwriting; "
              f"merge by hand if this is the same study", file=sys.stderr)
        return None
    header = (f"# {key} — written by the ingest pipeline from {aid}, and UNVERIFIED.\n"
              f"# Extraction method is in provenance. Every field was validated against\n"
              f"# observations/SCHEMA.md; none was checked against the article by a person.\n\n")
    text = header + yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
    if dry_run:
        print(f"  [DRY-RUN] would write {rel}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"  [OK] wrote {rel}")
    return rel


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


_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(((?:\.\./[\w-]+/)?[^)\s#/]+\.md)(#[^)]*)?\)")


def repair_cross_folder_links(paths: list) -> dict:
    """Re-point links whose target is not where the renderer assumed.

    A contribution's `related` list names sibling slugs without a type, and
    _render_other links each one into the linking page's own folder. A
    sibling of another type (a principle naming its theory) then lands as a
    broken link: 105 of them on the first in-session ingest (2026-09-24).
    The render step cannot resolve this, because a sibling may be written
    later in the same run, so this runs once every page exists.

    A slug found in exactly one content folder is re-pointed there. A slug
    in several is ambiguous, so the link is dropped and its text kept:
    picking one of several same-named pages is a guess."""
    where = {}
    for f in ok.CONTENT_FOLDERS:
        for q in (WIKI_ROOT / f).glob("*.md"):
            where.setdefault(q.stem, []).append(f)
    stats = {"repointed": 0, "unlinked": 0}
    for path in paths:
        path = WIKI_ROOT / path
        folder = path.parent.name
        text = path.read_text(encoding="utf-8")

        def fix(m):
            label, dest, frag = m.group(1), m.group(2), m.group(3) or ""
            if (path.parent / dest).resolve().exists():
                return m.group(0)
            slug = Path(dest).stem
            locs = where.get(slug, [])
            if len(locs) == 1:
                stats["repointed"] += 1
                prefix = "" if locs[0] == folder else f"../{locs[0]}/"
                return f"[{label}]({prefix}{slug}.md{frag})"
            stats["unlinked"] += 1
            return label

        out = _MD_LINK_RE.sub(fix, text)
        if out != text:
            path.write_text(out, encoding="utf-8")
    return stats


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
        gate = record.get("judge_gate") or {}
        if validation.get("passed") and gate.get("final_verdict") == "fail":
            # eval_harness --judge-gate: valid in form, misstated in substance, and one
            # revision did not fix it. Not ingested; the article stays eligible.
            n_skipped_validation += 1
            print(f"  [SKIP] {article_id}: the {gate.get('judge')} judge failed this extraction "
                  f"(score {gate.get('final_score')}) and one revision did not fix it", file=sys.stderr)
            if not args.dry_run:
                ok.append_manifest_entry(source_id=article_id, title=record.get("article_title", ""),
                                         status="rejected", reason_code="judge-failed",
                                         reason=f"{gate.get('judge')} judge verdict fail after one revision "
                                                f"(score {gate.get('final_score')})")
            article_registry_entries[article_id] = {
                "outcome": "validation_failed", "run_id": args.run_id, "model": args.model,
                "pages": [], "reason": "judge-failed",
            }
            continue
        if not validation.get("passed"):
            n_skipped_validation += 1
            print(f"  [SKIP] {article_id}: structural validation did not pass "
                  f"({validation.get('error_count', '?')} error(s)) — not ingesting any of "
                  f"this article's contributions", file=sys.stderr)
            reason = None
            # An extraction may carry the extractor's own inclusion verdict
            # (scripts/eval/agent_arm.py's contract). A reject with a verdict
            # code from INCLUSION.md (E1-E4) is a finding about the SOURCE,
            # so it is recorded as that code. Recording it as
            # no-contributions-extracted would mark a settled source as a
            # failed run, and discovery would keep re-surfacing it.
            inclusion = (record.get("parsed") or {}).get("inclusion") or {}
            verdict_code = inclusion.get("reason_code")
            is_verdict = (inclusion.get("verdict") == "reject" and verdict_code in ok.REJECTION_CODES
                          and not ok.REJECTION_CODES[verdict_code][0])
            if not args.dry_run:
                if is_verdict:
                    reason = inclusion.get("reason") or ok.REJECTION_CODES[verdict_code][1]
                    reason_code = verdict_code
                elif validation.get("parse_error"):
                    reason = f"parse error: {validation['parse_error']}"
                    reason_code = "parse-error"
                elif not validation.get("n_contributions"):
                    reason = "no extractable contributions (out of scope or no learning-design content found)"
                    reason_code = "no-contributions-extracted"
                else:
                    reason = f"{validation.get('error_count', '?')} structural validation error(s)"
                    reason_code = "validation-error"
                ok.append_manifest_entry(
                    source_id=article_id,
                    title=record.get("article_title", ""),
                    status="rejected",
                    reason=reason,
                    reason_code=reason_code,
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
            obs_rel = ingest_study_record(record, written, args.by, args.dry_run,
                                          removed_dois=citations.get("removed"))
            if obs_rel:
                page_paths.append(obs_rel)
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
        stats = repair_cross_folder_links([f"{f}/{s}.md" for f, s, _, _ in all_written])
        print(f"\nCross-folder links: {stats['repointed']} re-pointed, {stats['unlinked']} ambiguous "
              "and unlinked.")
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
