#!/usr/bin/env python3
"""
evidence_rollup.py — what the wiki's evidence adds up to, computed, never judged.

Every claim page carries per-study codes in its frontmatter `sources[]` (q, i,
n, mirrored out of `## Evidence` by sync_evidence_codes.py), and every other
page cites claims with a `[±~][SMW]` marker. Put together, those answer
questions no single page can: how many distinct studies stand behind a
strategy, which studies the wiki leans on hardest, which claims are cited
hundreds of times on the strength of two papers. This module computes them;
add_evidence_profile.py writes the per-page header, build_evidence_report.py
writes `evidence.md`.

Four rules, each the lesson of an earlier mistake here:

- **Count studies, not claims.** One source often yields many claims:
  Karpicke (2017), a review chapter, stands behind 34. Counting claims would
  let one prolific source look like a literature. Two entries are one study
  when they share a DOI or a year and title (StudyIndex).
- **Never collapse to a verdict.** Ranges and counts only: `q2`–`q4`, "9 of
  19 report an effect size". `evidence_strength:` tried a verdict and produced
  nineteen spellings; add_evidence_summary.py already refuses one per claim.
- **Never average the impact bins.** `i` is an ordinal bin (d < .2, .2–.4,
  .4–.8, ≥ .8), and `i?` means no effect size was reported, which is not 0.
  Pooling belongs to observations/, where effect sizes and their uncertainty
  are recorded, and only across comparable measures.
- **Where one study is coded differently on two claims, the tier most of its
  entries give is used, and a tie goes to the lower.** Taking the minimum let
  one stray code outvote the rest: Karpicke (2017) is coded q2 on 78 entries
  and q1 on one.

    python3 scripts/evidence_rollup.py principles/example-slug   # one page's profile
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import build_reverse_index  # noqa: E402
import okf_lib  # noqa: E402

# Kinds whose pages cite claims and get a profile. Claims have their own header
# (add_evidence_summary.py): a claim linking a claim is a relation, not a citation.
PROFILE_KINDS = ["principles", "elements", "patterns", "strategies", "processes", "methods",
                 "theories", "learner-variables"]

_DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)
_YEAR_TITLE = re.compile(r"\((\d{4})[a-z]?\)\.?\s*(.+)")
_WORD = re.compile(r"[a-z0-9]+")


def _doi(src: dict):
    m = _DOI.search(str(src.get("resource") or "")) or _DOI.search(str(src.get("title") or ""))
    return m.group(0).rstrip(".,;)").lower() if m else None


def _fingerprint(src: dict):
    """Year plus the first six title words, from the citation line: the part of a
    citation that survives the author list being written three ways ("Shen, S."
    and "Shuanghong Shen, Qi Liu, …" are one study)."""
    m = _YEAR_TITLE.search(" ".join(str(src.get("title") or "").split()))
    if not m:
        return None
    words = _WORD.findall(m.group(2).lower())[:6]
    return f"{m.group(1)}:{' '.join(words)}" if len(words) >= 3 else None


class StudyIndex:
    """One key per distinct study across the whole corpus. Entries sharing a DOI
    or a year-and-title fingerprint are the same study (union-find), so a study
    cited with its DOI on one claim and without it on another is still one study."""

    def __init__(self, claims: dict):
        self.parent = {}
        for c in claims.values():
            for s in c["sources"]:
                keys = [k for k in (("doi:" + _doi(s)) if _doi(s) else None, _fingerprint(s)) if k]
                keys = keys or ["id:" + str(s.get("id") or s.get("title") or "?")]
                s["_keys"] = keys
                for k in keys:
                    self.parent.setdefault(k, k)
                for k in keys[1:]:
                    self._union(keys[0], k)

    def _find(self, k):
        while self.parent[k] != k:
            self.parent[k] = self.parent[self.parent[k]]
            k = self.parent[k]
        return k

    def _union(self, a, b):
        ra, rb = self._find(a), self._find(b)
        if ra != rb:
            self.parent[max(ra, rb)] = min(ra, rb)

    def key(self, src: dict) -> str:
        return self._find(src["_keys"][0])


_INDEX = None


def study_key(src: dict) -> str:
    return _INDEX.key(src)


def _coded(src: dict) -> bool:
    return isinstance(src, dict) and ("q" in src or "i" in src)


def load_claims() -> dict:
    """{claim slug: {"title", "sources": [coded source dicts]}} from frontmatter."""
    out = {}
    for path in sorted((WIKI_ROOT / "claims").glob("*.md")):
        if path.stem == "index":
            continue
        m = okf_lib.FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
        try:
            fm = yaml.safe_load(m.group(1)) if m else {}
        except yaml.YAMLError:
            fm = {}
        fm = fm if isinstance(fm, dict) else {}
        out[path.stem] = {"title": fm.get("title") or path.stem,
                          "sources": [s for s in fm.get("sources") or [] if _coded(s)]}
    global _INDEX
    _INDEX = StudyIndex(out)
    return out


def citations_by_page(reverse: dict = None) -> dict:
    """{(kind, slug): [(claim slug, polarity or None, strength or None)]}, from the
    same link parse the reverse index uses, so the two cannot disagree."""
    reverse = reverse or build_reverse_index.build()
    out = defaultdict(list)
    for claim, by_kind in reverse["edges"].get("claims", {}).items():
        for kind, entries in by_kind.items():
            for e in entries:
                out[(kind, e["slug"])].append((claim, e.get("polarity"), e.get("strength")))
    return out


class Studies:
    """Distinct studies over a set of claims, with the conservative per-study codes."""

    def __init__(self, claims: dict, slugs):
        self.entries = defaultdict(list)
        for c in slugs:
            for s in claims.get(c, {}).get("sources", []):
                self.entries[study_key(s)].append(s)

    def __len__(self):
        return len(self.entries)

    def q(self, key):
        """The tier most entries give this study; a tie goes to the lower tier."""
        vals = Counter(s["q"] for s in self.entries[key] if isinstance(s.get("q"), int))
        return min(vals, key=lambda q: (-vals[q], q)) if vals else None

    def reports_effect(self, key) -> bool:
        return any(isinstance(s.get("i"), int) for s in self.entries[key])

    def q_values(self):
        return [q for q in (self.q(k) for k in self.entries) if q is not None]


def page_profile(cites: list, claims: dict) -> dict:
    slugs = [c for c, _, _ in cites]
    studies = Studies(claims, slugs)
    qs = studies.q_values()
    n_by_claim = {c: len({study_key(s) for s in claims.get(c, {}).get("sources", [])}) for c in slugs}
    return {
        "claims": len(slugs),
        "polarity": Counter(p or "unmarked" for _, p, _ in cites),
        "studies": len(studies),
        "q_min": min(qs) if qs else None,
        "q_max": max(qs) if qs else None,
        "q3_plus": sum(1 for q in qs if q >= 3),
        "with_effect": sum(1 for k in studies.entries if studies.reports_effect(k)),
        "one_study": sum(1 for n in n_by_claim.values() if n == 1),
        "no_study": sum(1 for n in n_by_claim.values() if n == 0),
    }


def profile_line(p: dict) -> str:
    """The `> **Evidence** ·` header for a page that cites claims. Closed grammar:
    add_evidence_profile.GENERATED_RE must match every line this can return."""
    if not p["claims"]:
        return "> **Evidence** · no claims cited"
    pol = p["polarity"]
    parts_pol = [f"{pol[k]} {label}" for k, label in (("+", "for"), ("~", "mixed"), ("-", "against"),
                                                     ("unmarked", "unmarked")) if pol.get(k)]
    head = f"{p['claims']} claim{'s' if p['claims'] != 1 else ''} ({', '.join(parts_pol)})"
    if not p["studies"]:
        return f"> **Evidence** · {head} · no studies recorded yet"
    st = f"{p['studies']} stud{'y' if p['studies'] == 1 else 'ies'}"
    if p["q_min"] is not None:
        st += (f", `q{p['q_min']}`" if p["q_min"] == p["q_max"] else f", `q{p['q_min']}`–`q{p['q_max']}`")
    parts = [head, st, f"{p['with_effect']} of {p['studies']} report an effect size"]
    if p["one_study"]:
        parts.append(f"{p['one_study']} claim{'s' if p['one_study'] != 1 else ''} rest on one study"
                     if p["one_study"] != 1 else "1 claim rests on one study")
    return "> **Evidence** · " + " · ".join(parts)


if __name__ == "__main__":
    claims = load_claims()
    cites = citations_by_page()
    for arg in sys.argv[1:]:
        kind, slug = arg.split("/", 1)
        print(profile_line(page_profile(cites.get((kind, slug.removesuffix(".md")), []), claims)))
