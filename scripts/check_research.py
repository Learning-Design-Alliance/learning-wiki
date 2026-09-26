#!/usr/bin/env python3
"""
check_research.py — validate the research layer, and read it back.

    python3 scripts/check_research.py            # validate; exit 1 on any problem
    python3 scripts/check_research.py --summary  # what is in the store, by shape
    python3 scripts/check_research.py --why <claim-slug>
    python3 scripts/check_research.py --issues   # open and resolved issues

The same validation runs inside `lint.py` (`--type research`), so this script
is for working on one object with full output rather than for CI. It is safe to
run with nothing in research/ at all: an empty layer is valid, which keeps
CLAUDE.md's "a count of zero means the work is done" property intact.

`--why` is the acceptance test run as a command. The question the layer exists
to answer is *why does the wiki believe claim X*, and the answer has to reach
past the citation to the analysis, the dataset, the release and the governance
the data was collected under — from the records alone, reading no prose.
"""

import argparse
import sys
from datetime import date
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import research_lib as rl
import observation_lib as ol


def _fmt_result(result: dict) -> str:
    if not isinstance(result, dict):
        return "no result"
    mt = result.get("measure_type", "?")
    est = result.get("estimate")
    out = f"{mt}" if est is None else f"{mt} = {est}"
    if result.get("ci_lower") is not None:
        out += f" [{result['ci_lower']}, {result['ci_upper']}]"
    if result.get("k"):
        out += f", k = {result['k'].get('value')} {result['k'].get('unit')}"
    return out


def why(claim_slug: str) -> int:
    """Traverse claim <- evidence <- analysis <- dataset <- release <- protocol."""
    if not (rl.WIKI_ROOT / "claims" / f"{claim_slug}.md").is_file():
        # A merged or renamed claim answers to its old slug as an alias
        # (merge_claims.py, update_links_for_renames.py); follow it.
        import json
        try:
            idx = json.loads((rl.WIKI_ROOT / "wiki-index.json").read_text(encoding="utf-8"))
            target = idx["resolve"].get("claim", {}).get(claim_slug)
        except (OSError, ValueError, KeyError):
            target = None
        if not target:
            print(f"no claims/{claim_slug}.md", file=sys.stderr)
            return 1
        print(f"{claim_slug} is an alias of {target}")
        claim_slug = target
    obs_records, _ = ol.load_all()
    releases, _ = rl.load_releases()
    protocols, _ = rl.load_protocols()
    reviews, _ = rl.load_reviews()
    issue_recs, _ = rl.load_issues()

    print(f"claim: {claim_slug}\n")

    cited = [(k, r) for k, r in sorted(obs_records.items())
             if any((a or {}).get("claim") == claim_slug
                    for a in (r or {}).get("appears_in") or [])]
    if not cited:
        print("  No structured evidence record names this claim.")
        print("  (That is a normal state: 424 claim pages have no record. The page's")
        print("   own ## Evidence section is the argument; this store is the")
        print("   configuration that argument rests on, where anyone has written it.)")
        return 0

    for study_key, rec in cited:
        study = rec.get("study") or {}
        prov = rec.get("provenance") or {}
        edge = next(a for a in rec["appears_in"] if a.get("claim") == claim_slug)
        source_type = prov.get("source_type")
        banner = ""
        if source_type != "research":
            # Loud, because this is the field that separates a finding from a
            # simulation, a model's proposal and a platform's own telemetry. A
            # reader who misses it pools the wrong rows.
            banner = f"   << NOT A PUBLISHED FINDING: source_type = {source_type} >>"
        print(f"  [{edge.get('bearing', '?')}] {study_key}{banner}")
        if edge.get("anchor"):
            print(f"      written into the claim's argument at "
                  f"### anchor {edge['anchor']!r}")
        else:
            print("      recorded against the claim but not written into its "
                  "argument (no anchor)")
        design = (study.get("design") or {}).get("family")
        print(f"      design: {design}")

        release_ref = study.get("release")
        release = None
        if isinstance(release_ref, dict):
            pair = (release_ref.get("ref"), release_ref.get("version"))
            release = releases.get(pair)
            print(f"      release: {pair[0]}@{pair[1]}")
            if isinstance(release, dict):
                r = release.get("release") or {}
                print(f"        question: {' '.join(str(r.get('question','')).split())}")
                current = rl.latest(v for (i, v) in releases if i == pair[0])
                if current and current != pair[1]:
                    print(f"        NOTE: {pair[0]} is now at {current}; this evidence "
                          f"was produced by {pair[1]} and stays attached to it")
        elif study.get("citation"):
            print(f"      source: {' '.join(str(study['citation']).split())[:100]}")

        analyses = {a.get("id"): a for a in (release or {}).get("analyses") or []
                    if isinstance(a, dict)}
        datasets = {d.get("id"): d for d in (release or {}).get("datasets") or []
                    if isinstance(d, dict)}
        for o in rec.get("observations") or []:
            if not isinstance(o, dict):
                continue
            out = o.get("outcome") or {}
            print(f"      - {o.get('id')}: {out.get('construct')} "
                  f"-> {_fmt_result(o.get('result'))}")
            gaps = [f"{k}: {v}" for k, v in (o.get("observability") or {}).items()
                    if v != "observed"]
            if gaps:
                print(f"          not fully observed: {', '.join(sorted(gaps))}")
            a = analyses.get(o.get("analysis_ref"))
            if a:
                code = a.get("code") or {}
                print(f"          analysis: {a.get('id')} — {code.get('repo')} "
                      f"@{str(code.get('commit'))[:12]} {code.get('path')}")
                for dep in a.get("inputs") or []:
                    d = datasets.get(dep) or {}
                    loc = d.get("location") or {}
                    print(f"          dataset:  {dep} ({d.get('grain')}) "
                          f"{loc.get('kind')}:{loc.get('ref')}")
                    print(f"                    sha256 {str(d.get('sha256'))[:16]}…  "
                          f"{d.get('identifiability')} / access {d.get('access')}")

        proto = (release or {}).get("protocol")
        if isinstance(proto, dict):
            p = protocols.get((proto.get("ref"), proto.get("version"))) or {}
            consent = p.get("consent") or {}
            ext = p.get("external_review") or {}
            print(f"      protocol: {proto.get('ref')}@{proto.get('version')}")
            print(f"        consent {consent.get('mechanism')}; secondary use "
                  f"{consent.get('secondary_research_use')}; AI processing disclosed "
                  f"{consent.get('ai_processing_disclosed')}")
            print(f"        external review: {ext.get('status')}"
                  f"{' — ' + str(ext.get('approval_id')) if ext.get('approval_id') else ''}")

        # What anybody has said about any of it.
        targets = {("evidence", f"{study_key}/{o.get('id')}")
                   for o in rec.get("observations") or [] if isinstance(o, dict)}
        if isinstance(release_ref, dict):
            targets.add(("release", release_ref.get("ref")))
        targets.add(("claim", claim_slug))
        related = _reviews_for(reviews, targets) | _issues_for(issue_recs, targets)
        if related:
            print(f"      contested by: {', '.join(sorted(related))}")
        print()
    return 0


