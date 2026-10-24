#!/usr/bin/env python3
"""
add_currency.py — say on each claim how current it is, and how far it has been checked.

Prompted by the wiki's first outside feedback (2026-10-24): an agent quoting a claim
cannot tell a finding resting on a 1921 study, last compared with its source never,
from one checked last week against a 2024 meta-analysis, so it quotes both as settled.
Research does not expire on a date, and nothing here gives a claim one. What an agent
needs is the claim's age and its checking history, stated where it reads.

Three frontmatter fields (flat scalars, so every frontmatter writer keeps them) and one
header line under the evidence line:

    newest_evidence: 2019        year of the newest study the claim's evidence cites
    source_checked: 2026-10-20   every evidence entry was compared with its source text
                                 by the load-bearing judge (check_load_bearing.py) and
                                 passed, or its failure was read and dismissed; the
                                 latest of those dates. Absent when any entry is unchecked.
    recheck_by: 2029             only for claims whose findings age quickly: the accuracy
                                 of a tool or model ("component"), and local or general
                                 context (baselines, enrolment, post-COVID data), from the
                                 claim sort (eval/claim-sort/sort.ndjson). It is the newest
                                 study's year plus RECHECK_YEARS for the kind. A design
                                 finding gets none: spacing research from 1885 still holds.

    > **Claim** · [All claims](index.md)
    > **Evidence** · 2 studies · ...
    > **Currency** · newest study 2019 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

Past recheck_by the line says "overdue for a recheck since 2029". It never hides the
claim: the agent still has the finding, with its age attached.

The judge's verdicts live in eval/runs/load-bearing/judged.ndjson, which is not
committed. So a missing verdict file changes nothing: the script only sets
source_checked from verdicts it can confirm still apply to the page as written, and
removes it only when a verdict it can read no longer matches the entry (the page
changed since it was checked). An entry whose source text is not cached here is left
as it was. The fields on the page are the durable record.

    python3 scripts/add_currency.py --check
    python3 scripts/add_currency.py --apply
    python3 scripts/add_currency.py --overdue      # claims past recheck_by, oldest first
"""
import argparse
import collections
import datetime
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402

JUDGED = WIKI_ROOT / "eval" / "runs" / "load-bearing" / "judged.ndjson"
SORT = WIKI_ROOT / "eval" / "claim-sort" / "sort.ndjson"
FIELDS = ("newest_evidence", "source_checked", "recheck_by")

# Years a finding of each kind stays current from its newest study. Only these
# kinds get a recheck date; a design finding is not dated by its age alone.
RECHECK_YEARS = {"component": 3, "context-local": 3, "context-general": 5}
WHY = {"component": "tool and model accuracy changes quickly",
       "context-local": "local conditions change quickly",
       "context-general": "baselines and conditions change"}

BANNER_RE = re.compile(r"^>\s*\*\*[^*]+\*\*\s*·\s*\[[^\]]*\]\(index\.md\)\s*$")
EVIDENCE_RE = re.compile(r"^>\s*\*\*Evidence\*\*\s*·")
CURRENCY_RE = re.compile(r"^>\s*\*\*Currency\*\*\s*·")
YEAR_RE = re.compile(r"\((1[89]\d\d|20\d\d)[a-z]?(?:[,)]|, )")


def newest_year(evidence: str):
    """The newest publication year among the entries' citation lines (the line after
    each ### heading), so a year mentioned in prose is never taken for one."""
    years = []
    for chunk in re.split(r"(?m)^### ", evidence or "")[1:]:
        lines = [l for l in chunk.split("\n")[1:] if l.strip()]
        if lines:
            years += [int(y) for y in YEAR_RE.findall(lines[0])]
    this_year = datetime.date.today().year
    years = [y for y in years if y <= this_year]
    return max(years) if years else None


def categories() -> dict:
    out = {}
    if SORT.exists():
        for line in SORT.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if r.get("claim"):
                out[r["claim"]] = r.get("category")
    return out


def source_checks(claims: dict) -> dict:
    """claim -> (entries, confirmed, latest date, unknown) from the judge's verdicts that
    still match the page. `unknown` counts entries whose current text could not be
    rebuilt here (source not cached), whose state is therefore left as it was."""
    if not JUDGED.exists():
        return {}
    import check_load_bearing as clb
    judged = clb.done_before(JUDGED)
    by_claim = collections.defaultdict(list)
    for r in judged.values():
        by_claim[r["claim"]].append(r)
    reviewed = clb.load_reviewed()
    # The ranking rows carry each claim's ingest articles, which the judge read as its
    # source text; rebuilding the jobs without them would change every digest.
    rows = [r for r in clb.ranking(claims) if r["claim"] in by_claim]
    out = {}
    jobs, _ = clb.entry_jobs(rows, claims, offline=True)
    current = collections.defaultdict(dict)
    for j in jobs:
        current[j[0]["claim"]][j[1]] = (j[-2], j[-1])
    for claim, recs in by_claim.items():
        if claim not in claims:
            continue
        _, entries = clb.units(claims[claim])
        anchors = [a for a, _, _ in entries]
        if not anchors:
            continue
        by_digest = {r["digest"]: r for r in recs}
        ok, dates, unknown = 0, [], 0
        for a in anchors:
            if a not in current[claim]:
                unknown += 1
                continue
            dg, pdg = current[claim][a]
            r = by_digest.get(dg)
            if not r:
                continue
            if r["verdict"] == "pass" or (r["verdict"] in ("fail", "not-this-study") and pdg in reviewed):
                ok += 1
                dates.append(r["judged_at"])
        out[claim] = (len(anchors), ok, max(dates) if dates else None, unknown)
    return out


