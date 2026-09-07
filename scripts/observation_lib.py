#!/usr/bin/env python3
"""
observation_lib.py — the structured record of what a study actually did.

A claim page argues something; an observation file records the configuration
that argument rests on. `d = .78` is not a weight between two concepts, it is
one measurement of one configuration on one population against one comparison
at one point in time.

THREE LEVELS, NOT TWO (schema_version 2)
----------------------------------------
v1 had two: a `study` whose population/context/intervention were assumed
SINGULAR, and the observations under it. That middle assumption is a
primary-study assumption, and it broke the moment a meta-analysis and a
three-arm trial were put through it. So the levels are now:

  study          the SOURCE. What the report is, and by what method it produced
                 results. `synthesis:` appears iff it pools other people's work.
  evidence_base  what the results are ABOUT: who or what was counted, in what
                 population and context, and the ARMS the source contrasts.
  observations   the individual results, each naming one comparison of arms,
                 at one time, on one outcome, with its own analysed sample.

The generalisation that makes one schema fit both shapes is **arms +
comparisons**. A three-arm trial's "unenhanced elaboration vs baseline" and a
meta-analysis's "spaced online education vs massed online education" are the
same object — a contrast between two named configurations. The synthesis just
pools that contrast across studies instead of measuring it once. Nothing about
a meta-analysis needed a parallel set of fields; it needed the middle layer to
stop assuming there was exactly one group of people.

THE GOVERNING RULE
------------------
Put information at the LOWEST LEVEL AT WHICH IT ACTUALLY VARIES, and preserve
observations at the GRAIN AT WHICH THE SOURCE ACTUALLY REPORTS THEM.

That one rule explains every placement here, and it is also what settled the
two questions this schema got wrong first time round:

  * total corpus N varies per study, so it sits on `evidence_base`; analysed N
    varies per result, so it sits on the observation;
  * `k` varies per pooled estimate (9 for knowledge, 2 for surgical skills,
    from one corpus of 23), so it sits on the result;
  * arms and comparisons vary per contrast rather than per result or per
    study, so they sit between the two;
  * an arm has no fixed `role`, because whether it is the intervention or the
    comparator varies BY COMPARISON — see `comparisons` below;
  * and a pooled estimate over heterogeneous comparators stays ONE
    observation, because that is the grain the source reports, with the
    heterogeneity recorded structurally rather than normalised into effects
    nobody measured.

EVERY COUNT CARRIES ITS UNIT
----------------------------
The corpus had already proved this necessary before either fixture was
written. Its evidence entries carry `n=18`, `n=30 studies`, `n=66 articles`,
`n=N/A` and `n=large (aggregated)` — one field doing four jobs, so nothing can
read it. Here a count is `{value, unit}` and `unit` is required: 23 studies and
3371 participants are two different facts about one synthesis, and both are
recorded.

WHY NOT IN THE CLAIM'S FRONTMATTER
----------------------------------
`sources[]` is DERIVED: `sync_evidence_codes.py --apply` rebuilds it from the
body's `## Evidence` through `okf_lib.dump_frontmatter`, which emits exactly
id/resource/title/author/q/i/n — so anything nested there dies on the next run
of a script already in the unattended batch chain. `check_source_entry_keys`
also holds a closed key set there on purpose. And a study is cited by many
claims, so a per-claim copy is the drift shape this repo has lost weeks to.

ABSENCE IS NOT A VERDICT
------------------------
An omitted field means "not established". `observability.<field>: unreported`
means "somebody read the source and it does not say". And
`study.synthesis.attempted_but_precluded` means a third thing again — the
authors TRIED an analysis and could not complete it, which is a finding about
the evidence base rather than a silence. Martinengo et al. attempted subgroup
analyses and publication-bias assessment and were precluded by both the number
of studies and their heterogeneity; recording that as `unreported` would lose
the reason and recording it as absent would lose the attempt.

A RESEARCH OBSERVATION IS NOT A DESIGN HYPOTHESIS
-------------------------------------------------
There is deliberately NO field saying "this supports design edge X". A design
logic model says "Goal A is intended to contribute to Outcome B"; a record here
says "Study S observed relationship R between configuration A and outcome B
under population/context C". The second may later be offered as evidence for or
against the first, by something that weighs it. It does not become it here.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - environment problem, not data
    print("observation_lib needs PyYAML (pip install -r requirements-docs.txt)",
          file=sys.stderr)
    raise

WIKI_ROOT = Path(__file__).parent.parent
OBS_DIR = WIKI_ROOT / "observations"

SCHEMA_VERSION = 2

# ---------------------------------------------------------------- vocabularies
#
# Closed where a wrong value silently mis-weights a study; open (free text)
# wherever the author's own language carries information a category would throw
# away. Population, context, arm descriptions and all prose stay open ON
# PURPOSE — a closed demographic ontology would force "newly arrived migrant
# students aged 11-19 across nine north-east Italian secondary schools" into a
# box that loses the study.

DESIGN_FAMILIES = {
    "randomized-controlled-trial",
    # Named separately because the unit randomised is not the unit analysed,
    # and that changes what every estimate in the study means. Requires
    # `evidence_base.allocation` — see CLUSTER_ALLOCATION below.
    "cluster-randomized-controlled-trial",
    "quasi-experimental", "observational",
    "longitudinal", "qualitative", "mixed-methods", "meta-analysis",
    "systematic-review", "simulation", "other",
}

# Families whose results are ABOUT other studies rather than about people the
# authors measured. These require `study.synthesis` and an evidence_base
# counted in studies.
SYNTHESIS_FAMILIES = {"meta-analysis", "systematic-review"}

MEASURE_TYPES = {
    "cohens_d", "hedges_g", "odds_ratio", "risk_ratio", "correlation",
    "mean_difference", "standardized_mean_difference", "regression_coefficient",
    "probability", "count", "qualitative", "other",
    # Beyond the commissioning list: partial eta squared is the effect size an
    # ANOVA actually prints, and `other` is where a value stops being
    # comparable with anything.
    "eta_squared", "partial_eta_squared",
}

# The subset that quantifies a RELATIONSHIP rather than describing a sample.
# A SILL mean of 3.09 beside `effect_size: unreported` is two true statements;
# an odds ratio beside it is a contradiction.
EFFECT_MEASURE_TYPES = {
    "cohens_d", "hedges_g", "odds_ratio", "risk_ratio", "correlation",
    "mean_difference", "standardized_mean_difference", "regression_coefficient",
    "eta_squared", "partial_eta_squared",
}

# What a count counts. Required on every {value, unit} pair, because the wiki's
# own `n=` field already proved that a bare number is unreadable.
COUNT_UNITS = {
    "participants", "studies", "reports", "classes", "schools", "sites",
    "effect-sizes", "comparisons", "pairs", "items", "sessions", "other",
}

DIRECTIONS = {"higher-is-better", "lower-is-better", "contextual"}

# The Learning Design Spec separates a learner capability from a valued
# outcome. A dependent variable is not automatically a competency —
# "training completion -> workplace performance" measures neither end as one.
OUTCOME_ROLES = {
    "capability-evidence", "proximal-outcome", "intermediate-outcome",
    "distal-outcome", "organizational-outcome", "learner-characteristic",
    "other",
}
ROLE_BASIS = {"stated", "inferred", "ambiguous"}

# Recorded ONLY where the source identifies them. A researcher measuring
# graduation does not establish that anybody values graduation, so this field
# has no default.
ACTORS = {"learner", "teacher", "institution", "employer", "community",
          "government", "researcher", "other"}

OBSERVABILITY_STATES = {"observed", "partial", "unreported"}

SOURCE_TYPES = {"research", "runtime-learner-data", "synthetic-simulation",
                "llm-proposed", "platform-experiment"}
VERIFICATION_STATES = {"unverified", "machine-checked", "human-reviewed"}

# An arm carries NO `role`. It was there in the first draft and removed on
# evidence: nothing read it, and it is not a property of an arm. In the
# three-arm fixture `unenhanced-elaboration` was declared `role: intervention`
# and is the REFERENCE side of `enhanced-vs-unenhanced` — so whether an arm is
# the intervention or the comparator varies by comparison, which is exactly
# where `index_arm`/`reference_arm` already say it. A type tag on the arm
# duplicates that and contradicts it.
#
# Nor does an arm need an epistemic type to mark a synthesis: the containing
# source already says `design.family: meta-analysis`, and the arm's own
# `size: {value: 17, unit: studies}` already says it is 17 studies rather than
# 17 people. An arm is a named configuration; what it means is read from where
# it sits.

COMPARISON_KINDS = {
    "between-groups",          # separate people, or separate corpus strata
    "within-subject-baseline", # the same people, earlier
    "historical",
    "none",                    # explicitly no counterfactual — recorded, never omitted
    "other",
}

TIME_UNITS = {"minutes", "hours", "days", "weeks", "months", "years",
              "sessions", "items", "readings"}

HETEROGENEITY_STATISTICS = {"I2", "tau2", "Q", "H", "other"}

# Deliberately NOT folded into `heterogeneity`. Both answer "how much does this
# vary across the units it pools over", and they are different questions: I2 is
# between-STUDY heterogeneity of effects in a synthesis; an ICC is the
# within-study correlation of observations sharing a cluster. Merging them
# would be exactly the normalise-into-one-shape error this schema exists to
# avoid, and a consumer pooling an ICC with an I2 would be pooling nonsense.
CLUSTERING_STATISTICS = {"ICC", "design-effect", "other"}

# Power is recorded where it is reported and never computed here. Rosario et
# al. report a POST-HOC power of 0.44 for their group-by-time interaction —
# which is a fact about that one test, not about the study, so it rides on the
# result. `kind` is required because a-priori and post-hoc power are different
# claims and conflating them flatters an underpowered study.
POWER_KINDS = {"a-priori", "post-hoc", "sensitivity"}

KEY_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# ------------------------------------------------------------------- helpers

def _err(issues: list, where: str, msg: str) -> None:
    issues.append(f"{where}: {msg}")


def _enum(issues, where, value, allowed, field, required=False):
    if value is None:
        if required:
            _err(issues, where, f"{field} is required")
        return
    if value not in allowed:
        _err(issues, where, f"{field} is {value!r}; expected one of {', '.join(sorted(allowed))}")


def _str(issues, where, value, field, required=False):
    if value is None or value == "":
        if required:
            _err(issues, where, f"{field} is required")
        return
    if not isinstance(value, str):
        _err(issues, where, f"{field} must be a string, got {type(value).__name__}")


def _count(issues, where, value, field, required=False):
    """A {value, unit} pair. The unit is not optional: the wiki's own `n=`
    field already demonstrated what a bare number costs — `n=30 studies`,
    `n=66 articles` and `n=18` sit in one column and nothing can read it."""
    if value is None:
        if required:
            _err(issues, where, f"{field} is required")
        return
    if not isinstance(value, dict):
        _err(issues, where, f"{field} must be a mapping {{value, unit}}")
        return
    if not isinstance(value.get("value"), (int, float)):
        _err(issues, where, f"{field}.value must be a number")
    _enum(issues, where, value.get("unit"), COUNT_UNITS, f"{field}.unit", required=True)


def arms_named(value) -> list:
    """An arm reference is a string or a list of strings, always read as a list.

    Authored either way for ergonomics — one arm is the overwhelmingly common
    case and should not need brackets — and normalised here so that every
    consumer sees one shape. Same call the repo makes about unescaping
    Crossref's HTML entities once, at the boundary."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [v for v in value if isinstance(v, str)]
    return []


