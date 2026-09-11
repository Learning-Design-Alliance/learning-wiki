# Research observations — schema (version 2)

> **Revised 2026-09-11** when the research layer landed (`research/SCHEMA.md`).
> Three additive fields — `study.release`, `observations[].analysis_ref` and a
> newly **required** `appears_in[].bearing` — and `appears_in[].anchor` became
> optional. The version stays 2: nothing about the three levels changed, and a
> file written before the revision fails loudly on the missing `bearing` rather
> than being read wrongly.

A claim page argues something. An **observation** records the configuration that
argument rests on.

`d = .78` is not a weight between two concepts. It is one measurement, of one
configuration, on one population, against one comparison, at one point in time.

```
intervention/configuration + population + context + comparison + measurement + time
    → observed outcome/effect
```

> Field reference below. The rationale, and the reading of the existing code that
> produced it, is in `scripts/observation_lib.py`.

---

## The governing rule

> **Put information at the lowest level at which it actually varies, and preserve
> observations at the grain at which the source actually reports them.**

That one rule explains every placement in this schema, and settles the questions
it got wrong first time round:

- **total corpus N** varies per study → `evidence_base`; **analysed N** varies per
  result → the observation;
- **`k`** varies per pooled estimate (9 for knowledge, 2 for surgical skills, from
  one corpus of 23) → the result;
- **arms and comparisons** vary per *contrast* rather than per study or per result
  → between the two;
- an arm has **no fixed role**, because whether it is the intervention or the
  comparator varies *by comparison* — see below;
- and a pooled estimate over heterogeneous comparators **stays one observation**,
  because that is the grain the source reports, with the heterogeneity recorded
  structurally rather than normalised into effects nobody measured.

---

## Why version 2: source, evidence base, observations

v1 had **two** levels — a `study` whose `population` / `context` / `intervention`
were assumed **singular**, and the observations under it. That middle assumption
is a *primary-study* assumption. It broke the moment a meta-analysis and a
three-arm trial were put through it, in nine places:

| # | Fact that had to be recorded | v1 slot |
|---|---|---|
| 1 | 23 studies pooled | `population.n` (an int meaning participants) |
| 2 | 3371 participants across those 23 | **none** — one int, two facts |
| 3 | 19/23 high-income, 3/23 upper-middle, 1/23 lower-middle | **none** — `population.description` flattens a distribution |
| 4 | Random-effects, RoB-2, GRADE, PRISMA, 8 databases, 85,755 screened | **none** |
| 5 | I² = 66%; GRADE moderate; no prediction interval | **none** |
| 6 | Subgroup analyses *attempted and precluded* | **none** — `unreported` loses the attempt, absent loses that anyone looked |
| 7 | k = 9 for knowledge, k = 2 for surgical skills, from a corpus of 23 | **none** — and k on the *study* is wrong for every observation in it |
| 8 | Three arms: baseline, unenhanced, enhanced | `intervention` (singular) |
| 9 | Comprehension analysed on 62 of 67 randomised | `population.n` (the study's, not the result's) |

So the levels are now **three**:

```
study          the SOURCE — what the report is, and by what method it produced
               results. `synthesis:` appears iff it pools other people's work.
evidence_base  what the results are ABOUT — who or what was counted, in what
               population and context, and the ARMS the source contrasts.
observations   the individual results — each naming one comparison of arms, at
               one time, on one outcome, with its own analysed sample.
```

### The abstraction that makes one schema fit both: arms + comparisons

A three-arm trial's *"unenhanced elaboration vs baseline"* and a meta-analysis's
*"spaced online education vs massed online education"* are **the same object** —
a contrast between two named configurations. The synthesis pools that contrast
across studies instead of measuring it once; the trial measures it once. Nothing
about a meta-analysis needed a parallel set of fields. It needed the middle layer
to stop assuming there was exactly one group of people.

**An arm carries no `role`, and no epistemic type.** The first draft gave it one
(`intervention` / `comparator` / `baseline` / `corpus-stratum`) and it was removed
on evidence: nothing read it, and it is not a property of an arm. In the three-arm
fixture, `unenhanced-elaboration` was declared `role: intervention` and is the
**reference** side of `enhanced-vs-unenhanced` — so whether an arm is the
intervention or the comparator **varies by comparison**, which is exactly where
`index_arm` / `reference_arm` already say it. A tag on the arm both duplicates and
contradicts that.

