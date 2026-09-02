#!/usr/bin/env python3
"""
check_citations.py — Cross-page citation consistency checker.

Finds the same citation (same first author + year) appearing in ## Key
Sources / ## Evidence sections across multiple wiki pages, and flags any
case where they disagree — most importantly, two different DOIs given for
what should be the identical source. Built after an enrich.py batch (GLM-5.3
via --provider openrouter) cited Sailer & Homner (2020) with two different
DOIs across gamification.md and leaderboards.md, and cited Hamari, Koivisto
& Sarsa (2014) with a DOI on one page but not the other — a real,
citable-looking fabrication risk that a per-page read can't catch, since
no single page looks wrong in isolation.

This is a self-consistency check only — it does not verify a DOI against a
real registry (e.g. Crossref); it just catches disagreement across the
wiki's own pages, which is a strong signal that at least one instance was
invented or misremembered.

Usage:
    python3 scripts/check_citations.py                       # whole wiki
    python3 scripts/check_citations.py --type strategies      # one folder
    python3 scripts/check_citations.py --files strategies/games.md strategies/simulations.md
                                                                # only report conflicts touching these
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok

# Every content folder. Derived rather than repeated: thirteen scripts each
# kept their own copy of this list, which is how learner-variables ended up
# missing from one of them for weeks. See okf_lib.CONTENT_FOLDERS.
PAGE_TYPES = tuple(ok.CONTENT_FOLDERS)

# Matches a citation line's leading "Author, A. ... (Year)." — single author
# ("Smith, J. (2020)") or first-of-several ("Smith, J., & Jones, K. (2020)").
CITATION_KEY_RE = re.compile(r"^[-*]?\s*([A-Z][A-Za-z'’-]+),.*?\((\d{4}[a-z]?)\)")
# Excludes bare ')'/']' so a DOI embedded in a markdown link — [doi:X](url) —
# doesn't swallow the link's own closing punctuation, but still allows a
# BALANCED (...) pair as part of the DOI itself: several publishers'
# DOIs legitimately contain parens (Wiley SICI-style, ASCE, ASHA, and
# Academic Press's older series all do — e.g. 10.1061/(ASCE)0733-9445
# (2002)128:9(1119), 10.1044/0161-1461(2004/018)). The plain-exclusion
# version truncated these mid-DOI at the first paren (confirmed against
# real citations via resolve_doi_conflicts.py: chi-1996, nelson-1990, and
# several others all had a real, resolvable DOI reported as "not_found"
# only because the truncated fragment sent to Crossref wasn't a real DOI
# at all — the wiki content was fine, this regex was the actual bug).
DOI_RE = re.compile(r"10\.\d{4,9}/(?:\([^\s()]*\)|[^\s()\]])+")

# Same first-author-surname + year is not enough to call two citations "the
# same paper" — e.g. Ericsson, Krampe & Tesch-Romer (1993) vs. Ericsson &
# Simon (1993) are different works by an overlapping author list in the same
# year. Require the title text (the part of the line after the year) to
# actually overlap before treating two same-key entries as one citation.
#
# Deliberately grammatical function words ONLY — no domain topic words (no
# "learning", "research", "science", "instruction", "practice", ...). An
# earlier version included those, tuned only against the two same-author-
# year false positives this file was built to fix (Ericsson 1993 x2, Clark
# 2016 x2) — those still separate fine on their other, more distinctive
# words either way. But doi_resolver.py reuses this same word-set logic to
# compare a citation's title against Crossref's title directly, with no
# author-year prefilter, and education-research titles routinely consist
# ALMOST ENTIRELY of exactly those "topic" words (e.g. "E-Learning and the
# Science of Instruction") — stripping them collapsed both sides to an
# empty set and reported an automatic false "different paper" on a title
# that was actually identical. Confirmed by hand against two real
# doi_resolver.py false positives before narrowing this list.
_TITLE_STOPWORDS = {
    "the", "and", "of", "in", "a", "an", "for", "on", "to", "with", "from",
    "how", "what", "when", "does",
}


def _words_from_text(text: str) -> set:
    """Significant (lowercase, len>=4, stopword-filtered) words from any text
    — shared by _title_words below and doi_resolver.py's title-match check,
    so both use the exact same notion of "same paper"."""
    return {w for w in re.findall(r"[a-zA-Z]{4,}", text.lower()) if w not in _TITLE_STOPWORDS}


def _extract_title_text(line: str, year: str) -> str:
    """The raw title substring of a citation line (everything between the
    "(Year)." clause and the venue/DOI that follows) — used both to build
    the word-set _title_words compares with, and, as actual text (word
    order preserved), as a Crossref bibliographic search query when no
    already-cited DOI verifies (see resolve_doi_conflicts.py)."""
    idx = line.find(f"({year})")
    tail = line[idx + len(year) + 2:] if idx != -1 else line
    # The slice above still starts with the ". " ending the "(Year)."
    # clause, immediately before the title itself — strip that first, or
    # the title-end search below matches THAT period (since it's often
    # also immediately followed by an italic "*", when the title itself is
    # italicized) and cuts the tail down to nothing before the title text
    # is ever reached.
    tail = tail.lstrip(". ")
    # A BOOK in APA form italicises the TITLE and puts the publisher after
    # it in plain text — "*How learning works*. Jossey-Bass." — the exact
    # mirror image of the journal-article form the end-marker search below
    # handles ("Title. *Journal, vol*(issue)"). Nothing in a book citation
    # matches "[.?!] followed by * or 'In '", so that search found no
    # boundary at all and kept the WHOLE tail as the title, folding the
    # publisher into both the title-word set used to verify a DOI and the
    # Crossref search query ("jossey", "bass", "cambridge", "university",
    # "press", "routledge", ... as if they were title words). Books are the
    # overwhelming majority of this wiki's stuck citation conflicts —
    # Ambrose 2010, Mayer 2009/2021, Paivio 1986, Bandura 1977, Hattie 2009,
    # Sweller 2011, Boud 1985, Mercer 2000, Archer 2011, Brookhart 2013 and
    # more all failed here — so when the tail opens with an italic span,
    # that span IS the title.
    if tail.startswith("*"):
        close = tail.find("*", 1)
        if close != -1:
            return tail[1:close].strip()
    # Cut at the title's actual end, not just before the DOI/URL — otherwise
    # venue text (an italicized journal/book name, "In *Conference
    # Proceedings*", a publisher name after ". ") gets pulled in as if it
    # were part of the title, diluting a genuine match below threshold (a
    # second confirmed doi_resolver.py false positive: matching venue noise
    # like "ASEE Annual Conference & Exposition Proceedings" swamped the two
    # words that actually matched). A title phrased as a question or
    # exclamation ends in "?"/"!", not ".", so the period-only version of
    # this regex missed that boundary entirely and let the ENTIRE venue,
    # volume, and page range through as if it were part of the title —
    # confirmed against real wiki content: Andre (1979), "Does answering
    # questions really promote reading comprehension? *Review of
    # Educational Research, 49*(2), 323-369.", produced a resolve_doi_
    # conflicts.py search query and title-word set both polluted with
    # "review", "educational", "research" from the journal name.
    end_marker = re.search(r"[.?!]\s+(?=\*|In\s)", tail)
    if end_marker:
        tail = tail[:end_marker.start() + 1]
    else:
        tail = re.split(r"doi:|https?://", tail, maxsplit=1)[0]
    return tail.strip()


def _title_words(line: str, year: str) -> set:
    return _words_from_text(_extract_title_text(line, year))


def _norm_title(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace — for comparing two
    title strings positionally rather than as bags of words."""
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", text.lower()).split())


