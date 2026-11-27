#!/usr/bin/env python3
"""ingest_simulator_hypothesis.py — write a simulator discovery as a hypothesis principle.

The learning-graph simulator finds patterns in its ensembles of model worlds. Its
simulation index, configurations and ensemble results stay in the simulator
repository; the study that would test a discovery is filed there as an `experiment`
issue, which the simulator generates. The wiki receives only the statement, written
as a principle page flagged as a hypothesis (hypothesis_lib.py, maintainer
2026-11-27), with pointers to the simulator release and the issue.

Input is one discovery record (YAML), written by the simulator for a published
release:

    slug: lower-hyphen-slug                    # the principle's id
    title: One-sentence principle statement
    statement: >                               # the principle, with its qualifiers
      ...
    simulator: {release: learning-graph-simulator, version: 1.2.0}
    discovery_id: <the simulator's id for the discovery>
    learners:                                  # who it holds for: learner-variables slugs
      - {variable: prior-knowledge, range: "below the 30th percentile of the cohort"}
    conditions: [novice, online-self-paced]     # evidence-dimensions.json tags
    configuration:                             # what was varied, as wiki ids
      - {id: pattern/worked-example-fading, role: "faded after two problems"}
    mechanisms: [cognitive-load]               # simulator mechanism ids (named, not linked)
    outcome: "delayed post-test score"
    robustness: "holds in 174 of 200 ensemble worlds; median effect 0.21 SD (80% of worlds 0.08 to 0.35)"
    boundaries:                                # where it stops or reverses
      - "reverses above the 70th percentile of prior knowledge"
    situations:                                # optional rows for the situation table
      - {if: "`novice`, `online-self-paced`", change: "fade worked examples after two problems"}
    would_test: [claims/some-claim-slug]       # optional: claims the proposed study bears on
    proposed_study: https://github.com/<org>/<simulator repo>/issues/<n>   # or `pending`

Every wiki id is resolved against wiki-index.json and every condition against
evidence-dimensions.json, and the page is checked with hypothesis_lib before it is
written; anything unresolved stops the run. Nothing is written without --apply.

    python3 scripts/ingest_simulator_hypothesis.py discovery.yaml            # show the page
    python3 scripts/ingest_simulator_hypothesis.py discovery.yaml --apply    # write it
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import yaml

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import hypothesis_lib  # noqa: E402
import build_situation_index as bsi  # noqa: E402

REQUIRED = ("slug", "title", "statement", "simulator", "discovery_id", "learners",
            "conditions", "configuration", "outcome", "robustness", "proposed_study")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
KIND_FOLDER = {"principle": "principles", "element": "elements", "pattern": "patterns",
               "design": "designs", "strategy": "strategies", "theory": "theories",
               "process": "processes", "method": "methods", "claim": "claims",
               "learner-variable": "learner-variables", "product": "products",
               "research-method": "research-methods"}


def load_resolve() -> dict:
    return json.loads((WIKI_ROOT / "wiki-index.json").read_text(encoding="utf-8"))["resolve"]


def resolve(resolve_map: dict, ref: str) -> tuple[str, str] | None:
    """'pattern/foo' or 'patterns/foo' -> (folder, current slug), following aliases."""
    kind, _, slug = ref.partition("/")
    kind = {v: k for k, v in KIND_FOLDER.items()}.get(kind, kind)
    target = (resolve_map.get(kind) or {}).get(slug)
    return (KIND_FOLDER[kind], target) if target else None


def check(d: dict) -> list[str]:
    errs = [f"missing `{k}`" for k in REQUIRED if not d.get(k)]
    if errs:
        return errs
    if not SLUG_RE.match(str(d["slug"])):
        errs.append("slug must be lowercase-hyphenated ASCII")
    if (WIKI_ROOT / "principles" / f"{d['slug']}.md").exists():
        errs.append(f"principles/{d['slug']}.md already exists; a discovery never overwrites a page")
    sim = d["simulator"]
    if not (isinstance(sim, dict) and sim.get("release") and sim.get("version")):
        errs.append("simulator must be {release, version}")
    rmap = load_resolve()
    for lv in d["learners"]:
        if not resolve(rmap, f"learner-variable/{lv.get('variable')}"):
            errs.append(f"learner variable {lv.get('variable')!r} is not a learner-variables/ page")
        if not lv.get("range"):
            errs.append(f"learner variable {lv.get('variable')!r} has no range")
    vocab = bsi.tag_vocabulary()
    for tag in d["conditions"]:
        if tag not in vocab:
            errs.append(f"condition {tag!r} is not an evidence-dimensions.json tag")
    for c in d["configuration"]:
        if not resolve(rmap, str(c.get("id", ""))):
            errs.append(f"configuration id {c.get('id')!r} does not resolve in wiki-index.json")
    for ref in d.get("would_test") or []:
        if not resolve(rmap, ref if "/" in ref else f"claim/{ref}"):
            errs.append(f"would_test {ref!r} is not a claim page")
    study = str(d["proposed_study"])
    if study != "pending" and not study.startswith("https://"):
        errs.append("proposed_study must be the issue URL or `pending`")
    return errs


def render(d: dict) -> str:
    rmap = load_resolve()
    sim = f"{d['simulator']['release']}@{d['simulator']['version']}"
    today = datetime.date.today().isoformat()
    title = str(d["title"]).strip()
    desc = re.sub(r"\s+", " ", str(d["statement"])).strip()
    desc = desc if len(desc) <= 240 else desc[:237].rsplit(" ", 1)[0] + "..."

    def link(ref: str) -> str:
        folder, slug = resolve(rmap, ref)
        return f"[{slug}](../{folder}/{slug}.md)"

    lines = [
        "---", "type: principle", f"id: {d['slug']}", f"title: {json.dumps(title)}",
        f"description: {json.dumps('Simulator hypothesis, not tested in learners: ' + desc)}",
        "status: review", f"hypothesis: {hypothesis_lib.FLAG_VALUE}", "hypothesis_status: open",
        f"simulated_by: {sim}", f"proposed_study: {d['proposed_study']}",
        "generated:", "  by: process:simulator-intake", f"  at: {today}", "---", "",
        f"# {title}", "",
        "> **Principle** · [All principles](index.md)",
        hypothesis_lib.banner_line("open"), "",
        "## Description", "",
        re.sub(r"\s+", " ", str(d["statement"])).strip(), "",
        "This is a prediction of the learning-graph simulator "
        f"(`{sim}`, discovery `{d['discovery_id']}`), not a finding from learners. "
        "Do not cite it as evidence. The study that would test it is "
        + (f"[proposed in the simulator repository]({d['proposed_study']})."
           if d["proposed_study"] != "pending" else "being proposed in the simulator repository."), "",
        "## Where the model predicts it holds", "",
        "### Target Learners",
    ]
    lines += [f"- {link('learner-variable/' + lv['variable'])}: {lv['range']}" for lv in d["learners"]]
    lines += ["", "### Conditions"]
    lines += [f"- `{t}`" for t in d["conditions"]]
    lines += ["", "### Configuration simulated"]
    lines += [f"- {link(c['id'])}" + (f": {c['role']}" if c.get("role") else "") for c in d["configuration"]]
    if d.get("mechanisms"):
        lines += [f"- Simulator mechanisms: {', '.join('`' + m + '`' for m in d['mechanisms'])}"]
    lines += ["", "### Outcome", f"- {d['outcome']}", "",
              "### Robustness across the ensemble", f"- {d['robustness']}"]
    if d.get("boundaries"):
        lines += ["", "### Boundaries"] + [f"- {b}" for b in d["boundaries"]]
    if d.get("situations"):
        lines += ["", "## Fitting the design to a situation", "",
                  "| If the brief says | Change | Basis |", "|---|---|---|"]
        lines += [f"| {r['if']} | {r['change']} | Simulated: `{sim}` |" for r in d["situations"]]
    if d.get("would_test"):
        lines += ["", "## Claims it would test", ""]
        lines += [f"- {link(r if '/' in r else 'claim/' + r)}" for r in d["would_test"]]
    lines += ["", "## Key Sources", "",
              f"- Learning-graph simulator, release `{sim}`, discovery `{d['discovery_id']}`.", ""]
    return "\n".join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("discovery", type=Path)
    ap.add_argument("--apply", action="store_true", help="write the page (default: show it)")
    a = ap.parse_args()
    d = yaml.safe_load(a.discovery.read_text(encoding="utf-8")) or {}
    errs = check(d)
    if errs:
        sys.exit("refused:\n  " + "\n  ".join(errs))
    page = render(d)
    problems = hypothesis_lib.problems(page, "principles")
    if problems:
        sys.exit("the rendered page fails hypothesis_lib:\n  " + "\n  ".join(problems))
    if not a.apply:
        print(page)
        return
    out = WIKI_ROOT / "principles" / f"{d['slug']}.md"
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(WIKI_ROOT)}; now run build_indexes.py and add_type_banner.py --check")


if __name__ == "__main__":
    main()
