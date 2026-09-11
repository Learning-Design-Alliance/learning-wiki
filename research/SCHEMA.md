# The research layer — schema (version 1)

The rest of this wiki records **what we currently believe**. This folder records
**where that came from and how it can be interrogated**.

```
RESEARCH LAYER                     KNOWLEDGE LAYER

What happened?                     What do we currently believe?
How was it investigated?           What propositions are supported?
Under what conditions?             What theories/patterns follow?
What evidence resulted?
Who challenged or reproduced it?
```

```
Protocol ──> Research Release ──> Evidence ──> Claim
                                     ^
                            Review ──┴── Issue
```

> Field reference below. The rationale, and the reading of the existing code
> that produced it, is in `scripts/research_lib.py`.

---

## There is no `evidence/` folder, and that is the main decision here

`observations/` **already is** the evidence layer. Its `study:` block is *"the
SOURCE — what the report is, and by what method it produced results"*, and its
observations are the individual results, each with its own arms, comparison,
analysed sample, timepoint, uncertainty and `observability`. A second object
called Evidence would hold the same fields about the same results, and two
records of one finding is the exact drift shape this repo has lost weeks to on
DOIs.

So a release does not restate its findings. It **names** them, and they name it
back:

```yaml
# research/releases/<id>/<version>.yaml
evidence:
  - ref: example-spaced-review-2026/retention-four-week

# observations/example-spaced-review-2026.yaml
study:
  release: {ref: example-spaced-review-scheduling, version: 1.0.0}
```

Both halves are required to agree, because a half-written edge is worse than no
edge: it reads as a working link from whichever side you arrive on, and only a
reader who checks the other side ever finds out.

**What changed in `observations/` to make this work** — three fields, and no new
object:

| field | why |
|---|---|
| `study.release: {ref, version}` | The source is a release of ours rather than a paper we read. It **replaces** `citation`: a release already carries title, authors, version and date, and writing them again here would be a second copy. Exactly one of the two is required. |
| `appears_in[].bearing` | **Required.** `supports` / `contradicts` / `qualifies`. The direction is a property of the *edge*, not of either end — one result supports one claim and qualifies another. |
| `appears_in[].anchor` | Now **optional**. See below. |
| `observations[].analysis_ref` | Which declared analysis produced this result, closing the chain to the code and the data. |

**`anchor` became optional, and that is the separation between the two layers
rather than a relaxation.** A record may name the proposition it bears on before
anybody has written it into that claim's argument — which is the normal state
for new evidence, and the state this repo wants, because promoting evidence into
a claim's `## Evidence` section is an editorial act and must stay one. When an
anchor *is* given it is still ratcheted: a rename fails lint instead of silently
orphaning the record.

---

## Where the records live

```
research/
  SCHEMA.md
  protocols/<id>/<version>.yaml     versioned, immutable
  releases/<id>/<version>.yaml      versioned, immutable
  reviews/<review-id>.yaml          not versioned; a changed mind is a new review
  issues/<issue-id>.yaml            one problem, however many people found it
```

**Immutability is structural, not a promise.** A version is a *file*: publishing
1.1.0 writes a new file and never touches 1.0.0. "Never silently rewrite what an
earlier release claimed" is then a property of the layout rather than a rule
somebody has to remember.

**Which version is current is derived — the highest semver present — and never
stated.** Stating it would require editing an older file to say it is no longer
current, reintroducing exactly the edit the layout exists to prevent.

**The cost is real and visible in the fixture:** 1.1.0 repeats almost everything
from 1.0.0, because a version has to stand alone to be citable on its own. That
is the trade, and it is the right way round — storage is cheap and a rewritten
record is unrecoverable.

**These are not wiki pages.** They carry no `type:` frontmatter, no page-type
banner, no `id:` in the design-spec sense, and they are absent from
`wiki-index.json`, the mkdocs nav and `okf_lib.CONTENT_FOLDERS` — the same
arrangement `observations/` has, for the same reason. Unattended batch tools
(`sync_evidence_codes`, `add_type_banner`, `build_indexes`, the enrichment
chain) iterate the content folders and rewrite what they find. An immutable
versioned object must not live where a batch job rewrites things. How a release
is *rendered* for a reader is deliberately a separate problem: see "Presentation"
below.