def _reviews_for(reviews, targets) -> set:
    out = set()
    for rid, rec in reviews.items():
        t = ((rec or {}).get("review") or {}).get("target") or {}
        if (t.get("kind"), t.get("ref")) in targets:
            out.add(f"review {rid}")
    return out


def _issues_for(issue_recs, targets) -> set:
    out = set()
    for iid, rec in issue_recs.items():
        block = (rec or {}).get("issue") or {}
        t = block.get("target") or {}
        if (t.get("kind"), t.get("ref")) in targets:
            out.add(f"issue {iid} ({block.get('state')})")
    return out


def issues_report() -> None:
    issue_recs, _ = rl.load_issues()
    reviews, _ = rl.load_reviews()
    if not issue_recs:
        print("No issues recorded.")
        return
    for iid, rec in sorted(issue_recs.items()):
        b = (rec or {}).get("issue") or {}
        t = b.get("target") or {}
        print(f"{b.get('state','?'):<11} {iid}")
        print(f"            {t.get('kind')} {t.get('ref')}"
              f"{'@' + t.get('version') if t.get('version') else ''} "
              f"[{b.get('category')}]")
        print(f"            {' '.join(str(b.get('summary','')).split())}")
        counts = {f: len(b.get(f) or []) for f in
                  ("raised_by", "supporting", "disputing", "response")}
        # The whole point of the object, printed: N people, one problem.
        print(f"            {counts['raised_by']} independent identification(s), "
              f"{counts['supporting']} supporting, {counts['disputing']} disputing, "
              f"{counts['response']} response(s)")
        first = (b.get("raised_by") or [None])[0]
        if first:
            when = ((reviews.get(first) or {}).get("review") or {}).get("created_at")
            print(f"            first identified by {first} ({when})")
        res = b.get("resolution") or {}
        if res:
            rr = res.get("resulting_release") or {}
            print(f"            resolution: {res.get('outcome')} "
                  f"(asserted by {res.get('decided_by')})"
                  f"{' -> ' + rr.get('ref') + '@' + rr.get('version') if rr else ''}")
        print()


