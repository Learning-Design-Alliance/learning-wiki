#!/usr/bin/env python3
"""
link_learner_variables.py — link claims to the learner-variable pages they report on.

learning-design-spec joins a learner dimension to the research through its page in
learner-variables/ (spec/learners.md): a course whose learners vary on prior knowledge
reaches the claims about prior knowledge through that page. On 2026-10-10 only 7 of
the 12 pages had any inbound link and nothing linked to prior-knowledge, so the join
reached almost nothing (maintainer's retest, PR #210).

For each learner variable, candidate claims come from the search index (its title,
definition and a few synonyms below). A model then reads each candidate's title and
evidence line and says whether the claim reports a finding about that characteristic,
and in which role:

    predictor  learners who differ on it learn or achieve differently
    moderator  an instructional effect differs with it (works for novices, not experts)
    outcome    instruction changes it (an intervention raises self-efficacy)

and with what marker (+ the finding shows the characteristic matters as the claim
says, ~ under conditions, - it did not matter here), whose strength is capped at what
the claim's recorded evidence allows (link_pages.strength_cap). Each kept link is
written both ways: onto the variable's `## Claims` and onto the claim's
`## Learner Variables`, so the variable page has its evidence and the claim says which
learner characteristic it is about. Decisions go to eval/runs/learner-links/ first.

    python3 scripts/link_learner_variables.py                 # dry run, every variable
    python3 scripts/link_learner_variables.py --apply
    python3 scripts/link_learner_variables.py --new --apply   # only claims new in the tree (batches)
"""
import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WIKI_ROOT / "scripts"))
sys.path.insert(0, str(WIKI_ROOT))
import link_pages as lp  # noqa: E402
import search_index  # noqa: E402