---

## Protocol

A configuration file, not a checkbox. `IRB approved: yes` records that somebody
decided and nothing about *what* was decided; written as configuration, the
rules can be **checked** (see "The two enforcement checks" below).

**This layer records governance. It does not constitute it.** A protocol object
is not an IRB, an ethics committee, a DPIA or a legal basis. `external_review`
exists so a release can never imply an approval it does not have.

```yaml
schema_version: 1

protocol:
  id:                    # == the directory name
  version:               # == the filename stem, semver
  title:                 # required
  effective_from:        # required
  supersedes:            # an earlier version in this directory
  change_note:           # REQUIRED when supersedes is present

participants:
  population:            # required
  recruitment:           # required
  inclusion: [...]       # required
  exclusion: [...]       # required
  vulnerable_populations:          # required; [] is a CLAIM, absence is not
    - {group, safeguards: [...]}
  age_assurance:                   # required — HOW age was established, not what the
    method:                        # criterion says. verified-document | verified-third-party
                                   # | self-attested | inferred | not-established
    jurisdiction:                  # REQUIRED with it: the operative consent age is set per
                                   # member state, so a band without one decides nothing.
                                   # Reasoning adopted from the pipeline's row-level gate.
  compensation: {kind, detail}     # required; `{kind: none}` is an answer

consent:
  required:                        # required, boolean
  mechanism:                       # explicit | broad | opt-out | waived
                                   # | not-applicable | unspecified
  information_provided: [...]      # required when consent is required — WHAT THE
                                   # PARTICIPANT WAS SHOWN. Consent is only
                                   # meaningful for what was disclosed.
  withdrawal:                      # required when consent is required
    allowed:
    mechanism:
    effect_on_collected_data:      # required — "you may withdraw" and "what
                                   # happens to what you already gave us" are
                                   # two promises; only the second is operational
  permitted_uses:                  # required — a MAPPING, not a list. See below.
    internal-pipeline-validation:  # permitted | prohibited | unspecified
    product-improvement:
    research-analysis:
    research-publication:
    secondary-research-by-others:
    model-training:
  permitted_uses_note:             # prose beside the classes, never instead of them
  ai_processing_disclosed:         # required — true | false | unspecified
  ai_processing_detail:            # required when disclosed is true

data:
  collected:                       # required, non-empty
    - {item, purpose, identifiability}      # purpose required per item
  prohibited: [...]                # required — what must NEVER be collected, so a
                                   # later batch can be refused on this line
  identifiability: {collected, published}   # required, both
  deidentification:                # required when collected is identified/pseudonymous
    {method, applied_at, reversible, key_holder}
  retention: {raw, derived, basis} # raw and derived required
  storage:                         # the three controls are TRI-STATE: true | false |
    location:                      # unspecified. The first real protocol forced that — a
    encryption_at_rest:            # bare boolean gave an author who had not checked the
    encryption_in_transit:         # hosting config only "claim true" or "claim false", and
    access_logging:                # both assert something about an unexamined system.
  access:                          # required, keyed by access class
    raw: [...]
    derived: [...]
    published: [...]

risks:
  classification:                  # minimal | more-than-minimal | not-determined
  identified: [{risk, mitigation}] # mitigation required per risk

external_review:
  status:            # approved | exempt | not-required | not-determined | pending
  authority:         # required for approved / exempt / pending
  approval_id:       # required for approved
  determination:     # required for exempt / not-required

deviations: [...]    # {at, description, reported_to, resolution} — append-only

provenance: {source_type, created_at, authored_by, verification, verified_by}
```

**`status` is a five-value vocabulary, not a boolean**, because the two
questions a boolean collapses are both load-bearing: `exempt` means an authority
determined so and can be named, `not-required` means *we* reasoned that no
external review applies — a claim by us, recorded as one — and `not-determined`
says nobody has established either. It is also deliberately not spelled
`yes`/`no`: YAML 1.1 reads a bare `yes` as the boolean `True`, so `required: yes`
arrives as `True` and fails a string check for reasons no author can see. That
happened while writing this fixture.

