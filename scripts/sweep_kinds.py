#!/usr/bin/env python3
"""
sweep_kinds.py — re-decide the element, theory and design pages batches wrote before
products/, research-methods/ and the element/theory ledger existed.

Batches 16–47 wrote one element and theory page per source, and the candidate settle
step wrote designs for named programmes. Many of those are what the wiki now files
elsewhere (maintainer, 2026-10-10): a product or programme others adopt (Edmentum Exact
Path, the Teacher Incentive Fund), one programme's own framework or indicator, or an
education research method. This treats each such page as a ledger candidate and asks
what it is now, with the same decision settle_candidates.decide() gives a new candidate:

    elements, theories (not canonical): attach (fold into the canonical page), product,
        research-method, or anything else (left as it is)
    designs: product (a branded programme many sites adopt) or design (left as it is)

Every move needs a second, independent read by another model that agrees; a page on
which the two disagree is left where it is. A confirmed move:

    attach            merge_pages.py folds the page into its canonical page (an alias)
    product, method   settle_candidates.write_named() writes or extends the page for
                      that name, then merge_pages.py folds the old page into it across
                      kinds, so its links are repointed and its body kept in a comment

Decisions go to eval/candidates/sweep-kinds.ndjson, first read and second together.

    python3 scripts/sweep_kinds.py                 # dry run: counts and a sample
    python3 scripts/sweep_kinds.py --apply
"""
import argparse
import collections
import concurrent.futures
import json
import os
import re
import sqlite3
import subprocess
import sys
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import link_pages as lp  # noqa: E402
import search_index  # noqa: E402
import settle_candidates as sc  # noqa: E402

OUT = WIKI_ROOT / "eval" / "candidates" / "sweep-kinds.ndjson"
SECOND_MODEL = "deepseek/deepseek-v4-pro"

KIND_PROMPT = """A learning-design wiki is re-filing pages a batch wrote, one per source, before it had
kinds for products and research methods.
- An ELEMENT is a general building block of instruction, reusable across courses (worked examples, a rubric).
- A THEORY is a general explanatory framework of how people learn or are taught.
- A DESIGN is one setting's design: a course, a lesson sequence, one site's implementation.
- A PRODUCT OR PROGRAMME is a named thing others adopt or use: software or a platform, a curriculum or
  programme package, an assessment or measurement instrument, a dataset, a branded intervention or initiative
  offered to many sites; one programme's own framework, indicator, tool or report belongs to that programme.
- A RESEARCH METHOD is a method for studying learning or evaluating education, specific to education or
  especially useful there. A general social-science method is not one.

PAGE (now filed as a {kind}): {title}
{description}

Is it rightly a {kind} ("keep"), a product or programme or one's component ("product"), or a research
method ("research-method")?
Reply: {{"outcome": "keep", "product" or "research-method", "name": <the product or programme it is or
 belongs to, as its maker names it, or the method's name>, "product_kind": <software, curriculum,
 assessment, dataset, programme or framework>, "product_description": <one sentence on what that product or
 programme is and who makes or runs it>, "why": "one sentence"}}"""

NAMES_PROMPT = """These are names of products, programmes and research methods a wiki is about to give pages,
sorted alphabetically. Several may name the same thing in different words ("5Essentials Survey" and
"5Essentials Survey (My Voice, My School survey)"; "MAP Growth" and "NWEA MAP Growth assessment"). Map every
name to one canonical name: the shortest name its maker uses. Map a component to its programme only if the
name itself says so. Leave distinct things distinct.
{names}
Reply: {{"map": {{"<name as given>": "<canonical name>", ...}}}}  (every name given, exactly as given)"""

CONFIRM_PROMPT = """A learning-design wiki is re-filing old pages. A first reader proposed a move for the page
below; check it independently.

PAGE (now a {kind}): {title}
{description}

PROPOSED: {proposal}

What the kinds mean: an ELEMENT is a general building block of instruction, reusable across courses; a
THEORY is a general explanatory framework of how people learn or are taught; a PRODUCT OR PROGRAMME is a
named thing others adopt (software, curriculum package, assessment or instrument, dataset, branded
intervention or initiative), and one programme's own framework, indicator or tool belongs on that
programme's page; a RESEARCH METHOD is a method for studying learning or evaluating education that is
specific to education or especially useful there (a general social-science method is not one); a
DESIGN is one setting's course or implementation. Folding into a canonical page is right only when the page
states that page's idea, or a narrower case of it.
Reply: {{"agree": true or false, "why": "one clause"}}"""


