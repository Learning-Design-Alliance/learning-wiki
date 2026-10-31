#!/usr/bin/env python3
"""
screen_sources.py — screen a defined universe of candidate sources by abstract, before anything is
ingested, so that "every source in it was reviewed" is a statement the record can back.

Topic search added volume by taking the top few hits per wiki topic, so there was never a list of
"the remaining ERIC and PubMed articles" to finish. This defines one: a universe is a saved query
against a source's own search API (UNIVERSES below), frozen as an id list, and every member gets a
recorded decision:

  1. --build <universe>   run the query, save each member's id, title, year and DOI to
                          eval/screening/<universe>.ndjson (committed), and its abstract to
                          eval/runs/screening/<universe>-abstracts.ndjson (ignored: abstracts are the
                          publishers', not ours to republish).
  2. --screen <universe>  two models from different families read each abstract against
                          INCLUSION.md. Their votes go to eval/screening/decisions.ndjson (committed).
  3. --record <universe>  settle each member: a source the manifest already holds is left as it is;
                          one both models exclude is written to sources/manifest.ndjson as rejected,
                          with its INCLUSION.md code; every other one passes, and is written to an
                          ingest queue (eval/runs/queues/screen-<universe>.ndjson) for a person to
                          approve. A split vote passes: INCLUSION.md's default is to include.

Nothing here ingests. A pass means "worth reading in full", and the full read happens only in an
approved batch, whose extraction can still reject it.

    python3 scripts/screen_sources.py --build pmc-teaching-trials
    python3 scripts/screen_sources.py --screen pmc-teaching-trials --limit 50   # pilot: check cost
    python3 scripts/screen_sources.py --screen pmc-teaching-trials
    python3 scripts/screen_sources.py --record pmc-teaching-trials
    python3 scripts/screen_sources.py --summary
"""
import argparse
import collections
import concurrent.futures
import html
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

import requests

WIKI_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(WIKI_ROOT))
import okf_lib  # noqa: E402

SCREEN_DIR = WIKI_ROOT / "eval" / "screening"
DECISIONS = SCREEN_DIR / "decisions.ndjson"
CACHE_DIR = WIKI_ROOT / "eval" / "runs" / "screening"
QUEUE_DIR = WIKI_ROOT / "eval" / "runs" / "queues"
MODELS = ("z-ai/glm-5.3-flash", "openai/gpt-5.6-luna")
EXCLUDE_CODES = ("opinion-piece", "out-of-scope", "no-ingestable-content")
CONTACT = os.environ.get("EVAL_HARNESS_CONTACT_EMAIL", "contact@learningdesignalliance.org")

ERIC_URL = "https://api.ies.ed.gov/eric/"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# A universe's query is part of its definition: changing one is defining a new universe, so give it
# a new name rather than editing a query whose members were already screened.
UNIVERSES = {
    "eric-intervention-studies": {
        "source": "eric",
        "query": ('e_fulltextauth:1 AND peerreviewed:T AND publicationdateyear:[2010 TO 2026] AND '
                  'publicationtype:"Reports - Research" AND '
                  '(subject:"Instructional Effectiveness" OR subject:"Intervention" OR subject:"Teaching Methods") AND '
                  '(subject:"Experimental Groups" OR subject:"Quasiexperimental Design" OR '
                  'subject:"Randomized Controlled Trials" OR subject:"Control Groups" OR subject:"Meta Analysis")'),
        "note": "ERIC-hosted full text, peer reviewed, research reports since 2010, indexed as instruction "
                "or intervention studies with an experimental, quasi-experimental, RCT or meta-analytic design",
    },
    "pmc-teaching-trials": {
        "source": "pmc",
        "query": ('open access[filter] AND ("Teaching"[MeSH Major Topic] OR "Educational Measurement"[MeSH Major Topic] '
                  'OR "Computer-Assisted Instruction"[MeSH Major Topic] OR "Simulation Training"[MeSH Major Topic]) '
                  'AND (randomized controlled trial[pt] OR meta-analysis[pt]) AND 2010:2026[pdat]'),
        "note": "PMC open access since 2010, with teaching, educational measurement, computer-assisted "
                "instruction or simulation training as a major MeSH topic, typed RCT or meta-analysis",
    },
    # arXiv's search API is closed to automated clients (robots.txt), so this universe is read from the
    # Kaggle metadata snapshot (--snapshot, or ARXIV_SNAPSHOT). Its query is the filter below, applied to
    # every record: physics.ed-ph in any category, or a primary category among ARXIV_CS_CATEGORIES with
    # an education term and a learning-outcome term in the title or abstract.
    "arxiv-education-research": {
        "source": "arxiv",
        "query": "categories contains physics.ed-ph; or primary in cs.CY, cs.HC, cs.AI, cs.CL, cs.LG, stat.AP "
                 "and title+abstract match ARXIV_EDU and ARXIV_OUTCOME",
        "note": "arXiv physics education research, and computing and statistics papers about learners "
                "or instruction that name a learning outcome or an experimental design",
    },
}

