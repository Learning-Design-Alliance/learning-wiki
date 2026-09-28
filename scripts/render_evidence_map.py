#!/usr/bin/env python3
"""
render_evidence_map.py — PILOT. Turn the coded cells (code_evidence_axes.py) behind a
page's Design Decisions into one table per decision, in a form a designer can reason
with instead of a score: options as rows, outcomes as columns, and in each cell what
was found, how strong the design was, and how close the studied learners, goals and
conditions are to the designer's own. Nothing is ranked and nothing is summed across
outcomes; a trade-off stays visible as + in one column and - in another.

    python3 scripts/render_evidence_map.py elements/worked-examples [--profile P.json]

A profile names the designer's learners, goal and conditions on the same axes
(eval/evidence-axes/axes.json), plus the outcomes they are aiming at, e.g.
    {"name": "S1", "L": {"expertise": "novice", "age": "adult"},
     "G": {"knowledge_type": ["verbal-association", "complex-skill"]},
     "C": {"setting": "online-self-paced", "duration": "days-weeks"},
     "O": ["delayed-retention", "skill-performance", "persistence"]}
Without one, match is not judged and every experimental cell reads "extrapolated".
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
RUNS = WIKI_ROOT / "eval" / "runs" / "evidence-axes"
AXES = json.loads((WIKI_ROOT / "eval" / "evidence-axes" / "axes.json").read_text(encoding="utf-8"))

COLUMNS = [  # outcome groups, in the order a designer usually weighs them
    ("Retention", ("delayed-retention",)),
    ("Immediate", ("immediate-performance",)),
    ("Transfer / understanding", ("near-transfer", "far-transfer", "conceptual-understanding")),
    ("Skill", ("skill-performance",)),
    ("Achievement (pooled)", ("general-achievement",)),
    ("Time / load", ("learning-time", "cognitive-load")),
    ("Motivation / persistence", ("motivation-affect", "persistence")),
    ("Other", ("assessment-accuracy", "other", "?")),
]
EXPERIMENTAL = {"randomised", "within-subject", "synthesis-experimental", "randomised?", "synthesis-experimental?"}
ASSOC = {"controlled-nonrandom", "correlational", "synthesis-mixed", "qualitative"}
ARGUMENT = {"argument"}
MATCH_AXES = (("L", "expertise"), ("L", "age"), ("G", "knowledge_type"), ("C", "setting"))


KIND_DESIGN = {  # the entry's recorded kind, used only where the coder could not read the design
    "causal": "randomised?", "quant-synthesis": "synthesis-experimental?", "associational": "correlational",
    "qualitative": "qualitative", "review": "argument", "theoretical": "argument", "design": "argument"}


def entry_kinds(claim):
    sys.path.insert(0, str(WIKI_ROOT / "scripts"))
    import okf_lib
    try:
        ev = okf_lib.get_section((WIKI_ROOT / "claims" / f"{claim}.md").read_text(encoding="utf-8"), "Evidence") or ""
    except FileNotFoundError:
        return {}
    out = {}
    for part in re.split(r"(?m)^(?=### )", ev):
        if part.startswith("### "):
            out[okf_lib.slugify(part.split("\n", 1)[0][4:].strip())] = okf_lib.parse_evidence_codes(part).get("kind")
    return out


def load_cells(run="a"):
    by_claim = defaultdict(list)
    kinds = {}
    for line in (RUNS / f"{run}.ndjson").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            for c in r["cells"]:
                c["_basis"], c["_entry"], c["_i"] = r["basis"], r["entry"], r["codes"].get("i")
                if r["claim"] not in kinds:
                    kinds[r["claim"]] = entry_kinds(r["claim"])
                res = c.setdefault("result", {})
                if res.get("design") in (None, "?"):
                    res["design"] = KIND_DESIGN.get(kinds[r["claim"]].get(r["entry"]), "?")
                by_claim[r["claim"]].append(c)
    return by_claim


def decisions(page: str):
    t = (WIKI_ROOT / f"{page}.md").read_text(encoding="utf-8")
    sec = t[t.index("## Design Decisions"):]
    m = re.search(r"\n## (?!Design Decisions)", sec)
    sec = sec[:m.start()] if m else sec
    for part in re.split(r"(?m)^### ", sec)[1:]:
        q = part.split("\n", 1)[0].strip()
        yield q, list(dict.fromkeys(re.findall(r"\.\./claims/([^)#]+)\.md", part)))


def match(cell, profile):
    """'●' at least three of the four axes are reported and all agree with the profile;
    '◎' all reported axes agree but fewer than three are reported; '◐' one differs;
    '○' two or more differ; '?' when the study reports none of them."""
    if not profile:
        return None
    known = differ = 0
    for axis, field in MATCH_AXES:
        want = (profile.get(axis) or {}).get(field)
        got = (cell.get(axis) or {}).get(field)
        if not want or got in (None, "?"):
            continue
        want = want if isinstance(want, list) else [want]
        known += 1
        if got != "mixed" and got not in want:
            differ += 1
    if not known:
        return "?"
    if differ == 0:
        return "●" if known >= 3 else "◎"
    return "◐" if differ == 1 else "○"


def usable(c):
    """A cell counts only when its direction is quoted from the study's own text."""
    return c.get("quote_ok") and not c.get("invalid") and (c.get("result") or {}).get("direction") not in (None, "?")