def _anchors(anchors, issues, where):
    """Wiki concept anchors are bundle-relative page paths without the .md.

    Source language is preserved alongside them and never replaced by them:
    the point is `human concept anchors + raw source-described variables`, not
    ontology conformity. An anchor nobody can follow is worse than none."""
    for a in anchors or []:
        if not isinstance(a, str):
            _err(issues, where, f"anchor {a!r} must be a string like 'principles/game-based-learning'")
        elif not (WIKI_ROOT / f"{a}.md").is_file():
            _err(issues, where, f"anchor {a!r} does not resolve to a page on disk")


def _elements(elements, issues, where):
    for i, el in enumerate(elements or []):
        w = f"{where}.elements[{i}]"
        if not isinstance(el, dict):
            _err(issues, w, "must be a mapping with at least `term`")
            continue
        _str(issues, w, el.get("term"), "term", required=True)
        _anchors(el.get("anchors"), issues, w)


# -------------------------------------------------------------- the validator

def validate_record(rec: dict, key: str, claim_index: dict | None = None) -> list:
    """Return a list of human-readable problems. Empty list means valid."""
    issues: list = []
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]

    if rec.get("schema_version") != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {rec.get('schema_version')!r}; "
                          f"this reader understands {SCHEMA_VERSION}")

    family = _validate_study(rec, key, issues)
    _validate_provenance(rec, key, issues)
    _validate_appears_in(rec, key, issues, claim_index)
    arm_ids = _validate_evidence_base(rec, key, issues, family)
    comp_ids = _validate_comparisons(rec, key, issues, arm_ids)

    obs = rec.get("observations")
    if not isinstance(obs, list) or not obs:
        _err(issues, key, "observations: at least one is required")
        obs = []
    seen: set = set()
    for i, o in enumerate(obs):
        issues.extend(_validate_observation(o, key, i, comp_ids, seen, family))
    return issues


