"""
validator.py — Deterministic structural checks on a model's JSON contribution
output. This is the "did it accurately complete all required fields" half of
quality measurement; judge.py covers the half that needs an LLM (does the
content actually reflect the source article).

No field being merely present-and-non-empty proves it's correct — that's the
judge's job — but every field a page template requires is enforced here, along
with referential integrity (subclaim -> evidence anchors, cross-link slugs)
that's cheap to check exactly and easy for a smaller model to get wrong.
"""

import re
from dataclasses import dataclass, field

from . import consistency, ground_truth

ALLOWED_TYPES = {"claim", "principle", "element", "pattern", "strategy", "theory"}
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EVIDENCE_TAG_RE = re.compile(r"^[+~-][SMW]$|^X$")
YEAR_RE = re.compile(r"\b(19|20)\d{2}[a-z]?\b")
CITATION_LINK_RE = re.compile(r"(doi\.org|https?://)", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"^(\.\.\.|tbd|todo|n/?a|none|\[.*\])$", re.IGNORECASE)

CLAIM_STATUS_VALUES = {"strong", "moderate", "weak", "mixed"}


@dataclass
class Issue:
    contribution_index: int
    contribution_slug: str
    severity: str  # "error" | "warning"
    field: str
    message: str


@dataclass
class ValidationReport:
    has_article_meta: bool
    n_contributions: int
    issues: list = field(default_factory=list)
    fields_checked: int = 0
    fields_ok: int = 0
    parse_error: str = ""

    @property
    def completeness_score(self) -> float:
        if self.fields_checked == 0:
            return 0.0
        return round(self.fields_ok / self.fields_checked, 3)

    @property
    def error_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "error")

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == "warning")

    @property
    def passed(self) -> bool:
        return not self.parse_error and self.error_count == 0 and self.n_contributions > 0


def _is_placeholder(text) -> bool:
    if not isinstance(text, str) or not text.strip():
        return True
    return bool(PLACEHOLDER_RE.match(text.strip()))


def _looks_like_real_citation(citation) -> bool:
    if not isinstance(citation, str) or len(citation.strip()) < 20:
        return False
    return bool(YEAR_RE.search(citation)) and bool(CITATION_LINK_RE.search(citation))