FOLDER = WIKI_ROOT / "learner-variables"
OUT_DIR = WIKI_ROOT / "eval" / "runs" / "learner-links"
GROUP = 15
# Words a claim about the characteristic tends to use, beyond the page's own title and
# definition. Retrieval only: the model decides.
SYNONYMS = {
    "access": ["accessibility", "disability", "disabilities", "visual impairment", "hearing impairment",
               "deaf", "blind", "assistive technology", "internet access", "broadband", "device access"],
    "affect-regulation": ["anxiety", "math anxiety", "test anxiety", "frustration", "emotion regulation",
                          "emotional regulation", "stress", "coping"],
    "attention": ["attention", "distraction", "mind wandering", "ADHD", "attentional control", "sustained attention"],
    "belonging": ["belonging", "social belonging", "stereotype threat", "identity threat", "relatedness",
                  "connectedness", "sense of community"],
    "digital-literacy": ["digital literacy", "digital skills", "computer skills", "technology proficiency",
                         "ICT skills", "computer literacy"],
    "domain-context": ["authentic context", "workplace", "real-world relevance", "situated learning", "relevance"],
    "motivation": ["motivation", "interest", "self-efficacy", "expectancy", "intrinsic motivation",
                   "persistence", "engagement", "growth mindset"],
    "prior-knowledge": ["prior knowledge", "expertise", "novice", "novices", "expert learners", "background knowledge",
                        "prior achievement", "expertise reversal", "pretest scores", "domain knowledge"],
    "reading-and-language": ["reading comprehension", "reading ability", "English learners", "English language learners",
                             "second language", "bilingual", "multilingual", "reading fluency", "vocabulary knowledge"],
    "self-regulation": ["self-regulated learning", "self-regulation", "metacognition", "metacognitive",
                        "executive function", "self-monitoring", "goal setting", "strategy use"],
    "time-and-continuity": ["time on task", "attendance", "absenteeism", "summer learning", "learning loss",
                            "instructional time", "dosage", "interruption"],
    "socioeconomic-status": ["socioeconomic status", "SES", "low-income", "low income", "poverty", "economically disadvantaged",
                             "free or reduced-price lunch", "free school meals", "Pell", "first-generation", "first generation",
                             "family income", "parental education", "disadvantaged students"],
    "learning-disabilities": ["learning disability", "learning disabilities", "specific learning disability", "dyslexia",
                              "dyscalculia", "autism", "autistic", "intellectual disability", "special educational needs",
                              "special education", "IEP", "students with disabilities", "developmental disability"],
    "race-and-ethnicity": ["racial", "ethnic", "race/ethnicity", "Black students", "Hispanic", "Latino", "Latinx", "African American", "Native American", "Indigenous", "students of color", "racial gap", "minority students", "underrepresented minority"],
    "english-learner-status": ["English learner", "English learners", "English language learner", "English language learners", "ELL", "multilingual learner", "emergent bilingual", "dual language learner", "reclassification", "limited English proficiency", "second-language learner"],
    "gender": ["gender", "girls", "boys", "female students", "male students", "women in STEM", "gender gap", "gender differences", "sex differences"],
    "age-and-developmental-stage": ["older students", "younger students", "younger children", "older children", "adolescents", "age differences", "grade level", "early childhood", "adult learners", "nontraditional students", "developmental stage", "elementary versus secondary"],
    "self-efficacy": ["self-efficacy", "self efficacy", "efficacy beliefs", "confidence in ability", "academic confidence", "perceived competence"],
    "academic-anxiety": ["anxiety", "math anxiety", "mathematics anxiety", "test anxiety", "exam anxiety", "foreign language anxiety", "language anxiety", "statistics anxiety", "evaluation anxiety"],
    "interest": ["interest", "situational interest", "individual interest", "curiosity", "utility value", "relevance intervention", "enjoyment", "liking for the subject"],
    "epistemic-beliefs": ["epistemic beliefs", "epistemological beliefs", "epistemic cognition", "beliefs about knowledge", "nature of science", "personal epistemology"],
    "mindset": ["mindset", "growth mindset", "fixed mindset", "implicit theories of intelligence", "implicit theories", "beliefs about intelligence", "malleability of intelligence"],
    "learning-style-preferences": ["learning styles", "learning style", "VARK", "visual learners", "auditory learners", "kinesthetic learners", "meshing hypothesis", "preferred modality"],
    "general-cognitive-ability": ["cognitive ability", "general intelligence", "intelligence", "IQ", "fluid intelligence", "reasoning ability", "aptitude", "gifted", "high-ability", "aptitude-treatment interaction"],
    "executive-function": ["executive function", "executive functions", "executive functioning", "inhibitory control", "cognitive flexibility", "task switching", "effortful control"],
    "spatial-ability": ["spatial ability", "spatial skills", "spatial reasoning", "mental rotation", "visuospatial", "spatial visualization", "spatial thinking"],
    "number-sense": ["number sense", "numerical magnitude", "magnitude comparison", "number line estimation", "approximate number system", "numeracy", "early numeracy", "symbolic number"],
    "academic-self-concept": ["self-concept", "academic self-concept", "math self-concept", "ability self-concept", "big-fish-little-pond", "self-perceived ability"],
    "achievement-goal-orientation": ["mastery goals", "performance goals", "achievement goals", "goal orientation", "performance-avoidance", "performance-approach", "mastery orientation"],
    "achievement-emotions": ["achievement emotions", "academic emotions", "enjoyment", "boredom", "frustration", "pride", "shame", "control-value theory", "epistemic emotions", "confusion"],
    "personality-traits": ["personality", "Big Five", "conscientiousness", "openness", "agreeableness", "extraversion", "neuroticism", "grit"],
    "need-for-cognition": ["need for cognition", "cognitive engagement disposition", "enjoyment of thinking", "typical intellectual engagement"],
    "creativity": ["creativity", "creative thinking", "divergent thinking", "creative potential", "originality"],
    "emotional-intelligence": ["emotional intelligence", "emotional competence", "trait emotional intelligence", "emotion recognition", "social-emotional skills"],
    "academic-and-critical-literacy": ["academic literacy", "disciplinary literacy", "critical literacy", "content-area literacy", "health literacy", "financial literacy", "academic language", "reading across the disciplines", "media literacy", "core academic skills"],
    "adverse-experiences": ["adverse childhood experiences", "ACEs", "childhood trauma", "maltreatment", "abuse and neglect", "exposure to violence", "toxic stress", "trauma-informed", "early adversity", "chronic stress"],
    "algebraic-thinking": ["algebraic thinking", "algebraic reasoning", "early algebra", "equation solving", "generalisation in mathematics", "functional thinking", "symbolic reasoning", "pre-algebra", "algebra readiness"],
    "alphabet-knowledge-and-print-awareness": ["alphabet knowledge", "letter knowledge", "letter-name knowledge", "letter-sound knowledge", "print awareness", "concepts about print", "print knowledge", "emergent literacy"],
    "arithmetic-fact-retrieval": ["arithmetic fact retrieval", "math fact fluency", "number fact recall", "basic fact fluency", "retrieval of arithmetic facts", "multiplication facts", "addition facts", "fact retrieval strategy", "computational fluency"],
    "auditory-processing": ["auditory processing", "auditory processing disorder", "speech perception", "speech in noise", "listening comprehension", "auditory discrimination", "auditory attention", "central auditory processing"],
    "civic-mindedness": ["civic mindedness", "civic engagement", "civic identity", "critical consciousness", "prosocial behaviour", "civic participation", "citizenship dispositions", "community engagement", "civic knowledge"],
    "collaboration": ["collaboration", "collaborative learning", "cooperative learning skills", "teamwork", "group work", "peer collaboration", "collaborative problem solving", "working with others"],
    "communication-skills": ["communication skills", "oral communication", "oral language skills", "mathematical communication", "math discussion", "explaining reasoning", "public speaking", "expressive language", "multimodal communication", "classroom discourse"],
    "critical-thinking": ["critical thinking", "critical-thinking skills", "critical thinking disposition", "evaluating evidence", "argument evaluation", "reasoned judgement", "higher-order thinking", "source evaluation"],
    "decoding": ["decoding", "word decoding", "phonics skills", "word recognition", "sight word reading", "orthographic processing", "word reading", "foundational reading skills", "pseudoword reading"],
    "geometric-reasoning": ["geometric reasoning", "geometry understanding", "geometric thinking", "reasoning about shapes", "geometric proof", "van Hiele levels", "shape properties", "spatial geometry"],
    "home-learning-environment": ["home learning environment", "home literacy environment", "print exposure", "shared book reading", "parental involvement", "family engagement", "home numeracy environment", "books in the home", "parent math anxiety", "literacy environment"],
    "identity": ["identity development", "ethnic identity", "racial identity", "ethnic-racial identity", "social identity", "cultural identity", "sense of self", "identity salience", "Deaf identity"],
    "inferencing": ["inferencing", "inference making", "inferential comprehension", "making inferences", "bridging inferences", "reading between the lines", "inference generation", "text-level inference"],
    "long-term-memory": ["long-term memory", "retention", "memory consolidation", "declarative memory", "delayed recall", "episodic memory", "semantic memory", "long-term retention", "memory retrieval"],
    "mathematical-flexibility": ["mathematical flexibility", "strategy flexibility", "procedural flexibility", "adaptive expertise in mathematics", "multiple strategies", "representational flexibility", "strategic flexibility", "flexible problem solving"],
    "measurement": ["measurement skills", "measurement concepts", "understanding of units", "length area and volume", "spatial measurement", "area and perimeter", "unit iteration", "measurement reasoning"],
    "metacognition": ["metacognition", "metacognitive awareness", "metacognitive knowledge", "metacognitive regulation", "comprehension monitoring", "thinking about thinking", "judgements of learning", "calibration of confidence", "metacognitive strategies", "self-monitoring"],
    "morphological-awareness": ["morphological awareness", "morphological knowledge", "morphology", "morpheme knowledge", "word parts", "prefixes and suffixes", "derivational morphology", "morphological processing"],
    "operations-and-place-value": ["arithmetic operations", "computation", "calculation skills", "place value", "base-ten understanding", "multi-digit arithmetic", "computational estimation", "procedural arithmetic", "conceptual understanding of operations"],
    "oral-language": ["oral language", "spoken language", "language skills", "narrative skills", "storytelling ability", "listening comprehension", "expressive language", "receptive language", "oral narrative"],
    "phonological-awareness": ["phonological awareness", "phonemic awareness", "phonological processing", "phoneme segmentation", "phoneme blending", "rhyme awareness", "sound awareness", "phonological skills"],
    "physical-wellbeing": ["physical activity", "physical fitness", "exercise", "nutrition", "health", "aerobic fitness", "physical education", "obesity", "hunger", "health literacy"],
    "problem-solving": ["problem solving", "problem-solving skills", "everyday problem solving", "creative problem solving", "decision making", "ill-structured problems", "solving novel problems"],
    "processing-speed": ["processing speed", "speed of processing", "speed of information processing", "rapid automatized naming", "RAN", "reaction time", "perceptual speed", "cognitive speed", "slow processing"],
    "proportional-reasoning": ["proportional reasoning", "ratio reasoning", "fraction understanding", "rational number knowledge", "fractions and decimals", "ratios and rates", "percentages", "multiplicative reasoning", "fraction magnitude"],
    "reading-fluency": ["reading fluency", "oral reading fluency", "reading rate", "reading speed", "reading accuracy", "fluent reading", "word reading efficiency", "reading automaticity"],
    "safety": ["school safety", "feeling safe", "bullying", "cyberbullying", "peer victimization", "neighborhood safety", "community violence", "school climate", "risk-taking behavior", "psychological safety"],
    "sensory-integration": ["sensory integration", "sensory processing", "sensory processing disorder", "sensory sensitivity", "sensory over-responsivity", "sensory modulation", "tactile sensitivity", "sensory-motor"],
    "sleep": ["sleep", "sleep duration", "sleep quality", "sleep deprivation", "daytime sleepiness", "sleep disturbance", "insufficient sleep", "bedtime", "sleep hygiene", "school start times"],
    "social-awareness-and-relationship-skills": ["social awareness", "relationship skills", "social competence", "social skills", "peer relationships", "empathy", "perspective taking", "social-emotional learning", "prosocial behaviour", "interpersonal skills"],
    "social-supports": ["social support", "perceived social support", "family support", "teacher support", "peer support", "support network", "parental support", "social isolation", "supportive relationships"],
    "statistical-reasoning": ["statistical reasoning", "statistical literacy", "data literacy", "reasoning about data", "probability reasoning", "understanding variation", "graph interpretation", "data analysis skills"],
    "stereotype-threat": ["stereotype threat", "stereotype vulnerability", "fear of confirming a stereotype", "identity threat", "diagnostic test framing", "stereotype awareness", "social identity threat", "math stereotype", "gender stereotype in math"],
    "syntax": ["syntax", "syntactic knowledge", "syntactic awareness", "grammar", "grammatical skills", "sentence structure", "syntactic complexity", "morphosyntax", "sentence comprehension"],
    "visual-processing": ["visual processing", "visual perception", "visual-motor integration", "visual discrimination", "visuospatial processing", "visual attention", "visual processing disorder", "figure copying"],
    "vocabulary": ["vocabulary", "vocabulary knowledge", "receptive vocabulary", "expressive vocabulary", "academic vocabulary", "word knowledge", "lexical knowledge", "vocabulary breadth", "vocabulary depth"],
    "writing-skills": ["writing skills", "written composition", "writing quality", "handwriting", "spelling and transcription", "genre knowledge", "argumentative writing", "writing fluency", "written expression", "persuasive writing"],
    "working-memory": ["working memory", "cognitive load", "memory capacity", "element interactivity",
                       "short-term memory", "cognitive overload"],
}
ROLE_TEXT = {"predictor": "learners who differ on it differ in outcomes",
             "moderator": "an instructional effect differs with it",
             "outcome": "instruction changes it"}
