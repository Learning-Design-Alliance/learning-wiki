#!/usr/bin/env python3
"""Tests for graph_search.py on a small synthetic wiki (no real pages read): the loader's edges, the basis
each row names, and each query with a planted case (a positive, a null, a moderator flip, a same-study
crossover, a pair of designs differing in one element). The cells are written and read through
evidence_cells.py, as the real store is.

    python3 scripts/test_graph_search.py
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import evidence_cells  # noqa: E402
import graph_search as GS  # noqa: E402


def claim(slug, title, sources, body=""):
    src = "".join(f"  - id: {s['id']}\n    resource: \"{s.get('res', 'https://example.org')}\"\n    author: A\n"
                  f"    q: {s['q']}\n    i: \"{s.get('i', '?')}\"\n    n: {s.get('n', '')}\n    kind: causal\n"
                  for s in sources)
    return f"---\ntype: claim\ntitle: \"{title}\"\nid: {slug}\nstatus: review\nsources:\n{src}---\n\n# {title}\n\n{body}\n"


def cell(claim_slug, var, direction, age="adult", expertise="?", outcome="delayed-retention", timing="delayed",
         design="randomized"):
    return {"key": f"{claim_slug}-{var}-{direction}-{expertise}-{timing}", "claim": claim_slug, "entry": "e",
            "cells": [{"L": {"age": age, "expertise": expertise},
                       "D": {"variable": var, "treatment": "t", "comparison": "c"},
                       "O": {"outcome": outcome, "timing": timing},
                       "result": {"direction": direction, "design": design}, "quote_ok": True}]}


class SyntheticWiki(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        w = Path(cls.tmp.name)
        for d in ("claims", "elements", "patterns", "designs"):
            (w / d).mkdir(parents=True)
        claims = {
            "spaced-wins": claim("spaced-wins", "Spaced practice beats massed practice in undergraduates",
                                 [{"id": "a-2020", "q": 4, "i": 2, "res": "https://doi.org/10.1000/aaa"}]),
            "spaced-null": claim("spaced-null", "Spacing did not improve retention among residents",
                                 [{"id": "b-2019", "q": 3, "res": "https://doi.org/10.1000/bbb"}]),
            "we-flip": claim("we-flip", "Worked examples help novices but not experts",
                             [{"id": "c-2018", "q": 3, "res": "https://doi.org/10.1000/ccc"}]),
            "lyle-practice": claim("lyle-practice", "Spaced quizzing reduces practice quiz performance",
                                   [{"id": "lyle-2022", "q": 3, "res": "https://doi.org/10.1000/lyle"}]),
            "lyle-retention": claim("lyle-retention", "Spaced quizzing increases end-of-semester retention",
                                    [{"id": "lyle-2022-2", "q": 3, "res": "https://doi.org/10.1000/lyle"}]),
            "weak-one": claim("weak-one", "Spacing helps in one case study", [{"id": "d-2010", "q": 1}]),
            "no-cell": claim("no-cell", "Interleaved practice improves college students' category learning",
                             [{"id": "e-2015", "q": 3, "n": "120 undergraduates"}]),
        }
        for slug, text in claims.items():
            (w / "claims" / f"{slug}.md").write_text(text)
        pages = [("element", "spacing-element"), ("element", "worked-ex"), ("element", "interleaving"),
                 ("pattern", "spaced-learning"), ("design", "d1"), ("design", "d2")]
        for kind, slug in pages:
            shard = w / "wiki-index" / kind / f"{slug[:2]}.ndjson"
            shard.parent.mkdir(parents=True, exist_ok=True)
            with shard.open("a") as f:
                f.write(json.dumps({"id": slug, "type": kind, "title": slug, "path": f"{kind}s/{slug}.md"}) + "\n")
        ri = {"kinds": {"claims": "claim", "designs": "design", "elements": "element", "patterns": "pattern"},
              "edges": {
                  "claims": {
                      "spaced-wins": {"elements": [{"slug": "spacing-element", "polarity": "+", "strength": "S"}],
                                      "patterns": [{"slug": "spaced-learning", "polarity": "+", "strength": "S"}]},
                      "spaced-null": {"elements": [{"slug": "spacing-element", "polarity": "-", "strength": "W"}]},
                      "we-flip": {"elements": [{"slug": "worked-ex", "polarity": "~", "strength": "M"}]},
                      "lyle-retention": {"elements": [{"slug": "spacing-element", "polarity": "+", "strength": "W"}]},
                      "no-cell": {"elements": [{"slug": "interleaving", "polarity": "+", "strength": "M"}]}},
                  "elements": {
                      "spacing-element": {"designs": [{"slug": "d1"}, {"slug": "d2"}]},
                      "worked-ex": {"designs": [{"slug": "d1"}, {"slug": "d2"}],
                                    "elements": [{"slug": "spacing-element"}]},
                      "interleaving": {"designs": [{"slug": "d2"}]}}}}
        (w / "reverse-index.json").write_text(json.dumps(ri))
        with GS.cell_store(w):
            for c in [cell("spaced-wins", "spacing", "+"), cell("spaced-null", "spacing", "ns"),
                      cell("we-flip", "worked-examples", "+", expertise="novice"),
                      cell("we-flip", "worked-examples", "-", expertise="advanced"),
                      cell("lyle-retention", "spacing", "+"),
                      cell("lyle-practice", "spacing", "-", outcome="practice-performance", timing="immediate"),
                      cell("weak-one", "spacing", "+")]:
                evidence_cells.append("cells", c)
        cls.store_after = evidence_cells.STORE
        cls.g = GS.load(w)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_store_restored(self):
        self.assertEqual(self.store_after, GS.WIKI_ROOT / "eval" / "runs" / "evidence-axes")

    def test_edges_typed(self):
        g = self.g
        self.assertEqual(g.nodes["claim/spaced-wins"]["max_q"], 4)
        self.assertEqual(g.nodes["claim/spaced-wins"]["title"], "Spaced practice beats massed practice in undergraduates")
        self.assertIn(("claim/spaced-wins", {"polarity": "+", "strength": "S"}),
                      g.edges("element/spacing-element", "cites"))
        self.assertEqual(len(g.edges("claim/spaced-wins", "tests")), 1)
        self.assertIn(("element/worked-ex", {}), g.edges("design/d1", "links"))
        # one study split over two claims and two entries is one source
        self.assertEqual(g.edges("claim/lyle-practice", "from")[0][0], g.edges("claim/lyle-retention", "from")[0][0])
        self.assertEqual(g.meta["cells"], 7)

    def test_evidence_filters_level_and_direction(self):
        rows = GS.q_evidence(self.g, ["spacing"], "+", min_q=3, age="adult")
        slugs = [r["claim"] for r in rows]
        self.assertEqual(slugs[0], "spaced-wins")             # q4, cited by its home pages, ranks first
        self.assertEqual(rows[0]["basis"], "cell")
        self.assertEqual(rows[0]["population_basis"], "cell")
        self.assertNotIn("weak-one", slugs)                   # q1 is below the floor
        self.assertNotIn("spaced-null", slugs)                # wrong direction

    def test_fallback_is_labelled(self):
        rows = GS.q_evidence(self.g, ["interleaving"], "+", min_q=3, age="adult")
        self.assertEqual([(r["claim"], r["basis"], r["population"], r["population_basis"]) for r in rows],
                         [("no-cell", "keyword+marker", "adult", "regex")])

    def test_nulls(self):
        rows = {r["claim"]: r["basis"] for r in GS.q_nulls(self.g, ["spacing"], 3)}
        self.assertEqual(rows.get("spaced-null"), "cell")
        self.assertNotIn("spaced-wins", rows)

    def test_nulls_need_an_experimental_design(self):
        g = GS.Graph()
        g.add_node("claim/x", type="claim", title="x", max_q=3, text_population="?")
        g.add_node("variable/spacing", type="variable")
        g.add_edge("claim/x", "tests", "variable/spacing", direction="ns", design="correlational", age="adult",
                   expertise="?", outcome="o", timing="delayed", quote_ok=True)
        self.assertEqual(GS.q_nulls(g, ["spacing"], 3), [])

    def test_boundary_flip(self):
        b = GS.q_boundaries(self.g, ["worked-examples"], 3)
        flips = {r["claim"]: r.get("flips") for r in b["within_claim"]}
        self.assertEqual(flips.get("we-flip"), {"novice": "+", "advanced": "-/ns"})
        self.assertEqual(b["pages_for_and_against"][0]["page"], "element/spacing-element")

    def test_crossover_same_study_and_within(self):
        cx = GS.q_crossovers(self.g, 3, variables=["spacing"])
        pairs = {(r["positive"], r["negative_or_null"], r["basis"]) for r in cx["same_study_pairs"]}
        self.assertIn(("lyle-retention", "lyle-practice", "cell/cell"), pairs)

    def test_paths(self):
        p = GS.q_paths(self.g, "elements/spacing-element")
        self.assertEqual(p["claims_cited"], 3)
        self.assertEqual(p["variables"]["spacing"], {"+": 2, "ns": 1})

    def test_one_diff(self):
        pairs = GS.q_one_diff(self.g)["pairs"]
        self.assertEqual([p["differs"] for p in pairs], [["element/interleaving"]])

    def test_keywords_name_real_variables(self):
        self.assertEqual(set(GS.VARIABLE_KEYWORDS) - set(GS.ed.values("variable")), set())


if __name__ == "__main__":
    unittest.main()