def crosswalk() -> int:
    """Print the pipeline crosswalk, and fail if any of its values is unmapped.

    The row-level governance vocabulary in learning-engine-ai-frontend
    (`experiments/learning-graph`) and this layer's protocol-level one have to
    be relatable, or the two publication gates can disagree without anybody
    noticing. A crosswalk written in a document rots; this one is executable,
    and it exits 1 the moment the other side grows a value nothing maps."""
    gaps = 0
    print("identifiability — pipeline row value -> this layer's protocol value\n")
    for v in rl.PIPELINE_IDENTIFIABILITY:
        mapped, note = rl.identifiability_from_pipeline(v)
        if mapped is None:
            gaps += 1
        print(f"  {v:<16} -> {str(mapped):<16} {note}")

    print("\nsource_type — pipeline row value -> this layer's record kind\n")
    for v in rl.PIPELINE_SOURCE_TYPES:
        mapped, note = rl.source_type_from_pipeline(v)
        if mapped is None and v != "human":
            gaps += 1
        print(f"  {v:<16} -> {str(mapped):<16} {note}")
    # Shown explicitly, because `human` resolving to None is the CORRECT answer
    # to a question the row cannot settle, not a gap in the table.
    for flag in (False, True):
        mapped, note = rl.source_type_from_pipeline("human", assigned_conditions=flag)
        print(f"  human, assigned_conditions={str(flag):<5} -> {mapped:<22} {note}")

    print("\nNot a collision, and worth being clear about: the two `source_type`")
    print("fields answer different questions. The pipeline's says what produced a")
    print("ROW; this layer's says what KIND of record it is. Only `research` is the")
    print("same value in both. Renaming either would destroy information, which is")
    print("why this is a mapping rather than an alignment.")
    print("\n`pseudonymised` IS a settled collision: this layer moved to the")
    print("pipeline's spelling. See IDENTIFIABILITY in scripts/research_lib.py.")

    if gaps:
        print(f"\n{gaps} pipeline value(s) have no mapping — the vocabularies have "
              f"drifted.", file=sys.stderr)
        return 1
    print("\nEvery pipeline value maps, or says why it cannot. 0 gaps.")
    return 0


def summary() -> None:
    protocols, _ = rl.load_protocols()
    releases, _ = rl.load_releases()
    studies, _ = rl.load_studies()
    reviews, _ = rl.load_reviews()
    issue_recs, _ = rl.load_issues()
    obs_records, _ = ol.load_all()

    by_obj = defaultdict(list)
    for (oid, v) in protocols:
        by_obj[("protocol", oid)].append(v)
    for (oid, v) in studies:
        by_obj[("study", oid)].append(v)
    for (oid, v) in releases:
        by_obj[("release", oid)].append(v)
    print(f"{len({k for k, _ in protocols})} protocol(s), "
          f"{len({k for k, _ in studies})} study plan(s), "
          f"{len({k for k, _ in releases})} release(s), "
          f"{len(reviews)} review(s), {len(issue_recs)} issue(s).\n")

    for (kind, oid), versions in sorted(by_obj.items()):
        print(f"  {kind} {oid}: {', '.join(sorted(versions, key=rl.semver))} "
              f"(current: {rl.latest(versions)})")
    print()

    linked = [k for k, r in obs_records.items()
              if isinstance((r or {}).get("study", {}).get("release"), dict)]
    print(f"  {len(linked)} observation record(s) produced by a release of ours; "
          f"{len(obs_records) - len(linked)} from sources we read.")

    bearings = Counter(a.get("bearing") for r in obs_records.values()
                       for a in (r or {}).get("appears_in") or [])
    anchored = sum(1 for r in obs_records.values()
                   for a in (r or {}).get("appears_in") or [] if a.get("anchor"))
    total_edges = sum(bearings.values())
    print(f"  {total_edges} evidence->claim edge(s): "
          f"{', '.join(f'{v} {k}' for k, v in bearings.most_common())}")
    print(f"  {anchored} of them written into a claim's argument; "
          f"{total_edges - anchored} recorded but not promoted.\n")

    types = Counter(((r or {}).get("review") or {}).get("review_type")
                    for r in reviews.values())
    bases = Counter(b for r in reviews.values()
                    for b in (((r or {}).get("review") or {}).get("author") or {}).get("basis") or [])
    moderated = [rid for rid, r in reviews.items()
                 if any(m.get("state") != "visible"
                        for m in ((r or {}).get("review") or {}).get("moderation") or [])]
    for label, counter in (("review type", types), ("contribution basis", bases)):
        print(f"  {label}")
        for k, v in counter.most_common():
            print(f"    {v:>4}  {k}")
        print()
    print(f"  {len(moderated)} review(s) carry a moderation action "
          f"{'(' + ', '.join(sorted(moderated)) + ')' if moderated else ''}")

    states = Counter(((r or {}).get("issue") or {}).get("state") for r in issue_recs.values())
    print(f"  issue state: " + ", ".join(f"{v} {k}" for k, v in states.most_common()))

    # Synthetic and model-proposed records, named. The store must never make a
    # simulation indistinguishable from a finding at a glance.
    synthetic = sorted(k for k, r in obs_records.items()
                       if ((r or {}).get("provenance") or {}).get("source_type") != "research")
    if synthetic:
        print(f"\n  NOT PUBLISHED FINDINGS ({len(synthetic)}): {', '.join(synthetic)}")