**`permitted_uses` is a mapping of closed classes, not a list of sentences, and
the first real protocol is what forced that.** Platform telemetry collected under
terms of service, with no research consent step, may legitimately be used to
check that a pipeline works and may **not** be published as research. Written as
free text that distinction is a sentence nobody reads; written as classes it is a
release being refused. An **absent** class means `unspecified` — nobody
established anything — so absence is safe by construction, and adding a class to
the vocabulary later cannot invalidate an already-frozen protocol file.

`consent.secondary_research_use` was a separate tri-state flag in the first
draft. It is exactly `permitted_uses: {secondary-research-by-others: ...}` said a
second way, so it is now **refused by name** — two places to state one fact is the
drift shape this repo has lost weeks to.

**`deviations:` is appended to a frozen file, which is the one place that is
allowed.** A deviation is a fact about the version that was in force when it
happened; recording it as a new version would assert that the rules changed,
which is a different and false statement. Whether it should instead be an
append-only NDJSON log beside the object — the shape `manifest.ndjson` and
`authorities.ndjson` already use here — is **open**, and left open until a real
deviation exists.

---

## Research Release

The principal aggregate: one versioned, citable investigation.

```yaml
schema_version: 1

release:
  id:                  # == the directory name
  version:             # == the filename stem, semver
  title:               # required
  question:            # required — the QUESTION, not the finding
  released_at:         # required
  supersedes:          # an earlier version
  change_note:         # REQUIRED when supersedes is present
  addresses:           # [{kind: issue|review, ref}] — what this version answers

protocol: {ref, version}     # required, OR:
no_protocol_reason:          # ...why this investigation has no protocol of ours

research_design:
  family:              # required — the SAME closed vocabulary observations use
  detail:
  preregistration: {registered, ref, note}

datasets:
  - id: title: grain:          # grain required — the unit of a row
    format:                    # parquet | csv | ndjson | ...
    location: {kind, ref}      # url | doi | s3 | gcs | git | internal
                               # | physical | not-yet-deposited
    sha256:                    # REQUIRED once deposited
    rows: size_bytes:
    identifiability:           # required
    access:                    # required — raw | derived | published
    derived_from: [dataset ids]

analyses:
  - id: title:
    code: {repo, commit, path}     # a COMMIT, never a branch or tag
    environment: {kind, detail, lockfile}
    inputs: [dataset ids]          # required, non-empty, must resolve
    outputs: [...]
    ai_processing:                 # required — true | false | unspecified

evidence:
  - {ref: "<study-key>/<observation-id>", note}

artifacts:
  - {id, kind, title, location}    # renderings: brief, notebook, PDF, dashboard

interpretation:        # required — what the authors think it means
limitations: [...]     # required, non-empty
funding:               # required
conflicts:             # required
provenance: {authors: [{id, role}], source_type, created_at,
             software_versions, verification, verified_by}
```

**There is no `claims:` block, on purpose.** The claim edge is per-*evidence* and
carries a direction, and it already lives on the observation's `appears_in`. A
release-level list would be a second place for the same edge to be stated, with
no way to tell which was right when they disagreed.

**Large research artifacts stay outside the wiki.** What is held here is what is
needed to *find* the data and to prove that what was found is what was analysed:
a location, a hash, a grain, and the access class it falls under. A Parquet table
of attempt events does not belong in a git repository of markdown, and a summary
of it here would be a second version of the numbers.

### The two enforcement checks

The arrow the protocol object exists for — *machine-readable protocol →
automated checking*. Both are narrow on purpose: this is a demonstration, not a
policy engine, and a rule that fires on a case nobody has met is a rule nobody
trusts.

1. **A dataset may not be more identifiable than its protocol permits at its
   access class.** `identified > pseudonymous > deidentified > aggregate`;
   `published` is bounded by `data.identifiability.published` (the promise made
   to the participant), `raw` and `derived` by `.collected`.
2. **An analysis declaring `ai_processing: true` requires
   `consent.ai_processing_disclosed: true`.** `unspecified` fails as well as
   `false` — silence is not permission.