def page_candidates(kinds: tuple) -> list:
    """Batch-written element and theory pages (a canonical one too: 10+ inbound links
    made some products canonical, the 5Essentials survey and MAP Growth among them),
    and every design page. A page carries `canonical` so the first read knows whether
    folding it into a canonical page is an option."""
    canon = sc.canonical_keys()
    source = {}
    for line in (WIKI_ROOT / "sources" / "manifest.ndjson").read_text(encoding="utf-8").splitlines():
        e = json.loads(line)
        if e.get("status") == "ingested":
            for p in e.get("pages") or []:
                source.setdefault(p[:-3], (e["id"], e.get("title", "")))
    out = []
    for folder in kinds:
        for path in sorted((WIKI_ROOT / folder).glob("*.md")):
            key = f"{folder}/{path.stem}"
            if path.stem == "index":
                continue
            text = path.read_text(encoding="utf-8")
            if folder != "designs" and "process:wiki-ingest" not in text[:800]:
                continue                  # written by hand or by an agent, not by a batch
            rec = lp.record(key, path)
            aid, atitle = source.get(key, (f"page:{key}", ""))
            ks = re.search(r"^## Key Sources\s*\n- (.+)$", text, re.M)
            claims = [{"slug": m.group(1), "tag": m.group(2)}
                      for m in re.finditer(r"\]\(\.\./claims/([^)#\s]+)\.md\)\s*\[([+~-][SMW])\]", text)]
            out.append({"id": f"page:{key}", "page": key, "article_id": aid, "article_title": atitle,
                        "type": folder[:-1] if folder != "theories" else "theory", "slug": path.stem,
                        "title": rec["title"], "description": lp._desc_section(path) or rec["description"],
                        "claims_cited": claims, "citation": ks.group(1) if ks else None, "origin": "page",
                        "canonical": key in canon})
    return out


def first_reads(cands: list, model: str, concurrency: int) -> list:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    key = os.environ["OPENROUTER_API_KEY"]
    et = [c for c in cands if c["type"] in ("element", "theory") and not c["canonical"]]
    designs = [c for c in cands if c["type"] == "design" or c["canonical"]]
    out = sc.settle(et, [], model, concurrency) if et else []

    def design_read(c):
        try:
            gen = oc.generate(model, "Reply with JSON only.", KIND_PROMPT.format(
                kind=c["type"], title=c["title"], description=(c["description"] or "")[:900]), key, max_tokens=4000)
            d = extract_json(gen.raw_text) or {}
            o = d.get("outcome") if d.get("outcome") in ("keep", "product", "research-method") else "error"
            r = {"id": c["id"], "outcome": o, "why": d.get("why"), "cost_usd": gen.cost_usd}
            if o == "research-method":
                r["name"] = (d.get("name") or c["title"]).strip()
            if o == "product":
                r.update(name=(d.get("name") or c["title"]).strip(), product_kind=d.get("product_kind")
                         if d.get("product_kind") in sc.PRODUCT_KINDS else None,
                         product_description=d.get("product_description"))
            return r
        except Exception as e:
            return {"id": c["id"], "outcome": "error", "why": str(e)[:200], "cost_usd": 0}

    with concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        out += list(ex.map(design_read, designs))
    return out


def consolidate_names(decs: list, model: str) -> int:
    """One name per product or method across the run: decisions are made in parallel,
    so the settle prompt's list of existing pages cannot stop two reads naming one
    programme two ways. Names are sent in alphabetical chunks, so variants sit together."""
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    key = os.environ["OPENROUTER_API_KEY"]
    names = sorted({d["name"] for d in decs if d.get("name")}, key=str.lower)
    mapping = {}
    for i in range(0, len(names), 120):
        chunk = names[i:i + 120]
        try:
            gen = oc.generate(model, "Reply with JSON only.", NAMES_PROMPT.format(names="\n".join(chunk)), key,
                              max_tokens=16000)
            m = (extract_json(gen.raw_text) or {}).get("map") or {}
            mapping.update({k: v for k, v in m.items() if k in chunk and isinstance(v, str) and v.strip()})
        except Exception:
            pass
    n = 0
    for d in decs:
        if d.get("name") in mapping and mapping[d["name"]] != d["name"]:
            d["name_as_read"], d["name"] = d["name"], mapping[d["name"]].strip()
            n += 1
    return n


def follow_moved_targets(cands: dict, decs: list) -> int:
    """A fold into a canonical page that is itself being re-filed as a product or method
    goes with it: the page becomes a component of that product instead."""
    moved = {cands[d["id"]]["page"]: d for d in decs if d["outcome"] in ("product", "research-method")
             and d.get("confirmed")}
    n = 0
    for d in decs:
        t = moved.get(d.get("target")) if d["outcome"] == "attach" else None
        if t:
            d.update(outcome=t["outcome"], name=t["name"], product_kind=t.get("product_kind"),
                     product_description=t.get("product_description"), followed=d.pop("target"))
            n += 1
    return n


def proposal_text(d: dict, pages_title) -> str:
    if d["outcome"] == "attach":
        return f"fold it into the canonical page \"{pages_title(d['target'])}\" ({d['target']})"
    if d["outcome"] == "product":
        return f"re-file it as the product or programme \"{d['name']}\" (or a component of it)"
    return f"re-file it as the research method \"{d['name']}\""