def titles_align(cited_text: str, resolved_title: str) -> bool:
    """Guard against a short, generic cited title "matching" a longer, different
    work that merely CONTAINS it.

    Word-overlap alone cannot tell these two apart:

      Bandura (1977), *Social learning theory*  ->  Crossref: "Model of
      Causality in Social Learning Theory"   overlap 3/5 = 0.60, but this is a
      Springer chapter ABOUT the theory, not Bandura's Prentice-Hall book.
      Confirmed in production: this DOI was auto-applied to 69 pages.

      Ambrose (2010), *How learning works*  ->  Crossref: "How Learning Works:
      Seven Research-Based Principles for Smart Teaching"   overlap is lower
      still, and this one IS the same book.

    What separates them is position, not proportion. A genuine subtitle
    expansion is a PREFIX; a work about the cited topic carries the cited words
    somewhere after its own leading words. So when the resolved title adds
    anything on top of everything the citation named, require one title to
    actually begin with the other. One extra word is enough to matter —
    "Advances in Cognitive Load Theory" is not Sweller's "Cognitive Load
    Theory" — and since this guard only rejects NON-prefix containment, a
    genuine subtitle expansion is unaffected at any size. Titles that merely
    differ in wording, rather than one containing the other, never reach this
    and are left to the word-overlap check, which handles article and
    word-order differences ("The uses of argument" vs "Uses of Argument")."""
    cited_words, resolved_words = _words_from_text(cited_text), _words_from_text(resolved_title)
    if not cited_words or not resolved_words:
        return True   # nothing to judge on; defer to the overlap check
    contained = cited_words <= resolved_words
    if not (contained and len(resolved_words) > len(cited_words)):
        return True   # not the risky containment shape
    c, r = _norm_title(cited_text), _norm_title(resolved_title)
    return bool(c and r and (r.startswith(c) or c.startswith(r)))


def _same_paper(a: set, b: set) -> bool:
    if not a or not b:
        return False
    union = len(a | b)
    return union > 0 and len(a & b) / union >= 0.35


def _normalize_doi(doi: str) -> str:
    doi = doi.strip().rstrip(".,;")
    # Only strip a trailing ')' if it's unbalanced (more ')' than '(' seen
    # so far) — several publishers' DOIs legitimately end in a closing
    # paren (e.g. 10.1061/(ASCE)0733-9445(2002)128:9(1119)), so an
    # unconditional rstrip(")") would corrupt those right back to the
    # truncated form DOI_RE was just fixed to stop producing. In the
    # normal case (DOI_RE's match is already balanced) this loop never
    # runs at all.
    while doi.endswith(")") and doi.count("(") < doi.count(")"):
        doi = doi[:-1]
    return doi.lower()


def extract_citations(text: str, source_label: str) -> list[dict]:
    """Return one entry per citation-looking line found in this page's
    Key Sources or Evidence section(s): {"key", "doi" (or None), "line",
    "source", "title_words"}."""
    results = []
    for section_name in ("Key Sources", "Evidence"):
        m = re.search(rf"##\s*{re.escape(section_name)}\s*\n(.+?)(?=\n##\s|\Z)", text, re.DOTALL)
        if not m:
            continue
        for line in m.group(1).splitlines():
            line = line.strip()
            if not line or line.startswith("<!--"):
                continue
            key_m = CITATION_KEY_RE.search(line)
            if not key_m:
                continue
            year = key_m.group(2)
            key = f"{key_m.group(1).lower()}-{year}"
            doi_m = DOI_RE.search(line)
            results.append({
                "key": key,
                "doi": _normalize_doi(doi_m.group(0)) if doi_m else None,
                "line": line[:160],
                # Parsed from the FULL line, not from the truncated "line"
                # above: the journal/volume/page string sits at roughly
                # characters 100-180 of a typical APA citation, so reading it
                # back off the 160-char excerpt silently drops it for the
                # longer half of the corpus.
                "meta": parse_source_meta(line),
                "source": source_label,
                "title_words": _title_words(line, year),
            })
    return results


def _cluster_by_title(entries: list) -> list:
    """Split same author-year entries into groups that are actually the same
    paper by title-word overlap (see _same_paper)."""
    clusters: list[list[dict]] = []
    for e in entries:
        for cluster in clusters:
            if any(_same_paper(e["title_words"], m["title_words"]) for m in cluster):
                cluster.append(e)
                break
        else:
            clusters.append([e])
    return clusters


