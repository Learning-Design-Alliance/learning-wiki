#!/usr/bin/env python3
"""
check_observations.py — validate observations/*.yaml against the schema.

    python3 scripts/check_observations.py            # report, exit 1 on any problem
    python3 scripts/check_observations.py --summary  # what is in the store, by shape

The same checks run inside `lint.py` (`--type observations`), so this script
is for working on one file with full output rather than for CI. It is safe to
run with no observation files at all: an empty store is valid.
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import observation_lib as ol


STUB_TEMPLATE = """# TODO: {key} — draft observation record.
#
# Everything below marked TODO must come from the SOURCE, not from this file's
# own guesses and not from the claim page's paraphrase. Delete any TODO block
# you cannot fill from the article; an omitted field says "not established",
# which is honest, while a filled-in plausible one is a fabrication.
#
# Then: python3 scripts/check_observations.py

schema_version: 1

study:
  key: {key}
  citation: "{citation}"
  doi: {doi}
  design:
    # TODO one of: randomized-controlled-trial quasi-experimental observational
    #              longitudinal qualitative mixed-methods meta-analysis
    #              systematic-review simulation other
    # NEVER infer a stronger design than the source states.
    family: TODO
    design_detail: TODO

provenance:
  source_type: research
  extracted_by: TODO            # e.g. claude/unspecified, human:david
  extracted_at: {today}
  extraction_method: TODO       # SAY WHAT WAS READ: manual-from-publisher-fulltext,
                                # manual-from-publisher-abstract, manual-from-wiki-claim-page
  verification: unverified

appears_in:
{appears_in}
population:
  n:                            # integer, or omit the field
  description: TODO
  age_or_stage:
  prior_knowledge:
  language_background:
  relevant_characteristics: []

context:
  setting: TODO
  institution_or_environment:
  geography:
  delivery_mode:
  duration:

intervention:
  description: TODO             # write "None. ..." for an observational study
  elements: []                  # - term: "the source's own words"
                                #   anchors: []   # bundle paths that resolve on disk

comparisons:
  # "none" is a VALUE, not an omission — a single-group study records the
  # absence of a control arm here rather than by leaving the list empty.
  - id: TODO
    kind: TODO                  # between-groups within-subject-baseline historical none other
    description: TODO
    elements: []

observations:
  # One per (outcome x timepoint). Two timepoints of one outcome are TWO
  # observations, because an immediate effect and a delayed one are different
  # observations and collapsing them destroys the finding.
  - id: TODO
    outcome:
      construct: TODO
      source_language: TODO     # the author's own wording, preserved
      measure:
      scale:
      direction: TODO           # higher-is-better lower-is-better contextual
      role: TODO                # capability-evidence proximal-outcome intermediate-outcome
                                # distal-outcome organizational-outcome
                                # learner-characteristic other
      role_basis: TODO          # stated inferred ambiguous
      valued_by: []             # ONLY where the source identifies who values it
      anchors: []
    time:
      label: TODO
      offset:
        value: 0
        unit: weeks
        from: TODO
    comparison_ref: TODO
    result:
      measure_type: TODO        # the ONLY required field here — an unquantified
                                # relationship is still a valid observation
      estimate:
      p_value:
    moderators:
      reported: []              # each entry needs variable, relationship AND source_quote
      candidate: []
    observability:
      population_detail: TODO   # observed partial unreported
      implementation_detail: TODO
      outcome_timing: TODO
      effect_size: TODO
    source_quote: TODO
    source_location: TODO
"""


def stub(claim_slug: str) -> int:
    """Print a skeleton record for a claim, pre-filled with what IS mechanical.

    The citation, DOI and the claim/anchor join come off the page and are
    always right. Everything the source alone can answer is left as TODO and
    the validator refuses the file until it is gone — which is the whole
    migration strategy in one command: cheap where it is mechanical, blocked
    where it is not."""
    sys.path.insert(0, str(Path(__file__).parent))
    import okf_lib as ok
    from datetime import date

    path = ol.WIKI_ROOT / "claims" / f"{claim_slug}.md"
    if not path.is_file():
        print(f"no claims/{claim_slug}.md", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    fm_lines, body = ok.split_frontmatter(text)
    fm = ok.parse_frontmatter_scalars(fm_lines)
    section = ok.get_section(body, "Evidence") or ""
    entries = ol.parse_evidence_for_stub(section)
    if not entries:
        print(f"claims/{claim_slug}.md has no '### ' evidence entries to build from",
              file=sys.stderr)
        return 1

    # One study per evidence anchor. A claim citing two studies produces two
    # stubs, because an observation file is keyed by STUDY, not by claim.
    for anchor, key, citation, doi in entries:
        print(STUB_TEMPLATE.format(
            key=key,
            citation=citation.replace('"', "'"),
            doi=f'"{doi}"' if doi else "null   # null is a VERDICT (none registered); "
                                       "delete the line if simply not established",
            today=date.today().isoformat(),
            appears_in=f"  - claim: {claim_slug}\n    anchor: {anchor}\n",
        ))
        print(f"# ---- write the block above to observations/{key}.yaml ----\n")
    return 0


def summary() -> None:
    records, errors = ol.load_all()
    for e in errors:
        print(f"  UNPARSEABLE {e}")
    n_obs = sum(len((r or {}).get("observations") or []) for r in records.values())
    print(f"{len(records)} study/studies, {n_obs} observation(s).\n")

    designs = Counter((r.get("study") or {}).get("design", {}).get("family")
                      for r in records.values())
    measures, roles, unreported = Counter(), Counter(), Counter()
    for r in records.values():
        for o in r.get("observations") or []:
            measures[(o.get("result") or {}).get("measure_type")] += 1
            roles[(o.get("outcome") or {}).get("role")] += 1
            for k, v in (o.get("observability") or {}).items():
                if v in ("unreported", "partial"):
                    unreported[f"{k}: {v}"] += 1

    for label, counter in (("design family", designs), ("result measure_type", measures),
                           ("outcome role", roles), ("known gaps", unreported)):
        print(f"  {label}")
        for k, v in counter.most_common():
            print(f"    {v:>4}  {k}")
        print()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true",
                    help="describe the store rather than validating it")
    ap.add_argument("--stub", metavar="CLAIM_SLUG",
                    help="print a skeleton record for a claim, pre-filled with the "
                         "citation, DOI and claim/anchor join, everything else TODO")
    args = ap.parse_args()

    if args.stub:
        sys.exit(stub(args.stub))

    if args.summary:
        summary()
        return

    issues = ol.validate_all()
    if not issues:
        records, _ = ol.load_all()
        n_obs = sum(len((r or {}).get("observations") or []) for r in records.values())
        print(f"observations/: {len(records)} study/studies, {n_obs} observation(s), 0 issues.")
        return
    print(f"{len(issues)} issue(s):", file=sys.stderr)
    for i in issues:
        print(f"  {i}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
