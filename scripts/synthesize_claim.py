#!/usr/bin/env python3
"""
synthesize_claim.py — gather the single-study claims that bear on one general claim into a table of
the distinct studies behind it.

Extraction writes one claim per finding per article, so 97% of claims rest on one study, and a
designer reading any one of them sees one study's result rather than what the literature says. The
principle pages were the only place evidence came together. This adds the missing level: a general
claim (the hub) carries a `## Studies bearing on this claim` table, one row per DISTINCT study, built
from the evidence entries of the hub and of the narrower claims that bear on it (its members).

What the table does and does not do, following CLAUDE.md's evidence rules:

- It counts distinct studies, never claims: a study is its DOI, or its first author and year where
  it has none, so a meta-analysis cited by six claims is one row.
- It copies each entry's codes as written (design tier, kind and rigour, the effect size as
  printed). Nothing is re-judged, converted or averaged, and there is no verdict: the header gives
  counts and the range of design tiers.
- Each member's direction relative to the hub (supports, qualifies, counts against) comes from the
  spec, which a person or agent writes after reading the claims, and is shown per claim.
- Members are not folded or edited, apart from a `## Related Claims` link up to the hub.

The grouping lives in a spec, so it can be reviewed and re-run; the table sits between
<!-- synthesis:start --> and <!-- synthesis:end --> markers and a re-run replaces it.

    python3 scripts/synthesize_claim.py eval/synthesis/retrieval-practice.json --check
    python3 scripts/synthesize_claim.py eval/synthesis/retrieval-practice.json --apply
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
import okf_lib  # noqa: E402

BEARS = {"+": "supports", "~": "qualifies", "-": "counts against"}
KINDS = r"(causal|quant-synthesis|review|associational|qualitative|design|theoretical) · r[1-3?]"
START, END = "<!-- synthesis:start -->", "<!-- synthesis:end -->"
SECTION = "## Studies bearing on this claim"


def resolve(prefix: str) -> str:
    hits = [p.stem for p in (WIKI_ROOT / "claims").glob(f"{prefix}*.md")]
    exact = [h for h in hits if h == prefix]
    if exact:
        return exact[0]
    if len(hits) != 1:
        sys.exit(f"claim prefix {prefix!r} matches {len(hits)} pages")
    return hits[0]


def title_of(slug: str) -> str:
    fm_lines, _ = okf_lib.split_frontmatter((WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8"))
    return str(okf_lib.parse_frontmatter_scalars(fm_lines).get("title") or slug).replace("[", "(").replace("]", ")")


def entries(slug: str) -> list:
    """[{heading, citation, doi, q, i, kind}] for each evidence entry on a claim page, outside comments."""
    text = (WIKI_ROOT / "claims" / f"{slug}.md").read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    ev = text.split("\n## Evidence", 1)[1] if "\n## Evidence" in text else ""
    ev = re.split(r"\n## (?!#)", ev, maxsplit=1)[0]
    out = []
    for block in re.split(r"^### ", ev, flags=re.M)[1:]:
        lines = block.split("\n")
        heading = lines[0].strip()
        body = [l for l in lines[1:] if l.strip()]
        citation = next((l for l in body if not l.startswith("`") and not l.startswith(">")), "")
        codes = next((l for l in body if l.startswith("`q")), "")
        spans = re.findall(r"`([^`]*)`", codes)
        joined = " · ".join(spans)
        q = re.search(r"\bq([1-4?])\b[^·`]*", joined)
        i = re.search(r"\bi([0-3?])\b(?:\s*·\s*(?!\s*(?:causal|quant-synthesis|review|associational|qualitative|"
                      r"design|theoretical)\b|\s*n=|\s*r[1-3?]\b)([^·`]*))?", joined)
        kind = re.search(KINDS, joined)
        # A DOI may carry balanced parentheses (10.1016/s0959-4752(01)00011-5); stopping at the first ")"
        # truncated it, and the table linked a DOI that does not resolve (2026-10-14).
        doi = re.search(r"10\.\d{4,9}/(?:[^\s()\]>]|\([^\s()]*\))+", citation)
        out.append({"heading": heading, "citation": citation,
                    "doi": doi.group(0).rstrip(".,;").lower() if doi else None,
                    "q": q.group(0).strip() if q else "q?",
                    "i": (f"i{i.group(1)}" + (f" · {i.group(2).strip()}" if i.group(2) else "")) if i else "i?",
                    "kind": kind.group(0) if kind else ""})
    return out


def study_key(e: dict) -> str:
    if e["doi"]:
        return "doi:" + e["doi"]
    m = re.match(r"([^\d(]+?)\s*(?:et al\.?|and [^\d]+|& [^\d]+)?\s*\(?(\d{4})", e["heading"])
    if m:
        return f"{m.group(1).strip().lower().split()[-1]}-{m.group(2)}"
    return e["heading"].lower()


def build(finding: dict) -> tuple:
    hub = resolve(finding["hub"])
    members = [(resolve(p), d) for p, d in finding["members"]]
    studies = collections.OrderedDict()
    for slug, bearing in [(hub, "hub")] + members:
        for e in entries(slug):
            k = study_key(e)
            s = studies.setdefault(k, {"entry": e, "q": set(), "i": [], "claims": []})
            s["q"].add(e["q"])
            if e["i"] not in s["i"]:
                s["i"].append(e["i"])
            if (slug, bearing) not in s["claims"]:
                s["claims"].append((slug, bearing))
    return hub, members, studies


def table(hub: str, members: list, studies: dict, question: str) -> str:
    tiers = sorted({re.match(r"q([1-4])", q).group(1) for s in studies.values() for q in s["q"] if re.match(r"q[1-4]", q)})
    kinds = collections.Counter((s["entry"]["kind"].split(" · ")[0] or "kind not coded") for s in studies.values())
    with_es = sum(1 for s in studies.values() if any(re.match(r"i[0-3]\b", i) for i in s["i"]))
    rows = []
    for s in studies.values():
        e = s["entry"]
        name = e["heading"]
        if e["doi"]:
            url = f"https://doi.org/{e['doi']}"
            name = f"[{name}](<{url}>)" if "(" in url else f"[{name}]({url})"   # a bare ")" ends the link
        design = " / ".join(sorted(s["q"])) + (f" · {e['kind']}" if e["kind"] else "")
        effect = "; ".join(s["i"]).replace("|", "/")
        via = "; ".join(("this claim" if b == "hub" else f"[{title_of(c)[:90]}]({c}.md) ({BEARS[b]})")
                        for c, b in s["claims"])
        rows.append(f"| {name} | {design} | {effect} | {via} |")
    tier = (f"`q{tiers[0]}`–`q{tiers[-1]}`" if len(tiers) > 1 else f"`q{tiers[0]}`") if tiers else "no design tier coded"
    head = (f"{SECTION}\n\n{START}\n"
            f"*{question}* This table gathers the studies behind this claim and the {len(members)} narrower "
            f"claims that bear on it: **{len(studies)} distinct studies** "
            f"({', '.join(f'{v} {k}' for k, v in kinds.most_common())}), {tier}, "
            f"{with_es} of {len(studies)} with an effect size coded. One row per study, codes as each entry "
            f"records them; no effect is averaged and no verdict is drawn. Built by "
            f"`scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the "
            f"claim it comes from.\n\n"
            f"| Study | Design | Effect as recorded | Bears on this claim through |\n|---|---|---|---|\n")
    return head + "\n".join(rows) + f"\n{END}\n"


def write_hub(hub: str, block: str) -> None:
    path = WIKI_ROOT / "claims" / f"{hub}.md"
    text = path.read_text(encoding="utf-8")
    if START in text:
        text = re.sub(re.escape(SECTION) + r"\n\n" + re.escape(START) + r".*?" + re.escape(END) + r"\n",
                      lambda m: block, text, count=1, flags=re.S)
    else:
        anchor = next((h for h in ("\n## Discussion", "\n## Related Claims") if h in text), None)
        text = text.replace(anchor, "\n" + block + anchor, 1) if anchor else text.rstrip("\n") + "\n\n" + block
    path.write_text(text, encoding="utf-8")


def link_up(member: str, hub: str) -> bool:
    path = WIKI_ROOT / "claims" / f"{member}.md"
    text = path.read_text(encoding="utf-8")
    if f"]({hub}.md)" in re.sub(r"<!--.*?-->", "", text, flags=re.S):
        return False
    bullet = f"- [{title_of(hub)}]({hub}.md) — the general claim this finding bears on, with the studies behind it"
    if "\n## Related Claims" in text:
        text = text.replace("\n## Related Claims\n", f"\n## Related Claims\n\n{bullet}\n", 1)
    else:
        text = text.rstrip("\n") + f"\n\n## Related Claims\n\n{bullet}\n"
    path.write_text(re.sub(r"\n{3,}", "\n\n", text), encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    linked = 0
    for f in spec["findings"]:
        hub, members, studies = build(f)
        claims = 1 + len(members)
        print(f"{hub}: {claims} claims -> {len(studies)} distinct studies")
        if args.apply:
            write_hub(hub, table(hub, members, studies, f["question"]))
            linked += sum(link_up(m, hub) for m, _ in members)
    if args.apply:
        print(f"{linked} member claim(s) given a link up to their hub")


if __name__ == "__main__":
    main()