3. **A release requires `permitted_uses['research-publication'] == permitted` on
   its protocol.** A release *is* a publication, so naming a protocol that does
   not permit publication is the release saying it may not exist. `prohibited`
   and absent both fail and are reported differently, because "we decided not
   to" and "nobody has decided" are different states, and only the second is
   fixed by asking somebody.

All three were tested against the fixture by mutation — publishing a pseudonymous
dataset, running an AI analysis under a protocol that did not disclose it, and
publishing from data whose protocol does not permit publication — each producing
exactly one error naming the field that governs it.

---

## Reconciling with the row-level gate in learning-engine-ai-frontend

The Lazuli learning-observation pipeline (`experiments/learning-graph/` in
`learning-engine-ai-frontend`) independently arrived at the same rule this layer
enforces, at a different grain. `report/gate.py` reads the compiled rows and
refuses publication; the check here reads the protocol and refuses a release.

**They are not redundant, and both are needed.** A protocol can permit
publication while the actual rows carry no recorded basis; the rows can all be
clean while the protocol never authorised publishing. Two gates at two grains
catch two different failures.

Its reasoning on `product_terms` is worth quoting, because it is the same
conclusion reached independently in another repo:

> a product privacy policy is a basis for operating the product, not for
> publishing findings about its users as research; an ethics review at analysis
> time cannot cure it

**The vocabularies do not currently agree, and each mismatch would break the
join silently.** Recorded here rather than fixed by fiat, because changing either
side unilaterally is how one repo starts lying about the other:

| concept | pipeline (per row) | this layer (per protocol) | status |
|---|---|---|---|
| identifiability | `pseudonymised` | `pseudonymous` | **collision** — same meaning, different word. One has to win. |
| consent basis | `consent_basis`: `product_terms`, `research_consent`, `parental_consent`, `school_dpa`, `legitimate_interest`, `synthetic_no_subject`, `not_recorded` | `consent.mechanism` + `permitted_uses` | **no crosswalk yet.** `product_terms` implies `research-publication: prohibited`; `not_recorded` implies `unspecified`. The rest are unmapped. |
| age | `age_band` plus a required `jurisdiction` | `participants.age_assurance.{method, jurisdiction}` | **adopted from the pipeline** — its reasoning that a band without a jurisdiction decides nothing is why `jurisdiction` is required here. |
| synthetic data | `source_type: synthetic` / `consent_basis: synthetic_no_subject` | `provenance.source_type: synthetic-simulation` | **collision** on the value spelling. |

Two further things the pipeline holds that this layer does not, deliberately:

- **Per-row governance.** `RawAttempt` carries `identifiability`, `consent_basis`,
  `age_band` and `jurisdiction` on *every row*, because a dataset can mix bases
  and a protocol-level statement cannot express that. A protocol states the
  rules; the rows state what was actually captured under them. Neither replaces
  the other, and a release drawing on mixed rows needs both checks to pass.
- **Publication *kind*.** The gate retitles rather than blocks a fully synthetic
  dataset — it cannot carry findings about learners because there are no learners
  in it, but it can be an honest instrument report. This layer has no equivalent
  and does not need one yet: `provenance.source_type` on the evidence already
  tells a consumer what it is holding.

---

## Review

A structured contribution that interrogates a research object. **Not a comment,
and not peer review in the journal sense.**

```yaml
schema_version: 1

review:
  id:                  # == the filename
  created_at:          # required
  review_type:         # required — extensible controlled vocabulary:
                       # question methodological_concern statistical_concern
                       # governance_concern verification reanalysis replication
                       # boundary_condition practice_report theoretical_alternative
                       # supporting_evidence contradictory_evidence response

  target:              # required — reviews attach THROUGHOUT the graph
    kind:              # protocol | release | evidence | claim | review | issue
                       # | analysis | dataset
    ref:
    version:           # required for protocol and release targets

  assertion:           # required — one sentence, what this contribution asserts
  rationale:           # required — the argument for it, kept separate
  supporting_artifacts: [{kind, title, location, note}]
  evidence: [{kind, ref, note}]

  author:
    id:                # required — a STABLE contributor id
    basis: [...]       # required, non-empty — what GROUNDS this contribution
    identity_state:    # public_verified_identity | verified_pseudonym
                       # | unverified_identity  (claimed, never verified here)
    stated_affiliation: disclosure:

  issues: [issue-id]   # the problem(s) this is an instance of
  assessment: {...}    # properties of FORM — see below
  moderation: [{...}]  # conduct, never correctness — see below
  withdrawn: {at, reason}   # the only permitted self-edit
```