STUDY_STUB = """\
# ============================================================================
# STUDY PLAN — written BEFORE the data exists, and before the release reports it.
#
# Write it to  research/studies/{sid}/{version}.yaml  and commit it before
# collection opens. The commit date in a public repository is the only evidence
# that this preceded the data, so a plan committed afterwards plans nothing.
#
# Every marker below must be answered before this validates: `check_research.py`
# refuses a file still carrying one. That is the point of the stub — the
# mechanical half is filled in, and the half that needs a decision is BLOCKED
# rather than quietly defaulted. (The check scans raw text including comments,
# so this header deliberately avoids spelling the marker out.)
#
# The findings become a RELEASE naming this plan back through `study: {{ref,
# version}}`. Then:
#
#   python3 scripts/check_research.py --deviations {sid}
#
# prints what the release ran that this plan does not declare.
#
# A plan is NOT a publication, which is why it is this object and not a release:
# a release is refused under a protocol whose `permitted_uses` prohibits
# research-publication, and an internal validation study has to be plannable
# under exactly such a protocol.
# ============================================================================

schema_version: {schema_version}

study:
  id: {sid}
  version: {version}
  title: >-
    TODO one line naming what is being investigated
  status: planned
  effective_from: {today}
  # The QUESTION, not the expected answer.
  question: >-
    TODO the question this study is asking, in one sentence
  background: >-
    TODO what is already known, and what this adds. Two or three sentences

protocol:
  ref: TODO protocol id under research/protocols/
  version: TODO

design:
  # One of: {design_families}
  family: TODO
  detail: >-
    TODO what is manipulated, what is held constant, and what differs by arm
  allocation: >-
    TODO how participants reach conditions, and the unit randomised if it
    differs from the unit analysed
  preregistration:
    # Whether this plan is ALSO deposited with an external registry. The
    # guarantee here is git commit history in a public repo, which is real and
    # weaker than a third-party timestamp.
    registered: false
    note: TODO or name the registry and identifier

setting:
  conducted_where: TODO
  recruitment_sites: TODO
  resources:
    staff:
      - TODO who conducts this, and at what commitment
    investigator_time: TODO
    participant_support: TODO what support exists if a participant needs it

enrolment:
  planned: {{value: TODO, unit: TODO}}   # a count carries its unit
  justification: >-
    TODO why this number: the effect it is powered to detect, and at what
    assumed variance. This is also where the STOPPING RULE has to be stated,
    before the data can influence it
  # A mapping per class, never a bare `none`: the protocol ceiling is checked
  # per class, and "which ones" is what a scalar cannot answer.
  special_populations:
    minors: TODO           # included | excluded | not-addressed
    adults-unable-to-consent: TODO
    pregnant-women: TODO
    prisoners: TODO

timelines:
  participation_duration: TODO
  enrolment_period: TODO
  estimated_completion: TODO

procedures:
  steps:
    - TODO what actually happens, in order
  instruments:
    - TODO every instrument administered
  data_quality:
    procedures:
      - TODO what is checked, and what happens to data that fails the check

endpoints:
  # A primary endpoint IS the hypothesis. At least one is required.
  - name: TODO
    role: primary
    measure: TODO exactly what is measured, and how it is computed
    timepoint: TODO when
    # THE FIELD THAT MAKES A PLAN WORTH WRITING. Without a result that would
    # count against the prediction, every outcome can be narrated afterwards as
    # a success and the plan is a timestamp on a wish.
    prespecified_prediction:
      prediction: >-
        TODO what is expected, with a direction and a magnitude
      disconfirming_result: >-
        TODO what result would count as this prediction FAILING. Specific
        enough that somebody else could apply it to the output without asking

  # Declaring an endpoint exploratory IN ADVANCE is the half people forget, and
  # the half that protects the work: it is what stops a striking result here
  # being written up later as though it had been predicted. A prediction on an
  # `exploratory` endpoint is refused. Delete this block if there is none.
  - name: TODO
    role: exploratory
    measure: TODO
    timepoint: TODO

analysis_plan:
  approach: >-
    TODO the analysis as planned. The release's `analyses` records what was
    actually run, and the difference between the two is the point
  tests:
    - TODO each statistical test, named
  missing_data: TODO how dropout and missingness are handled
  multiplicity: TODO adjustment across endpoints, or why none

benefits:
  to_participants: TODO    # none-to-participants | ...
  detail: TODO

participant_burden:
  costs: TODO
  detail: TODO

results_sharing:
  policy: TODO     # aggregate-to-participants | individual-to-participants
                   # | none | not-determined
  detail: TODO

community_involvement:
  involved: TODO
  detail: TODO whether the people affected shaped this, or did not

determination:
  # `not-sought` | `pending` need nothing further. Anything beyond them requires
  # an authority and a `determined_by` that is human:<id> or org:<id> — a
  # machine may compute conformance and may never record a determination.
  status: not-sought

provenance:
  authors:
    - id: TODO human:<id> or <tool>/unspecified
      role: TODO
  source_type: TODO      # {source_types}
  created_at: {today}
  verification: unverified
"""