Nor does an arm need a type to mark a synthesis. The containing source already
says `design.family: meta-analysis`, and the arm's own `size: {value: 17, unit:
studies}` already says it is 17 studies rather than 17 people. **An arm is a named
configuration; what it means is read from where it sits.**

What replaced `role` is the invariant it was standing in for without enforcing:
**every arm must be named by at least one comparison.** An arm nothing is
contrasted with cannot be reached from any observation, and is dead data. A
within-subject comparison may name its index arm — "this configuration against its
own earlier state" — which is how a single-group study's one arm gets used.

A single-group study has one arm. An observational survey has `arms: []`. Neither
is a special case; both are the same mechanism with fewer arms.

### A heterogeneous comparator stays one observation

Either side of a comparison may name **more than one arm**:

```yaml
  - id: spaced-online-vs-heterogeneous-control
    kind: between-groups
    index_arm: spaced-online
    reference_arm:
      - massed-online
      - no-intervention
```

Martinengo et al. pool three studies of which two compared against massed online
education and one against no intervention. The paper reports **one** estimate, so
this is **one** observation — splitting it into per-comparator effects would
invent effects the source never reported. But "the comparator is two
configurations" is relational structure, so it is readable without parsing prose:
the compiler emits `reference_is_heterogeneous: true` alongside the resolved arms.

Per-study contribution counts (2 and 1) are deliberately **not** recorded. The
source does report them, but no use case yet needs that grain, and a field nobody
reads is a field that goes stale.

### Every count carries its unit

The corpus proved this necessary before either fixture was written. Its evidence
entries carry `n=18`, `n=30 studies`, `n=66 articles`, `n=N/A` and
`n=large (aggregated)` — **one field doing four jobs**, so nothing can read it.

Here a count is `{value, unit}` and `unit` is required. 23 studies and 3371
participants are two different facts about one synthesis and both are recorded —
`evidence_base.size` and `evidence_base.additional_sizes`.

### `k` belongs to the observation, not the study

The single clearest reason the middle layer had to stop being one thing.
Martinengo et al. pool **9** studies for knowledge, **3** for clinical behaviour
change and **2** for surgical skills, out of a corpus of **23**. A `k` on the
study would be wrong for every observation in it.

---

## The four epistemic states

Collapsing any pair of these is how a store fills with confident wrong numbers.

| state | written as | means |
|---|---|---|
| not established | field omitted | nobody has looked |
| unreported | `observability.<field>: unreported` | somebody read the source and it does not say |
| **attempted and precluded** | `study.synthesis.attempted_but_precluded` | the authors **tried** the analysis and could not complete it, with the reason |
| measured as null | an observation with a null result | the source looked and found no effect |

Martinengo et al. attempted subgroup analyses and publication-bias assessment and
were precluded by the number of studies and their heterogeneity. Recording that as
`unreported` loses the reason; recording it as absent loses the attempt.

---

## Two more distinctions the schema holds

**A capability is not a valued outcome.** `outcome.role` records which a dependent
variable appears to be; `outcome.role_basis` records whether the source *stated*
that or you *inferred* it; `outcome.source_language` keeps the author's own
construct wording regardless. `outcome.valued_by` is populated **only where the
source identifies who values an outcome** — a researcher measuring graduation does
not establish that anybody values graduation, so the field has no default.

**A research observation is not a design hypothesis.**

```
DESIGN HYPOTHESIS    "Goal A is intended to contribute to Outcome B."
RESEARCH OBSERVATION "Study S observed relationship R between configuration A
                      and Outcome B under population/context C."
```

A finding may later be offered as evidence for or against a logic-model edge, by
something that weighs it. **It does not become that edge here**, and there is no
field in which to write that it does. Every compiled record carries
`kind: research_observation` and `provenance.source_type`.

---

## Where the records live

`observations/<study-key>.yaml`, one file per study, keyed by the author-year key
`check_citations.py`, `authorities.ndjson` and `citation_worklist.py` already use.
A study we produced ourselves is keyed the same way and names its release in
`study.release`; two versions of one release that report different estimates are
two files, because an adjusted estimate is a different measurement and
overwriting the first would destroy what was published at the time.

**Not inside a claim's `sources[]` frontmatter**, for three reasons read out of the
code: that block is *derived* (`sync_evidence_codes.py --apply` rebuilds it through
`dump_frontmatter`, which emits only `id/resource/title/author/q/i/n`, and runs
inside the unattended batch chain); `check_source_entry_keys` holds a closed key
set there precisely to catch a rewrite landing on a YAML key; and a study is cited
by many claims, so a per-claim copy is the drift shape this repo has lost weeks to.

**`appears_in` is optional in v2.** v1 required it, which made the evidence layer
depend on the argument layer — a structured record of a real study is valid
evidence whether or not anyone has yet written an argument that appeals to it. The
ratchet stays where it belongs: a *listed* claim and anchor must still resolve, so
a rename fails lint rather than silently orphaning the record.
`check_observations.py --summary` reports records nothing cites.

---

## File shape

```yaml
schema_version: 2