**No institution, academic rank, degree or publication history is required,
requested, or able to gate whether a contribution exists.** What differs between
contributions is `author.basis` — *what grounds this contribution*, a property of
the **contribution** and not of the person. The same reviewer writes one review
having reproduced the analysis and another having only read the release, and
those are not equally grounded:

```
reproduced-the-analysis   reanalysed-the-data      ran-a-replication
read-the-release          read-the-protocol        read-the-artifacts
practitioner-in-this-setting                       participant-in-this-research
domain-expertise-stated   methodological-expertise-stated
automated-check           other
```

`domain-expertise-stated` is named `stated` because that is all this layer can
honestly record. Nothing scores, weights or ranks a basis.

**A review is not evidence.** It may *introduce* evidence; the evidence then
bears on the claim, through `observations/.../appears_in[].bearing`. A review
carrying its own `bearing:` is **rejected by the validator** — a second,
incompatible positive/negative axis is exactly what must not exist.

### Fields the schema refuses by name

`positive`, `approved`, `helpful_votes`, `votes`, `score`, `reputation`,
`credentials`, `bearing` — each one fails validation with the reason. A field
that records agreement or popularity makes those things readable as validity,
and once one release writes it, every consumer has to decide what it means. The
refusal is enforced rather than requested so it survives the first person who
thinks a vote count would be handy.

### `assessment` — form, not favour

```yaml
assessment:
  target_specific: true          # true | false | unassessed
  rationale_present: true
  evidence_present: false
  independently_reproduced: unassessed
  duplicate_of: null             # a review id, never a merge
  assessed_by: assessed_at: note:
```

Every field is checkable by a machine looking at the object and the graph, which
is the point: **form is what automation may judge, and truth is not.** A future
prominence calculation can read specificity, evidence supplied, reproduction,
independent confirmation and non-duplication. None of them records whether
anybody agreed. They are author-entered today and expected to become computed —
which is why each is a tri-state: `unassessed` says nobody has evaluated this,
which is not the same as evaluating it as false.

Adding a field here that records *reception* rather than *form* fails
validation, by the same mechanism as the refused fields above.

### `moderation` — conduct, never correctness

```yaml
moderation:                      # a LIST: a history that can be overwritten is not a record
  - state: limited               # visible | limited | withheld
    reason:
      code: personal_attack      # a CLOSED set of conduct categories
      policy: <policy id>        # the rule it was taken under, so it can be argued with
    decision: {mechanism, at, note}   # automated | human | automated-then-human
    appeal: {status}             # none | requested | upheld | overturned
```

The reason codes are `spam personal_attack harassment threat impersonation
privacy_violation off_topic duplicate_submission illegal_content
other-conduct`. **There is no code meaning "wrong", "unfounded", "hostile to the
authors" or "disagrees with the release"** — so suppressing a critique on the
merits requires inventing a code the schema does not have, and fails.

`withheld` never means deleted. The object stays with its assertion readable;
what changes is prominence, and the reason, the policy, the mechanism and the
appeal state stay attached forever.

**Does ModerationDecision deserve its own object?** Not yet: a decision is only
ever about one review, so a list on the review holds the same information with
one fewer file to join. It would earn its own object the moment one decision can
cover many contributions, or an appeal acquires its own history.

**A malformed submission never becomes a review at all.** `assertion` and
`rationale` are required, and the target must resolve — so a bare "interesting
study" or an insult with no assertion fails at the door. That is a form check,
not moderation: moderation is for a *well-formed* contribution whose conduct is
a problem. This is what makes open review expensive to spam without making it
gated.

---

## Issue — one problem, however many people found it

The object that keeps open review from becoming a hundred repetitive comments.