def _validate_study(rec, key, issues) -> str | None:
    study = rec.get("study")
    if not isinstance(study, dict):
        _err(issues, key, "study: block is required")
        return None
    where = f"{key}.study"
    if study.get("key") != key:
        _err(issues, where, f"key is {study.get('key')!r} but the filename says {key!r}")
    if study.get("key") and not KEY_RE.match(str(study["key"])):
        _err(issues, where, "key must be lowercase-hyphenated ASCII (the author-year citation key)")
    _str(issues, where, study.get("citation"), "citation", required=True)
    # doi: absent means not established; explicit null means a human
    # established none is registered. Both legal; a non-string non-null is not.
    if "doi" in study and study["doi"] is not None and not isinstance(study["doi"], str):
        _err(issues, where, "doi must be a string or null (null = established that none exists)")

    design = study.get("design") or {}
    if not isinstance(design, dict):
        _err(issues, where, "design must be a mapping")
        design = {}
    family = design.get("family")
    _enum(issues, f"{where}.design", family, DESIGN_FAMILIES, "family", required=True)
    _str(issues, f"{where}.design", design.get("design_detail"), "design_detail")

    synth = study.get("synthesis")
    if family in SYNTHESIS_FAMILIES:
        if not isinstance(synth, dict):
            _err(issues, where, f"design.family is {family!r} so `synthesis:` is required — "
                                f"the method by which results were pooled is the design")
        else:
            _validate_synthesis(synth, f"{where}.synthesis", issues)
    elif synth is not None:
        _err(issues, where, f"`synthesis:` is present but design.family is {family!r}; "
                            f"it belongs only to {' or '.join(sorted(SYNTHESIS_FAMILIES))}")
    return family