def status(cells, profile):
    exp = [c for c in cells if (c.get("result") or {}).get("design") in EXPERIMENTAL]
    if exp:
        return "known" if profile and any(match(c, profile) == "●" for c in exp) else "extrapolated"
    if any((c.get("result") or {}).get("design") in ASSOC for c in cells):
        return "associational"
    if any((c.get("result") or {}).get("design") in ARGUMENT for c in cells):
        return "hypothesized"
    return "undetermined" if cells else "unknown"


SYMBOL = {"known": "◆ known", "extrapolated": "◇ extrap.", "associational": "△ assoc.",
          "hypothesized": "◌ hyp.", "undetermined": "? design", "unknown": "·"}


def cell_text(cells, profile):
    if not cells:
        return "·"
    d = Counter(c["result"]["direction"] for c in cells)
    dirs = " ".join(f"{k}{d[k]}" for k in ("+", "-", "0", "ns", "mixed") if d[k])
    n_exp = sum(1 for c in cells if c["result"].get("design") in EXPERIMENTAL)
    iv = sorted({c["_i"] for c in cells if isinstance(c.get("_i"), int)})
    size = f" i{iv[0]}" + (f"–{iv[-1]}" if len(iv) > 1 else "") if iv else ""
    m = Counter(match(c, profile) for c in cells) if profile else None
    fit = (" " + "".join(k * m[k] for k in ("●", "◎", "◐", "○", "?") if m[k])) if m else ""
    return f"{SYMBOL[status(cells, profile)]} · {dirs}{size} · {n_exp} exp{fit}"


def describe_sample(cells):
    parts = []
    for axis, field in (("L", "expertise"), ("L", "age"), ("G", "knowledge_type"), ("C", "setting")):
        vals = Counter((c.get(axis) or {}).get(field) for c in cells)
        vals.pop("?", None), vals.pop(None, None)
        unknown = len(cells) - sum(vals.values())
        s = ", ".join(f"{k} {v}" for k, v in vals.most_common(3))
        parts.append(f"{field.replace('_', ' ')}: {s or '—'}" + (f" (not reported {unknown})" if unknown else ""))
    return "; ".join(parts)


def render(page, profile, run="a"):
    by_claim = load_cells(run)
    title = re.search(r"^title: (.*)$", (WIKI_ROOT / f"{page}.md").read_text(encoding="utf-8"), re.M).group(1)
    title = title.strip().strip('"')
    out = [f"# Evidence map: {title}", ""]
    if profile:
        want = "; ".join(f"{a}.{f} = {v}" for a in ("L", "G", "C") for f, v in (profile.get(a) or {}).items())
        out += [f"**Designing for {profile.get('name', 'this profile')}:** {want}. "
                f"**Aiming at:** {', '.join(profile.get('O') or []) or 'not stated'}.", ""]
    out += [
        "Each cell: evidence status · directions found (+ better, - worse; for time and load, + means less, 0 no difference with power, ns not significant and "
        "inconclusive) · impact bin where the entry has one · how many results are experimental" +
        (" · fit to your learners, one mark per result, on expertise, age, knowledge type and setting (● at least three "
         "reported and all match yours; ◎ what is reported matches, but most is not reported; ◐ one differs; ○ two or more "
         "differ; ? none reported)" if profile else "") + ". A dot means no study in the wiki tested it: unknown, not zero.",
        "", "Status: ◆ known (experimental, and it matches your learners) · ◇ extrapolated (experimental, other learners or "
        "settings) · △ associational (no experiment) · ◌ hypothesized (argument only) · · unknown.", ""]
    aim = set(profile.get("O") or []) if profile else set()
    for q, claims in decisions(page):
        rows = defaultdict(list)
        for c in (x for cl in claims for x in by_claim.get(cl, []) if usable(x)):
            rows[c["D"]["variable"]].append(c)
        out += [f"## {q}", ""]
        if not rows:
            out += ["No coded cells: the claims this decision cites have no result quoted from a study's text.", ""]
            continue
        cols = [(name, outs) for name, outs in COLUMNS
                if any(c["O"]["outcome"] in outs for cs in rows.values() for c in cs) or aim & set(outs)]
        head = [f"{name}{' ★' if aim & set(outs) else ''}" for name, outs in cols]
        out += ["| Option | " + " | ".join(head) + " |", "|---" * (len(cols) + 1) + "|"]
        for var, cs in sorted(rows.items(), key=lambda kv: -len(kv[1])):
            ex = Counter(f"{c['D'].get('treatment')} vs {c['D'].get('comparison')}" for c in cs).most_common(1)[0][0]
            label = f"**{var}**<br><small>{ex[:90]}</small>"
            out.append("| " + label + " | " + " | ".join(
                cell_text([c for c in cs if c["O"]["outcome"] in outs], profile) for _, outs in cols) + " |")
        allc = [c for cs in rows.values() for c in cs]
        out += ["", f"*Who was studied* ({len(allc)} results): {describe_sample(allc)}.", ""]
    if aim:
        out += ["★ marks the outcomes you are aiming at."]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("page")
    ap.add_argument("--profile")
    ap.add_argument("--run", default="a")
    ap.add_argument("--out")
    a = ap.parse_args()
    profile = json.loads(Path(a.profile).read_text(encoding="utf-8")) if a.profile else None
    text = render(a.page, profile, a.run)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