```yaml
schema_version: 1

issue:
  id: created_at:
  category:            # statistical_assumption design_confound measurement_validity
                       # data_quality reporting_gap reproducibility generalisability
                       # governance interpretation other
  target: {kind, ref, version}    # a clearly identified object; NOT always a release
  summary:             # required
  state:               # open | unresolved | resolved | withdrawn

  raised_by: [review-id, ...]     # required, non-empty; ORDERED BY FIRST APPEARANCE
  supporting: [...]
  disputing: [...]                # kept permanently, whatever the resolution says
  response: [...]

  resolution:          # required when state is resolved
    outcome:           # confirmed | partially_confirmed | not_supported
                       # | superseded | cannot_be_determined
    explanation:       # required
    decided_by:        # required — a position held by somebody, not a platform verdict
    at:
    resulting_release: {ref, version}
```

Without this object, eighteen people independently noticing one statistical
defect produce eighteen unlinked reviews: nothing can tell they are one problem,
prominence has to be computed from volume, and the person who said it first is
indistinguishable from the seventeenth. With it, `--issues` prints:

```
resolved    time-on-task-not-held-constant
            release example-spaced-review-scheduling@1.0.0 [design_confound]
            2 independent identification(s), 1 supporting, 1 disputing, 1 response(s)
            first identified by 2026-09-11-spacing-confounded-with-total-time (2026-09-11)
            resolution: confirmed (asserted by claude/unspecified) -> …@1.1.0
```

**A resolved criticism stays in the record.** The reviews that raised it stay
listed, the objections stay listed, and a later review may target the issue
again. `resolution` is an assertion by a named author like any other — which is
why `decided_by` is required, and why `not_supported` and `confirmed` sit in one
vocabulary rather than one being an absence of the other.

**The aggregation edge may be written from either end.** A reviewer who knows
they are piling onto a known problem writes `issues:` on their review; a later
process that *notices* eighteen reviews are one problem writes `raised_by` on the
issue. The issue side is authoritative — so post-hoc aggregation needs no edit to
anybody's review — and where both ends are written, validation requires them to
agree.

**Two independent identifications are not a duplicate.** `assessment.duplicate_of`
names an earlier review without merging into it, so the later contributor keeps
their own object, author and date. Recording an independent re-identification as a
duplicate would erase the independence that makes two identifications worth more
than one.

---

## The adversarial test

The commissioning brief's worked example, walked through the model. LDA publishes
a release making a claim; within 24 hours 40 people say "interesting study", 18
independently notice the same statistical problem, 3 post insults, 2 supply
executable reanalyses, a famous professor says the methodology is fine with no
analysis, an unknown graduate student explains rigorously why it is not, the
authors respond, a week later they agree the student was right, a new release
changes the estimate, and six months later another team replicates the corrected
finding.

| what happens | how it is represented |
|---|---|
| 40 × "interesting study" | Never become objects. `assertion` and `rationale` are required and the target must resolve, so nothing with no assertion validates. |
| 18 independent identifications | 18 reviews, one `Issue`, `raised_by` ordered by arrival. Attribution for all 18 survives; the first is identifiable. |
| 3 insults | Either fail the form check (no assertion), or — if well-formed and abusive — carry a `moderation` entry with a conduct code, a policy, a mechanism and an appeal. Nothing is deleted. |
| 2 executable reanalyses | `review_type: reanalysis`, `supporting_artifacts` naming code at a commit against a published dataset hash, `assessment.independently_reproduced: true`, listed in `issue.supporting`. |
| famous professor, no analysis | A review like any other. `assessment.evidence_present: false` sits beside the reanalysis that has it. No field lets the eminence outrank the evidence; `identity_state` is read by nothing. |
| unknown graduate student, rigorous | Same object, same fields, `basis: [reanalysed-the-data]`. No credential is required for it to exist or to be inspected. |
| authors respond | `review_type: response` targeting the issue. Not a privileged reply slot, and it does not close the issue by existing. |
| authors agree the student was right | `issue.resolution.outcome: confirmed`, `decided_by` naming who asserts it. The dispute stays listed. |
| new release changes the estimate | A new *file*, 1.1.0, `addresses: [{kind: issue, …}]`. 1.0.0 is untouched, and so is the evidence record it produced — the superseded estimate remains readable beside the corrected one, both bearing on the same claim with different `bearing` values. |
| independent replication, 6 months later | Its own release, its own evidence, and a `review_type: replication` linked to the issue as supporting. A replication is **both** a release and a relation, and the model does not force a choice. |