def _validate_synthesis(synth, where, issues):
    _str(issues, where, synth.get("model"), "model", required=True)
    _str(issues, where, synth.get("heterogeneity_statistic"), "heterogeneity_statistic")
    for f in ("quality_tool", "certainty_framework", "reporting_guideline"):
        _str(issues, where, synth.get(f), f)
    search = synth.get("search")
    if search is not None and not isinstance(search, dict):
        _err(issues, where, "search must be a mapping")
    # The third epistemic state, alongside absent and `unreported`: the authors
    # TRIED and could not. Losing the attempt loses a fact about the evidence
    # base, not about the reporting.
    for i, a in enumerate(synth.get("attempted_but_precluded") or []):
        w = f"{where}.attempted_but_precluded[{i}]"
        if not isinstance(a, dict):
            _err(issues, w, "must be a mapping with analysis and reason")
            continue
        _str(issues, w, a.get("analysis"), "analysis", required=True)
        _str(issues, w, a.get("reason"), "reason", required=True)


def _validate_provenance(rec, key, issues):
    prov = rec.get("provenance")
    where = f"{key}.provenance"
    if not isinstance(prov, dict):
        _err(issues, key, "provenance: block is required — a research-derived record must stay "
                          "distinguishable from runtime, synthetic and LLM-proposed data")
        return
    _enum(issues, where, prov.get("source_type"), SOURCE_TYPES, "source_type", required=True)
    _enum(issues, where, prov.get("verification"), VERIFICATION_STATES, "verification")
    for f in ("extracted_by", "extraction_method"):
        _str(issues, where, prov.get(f), f, required=True)
    at = prov.get("extracted_at")
    if at is None or at == "":
        _err(issues, where, "extracted_at is required")
    elif not isinstance(at, (str, date)):
        _err(issues, where, "extracted_at must be a date or an ISO date string")
    # Same rule as a page's `verified:` and as authorities.ndjson: a machine
    # may not certify its own extraction.
    if prov.get("verification") == "human-reviewed" \
            and not str(prov.get("verified_by") or "").startswith("human:"):
        _err(issues, where, "verification is 'human-reviewed' but verified_by is not a "
                            "human:<id> — an agent must never mark its own extraction reviewed")


def _validate_appears_in(rec, key, issues, claim_index):
    """Optional, and validated when present.

    v1 required it. That was backwards: the store is keyed by STUDY, and a
    structured record of a real study is valid evidence whether or not anyone
    has yet written an argument that appeals to it — requiring a claim first
    makes the evidence layer depend on the argument layer. The ratchet is
    kept where it belongs: a listed claim and anchor must still resolve, so a
    rename fails here rather than silently orphaning the record.
    `check_observations.py --summary` reports records nothing cites."""
    appears = rec.get("appears_in")
    if appears is None:
        return
    if not isinstance(appears, list):
        _err(issues, key, "appears_in must be a list (possibly empty)")
        return
    for i, ref in enumerate(appears):
        where = f"{key}.appears_in[{i}]"
        if not isinstance(ref, dict):
            _err(issues, where, "must be a mapping with claim and anchor")
            continue
        slug, anchor = ref.get("claim"), ref.get("anchor")
        _str(issues, where, slug, "claim", required=True)
        _str(issues, where, anchor, "anchor", required=True)
        if claim_index is not None and slug:
            anchors = claim_index.get(slug)
            if anchors is None:
                _err(issues, where, f"claims/{slug}.md does not exist")
            elif anchor and anchor not in anchors:
                _err(issues, where, f"claims/{slug}.md has no '### ' evidence heading with "
                                    f"anchor {anchor!r} (it has: "
                                    f"{', '.join(sorted(anchors)) or 'none'})")