def second_reads(cands: dict, decs: list, model: str, concurrency: int) -> list:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    key = os.environ["OPENROUTER_API_KEY"]
    titles = {}

    def title(k):
        if k not in titles:
            p = WIKI_ROOT / f"{k}.md"
            titles[k] = lp.record(k, p)["title"] if p.exists() else k
        return titles[k]

    def one(d):
        c = cands[d["id"]]
        prompt = CONFIRM_PROMPT.format(kind=c["type"], title=c["title"], description=(c["description"] or "")[:900],
                                       proposal=proposal_text(d, title))
        try:
            gen = oc.generate(model, "Reply with JSON only.", prompt, key, max_tokens=4000)
            v = extract_json(gen.raw_text) or {}
            return {**d, "confirmed": bool(v.get("agree")), "second_why": v.get("why"),
                    "second_model": model, "cost_usd": (d.get("cost_usd") or 0) + (gen.cost_usd or 0)}
        except Exception as e:
            return {**d, "confirmed": False, "second_why": f"error: {e}"[:200], "second_model": model}

    with concurrent.futures.ThreadPoolExecutor(concurrency) as ex:
        return list(ex.map(one, decs))


def apply(cands: dict, decs: list, actor: str) -> collections.Counter:
    import merge_pages
    done = collections.Counter()
    for d in sorted(decs, key=lambda d: d["outcome"] == "attach"):
        c = cands[d["id"]]
        folder, slug = c["page"].split("/")
        if not (WIKI_ROOT / f"{c['page']}.md").exists():
            continue                      # already folded by an earlier decision
        if d["outcome"] == "attach":
            kfolder, keep = d["target"].split("/")
            if kfolder != folder or not (WIKI_ROOT / f"{d['target']}.md").exists():
                continue
            merge_pages.merge(folder, keep, slug, True)
            done["attach"] += 1
        else:
            dest = sc.write_named(c, d, actor)
            if not dest:
                continue
            dfolder, dslug = dest[:-3].split("/")
            merge_pages.merge(dfolder, dslug, c["page"], True)
            done[d["outcome"]] += 1
    return done


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--kinds", nargs="+", default=["elements", "theories", "designs"])
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--model", default=sc.DEFAULT_MODEL)
    ap.add_argument("--second-model", default=SECOND_MODEL)
    ap.add_argument("--concurrency", type=int, default=12)
    ap.add_argument("--by", default="process:sweep-kinds")
    ap.add_argument("--no-attach", action="store_true",
                    help="apply only the re-filings (products, methods), not plain folds into a canonical page")
    ap.add_argument("--from", dest="from_file", help="apply decisions from an earlier run without asking again")
    args = ap.parse_args()
    cands = {c["id"]: c for c in page_candidates(tuple(args.kinds))}
    if args.from_file:
        decs = [json.loads(l) for l in Path(args.from_file).read_text(encoding="utf-8").splitlines() if l.strip()]
        decs = [d for d in decs if d["id"] in cands]
    else:
        todo = list(cands.values())[:args.limit] if args.limit else list(cands.values())
        print(f"first read of {len(todo)} pages with {args.model}", flush=True)
        firsts = first_reads(todo, args.model, args.concurrency)
        print("first reads:", dict(collections.Counter(d["outcome"] for d in firsts)), flush=True)
        moves = [d for d in firsts if d["outcome"] in ("attach", "product", "research-method")]
        print(f"product and method names merged: {consolidate_names(moves, args.model)}", flush=True)
        print(f"second read of {len(moves)} proposed moves with {args.second_model}", flush=True)
        decs = second_reads(cands, moves, args.second_model, args.concurrency)
        print(f"folds that follow a re-filed target: {follow_moved_targets(cands, decs)}", flush=True)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        stamp = date.today().isoformat()
        with OUT.open("a", encoding="utf-8") as fh:
            for d in decs:
                fh.write(json.dumps({**d, "page": cands[d["id"]]["page"], "at": stamp}, ensure_ascii=False) + "\n")
        cost = sum(d.get("cost_usd") or 0 for d in firsts) + sum(
            (d.get("cost_usd") or 0) for d in decs) - sum(d.get("cost_usd") or 0 for d in moves)
        print(f"cost ${cost:.2f}; decisions -> {OUT.relative_to(WIKI_ROOT)}")
    ok = [d for d in decs if d.get("confirmed") and not (args.no_attach and d["outcome"] == "attach")]
    by = collections.Counter((cands[d["id"]]["type"], d["outcome"]) for d in ok)
    print("confirmed moves:", dict(by), "| refused:", sum(1 for d in decs if not d.get("confirmed")))
    for d in ok[:25]:
        c = cands[d["id"]]
        print(f"  {d['outcome']:15} {c['page']} -> {d.get('target') or d.get('name')}")
    if args.apply:
        print("applied:", dict(apply(cands, ok, args.by)))
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "add_type_banner.py"), "--apply"],
                       cwd=WIKI_ROOT, capture_output=True)
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "add_evidence_profile.py"), "--apply"],
                       cwd=WIKI_ROOT, capture_output=True)
        subprocess.run([sys.executable, str(WIKI_ROOT / "scripts" / "build_indexes.py")], cwd=WIKI_ROOT,
                       capture_output=True)


if __name__ == "__main__":
    main()
