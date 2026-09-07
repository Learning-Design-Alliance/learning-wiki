#!/usr/bin/env python3
"""
observation_lib.py — the structured record of what a study actually observed.

A claim page argues something; an observation file records the configuration
that argument rests on. `d = .78` is not a weight between two concepts, it is
one measurement of one intervention on one population in one setting against
one comparison at one point in time. This module is the schema for that tuple,
and the validator for it.

WHY THIS IS NOT IN THE CLAIM'S FRONTMATTER
------------------------------------------
The obvious home is a `sources[]` entry, and it is the wrong one, for two
reasons that were established by reading the code rather than guessed at:

1. `sources[]` is DERIVED, not authored. `sync_evidence_codes.py --apply`
   rebuilds the whole block from the body's `## Evidence` section through
   `okf_lib.dump_frontmatter`, which emits exactly id/resource/title/author/
   q/i/n. Anything else nested there is silently destroyed on the next run —
   and that script runs inside `run_scrape_batch.py`'s unattended chain.
2. `lint.check_source_entry_keys` holds a closed key set at four-space indent,
   precisely so a rewrite that lands on a YAML key is caught. A new key there
   is indistinguishable from that damage.

And a third reason from the data: a study is cited by many claims (the wiki
has 12,893 citations over ~1,232 author-year keys). An observation belongs to
the STUDY, not to any one claim that appeals to it. Copying it per claim is
the drift shape this repo has lost weeks to on DOIs.

So: one file per study, keyed by the same author-year key `check_citations.py`
and `authorities.ndjson` already use, and NOT ONE BYTE of any existing claim
page changes. `appears_in` carries the join, and the validator checks it
resolves — so renaming a claim or an evidence heading fails lint rather than
silently orphaning the record.

ABSENCE IS NOT A VERDICT
------------------------
The same discipline as `crossref_reachable: false` vs `flagged`, and `"doi":
null` vs an absent `doi`. An omitted field means "not established". A field
under `observability` set to `unreported` means "somebody read the paper and
it does not say". Only the second is evidence about the paper. Nothing here
may be inferred: `study.design.family` is what the authors call their design,
not what the description sounds like.

A RESEARCH OBSERVATION IS NOT A DESIGN HYPOTHESIS
-------------------------------------------------
There is deliberately NO field saying "this supports design edge X". A design
logic model says "Goal A is intended to contribute to Outcome B"; a research
observation says "Study S measured relationship R between configuration A and
outcome B under population/context C". The second may later be offered as
evidence for or against the first, by something that weighs it. It does not
become it here, and this schema gives no way to write that it does.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - environment problem, not a data problem
    print("observation_lib needs PyYAML (pip install -r requirements-docs.txt)",
          file=sys.stderr)
    raise

WIKI_ROOT = Path(__file__).parent.parent
OBS_DIR = WIKI_ROOT / "observations"

SCHEMA_VERSION = 1

# ---------------------------------------------------------------- vocabularies
#
# Closed where a closed set is defensible and the cost of a wrong value is a
# silently mis-weighted study; open (free text) everywhere the user's own
# language carries information a category would throw away. Population,
# context and intervention are open ON PURPOSE — a closed demographic
# ontology would force "newly arrived migrant students aged 11-19 in nine
# north-east Italian secondary schools" into a box that loses the study.

DESIGN_FAMILIES = {
    "randomized-controlled-trial", "quasi-experimental", "observational",
    "longitudinal", "qualitative", "mixed-methods", "meta-analysis",
    "systematic-review", "simulation", "other",
}

MEASURE_TYPES = {
    "cohens_d", "hedges_g", "odds_ratio", "risk_ratio", "correlation",
    "mean_difference", "standardized_mean_difference", "regression_coefficient",
    "probability", "count", "qualitative", "other",
    # Added beyond the commissioning list: partial eta squared is the effect
    # size an ANOVA actually prints, and the first fixture that needed it
    # (Frolli et al. 2023, partial η² = 0.827) would otherwise have been
    # filed under `other` — which is where a value goes to stop being
    # comparable with anything.
    "eta_squared", "partial_eta_squared",
}

DIRECTIONS = {"higher-is-better", "lower-is-better", "contextual"}

# The subset of MEASURE_TYPES that quantify a RELATIONSHIP rather than
# describe a sample. The distinction matters for exactly one rule below, and
# the first fixture to need it was a SILL mean of 3.09 sitting beside
# `effect_size: unreported` — both true at once, because a mean is not an
# effect. Conflating the two would have forced the author to either delete a
# real number or claim an effect size the paper never printed.
EFFECT_MEASURE_TYPES = {
    "cohens_d", "hedges_g", "odds_ratio", "risk_ratio", "correlation",
    "mean_difference", "standardized_mean_difference", "regression_coefficient",
    "eta_squared", "partial_eta_squared",
}

# The Learning Design Spec separates a learner capability from a valued
# outcome and uses a logic model for the hypothesised link between them. A
# study's dependent variable is not automatically a learner competency —
# "training completion -> workplace performance" measures neither end as a
# capability. `other` and `ambiguous` exist so the classification can decline.
OUTCOME_ROLES = {
    "capability-evidence",    # performance evidence of a learner competency
    "proximal-outcome",       # immediate learning outcome
    "intermediate-outcome",
    "distal-outcome",
    "organizational-outcome", # institution, employer, community
    "learner-characteristic", # a trait/state measured about the learner, not a capability
    "other",
}

# How the role above was arrived at. `inferred` is honest and useful;
# silently presenting an inference as the source's own framing is not.
ROLE_BASIS = {"stated", "inferred", "ambiguous"}

# Who defines, values, measures or is affected by an outcome — recorded ONLY
# where the source identifies them. A researcher measuring graduation does not
# establish that a learner, an employer or a government values graduation, and
# there is no default value for this field for exactly that reason.
ACTORS = {"learner", "teacher", "institution", "employer", "community",
          "government", "researcher", "other"}

OBSERVABILITY_STATES = {"observed", "partial", "unreported"}

# Kept separate from `flagged`-style findings: what an extraction was, and
# whether anybody has checked it, must stay answerable for every record so a
# published finding is never confusable with runtime learner data, a synthetic
# learner, or a relationship an LLM proposed.
SOURCE_TYPES = {"research", "runtime-learner-data", "synthetic-simulation",
                "llm-proposed", "platform-experiment"}
VERIFICATION_STATES = {"unverified", "machine-checked", "human-reviewed"}

COMPARISON_KINDS = {
    "between-groups",          # a separate group of people
    "within-subject-baseline", # the same people, earlier
    "historical",              # a different cohort, earlier
    "none",                    # explicitly no counterfactual — recorded, never omitted
    "other",
}

TIME_UNITS = {"minutes", "hours", "days", "weeks", "months", "years", "sessions", "items"}

KEY_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ObsError(Exception):
    """A schema violation, with the file and path already in the message."""


# ------------------------------------------------------------------- helpers

def _err(issues: list, where: str, msg: str) -> None:
    issues.append(f"{where}: {msg}")


def _check_enum(issues, where, value, allowed, field):
    if value is None:
        return
    if value not in allowed:
        _err(issues, where, f"{field} is {value!r}; expected one of "
                            f"{', '.join(sorted(allowed))}")


def _check_str(issues, where, value, field, required=False):
    if value is None or value == "":
        if required:
            _err(issues, where, f"{field} is required")
        return
    if not isinstance(value, str):
        _err(issues, where, f"{field} must be a string, got {type(value).__name__}")


def _anchor_targets(anchors, issues, where):
    """Wiki concept anchors are bundle-relative page paths without the .md.

    Source language is preserved alongside them and is never replaced by
    them: the point is `human concept anchors + raw source-described
    variables`, not ontology conformity. An anchor that does not resolve is
    an error, because an anchor nobody can follow is worse than none."""
    for a in anchors or []:
        if not isinstance(a, str):
            _err(issues, where, f"anchor {a!r} must be a string like 'principles/game-based-learning'")
            continue
        if not (WIKI_ROOT / f"{a}.md").is_file():
            _err(issues, where, f"anchor {a!r} does not resolve to a page on disk")


# -------------------------------------------------------------- the validator

def validate_record(rec: dict, key: str, claim_index: dict | None = None) -> list:
    """Return a list of human-readable problems. Empty list means valid.

    Pure apart from the two filesystem lookups (`_anchor_targets` and the
    `appears_in` resolution), which is what makes the decision logic testable
    offline the way `resolve_citation_metadata.decide()` is."""
    issues: list = []
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]

    version = rec.get("schema_version")
    if version != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {version!r}; this reader understands {SCHEMA_VERSION}")

    # ---- study
    study = rec.get("study")
    if not isinstance(study, dict):
        _err(issues, key, "study: block is required")
        study = {}
    if study.get("key") != key:
        _err(issues, f"{key}.study", f"key is {study.get('key')!r} but the filename says {key!r}")
    if study.get("key") and not KEY_RE.match(str(study["key"])):
        _err(issues, f"{key}.study", "key must be lowercase-hyphenated (the author-year citation key)")
    _check_str(issues, f"{key}.study", study.get("citation"), "citation", required=True)
    # doi: absent means not established; an explicit null means a human
    # established that none is registered. Both are legal; a non-string
    # non-null is not.
    if "doi" in study and study["doi"] is not None and not isinstance(study["doi"], str):
        _err(issues, f"{key}.study", "doi must be a string or null (null = established that none exists)")

    design = study.get("design") or {}
    if not isinstance(design, dict):
        _err(issues, f"{key}.study", "design must be a mapping")
        design = {}
    if not design.get("family"):
        _err(issues, f"{key}.study.design", "family is required — never infer a stronger "
                                            "design than the source states")
    _check_enum(issues, f"{key}.study.design", design.get("family"), DESIGN_FAMILIES, "family")
    _check_str(issues, f"{key}.study.design", design.get("design_detail"), "design_detail")

    # ---- provenance
    prov = rec.get("provenance")
    if not isinstance(prov, dict):
        _err(issues, key, "provenance: block is required — a research-derived record must "
                          "stay distinguishable from runtime, synthetic and LLM-proposed data")
        prov = {}
    _check_enum(issues, f"{key}.provenance", prov.get("source_type"), SOURCE_TYPES, "source_type")
    if not prov.get("source_type"):
        _err(issues, f"{key}.provenance", "source_type is required")
    _check_enum(issues, f"{key}.provenance", prov.get("verification"), VERIFICATION_STATES, "verification")
    for f in ("extracted_by", "extraction_method"):
        _check_str(issues, f"{key}.provenance", prov.get(f), f, required=True)
    # YAML resolves an unquoted 2026-09-07 to a datetime.date, and quoting it
    # is the kind of detail an author gets wrong once per file. Accept both
    # spellings rather than making the schema depend on a quoting convention.
    at = prov.get("extracted_at")
    if at is None or at == "":
        _err(issues, f"{key}.provenance", "extracted_at is required")
    elif not isinstance(at, (str, date)):
        _err(issues, f"{key}.provenance", "extracted_at must be a date or an ISO date string")
    # Same rule as a page's `verified:` and as authorities.ndjson: a machine
    # may not certify its own extraction.
    if prov.get("verification") == "human-reviewed":
        by = str(prov.get("verified_by") or "")
        if not by.startswith("human:"):
            _err(issues, f"{key}.provenance",
                 "verification is 'human-reviewed' but verified_by is not a human:<id> — "
                 "an agent must never mark its own extraction reviewed")

    # ---- appears_in
    appears = rec.get("appears_in") or []
    if not isinstance(appears, list) or not appears:
        _err(issues, key, "appears_in: at least one {claim, anchor} is required — an "
                          "observation nothing cites is unreachable")
        appears = []
    for i, ref in enumerate(appears):
        where = f"{key}.appears_in[{i}]"
        if not isinstance(ref, dict):
            _err(issues, where, "must be a mapping with claim and anchor")
            continue
        slug, anchor = ref.get("claim"), ref.get("anchor")
        _check_str(issues, where, slug, "claim", required=True)
        _check_str(issues, where, anchor, "anchor", required=True)
        if claim_index is not None and slug:
            anchors = claim_index.get(slug)
            if anchors is None:
                _err(issues, where, f"claims/{slug}.md does not exist")
            elif anchor and anchor not in anchors:
                _err(issues, where,
                     f"claims/{slug}.md has no '### ' evidence heading with anchor {anchor!r} "
                     f"(it has: {', '.join(sorted(anchors)) or 'none'})")

    # ---- population / context: open-world, so only shape is checked
    for block in ("population", "context", "intervention"):
        val = rec.get(block)
        if val is not None and not isinstance(val, dict):
            _err(issues, key, f"{block} must be a mapping")
    pop = rec.get("population") or {}
    if "n" in pop and pop["n"] is not None and not isinstance(pop["n"], int):
        _err(issues, f"{key}.population", "n must be an integer or absent")

    inter = rec.get("intervention") or {}
    for i, el in enumerate(inter.get("elements") or []):
        where = f"{key}.intervention.elements[{i}]"
        if not isinstance(el, dict):
            _err(issues, where, "must be a mapping with at least `term`")
            continue
        _check_str(issues, where, el.get("term"), "term", required=True)
        _anchor_targets(el.get("anchors"), issues, where)

    # ---- comparisons
    comparisons = rec.get("comparisons") or []
    comp_ids = set()
    if not isinstance(comparisons, list):
        _err(issues, key, "comparisons must be a list")
        comparisons = []
    for i, comp in enumerate(comparisons):
        where = f"{key}.comparisons[{i}]"
        if not isinstance(comp, dict):
            _err(issues, where, "must be a mapping")
            continue
        cid = comp.get("id")
        _check_str(issues, where, cid, "id", required=True)
        if cid in comp_ids:
            _err(issues, where, f"duplicate comparison id {cid!r}")
        comp_ids.add(cid)
        _check_enum(issues, where, comp.get("kind"), COMPARISON_KINDS, "kind")
        if not comp.get("kind"):
            _err(issues, where, "kind is required — 'none' is a value, not an omission")
        _check_str(issues, where, comp.get("description"), "description", required=True)
        for j, el in enumerate(comp.get("elements") or []):
            w2 = f"{where}.elements[{j}]"
            if not isinstance(el, dict):
                _err(issues, w2, "must be a mapping with at least `term`")
                continue
            _check_str(issues, w2, el.get("term"), "term", required=True)
            _anchor_targets(el.get("anchors"), issues, w2)

    # ---- observations
    obs = rec.get("observations")
    if not isinstance(obs, list) or not obs:
        _err(issues, key, "observations: at least one is required")
        obs = []
    seen_ids = set()
    for i, o in enumerate(obs):
        issues.extend(_validate_observation(o, key, i, comp_ids, seen_ids))
    return issues


def _validate_observation(o: dict, key: str, i: int, comp_ids: set, seen_ids: set) -> list:
    issues: list = []
    where = f"{key}.observations[{i}]"
    if not isinstance(o, dict):
        return [f"{where}: must be a mapping"]
    oid = o.get("id")
    _check_str(issues, where, oid, "id", required=True)
    if oid:
        where = f"{key}/{oid}"
        if oid in seen_ids:
            _err(issues, where, "duplicate observation id within this study")
        seen_ids.add(oid)

    # ---- outcome
    out = o.get("outcome")
    if not isinstance(out, dict):
        _err(issues, where, "outcome: block is required")
        out = {}
    _check_str(issues, where, out.get("construct"), "outcome.construct", required=True)
    # The source's own words survive whatever classification is applied on top.
    _check_str(issues, where, out.get("source_language"), "outcome.source_language", required=True)
    _check_str(issues, where, out.get("measure"), "outcome.measure")
    _check_enum(issues, where, out.get("direction"), DIRECTIONS, "outcome.direction")
    _check_enum(issues, where, out.get("role"), OUTCOME_ROLES, "outcome.role")
    _check_enum(issues, where, out.get("role_basis"), ROLE_BASIS, "outcome.role_basis")
    if out.get("role") and not out.get("role_basis"):
        _err(issues, where, "outcome.role is set but role_basis is not — say whether the "
                            "source stated this classification or you inferred it")
    for j, v in enumerate(out.get("valued_by") or []):
        w2 = f"{where}.outcome.valued_by[{j}]"
        if not isinstance(v, dict):
            _err(issues, w2, "must be a mapping with actor and basis")
            continue
        _check_enum(issues, w2, v.get("actor"), ACTORS, "actor")
        # No inferring a stakeholder's values from the fact that a study
        # measured something. If the source does not say who values it, the
        # list stays empty.
        _check_str(issues, w2, v.get("basis"), "basis", required=True)
    _anchor_targets(out.get("anchors"), issues, f"{where}.outcome")

    # ---- time
    t = o.get("time")
    if not isinstance(t, dict):
        _err(issues, where, "time: block is required — an immediate effect and a "
                            "three-month effect are different observations")
        t = {}
    _check_str(issues, where, t.get("label"), "time.label", required=True)
    off = t.get("offset")
    if off is not None:
        if not isinstance(off, dict):
            _err(issues, where, "time.offset must be a mapping {value, unit, from}")
        else:
            if not isinstance(off.get("value"), (int, float)):
                _err(issues, where, "time.offset.value must be a number")
            _check_enum(issues, where, off.get("unit"), TIME_UNITS, "time.offset.unit")
            _check_str(issues, where, off.get("from"), "time.offset.from", required=True)

    # ---- result
    r = o.get("result")
    if not isinstance(r, dict):
        _err(issues, where, "result: block is required")
        r = {}
    mt = r.get("measure_type")
    _check_enum(issues, where, mt, MEASURE_TYPES, "result.measure_type")
    if not mt:
        _err(issues, where, "result.measure_type is required — it is the ONLY required "
                            "field of a result, so a study reporting no effect size is "
                            "still representable")
    if mt == "qualitative":
        _check_str(issues, where, r.get("finding"), "result.finding", required=True)
        _check_enum(issues, where, r.get("perspective"),
                    {"participant", "researcher", "mixed"}, "result.perspective")
        if r.get("estimate") is not None:
            _err(issues, where, "a qualitative result must not carry an `estimate` — "
                                "reducing a qualitative finding to a number invents one")
    for f in ("estimate", "ci_lower", "ci_upper", "standard_error"):
        v = r.get(f)
        if v is not None and not isinstance(v, (int, float)):
            _err(issues, where, f"result.{f} must be a number or absent (got {v!r}); "
                                f"a p-value written as '<.001' belongs in p_value, "
                                f"which is free text")
    if (r.get("ci_lower") is None) != (r.get("ci_upper") is None):
        _err(issues, where, "result.ci_lower and result.ci_upper must be given together")

    # ---- comparison
    cref = o.get("comparison_ref")
    if cref is None:
        _err(issues, where, "comparison_ref is required — name a comparison, including "
                            "the one whose kind is 'none'")
    elif cref not in comp_ids:
        _err(issues, where, f"comparison_ref {cref!r} names no entry in this study's "
                            f"comparisons ({', '.join(sorted(comp_ids)) or 'none defined'})")

    # ---- moderators
    mods = o.get("moderators") or {}
    if not isinstance(mods, dict):
        _err(issues, where, "moderators must be a mapping with `reported` and/or `candidate`")
        mods = {}
    for j, m in enumerate(mods.get("reported") or []):
        w2 = f"{where}.moderators.reported[{j}]"
        if not isinstance(m, dict):
            _err(issues, w2, "must be a mapping with variable and relationship")
            continue
        _check_str(issues, w2, m.get("variable"), "variable", required=True)
        _check_str(issues, w2, m.get("relationship"), "relationship", required=True)
        # `reported` means the study said it. A plausible explanation belongs
        # in `candidate`, where nothing downstream will read it as a finding.
        _check_str(issues, w2, m.get("source_quote"), "source_quote", required=True)

    # ---- observability
    obsv = o.get("observability")
    if not isinstance(obsv, dict):
        _err(issues, where, "observability: block is required — absence of a detail must "
                            "be sayable, so it is not read as absence of an effect")
        obsv = {}
    for f in ("population_detail", "implementation_detail", "outcome_timing", "effect_size"):
        if f not in obsv:
            _err(issues, where, f"observability.{f} is required")
        _check_enum(issues, where, obsv.get(f), OBSERVABILITY_STATES, f"observability.{f}")
    # The one cross-field rule worth enforcing: an effect ESTIMATE and "the
    # effect size was not reported" cannot both be true. Scoped to
    # EFFECT_MEASURE_TYPES so a descriptive statistic — a mean, a count, a
    # proportion — can sit beside an honest `unreported` without a fight.
    if (obsv.get("effect_size") == "unreported"
            and mt in EFFECT_MEASURE_TYPES
            and r.get("estimate") is not None):
        _err(issues, where, "observability.effect_size says 'unreported' but result.estimate "
                            "carries a number")

    _check_str(issues, where, o.get("source_quote"), "source_quote", required=True)
    return issues


# ------------------------------------------------------------------- loading

EVIDENCE_HEADING_RE = re.compile(r"^### (.+)$", re.M)


def claim_evidence_anchors() -> dict:
    """{claim-slug: {anchor-slug, ...}} from every claim page's `## Evidence`.

    The anchor slugs are what `## Subclaims` links to and what `sources[].id`
    carries, so this is the join `appears_in` has to resolve against."""
    sys.path.insert(0, str(Path(__file__).parent))
    import okf_lib as ok
    index = {}
    for path in sorted((WIKI_ROOT / "claims").glob("*.md")):
        if path.stem == "index":
            continue
        body = ok.split_frontmatter(path.read_text(encoding="utf-8"))[1]
        section = ok.get_section(body, "Evidence") or ""
        index[path.stem] = {ok.slugify(h.group(1).strip())
                            for h in EVIDENCE_HEADING_RE.finditer(section)}
    return index


def load_all(directory: Path | None = None) -> tuple[dict, list]:
    """({study-key: record}, [parse errors]). A file that does not parse is
    reported rather than raised, so one bad file does not hide the rest."""
    directory = directory or OBS_DIR
    records, errors = {}, []
    if not directory.is_dir():
        return records, errors
    for path in sorted(directory.glob("*.yaml")):
        try:
            rec = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"{path.name}: not valid YAML — {e}")
            continue
        records[path.stem] = rec
    return records, errors


def validate_all(directory: Path | None = None) -> list:
    records, issues = load_all(directory)
    claim_index = claim_evidence_anchors()
    for key, rec in records.items():
        issues.extend(validate_record(rec, key, claim_index))
    return issues


def parse_evidence_for_stub(evidence_section: str) -> list:
    """[(anchor-slug, citation, doi-or-None), ...] from a claim's `## Evidence`.

    Reuses okf_lib's own parser rather than a second one, so a stub's anchor is
    by construction the anchor `appears_in` has to match."""
    sys.path.insert(0, str(Path(__file__).parent))
    import okf_lib as ok
    out = []
    for src in ok.parse_evidence_sources(evidence_section):
        res = src.get("resource") or ""
        m = re.search(r"doi\.org/(10\.[^\s)]+)", res)
        out.append((src["id"], ascii_key(src["id"]),
                    src.get("title") or src["id"], m.group(1) if m else None))
    return out


def ascii_key(anchor: str) -> str:
    """A study key an author can type, from an evidence anchor that may not be.

    Evidence headings carry the author's name as printed, so anchors like
    `peskova-2026` arrive spelled `pe\u0161kov\u00e1-2026`. CLAUDE.md is explicit that a
    non-ASCII id is an NFC/NFD normalisation trap for a repo that resolves by
    string equality, and untypeable besides — the same reasoning that moved
    Gagne's page to an ASCII slug. The diacritics survive in `citation`, where
    they belong."""
    folded = unicodedata.normalize("NFKD", anchor)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    folded = re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")
    return folded or anchor