ARXIV_CS_CATEGORIES = ("cs.CY", "cs.HC", "cs.AI", "cs.CL", "cs.LG", "stat.AP")
ARXIV_EDU = re.compile(r"\b(students?|learners?|pupils?|classroom|teachers?|tutor(ing)?|instruction(al)?|"
                       r"curricul\w*|courses?|courseware|education(al)?|MOOCs?)\b", re.I)
ARXIV_OUTCOME = re.compile(r"(learning (outcomes?|gains?)|achievement|post-?test|pre-?test|randomi[sz]ed|"
                           r"controlled (trial|experiment)|quasi-experiment|effect size|meta-analy|"
                           r"improv\w* (learning|performance|understanding)|experimental (group|condition))", re.I)

PROMPT = """You are screening a source for a learning-design wiki, from its title and abstract only.
The default is to INCLUDE. Anyone designing learning, in any setting, uses this wiki.

Include when all three hold:
I1. It is about learning or designing for it, in any setting (schools, universities, workplaces, health
    professions, clinical training, military, museums, families, sport, online), any age, any domain.
    Design processes, teachers, programme evaluation and educational technology are in.
I2. It offers something extractable: a finding, a reasoned argument, a model, a design method, a
    described practice, or a synthesis.
I3. It gives evidence or reasoning for what it proposes. Strength of evidence never decides inclusion.
A narrow population or unusual setting is NEVER a reason to exclude. Every research paradigm is in.

Exclude only for one of these:
- opinion-piece: asserts positions with neither data nor a developed argument (editorial, commentary).
- out-of-scope: not about learning or its design. The test is the subject, not the domain: how nurses
  learn a procedure is in; nurse staffing levels are out. A patient-education or health-promotion study
  is in only if what it tests is how people learn (an instructional design, a teaching method, a
  training programme, learning outcomes); a trial whose outcome is a clinical or health result of a
  treatment is out. A research-methods paper is out unless it helps someone design an intervention.
- no-ingestable-content: nothing to extract (a protocol announcement with no results, an erratum, a
  table of contents, a bare bibliography).
When in doubt, include.

Title: {title}
Publication type: {ptype}
Abstract: {abstract}

Reply with JSON only: {{"decision": "include" or "exclude", "code": null or one of "opinion-piece",
"out-of-scope", "no-ingestable-content", "reason": "<one sentence>"}}"""


def _get(url, params, tries=5):
    for attempt in range(tries):
        try:
            r = requests.get(url, params=params, timeout=60)
            if r.status_code in (429, 500, 502, 503):
                time.sleep(int(r.headers.get("Retry-After") or 2 ** (attempt + 1)))
                continue
            r.raise_for_status()
            return r
        except requests.RequestException:
            if attempt == tries - 1:
                raise
            time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"{url}: gave up after {tries} tries")