def load_all_citations(page_types=PAGE_TYPES) -> dict:
    """Return {key: [citation, ...]} across every page of the given types."""
    by_key = defaultdict(list)
    for page_type in page_types:
        folder = WIKI_ROOT / page_type
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            rel = str(path.relative_to(WIKI_ROOT))
            for c in extract_citations(text, rel):
                by_key[c["key"]].append(c)
    return by_key


def find_conflicts(by_key: dict, touched_files: set = None) -> list[dict]:
    """Return (author-year, title-cluster) groups where >1 distinct non-null
    DOI is cited, or where some entries carry a DOI and others (for what
    title-clustering judged the same paper) don't. If touched_files is
    given, only report conflicts involving at least one of those files —
    used for a targeted post-enrichment-batch check."""
    conflicts = []
    for key, entries in by_key.items():
        if len(entries) < 2:
            continue
        for cluster in _cluster_by_title(entries):
            if len(cluster) < 2:
                continue
            if touched_files and not any(e["source"] in touched_files for e in cluster):
                continue
            dois = {e["doi"] for e in cluster if e["doi"]}
            has_missing = any(e["doi"] is None for e in cluster)
            if len(dois) > 1 or (dois and has_missing):
                conflicts.append({"key": key, "entries": cluster, "dois": dois})
    return conflicts


def load_by_doi(by_key: dict) -> dict:
    """Invert the corpus: {normalised DOI -> [citation, ...]}."""
    by_doi = defaultdict(list)
    for entries in by_key.values():
        for e in entries:
            if e["doi"]:
                by_doi[e["doi"]].append(e)
    return by_doi


def find_doi_collisions(by_doi: dict, touched_files: set = None) -> list[dict]:
    """Return DOIs that are attached to what look like *different papers*.

    This is the opposite direction from find_conflicts, and the more dangerous
    one. find_conflicts groups by author+year and asks "does this one paper
    carry two DOIs?" — it can only ever compare citations that already agree on
    author and year, so a DOI copied onto an unrelated work is invisible to it.
    That is exactly how 10.1007/978-1-4684-7562-3_3 ("Model of Causality in
    Social Learning Theory") ended up asserted as Bandura (1977) on 69 pages:
    every page agreed with every other, because they had all copied the same
    wrong DOI. Only a manual audit caught it.

    Two signals, either of which is enough:

      * the entries split into more than one title cluster (_same_paper), or
      * they disagree on first author or year *and* their titles are not
        word-for-word the same.

    The second exists because title clustering is a similarity judgment and
    0.35 Jaccard is loose: Zoogman et al. (2015) "Mindfulness interventions
    with youth" and Zoogman et al. (2019) "Mindfulness-based interventions for
    youth" — different author lists, different papers — overlap far too much to
    separate on title alone, so clustering alone would miss them.

    The identical-title escape clause is what keeps that signal usable.
    CITATION_KEY_RE reads the first "Surname, ... (year)" in the line, which on
    a book chapter is often the *editor* rather than the author, and on a line
    carrying two years picks the wrong one — so the same citation, copied
    verbatim onto two pages, can yield sugai-2009 on one and horner-2005 on the
    other. Those are artifacts of key extraction, not disagreements about the
    work: if the two lines state the same title, they are the same paper
    whatever the key says. Without this clause the check reports 44 collisions,
    most of them that artifact, and a check that mostly cries wolf gets ignored.

    A DOI cited for one paper across many pages — the normal case — is silent."""
    collisions = []
    for doi, entries in sorted(by_doi.items()):
        if len(entries) < 2:
            continue
        if touched_files and not any(e["source"] in touched_files for e in entries):
            continue
        clusters = _cluster_by_title(entries)
        keys = {e["key"] for e in entries}
        titles = {frozenset(e["title_words"]) for e in entries}
        if len(clusters) > 1 or (len(keys) > 1 and len(titles) > 1):
            collisions.append({"doi": doi, "clusters": clusters, "keys": keys,
                               # Which test fired. The report has to know:
                               # when it was the key test, title clustering
                               # merged the papers into one group, so printing
                               # the clusters shows the reader one undivided
                               # blob under a heading that says there are two.
                               "signal": "cluster" if len(clusters) > 1 else "key",
                               "groups": collision_groups(clusters)})
    return collisions


def collision_groups(clusters: list) -> list[tuple]:
    """[(label, [citation, ...])] — the papers, actually separated.

    A title cluster can still hold two works: the key test flags a collision
    precisely when clustering failed to split them (Zoogman 2015 vs Zoogman
    2019 overlap far too much on title alone). Sub-grouping each cluster by
    author-year key recovers the division, so the reader is shown the two
    papers rather than left to spot the seam. That is not cosmetic — the whole
    job on a collision is deciding which side keeps the DOI, and a report that
    hides the sides makes the reader redo the detection by eye."""
    groups = []
    for i, cluster in enumerate(clusters, 1):
        by_key = {}
        for e in cluster:
            by_key.setdefault(e["key"], []).append(e)
        for j, (key, es) in enumerate(sorted(by_key.items())):
            label = f"paper {i}" if len(clusters) > 1 else "paper"
            if len(by_key) > 1:
                label = f"{label}{'abcdefgh'[j] if len(clusters) > 1 else f' {j + 1}'}"
            groups.append((f"{label}  [{key}]", es))
    return groups


def format_collision_report(collisions: list[dict]) -> str:
    if not collisions:
        return "No DOI collisions found — every DOI is cited for one paper."
    lines = [f"{len(collisions)} DOI(s) attached to more than one paper:\n"]
    for c in collisions:
        lines.append(f"## {c['doi']}")
        if c["signal"] == "key":
            lines.append("   (caught by author/year, not by title — the titles are close "
                         "enough that clustering merged them)")
        for label, es in c["groups"]:
            lines.append(f"  {label}: {len(es)} citation(s)")
            for e in es:
                lines.append(f"    - {e['source']}: {e['line']}")
        lines.append("")
    return "\n".join(lines)