class _Checker:
    """Accumulates (checked, ok) pairs and issues for one contribution."""

    def __init__(self, report: ValidationReport, index: int, slug: str, ground_truth_enabled: bool = False,
                 require_source_quotes: bool = False, article_text: str = None,
                 comparison_sets: list = None):
        self.report = report
        self.index = index
        self.slug = slug or f"contribution[{index}]"
        self.ground_truth_enabled = ground_truth_enabled
        self.require_source_quotes = require_source_quotes
        self.article_text = article_text
        self.comparison_sets = comparison_sets or []

    def error(self, field_name: str, message: str) -> None:
        self.report.issues.append(Issue(self.index, self.slug, "error", field_name, message))

    def warn(self, field_name: str, message: str) -> None:
        self.report.issues.append(Issue(self.index, self.slug, "warning", field_name, message))

    def check(self, ok: bool, field_name: str, message: str, severity: str = "error") -> bool:
        self.report.fields_checked += 1
        if ok:
            self.report.fields_ok += 1
        else:
            (self.error if severity == "error" else self.warn)(field_name, message)
        return ok

    def check_citation_ground_truth(self, field_name: str, citation_text) -> None:
        """The shape check (`_looks_like_real_citation`) only confirms the
        text LOOKS like a citation — a year-shaped substring, a doi.org/http
        substring — never that the DOI actually resolves to a real work.
        That gap is exactly where a fabricated-but-plausible citation slips
        through. Live-checks against Crossref (free, no key) when a DOI is
        present; silently does nothing when Crossref can't be reached at
        all, so a network hiccup is never mistaken for evidence of
        fabrication, and does nothing when there's no DOI to extract (the
        shape check already flags a missing DOI on its own)."""
        if not self.ground_truth_enabled:
            return
        result = ground_truth.verify_citation(citation_text)
        if result is None or result["error"]:
            return
        if result["exists"] is False:
            self.error(field_name, f"citation's {result['kind']} ({result['id']}) does not resolve to any "
                                    f"real work — likely fabricated.")
        elif result["year_match"] is False:
            self.warn(field_name, f"citation's stated year doesn't match the record found for its "
                                   f"{result['kind']} ({result['id']}).")

    def check_source_quote(self, field_name: str, source_quote) -> None:
        """A citation resolving to a real paper (check_citation_ground_truth)
        doesn't prove the specific CLAIM attributed to it is real — the model
        could cite a genuine DOI in support of something that paper never
        said. This checks a required verbatim source_quote field against the
        actual article text the model was given, which is the only local,
        deterministic way to catch that. Off by default (require_source_quotes)
        since no prompt version's schema includes this field yet — turning it
        on before one does will legitimately fail almost everything, which is
        the intended signal for the next auto-optimize round to react to."""
        if not self.require_source_quotes:
            return
        if not source_quote or not str(source_quote).strip():
            self.error(field_name, "missing — a short verbatim quote from the article supporting this "
                                    "evidence entry is required (checked against the source text).")
            return
        if self.article_text is None:
            return  # nothing to check the quote against (e.g. re-scoring without the cached article text)
        if not ground_truth.quote_is_grounded(source_quote, self.article_text):
            shown = str(source_quote).strip()
            shown = shown if len(shown) <= 80 else shown[:80] + "…"
            self.error(field_name, f"quote {shown!r} does not appear in the source article (checked "
                                    f"verbatim, with a fuzzy word-overlap fallback) — likely fabricated or "
                                    f"too heavily paraphrased; quotes must be copied verbatim.")

    def check_consistency(self, field_name: str, value) -> None:
        """SelfCheckGPT-style: no external source to check against here —
        just whether this exact citation/quote also shows up in independent
        re-generations of the same (model, article) pair (see
        consistency.py). A fact the model can't reproduce consistently
        across samples is a confabulation risk even when nothing else can
        ground-truth it. Off by default (comparison_sets empty unless
        --consistency-samples > 1 was passed) — this needs real extra
        generation calls, so it can't be retrofitted onto cached results the
        way ground-truthing and quote-grounding can."""
        if not self.comparison_sets or not value:
            return
        matched = consistency.match_count(value, self.comparison_sets)
        total = len(self.comparison_sets)
        if matched < total:
            shown = str(value).strip()
            shown = shown if len(shown) <= 80 else shown[:80] + "…"
            self.warn(field_name, f"{shown!r} reproduced in only {matched}/{total} independent "
                                   f"re-generations of this article — possible confabulation "
                                   f"(SelfCheckGPT-style consistency check).")


def _existing_slug_set(existing_slugs: dict) -> set:
    out = set()
    for slugs in existing_slugs.values():
        out.update(slugs)
    return out


def validate_output(parsed: dict, existing_slugs: dict, ground_truth_enabled: bool = False,
                     require_source_quotes: bool = False, article_text: str = None,
                     comparison_sets: list = None) -> ValidationReport:
    """existing_slugs: {folder: [slug, ...]} — the real wiki slugs offered to the
    model in the prompt, used to catch invented cross-links.

    ground_truth_enabled: also live-verify each citation's DOI/arXiv id
    against Crossref/arXiv (see ground_truth.py) instead of only checking
    that it LOOKS like a real citation. Off by default — see
    ground_truth.py's module docstring for why this is opt-in.

    require_source_quotes / article_text: require (and verify against the
    actual article text) a verbatim source_quote field on each claim's
    evidence entries — see ground_truth.py's module docstring and
    _Checker.check_source_quote. Off by default: no existing prompt version's
    schema includes this field yet.

    comparison_sets: normalized citation/quote sets from independent
    re-generations of this same (model, article) pair (see consistency.py
    and consistency.extraction_identifier_set) — enables a SelfCheckGPT-style
    consistency check per citation/quote. Empty unless --consistency-samples
    > 1 was passed."""
    article = parsed.get("article") if isinstance(parsed, dict) else None
    contributions = parsed.get("contributions") if isinstance(parsed, dict) else None
    contributions = contributions if isinstance(contributions, list) else []

    report = ValidationReport(has_article_meta=isinstance(article, dict), n_contributions=len(contributions))

    if not isinstance(parsed, dict):
        report.parse_error = "Top-level output is not a JSON object."
        return report
    if not isinstance(article, dict):
        report.issues.append(Issue(-1, "article", "error", "article", "Missing or malformed top-level `article` object."))
    else:
        for f in ("title", "summary"):
            c = _Checker(report, -1, "article")
            c.check(not _is_placeholder(article.get(f)), f, f"article.{f} is missing or a placeholder.")

    if not contributions:
        report.issues.append(Issue(-1, "-", "warning", "contributions",
                                    "No contributions extracted — verify this article genuinely offers nothing citable, "
                                    "rather than the model giving up."))
        return report

    real_slugs = _existing_slug_set(existing_slugs)
    sibling_slugs = {c.get("slug") for c in contributions if isinstance(c, dict) and c.get("slug")}
    known_slugs = real_slugs | sibling_slugs

    for i, contrib in enumerate(contributions):
        if not isinstance(contrib, dict):
            report.issues.append(Issue(i, "-", "error", "contribution", "Contribution is not a JSON object."))
            continue
        slug = contrib.get("slug", "")
        c = _Checker(report, i, slug, ground_truth_enabled=ground_truth_enabled,
                     require_source_quotes=require_source_quotes, article_text=article_text,
                     comparison_sets=comparison_sets)

        ctype = contrib.get("type")
        c.check(ctype in ALLOWED_TYPES, "type", f"type '{ctype}' is not one of {sorted(ALLOWED_TYPES)}.")
        c.check(not _is_placeholder(contrib.get("title")), "title", "title is missing or a placeholder.")
        c.check(bool(SLUG_RE.match(slug or "")), "slug", f"slug '{slug}' must be lowercase-hyphenated ([a-z0-9-]+).")
        c.check(contrib.get("status") == "draft", "status", "status should be 'draft' for a freshly ingested page.",
                severity="warning")

        if real_slugs and slug in real_slugs:
            c.warn("slug", f"slug '{slug}' collides with an existing wiki page — "
                            "should this have been an update instead of a new page?")

        if ctype == "claim":
            _validate_claim(c, contrib, known_slugs)
        elif ctype in ALLOWED_TYPES:
            _validate_other(c, contrib, known_slugs)

    return report