def build_eric(spec):
    members, start = [], 0
    while True:
        resp = _get(ERIC_URL, {"search": spec["query"], "format": "json", "rows": 200, "start": start,
                               "fields": "id,title,publicationdateyear,description,publicationtype,author,doi"})
        body = resp.json()["response"]
        for d in body["docs"]:
            eid = d["id"].strip()
            members.append({
                "id": f"eric-{eid.lower()}", "title": html.unescape(d.get("title") or "").strip(),
                "year": d.get("publicationdateyear"),
                "doi": (d.get("doi") or "").lower() or None,
                "ptype": "; ".join(d.get("publicationtype") or []),
                "authors": ", ".join(d.get("author") or []) or "et al.",
                "abstract": html.unescape(d.get("description") or "").strip(),
                "url": f"https://eric.ed.gov/?id={eid}",
                "fetch_url": f"https://files.eric.ed.gov/fulltext/{eid}.pdf",
            })
        start += 200
        if start >= body["numFound"]:
            return members
        time.sleep(2)


def build_pmc(spec):
    search = _get(EUTILS + "esearch.fcgi", {"db": "pmc", "term": spec["query"], "retmax": 100000,
                                            "retmode": "json", "email": CONTACT}).json()["esearchresult"]
    uids = search["idlist"]
    print(f"{len(uids)} PMC ids", flush=True)
    members = {}
    for i in range(0, len(uids), 200):
        chunk = uids[i:i + 200]
        res = _get(EUTILS + "esummary.fcgi", {"db": "pmc", "id": ",".join(chunk), "retmode": "json",
                                              "email": CONTACT}).json().get("result", {})
        for uid in chunk:
            doc = res.get(uid)
            if not isinstance(doc, dict) or not (doc.get("title") or "").strip():
                continue
            ids = {a.get("idtype"): a.get("value") for a in doc.get("articleids", [])}
            m = re.search(r"\b(19|20)\d{2}\b", doc.get("pubdate") or doc.get("epubdate") or "")
            members[uid] = {
                "id": f"pmc-{uid}", "title": html.unescape(re.sub(r"<[^>]+>", "", doc["title"])).strip(),
                "year": int(m.group(0)) if m else None, "doi": (ids.get("doi") or "").lower() or None,
                "pmid": ids.get("pmid"), "ptype": "", "abstract": "",
                "authors": ", ".join(a.get("name", "") for a in doc.get("authors", []) if a.get("name")) or "et al.",
                "url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{uid}",
                "fetch_url": f"https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC{uid}.1.json",
                "pmcid": f"PMC{uid}",
            }
        time.sleep(0.4)
    # Abstracts and publication types come from PubMed, whose records are small; the PMC record is the
    # whole article.
    by_pmid = {m["pmid"]: m for m in members.values() if m.get("pmid")}
    pmids = list(by_pmid)
    for i in range(0, len(pmids), 200):
        xml = _get(EUTILS + "efetch.fcgi", {"db": "pubmed", "id": ",".join(pmids[i:i + 200]),
                                            "retmode": "xml", "email": CONTACT}).text
        for art in ET.fromstring(xml).iter("PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID")
            m = by_pmid.get(pmid)
            if m is None:
                continue
            m["abstract"] = " ".join("".join(t.itertext()).strip() for t in art.iter("AbstractText")).strip()
            m["ptype"] = "; ".join(t.text for t in art.iter("PublicationType") if t.text)
        time.sleep(0.4)
    return list(members.values())


def build_arxiv(snapshot):
    path = snapshot or os.environ.get("ARXIV_SNAPSHOT")
    if not path or not Path(path).exists():
        sys.exit("arXiv needs the Kaggle metadata snapshot: --snapshot <arxiv-metadata-oai-snapshot.json>")
    members = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            p = json.loads(line)
            cats = (p.get("categories") or "").split()
            text = f"{p.get('title') or ''} {p.get('abstract') or ''}"
            if not ("physics.ed-ph" in cats or (cats and cats[0] in ARXIV_CS_CATEGORIES
                                                 and ARXIV_EDU.search(text) and ARXIV_OUTCOME.search(text))):
                continue
            aid = p["id"].strip()
            versions = p.get("versions") or []
            m = re.search(r"\b(19|20)\d{2}\b", str(versions[0].get("created") if versions else p.get("update_date")))
            members.append({
                "id": f"arxiv-{aid}", "title": " ".join((p.get("title") or "").split()),
                "year": int(m.group(0)) if m else None, "doi": (p.get("doi") or "").lower() or None,
                "ptype": f"arXiv preprint ({' '.join(cats)})" + (f"; published as {p['journal-ref']}"
                                                                 if p.get("journal-ref") else ""),
                "authors": p.get("authors") or "et al.",
                "abstract": " ".join((p.get("abstract") or "").split()),
                "url": f"https://arxiv.org/abs/{aid}", "fetch_url": f"https://arxiv.org/pdf/{aid}",
            })
    return members


