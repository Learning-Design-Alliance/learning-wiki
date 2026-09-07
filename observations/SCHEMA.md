# Research observations — schema

A claim page argues something. An **observation** records the configuration that
argument rests on.

`d = .78` is not a weight between two concepts. It is one measurement, of one
intervention, on one population, in one setting, against one comparison, at one
point in time. This store keeps enough of that context that

```
intervention/configuration + population + context + comparison + measurement + time
    → observed outcome/effect
```

survives into whatever reasons over it later, and that

```
retrieval practice + novice learners + immediate feedback + specific content
    + delayed test + specific comparison → d = .78
```

stays distinguishable from another study of "retrieval practice" with different
learners, a different implementation, a different outcome, or a different horizon.

> This file is the reference. The rationale for the shape — and the reading of
> the existing code that produced it — is in `scripts/observation_lib.py`.

---

## Where the records live, and why not in the claim

`observations/<study-key>.yaml`, one file per study, keyed by the same
author-year key `check_citations.py`, `authorities.ndjson` and
`citation_worklist.py` already use.

**Not inside a claim's `sources[]` frontmatter**, for three reasons established
by reading the code rather than guessed at:

1. `sources[]` is **derived, not authored**. `sync_evidence_codes.py --apply`
   rebuilds the whole block from the body's `## Evidence` section through
   `okf_lib.dump_frontmatter`, which emits exactly `id/resource/title/author/q/i/n`.
   Anything else nested there is destroyed on the next run — and that script runs
   inside `run_scrape_batch.py`'s unattended chain.
2. `lint.check_source_entry_keys` holds a **closed key set** at four-space indent,
   precisely so that a rewrite landing on a YAML key is caught. A new key there is
   indistinguishable from that damage.
3. An observation belongs to the **study**, not to any one claim. The wiki has
   12,893 citations over ~1,232 author-year keys, so studies are reused heavily;
   copying a record per citing claim is the drift shape this repo has already lost
   weeks to on DOIs.

**No existing claim page changes.** The join runs the other way: each record's
`appears_in` names the claim slug and the `### Author Year` evidence anchor, and
lint fails if either stops resolving. A rename breaks loudly instead of silently
orphaning the record.

---

## The three distinctions the schema exists to hold

### 1. Absent ≠ unreported ≠ zero

An **omitted field** means "not established". `observability.<field>: unreported`
means "somebody read the source and it does not say". Neither means the effect is
zero. A consumer that reads a missing effect size as zero will pull any pooled
estimate toward nothing; one that reads `effect_size: unreported` can decline to
pool the row.

Same discipline as `crossref_reachable: false` vs `flagged` in the source
manifest, `"doi": null` vs an absent `doi` in `authorities.ndjson`, and
`classify_doi`'s `error` vs `wrong_paper`.

### 2. A capability is not a valued outcome

The Learning Design Spec separates a learner capability from a valued outcome and
uses a logic model for the hypothesised link. Not every dependent variable is a
learner competency — `training completion → workplace performance` measures
neither end as one. `outcome.role` records which it appears to be, and
`outcome.role_basis` records whether the source said so or you inferred it.
`outcome.source_language` keeps the author's own construct wording whatever the
classification.

`outcome.valued_by` is populated **only where the source identifies who defines,
values, measures or is affected by an outcome**. A researcher measuring
graduation does not establish that a learner, an employer or a government values
graduation. There is no default value for this field, for that reason.

### 3. A research observation is not a design hypothesis

```
DESIGN HYPOTHESIS    "Goal A is intended to contribute to Outcome B."
RESEARCH OBSERVATION "Study S observed relationship R between configuration A
                      and Outcome B under population/context C."
```

A finding may later be offered as evidence for or against a logic-model edge, by
something that weighs it. **It does not become that edge here.** There is
deliberately no field in which to write that it does, and every compiled record
carries `kind: research_observation` plus `provenance.source_type` so a consumer
cannot lose track of which it is holding.

---

## File shape

Study-level blocks are shared by every observation in the file; observation-level
blocks are what differ. That is what lets one study yield five observations
without five copies of its population.

```yaml
schema_version: 1

study:                    # required
  key:                    # required — equals the filename, lowercase-hyphenated
  citation:               # required — the full reference string
  doi:                    # string, or null (null is a VERDICT: none is registered).
                          # Omitting the field says only "not established".
  design:
    family:               # required — closed vocabulary, see below
    design_detail:        # free text; never infer a stronger design than stated

provenance:               # required
  source_type:            # research | runtime-learner-data | synthetic-simulation
                          # | llm-proposed | platform-experiment
  extracted_by:           # required — actor convention, e.g. claude/unspecified
  extracted_at:           # required — a date or an ISO date string
  extraction_method:      # required — free text, but SAY WHAT WAS READ, e.g.
                          # manual-from-publisher-fulltext,
                          # manual-from-publisher-abstract,
                          # manual-from-wiki-claim-page, ingest-pipeline-v127
  verification:           # unverified | machine-checked | human-reviewed
  verified_by:            # required to be human:<id> if verification is human-reviewed —
                          # an agent must never mark its own extraction reviewed

appears_in:               # required, non-empty — the join, checked by lint
  - claim:                # a claims/ slug
    anchor:               # a `### Author Year` heading slug on that page

population:               # open-world; only populate what is reported
  n: 18
  description: | age_or_stage: | prior_knowledge: | language_background:
  relevant_characteristics: [ ... ]