def _check_cross_links(c: _Checker, contrib: dict, known_slugs: set, list_field: str,
                        slug_key: str = None) -> None:
    items = contrib.get(list_field)
    if not isinstance(items, list):
        return
    for item in items:
        target_slug = item.get(slug_key) if (slug_key and isinstance(item, dict)) else item
        if not target_slug:
            continue
        if not isinstance(target_slug, str):
            # A model occasionally emits an object here instead of a plain
            # string slug — flag it as a real validation issue rather than
            # crashing on `dict in known_slugs` (unhashable).
            c.error(list_field, f"{list_field} entry should be a plain string slug, "
                                 f"got {type(target_slug).__name__}.")
            continue
        if known_slugs and target_slug not in known_slugs:
            c.warn(list_field, f"'{target_slug}' in {list_field} is not an existing wiki slug or a "
                                f"sibling contribution in this output — possible hallucinated link.")


def _validate_claim(c: _Checker, contrib: dict, known_slugs: set) -> None:
    c.check(bool(re.match(r"^CL-", str(contrib.get("id", "")))), "id", "claim id should look like 'CL-<shortcode>'.")
    c.check(contrib.get("evidence_strength") in CLAIM_STATUS_VALUES, "evidence_strength",
            f"evidence_strength must be one of {sorted(CLAIM_STATUS_VALUES)}.")

    subclaims = contrib.get("subclaims")
    c.check(isinstance(subclaims, list) and len(subclaims) > 0, "subclaims", "claim needs at least one subclaim.")
    evidence = contrib.get("evidence")
    c.check(isinstance(evidence, list) and len(evidence) > 0, "evidence", "claim needs at least one evidence entry.")

    evidence_anchors = set()
    if isinstance(evidence, list):
        for j, ev in enumerate(evidence):
            if not isinstance(ev, dict):
                c.error(f"evidence[{j}]", "evidence entry is not an object.")
                continue
            anchor = ev.get("anchor")
            if anchor:
                evidence_anchors.add(anchor)
            c.check(bool(anchor), f"evidence[{j}].anchor", "evidence entry missing an anchor id.")
            c.check(_looks_like_real_citation(ev.get("citation")), f"evidence[{j}].citation",
                    "citation should include a year and a DOI/URL.")
            c.check_citation_ground_truth(f"evidence[{j}].citation", ev.get("citation"))
            c.check_consistency(f"evidence[{j}].citation", ev.get("citation"))
            c.check(isinstance(ev.get("quality"), int) and 1 <= ev["quality"] <= 4,
                    f"evidence[{j}].quality", "quality must be an integer 1-4.")
            c.check(isinstance(ev.get("impact"), int) and 0 <= ev["impact"] <= 3,
                    f"evidence[{j}].impact", "impact must be an integer 0-3.")
            c.check(isinstance(ev.get("description"), str) and len(ev["description"]) >= 40,
                    f"evidence[{j}].description", "description should be a substantive 2-4 sentence summary.",
                    severity="warning")
            c.check_source_quote(f"evidence[{j}].source_quote", ev.get("source_quote"))
            c.check_consistency(f"evidence[{j}].source_quote", ev.get("source_quote"))

    if isinstance(subclaims, list):
        for j, sc in enumerate(subclaims):
            if not isinstance(sc, dict):
                c.error(f"subclaims[{j}]", "subclaim is not an object.")
                continue
            c.check(isinstance(sc.get("q"), int) and 1 <= sc["q"] <= 4, f"subclaims[{j}].q", "q must be an integer 1-4.")
            c.check(isinstance(sc.get("i"), int) and 0 <= sc["i"] <= 3, f"subclaims[{j}].i", "i must be an integer 0-3.")
            c.check(not _is_placeholder(sc.get("text")), f"subclaims[{j}].text", "subclaim text is missing or a placeholder.")
            ref = sc.get("evidence_ref")
            ok = bool(ref) and (not evidence_anchors or ref in evidence_anchors)
            c.check(ok, f"subclaims[{j}].evidence_ref",
                    f"evidence_ref '{ref}' does not match any evidence[].anchor — broken same-page reference.")

    key_sources = contrib.get("key_sources")
    c.check(isinstance(key_sources, list) and len(key_sources) > 0, "key_sources", "claim needs at least one key source.")
    if isinstance(key_sources, list):
        # Claims never had their key_sources entries checked past "is this a
        # non-empty list" — only elements/principles/patterns/strategies
        # (_validate_other, below) checked each entry's citation shape. A
        # claim's key_sources duplicate the same citations already scrutinized
        # in its evidence[] list, but there's no reason to leave a second,
        # unrelated copy of the same fabricated-DOI hole unchecked here.
        for j, src in enumerate(key_sources):
            c.check(_looks_like_real_citation(src), f"key_sources[{j}]",
                    "citation should include a year and a DOI/URL.", severity="warning")
            c.check_citation_ground_truth(f"key_sources[{j}]", src)

    _check_cross_links(c, contrib, known_slugs, "related_claims")