No editor adjudicates anything; no credential is weighted; no criticism is
buried; spam never becomes an object; the historical disagreement is a file; and
the first identifier keeps their attribution.

**A contributor's history is derivable and must never be stored.** "Eleven
methodological concerns later confirmed, two not supported, four reproducible
reanalyses" is a traversal of `author.id → reviews → issues → resolution
outcome`. `reputation` is a refused field for exactly that reason: a stored copy
is a second version of the graph that nothing can check.

---

## Presentation is out of scope

A release is not a paper. The same object should eventually render as an
interactive report, a conventional article, a PDF, a practitioner summary, a
methods report, a visualization, a notebook, a talk, an AI conversation, an API
response or a machine-readable evidence package. `artifacts:` lists the
renderings that happen to exist and is indifferent to which. Nothing in this
schema describes typography, APA formatting or citation presentation.

---

## Tools

```bash
python3 scripts/check_research.py                     # validate; exit 1 on any problem
python3 scripts/check_research.py --summary           # what is in the layer
python3 scripts/check_research.py --issues            # issues, their state and provenance
python3 scripts/check_research.py --why <claim-slug>  # the traversal
python3 scripts/lint.py --type research               # the same checks, in CI
```

`--why` is the acceptance test run as a command: *why does the wiki believe this
claim* — answered by walking

```
claim <- evidence <- analysis <- dataset <- release <- protocol
```

from the records alone, reading no prose, and printing what is contested at every
level. It names any record whose `provenance.source_type` is not `research`
loudly, so a simulation, a runtime telemetry record or a model's proposal can
never be mistaken for a published finding at a glance.

---

## The fixture

One synthetic chain, marked at every level (`source_type:
synthetic-simulation`, `SYNTHETIC` in every title and header comment):

```
research/protocols/example-platform-learning-telemetry/1.0.0.yaml
research/releases/example-spaced-review-scheduling/1.0.0.yaml
research/releases/example-spaced-review-scheduling/1.1.0.yaml
observations/example-spaced-review-2026.yaml            (evidence from 1.0.0)
observations/example-spaced-review-2026-adjusted.yaml   (evidence from 1.1.0)
research/reviews/  5 reviews
research/issues/time-on-task-not-held-constant.yaml
claims/spaced-practice-improves-long-term-retention.md  (UNCHANGED)
```

**The claim page is deliberately untouched.** The evidence names it with a
`bearing` and no `anchor`, so the edge exists and nothing fabricated appears in a
real claim's `## Evidence` section. That is also the general rule, not a fixture
workaround: evidence arriving does not promote itself into an argument.

---

## Deliberately unresolved

Left open until there are real releases to learn from:

- **Whether `Analysis` and `Dataset` become first-class objects.** Today they are
  declared inside a release and addressed as `<release-id>/<version>/<local-id>`,
  which is enough to target a review at one. They would earn their own files when
  one dataset is shared across releases, or when an analysis is re-run
  independently of the release that declared it.
- **Whether `deviations:` belongs in the protocol file or an append-only log.**
- **`ModerationDecision` as its own object.**
- **The review-type vocabulary.** `methodological_concern` and
  `statistical_concern` overlap; which distinctions reviewers actually draw is
  something to learn from reviews, not to decide now.
- **Who may assert an issue `resolution`, and whether an issue can have
  competing resolutions.** Today it is one block with a `decided_by`.
- **How `bearing` interacts with living synthesis.** A pooled estimate over rows
  whose edges disagree in direction is a question this schema keeps answerable
  and does not answer.
- **Identity verification, reputation, ranking, voting, notifications,
  moderation services and AI classifiers** — none of them, deliberately. The
  objects are shaped so each can be added later without a migration.
