# Checking the claims the wiki leans on

The batch extractor runs without a gating judge (CLAUDE.md, 2026-09-26): it costs $0.0027 an
article, and a judge on every article would nearly triple that. The judge is spent here instead,
on the claims that many design pages rest on, where a misstatement does the most harm. This is
the procedure for running that check and acting on what it finds.

`scripts/check_load_bearing.py` does the work. It never edits a page. Deciding what a finding
means, and fixing it, is the part below that a person or a session does by hand.

## When to run it

- **After every batch.** `run_scrape_batch.py` runs it (top 200 claims, $0.25 cap) once the new
  pages are linked. Only entries whose text changed, or that newly entered the top 200, are
  judged again, so a routine run costs a few cents. The console prints the summary.
- **After editing a claim's evidence by hand**, for the claims you changed:
  `--claims <slug> ...`. A fix is not finished until the re-judge passes.
- **Every month or so, wider**: `--top 500` (about $0.50 the first time). The ranking moves as
  batches add links, and a claim that becomes load-bearing has never been checked.

## Commands

```bash
set -a && . /etc/eval-harness.env && set +a        # OPENROUTER_API_KEY (and OPENALEX_API_KEY)

python3 scripts/check_load_bearing.py --rank --top 40            # who ranks where; free
python3 scripts/check_load_bearing.py --top 200 --budget 0.50    # judge; skips anything already judged
python3 scripts/check_load_bearing.py --report                   # the open failures, most-cited first
python3 scripts/check_load_bearing.py --claims <slug> <slug>     # re-judge specific claims after a fix
python3 scripts/check_load_bearing.py --dismiss "<slug>#<entry>" --because judge-wrong \
    --reason "what you checked and what it showed" --by human:<id>
```

What the ranking counts: the design pages (principles, elements, patterns, strategies, theories,
learner variables, processes, methods) that cite the claim, then the claims that link it.

What the judge sees: one evidence entry at a time, with the claim's title and the subclaims that
point at that entry, against the study's own text. That is the article the pipeline fetched
(`eval/corpus/cache/`) when the claim came from a batch; otherwise the OpenAlex abstract for the
entry's DOI. Entries with no DOI, or whose DOI has no abstract, are counted as not checkable and
never reported as passing.

## Reading the verdicts

| Verdict | Meaning | What to do |
|---|---|---|
| `pass` | Nothing on the entry misstates the source | Nothing |
| `unverifiable` | Judged on an abstract, which does not carry the entry's details; nothing contradicted | Nothing now. Full text would settle it |
| `fail` | Something the entry or its subclaims say contradicts or overstates the source | Triage it (below) |
| `ABSTRACT-IS-ANOTHER-WORK` | The abstract OpenAlex returned is a different work from the one cited | Check the DOI in Crossref; usually `--dismiss --because registry-wrong` |

**Read each failure against the source before acting on it.** The judge is a model and has been
wrong in recognisable ways:

- **Years.** It compares the citation's year with OpenAlex's, which is often the online-first
  date (González et al.: 2018 online, 2019 in the issue). Crossref's `issued` date settles it.
- **Author lists.** OpenAlex truncates some; Crossref's `author` list settles it (Lehman et al.
  2013 has nine).
- **Wrong abstracts.** OpenAlex attaches another work's abstract to some classics, under the
  right DOI and title: Wood, Bruner & Ross (1976), Deci (1971), Alfieri et al. (2011). Non-English
  ones are refused automatically; English ones reach the judge and come back as
  `not-this-study`.

## Fixing a failure

Only fix what you have confirmed in the source. Before each edit:

```bash
cat "eval/corpus/cache/doi-<doi with / as _>.txt"      # the abstract the judge saw
grep -n -i "<phrase>" eval/corpus/cache/<source-id>.txt # the article, for a batch claim
curl -s "https://api.crossref.org/works/<doi>?mailto=contact@learningdesignalliance.org"
```

Then make the smallest edit that makes the entry true, and keep the finding where the finding is
right. What went wrong in the first run (2026-09-27), and what fixing it looked like:

- **The direction is reversed** (Trypke et al. 2023, Lively et al. 2023): state the scenario the
  finding holds for, and the one where it reverses.
- **Opinion coded as evidence**: a framework, a design proposal or a conceptual paper coded as an
  experiment (Stefanou et al. 2004, van Merriënboer et al. 2006, Sözen 2024). Recode to `q1`
  (or `q2` for a narrative review), `i?`, and say what kind of work it is.
- **An effect size where none is reported**: `i1`/`i2` beside a source that prints no statistic.
  Recode to `i?`. `i` codes a printed magnitude (CLAUDE.md, impact table).
- **Causal wording for a correlation** (Uchihara et al. 2019, Li et al. 2010): keep the
  correlation and say that it cannot show cause.
- **A number, word or scope off** (Sinha & Kapur's range, Deci et al.'s "modest", Okonofua's
  n, "often" dropped from Cummins): copy the source's figure or word.
- **The title overstates the finding**: change the `title:`, `description:` and `# H1` text, and
  **keep the slug**, since the slug is the id design documents cite. Update link text on other
  pages that repeats the old title. Renaming the slug is the maintainer's call.

Then regenerate what the edit feeds, check, and re-judge:

```bash
python3 scripts/sync_evidence_codes.py --apply
python3 scripts/add_evidence_summary.py --apply
python3 scripts/add_evidence_profile.py --apply
python3 scripts/fix_dead_anchors.py --apply
python3 scripts/build_indexes.py
python3 scripts/lint.py
python3 scripts/check_load_bearing.py --claims <the slugs you edited>
```

A re-judge that still fails means the edit did not settle it: read the new issues, or dismiss if
what remains is one of the judge errors above.

## Dismissing a failure

`--dismiss` records that you read the failure and the page is right. It is appended to
`eval/load-bearing/reviewed.ndjson`, which is committed, so every machine and later run sees it.
It needs a `--because`:

- `judge-wrong`: the source supports the page, and the reason says how you know.
- `registry-wrong`: the text the judge was given is not the cited work.

A dismissal is tied to the exact text of the entry it vouches for. Any later edit to that entry
re-opens it for judging, because the dismissal no longer describes what the page says. Dismissing
is triage, not verification: it never adds a page's `verified:` entry, which only a person's
review of the whole page may do (CLAUDE.md, trust tiers).

## Files

| File | Committed | What it holds |
|---|---|---|
| `eval/runs/load-bearing/judged.ndjson` | no (per machine) | Every verdict, keyed by a digest of the entry and the source text, so nothing is paid for twice |
| `eval/corpus/cache/doi-*.txt` | no | OpenAlex abstracts; an empty file records a 404 |
| `eval/load-bearing/reviewed.ndjson` | yes | Dismissals, keyed by the entry's text |

## First run, for scale

2026-09-27, top 200 claims plus the claims that joined the top 200 once that day's links landed:
366 entries judged for $0.59 in all. Thirty came back failing or naming another work. 25 were
real and are corrected, 2 were the judge's errors (a year, an author list), and 3 were OpenAlex
supplying another work's abstract. After the fixes: 180 pass, 183 unverifiable, 0 open, 3
dismissed. Of the 137 claims three or more design pages cite, 3 came from a batch, so the check
mostly lands on older hand-written and gap-filled pages; the batch claims it reaches are the ones
the day's linking made load-bearing.