# "*Journal Name, 99*(3), 445-476" — the APA source string as this wiki writes
# it. Journal and volume sit inside the italics, issue and pages outside.
SOURCE_META_RE = re.compile(r"\*([^*]+?),\s*(\d+)\*\((\d+)\),\s*(\d+)([\u2013\u2014\-]\d+)?")


def parse_source_meta(line: str):
    """(journal, volume, issue, first_page) or None — the grouping key.

    First page only, not the full range: the same article is written both
    "445-476" and "445-76" in this corpus, and splitting those into two
    variants would manufacture conflicts out of a dash convention."""
    m = SOURCE_META_RE.search(line)
    if not m:
        return None
    return (" ".join(m.group(1).split()), m.group(2), m.group(3), m.group(4))


def source_meta_span(line: str):
    """(start, end, exact_text) of the journal/volume/page substring, for a
    repair that needs to rewrite it verbatim rather than re-render it."""
    m = SOURCE_META_RE.search(line)
    return (m.start(), m.end(), m.group(0)) if m else None


def doi_corroborates(doi: str, volume: str, issue: str, first_page: str) -> bool:
    """True when the DOI's own suffix spells out this volume/issue/page.

    Many APA and APA-adjacent DOIs are literally built from the citation:
    10.1037/0022-0663.99.3.445 is ISSN 0022-0663, volume 99, issue 3, page
    445. Where that holds, which of two disagreeing journal strings is right
    is arithmetic rather than a vote, and no Crossref call is needed.

    Deliberately narrow. Only the trailing dotted `.VOL.ISS.PAGE` form counts;
    publisher schemes that pack the volume into a longer opaque token
    (10.1207/s1532690xci0201_3) are NOT parsed, because a substring search for
    "02" in an arbitrary identifier matches by luck as often as by meaning.
    Those are reported for a Crossref pass instead."""
    m = re.search(r"\.(\d+)\.(\d+)\.(\d+)$", doi.strip())
    if not m:
        return False
    return (m.group(1), m.group(2), m.group(3)) == (volume, issue, first_page)


def _is_naming_variant(a: tuple, b: tuple) -> bool:
    """Two source strings that differ only in how the journal is named.

    "PNAS 111(23)" and "Proceedings of the National Academy of Sciences
    111(23)" are the same citation written two ways; "Cognition and
    Instruction 1(2)" and "Cognition and Instruction 2(2)" are not. Volume,
    issue and first page are the discriminator: when those agree the
    disagreement is style, and when they differ at least one side states a
    paper that does not exist at that DOI."""
    if a[1:] != b[1:]:
        return False
    ja, jb = a[0].lower(), b[0].lower()
    if ja.startswith(jb) or jb.startswith(ja):      # subtitle dropped
        return True
    short, long_ = sorted((ja, jb), key=len)
    initials = "".join(w[0] for w in re.findall(r"[a-z]+", long_)
                       if w not in {"of", "the", "and", "for", "in", "on"})
    return short.replace(".", "").replace(" ", "") in (initials, initials[:len(short)])


def find_metadata_divergence(by_doi: dict, touched_files: set = None) -> list[dict]:
    """DOIs whose citations disagree about the journal, volume, issue or pages.

    find_doi_collisions compares titles, so it cannot see this at all: the
    title is usually copied correctly while the journal around it is invented.
    Graham & Perin (2007) is cited 101 times under one DOI with seven
    different journal/volume/page strings, and every one of those pages passes
    every existing check — the DOI resolves, so nothing downstream questions
    the fabricated volume and page numbers wrapped around it.

    That is worse than a wrong DOI. A wrong DOI at least resolves to something
    a reader can check against; a correct DOI wearing an invented journal name
    validates cleanly and reads as precision.

    Each result carries `severity`: "conflict" when the variants disagree on
    volume/issue/page (at least one states a paper that does not exist at that
    DOI), or "naming" when they agree on all three and differ only in how the
    journal is written."""
    results = []
    for doi, entries in sorted(by_doi.items()):
        if touched_files and not any(e["source"] in touched_files for e in entries):
            continue
        variants = defaultdict(list)
        for e in entries:
            if e.get("meta"):
                variants[e["meta"]].append(e)
        if len(variants) < 2:
            continue
        ordered = sorted(variants.items(), key=lambda kv: -len(kv[1]))
        majority = ordered[0][0]
        severity = ("naming" if all(_is_naming_variant(majority, v) for v, _ in ordered[1:])
                    else "conflict")
        results.append({
            "doi": doi,
            "severity": severity,
            "majority": majority,
            "majority_corroborated": doi_corroborates(doi, *majority[1:]),
            "variants": ordered,
        })
    return results


def format_metadata_report(results: list[dict]) -> str:
    if not results:
        return "No citation metadata divergence found."
    conflicts = [r for r in results if r["severity"] == "conflict"]
    naming = [r for r in results if r["severity"] == "naming"]
    lines = [f"{len(conflicts)} DOI(s) with conflicting journal/volume/page metadata, "
             f"{len(naming)} with journal-name style variants only:\n"]
    for r in conflicts + naming:
        tag = "CONFLICT" if r["severity"] == "conflict" else "naming"
        seal = " [DOI self-describes the majority]" if r["majority_corroborated"] else ""
        lines.append(f"## {r['doi']}  ({tag}){seal}")
        for i, (meta, es) in enumerate(r["variants"]):
            j, v, iss, pg = meta
            mark = "  <- majority" if i == 0 else ""
            lines.append(f"  {len(es):4}x  {j} {v}({iss}), {pg}{mark}")
            if len(es) <= 3:
                for e in es:
                    lines.append(f"          {e['source']}")
        lines.append("")
    return "\n".join(lines)