def build(name, snapshot=None):
    spec = UNIVERSES[name]
    members = {"eric": build_eric, "pmc": build_pmc}[spec["source"]](spec) if spec["source"] != "arxiv" \
        else build_arxiv(snapshot)
    SCREEN_DIR.mkdir(parents=True, exist_ok=True)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with (SCREEN_DIR / f"{name}.ndjson").open("w", encoding="utf-8") as fh:
        fh.write(json.dumps({"universe": name, "source": spec["source"], "query": spec["query"],
                             "note": spec["note"], "built": date.today().isoformat(),
                             "members": len(members)}) + "\n")
        for m in members:
            fh.write(json.dumps({k: m.get(k) for k in ("id", "title", "year", "doi")}, ensure_ascii=False) + "\n")
    with (CACHE_DIR / f"{name}-abstracts.ndjson").open("w", encoding="utf-8") as fh:
        for m in members:
            fh.write(json.dumps(m, ensure_ascii=False) + "\n")
    print(f"{name}: {len(members)} members, {sum(1 for m in members if m['abstract'])} with an abstract")


def load_members(name):
    path = CACHE_DIR / f"{name}-abstracts.ndjson"
    if not path.exists():
        sys.exit(f"no abstracts for {name}: run --build {name} first")
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def settled_ids():
    """Source ids, and DOIs, the manifest already holds a verdict or an ingest for."""
    ids, dois = set(), set()
    for e in okf_lib.load_manifest():
        if not okf_lib.manifest_rejection_is_final(e):
            continue   # a failed run says nothing about the source, so it is screened like any other
        ids.add(e.get("id"))
        if e.get("doi"):
            dois.add(str(e["doi"]).lower())
    return ids, dois


def decided():
    out = {}
    if DECISIONS.exists():
        for line in DECISIONS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                d = json.loads(line)
                out[(d["universe"], d["id"])] = d
    return out


def ask(model, m, key):
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    gen = oc.generate(model, "Reply with one JSON object.",
                      PROMPT.format(title=m["title"], ptype=m.get("ptype") or "not given",
                                    abstract=(m.get("abstract") or "(no abstract available)")[:6000]),
                      key, max_tokens=1500)
    d = extract_json(gen.raw_text) or {}
    dec = str(d.get("decision") or "").strip().lower()
    code = d.get("code") if d.get("code") in EXCLUDE_CODES else None
    if dec not in ("include", "exclude") or (dec == "exclude" and not code):
        dec, code = None, None
    return {"decision": dec, "code": code, "reason": str(d.get("reason") or "")[:300],
            "cost_usd": gen.cost_usd or 0}


def screen(name, limit, workers):
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    members = load_members(name)
    ids, dois = settled_ids()
    done = decided()
    todo = [m for m in members if (name, m["id"]) not in done
            and m["id"] not in ids and not (m.get("doi") and m["doi"] in dois)]
    if limit:
        todo = todo[:limit]
    print(f"{name}: {len(members)} members, {len(todo)} to screen", flush=True)

    def one(m):
        votes = {}
        for model in MODELS:
            try:
                votes[model] = ask(model, m, key)
            except Exception as e:  # noqa: BLE001 - a failed call is a missing vote, never a decision
                votes[model] = {"decision": None, "error": f"{type(e).__name__}: {e}"[:200], "cost_usd": 0}
        return {"universe": name, "id": m["id"], "basis": "abstract" if m.get("abstract") else "title",
                "votes": votes, "at": date.today().isoformat()}

    cost = 0.0
    with DECISIONS.open("a", encoding="utf-8") as fh, concurrent.futures.ThreadPoolExecutor(workers) as ex:
        for i, fut in enumerate(concurrent.futures.as_completed([ex.submit(one, m) for m in todo])):
            rec = fut.result()
            cost += sum(v.get("cost_usd") or 0 for v in rec["votes"].values())
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            if i % 250 == 0:
                print(i, f"${cost:.2f}", flush=True)
    print(f"screened {len(todo)}: ${cost:.2f}" + (f" (${cost / len(todo):.4f} each)" if todo else ""))