# Group categories are not causes. A gap between racial groups, genders or income groups records the
# circumstances and treatment that go with membership (school funding, teacher assignment, tracking,
# discrimination, stereotypes, poverty), not something about the learners; the default wording read
# as if the category itself drove outcomes (maintainer, 2026-10-16). Learning-style claims are
# worded so a single study is not read as support for matching instruction to style.
ROLE_TEXT_BY_VARIABLE = {
    **{v: {"predictor": "outcomes differ by group: a gap reflecting circumstances and treatment, not a cause",
           "moderator": "an instructional effect differs by group",
           "outcome": "instruction changes the gap"}
       for v in ("race-and-ethnicity", "gender", "socioeconomic-status")},
    "learning-style-preferences": {
        "predictor": "learners reporting different styles differed here; not a test of matching instruction to style",
        "moderator": "an effect differed by reported style in this study; matching to style is not supported overall",
        "outcome": "instruction changes reported style"},
}


def role_text(variable: str, role: str) -> str:
    return ROLE_TEXT_BY_VARIABLE.get(variable, ROLE_TEXT)[role]

PROMPT = """A learning-design wiki has one page per learner characteristic. Designers reach the research
on a characteristic through that page, so it should link every claim that reports a finding about it.

LEARNER CHARACTERISTIC: {title}
Definition: {description}

CLAIMS (title, then the evidence the wiki records for it):
{claims}

For each claim, decide whether it reports a finding ABOUT this characteristic: learners who differ on it
learn or achieve differently ("predictor"); an instructional effect differs with it ("moderator"); or
instruction changes it ("outcome"). A claim that only mentions the word, or is about a different
characteristic, does not bear. Also not bearing: a check that two study groups started out equal (baseline
equivalence), a claim about a research or measurement method, a claim about a programme's overall effect
on an outcome that is not this characteristic, and a characteristic that belongs to another page (digital
skills are digital literacy, not access). Give a marker: "+" the finding shows the characteristic matters in the way the
claim states, "~" it matters only under conditions or the results are mixed, "-" it did not matter here (a
null result is "-", never "+"); then S, M or W from the evidence line.
Reply: {{"links": [{{"k": <claim number>, "bears": true, "role": "predictor|moderator|outcome",
 "marker": "+M"}}]}}  (list only claims that bear)"""