context:                  # open-world
  setting: | institution_or_environment: | geography: | delivery_mode: | duration:

intervention:             # present and explicitly empty when there was none
  description:
  elements:               # the active ingredients AS DESCRIBED, kept together
    - term:               # required — the source's language
      anchors: [ ... ]    # optional wiki pages, e.g. principles/game-based-learning
                          # every anchor must resolve on disk; lint checks
  dose: {amount, unit, detail}
  sequence: [ ... ]
  implementation_notes: [ ... ]

comparisons:              # a named list; observations reference one by id
  - id:
    kind:                 # between-groups | within-subject-baseline | historical
                          # | none | other       ("none" is a VALUE, never an omission)
    description:          # required
    elements: [ ... ]

observations:             # required, non-empty
  - id:                   # required, unique in this file
    outcome:
      construct:          # required — your normalised label
      source_language:    # required — the author's own wording, preserved
      measure: | scale:
      direction:          # higher-is-better | lower-is-better | contextual
      role:               # capability-evidence | proximal-outcome | intermediate-outcome
                          # | distal-outcome | organizational-outcome
                          # | learner-characteristic | other
      role_basis:         # stated | inferred | ambiguous — required if role is set
      valued_by:
        - actor:          # learner | teacher | institution | employer | community
                          # | government | researcher | other
          basis:          # required — what in the source establishes it
      anchors: [ ... ]
    time:                 # required
      label:              # e.g. pre | post | followup | single-administration
      offset: {value, unit, from}   # unit ∈ minutes hours days weeks months years
                                    #        sessions items
    comparison_ref:       # required — names an entry in `comparisons`
    result:               # required
      measure_type:       # required, and the ONLY required field of a result —
                          # so a study reporting no effect size is representable
      estimate: | unit: | ci_lower: | ci_upper: | standard_error: | p_value:
      statistic: | model: | descriptives: | interpretation:
      # measure_type: qualitative additionally takes
      finding:            # required for qualitative
      perspective:        # participant | researcher | mixed
      collection_method:
      # and MUST NOT carry `estimate`
    moderators:
      reported:           # only what the study directly supports
        - variable: | relationship: | source_quote:   # all three required
      candidate: [ ... ]  # plausible explanations; free text; never promoted
    observability:        # required — all four fields
      population_detail:  # observed | partial | unreported
      implementation_detail:
      outcome_timing:
      effect_size:
    observability_notes:
    source_quote:         # required
    source_location:

not_yet_extracted: [ ... ]  # findings you saw and did not encode. An observation
                            # with no result is not a null, it is an unwritten record
```

### Closed vocabularies

| field | values |
|---|---|
| `study.design.family` | `randomized-controlled-trial` `quasi-experimental` `observational` `longitudinal` `qualitative` `mixed-methods` `meta-analysis` `systematic-review` `simulation` `other` |
| `result.measure_type` | `cohens_d` `hedges_g` `odds_ratio` `risk_ratio` `correlation` `mean_difference` `standardized_mean_difference` `regression_coefficient` `probability` `count` `qualitative` `eta_squared` `partial_eta_squared` `other` |
| `outcome.direction` | `higher-is-better` `lower-is-better` `contextual` |
| `outcome.role` | see above |
| `comparisons[].kind` | `between-groups` `within-subject-baseline` `historical` `none` `other` |
| `observability.*` | `observed` `partial` `unreported` |

`eta_squared` and `partial_eta_squared` are additions to the commissioned list:
partial η² is the effect size an ANOVA actually prints, and the first fixture that
needed it (Frolli et al. 2023, partial η² = 0.827) would otherwise have been filed
under `other`, which is where a value goes to stop being comparable with anything.

Everything else — population, context, intervention, all descriptions — is
deliberately **open-world**. A closed demographic ontology would force "newly
arrived migrant students aged 11–19 across nine north-east Italian secondary
schools" into a box that loses the study.

---

## Wiki concepts are anchors, not a target ontology

`intervention.elements[].anchors`, `comparisons[].elements[].anchors` and
`outcome.anchors` link to existing pages — principles, elements, patterns,
strategies, processes, methods, theories, learner variables, claims — by
bundle-relative path without the `.md`. Every anchor must resolve on disk.

**`term` and `source_language` are never replaced by an anchor.** The goal is
`human concept anchors + raw source-described variables`, not conformity: a study
whose active ingredient has no wiki page is fully representable, and does not
justify inventing a page for it.

---

## Tools

```bash
python3 scripts/check_observations.py            # validate; exit 1 on any problem
python3 scripts/check_observations.py --summary  # what is in the store, by shape
python3 scripts/lint.py --type observations      # the same checks, in CI
python3 scripts/compile_observations.py          # research_observation NDJSON
python3 scripts/compile_observations.py --explain <study-key>/<observation-id>
```

`--explain` is the success criterion run as a command: it answers *what exactly
was done, to whom, compared with what, in what context, measured how, at what
time, with what result and uncertainty, and what important information was not
reported* — from the record alone, reading no narrative prose.

## What the compiler will not do

- **No metric conversion.** A partial η² stays a partial η². Turning β = 17.17
  words into a *d* needs a pooled SD, and inventing one to make records comparable
  is how a store fills with confident untraceable numbers. Comparability is a
  separate, explicit, downstream analytical step.
- **No pooling and no universal weights.** Two observations of one intervention
  are two rows and stay two rows.
- **No design-model edges.** See distinction 3 above.
- **No filling of gaps.** `observability` rides on every emitted record.