def find_title_divergence(by_doi: dict, touched_files: set = None) -> list[dict]:
    """DOIs cited with more than one distinct title.

    The third and largest layer of the same defect. The model reproduces a
    paper's DOI and the *stem* of its title reliably, then invents whatever
    follows the colon. 10.37016/mr-2020-56 is cited 37 times as "Lateral
    reading and the nature of expertise: ..." with ten different subtitles —
    "reading less and learning more when evaluating digital information",
    "the studies of professional fact-checkers", "the ability of historians to
    evaluate digital sources is limited", and seven more.

    Neither existing check sees it. find_doi_collisions clusters by title-word
    overlap, and a shared stem carries these far past the 0.35 threshold, so
    all ten land in one cluster and report as one paper.
    find_metadata_divergence only ever looks at the journal string.

    `severity` is "truncation" when every variant is a prefix of the longest —
    someone dropped the subtitle, which loses detail but asserts nothing false
    — and "conflict" otherwise, where at least one subtitle was invented.

    Reported, never repaired. The majority spelling is *evidence* about the
    real title but not proof of it, and a subtitle is exactly the kind of
    plausible-sounding detail that is worth nothing unless it came from the
    registry. Resolve from a machine that can reach Crossref."""
    results = []
    for doi, entries in sorted(by_doi.items()):
        if touched_files and not any(e["source"] in touched_files for e in entries):
            continue
        variants = defaultdict(list)
        for e in entries:
            year = e["key"].rsplit("-", 1)[-1]
            norm = _norm_title(_extract_title_text(e["line"], year))
            if norm:
                variants[norm].append(e)
        if len(variants) < 2:
            continue
        ordered = sorted(variants.items(), key=lambda kv: -len(kv[1]))
        longest = max(variants, key=len)
        severity = ("truncation" if all(longest.startswith(v) for v in variants)
                    else "conflict")
        results.append({"doi": doi, "severity": severity, "variants": ordered})
    return results


def format_title_report(results: list[dict]) -> str:
    if not results:
        return "No title divergence found — every DOI is cited with one title."
    conflicts = [r for r in results if r["severity"] == "conflict"]
    trunc = [r for r in results if r["severity"] == "truncation"]
    lines = [f"{len(conflicts)} DOI(s) cited with conflicting titles, "
             f"{len(trunc)} with a truncated variant only:\n"]
    for r in sorted(conflicts, key=lambda r: -len(r["variants"])) + trunc:
        tag = "CONFLICT" if r["severity"] == "conflict" else "truncation"
        lines.append(f"## {r['doi']}  ({tag}, {len(r['variants'])} variants)")
        for v, es in r["variants"]:
            lines.append(f"  {len(es):4}x  {v[:100]}")
            if len(es) <= 2:
                for e in es:
                    lines.append(f"          {e['source']}")
        lines.append("")
    return "\n".join(lines)


# The journal-identifying part of a DOI suffix, read off the string itself:
#   10.1037/0022-0663.99.3.445  -> 0022-0663   (dotted ISSN)
#   10.1177/1754073917742706    -> 17540739    (SAGE: bare ISSN, then digits)
#   10.17763/haer.81.4....      -> haer        (publisher's journal code)
_JOURNAL_TOKEN = (
    re.compile(r"^(\d{4}-\d{3}[\dxX])\."),
    re.compile(r"^(\d{7}[\dxX])\d"),
    re.compile(r"^([a-z]{3,})[.\d]"),
)
def journal_token(doi: str):
    """(prefix, token) identifying the journal, or None."""
    prefix, _, suffix = doi.partition("/")
    for pat in _JOURNAL_TOKEN:
        m = pat.match(suffix)
        if m:
            return (prefix, m.group(1))
    return None


# Only these two shapes encode a volume and issue. Both are anchored at the
# start of the suffix on purpose: Elsevier writes 10.1016/j.learninstruc.
# 2011.11.001, where ".2011.11." is a year and month, and an unanchored search
# for ".N.N." reads that as "volume 2011, issue 11" and then reports every
# correctly-cited Elsevier article as contradicting its own DOI.
_CODE_VOL_ISS = re.compile(r"^[a-z]{3,}\.(\d+)\.(\d+)\.")               # haer.81.4....
_ISSN_VOL_ISS = re.compile(r"^\d{4}-\d{3}[\dxX]\.(\d+)\.(\d+)\.\d+$")  # 0022-0663.99.3.445


def encoded_volume_issue(doi: str):
    """(volume, issue) if the DOI spells them out, else None."""
    suffix = doi.partition("/")[2]
    for pat in (_CODE_VOL_ISS, _ISSN_VOL_ISS):
        m = pat.match(suffix)
        if m:
            # A four-digit "volume" in the recent past is a publication year,
            # not a volume — no journal has reached volume 2011.
            if len(m.group(1)) == 4 and m.group(1).startswith(("19", "20")):
                return None
            return (m.group(1), m.group(2))
    return None


def token_consensus(by_doi: dict, min_share: float = 0.75, min_cites: int = 3) -> dict:
    """{(prefix, token): journal name} where the wiki overwhelmingly agrees.

    Needs no journal database. DOIs sharing a journal token are, by
    construction, articles in the same journal, so the corpus can check itself:
    862 citations under 10.3102/00346543 say "Review of Educational Research"
    and three say something else. That is evidence about the journal, not about
    any one citation, which is what makes it usable to judge a citation."""
    tallies = defaultdict(lambda: defaultdict(int))
    for doi, entries in by_doi.items():
        key = journal_token(doi)
        if not key:
            continue
        for e in entries:
            if e.get("meta"):
                tallies[key][e["meta"][0]] += 1
    out = {}
    for key, names in tallies.items():
        total = sum(names.values())
        top, n = max(names.items(), key=lambda kv: kv[1])
        if total >= min_cites and n / total >= min_share:
            out[key] = top
    return out