study:                       # the SOURCE
  key:                       # required — equals the filename, lowercase ASCII
  citation:                  # required UNLESS `release:` is given
  release: {ref, version}    # the source is a research RELEASE of ours rather than
                             # a paper we read (research/releases/<ref>/<version>).
                             # It replaces `citation` — a release already carries
                             # title, authors, version and date, and a second copy
                             # here is the drift shape this repo knows well.
                             # Pinned to the version that produced the result and
                             # never moved to a later one.
  doi:                       # string, or null (null is a VERDICT: none registered).
                             # Omitting says only "not established".
  design:
    family:                  # required — closed vocabulary below
    design_detail:           # never infer a stronger design than stated
  synthesis:                 # REQUIRED iff family is meta-analysis/systematic-review,
                             # and forbidden otherwise
    model:                   # required — e.g. "Random-effects models"
    heterogeneity_statistic: | heterogeneity_thresholds:
    quality_tool: | certainty_framework: | reporting_guideline:
    search: {databases: [...], date_range:, records_screened:, records_included:}
    inclusion: [...] | exclusion: [...] | data_handling: [...]
    attempted_but_precluded:
      - analysis:            # required
        reason:              # required

provenance:                  # required
  source_type:               # research | runtime-learner-data | synthetic-simulation
                             # | llm-proposed | platform-experiment
  extracted_by: | extracted_at: | extraction_method:    # all required.
                             # extraction_method SAYS WHAT WAS READ:
                             # manual-from-publisher-fulltext / -abstract /
                             # manual-from-wiki-claim-page / ingest-pipeline-v127
  verification:              # unverified | machine-checked | human-reviewed
  verified_by:               # must be human:<id> if human-reviewed — an agent
                             # must never mark its own extraction reviewed

appears_in:                  # OPTIONAL; each entry validated when present
  - claim:                   # a claims/ slug
    bearing:                 # REQUIRED — supports | contradicts | qualifies.
                             # A property of the EDGE: one result supports one
                             # claim and qualifies another, and the same claim is
                             # supported by one record and contradicted by the
                             # next. Never defaulted — a record read as `supports`
                             # because nobody said otherwise is a fabrication.
    anchor:                  # OPTIONAL — a `### Author Year` heading slug on that
                             # page. Absent means the record names the proposition
                             # WITHOUT having been written into its argument, which
                             # is the normal state for new evidence: promoting it
                             # into `## Evidence` is an editorial act. Ratcheted
                             # when present, so a rename still fails loudly.

evidence_base:               # required — what the results are ABOUT
  unit:                      # required — participants | studies | reports | classes
                             # | schools | sites | effect-sizes | comparisons
                             # | pairs | items | sessions | other
  size: {value, unit}        # required; unit must agree with `unit` above
  additional_sizes:          # every other count worth keeping
    - {value, unit, note}    # note required — say what this counts
  population: | context:     # open-world mappings, as v1
  variation:                 # how the base VARIES — a corpus has a distribution
    - {dimension, distribution}   # over populations, not one population
  arms:
    - id:                    # required
      description:           # required. No `role`: an arm's role varies by
                             # comparison, and index_arm/reference_arm carry it.
                             # Every arm must be named by some comparison.
      size: {value, unit}
      elements: [{term, anchors: [...]}]   # `term` required; anchors must resolve
      dose: {amount, unit, detail}
      implementation_notes: [...]

comparisons:
  - id:                      # required
    kind:                    # required — between-groups | within-subject-baseline
                             # | historical | none | other   ("none" is a VALUE)
    index_arm: | reference_arm:   # an arm id, OR a list of them for a
                                  # heterogeneous side. Required except for kind
                                  # `none` and `within-subject-baseline`, which
                                  # may still name an index arm and usually should
    description:             # required