def _validate_evidence_base(rec, key, issues, family) -> set:
    """What the results are ABOUT. Returns the set of arm ids."""
    eb = rec.get("evidence_base")
    where = f"{key}.evidence_base"
    if not isinstance(eb, dict):
        _err(issues, key, "evidence_base: block is required")
        return set()

    _enum(issues, where, eb.get("unit"), COUNT_UNITS, "unit", required=True)
    _count(issues, where, eb.get("size"), "size", required=True)
    # The size and the unit have to agree, or the record says two things.
    if isinstance(eb.get("size"), dict) and eb.get("unit") \
            and eb["size"].get("unit") not in (None, eb["unit"]):
        _err(issues, where, f"unit is {eb['unit']!r} but size.unit is "
                            f"{eb['size'].get('unit')!r}")
    # A synthesis is counted in studies (or reports). Counting it in
    # participants is the v1 mistake: 3371 participants is a real fact about
    # this synthesis and it is NOT the number of things it pooled.
    if family in SYNTHESIS_FAMILIES and eb.get("unit") not in ("studies", "reports", "effect-sizes"):
        _err(issues, where, f"design.family is {family!r} but evidence_base.unit is "
                            f"{eb.get('unit')!r} — a synthesis is counted in what it pooled; "
                            f"put the participant total in additional_sizes")
    # THE CLUSTER CASE. `size` is what was ANALYSED; `allocation` is what was
    # RANDOMISED. When they differ the study is clustered, every contrast is
    # estimated at the allocation level, and reading `size` as the effective
    # sample overstates precision — in the fixture, the group contrasts carry
    # df = 16 (20 classes minus 4 conditions) while 370 students were measured.
    alloc = eb.get("allocation")
    if alloc is not None:
        _count(issues, where, alloc, "allocation", required=True)
        if isinstance(alloc, dict) and alloc.get("unit") == eb.get("unit"):
            _err(issues, where, f"allocation.unit equals evidence_base.unit "
                                f"({eb.get('unit')!r}) — allocation records the unit "
                                f"RANDOMISED when it differs from the unit analysed; "
                                f"omit it when they are the same")
    if family == "cluster-randomized-controlled-trial" and alloc is None:
        _err(issues, where, "design.family is 'cluster-randomized-controlled-trial' but "
                            "evidence_base.allocation is absent — the unit randomised is "
                            "what makes it a cluster design and what every contrast is "
                            "estimated at")
    if alloc is not None and family not in ("cluster-randomized-controlled-trial",
                                            "quasi-experimental", "observational"):
        _err(issues, where, f"evidence_base.allocation is present but design.family is "
                            f"{family!r}; a differing allocation unit means the design is "
                            f"clustered and the family should say so")

    for i, s in enumerate(eb.get("additional_sizes") or []):
        w = f"{where}.additional_sizes[{i}]"
        _count(issues, w, s, "additional size", required=True)
        if isinstance(s, dict):
            _str(issues, w, s.get("note"), "note", required=True)

    for block in ("population", "context"):
        if eb.get(block) is not None and not isinstance(eb[block], dict):
            _err(issues, where, f"{block} must be a mapping")

    # How the base VARIES. A single sample has one population; a corpus of 23
    # studies has a distribution over populations, and flattening that to a
    # description loses the thing that makes pooling questionable.
    for i, v in enumerate(eb.get("variation") or []):
        w = f"{where}.variation[{i}]"
        if not isinstance(v, dict):
            _err(issues, w, "must be a mapping with dimension and distribution")
            continue
        _str(issues, w, v.get("dimension"), "dimension", required=True)
        _str(issues, w, v.get("distribution"), "distribution", required=True)

    arm_ids: set = set()
    arms = eb.get("arms")
    if arms is None:
        arms = []
    if not isinstance(arms, list):
        _err(issues, where, "arms must be a list (possibly empty)")
        arms = []
    for i, arm in enumerate(arms):
        w = f"{where}.arms[{i}]"
        if not isinstance(arm, dict):
            _err(issues, w, "must be a mapping")
            continue
        aid = arm.get("id")
        _str(issues, w, aid, "id", required=True)
        if aid in arm_ids:
            _err(issues, w, f"duplicate arm id {aid!r}")
        arm_ids.add(aid)
        if "role" in arm:
            _err(issues, w, "`role` was removed in schema 2: an arm's role varies by "
                            "comparison, and index_arm/reference_arm already carry it")
        _str(issues, w, arm.get("description"), "description", required=True)
        if arm.get("size") is not None:
            _count(issues, w, arm.get("size"), "size")
        # Symmetric with evidence_base: five classes AND ~92 students per arm
        # are two facts, and one `size` slot could only hold one of them.
        if arm.get("allocation") is not None:
            _count(issues, w, arm.get("allocation"), "allocation")
        _elements(arm.get("elements"), issues, w)
    return arm_ids