def set_fields(fm_text: str, values: dict) -> str:
    """Write the three scalars into raw frontmatter text, together and in FIELDS order,
    after `evidence_strength:` (or before `sources:`); a None value is left out."""
    lines = [l for l in fm_text.split("\n") if not any(l.startswith(f"{k}:") for k in FIELDS)]
    anchor = next((i + 1 for i, l in enumerate(lines) if l.startswith("evidence_strength:")), None)
    if anchor is None:
        anchor = next((i for i, l in enumerate(lines) if l.startswith("sources:")), len(lines))
    lines[anchor:anchor] = [f"{k}: {values[k]}" for k in FIELDS if values.get(k) is not None]
    return "\n".join(lines)


def read_field(fm_text: str, key: str):
    m = re.search(rf"(?m)^{key}:\s*(\S+)\s*$", fm_text)
    return m.group(1) if m else None


def currency_line(newest, checked, n_entries, n_ok, recheck, kind, today) -> str:
    parts = [f"newest study {newest}" if newest else "no dated study recorded"]
    if checked and n_entries and n_ok == n_entries:
        parts.append(f"checked against its sources {checked} (automated, {n_ok} of {n_entries} "
                     f"{'entry' if n_entries == 1 else 'entries'})")
    elif n_ok:
        parts.append(f"{n_ok} of {n_entries} entries checked against their sources (automated)")
    else:
        parts.append("not yet checked against its sources")
    parts.append("not reviewed by a person")
    if recheck:
        if today.year > int(recheck):
            parts.append(f"**overdue for a recheck since {recheck}**: {WHY[kind]}")
        else:
            parts.append(f"recheck by {recheck}: {WHY[kind]}")
    return "> **Currency** · " + " · ".join(parts)


def process(path: Path, check: tuple, kind, apply: bool, today) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = okf_lib.FRONTMATTER_RE.match(text)
    if not m:
        return {"action": "skipped", "detail": "no frontmatter"}
    fm_text = m.group(1)
    body = text[m.end():]

    evidence = okf_lib.get_section(re.sub(r"<!--.*?-->", "", body, flags=re.S), "Evidence") or ""
    newest = newest_year(evidence)
    n_entries = len(re.findall(r"(?m)^### ", evidence))

    old_checked = read_field(fm_text, "source_checked")
    if check is None:
        checked, n_ok = old_checked, (n_entries if old_checked else 0)
    else:
        total, ok, latest, unknown = check
        if ok == total and latest:
            checked, n_ok = latest, ok
        elif unknown and old_checked:
            checked, n_ok = old_checked, n_entries   # cannot see every entry here: keep
        else:
            checked, n_ok = None, ok
    recheck = (newest + RECHECK_YEARS[kind]) if (newest and kind in RECHECK_YEARS) else None

    values = {"newest_evidence": newest, "source_checked": checked, "recheck_by": recheck}
    new_fm_text = set_fields(fm_text, values)
    want = currency_line(newest, checked, n_entries, n_ok, recheck, kind, today)

    lines = body.split("\n")
    h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1 is None:
        return {"action": "skipped", "detail": "no H1"}
    scan = h1 + 1
    while scan < len(lines) and not lines[scan].strip():
        scan += 1
    if scan >= len(lines) or not BANNER_RE.match(lines[scan].strip()):
        return {"action": "skipped", "detail": "no type banner"}
    at = scan + 1
    if at < len(lines) and EVIDENCE_RE.match(lines[at].strip()):
        at += 1
    if at < len(lines) and CURRENCY_RE.match(lines[at].strip()):
        if lines[at].strip() == want and new_fm_text == fm_text:
            return None
        lines[at] = want
        action = "updated"
    else:
        lines[at:at] = [want]
        action = "inserted"
    if apply:
        head = text[:m.start(1)] + new_fm_text + text[m.end(1):m.end()]
        path.write_text(head + "\n".join(lines), encoding="utf-8")
    return {"action": action, "detail": want, "recheck": recheck}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    g.add_argument("--overdue", action="store_true")
    a = ap.parse_args()
    today = datetime.date.today()
    claims = {p.stem: p for p in (WIKI_ROOT / "claims").glob("*.md") if p.stem != "index"}

    if a.overdue:
        rows = []
        for slug, p in claims.items():
            fm = p.read_text(encoding="utf-8").split("\n---", 1)[0]
            r = read_field(fm, "recheck_by")
            if r and int(r) < today.year:
                rows.append((int(r), slug))
        for r, slug in sorted(rows):
            print(f"{r}\t{slug}")
        print(f"{len(rows)} claim(s) overdue for a recheck", file=sys.stderr)
        return

    kinds = categories()
    checks = source_checks(claims)
    if not JUDGED.exists():
        print(f"no {JUDGED.relative_to(WIKI_ROOT)} here: source_checked left as the pages have it")
    counts = collections.Counter()
    for slug, p in sorted(claims.items()):
        rec = process(p, checks.get(slug), kinds.get(slug), a.apply, today)
        counts["unchanged" if rec is None else rec["action"]] += 1
    verb = "" if a.apply else " (dry run)"
    print(f"claims/{verb}: " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))


if __name__ == "__main__":
    main()