observations:                # required, non-empty
  - id:                      # required, unique in this file
    sample: {value, unit}    # the analysed n for THIS result
    comparison_ref:          # required — names a comparison, including kind `none`
    analysis_ref:            # an analysis id declared by the release in
                             # `study.release`. Closes the chain claim <- evidence
                             # <- analysis <- dataset <- release <- protocol, so
                             # "why does the wiki believe this" reaches the code
                             # and the data instead of stopping at a citation.
    outcome:
      construct:             # required — your normalised label
      source_language:       # required — the author's own wording, preserved
      measure: | scale:
      direction:             # higher-is-better | lower-is-better | contextual
      role:                  # REQUIRED — capability-evidence | proximal-outcome
                             # | intermediate-outcome | distal-outcome
                             # | organizational-outcome | learner-characteristic
                             # | other
      role_basis:            # required — stated | inferred | ambiguous.
                             # `other` + `ambiguous` is how to DECLINE to
                             # classify; silence is not an option
      valued_by: [{actor, basis}]      # ONLY where the source identifies them
      anchors: [...]
    time:
      label:                 # required
      offset: {value, unit, from}
    result:                  # required
      measure_type:          # required, and the ONLY required field of a result
      estimate: | unit: | ci_lower: | ci_upper: | standard_error: | p_value:
      statistic: | model: | descriptives: | interpretation: | note:
      k: {value, unit}       # REQUIRED for a pooled effect from a synthesis
      heterogeneity: {statistic, value, unit, interpretation}
      prediction_interval: {lower, upper, source}   # `source` required — a PI is
                             # NOT a CI and must never be derived from one
      certainty: {rating, framework}
      # measure_type: qualitative additionally takes finding (required),
      # perspective, collection_method — and MUST NOT carry `estimate`
    moderators:
      reported: [{variable, relationship, source_quote}]   # all three required
      candidate: [...]       # plausible explanations; never promoted
    observability:           # required — all four
      population_detail: | implementation_detail: | outcome_timing: | effect_size:
                             # observed | partial | unreported
    observability_notes:
    source_quote:            # required
    source_location:

not_yet_extracted: [...]     # findings seen and not encoded. An observation with
                             # no result is not a null, it is an unwritten record
```

### Closed vocabularies

| field | values |
|---|---|
| `study.design.family` | `randomized-controlled-trial` `quasi-experimental` `observational` `longitudinal` `qualitative` `mixed-methods` `meta-analysis` `systematic-review` `simulation` `other` |
| `result.measure_type` | `cohens_d` `hedges_g` `odds_ratio` `risk_ratio` `correlation` `mean_difference` `standardized_mean_difference` `regression_coefficient` `probability` `count` `qualitative` `eta_squared` `partial_eta_squared` `other` |
| count `unit` | `participants` `studies` `reports` `classes` `schools` `sites` `effect-sizes` `comparisons` `pairs` `items` `sessions` `other` |
| `comparisons[].kind` | `between-groups` `within-subject-baseline` `historical` `none` `other` |
| `observability.*` | `observed` `partial` `unreported` |
| `heterogeneity.statistic` | `I2` `tau2` `Q` `H` `other` |

`eta_squared` / `partial_eta_squared` are additions to the commissioned list: partial
η² is the effect size an ANOVA prints, and `other` is where a value stops being
comparable with anything.

Everything else — population, context, arm descriptions, all prose — is deliberately
**open-world**. A closed demographic ontology would force "newly arrived migrant
students aged 11–19 across nine north-east Italian secondary schools" into a box that
loses the study.

---

## Wiki concepts are anchors, not a target ontology

`arms[].elements[].anchors` and `outcome.anchors` link to existing pages by
bundle-relative path without the `.md`. Every anchor must resolve on disk.

**`term` and `source_language` are never replaced by an anchor.** The goal is
`human concept anchors + raw source-described variables`, not conformity: a study
whose active ingredient has no wiki page is fully representable, and does not
justify inventing a page for it.

---

## Tools

```bash
python3 scripts/check_observations.py            # validate; exit 1 on any problem
python3 scripts/check_observations.py --summary  # what is in the store, and orphans
python3 scripts/check_observations.py --stub <claim-slug>
python3 scripts/lint.py --type observations      # the same checks, in CI
python3 scripts/compile_observations.py          # research_observation NDJSON
python3 scripts/compile_observations.py --explain <study-key>/<observation-id>
```

`--explain` is the acceptance test run as a command: *what exactly was done, to whom,
compared with what, in what context, measured how, at what time, with what result and
uncertainty, and what important information was not reported* — from the record alone,
reading no narrative prose.

## What the compiler will not do

- **No metric conversion.** A partial η² stays a partial η²; an SMD stays an SMD.
  Turning β = 17.17 words into a *d* needs a pooled SD nobody printed.
- **No pooling, no averaging, no universal weights.** Two observations of one
  intervention are two rows and stay two rows.
- **No derived prediction intervals.** A CI is about the mean effect and a PI about
  the next study; `prediction_interval.source` is required so a computed one can
  never be read as a reported one.
- **No design-model edges**, and **no filling of gaps** — `observability` rides on
  every emitted record.
