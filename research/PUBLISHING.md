# Publishing LDA research

**Nothing is published here yet, and nothing unpublished belongs here at all.**

learning-wiki is a public repository. Every branch and every pull request is
visible to anyone from the moment it is pushed, merged or not. So there is no
"draft area" in this repo: work in progress, and anything under embargo, lives in
the private `Learning-engineering-research` repository until it is ready to be
public. The research layer here (`research/`) is where a finding lands **after**
it is published, with the governance that allowed it and a DOI that resolves.

What is in `research/` today is scaffolding, marked `SYNTHETIC` at every level:
example protocols, study plans, releases, reviews and one issue, which exist to
exercise the validators. Nothing in it is real. The one real governance file that
used to sit here, `protocols/lazuli-platform-telemetry/1.0.0.yaml` (which says
platform telemetry may **not** be published as research), moved to the private
repo's transplant tree on 2026-09-24.

## The route from embargoed to published

1. **In the private repo:** the work, the draft, the embargo. Files stamped with
   the embargo marker (see `scripts/check_embargo.py`) cannot be pushed here:
   a Claude Code hook, an opt-in git pre-push hook and `lint.py --type embargo`
   all refuse them.
2. **The embargo lifts.** Patent filings, depositor notices and anything else the
   embargo was holding for are done, and the marker is removed deliberately.
3. **Governance exists here first.** A protocol whose
   `consent.permitted_uses['research-publication']` is `permitted`, and a study plan
   that predates the release (`research/SCHEMA.md`). A release whose protocol does
   not permit publication fails validation, and the DOI script runs that validation.
4. **Draft the release file** at `research/releases/<id>/<version>.yaml`, with
   `provenance.source_type: research` and a `name` on every author. Validate it with
   `python3 scripts/check_research.py`.
5. **Reserve the DOI** before the file is frozen, because a version is immutable:

   ```bash
   python3 scripts/mint_release_doi.py --release <id> --version <v> --metadata      # read it
   python3 scripts/mint_release_doi.py --release <id> --version <v> --reserve --sandbox   # rehearse
   python3 scripts/mint_release_doi.py --release <id> --version <v> --reserve       # for real
   ```

   Write the two lines it prints (`doi:`, `doi_registrar: zenodo`) into the
   `release:` block, and merge. An unpublished deposition can still be deleted.
6. **Publish.** This makes the DOI resolve, and it cannot be undone:

   ```bash
   python3 scripts/mint_release_doi.py --release <id> --version <v> --publish \
       --deposition <n> --by human:<id> --yes
   ```

   It refuses anything but a `human:` actor. An agent may prepare and reserve;
   putting a work in public under a permanent identifier is a person's decision.

A later version is a new file with its own reserved DOI (`supersedes:` the old one).
The earlier version, and its DOI, stay exactly as published.