def stub_study(study_id: str) -> int:
    """Print a study-plan skeleton: mechanical parts filled, the rest blocked.

    Same strategy as `check_observations.py --stub`, and the same reason. What a
    plan needs that nobody can generate — the question, the prediction, the
    result that would disconfirm it, the stopping rule — is exactly what is left
    as a marker, and the validator refuses the file while any remains."""
    if not rl.ID_RE.match(study_id):
        print(f"{study_id!r} is not a valid study id (lowercase, hyphenated)",
              file=sys.stderr)
        return 1
    studies, _ = rl.load_studies()
    existing = sorted(v for (sid, v) in studies if sid == study_id)
    if existing:
        # Refuse rather than print. A plan is immutable once committed, and a
        # new version of one is a deliberate act — the schema treats a status
        # transition or a material change as a version bump precisely so it
        # invalidates the conformance result computed against the old one.
        print(f"study {study_id} already exists at {', '.join(existing)}. A plan is "
              f"immutable once committed; write the next version by hand and say in "
              f"`change_note` what changed and why.", file=sys.stderr)
        return 1
    print(STUDY_STUB.format(
        sid=study_id, version="1.0.0", schema_version=rl.SCHEMA_VERSION,
        today=date.today().isoformat(),
        design_families=" | ".join(sorted(rl.DESIGN_FAMILIES)),
        source_types=" | ".join(sorted(rl.SOURCE_TYPES)),
    ))
    return 0