def leading_contradicted(r: dict, consensus: dict) -> str | None:
    """Why this entry's most-cited variant is itself suspect, or None.

    The triage in summarize() assumes the leading variant is the true one and
    the stragglers are invented. Usually right — and catastrophically wrong
    where a whole cluster of pages inherited the same fabrication. In this
    corpus 10.17763/haer.81.4.t2k0m13756113566 is cited 32 times, never once as
    Harvard Educational Review 81(4), which is what its own DOI says and what
    the other five haer DOIs are all cited as. Following the majority there
    means rewriting the two correct citations to match thirty wrong ones."""
    journal, vol, issue, _page = r["variants"][0][0]
    enc = encoded_volume_issue(r["doi"])
    if enc and enc != (vol, issue):
        return (f"DOI encodes volume {enc[0]} issue {enc[1]}, "
                f"leading variant says {vol}({issue})")
    key = journal_token(r["doi"])
    if key and key in consensus and consensus[key].lower() != journal.lower():
        return (f"every other DOI under {key[0]}/{key[1]} is cited as "
                f"\"{consensus[key]}\", not \"{journal}\"")
    return None


def _variant_counts(r: dict) -> list:
    return [len(es) for _, es in r["variants"]]


def triage(r: dict, consensus: dict | None = None) -> str:
    """How settleable this entry is without a registry lookup.

    "decided"  - one variant dominates at 3:1 or better. The stragglers are
                 almost certainly the invented ones, and a Crossref call is
                 confirming a strong prior rather than discovering an answer.
    "split"    - no variant leads by that much, very often 1-vs-1. There is no
                 majority to appeal to and "majority" in the report means
                 nothing; only the registry settles it.
    "contra"   - a variant leads, but the DOI's own encoding or its journal's
                 consensus says that leader is wrong. Ranked first, because
                 following the majority here rewrites correct citations to
                 match incorrect ones. See leading_contradicted().

    This is the triage the raw dumps could not express. Reporting 166 DOIs as
    one flat list implies 166 equal problems, when in practice a large share
    are one confident reading plus a couple of stragglers, and the rest are
    genuine coin-flips that must not be resolved by counting."""
    if consensus is not None and leading_contradicted(r, consensus):
        return "contra"
    counts = _variant_counts(r)
    if len(counts) < 2:
        return "decided"
    return "decided" if counts[0] >= 3 * counts[1] else "split"


def _fmt_variant(v) -> str:
    return f"{v[0]} {v[1]}({v[2]}), {v[3]}" if isinstance(v, tuple) else str(v)


def summarize(results: list[dict], noun: str, conflict_key: str = "conflict",
              consensus: dict | None = None) -> str:
    """A triage table instead of every affected file. See triage()."""
    conflicts = [r for r in results if r["severity"] == conflict_key]
    other = [r for r in results if r["severity"] != conflict_key]
    if not conflicts:
        return f"No {noun} found." + (
            f" ({len(other)} lower-severity variant(s) — --full to list.)" if other else "")

    minority = sum(sum(_variant_counts(r)[1:]) for r in conflicts)
    tri = {id(r): triage(r, consensus) for r in conflicts}
    contra = [r for r in conflicts if tri[id(r)] == "contra"]
    decided = [r for r in conflicts if tri[id(r)] == "decided"]
    split = [r for r in conflicts if tri[id(r)] == "split"]

    lines = [f"{len(conflicts)} DOI(s) with {noun}; {minority} citation(s) disagree with "
             f"their DOI's leading reading.\n"]
    # Only claim a contra count when the contradiction test could actually run.
    # triage() returns "contra" only when a consensus was supplied, so on a
    # report without one the line is structurally always "0 contra" — which
    # reads as "checked, found none" rather than "not checked", and that is
    # the more dangerous of the two things to say.
    if consensus is not None:
        lines.append(f"  {len(contra)} contra   - a variant leads, but the DOI itself "
                     f"contradicts it. FIX THESE FIRST: following the majority here "
                     f"rewrites correct citations to match wrong ones")
    lines += [f"  {len(decided)} decided  - one variant leads 3:1 or better; the stragglers "
              f"are the likely fabrications",
              f"  {len(split)} split    - no variant leads; only Crossref settles these\n",
              "  worst by number of citations affected:\n"]
    # Contradicted first regardless of size — a wrong leader on five pages is
    # more urgent than an uncertain one on a hundred.
    ranked = sorted(conflicts, key=lambda r: (tri[id(r)] != "contra",
                                              -sum(_variant_counts(r))))
    for r in ranked[:12]:
        counts = _variant_counts(r)
        lines.append(f"  {sum(counts):5} cites  {len(counts)} variants  [{tri[id(r)]:7}]  "
                     f"{r['doi']}")
        lines.append(f"                  leading: {_fmt_variant(r['variants'][0][0])[:78]}")
        if consensus is not None:
            why = leading_contradicted(r, consensus)
            if why:
                lines.append(f"                  BUT {why}")
    if len(ranked) > 12:
        lines.append(f"\n  ... and {len(ranked) - 12} more.")
    if other:
        lines.append(f"\n{len(other)} lower-severity entr(y/ies) not shown "
                     f"(naming style or truncation).")
    lines.append("\nRun with --full for every affected file.")
    return "\n".join(lines)


def summarize_collisions(collisions: list[dict]) -> str:
    if not collisions:
        return "No DOI collisions found — every DOI is cited for one paper."
    lines = [f"{len(collisions)} DOI(s) attached to more than one paper. Every one needs "
             f"Crossref: which side is wrong cannot be counted out, and picking the "
             f"popular one is how the wrong citation becomes canonical.\n",
             "  worst by number of citations affected:\n"]
    ranked = sorted(collisions, key=lambda c: -sum(len(cl) for cl in c["clusters"]))
    for c in ranked[:12]:
        n = sum(len(cl) for cl in c["clusters"])
        lines.append(f"  {n:5} cites  {len(c['clusters'])} paper(s)  {c['doi']}")
        for cl in c["clusters"][:2]:
            lines.append(f"                  {cl[0]['line'][2:90].strip()}")
    if len(ranked) > 12:
        lines.append(f"\n  ... and {len(ranked) - 12} more.")
    lines.append("\nRun with --full for every affected file.")
    return "\n".join(lines)