def _validate_comparisons(rec, key, issues, arm_ids) -> set:
    comparisons = rec.get("comparisons")
    if not isinstance(comparisons, list):
        _err(issues, key, "comparisons must be a list")
        return set()
    comp_ids: set = set()
    used: set = set()
    for i, comp in enumerate(comparisons):
        where = f"{key}.comparisons[{i}]"
        if not isinstance(comp, dict):
            _err(issues, where, "must be a mapping")
            continue
        cid = comp.get("id")
        _str(issues, where, cid, "id", required=True)
        if cid in comp_ids:
            _err(issues, where, f"duplicate comparison id {cid!r}")
        comp_ids.add(cid)
        kind = comp.get("kind")
        _enum(issues, where, kind, COMPARISON_KINDS, "kind", required=True)
        _str(issues, where, comp.get("description"), "description", required=True)
        # Not every contrast is pairwise. Rosario et al. use Helmert contrasts,
        # where H1 sets control against the MEAN of three treatment arms — the
        # arm lists already carry which arms are on which side, and this
        # carries the weighting, copied from the source. Absent for an
        # ordinary pairwise contrast, where the weights are implied.
        contrast = comp.get("contrast")
        if contrast is not None:
            if not isinstance(contrast, dict):
                _err(issues, where, "contrast must be a mapping")
            else:
                _str(issues, where, contrast.get("method"), "contrast.method", required=True)
                coeffs = contrast.get("coefficients")
                if coeffs is not None and not isinstance(coeffs, dict):
                    _err(issues, where, "contrast.coefficients must be a mapping of "
                                        "arm id -> weight, as the source prints it")
                for arm_id in (coeffs or {}):
                    if arm_id not in arm_ids:
                        _err(issues, where, f"contrast.coefficients names {arm_id!r}, "
                                            f"which is not an arm id")
        # Arms are what make a multi-arm design representable: three arms give
        # three pairwise contrasts, and each observation says which one it is.
        #
        # Either side may name MORE THAN ONE arm. That is the smallest
        # representation of a heterogeneous comparator, and it exists because
        # Martinengo et al. pool three studies of which two compared against
        # massed online education and one against no intervention at all. The
        # paper reports one estimate, so it stays one observation — but "the
        # comparator is two configurations" is part of the relational
        # structure and has to be readable without parsing prose.
        for field in ("index_arm", "reference_arm"):
            named = arms_named(comp.get(field))
            if not named:
                if kind not in ("none", "within-subject-baseline"):
                    _err(issues, where, f"{field} is required for kind {kind!r} — name the "
                                        f"arm(s) in evidence_base.arms this contrast is over")
            for arm in named:
                if arm not in arm_ids:
                    _err(issues, where, f"{field} names {arm!r}, which is not an id in "
                                        f"evidence_base.arms "
                                        f"({', '.join(sorted(arm_ids)) or 'none'})")
                used.add(arm)

    # An arm nothing contrasts is dead data, and this is the invariant `role`
    # was standing in for without enforcing. A within-subject comparison may
    # name its index arm — "this configuration against its own earlier state" —
    # which is how a single-group study's one arm gets used.
    for orphan in sorted(arm_ids - used):
        _err(issues, f"{key}.evidence_base.arms",
             f"arm {orphan!r} is named by no comparison — an arm nothing is "
             f"contrasted against or with cannot be reached from any observation")
    return comp_ids


