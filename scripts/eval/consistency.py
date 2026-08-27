"""
consistency.py — SelfCheckGPT-style consistency sampling (Manakul et al.,
EMNLP 2023): no external knowledge base, no source text to check against —
just generate the same (model, article) pair multiple times independently
and see whether a specific citation or quote survives across samples. A
fact the model states differently (or drops entirely) each time it's asked
is a confabulation risk even when there's nothing to ground-truth it
against; a fact it reproduces identically every time is much more likely to
be something the model actually "knows" rather than improvised in the
moment.

This is a genuinely different signal from ground_truth.py's two techniques:
DOI/arXiv resolution and quote-grounding both check a claim against an
INDEPENDENT external source (Crossref, arXiv, the article text). Consistency
checking has no independent source at all — it only checks the model
against itself, which is exactly SelfCheckGPT's point: internal
inconsistency is informative even with zero external verification.

Opt-in (--consistency-samples N, N>1, on `run`/`optimize`/`auto-optimize`)
and expensive in a way the other two techniques aren't: N samples means
N-1 EXTRA full generation calls per (model, article) pair, on top of the
one that's actually used as the record. Unlike --ground-truth or
--require-source-quotes, this can't be retrofitted onto already-cached
results (spotcheck has nothing to resample from), so it isn't offered there.
"""

import re

_WORD_RE = re.compile(r"\w+")


def _normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def extraction_identifier_set(parsed: dict) -> set:
    """The set of normalized citation/quote strings found anywhere in one
    parsed extraction's evidence entries — what a comparison sample is
    reduced to for matching. Deliberately citation- and quote-text based,
    not full-JSON comparison: contribution count, order, and slugs can
    legitimately vary between independent samples without indicating any
    problem (a model may reasonably phrase a title differently each time);
    the specific factual payload — which paper, which exact sentence — is
    what should actually stay stable if it's real."""
    out = set()
    if not isinstance(parsed, dict):
        return out
    contributions = parsed.get("contributions")
    if not isinstance(contributions, list):
        return out
    for contrib in contributions:
        if not isinstance(contrib, dict):
            continue
        for ev in (contrib.get("evidence") or []):
            if not isinstance(ev, dict):
                continue
            citation = ev.get("citation")
            if isinstance(citation, str) and citation.strip():
                out.add(_normalize_ws(citation))
            quote = ev.get("source_quote")
            if isinstance(quote, str) and quote.strip():
                out.add(_normalize_ws(quote))
        for src in (contrib.get("key_sources") or []):
            if isinstance(src, str) and src.strip():
                out.add(_normalize_ws(src))
    return out


def match_count(value, comparison_sets: list) -> int:
    """How many of the independent comparison samples contain something
    matching `value` (exact after whitespace normalization). A citation or
    quote copied verbatim from the article should reproduce identically
    across independent samples if the model is actually drawing on the same
    real source each time; minor rewording differences are themselves mild
    evidence the "fact" isn't stable, which is exactly what this is meant
    to surface — unlike ground_truth.quote_is_grounded(), no fuzzy fallback
    is used here on purpose."""
    if not value or not isinstance(value, str):
        return 0
    norm = _normalize_ws(value)
    if not norm:
        return 0
    return sum(1 for s in comparison_sets if norm in s)