def _validate_other(c: _Checker, contrib: dict, known_slugs: set) -> None:
    c.check(isinstance(contrib.get("description"), str) and len(contrib["description"]) >= 20,
            "description", "description is missing or too short to be substantive.")

    for f in ("target_learners", "target_learning_goals"):
        vals = contrib.get(f)
        c.check(isinstance(vals, list) and len(vals) > 0, f, f"{f} should list at least one entry.",
                severity="warning")

    has_context = bool(contrib.get("requirements")) or bool(contrib.get("constraints"))
    c.check(has_context, "requirements/constraints", "should specify at least one requirement or constraint.",
            severity="warning")

    key_sources = contrib.get("key_sources")
    c.check(isinstance(key_sources, list) and len(key_sources) > 0, "key_sources",
            f"{contrib.get('type')} needs at least one key source.")
    if isinstance(key_sources, list):
        for j, src in enumerate(key_sources):
            c.check(_looks_like_real_citation(src), f"key_sources[{j}]",
                    "citation should include a year and a DOI/URL.", severity="warning")
            c.check_citation_ground_truth(f"key_sources[{j}]", src)

    claims_cited = contrib.get("claims_cited")
    if isinstance(claims_cited, list):
        for j, cc in enumerate(claims_cited):
            if not isinstance(cc, dict):
                c.error(f"claims_cited[{j}]", "claims_cited entry is not an object.")
                continue
            tag = cc.get("tag", "")
            c.check(bool(EVIDENCE_TAG_RE.match(tag)), f"claims_cited[{j}].tag",
                    f"tag '{tag}' is not a valid evidence tag (+S/+M/+W, ~S/~M/~W, -S/-M/-W, X).")

    _check_cross_links(c, contrib, known_slugs, "claims_cited", slug_key="slug")
    _check_cross_links(c, contrib, known_slugs, "related")
    _check_cross_links(c, contrib, known_slugs, "theory_supporting")