def verdict(rec):
    """'exclude' with a code when both models exclude; 'retry' when a vote is missing; else 'include'."""
    votes = list(rec["votes"].values())
    if any(v.get("decision") is None for v in votes):
        return "retry", None
    if all(v["decision"] == "exclude" for v in votes):
        # Both exclude but may name different rules; the first model's code is recorded, and the
        # manifest reason quotes both models' reasons, so the disagreement stays visible.
        return "exclude", votes[0]["code"]
    return "include", None


def record(name, apply):
    members = {m["id"]: m for m in load_members(name)}
    ids, dois = settled_ids()
    counts = collections.Counter()
    queue = []
    for (u, sid), rec in decided().items():
        if u != name or sid not in members:
            continue
        m = members[sid]
        if sid in ids or (m.get("doi") and m["doi"] in dois):
            counts["already in the manifest"] += 1
            continue
        v, code = verdict(rec)
        counts[v if v != "exclude" else f"exclude: {code}"] += 1
        if v == "exclude" and apply:
            reasons = "; ".join(f"{k.split('/')[0]}: {x['reason']}" for k, x in rec["votes"].items())
            okf_lib.append_manifest_entry(sid, m["title"], "rejected", doi=m.get("doi"), reason_code=code,
                                          reason=f"abstract screen of universe {name} ({rec['at']}), both "
                                                 f"models excluded on {rec['basis']}: {reasons}"[:900])
        elif v == "include":
            queue.append({k: m.get(k) for k in ("id", "title", "authors", "year", "url", "fetch_url", "pmcid")
                          if m.get(k) is not None}
                         | {"source": {"eric": "eric", "pmc": "pubmed", "arxiv": "arxiv"}[UNIVERSES[name]["source"]],
                            "topic_hint": f"screen:{name}"})
    for k, n in sorted(counts.items()):
        print(f"  {k:32} {n}")
    if apply:
        QUEUE_DIR.mkdir(parents=True, exist_ok=True)
        path = QUEUE_DIR / f"screen-{name}.ndjson"
        path.write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in queue), encoding="utf-8")
        print(f"wrote {len(queue)} passing source(s) to {path.relative_to(WIKI_ROOT)}")
    else:
        print("(dry run: --apply writes the rejections to the manifest and the passes to a queue)")


def summary():
    recs = decided()
    for name in UNIVERSES:
        path = SCREEN_DIR / f"{name}.ndjson"
        if not path.exists():
            print(f"{name}: not built")
            continue
        total = json.loads(path.read_text(encoding="utf-8").splitlines()[0])["members"]
        mine = [r for (u, _), r in recs.items() if u == name]
        c = collections.Counter(verdict(r)[0] for r in mine)
        cost = sum(v.get("cost_usd") or 0 for r in mine for v in r["votes"].values())
        print(f"{name}: {total} members, {len(mine)} screened ({dict(c)}), ${cost:.2f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--build", choices=UNIVERSES)
    g.add_argument("--screen", choices=UNIVERSES)
    g.add_argument("--record", choices=UNIVERSES)
    g.add_argument("--summary", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="with --screen: screen only this many (a pilot)")
    ap.add_argument("--workers", type=int, default=24)
    ap.add_argument("--apply", action="store_true", help="with --record: write the manifest and the queue")
    ap.add_argument("--snapshot", help="with --build of an arXiv universe: the Kaggle metadata snapshot")
    a = ap.parse_args()
    if a.build:
        build(a.build, a.snapshot)
    elif a.screen:
        screen(a.screen, a.limit, a.workers)
    elif a.record:
        record(a.record, a.apply)
    else:
        summary()


if __name__ == "__main__":
    main()