# --- Near-identical DOI families -------------------------------------------
#
# The fourth defect shape, and the one the other three checks are blind to by
# construction. find_conflicts reports "this paper carries N DOIs" and stops
# there; it treats 10.1073/pnas.1523698113 vs 10.1177/1745691615621640 (two
# unrelated registrants) exactly like 10.1177/1745691615621640 vs
# ...621643 vs ...621645 — nine SAGE suffixes for okonofua-2016 that differ
# from each other by two or three digits.
#
# The second shape is not a disagreement between sources. It is one DOI that
# the model reproduced from memory several times, getting the tail wrong a
# different way each time. At most one member of such a family can be the
# real article, so a family of N contributes at least N-1 provably wrong DOIs
# — which is a stronger statement than "these disagree", and it is available
# without any lookup.
#
# It is emphatically NOT a verdict on WHICH member is wrong. ehri-2001 cites
# 10.1598/rrq.36.3.2 and 10.1598/rrq.36.3.3 — one character apart, and both
# real: consecutive articles in the same Reading Research Quarterly issue.
# Nothing in the shape of a suffix distinguishes that from a fabricated
# neighbour. The family is a signal that narrows where to look; Crossref
# still says which one survives. See resolve_citation_metadata.py, where a
# family member Crossref 404s while a sibling resolves to the cited paper is
# the one case the family makes actionable.

MAX_SUFFIX_EDITS = 3


def _edit_distance(a: str, b: str, cap: int = MAX_SUFFIX_EDITS) -> int:
    """Levenshtein distance, abandoned once it provably exceeds `cap`."""
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > cap:
            return cap + 1
        prev = cur
    return prev[-1]


def near_identical(a: str, b: str, cap: int = MAX_SUFFIX_EDITS) -> bool:
    """True if two DOIs are the same registrant with near-identical suffixes.

    Requires an identical prefix: 10.1073/... and 10.1177/... are different
    publishers, and a coincidental suffix resemblance across registrants says
    nothing. Within a registrant, a suffix is an opaque article identifier, so
    two that differ by a couple of characters are either neighbours in one
    issue or one of them is a misremembering of the other."""
    pa, _, sa = a.partition("/")
    pb, _, sb = b.partition("/")
    if pa != pb or not sa or not sb or sa == sb:
        return False
    return _edit_distance(sa, sb, cap) <= cap


def find_doi_variant_families(by_key: dict, touched_files: set = None) -> list[dict]:
    """Return citation clusters that cite two or more near-identical DOIs.

    Runs over the same author-year + title clusters find_conflicts uses, so a
    "family" is always several DOIs offered for one paper — never two papers
    that happen to sit next to each other in an issue."""
    families = []
    for key, entries in by_key.items():
        if len(entries) < 2:
            continue
        for cluster in _cluster_by_title(entries):
            if touched_files and not any(e["source"] in touched_files for e in cluster):
                continue
            dois = sorted({e["doi"] for e in cluster if e["doi"]})
            if len(dois) < 2:
                continue
            # Union-find over near_identical, so a chain a~b~c groups as one
            # family even where a and c are three edits apart.
            parent = {d: d for d in dois}

            def find(d):
                while parent[d] != d:
                    parent[d] = parent[parent[d]]
                    d = parent[d]
                return d

            for i, a in enumerate(dois):
                for b in dois[i + 1:]:
                    if near_identical(a, b):
                        parent[find(a)] = find(b)
            groups = defaultdict(list)
            for d in dois:
                groups[find(d)].append(d)
            for members in groups.values():
                if len(members) < 2:
                    continue
                counts = {d: sum(1 for e in cluster if e["doi"] == d)
                          for d in members}
                families.append({
                    "key": key,
                    "prefix": members[0].partition("/")[0],
                    "members": sorted(members, key=lambda d: (-counts[d], d)),
                    "counts": counts,
                    "entries": [e for e in cluster if e["doi"] in set(members)],
                })
    return sorted(families, key=lambda f: (-len(f["members"]),
                                           -sum(f["counts"].values()), f["key"]))


def variant_siblings(families: list[dict]) -> dict:
    """{doi -> set of the other DOIs offered for the same paper}."""
    out = defaultdict(set)
    for f in families:
        for d in f["members"]:
            out[d] |= set(f["members"]) - {d}
    return dict(out)


def summarize_variant_families(families: list[dict]) -> str:
    if not families:
        return "No near-identical DOI families found."
    cites = sum(sum(f["counts"].values()) for f in families)
    wrong = sum(len(f["members"]) - 1 for f in families)
    lines = [
        f"{len(families)} paper(s) are cited with a family of near-identical DOIs "
        f"({cites} citation(s), {sum(len(f['members']) for f in families)} distinct DOIs).",
        f"At least {wrong} of those DOIs are wrong: the members of a family share a "
        f"registrant and differ by a few characters, so at most one can be the article.",
        "",
        "Which one survives still needs Crossref — 10.1598/rrq.36.3.2 and .3 differ by",
        "one character and are both real, consecutive articles in the same issue.",
        "",
    ]
    for f in families[:12]:
        lines.append(f"  {f['key']}  —  {len(f['members'])} variants under {f['prefix']}/")
        for d in f["members"]:
            lines.append(f"      {f['counts'][d]:4}x  {d}")
    if len(families) > 12:
        lines.append(f"\n  ... and {len(families) - 12} more.")
    lines.append("\nRun with --full for every affected file.")
    return "\n".join(lines)


def format_variant_report(families: list[dict]) -> str:
    if not families:
        return "No near-identical DOI families found."
    lines = [f"{len(families)} near-identical DOI famil(y/ies):\n"]
    for f in families:
        lines.append(f"## {f['key']}  ({f['prefix']}/)")
        for e in sorted(f["entries"], key=lambda e: (e["doi"], e["source"])):
            lines.append(f"  - {e['source']}: {e['doi']}")
        lines.append("")
    return "\n".join(lines)


