"""hypothesis_lib.py — principle pages that state a simulator prediction, not research.

The learning-graph simulator (a separate repository) runs ensembles of model worlds
and finds patterns: "for these learners, under these conditions, with this
configuration, outcome Y follows". The maintainer decided (2026-11-27) how such a
discovery enters the wiki:

  * it is written as a PRINCIPLE page, flagged as a hypothesis, stating the
    principle with its learner and context qualifiers;
  * the study that would test it is filed as a GitHub issue in the simulator
    repository, using its `experiment.yml` template, for a researcher to pick up;
  * the simulator keeps its simulation index, configurations and ensemble results
    in its own repository. The wiki holds only the statement and its pointers.

A flagged principle is the most dangerous page in the wiki: every tool and reader
that trusts principles as research-based guidance will read a model's prediction as
guidance unless it checks the flag. So the flag is defined once, here, and every
consumer calls `is_hypothesis()`; lint fails a flagged page that is incomplete.

Frontmatter (flat scalars, so every frontmatter writer keeps them):

    hypothesis: simulated
    hypothesis_status: open | under-test | supported | refuted
    simulated_by: <simulator release>@<version>
    proposed_study: <URL of the simulator issue>, or `pending` until it is filed

and a second banner line under the type banner:

    > **Hypothesis** · predicted by the learning-graph simulator, not yet tested in learners

A hypothesis is never evidence. It cites no claim as support; it may name the claims
it would test. When a study settles it, its status changes and a person decides
whether a research-based principle is written; the flag is never removed silently.
"""
from __future__ import annotations

import re

FLAG_VALUE = "simulated"
STATUSES = ("open", "under-test", "supported", "refuted")
FIELDS = ("hypothesis", "hypothesis_status", "simulated_by", "proposed_study")
BANNER_TEXT = "> **Hypothesis** · predicted by the learning-graph simulator, not yet tested in learners"
# The status changes the wording once a study has run, so the line is matched by its label.
BANNER_RE = re.compile(r"^>\s*\*\*Hypothesis\*\*\s*·", re.M)
FOLDER = "principles"

_FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def frontmatter_text(text: str) -> str:
    m = _FM_RE.match(text)
    return m.group(1) if m else ""


def field(fm_text: str, name: str) -> str | None:
    m = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", fm_text, re.M)
    if not m:
        return None
    return m.group(1).strip().strip('"').strip("'")


def is_hypothesis(text: str) -> bool:
    """True for a page that carries the flag at all, whatever its other fields say.
    Consumers that must not treat a page as research-based check this, not status."""
    return field(frontmatter_text(text), "hypothesis") is not None


def banner_line(status: str) -> str:
    if status in ("open", "under-test"):
        return BANNER_TEXT
    return (f"> **Hypothesis** · predicted by the learning-graph simulator; "
            f"a study has since {'supported' if status == 'supported' else 'refuted'} it")


def problems(text: str, folder: str) -> list[str]:
    """What is wrong with a flagged page. Empty for an unflagged page."""
    fm = frontmatter_text(text)
    if field(fm, "hypothesis") is None:
        stray = [f for f in FIELDS[1:] if field(fm, f) is not None]
        return [f"{', '.join(stray)} present without `hypothesis: {FLAG_VALUE}`"] if stray else []
    out = []
    if folder != FOLDER:
        out.append(f"a hypothesis is written as a principle page; this one is in {folder}/")
    if field(fm, "hypothesis") != FLAG_VALUE:
        out.append(f"hypothesis must be `{FLAG_VALUE}` (the only source of hypotheses so far)")
    status = field(fm, "hypothesis_status")
    if status not in STATUSES:
        out.append(f"hypothesis_status must be one of {', '.join(STATUSES)}")
    sim = field(fm, "simulated_by")
    if not sim or "@" not in sim:
        out.append("simulated_by must name the simulator release and version, `<release>@<version>`")
    study = field(fm, "proposed_study")
    if not study:
        out.append("proposed_study must be the simulator issue URL, or `pending` until it is filed")
    elif study != "pending" and not study.startswith("https://"):
        out.append("proposed_study must be a URL or `pending`")
    elif study == "pending" and status in ("under-test", "supported", "refuted"):
        out.append(f"status is {status!r} but proposed_study is still `pending`")
    if re.search(r"^canonical:\s*true\s*$", fm, re.M):
        out.append("a hypothesis cannot be `canonical: true`: canonical pages are what "
                   "the candidate ledger settles research against")
    if not BANNER_RE.search(text):
        out.append("the `> **Hypothesis** ·` banner line is missing under the type banner")
    # A hypothesis cites no claim as support: a [+..] marker on it would make a
    # prediction read as evidence-backed. It may list claims it would test, unmarked
    # or with [~..] under `## Claims it would test`.
    if re.search(r"\]\((?:\.\./)?claims/[^)]+\)\s*\[\+[SMW]\]", text):
        out.append("a hypothesis cites a claim with a [+..] support marker; list the claims it "
                   "would test under `## Claims it would test`, without a support marker")
    return out