def deviations(study_id: str) -> int:
    """What the release ran that the plan did not declare.

    The comparison this schema describes in prose as "exactly what
    preregistration exists to police", run as a command. It REPORTS rather than
    judges: an analysis added after the data is usually a reviewer's question
    being answered, which is what the spaced-review fixture shows at 1.1.0. What
    would be a problem is that analysis appearing with nothing to say it arrived
    late, which is why `prespecified` is required on every one."""
    studies, serrs = rl.load_studies()
    releases, rerrs = rl.load_releases()
    for e in list(serrs) + list(rerrs):
        print(f"  {e}", file=sys.stderr)

    versions = sorted((v for (sid, v) in studies if sid == study_id), key=rl.semver)
    if not versions:
        print(f"no study {study_id!r} under research/studies/", file=sys.stderr)
        return 1
    plan = studies[(study_id, versions[-1])] or {}
    print(f"study {study_id} {versions[-1]} "
          f"(effective {(plan.get('study') or {}).get('effective_from')})")

    endpoints = [e for e in (plan.get("endpoints") or []) if isinstance(e, dict)]
    for e in endpoints:
        pred = e.get("prespecified_prediction") or {}
        mark = "predicted" if pred else "no prediction"
        print(f"  endpoint [{e.get('role')}] {e.get('name')}  ({mark})")

    reporting = sorted(
        ((rid, v) for (rid, v), r in releases.items()
         if isinstance(r, dict) and (r.get("study") or {}).get("ref") == study_id),
        key=lambda p: rl.semver(p[1]))
    if not reporting:
        print("  no release reports this plan yet.")
        return 0

    for rid, v in reporting:
        rel = releases[(rid, v)]
        named = (rel.get("study") or {}).get("version")
        print(f"  release {rid} {v} "
              f"({(rel.get('release') or {}).get('released_at')}):")
        lines = []
        if named and named != versions[-1]:
            lines.append(f"    reports plan {named}, not the latest {versions[-1]}")
        for a in rel.get("analyses") or []:
            if not isinstance(a, dict):
                continue
            if a.get("prespecified") is False:
                lines.append(f"    + {a.get('id')}  run but not in the plan")
            elif a.get("prespecified") is not True:
                lines.append(f"    ? {a.get('id')}  does not say whether it was planned")
        # An endpoint declared and then not reported is the quieter failure and
        # the one a reader cannot detect from the release alone — but it is only
        # answerable where the release DECLARES which endpoint each analysis
        # reports. The first draft inferred it from word overlap between endpoint
        # names and analysis titles, and immediately reported an endpoint as
        # unreported on a release that reports it. Absent means not established.
        covered = {r for a in rel.get("analyses") or [] if isinstance(a, dict)
                   for r in (a.get("endpoint_refs") or [])}
        if covered:
            for e in endpoints:
                if e.get("name") not in covered:
                    lines.append(f"    - endpoint {e.get('name')!r} [{e.get('role')}] "
                                 f"declared, no analysis here reports it")
        else:
            lines.append("    (endpoint coverage not checkable: no analysis declares "
                         "endpoint_refs)")
        for ln in lines or ["    no deviation from the plan"]:
            print(ln)
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true",
                    help="describe the layer rather than validating it")
    ap.add_argument("--issues", action="store_true", help="list issues and their state")
    ap.add_argument("--crosswalk", action="store_true",
                    help="the governance-vocabulary crosswalk to the Lazuli pipeline's "
                         "row-level fields; exits 1 if a value there is unmapped")
    ap.add_argument("--stub-study", metavar="STUDY_ID",
                    help="print a study-plan skeleton: mechanical fields filled, "
                         "everything needing a decision left as a marker the validator "
                         "refuses until answered")
    ap.add_argument("--deviations", metavar="STUDY_ID",
                    help="compare a study plan with the release(s) reporting it: "
                         "analyses run but not planned, and endpoints declared but not "
                         "reported")
    ap.add_argument("--why", metavar="CLAIM_SLUG",
                    help="traverse claim <- evidence <- analysis <- dataset <- "
                         "release <- protocol")
    args = ap.parse_args()

    if args.stub_study:
        sys.exit(stub_study(args.stub_study))
    if args.deviations:
        sys.exit(deviations(args.deviations))
    if args.why:
        sys.exit(why(args.why))
    if args.crosswalk:
        sys.exit(crosswalk())
    if args.issues:
        issues_report()
        return
    if args.summary:
        summary()
        return

    problems = rl.validate_all()
    if not problems:
        protocols, _ = rl.load_protocols()
        studies, _ = rl.load_studies()
        releases, _ = rl.load_releases()
        reviews, _ = rl.load_reviews()
        issue_recs, _ = rl.load_issues()
        print(f"research/: {len(protocols)} protocol version(s), {len(studies)} study "
              f"version(s), {len(releases)} release version(s), {len(reviews)} "
              f"review(s), {len(issue_recs)} issue(s), 0 issues.")
        return
    print(f"{len(problems)} problem(s):", file=sys.stderr)
    for p in problems:
        print(f"  {p}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
