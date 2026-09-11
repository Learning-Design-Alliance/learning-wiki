#!/usr/bin/env python3
"""
research_lib.py — the research layer: protocol, release, review.

The wiki's existing kinds record WHAT WE CURRENTLY BELIEVE. This layer records
WHERE THAT CAME FROM and how it can be interrogated:

    Protocol   the rules under which data could be collected and used at all
        v
    Release    one versioned, citable investigation: its question, datasets,
        v      analyses, artifacts, interpretation and limitations
    Evidence   what was actually observed  ->  observations/<study-key>.yaml
        v
    Claim      the proposition                ->  claims/<slug>.md
        ^
    Review     a structured contribution interrogating any of the above

THERE IS NO `evidence/` FOLDER, AND THAT IS THE MAIN DESIGN DECISION HERE
------------------------------------------------------------------------
`observations/` already IS the evidence layer. Its `study:` block is "the
SOURCE — what the report is, and by what method it produced results", and its
observations are the individual results, each with its own arms, comparison,
sample, timepoint, uncertainty and `observability`. A second object called
Evidence would hold the same fields about the same results, and two records of
one finding is the exact drift shape this repo has lost weeks to on DOIs.

So a release does not restate its findings. It names them:

    evidence:
      - ref: <study-key>/<observation-id>

and the observation names the release back, through `study.release`. Both
halves are required to agree, because a half-written edge is worse than none:
it reads as a working link from whichever side you arrive on.

A PROTOCOL IS A CONFIGURATION FILE, NOT A CHECKBOX
--------------------------------------------------
`IRB approved: yes` records that somebody decided, and nothing about what was
decided. What a downstream system actually needs to know is the configuration:
who was recruited, what they consented to, what may be collected, how
identifiable it is, who may see which class of it, how long it is kept, and
what happens when somebody withdraws. Written that way it can be CHECKED —
`check_release_against_protocol` below refuses a release that publishes a
dataset more identifiable than its protocol permits, and one that runs an AI
analysis under a protocol whose consent did not disclose AI processing.

This file records governance. **It does not constitute governance.** A
protocol object is not an IRB, an ethics committee, a DPIA or a legal basis,
and `external_review` exists precisely so that the human review a piece of
research actually needed is named rather than implied. An absent
`external_review` block fails validation; `required: not-determined` is a legal
value and a loud one.

ABSENCE IS NOT A VERDICT (the same rule as everywhere else in this repo)
-----------------------------------------------------------------------
`consent.permitted_uses: {model-training: prohibited}` says somebody
established that this use is not allowed. Omitting the class says nobody has
established anything, and nothing may act on it. The two must never collapse, so the
fields where the difference has consequences are REQUIRED and carry an
explicit `unspecified` value rather than being left out. Same discipline as
`"doi": null` vs an absent `doi`, `crossref_reachable: false` vs `flagged`,
and `classify_doi`'s `error` vs `wrong_paper`.

IMMUTABILITY IS STRUCTURAL, NOT A PROMISE
-----------------------------------------
A version is a FILE: `research/releases/<id>/<version>.yaml`. Publishing 1.1.0
writes a new file and never touches 1.0.0, so "never silently rewrite what an
earlier release claimed" is a property of the layout rather than a rule
somebody has to remember. Which version is current is DERIVED (the highest
semver present) and never stated, because stating it would require editing an
older file to say it is no longer current — reintroducing the edit the layout
exists to prevent.

Reviews are not versioned: a review is one person's assertion at one time. A
changed mind is a new review, and the only permitted self-edit is
`withdrawn:`. Nothing here adjudicates a review — see REVIEW_TYPES.

WHAT IS DELIBERATELY NOT HERE
-----------------------------
No reputation, no scores, no voting, no reviewer ranking, no moderation state,
no `accepted`/`rejected` on a review, no pooled estimate, no promotion of
evidence into a claim's argument. Every one of those is a decision this repo
has no real releases with which to make yet.
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - environment problem, not data
    print("research_lib needs PyYAML (pip install -r requirements-docs.txt)",
          file=sys.stderr)
    raise

sys.path.insert(0, str(Path(__file__).parent))
import observation_lib as ol

WIKI_ROOT = Path(__file__).parent.parent
RESEARCH_DIR = WIKI_ROOT / "research"
PROTOCOL_DIR = RESEARCH_DIR / "protocols"
RELEASE_DIR = RESEARCH_DIR / "releases"
REVIEW_DIR = RESEARCH_DIR / "reviews"
ISSUE_DIR = RESEARCH_DIR / "issues"

SCHEMA_VERSION = 1

# The helpers and the shared vocabularies come from observation_lib rather than
# being written again here. `design.family`, `source_type` and the verification
# states mean the same thing about a release as they do about a study, and two
# copies of a closed vocabulary is the defect CLAUDE.md documents fourteen
# times over.
_err, _str, _enum = ol._err, ol._str, ol._enum
DESIGN_FAMILIES = ol.DESIGN_FAMILIES
SOURCE_TYPES = ol.SOURCE_TYPES
VERIFICATION_STATES = ol.VERIFICATION_STATES

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")

# ------------------------------------------------------------- vocabularies

# ORDERED, most identifiable first. The order is the whole point: it is what
# lets `check_release_against_protocol` say that publishing a pseudonymous
# dataset under a protocol that promised deidentified publication is a
# violation, without anybody writing that rule out per release.
IDENTIFIABILITY = ["identified", "pseudonymous", "deidentified", "aggregate",
                   "not-applicable"]

# Three classes, because the interesting rules are about the boundary between
# them: who may touch the collected data, who may touch derivatives, and what
# leaves the building. A finer taxonomy is easy to add and impossible to
# remove once releases reference it.
ACCESS_CLASSES = ["raw", "derived", "published"]

# Which protocol identifiability ceiling governs each access class. `raw` and
# `derived` are both bounded by what was COLLECTED (a derivative cannot be
# more identifiable than its input); `published` is bounded by what the
# protocol says may be published, which is the promise made to the participant.
ACCESS_CEILING = {"raw": "collected", "derived": "collected",
                  "published": "published"}

CONSENT_MECHANISMS = {"explicit", "broad", "opt-out", "waived",
                      "not-applicable", "unspecified"}

# WHAT THE DATA MAY BE USED FOR — a closed vocabulary, because the first real
# protocol immediately needed a use it could refuse.
#
# Learning telemetry collected under terms of service, with no research consent
# step, may legitimately be used to check that a pipeline works and may NOT be
# published as research. Written as free text that distinction is a sentence
# nobody reads; written as classes it is `check_release_against_protocol`
# refusing a release, which is the only form of the rule that holds.
#
# `model-training` is here because being able to say `prohibited` about it out
# loud, permanently, in a file a release is checked against, is worth more than
# the same sentence in a privacy policy.
USE_CLASSES = {
    "internal-pipeline-validation",   # does the pipeline work; never leaves the org
    "product-improvement",            # making the courses better for the learners in them
    "research-analysis",              # analysed for research, not necessarily published
    "research-publication",           # findings published as a research release
    "secondary-research-by-others",   # investigators outside the collecting team
    "model-training",
    "other",
}

# Three states, never two. `prohibited` says somebody established that this use
# is not allowed — which a later batch can be refused on. An ABSENT class means
# `unspecified`: nobody has established anything, and nothing may rely on it.
# Absence is therefore safe by construction, and adding a class to the
# vocabulary later cannot invalidate an already-frozen protocol file.
USE_STATES = {"permitted", "prohibited", "unspecified"}

RISK_CLASSES = {"minimal", "more-than-minimal", "not-determined"}

# The state of the human review this research actually needed.
#
# Five values rather than a boolean, because the two questions a boolean
# collapses are both load-bearing: whether a body reviewed it, and who decided
# it did not need reviewing. `exempt` means an authority determined so and can
# be named; `not-required` means WE reasoned that no external review applies,
# which is a claim by us and is recorded as one. `not-determined` says nobody
# has established either, which is a normal early state and a loud one.
#
# Deliberately not spelled yes/no: YAML 1.1 reads a bare `yes` as the boolean
# True, so `required: yes` would arrive as `True` and fail a string check for
# reasons no author could see. A vocabulary that cannot be written by accident
# is worth more than one that reads a word better.
EXTERNAL_REVIEW_STATES = {"approved", "exempt", "not-required",
                          "not-determined", "pending"}

# A tri-state for every consent flag whose absence would otherwise be read as
# `false`. "Nobody decided" is a state this layer must be able to say out loud.
TRISTATE = {True, False, "unspecified", "not-applicable"}

LOCATION_KINDS = {"url", "doi", "s3", "gcs", "git", "internal", "physical",
                  "not-yet-deposited"}

DATA_FORMATS = {"parquet", "csv", "ndjson", "json", "sqlite", "arrow",
                "audio", "video", "image", "text", "other"}

# What a contribution IS. An EXTENSIBLE controlled vocabulary, not a final
# list: which distinctions real reviewers actually draw is the kind of thing to
# learn from real reviews rather than to decide now. Two beyond the
# commissioning list, because a protocol review and an author reply had no
# other home and would otherwise have been forced into `question`.
REVIEW_TYPES = {
    "question", "methodological_concern", "statistical_concern",
    "governance_concern", "verification", "reanalysis", "replication",
    "boundary_condition", "practice_report", "theoretical_alternative",
    "supporting_evidence", "contradictory_evidence", "response",
}

# WHAT A REVIEW IS NOT ALLOWED TO CARRY, enforced rather than asked for.
#
# A field that records agreement, approval or popularity makes those things
# readable as validity, and once one release writes it every consumer has to
# decide what it means. The schema refuses them by name so that the refusal
# survives the first person who thinks a vote count would be handy.
#
# `bearing` is refused for a different reason: supports/contradicts/qualifies
# already exists, on the edge from an OBSERVATION to a claim, where it is a
# statement about evidence. A review that classified itself that way would be a
# second, incompatible positive/negative axis — and a review is not evidence.
# A review may INTRODUCE evidence; the evidence then bears on the claim.
FORBIDDEN_REVIEW_FIELDS = {
    "positive": "records sentiment, which is not validity",
    "approved": "records agreement, which is not validity",
    "helpful_votes": "records popularity, which is not validity",
    "votes": "records popularity, which is not validity",
    "score": "a ranking belongs to a consumer, computed from the graph, not "
             "stored on the object it would rank",
    "reputation": "a contributor's history is DERIVABLE from their reviews and "
                  "the issues those reviews were confirmed by; a stored copy is "
                  "a second version of it that nothing can check",
    "credentials": "a credential is not a basis — see CONTRIBUTION_BASES",
    "bearing": "supports/contradicts/qualifies is a property of EVIDENCE against "
               "a claim (observations/, appears_in[].bearing). A review may "
               "introduce evidence; it is not evidence",
}

# How a contributor is identified, for a future system that verifies identity.
# NOT implemented here: no authentication, no verification, no proof. The field
# records which state a contributor's identity is CLAIMED to be in, so that the
# distinction exists in the data before anything can act on it.
IDENTITY_STATES = {"public_verified_identity", "verified_pseudonym",
                   "unverified_identity"}

# ---- the assessment block --------------------------------------------------
#
# Properties of the CONTRIBUTION's form, which a future ranking could read,
# instead of properties of how much anybody liked it. Every one is checkable by
# a machine looking at the object and the graph — which is the point: form is
# what automation may judge, and truth is not.
#
# They are author-entered today and expected to become computed. That is why
# each is a tri-state rather than a bare boolean: `unassessed` says nobody has
# evaluated this yet, which is different from evaluating it as false.
ASSESSMENT_FIELDS = ("target_specific", "rationale_present", "evidence_present",
                     "independently_reproduced")

# ---- moderation ------------------------------------------------------------
#
# Conduct, never correctness. The reason codes are deliberately a CLOSED set
# containing only platform-conduct categories: there is no code for "wrong",
# "unfounded", "hostile to the authors" or "disagrees with the release", so a
# harsh methodological critique cannot be moderated away without someone
# inventing a code the schema does not have and failing validation.
#
# `withheld` never means deleted. The object stays in the record with its
# assertion readable; what changes is prominence, and the reason, the policy
# and the mechanism stay attached to it forever.
MODERATION_STATES = {"visible", "limited", "withheld"}
MODERATION_REASONS = {
    "spam", "personal_attack", "harassment", "threat", "impersonation",
    "privacy_violation", "off_topic", "duplicate_submission",
    "illegal_content", "other-conduct",
}
MODERATION_MECHANISMS = {"automated", "human", "automated-then-human"}
APPEAL_STATES = {"none", "requested", "upheld", "overturned"}

# ---- issues ----------------------------------------------------------------

ISSUE_STATES = {"open", "unresolved", "resolved", "withdrawn"}

# What KIND of problem, so that eighteen reviews of one problem can be matched
# to each other. Extensible for the same reason REVIEW_TYPES is.
ISSUE_CATEGORIES = {
    "statistical_assumption", "design_confound", "measurement_validity",
    "data_quality", "reporting_gap", "reproducibility", "generalisability",
    "governance", "interpretation", "other",
}

# A resolution is an ASSERTION BY ITS AUTHOR, not a verdict by the platform,
# which is why `not_supported` and `confirmed` sit in one vocabulary and why
# `decided_by` is required. A resolved issue stays in the record, keeps every
# review that raised it, and can still be targeted by a later review.
RESOLUTION_OUTCOMES = {"confirmed", "partially_confirmed", "not_supported",
                       "superseded", "cannot_be_determined"}

# WHAT GROUNDS THIS CONTRIBUTION — not who the contributor is.
#
# This is the whole of "provenance over prestige" in one field. It is a
# property of the CONTRIBUTION, not of the person: the same reviewer writes one
# review having reproduced the analysis and another having only read the
# release, and those are not equally grounded. Nothing here scores, weights or
# ranks a basis, and a credential is not a basis — `domain-expertise-stated` is
# named `stated` because that is all this layer can honestly record.
CONTRIBUTION_BASES = {
    "reproduced-the-analysis", "reanalysed-the-data", "ran-a-replication",
    "read-the-release", "read-the-protocol", "read-the-artifacts",
    "practitioner-in-this-setting", "participant-in-this-research",
    "domain-expertise-stated", "methodological-expertise-stated",
    "automated-check", "other",
}

# Reviews attach throughout the graph; that is the point of the layer, and
# nothing is forced to be a child of a release.
#
# `analysis` and `dataset` are here although neither is a first-class object:
# both are declared inside a release, so `<release-id>/<version>/<local-id>`
# addresses one unambiguously today and keeps addressing it if either is
# promoted to its own file later. A concern about one specific analysis is the
# single most likely review to be written, and having nowhere to put it would
# push it up to the release, where it stops being specific.
TARGET_KINDS = {"protocol", "release", "evidence", "claim", "review", "issue",
                "analysis", "dataset"}

# Targets addressed as <release-id>/<version>/<local-id> inside a release.
RELEASE_LOCAL_KINDS = {"analysis": "analyses", "dataset": "datasets"}


# ----------------------------------------------------------------- helpers

def _bool(issues, where, value, field, required=False, allow_tristate=False):
    """A flag whose absence must not be readable as `false`."""
    allowed = TRISTATE if allow_tristate else {True, False}
    if value is None:
        if required:
            _err(issues, where, f"{field} is required — omitting it says nobody "
                                f"established it, which is not the same as false")
        return
    if value not in allowed:
        shown = ", ".join(sorted(str(a) for a in allowed))
        _err(issues, where, f"{field} is {value!r}; expected one of {shown}")


def _date(issues, where, value, field, required=False):
    if value is None or value == "":
        if required:
            _err(issues, where, f"{field} is required")
        return
    if not isinstance(value, (str, date)):
        _err(issues, where, f"{field} must be a date or an ISO date string")


def _list_of_str(issues, where, value, field, required=False):
    if value is None:
        if required:
            _err(issues, where, f"{field} is required (an empty list is a legal "
                                f"value and says something; absence does not)")
        return
    if not isinstance(value, list):
        _err(issues, where, f"{field} must be a list")
        return
    for i, v in enumerate(value):
        if not isinstance(v, str) or not v.strip():
            _err(issues, where, f"{field}[{i}] must be a non-empty string")


def semver(version: str) -> tuple:
    m = SEMVER_RE.match(str(version or ""))
    return tuple(int(g) for g in m.groups()) if m else (-1, -1, -1)


def latest(versions) -> str | None:
    """Which version is current — DERIVED, never stated. See the module
    docstring: stating it would mean editing a file that is supposed to be
    frozen the moment its successor exists."""
    versions = [v for v in versions if SEMVER_RE.match(str(v))]
    return max(versions, key=semver) if versions else None


# ----------------------------------------------------------------- loading

def _load_versioned(root: Path) -> tuple[dict, list]:
    """{(id, version): record} from <root>/<id>/<version>.yaml."""
    records, errors = {}, []
    if not root.is_dir():
        return records, errors
    for obj_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for path in sorted(obj_dir.glob("*.yaml")):
            try:
                records[(obj_dir.name, path.stem)] = yaml.safe_load(
                    path.read_text(encoding="utf-8"))
            except yaml.YAMLError as e:
                errors.append(f"{path.relative_to(WIKI_ROOT)}: not valid YAML — {e}")
    return records, errors


def load_protocols() -> tuple[dict, list]:
    return _load_versioned(PROTOCOL_DIR)


def load_releases() -> tuple[dict, list]:
    return _load_versioned(RELEASE_DIR)


def _load_flat(root: Path) -> tuple[dict, list]:
    records, errors = {}, []
    if not root.is_dir():
        return records, errors
    for path in sorted(root.glob("*.yaml")):
        try:
            records[path.stem] = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            errors.append(f"{path.relative_to(WIKI_ROOT)}: not valid YAML — {e}")
    return records, errors


def load_reviews() -> tuple[dict, list]:
    return _load_flat(REVIEW_DIR)


def load_issues() -> tuple[dict, list]:
    return _load_flat(ISSUE_DIR)


# -------------------------------------------------------------- provenance

def _validate_provenance(block, where, issues, *, authors=False):
    """The same shape observations use, for the same reason: a record produced
    by a person, by a pipeline, by a simulation and by a model must stay
    distinguishable after it has been passed along a few times."""
    if not isinstance(block, dict):
        _err(issues, where, "provenance: block is required")
        return
    w = f"{where}.provenance"
    _enum(issues, w, block.get("source_type"), SOURCE_TYPES, "source_type", required=True)
    _enum(issues, w, block.get("verification"), VERIFICATION_STATES, "verification")
    _date(issues, w, block.get("created_at"), "created_at", required=True)
    # Same rule as a page's `verified:`, as authorities.ndjson, and as an
    # observation's extraction: a machine may not certify its own work.
    if block.get("verification") == "human-reviewed" \
            and not str(block.get("verified_by") or "").startswith("human:"):
        _err(issues, w, "verification is 'human-reviewed' but verified_by is not a "
                        "human:<id> — an agent must never mark its own work reviewed")
    if authors:
        people = block.get("authors")
        if not isinstance(people, list) or not people:
            _err(issues, w, "authors: at least one is required")
            return
        for i, person in enumerate(people):
            pw = f"{w}.authors[{i}]"
            if not isinstance(person, dict):
                _err(issues, pw, "must be a mapping with at least `id`")
                continue
            _str(issues, pw, person.get("id"), "id", required=True)
            _str(issues, pw, person.get("role"), "role")


# ---------------------------------------------------------------- protocol

def validate_protocol(rec, pid, version) -> list:
    issues: list = []
    key = f"protocols/{pid}/{version}"
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]
    if rec.get("schema_version") != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {rec.get('schema_version')!r}; "
                          f"this reader understands {SCHEMA_VERSION}")

    p = rec.get("protocol")
    if not isinstance(p, dict):
        _err(issues, key, "protocol: block is required")
        p = {}
    _validate_identity(p, key, pid, version, issues, PROTOCOL_DIR)
    _str(issues, key, p.get("title"), "protocol.title", required=True)
    _date(issues, key, p.get("effective_from"), "protocol.effective_from", required=True)

    _validate_participants(rec.get("participants"), key, issues)
    _validate_consent(rec.get("consent"), key, issues)
    _validate_data(rec.get("data"), key, issues)
    _validate_risks(rec.get("risks"), key, issues)
    _validate_external_review(rec.get("external_review"), key, issues)
    _validate_deviations(rec.get("deviations"), key, issues)
    _validate_provenance(rec.get("provenance"), key, issues)
    return issues


def _validate_identity(block, key, obj_id, version, issues, root):
    """id equals the directory, version equals the filename, and `supersedes`
    points backwards at a file that exists. Nothing points forwards: a file is
    frozen the moment its successor is written, so it cannot be asked to
    mention it."""
    if block.get("id") != obj_id:
        _err(issues, key, f"id is {block.get('id')!r} but the directory says {obj_id!r}")
    elif not ID_RE.match(str(obj_id)):
        _err(issues, key, "id must be lowercase-hyphenated ASCII")
    if block.get("version") != version:
        _err(issues, key, f"version is {block.get('version')!r} but the filename "
                          f"says {version!r}")
    if not SEMVER_RE.match(str(version)):
        _err(issues, key, f"filename {version!r} is not a semantic version (MAJOR.MINOR.PATCH)")
    prev = block.get("supersedes")
    if prev is not None:
        if not (root / str(obj_id) / f"{prev}.yaml").is_file():
            _err(issues, key, f"supersedes {prev!r} but no such version file exists")
        elif semver(prev) >= semver(version):
            _err(issues, key, f"supersedes {prev!r}, which is not earlier than {version!r}")
        # A superseding version that does not say what changed is the silent
        # rewrite the per-version layout exists to prevent, moved one level up.
        _str(issues, key, block.get("change_note"), "change_note", required=True)


def _validate_participants(block, key, issues):
    where = f"{key}.participants"
    if not isinstance(block, dict):
        _err(issues, key, "participants: block is required")
        return
    _str(issues, where, block.get("population"), "population", required=True)
    _str(issues, where, block.get("recruitment"), "recruitment", required=True)
    _list_of_str(issues, where, block.get("inclusion"), "inclusion", required=True)
    _list_of_str(issues, where, block.get("exclusion"), "exclusion", required=True)

    # `[]` here is a claim: somebody looked and identified no vulnerable group.
    # Absence is not, which is why the field is required rather than defaulted.
    vuln = block.get("vulnerable_populations")
    if vuln is None:
        _err(issues, where, "vulnerable_populations is required — an empty list says "
                            "somebody considered the question, absence says nobody did")
    elif not isinstance(vuln, list):
        _err(issues, where, "vulnerable_populations must be a list (possibly empty)")
    else:
        for i, v in enumerate(vuln):
            w = f"{where}.vulnerable_populations[{i}]"
            if not isinstance(v, dict):
                _err(issues, w, "must be a mapping with group and safeguards")
                continue
            _str(issues, w, v.get("group"), "group", required=True)
            _list_of_str(issues, w, v.get("safeguards"), "safeguards", required=True)

    comp = block.get("compensation")
    if not isinstance(comp, dict):
        _err(issues, where, "compensation is required — `{kind: none}` is a value and "
                            "an answer; silence is neither")
    else:
        _str(issues, f"{where}.compensation", comp.get("kind"), "kind", required=True)


def _validate_consent(block, key, issues):
    where = f"{key}.consent"
    if not isinstance(block, dict):
        _err(issues, key, "consent: block is required")
        return
    required_flag = block.get("required")
    _bool(issues, where, required_flag, "required", required=True)
    _enum(issues, where, block.get("mechanism"), CONSENT_MECHANISMS, "mechanism", required=True)
    _bool(issues, where, block.get("ai_processing_disclosed"), "ai_processing_disclosed",
          required=True, allow_tristate=True)
    if block.get("ai_processing_disclosed") is True:
        _str(issues, where, block.get("ai_processing_detail"), "ai_processing_detail",
             required=True)

    # `secondary_research_use` was a separate tri-state flag in the first draft.
    # It is exactly `permitted_uses: {secondary-research-by-others: ...}` said a
    # second way, and two places to state one fact is the drift shape this repo
    # has lost weeks to. Refused by name so it cannot quietly come back.
    if "secondary_research_use" in block:
        _err(issues, where, "`secondary_research_use` is not a consent field: it is "
                            "`permitted_uses: {secondary-research-by-others: permitted "
                            "| prohibited | unspecified}`, said once")

    uses = block.get("permitted_uses")
    if not isinstance(uses, dict):
        _err(issues, where, "permitted_uses must be a mapping of use class to "
                            f"{' | '.join(sorted(USE_STATES))} — a free-text list cannot be "
                            f"checked, and the rule that a release may not publish from "
                            f"data that does not permit it is the whole point of writing "
                            f"the protocol as configuration. Classes: "
                            f"{', '.join(sorted(USE_CLASSES))}")
    else:
        for cls, state in uses.items():
            if cls not in USE_CLASSES:
                _err(issues, f"{where}.permitted_uses", f"{cls!r} is not a use class; "
                             f"expected one of {', '.join(sorted(USE_CLASSES))}")
            _enum(issues, f"{where}.permitted_uses", state, USE_STATES, cls, required=True)
    _str(issues, where, block.get("permitted_uses_note"), "permitted_uses_note")

    if required_flag is True:
        # What the participant was actually shown. This is the field that makes
        # the difference between a protocol and a checkbox: consent is only
        # meaningful for what was disclosed, so the disclosure is the record.
        _list_of_str(issues, where, block.get("information_provided"),
                     "information_provided", required=True)
        w = block.get("withdrawal")
        if not isinstance(w, dict):
            _err(issues, where, "withdrawal: block is required when consent is required")
        else:
            ww = f"{where}.withdrawal"
            _bool(issues, ww, w.get("allowed"), "allowed", required=True)
            if w.get("allowed") is True:
                _str(issues, ww, w.get("mechanism"), "mechanism", required=True)
                # "You may withdraw" and "what happens to what you already gave
                # us" are two promises, and only the second is operational.
                _str(issues, ww, w.get("effect_on_collected_data"),
                     "effect_on_collected_data", required=True)


def _validate_data(block, key, issues):
    where = f"{key}.data"
    if not isinstance(block, dict):
        _err(issues, key, "data: block is required")
        return
    collected = block.get("collected")
    if not isinstance(collected, list) or not collected:
        _err(issues, where, "collected: at least one item is required")
    else:
        for i, item in enumerate(collected):
            w = f"{where}.collected[{i}]"
            if not isinstance(item, dict):
                _err(issues, w, "must be a mapping with item, purpose and identifiability")
                continue
            _str(issues, w, item.get("item"), "item", required=True)
            # Collection without a stated purpose is the thing data-minimisation
            # rules exist to stop, and it is cheap to require here.
            _str(issues, w, item.get("purpose"), "purpose", required=True)
            _enum(issues, w, item.get("identifiability"), IDENTIFIABILITY,
                  "identifiability", required=True)
    # An empty `prohibited: []` says nobody ruled anything out, which is
    # legal and visible. Absence says nobody considered it, which is not.
    _list_of_str(issues, where, block.get("prohibited"), "prohibited", required=True)

    ident = block.get("identifiability")
    if not isinstance(ident, dict):
        _err(issues, where, "identifiability: {collected, published} is required")
    else:
        for f in ("collected", "published"):
            _enum(issues, f"{where}.identifiability", ident.get(f), IDENTIFIABILITY,
                  f, required=True)

    if isinstance(ident, dict) and ident.get("collected") in ("identified", "pseudonymous"):
        d = block.get("deidentification")
        if not isinstance(d, dict):
            _err(issues, where, f"identifiability.collected is {ident.get('collected')!r}, "
                                f"so deidentification: is required — how the link to a "
                                f"person is broken, and by whom it can be restored")
        else:
            dw = f"{where}.deidentification"
            _str(issues, dw, d.get("method"), "method", required=True)
            _bool(issues, dw, d.get("reversible"), "reversible", required=True)
            if d.get("reversible") is True:
                _str(issues, dw, d.get("key_holder"), "key_holder", required=True)

    ret = block.get("retention")
    if not isinstance(ret, dict):
        _err(issues, where, "retention: block is required")
    else:
        for f in ("raw", "derived"):
            _str(issues, f"{where}.retention", ret.get(f), f, required=True)

    store = block.get("storage")
    if not isinstance(store, dict):
        _err(issues, where, "storage: block is required")
    else:
        sw = f"{where}.storage"
        _str(issues, sw, store.get("location"), "location", required=True)
        for f in ("encryption_at_rest", "encryption_in_transit", "access_logging"):
            _bool(issues, sw, store.get(f), f, required=True)

    access = block.get("access")
    if not isinstance(access, dict):
        _err(issues, where, "access: block is required, keyed by access class "
                            f"({', '.join(ACCESS_CLASSES)})")
    else:
        for cls in ACCESS_CLASSES:
            _list_of_str(issues, f"{where}.access", access.get(cls), cls, required=True)
        for cls in access:
            if cls not in ACCESS_CLASSES:
                _err(issues, f"{where}.access", f"{cls!r} is not an access class; "
                                                f"expected {', '.join(ACCESS_CLASSES)}")


def _validate_risks(block, key, issues):
    where = f"{key}.risks"
    if not isinstance(block, dict):
        _err(issues, key, "risks: block is required")
        return
    _enum(issues, where, block.get("classification"), RISK_CLASSES,
          "classification", required=True)
    identified = block.get("identified")
    if not isinstance(identified, list):
        _err(issues, where, "identified must be a list (empty is legal and means "
                            "somebody looked and found none)")
        return
    for i, r in enumerate(identified):
        w = f"{where}.identified[{i}]"
        if not isinstance(r, dict):
            _err(issues, w, "must be a mapping with risk and mitigation")
            continue
        _str(issues, w, r.get("risk"), "risk", required=True)
        # A risk with no stated mitigation is a risk nobody has decided about.
        _str(issues, w, r.get("mitigation"), "mitigation", required=True)


def _validate_external_review(block, key, issues):
    """The block that keeps this layer honest about what it is.

    A machine-readable protocol is not an ethics committee. This field says
    which human or institutional review the research actually needed and
    whether it happened, so that a release can never imply approval it does
    not have. `not-determined` is a legal value and states a real position."""
    where = f"{key}.external_review"
    if not isinstance(block, dict):
        _err(issues, key, "external_review: block is required — a protocol file records "
                          "governance, it does not constitute it, so which external review "
                          "was needed must be stated even when the answer is 'none'")
        return
    status = block.get("status")
    _enum(issues, where, status, EXTERNAL_REVIEW_STATES, "status", required=True)
    if status == "approved":
        # An approval nobody can look up is an assertion, not an approval.
        _str(issues, where, block.get("authority"), "authority", required=True)
        _str(issues, where, block.get("approval_id"), "approval_id", required=True)
        _date(issues, where, block.get("reviewed_at"), "reviewed_at")
    elif status == "exempt":
        _str(issues, where, block.get("authority"), "authority", required=True)
        _str(issues, where, block.get("determination"), "determination", required=True)
    elif status == "not-required":
        # Our own reasoning, recorded as ours. This is the value most likely to
        # be wrong, so it is the one that must show its working.
        _str(issues, where, block.get("determination"), "determination", required=True)
    elif status == "pending":
        _str(issues, where, block.get("authority"), "authority", required=True)


def _validate_deviations(block, key, issues):
    """Appended to a frozen file, and the one place that is allowed.

    A deviation is a fact about the version that was in force when it
    happened. Recording it as a new version would assert that the rules
    changed, which is a different and false statement. Whether this should
    instead be an append-only NDJSON log beside the object — the shape this
    repo already uses for manifest.ndjson and authorities.ndjson — is an open
    question, and is deliberately left open until a real deviation exists."""
    if block is None:
        return
    if not isinstance(block, list):
        _err(issues, f"{key}.deviations", "must be a list")
        return
    for i, d in enumerate(block):
        w = f"{key}.deviations[{i}]"
        if not isinstance(d, dict):
            _err(issues, w, "must be a mapping")
            continue
        _date(issues, w, d.get("at"), "at", required=True)
        _str(issues, w, d.get("description"), "description", required=True)
        _str(issues, w, d.get("reported_to"), "reported_to", required=True)
        _str(issues, w, d.get("resolution"), "resolution")


# ----------------------------------------------------------------- release

def validate_release(rec, rid, version) -> list:
    issues: list = []
    key = f"releases/{rid}/{version}"
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]
    if rec.get("schema_version") != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {rec.get('schema_version')!r}; "
                          f"this reader understands {SCHEMA_VERSION}")

    r = rec.get("release")
    if not isinstance(r, dict):
        _err(issues, key, "release: block is required")
        r = {}
    _validate_identity(r, key, rid, version, issues, RELEASE_DIR)
    _str(issues, key, r.get("title"), "release.title", required=True)
    # The QUESTION, not the finding. A release that cannot say what it was
    # asking is a paper, not an investigation.
    _str(issues, key, r.get("question"), "release.question", required=True)
    _date(issues, key, r.get("released_at"), "release.released_at", required=True)

    design = rec.get("research_design")
    if not isinstance(design, dict):
        _err(issues, key, "research_design: block is required")
    else:
        _enum(issues, f"{key}.research_design", design.get("family"), DESIGN_FAMILIES,
              "family", required=True)
        _str(issues, f"{key}.research_design", design.get("detail"), "detail")

    # A protocol ref, or an explicit statement of why there is none. A
    # secondary analysis of somebody else's public data genuinely has no
    # protocol of ours; "nobody wrote one down" is a different answer and this
    # forces the two apart.
    proto = rec.get("protocol")
    if isinstance(proto, dict):
        _str(issues, f"{key}.protocol", proto.get("ref"), "ref", required=True)
        _str(issues, f"{key}.protocol", proto.get("version"), "version", required=True)
    elif not rec.get("no_protocol_reason"):
        _err(issues, key, "protocol: {ref, version} is required, or `no_protocol_reason:` "
                          "must say why this investigation has no protocol of ours")

    _validate_datasets(rec.get("datasets"), key, issues)
    _validate_analyses(rec.get("analyses"), key, issues, rec.get("datasets"))
    _validate_evidence_refs(rec.get("evidence"), key, issues)
    _validate_artifacts(rec.get("artifacts"), key, issues)

    # Interpretation is what the authors think it means, and is kept apart
    # from the claim it might support: the claim is a durable object with its
    # own page and its own evidence from elsewhere, and a release that
    # restated it would be a second copy nobody could reconcile. The edge from
    # this release's evidence to a claim lives on the observation's
    # `appears_in`, in one place, with a direction.
    _str(issues, key, rec.get("interpretation"), "interpretation", required=True)
    _list_of_str(issues, key, rec.get("limitations"), "limitations", required=True)
    if isinstance(rec.get("limitations"), list) and not rec["limitations"]:
        _err(issues, key, "limitations is empty — a release with no limitations is a "
                          "claim about the research, and an implausible one")
    _str(issues, key, rec.get("funding"), "funding", required=True)
    _str(issues, key, rec.get("conflicts"), "conflicts", required=True)
    _validate_provenance(rec.get("provenance"), key, issues, authors=True)
    return issues


def _validate_datasets(datasets, key, issues):
    """Identifiers, metadata and hashes — never the data.

    A research dataset is Parquet on object storage, or a database, or audio.
    None of that belongs in a git repository of markdown, and copying a
    summary of it here would create a second version of the numbers. What the
    wiki holds is what is needed to FIND the data and to prove that what was
    found is what was analysed: a location, a hash, a grain, and the access
    class it falls under."""
    if datasets is None:
        return
    if not isinstance(datasets, list):
        _err(issues, f"{key}.datasets", "must be a list")
        return
    seen = set()
    for i, d in enumerate(datasets):
        w = f"{key}.datasets[{i}]"
        if not isinstance(d, dict):
            _err(issues, w, "must be a mapping")
            continue
        did = d.get("id")
        _str(issues, w, did, "id", required=True)
        if did in seen:
            _err(issues, w, f"duplicate dataset id {did!r}")
        seen.add(did)
        _str(issues, w, d.get("title"), "title", required=True)
        # The unit of a row. Lazuli's learning-observation pipeline is
        # attempt-grained; a table whose grain nobody wrote down cannot be
        # joined to anything without guessing.
        _str(issues, w, d.get("grain"), "grain", required=True)
        _enum(issues, w, d.get("format"), DATA_FORMATS, "format", required=True)
        _enum(issues, w, d.get("identifiability"), IDENTIFIABILITY,
              "identifiability", required=True)
        _enum(issues, w, d.get("access"), set(ACCESS_CLASSES), "access", required=True)
        loc = d.get("location")
        if not isinstance(loc, dict):
            _err(issues, w, "location: {kind, ref} is required — where this actually is")
        else:
            _enum(issues, f"{w}.location", loc.get("kind"), LOCATION_KINDS,
                  "kind", required=True)
            if loc.get("kind") != "not-yet-deposited":
                _str(issues, f"{w}.location", loc.get("ref"), "ref", required=True)
        # The hash is what makes the reference reproducible rather than
        # aspirational: without it, "the dataset at this URL" names whatever
        # is at that URL today.
        sha = d.get("sha256")
        if sha is None:
            if loc is not None and isinstance(loc, dict) \
                    and loc.get("kind") != "not-yet-deposited":
                _err(issues, w, "sha256 is required for a deposited dataset — a location "
                                "without a hash names whatever is there today")
        elif not SHA256_RE.match(str(sha)):
            _err(issues, w, f"sha256 {sha!r} is not 64 lowercase hex characters")
        for parent in d.get("derived_from") or []:
            if parent not in seen and parent not in {x.get("id") for x in datasets
                                                     if isinstance(x, dict)}:
                _err(issues, w, f"derived_from {parent!r} names no dataset in this release")


def _validate_analyses(analyses, key, issues, datasets):
    """Code, commit, environment, inputs. The reproducibility half."""
    if analyses is None:
        return
    if not isinstance(analyses, list):
        _err(issues, f"{key}.analyses", "must be a list")
        return
    dataset_ids = {d.get("id") for d in (datasets or []) if isinstance(d, dict)}
    seen = set()
    for i, a in enumerate(analyses):
        w = f"{key}.analyses[{i}]"
        if not isinstance(a, dict):
            _err(issues, w, "must be a mapping")
            continue
        aid = a.get("id")
        _str(issues, w, aid, "id", required=True)
        if aid in seen:
            _err(issues, w, f"duplicate analysis id {aid!r}")
        seen.add(aid)
        _str(issues, w, a.get("title"), "title", required=True)
        code = a.get("code")
        if not isinstance(code, dict):
            _err(issues, w, "code: {repo, commit, path} is required")
        else:
            cw = f"{w}.code"
            _str(issues, cw, code.get("repo"), "repo", required=True)
            # A branch or a tag moves. A commit is the analysis that ran.
            _str(issues, cw, code.get("commit"), "commit", required=True)
            _str(issues, cw, code.get("path"), "path", required=True)
        env = a.get("environment")
        if not isinstance(env, dict):
            _err(issues, w, "environment: is required — the same code on a different "
                            "stack is a different analysis")
        else:
            _str(issues, f"{w}.environment", env.get("detail"), "detail", required=True)
        inputs = a.get("inputs")
        if not isinstance(inputs, list) or not inputs:
            _err(issues, w, "inputs: at least one dataset id is required")
        else:
            for dep in inputs:
                if dep not in dataset_ids:
                    _err(issues, w, f"input {dep!r} names no dataset in this release")
        # Read by check_release_against_protocol against the protocol's
        # consent disclosure. Tri-state, because "nobody recorded whether a
        # model touched this" is not "no model touched it".
        _bool(issues, w, a.get("ai_processing"), "ai_processing",
              required=True, allow_tristate=True)


EVIDENCE_REF_RE = re.compile(r"^([a-z0-9][a-z0-9-]*)/([^\s/]+)$")


def _validate_evidence_refs(evidence, key, issues):
    """Shape only. Resolution against observations/ happens in validate_all,
    which has both stores loaded and can check the back-reference too."""
    if evidence is None:
        return
    if not isinstance(evidence, list):
        _err(issues, f"{key}.evidence", "must be a list")
        return
    for i, e in enumerate(evidence):
        w = f"{key}.evidence[{i}]"
        if not isinstance(e, dict):
            _err(issues, w, "must be a mapping with `ref`")
            continue
        ref = e.get("ref")
        _str(issues, w, ref, "ref", required=True)
        if ref and not EVIDENCE_REF_RE.match(str(ref)):
            _err(issues, w, f"ref {ref!r} must be '<study-key>/<observation-id>', naming "
                            f"a record in observations/")


def _validate_artifacts(artifacts, key, issues):
    """A PDF, a notebook, a dashboard, a conference talk — RENDERINGS of this
    release, listed as such. None of them is the release, and the schema is
    deliberately indifferent to which of them exist."""
    if artifacts is None:
        return
    if not isinstance(artifacts, list):
        _err(issues, f"{key}.artifacts", "must be a list")
        return
    for i, a in enumerate(artifacts):
        w = f"{key}.artifacts[{i}]"
        if not isinstance(a, dict):
            _err(issues, w, "must be a mapping")
            continue
        _str(issues, w, a.get("id"), "id", required=True)
        _str(issues, w, a.get("kind"), "kind", required=True)
        loc = a.get("location")
        if not isinstance(loc, dict):
            _err(issues, w, "location: {kind, ref} is required")
        else:
            _enum(issues, f"{w}.location", loc.get("kind"), LOCATION_KINDS,
                  "kind", required=True)


# ------------------------------------------------------------------ review

def validate_review(rec, rid) -> list:
    issues: list = []
    key = f"reviews/{rid}"
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]
    if rec.get("schema_version") != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {rec.get('schema_version')!r}; "
                          f"this reader understands {SCHEMA_VERSION}")

    r = rec.get("review")
    if not isinstance(r, dict):
        _err(issues, key, "review: block is required")
        return issues
    if r.get("id") != rid:
        _err(issues, key, f"id is {r.get('id')!r} but the filename says {rid!r}")
    _date(issues, key, r.get("created_at"), "created_at", required=True)
    _enum(issues, key, r.get("review_type"), REVIEW_TYPES, "review_type", required=True)

    target = r.get("target")
    if not isinstance(target, dict):
        _err(issues, key, "target: block is required")
    else:
        tw = f"{key}.target"
        _enum(issues, tw, target.get("kind"), TARGET_KINDS, "kind", required=True)
        _str(issues, tw, target.get("ref"), "ref", required=True)
        # A review of release 1.0.0 stays a review OF 1.0.0 after 1.1.0 ships.
        # Without the version a review silently re-points at work its author
        # never read, which is the opposite of what this layer is for.
        if target.get("kind") in ("release", "protocol"):
            _str(issues, tw, target.get("version"), "version", required=True)

    # One sentence saying what the contribution asserts, kept apart from the
    # argument for it. An agent reading a hundred reviews reads assertions.
    _str(issues, key, r.get("assertion"), "assertion", required=True)
    _str(issues, key, r.get("rationale"), "rationale", required=True)

    author = r.get("author")
    if not isinstance(author, dict):
        _err(issues, key, "author: block is required")
    else:
        aw = f"{key}.author"
        # A STABLE contributor id, so that a future system can derive a
        # contribution history from the graph — eleven concerns later confirmed
        # by an issue, two not supported, four reproducible reanalyses. It has
        # to be derivable, which means the edges have to be there; it must not
        # be stored, which is why FORBIDDEN_REVIEW_FIELDS refuses `reputation`.
        _str(issues, aw, author.get("id"), "id", required=True)
        # Claimed, never verified here. No institution, rank, degree or
        # publication history is required, requested or permitted to gate
        # whether this contribution exists.
        _enum(issues, aw, author.get("identity_state"), IDENTITY_STATES, "identity_state")
        basis = author.get("basis")
        if not isinstance(basis, list) or not basis:
            _err(issues, aw, "basis: at least one is required — what GROUNDS this "
                             "contribution, which is a property of the contribution "
                             "and not of the contributor")
        else:
            for b in basis:
                _enum(issues, aw, b, CONTRIBUTION_BASES, "basis entry")

    _validate_assessment(r.get("assessment"), key, issues)
    _validate_moderation(r.get("moderation"), key, issues)

    # The refusals, by name. See FORBIDDEN_REVIEW_FIELDS.
    for field, why in FORBIDDEN_REVIEW_FIELDS.items():
        if field in r:
            _err(issues, key, f"`{field}` is not a field of a review: {why}")

    # Which issue(s) this review is an instance of. The aggregation edge may be
    # written from either end — a reviewer may know they are piling onto a
    # known problem, or a later process may notice they were. Both ends are
    # checked against each other in validate_all.
    for i, ref in enumerate(r.get("issues") or []):
        _str(issues, f"{key}.issues[{i}]", ref, "issue ref", required=True)

    for i, e in enumerate(r.get("evidence") or []):
        w = f"{key}.evidence[{i}]"
        if not isinstance(e, dict):
            _err(issues, w, "must be a mapping with kind and ref")
            continue
        _enum(issues, w, e.get("kind"), TARGET_KINDS | {"external"}, "kind", required=True)
        _str(issues, w, e.get("ref"), "ref", required=True)

    # The one permitted self-edit. Everything else — a changed mind, an
    # answer, an agreement — is a NEW review, because a thread of assertions
    # each of which is attributable is the record this layer wants, and an
    # editable one is not.
    wd = r.get("withdrawn")
    if wd is not None:
        if not isinstance(wd, dict):
            _err(issues, key, "withdrawn must be a mapping {at, reason}")
        else:
            _date(issues, f"{key}.withdrawn", wd.get("at"), "at", required=True)
            _str(issues, f"{key}.withdrawn", wd.get("reason"), "reason", required=True)
    return issues


def _validate_assessment(block, key, issues):
    """Form, not favour.

    Every field here is something a machine can check by looking at the object
    and the graph: is it attached to a real target, does it reason, does it
    cite anything that exists, has anyone independently reproduced it, is it
    the same point somebody already made. A future prominence calculation can
    read these. None of them records whether anybody agreed.

    Tri-state on purpose: `unassessed` says nobody has evaluated this, which is
    not the same as evaluating it as false — the same distinction the rest of
    this repo draws between an absent field and a recorded negative."""
    if block is None:
        return
    if not isinstance(block, dict):
        _err(issues, f"{key}.assessment", "must be a mapping")
        return
    where = f"{key}.assessment"
    for f in ASSESSMENT_FIELDS:
        v = block.get(f)
        if v is not None and v not in (True, False, "unassessed"):
            _err(issues, where, f"{f} is {v!r}; expected true, false or 'unassessed'")
    # Not a score and not a merge: naming the earlier contribution keeps the
    # duplicate in the record with its own author and date, which is what
    # protects attribution for whoever said it first.
    dup = block.get("duplicate_of")
    if dup is not None and not isinstance(dup, str):
        _err(issues, where, "duplicate_of must be a review id, or absent")
    for f in block:
        if f not in (*ASSESSMENT_FIELDS, "duplicate_of", "assessed_by", "assessed_at",
                     "note"):
            _err(issues, where, f"{f!r} is not an assessment field; the block records "
                                f"checkable properties of form, and adding one that "
                                f"records reception is how form becomes popularity")


def _validate_moderation(block, key, issues):
    """A list, because a moderation history must not be overwritable.

    Content never disappears without a durable explanation: `withheld` changes
    prominence, not existence, and the reason, the policy it was taken under,
    the mechanism and the appeal state stay attached. There is deliberately no
    reason code meaning "wrong" or "disagrees with the authors" — see
    MODERATION_REASONS — so suppressing a critique on the merits requires
    inventing a code the schema does not have, and fails here.

    Whether ModerationDecision deserves its own object is left open. It does
    not yet: a decision is only ever about one review, so a list on the review
    holds the same information with one fewer file to join."""
    if block is None:
        return
    entries = block if isinstance(block, list) else [block]
    for i, m in enumerate(entries):
        where = f"{key}.moderation[{i}]"
        if not isinstance(m, dict):
            _err(issues, where, "must be a mapping")
            continue
        _enum(issues, where, m.get("state"), MODERATION_STATES, "state", required=True)
        if m.get("state") in ("limited", "withheld"):
            reason = m.get("reason")
            if not isinstance(reason, dict):
                _err(issues, where, "a limited or withheld review must carry "
                                    "reason: {code, policy} — content does not lose "
                                    "prominence without a durable explanation")
            else:
                _enum(issues, f"{where}.reason", reason.get("code"), MODERATION_REASONS,
                      "code", required=True)
                # The rule it was taken under, so the decision can be argued with.
                _str(issues, f"{where}.reason", reason.get("policy"), "policy", required=True)
            decision = m.get("decision")
            if not isinstance(decision, dict):
                _err(issues, where, "decision: {mechanism, at} is required")
            else:
                _enum(issues, f"{where}.decision", decision.get("mechanism"),
                      MODERATION_MECHANISMS, "mechanism", required=True)
                _date(issues, f"{where}.decision", decision.get("at"), "at", required=True)
        appeal = m.get("appeal")
        if isinstance(appeal, dict):
            _enum(issues, f"{where}.appeal", appeal.get("status"), APPEAL_STATES, "status")


# ------------------------------------------------------------------- issue

def validate_issue(rec, iid) -> list:
    """One problem, however many people found it.

    The object that stops open review becoming a hundred repetitive comments.
    Without it, eighteen people independently noticing the same statistical
    defect produce eighteen unlinked reviews: nothing can tell that they are
    one problem, prominence has to be computed from volume, and the person who
    said it first is indistinguishable from the seventeenth. With it, that
    becomes one issue, eighteen independent identifications in the order they
    arrived, whatever analyses support it, whatever reviews dispute it, and one
    author response.

    An issue is NOT an adjudication. `resolution` is an assertion by a named
    author like any other, it never removes the reviews that raised the issue,
    and a review may target the issue after it is resolved."""
    issues: list = []
    key = f"issues/{iid}"
    if not isinstance(rec, dict):
        return [f"{key}: file does not contain a YAML mapping"]
    if rec.get("schema_version") != SCHEMA_VERSION:
        _err(issues, key, f"schema_version is {rec.get('schema_version')!r}; "
                          f"this reader understands {SCHEMA_VERSION}")
    i = rec.get("issue")
    if not isinstance(i, dict):
        _err(issues, key, "issue: block is required")
        return issues
    if i.get("id") != iid:
        _err(issues, key, f"id is {i.get('id')!r} but the filename says {iid!r}")
    _date(issues, key, i.get("created_at"), "created_at", required=True)
    _enum(issues, key, i.get("category"), ISSUE_CATEGORIES, "category", required=True)
    _str(issues, key, i.get("summary"), "summary", required=True)
    _enum(issues, key, i.get("state"), ISSUE_STATES, "state", required=True)

    target = i.get("target")
    if not isinstance(target, dict):
        _err(issues, key, "target: block is required — an issue attaches to a clearly "
                          "identified object, not to a conversation")
    else:
        _enum(issues, f"{key}.target", target.get("kind"), TARGET_KINDS, "kind", required=True)
        _str(issues, f"{key}.target", target.get("ref"), "ref", required=True)
        if target.get("kind") in ("release", "protocol"):
            _str(issues, f"{key}.target", target.get("version"), "version", required=True)

    # Ordered by first appearance and append-only: the first entry is the first
    # person to identify the problem, and that attribution is the thing a
    # merge-into-one-thread would destroy.
    raised = i.get("raised_by")
    if not isinstance(raised, list) or not raised:
        _err(issues, key, "raised_by: at least one review is required — an issue nobody "
                          "raised has no provenance")
    for field in ("raised_by", "supporting", "disputing", "response"):
        v = i.get(field)
        if v is not None and not isinstance(v, list):
            _err(issues, key, f"{field} must be a list of refs")

    res = i.get("resolution")
    if i.get("state") == "resolved":
        if not isinstance(res, dict):
            _err(issues, key, "state is 'resolved' but there is no resolution: block — "
                              "a criticism must not be able to stop being visible without "
                              "a durable statement of what happened to it")
        else:
            rw = f"{key}.resolution"
            _enum(issues, rw, res.get("outcome"), RESOLUTION_OUTCOMES, "outcome", required=True)
            _str(issues, rw, res.get("explanation"), "explanation", required=True)
            # Who asserts this. A resolution is a position, not a verdict, and
            # an unattributed one reads as the platform having decided.
            _str(issues, rw, res.get("decided_by"), "decided_by", required=True)
            _date(issues, rw, res.get("at"), "at", required=True)
    elif res is not None and not isinstance(res, dict):
        _err(issues, key, "resolution must be a mapping")

    for field, why in FORBIDDEN_REVIEW_FIELDS.items():
        if field in i:
            _err(issues, key, f"`{field}` is not a field of an issue: {why}")
    return issues


# --------------------------------------------------------- the cross-checks

def check_release_against_protocol(rel, rel_key, protocol, issues):
    """The arrow the whole protocol object exists for.

    A protocol written as prose can only be read. Written as configuration it
    can be CHECKED, and these are the two checks that a real release would
    most want caught before rather than after publication. Both are narrow on
    purpose: this is an enforcement DEMONSTRATION, not a policy engine, and a
    rule that fires on a case nobody has met yet is a rule nobody can trust."""
    data = (protocol or {}).get("data") or {}
    ident = data.get("identifiability") or {}
    consent = (protocol or {}).get("consent") or {}

    for i, d in enumerate(rel.get("datasets") or []):
        if not isinstance(d, dict):
            continue
        w = f"{rel_key}.datasets[{i}]"
        cls, got = d.get("access"), d.get("identifiability")
        ceiling_field = ACCESS_CEILING.get(cls)
        ceiling = ident.get(ceiling_field) if ceiling_field else None
        if got in IDENTIFIABILITY and ceiling in IDENTIFIABILITY \
                and IDENTIFIABILITY.index(got) < IDENTIFIABILITY.index(ceiling):
            _err(issues, w, f"dataset is {got!r} at access class {cls!r}, but the protocol "
                            f"permits at most {ceiling!r} there "
                            f"(data.identifiability.{ceiling_field})")

    for i, a in enumerate(rel.get("analyses") or []):
        if not isinstance(a, dict) or a.get("ai_processing") is not True:
            continue
        if consent.get("ai_processing_disclosed") is not True:
            _err(issues, f"{rel_key}.analyses[{i}]",
                 f"analysis declares ai_processing: true, but the protocol's consent "
                 f"records ai_processing_disclosed: "
                 f"{consent.get('ai_processing_disclosed')!r}")

    # A RELEASE IS A PUBLICATION. So naming a protocol that does not permit
    # research publication is not a paperwork problem, it is the release saying
    # it may not exist.
    #
    # This is the check the first real protocol needed on the day it was
    # scoped: platform telemetry collected under terms of service, with no
    # research consent step, is legitimately usable to validate a pipeline and
    # is NOT publishable as research. Without this, a release could draw on it
    # and every other check would pass.
    #
    # `unspecified` and absent both fail, and are reported differently, because
    # "we decided not to" and "nobody has decided" are different states and the
    # second is the one that gets fixed by asking somebody.
    uses = consent.get("permitted_uses")
    state = uses.get("research-publication") if isinstance(uses, dict) else None
    if state != "permitted":
        shown = repr(state) if state else "not stated (so: unspecified)"
        why = ("Publication is prohibited under this protocol."
               if state == "prohibited" else
               "Nobody has established that these data may be published as research; "
               "that has to be settled in the protocol, not here.")
        _err(issues, rel_key,
             f"this release publishes findings, but its protocol's consent records "
             f"permitted_uses['research-publication'] as {shown}. {why}")


def validate_all() -> list:
    """Every object, plus every join between them and into observations/."""
    protocols, issues = load_protocols()
    releases, rel_errors = load_releases()
    reviews, rev_errors = load_reviews()
    issue_recs, iss_errors = load_issues()
    issues = list(issues) + rel_errors + rev_errors + iss_errors

    for (pid, version), rec in sorted(protocols.items()):
        issues.extend(validate_protocol(rec, pid, version))
    for (rid, version), rec in sorted(releases.items()):
        issues.extend(validate_release(rec, rid, version))
    for rid, rec in sorted(reviews.items()):
        issues.extend(validate_review(rec, rid))
    for iid, rec in sorted(issue_recs.items()):
        issues.extend(validate_issue(rec, iid))

    obs_records, obs_errors = ol.load_all()
    issues.extend(obs_errors)

    for (rid, version), rec in sorted(releases.items()):
        if not isinstance(rec, dict):
            continue
        key = f"releases/{rid}/{version}"
        proto = rec.get("protocol")
        protocol_rec = None
        if isinstance(proto, dict):
            pkey = (proto.get("ref"), proto.get("version"))
            protocol_rec = protocols.get(pkey)
            if protocol_rec is None:
                _err(issues, key, f"protocol {pkey[0]!r} version {pkey[1]!r} does not "
                                  f"exist under research/protocols/")
        if isinstance(protocol_rec, dict):
            check_release_against_protocol(rec, key, protocol_rec, issues)

        _check_evidence_join(rec, rid, version, obs_records, issues)

        # What this version was published to answer. Typed, because a version
        # may address an aggregated issue or a single review, and the two are
        # different objects with different provenance.
        for i, ref in enumerate(rec.get("release", {}).get("addresses") or []):
            w = f"{key}.release.addresses[{i}]"
            if not isinstance(ref, dict):
                _err(issues, w, "must be a mapping {kind, ref}")
                continue
            kind, target = ref.get("kind"), ref.get("ref")
            if kind == "issue" and target not in issue_recs:
                _err(issues, w, f"issue {target!r} does not exist in research/issues/")
            elif kind == "review" and target not in reviews:
                _err(issues, w, f"review {target!r} does not exist in research/reviews/")
            elif kind not in ("issue", "review"):
                _err(issues, w, f"kind is {kind!r}; a release addresses an issue or a review")

    # The other half of the edge: an observation naming a release.
    for study_key, rec in sorted(obs_records.items()):
        if not isinstance(rec, dict):
            continue
        release = (rec.get("study") or {}).get("release")
        if not isinstance(release, dict):
            continue
        pair = (release.get("ref"), release.get("version"))
        if pair not in releases:
            _err(issues, f"observations/{study_key}", f"study.release names "
                 f"{pair[0]!r} version {pair[1]!r}, which does not exist under "
                 f"research/releases/")
            continue
        _check_analysis_refs(rec, study_key, releases[pair], issues)

    for rid, rec in sorted(reviews.items()):
        if isinstance(rec, dict):
            _check_review_target(rec, rid, protocols, releases, reviews, issue_recs,
                                 obs_records, issues, f"reviews/{rid}",
                                 (rec.get("review") or {}).get("target"))
            for ref in (rec.get("review") or {}).get("issues") or []:
                if ref not in issue_recs:
                    _err(issues, f"reviews/{rid}", f"names issue {ref!r}, which does not "
                                                   f"exist in research/issues/")
            dup = ((rec.get("review") or {}).get("assessment") or {}).get("duplicate_of")
            if dup and dup not in reviews:
                _err(issues, f"reviews/{rid}", f"assessment.duplicate_of names review "
                                               f"{dup!r}, which does not exist")

    for iid, rec in sorted(issue_recs.items()):
        if not isinstance(rec, dict):
            continue
        block = rec.get("issue") or {}
        _check_review_target(rec, iid, protocols, releases, reviews, issue_recs,
                             obs_records, issues, f"issues/{iid}", block.get("target"))
        # Every review an issue names must exist, and the aggregation edge must
        # agree from both ends where both ends wrote it: a review claiming an
        # issue that does not list it is the half-written edge again.
        for field in ("raised_by", "supporting", "disputing", "response"):
            for ref in block.get(field) or []:
                if isinstance(ref, str) and ref not in reviews:
                    _err(issues, f"issues/{iid}", f"{field} names {ref!r}, which is not a "
                                                  f"review in research/reviews/")
        named_here = {r for f in ("raised_by", "supporting", "disputing", "response")
                      for r in (block.get(f) or []) if isinstance(r, str)}
        for rid, rrec in reviews.items():
            if iid in (((rrec or {}).get("review") or {}).get("issues") or []):
                if rid not in named_here:
                    _err(issues, f"issues/{iid}", f"review {rid!r} names this issue but the "
                                                  f"issue does not name it back in "
                                                  f"raised_by/supporting/disputing/response")
        # A resolution that points at a release version must point at one that
        # exists — otherwise "fixed in 1.1.0" is a claim nobody can follow.
        res = block.get("resolution") or {}
        rref = res.get("resulting_release")
        if isinstance(rref, dict):
            pair = (rref.get("ref"), rref.get("version"))
            if pair not in releases:
                _err(issues, f"issues/{iid}.resolution", f"resulting_release {pair[0]!r} "
                     f"version {pair[1]!r} does not exist")
    return issues


def _check_evidence_join(rel, rid, version, obs_records, issues):
    """A release's evidence ref resolves, AND the record names the release back.

    Both directions, because a half-written edge is the worst of the three
    states: it reads as a working link from whichever side you happen to
    arrive on, and only a reader who checks the other side ever finds out."""
    key = f"releases/{rid}/{version}"
    for i, e in enumerate(rel.get("evidence") or []):
        if not isinstance(e, dict):
            continue
        ref = str(e.get("ref") or "")
        m = EVIDENCE_REF_RE.match(ref)
        if not m:
            continue
        study_key, obs_id = m.group(1), m.group(2)
        rec = obs_records.get(study_key)
        if not isinstance(rec, dict):
            _err(issues, f"{key}.evidence[{i}]",
                 f"observations/{study_key}.yaml does not exist")
            continue
        ids = {o.get("id") for o in (rec.get("observations") or []) if isinstance(o, dict)}
        if obs_id not in ids:
            _err(issues, f"{key}.evidence[{i}]",
                 f"observations/{study_key}.yaml has no observation {obs_id!r} "
                 f"(it has: {', '.join(sorted(str(i) for i in ids)) or 'none'})")
            continue
        named = (rec.get("study") or {}).get("release") or {}
        if named.get("ref") != rid:
            _err(issues, f"{key}.evidence[{i}]",
                 f"observations/{study_key}.yaml does not name this release back "
                 f"(study.release.ref is {named.get('ref')!r}, expected {rid!r}) — "
                 f"an edge written from one side only reads as working from that side")


def _check_analysis_refs(rec, study_key, release, issues):
    """An observation's `analysis_ref` names an analysis the release declares.

    This is the link that makes "why does the wiki believe this" reach the
    code rather than stopping at a citation."""
    declared = {a.get("id") for a in (release or {}).get("analyses") or []
                if isinstance(a, dict)}
    for o in rec.get("observations") or []:
        if not isinstance(o, dict):
            continue
        ref = o.get("analysis_ref")
        if ref and ref not in declared:
            _err(issues, f"observations/{study_key}/{o.get('id')}",
                 f"analysis_ref {ref!r} names no analysis in the release it cites "
                 f"({', '.join(sorted(str(d) for d in declared)) or 'none declared'})")


def _check_review_target(rec, rid, protocols, releases, reviews, issue_recs,
                        obs_records, issues, key, target):
    """A review or issue must point at something that exists, at the version it
    read. Shared by both, because "the thing you are talking about" is the same
    question whichever object is asking it."""
    if not isinstance(target, dict):
        return
    kind, ref, version = target.get("kind"), target.get("ref"), target.get("version")
    if kind == "protocol" and (ref, version) not in protocols:
        _err(issues, key, f"target protocol {ref!r} version {version!r} does not exist")
    elif kind == "release" and (ref, version) not in releases:
        _err(issues, key, f"target release {ref!r} version {version!r} does not exist")
    elif kind == "review" and ref not in reviews:
        _err(issues, key, f"target review {ref!r} does not exist")
    elif kind == "issue" and ref not in issue_recs:
        _err(issues, key, f"target issue {ref!r} does not exist")
    elif kind == "claim" and not (WIKI_ROOT / "claims" / f"{ref}.md").is_file():
        _err(issues, key, f"target claim claims/{ref}.md does not exist")
    elif kind in RELEASE_LOCAL_KINDS:
        # <release-id>/<version>/<local-id>, resolved inside the release that
        # declares it. Neither analyses nor datasets are files of their own yet.
        parts = str(ref or "").split("/")
        if len(parts) != 3:
            _err(issues, key, f"target {kind} ref {ref!r} must be "
                              f"'<release-id>/<version>/<{kind}-id>'")
            return
        rel = releases.get((parts[0], parts[1]))
        if not isinstance(rel, dict):
            _err(issues, key, f"target {kind} names release {parts[0]!r} version "
                              f"{parts[1]!r}, which does not exist")
            return
        declared = {d.get("id") for d in rel.get(RELEASE_LOCAL_KINDS[kind]) or []
                    if isinstance(d, dict)}
        if parts[2] not in declared:
            _err(issues, key, f"release {parts[0]}/{parts[1]} declares no {kind} "
                              f"{parts[2]!r} (it has: "
                              f"{', '.join(sorted(str(d) for d in declared)) or 'none'})")
    elif kind == "evidence":
        m = EVIDENCE_REF_RE.match(str(ref or ""))
        if not m:
            _err(issues, key, f"target evidence ref {ref!r} must be "
                              f"'<study-key>/<observation-id>'")
            return
        study_key, obs_id = m.group(1), m.group(2)
        obs = obs_records.get(study_key)
        ids = {o.get("id") for o in (obs or {}).get("observations") or []
               if isinstance(o, dict)} if isinstance(obs, dict) else set()
        if obs_id not in ids:
            _err(issues, key, f"target evidence {ref!r} does not resolve in observations/")