def conflict_shape(c: dict) -> str:
    """"fill" if one DOI is agreed and the rest merely omit it, else "split"."""
    return "fill" if len(c["dois"]) == 1 else "split"


def format_report(conflicts: list[dict], full: bool = False) -> str:
    """Summarise each conflict by its shape; --full dumps every citation line.

    The flat dump this replaced printed one line per citation, so patall-2008 —
    where 22 pages agree on 10.1037/0033-2909.134.2.270 and exactly one omits
    it — arrived as 23 near-identical lines with nothing saying which one was
    the problem. A reader reasonably concludes the check is misfiring. It was
    not: 22 of those lines are the evidence and one is the finding, and a
    report that cannot tell them apart makes the reader re-derive the
    difference by eye on every entry.

    The two shapes need different work, which is why they are separated rather
    than counted together:

      fill  - one agreed DOI, N citations omit it. standardize_citations.py
              writes it onto them, but only where Crossref confirms the DOI
              resolves to the paper being cited. That gate is the whole
              difference between patall-2008 (22 assert / 1 omits) and
              bandura-1977 (1 asserts / 67 omit) — identical in shape, and
              copying the majority is right in one and catastrophic in the
              other. Direction of the majority is not evidence.

      split - two or more DOIs are asserted for one paper. Nothing can count
              its way out of this; only the registry settles it."""
    if not conflicts:
        return "No citation conflicts found."
    fill = [c for c in conflicts if conflict_shape(c) == "fill"]
    split = [c for c in conflicts if conflict_shape(c) == "split"]
    to_fill = sum(sum(1 for e in c["entries"] if not e["doi"]) for c in fill)

    lines = [f"{len(conflicts)} citation conflict(s).\n",
             f"  {len(split)} split - two or more DOIs asserted for one paper; only Crossref "
             f"settles these",
             f"  {len(fill)} fill  - one agreed DOI that {to_fill} citation(s) omit; "
             f"scripts/standardize_citations.py writes it where Crossref confirms it\n"]

    # Split first: a paper carrying two DOIs is a live fabrication, while a
    # missing DOI is only an incomplete citation.
    for c in sorted(split, key=lambda c: -len(c["entries"])):
        lines.append(f"## {c['key']}  —  {len(c['dois'])} DOIs over "
                     f"{len(c['entries'])} citation(s)")
        by_doi = defaultdict(list)
        for e in c["entries"]:
            by_doi[e["doi"]].append(e)
        for doi, es in sorted(by_doi.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"     {len(es):4}x  {doi or '(no DOI)'}")
            for e in (es if full else es[:2]):
                lines.append(f"             {e['source']}")
            if not full and len(es) > 2:
                lines.append(f"             ... and {len(es) - 2} more")
        lines.append("")

    for c in sorted(fill, key=lambda c: -sum(1 for e in c["entries"] if not e["doi"])):
        doi = next(iter(c["dois"]))
        missing = [e for e in c["entries"] if not e["doi"]]
        have = len(c["entries"]) - len(missing)
        lines.append(f"## {c['key']}  —  {have} assert / {len(missing)} omit   {doi}")
        for e in (missing if full or len(missing) <= 5 else missing[:5]):
            lines.append(f"     omits: {e['source']}")
        if not full and len(missing) > 5:
            lines.append(f"     ... and {len(missing) - 5} more")
        lines.append("")

    if not full:
        lines.append("Run with --full to list every citing page.")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--type", choices=PAGE_TYPES, default=None,
                        help="Restrict the corpus scanned to one page type (default: whole wiki)")
    parser.add_argument("--files", nargs="+", default=None,
                        help="Only report conflicts touching these bundle-relative files "
                             "(the corpus scanned is still the whole wiki, so a conflict "
                             "against an older unrelated page is still caught)")
    parser.add_argument("--collisions", action="store_true",
                        help="Report the other direction instead: DOIs asserted for more "
                             "than one paper (see find_doi_collisions)")
    parser.add_argument("--metadata", action="store_true",
                        help="Report DOIs whose citations disagree about journal, volume, "
                             "issue or pages (see find_metadata_divergence)")
    parser.add_argument("--full", action="store_true",
                        help="List every affected file rather than the triage summary. "
                             "The full dumps run to thousands of lines.")
    parser.add_argument("--titles", action="store_true",
                        help="Report DOIs cited with more than one distinct title "
                             "(see find_title_divergence)")
    parser.add_argument("--variants", action="store_true",
                        help="Report papers cited with a family of near-identical DOIs — "
                             "same registrant, suffixes a few characters apart "
                             "(see find_doi_variant_families)")
    args = parser.parse_args()

    page_types = PAGE_TYPES if args.files else ((args.type,) if args.type else PAGE_TYPES)
    by_key = load_all_citations(page_types)
    touched = set(args.files) if args.files else None

    if args.variants:
        families = find_doi_variant_families(by_key, touched)
        print(format_variant_report(families) if args.full
              else summarize_variant_families(families))
        sys.exit(0 if not families else 1)

    if args.titles:
        results = find_title_divergence(load_by_doi(by_key), touched)
        print(format_title_report(results) if args.full
              else summarize(results, "invented titles"))
        sys.exit(0 if not any(r["severity"] == "conflict" for r in results) else 1)

    if args.metadata:
        results = find_metadata_divergence(load_by_doi(by_key), touched)
        print(format_metadata_report(results) if args.full
              else summarize(results, "fabricated journal metadata",
                             consensus=token_consensus(load_by_doi(by_key))))
        sys.exit(0 if not any(r["severity"] == "conflict" for r in results) else 1)

    if args.collisions:
        collisions = find_doi_collisions(load_by_doi(by_key), touched)
        print(format_collision_report(collisions) if args.full
              else summarize_collisions(collisions))
        sys.exit(0 if not collisions else 1)

    conflicts = find_conflicts(by_key, touched)
    print(format_report(conflicts, args.full))
    sys.exit(0 if not conflicts else 1)


if __name__ == "__main__":
    main()