def _validate_observation(o, key, i, comp_ids, seen, family) -> list:
    issues: list = []
    where = f"{key}.observations[{i}]"
    if not isinstance(o, dict):
        return [f"{where}: must be a mapping"]
    oid = o.get("id")
    _str(issues, where, oid, "id", required=True)
    if oid:
        where = f"{key}/{oid}"
        if oid in seen:
            _err(issues, where, "duplicate observation id within this study")
        seen.add(oid)

    # The analysed sample for THIS result, which is routinely not the study's.
    # Jeon & Lee's comprehension ANOVA is F(2,59) on 62 of the 67 randomised.
    if o.get("sample") is not None:
        _count(issues, where, o.get("sample"), "sample")

    out = o.get("outcome")
    if not isinstance(out, dict):
        _err(issues, where, "outcome: block is required")
        out = {}
    _str(issues, where, out.get("construct"), "outcome.construct", required=True)
    _str(issues, where, out.get("source_language"), "outcome.source_language", required=True)
    _str(issues, where, out.get("measure"), "outcome.measure")
    _enum(issues, where, out.get("direction"), DIRECTIONS, "outcome.direction")
    # Required, with `other` + `role_basis: ambiguous` as the way to DECLINE
    # rather than to guess — the classification is never forced, but silence
    # about it is not an option. Made required after an editing pass deleted
    # `outcome.role` from all 21 observations and the validator passed: an
    # optional field cannot tell "nobody classified this" from "a regex ate it".
    _enum(issues, where, out.get("role"), OUTCOME_ROLES, "outcome.role", required=True)
    _enum(issues, where, out.get("role_basis"), ROLE_BASIS, "outcome.role_basis",
          required=bool(out.get("role")))
    for j, v in enumerate(out.get("valued_by") or []):
        w = f"{where}.outcome.valued_by[{j}]"
        if not isinstance(v, dict):
            _err(issues, w, "must be a mapping with actor and basis")
            continue
        _enum(issues, w, v.get("actor"), ACTORS, "actor")
        _str(issues, w, v.get("basis"), "basis", required=True)
    _anchors(out.get("anchors"), issues, f"{where}.outcome")

    t = o.get("time")
    if not isinstance(t, dict):
        _err(issues, where, "time: block is required — an immediate effect and a "
                            "three-month effect are different observations")
        t = {}
    _str(issues, where, t.get("label"), "time.label", required=True)
    off = t.get("offset")
    if off is not None:
        if not isinstance(off, dict):
            _err(issues, where, "time.offset must be a mapping {value, unit, from}")
        else:
            if not isinstance(off.get("value"), (int, float)):
                _err(issues, where, "time.offset.value must be a number")
            _enum(issues, where, off.get("unit"), TIME_UNITS, "time.offset.unit")
            _str(issues, where, off.get("from"), "time.offset.from", required=True)

    issues.extend(_validate_result(o, where, family))

    cref = o.get("comparison_ref")
    if cref is None:
        _err(issues, where, "comparison_ref is required — name a comparison, including "
                            "the one whose kind is 'none'")
    elif cref not in comp_ids:
        _err(issues, where, f"comparison_ref {cref!r} names no entry in this study's "
                            f"comparisons ({', '.join(sorted(comp_ids)) or 'none defined'})")

    mods = o.get("moderators") or {}
    if not isinstance(mods, dict):
        _err(issues, where, "moderators must be a mapping with `reported` and/or `candidate`")
        mods = {}
    for j, m in enumerate(mods.get("reported") or []):
        w = f"{where}.moderators.reported[{j}]"
        if not isinstance(m, dict):
            _err(issues, w, "must be a mapping with variable and relationship")
            continue
        _str(issues, w, m.get("variable"), "variable", required=True)
        _str(issues, w, m.get("relationship"), "relationship", required=True)
        # `reported` asserts the study said it. A plausible explanation belongs
        # in `candidate`, where nothing downstream reads it as a finding.
        _str(issues, w, m.get("source_quote"), "source_quote", required=True)

    obsv = o.get("observability")
    if not isinstance(obsv, dict):
        _err(issues, where, "observability: block is required — absence of a detail must be "
                            "sayable, so it is not read as absence of an effect")
        obsv = {}
    for f in ("population_detail", "implementation_detail", "outcome_timing", "effect_size"):
        _enum(issues, where, obsv.get(f), OBSERVABILITY_STATES, f"observability.{f}", required=True)

    r = o.get("result") or {}
    if (obsv.get("effect_size") == "unreported"
            and r.get("measure_type") in EFFECT_MEASURE_TYPES
            and r.get("estimate") is not None):
        _err(issues, where, "observability.effect_size says 'unreported' but result.estimate "
                            "carries an effect estimate")

    _str(issues, where, o.get("source_quote"), "source_quote", required=True)
    return issues