def variables() -> dict:
    out = {}
    for p in sorted(FOLDER.glob("*.md")):
        if p.stem == "index":
            continue
        rec = lp.record(f"learner-variables/{p.stem}", p)
        out[p.stem] = rec
    return out


def new_claims() -> set:
    r = subprocess.run(["git", "status", "--porcelain", "--", "claims"], cwd=WIKI_ROOT,
                       capture_output=True, text=True)
    return {Path(line[3:]).stem for line in r.stdout.splitlines() if line.startswith("??") or line[1] == "A"}


def linked_claims(path: Path) -> set:
    return set(re.findall(r"\]\(\.\./claims/([^)#]+)\.md", path.read_text(encoding="utf-8")))


def candidates(db, slug: str, rec: dict, limit: int, only: "set | None") -> list:
    """Claims matching the variable's title or any of its phrases (every word of a phrase
    in the claim), best first per phrase, merged; phrases keep "working memory" from
    being read as "working" or "memory"."""
    phrases = [rec["title"]] + SYNONYMS.get(slug, [])
    per = max(15, limit // len(phrases))
    seen, rows = set(), []
    for ph in phrases:
        for r in search_index.query(db, ph, folder="claims", limit=per, mode="AND"):
            if r[2] not in seen:
                seen.add(r[2])
                rows.append(r)
    have = linked_claims(FOLDER / f"{slug}.md")
    out = []
    for r in rows[:limit]:
        claim = r[2]
        if claim in have or (only is not None and claim not in only):
            continue
        path = WIKI_ROOT / "claims" / f"{claim}.md"
        if path.exists():
            out.append(lp.record(f"claims/{claim}", path))
    return out


def judge(slug: str, rec: dict, group: list, model: str, key: str) -> list:
    from scripts.eval import openrouter_client as oc
    from scripts.eval.jsonutil import extract_json
    listing = "\n".join(f"{i + 1}. {c['title']} [evidence: {c['evidence'] or 'none recorded'}]"
                        for i, c in enumerate(group))
    prompt = PROMPT.format(title=rec["title"], description=rec["description"], claims=listing)
    try:
        # A reasoning model spends most of its budget before the JSON: 2,500 ran out.
        gen = oc.generate(model, "You classify research claims for a learning-design wiki. Reply with JSON only.",
                          prompt, key, max_tokens=12000)
    except Exception as e:     # one failed call is recorded, not the end of the run
        return [{"variable": slug, "error": str(e)[:200], "cost_usd": 0}]
    try:
        d = extract_json(gen.raw_text)
    except Exception:
        return [{"variable": slug, "error": (gen.raw_text or "")[:200], "cost_usd": gen.cost_usd}]
    out = []
    for item in (d or {}).get("links") or []:
        k = item.get("k")
        if not (isinstance(k, int) and 1 <= k <= len(group)) or not item.get("bears"):
            continue
        marker, role = item.get("marker"), item.get("role")
        if not (isinstance(marker, str) and lp.MARKER_RE.match(marker)) or role not in ROLE_TEXT:
            continue
        claim = group[k - 1]
        cap = lp.strength_cap(claim["evidence"])
        if "WMS".index(marker[1]) > "WMS".index(cap):
            marker = marker[0] + cap
        out.append({"variable": slug, "claim": claim["key"].split("/", 1)[1], "title": claim["title"],
                    "role": role, "marker": marker})
    if out:
        out[0]["cost_usd"] = gen.cost_usd
    else:
        out.append({"variable": slug, "none": True, "cost_usd": gen.cost_usd})
    return out


def add_lines(text: str, heading: str, lines: list, before: tuple) -> str:
    """Append lines (skipping links already present) under `heading`, creating the
    section before the first of `before` that exists, else at the end."""
    lines = [l for l in lines if re.search(r"\]\(([^)]+)\)", l).group(1) not in text]
    if not lines:
        return text
    m = re.search(rf"^{re.escape(heading)}[ \t]*\n", text, re.M)
    if m:
        nxt = re.search(r"^#{1,3} ", text[m.end():], re.M)
        cut = m.end() + (nxt.start() if nxt else len(text) - m.end())
        block = text[m.end():cut].rstrip("\n")
        block = "\n".join(l for l in block.split("\n") if l.strip() != "-")
        rest = text[cut:]
        return text[:m.end()] + (block + "\n" if block.strip() else "") + "\n".join(lines) + \
            ("\n\n" + rest if rest else "\n")
    for b in before:
        mb = re.search(rf"^{re.escape(b)}[ \t]*$", text, re.M)
        if mb:
            return text[:mb.start()] + f"{heading}\n" + "\n".join(lines) + "\n\n" + text[mb.start():]
    return text.rstrip("\n") + f"\n\n{heading}\n" + "\n".join(lines) + "\n"


def apply(links: list, vars_: dict) -> dict:
    by_var, by_claim = {}, {}
    for l in links:
        by_var.setdefault(l["variable"], []).append(l)
        by_claim.setdefault(l["claim"], []).append(l)
    for slug, ls in by_var.items():
        path = FOLDER / f"{slug}.md"
        lines = [f"- [{l['title']}](../claims/{l['claim']}.md) [{l['marker']}] — {role_text(l['variable'], l['role'])}"
                 for l in sorted(ls, key=lambda x: x["title"].lower())]
        text = path.read_text(encoding="utf-8")
        path.write_text(add_lines(text, "## Claims", lines, ("## Related Learner Variables", "## Examples",
                                                               "## Key Sources")), encoding="utf-8")
    for claim, ls in by_claim.items():
        path = WIKI_ROOT / "claims" / f"{claim}.md"
        lines = [f"- [{vars_[l['variable']]['title']}](../learner-variables/{l['variable']}.md) — "
                 f"{l['role']}: {role_text(l['variable'], l['role'])}" for l in ls]
        text = path.read_text(encoding="utf-8")
        path.write_text(add_lines(text, "## Learner Variables", lines, ("## Related Claims",)), encoding="utf-8")
    return {"variable_pages": len(by_var), "claim_pages": len(by_claim), "links": len(links)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--new", action="store_true", help="only claims added in the working tree")
    ap.add_argument("--variables", nargs="+", help="these learner-variable slugs only")
    ap.add_argument("--limit", type=int, default=150, help="candidate claims per variable")
    ap.add_argument("--model", default="openai/gpt-5.6-luna")
    ap.add_argument("--concurrency", type=int, default=12)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("OPENROUTER_API_KEY is not set")
    vars_ = variables()
    only = new_claims() if args.new else None
    if only is not None and not only:
        print("no new claims")
        return
    db = search_index.ensure()
    jobs = []
    for slug, rec in vars_.items():
        if args.variables and slug not in args.variables:
            continue
        cands = candidates(db, slug, rec, args.limit if only is None else 400, only)
        jobs += [(slug, rec, cands[i:i + GROUP]) for i in range(0, len(cands), GROUP)]
    print(f"{len(jobs)} group(s) of up to {GROUP} candidate claims across {len(vars_)} learner variables")
    results = []
    with concurrent.futures.ThreadPoolExecutor(args.concurrency) as ex:
        for r in ex.map(lambda j: judge(j[0], j[1], j[2], args.model, key), jobs):
            results += r
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = Path(args.out) if args.out else OUT_DIR / ("new.ndjson" if args.new else "all.ndjson")
    out.write_text("".join(json.dumps(r) + "\n" for r in results), encoding="utf-8")
    links = [r for r in results if r.get("claim")]
    cost = sum(r.get("cost_usd") or 0 for r in results)
    errors = sum(1 for r in results if r.get("error"))
    counts = {}
    for l in links:
        counts[l["variable"]] = counts.get(l["variable"], 0) + 1
    print(f"links: {len(links)} {dict(sorted(counts.items()))}; errors {errors}; cost ${cost:.3f}; -> {out}")
    if args.apply:
        print("applied:", apply(links, vars_))


if __name__ == "__main__":
    main()