def _validate_result(o, where, family) -> list:
    issues: list = []
    r = o.get("result")
    if not isinstance(r, dict):
        _err(issues, where, "result: block is required")
        return issues
    mt = r.get("measure_type")
    _enum(issues, where, mt, MEASURE_TYPES, "result.measure_type", required=True)

    if mt == "qualitative":
        _str(issues, where, r.get("finding"), "result.finding", required=True)
        _enum(issues, where, r.get("perspective"),
              {"participant", "researcher", "mixed"}, "result.perspective")
        if r.get("estimate") is not None:
            _err(issues, where, "a qualitative result must not carry an `estimate` — "
                                "reducing a qualitative finding to a number invents one")

    for f in ("estimate", "ci_lower", "ci_upper", "standard_error"):
        v = r.get(f)
        if v is not None and not isinstance(v, (int, float)):
            _err(issues, where, f"result.{f} must be a number or absent (got {v!r}); a p-value "
                                f"written as '<.001' belongs in p_value, which is free text")
    if (r.get("ci_lower") is None) != (r.get("ci_upper") is None):
        _err(issues, where, "result.ci_lower and result.ci_upper must be given together")

    # --- pooled-estimate fields. Each observation carries its OWN k: the
    # Martinengo knowledge estimate pools 9 studies and the surgical-skills
    # estimate pools 2, out of a corpus of 23. k on the study would be wrong
    # for every observation in it, which is the clearest single reason the
    # middle layer had to stop being one thing.
    if r.get("k") is not None:
        _count(issues, where, r.get("k"), "result.k")
    if family in SYNTHESIS_FAMILIES and mt in EFFECT_MEASURE_TYPES and r.get("k") is None:
        _err(issues, where, "a pooled effect from a synthesis must carry result.k — how many "
                            "studies THIS estimate rests on, which is rarely the whole corpus")

    het = r.get("heterogeneity")
    if het is not None:
        if not isinstance(het, dict):
            _err(issues, where, "result.heterogeneity must be a mapping")
        else:
            _enum(issues, where, het.get("statistic"), HETEROGENEITY_STATISTICS,
                  "result.heterogeneity.statistic", required=True)
            if not isinstance(het.get("value"), (int, float)):
                _err(issues, where, "result.heterogeneity.value must be a number")

    pi = r.get("prediction_interval")
    if pi is not None:
        if not isinstance(pi, dict):
            _err(issues, where, "result.prediction_interval must be a mapping {lower, upper}")
        else:
            for f in ("lower", "upper"):
                if not isinstance(pi.get(f), (int, float)):
                    _err(issues, where, f"result.prediction_interval.{f} must be a number")
            # A prediction interval is not a confidence interval and must not
            # be derived from one: the CI is about the mean effect, the PI
            # about the next study. Recording a computed PI as reported would
            # be the same act as converting a metric during ingestion.
            _str(issues, where, pi.get("source"), "result.prediction_interval.source",
                 required=True)

    for j, c in enumerate(r.get("clustering") or []):
        w = f"{where}.result.clustering[{j}]"
        if not isinstance(c, dict):
            _err(issues, w, "must be a mapping")
            continue
        _enum(issues, w, c.get("statistic"), CLUSTERING_STATISTICS, "statistic", required=True)
        # `level` is required because a three-level model reports more than one
        # ICC and an unlabelled 0.49 beside an unlabelled 0.11 is unreadable.
        _str(issues, w, c.get("level"), "level", required=True)
        if not isinstance(c.get("value"), (int, float)):
            _err(issues, w, "value must be a number")

    power = r.get("power")
    if power is not None:
        if not isinstance(power, dict):
            _err(issues, where, "result.power must be a mapping")
        else:
            if not isinstance(power.get("value"), (int, float)):
                _err(issues, where, "result.power.value must be a number")
            _enum(issues, where, power.get("kind"), POWER_KINDS, "result.power.kind",
                  required=True)
            _str(issues, where, power.get("test"), "result.power.test", required=True)

    cert = r.get("certainty")
    if cert is not None:
        if not isinstance(cert, dict):
            _err(issues, where, "result.certainty must be a mapping {rating, framework}")
        else:
            _str(issues, where, cert.get("rating"), "result.certainty.rating", required=True)
            _str(issues, where, cert.get("framework"), "result.certainty.framework", required=True)
    return issues


# ------------------------------------------------------------------- loading

EVIDENCE_HEADING_RE = re.compile(r"^### (.+)$", re.M)


def claim_evidence_anchors() -> dict:
    """{claim-slug: {anchor-slug, ...}} from every claim page's `## Evidence`."""
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
    directory = directory or OBS_DIR
    records, errors = {}, []
    if not directory.is_dir():
        return records, errors
    for path in sorted(directory.glob("*.yaml")):
        try:
            records[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"{path.name}: not valid YAML — {e}")
    return records, errors


def validate_all(directory: Path | None = None) -> list:
    records, issues = load_all(directory)
    claim_index = claim_evidence_anchors()
    for key, rec in records.items():
        issues.extend(validate_record(rec, key, claim_index))
    return issues


def parse_evidence_for_stub(evidence_section: str) -> list:
    """[(anchor, ascii-key, citation, doi-or-None), ...] from a `## Evidence`."""
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
    """A study key an author can type, from an anchor that may not be.

    Evidence headings carry names as printed, so anchors arrive spelled
    `pešková-2026`. CLAUDE.md is explicit that a non-ASCII id is an NFC/NFD
    normalisation trap for a repo resolving by string equality — the same
    reasoning that moved Gagne's page to an ASCII slug. Diacritics survive in
    `citation`, where they belong."""
    folded = unicodedata.normalize("NFKD", anchor)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    folded = re.sub(r"[^a-z0-9]+", "-", folded.lower()).strip("-")
    return folded or anchor
