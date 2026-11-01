#!/usr/bin/env python3
"""
stat_checks.py — read a source's text for statistics that cannot be right, and for
references that cannot exist. A library; check_source_validity.py runs it.

Prompted by an audit of AI-in-education meta-analyses (O'Neill, preprint, 2026), which
found that a primary study several of them pooled, and this wiki had made ten claims
from, reports a partial eta squared of 1.374 and cites five "ChatGPT-supported"
studies dated 2017-2020 (Alneyadi & Wardat 2024; checked against the paper itself
2026-10-25). Nothing here was reading a source for that: the load-bearing judge asks
whether a claim matches its source, not whether the source can be believed.

Every check here is mechanical and errs toward silence. A finding names the text it
fired on, so a person can read it in seconds; it never removes or edits anything.

* impossible   a proportion of variance (eta squared, partial eta squared, omega
               squared, R squared) above 1, a correlation or Cronbach's alpha above 1,
               a p value above 1.
* anova-row    in an ANOVA table whose header names SS, df and MS, a row whose mean
               square is not its sum of squares over its degrees of freedom (5%
               tolerance), or whose eta squared column is above 1.
* p-decision   a t, F, chi-square or r test whose reported p and the p its own
               statistic and degrees of freedom give fall on opposite sides of .05
               (statcheck's "gross inconsistency"). A typo in one test is common; the
               finding is for a person, and several in one paper are a pattern.
* anachronism  a reference naming ChatGPT, GPT-3.5, GPT-4, Bard or LLaMA dated before
               the tool existed.

Extracted PDF text is messy (eta squared arrives as "η2", "η 2", "ηp2", "η²"), so
the patterns are deliberately narrow: a statistic must sit next to its symbol.
"""
import math
import re

# ---------------------------------------------------------------- distributions

def _betacf(a, b, x):
    """Continued fraction for the incomplete beta function (Numerical Recipes)."""
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = 1.0 + aa / c if abs(c) > 1e-300 else 1e300
        de = d * c
        h *= de
        if abs(de - 1.0) < 3e-12:
            break
    return h


def betainc(a, b, x):
    """Regularised incomplete beta I_x(a, b)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbt = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x)
    if x < (a + 1) / (a + b + 2):
        return math.exp(lbt) * _betacf(a, b, x) / a
    return 1.0 - math.exp(lbt) * _betacf(b, a, 1 - x) / b


def _gammainc_upper(s, x):
    """Regularised upper incomplete gamma Q(s, x)."""
    if x <= 0:
        return 1.0
    if x < s + 1:
        term = total = 1.0 / s
        n = s
        for _ in range(500):
            n += 1
            term *= x / n
            total += term
            if abs(term) < abs(total) * 1e-14:
                break
        return 1.0 - total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    b = x + 1 - s
    c, d = 1e300, 1.0 / b
    h = d
    for i in range(1, 500):
        an = -i * (i - s)
        b += 2
        d = an * d + b
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        c = b + an / c
        c = c if abs(c) > 1e-300 else 1e-300
        de = d * c
        h *= de
        if abs(de - 1) < 1e-14:
            break
    return math.exp(-x + s * math.log(x) - math.lgamma(s)) * h


def p_value(test, value, df1, df2=None):
    """Two-sided p for t and r, upper-tail p for F and chi-square."""
    try:
        if test == "t":
            return betainc(df1 / 2, 0.5, df1 / (df1 + value * value))
        if test == "r":
            if abs(value) >= 1:
                return None
            t = value * math.sqrt(df1 / (1 - value * value))
            return betainc(df1 / 2, 0.5, df1 / (df1 + t * t))
        if test == "F":
            return betainc(df2 / 2, df1 / 2, df2 / (df2 + df1 * value))
        if test == "chi2":
            return _gammainc_upper(df1 / 2, value / 2)
    except (ValueError, ZeroDivisionError, OverflowError):
        return None
    return None


# ---------------------------------------------------------------- helpers

NUM = r"(-?\d*\.?\d+)"
_ETA = r"(?:partial\s+)?(?:η|eta)\s*(?:p|\[?p\]?)?\s*(?:2|²|\^2|squared)(?:\s*p)?"
_VAR = rf"(?:{_ETA}|ω\s*(?:2|²)|omega\s+squared|\bR\s*(?:2|²)(?![\d.])|R-squared)"


def _ctx(text, m, width=90):
    s = text[max(0, m.start() - width):m.end() + width]
    return " ".join(s.split())


def _num(s):
    s = s.strip().replace("−", "-")
    if re.fullmatch(r"-?0\d+\.\d+", s):          # "00.401" from a PDF table
        s = s.lstrip("0") or "0"
    try:
        return float(s)
    except ValueError:
        return None


def body_and_refs(text):
    """Split at the last References heading; (body, references)."""
    m = None
    for m in re.finditer(r"(?im)^\s*(?:references|reference list|bibliography|works cited|literature cited)\s*:?\s*$", text):
        pass
    if m and m.start() > len(text) * 0.3:
        return text[:m.start()], text[m.end():]
    return text, ""


# ---------------------------------------------------------------- checks

def impossible_values(text):
    out = []
    dec = r"(-?\d*\.\d+)"          # a printed decimal: "R2 = 21%" and "p=2.9 10-12" are not
    tail = r"(?![\d.]|\s*%|\s*(?:×|x|\*|·)?\s*10\s*[-−–^]|\s*[eE][-−]|\s*[-−–]\s*\d|\s*[×*/])"
    pats = [
        ("variance-explained > 1", rf"{_VAR}\s*[=:]\s*{dec}{tail}"),
        ("correlation > 1", rf"(?<![A-Za-z])r\s*\(\s*\d+\s*\)\s*=\s*{dec}{tail}"),
        ("Cronbach's alpha > 1", rf"(?:Cronbach'?s?\s+(?:alpha|α)|\bα\s*\(Cronbach)\s*(?:of|was|=|:)?\s*{dec}{tail}"),
        ("p > 1", rf"(?<![\w?&=/\u0370-\u03ff])p\s*=\s*{dec}{tail}"),
    ]
    for label, pat in pats:
        for m in re.finditer(pat, text, re.I if label != "p > 1" else 0):
            v = _num(m.group(m.lastindex))
            if label.startswith("variance") and re.search(r"\bR\s*1\s*=|ROUGE|BLEU|RL\s*sum", text[max(0, m.start() - 60):m.end() + 40], re.I):
                continue                      # ROUGE-2, not R squared
            if v is not None and abs(v) > 1.0001:
                out.append({"check": "impossible", "what": label, "value": v, "text": _ctx(text, m)})
    return out


def anova_rows(text):
    """Rows under a header naming SS, df and MS, read as SS df MS F ...; the last
    number is read as eta squared only when the header names it last."""
    out = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        h = line
        if not (re.search(r"\bSS\b|sum of squares", h, re.I) and re.search(r"\bdf\b", h)
                and re.search(r"\bMS\b|mean square", h, re.I)):
            continue
        order = [k for k, _ in sorted(
            [(k, m.start()) for k, p in (("SS", r"\bSS\b|sum of squares"), ("df", r"\bdf\b"),
                                          ("MS", r"\bMS\b|mean square"))
             for m in [re.search(p, h, re.I)] if m], key=lambda kv: kv[1])]
        if order != ["SS", "df", "MS"]:
            continue
        eta_last = bool(re.search(rf"{_ETA}\s*(?:effect\s*size)?\s*$", h.strip(), re.I)) or \
            bool(re.search(_ETA, h, re.I) and re.search(r"effect\s*size\s*$", h.strip(), re.I))
        for row in lines[i + 1:i + 25]:
            if not re.match(r"\s*[A-Za-z][A-Za-z ()×*'\-]{1,40}\s+\d", row) or \
                    re.search(r"\bpage\b|\bvol(?:ume)?\b|\bjournal\b|\(\d{4}\)|\d+\s*/\s*\d+\s+[A-Z]", row, re.I):
                continue
            nums = re.findall(r"(?<![\w.])(\d+\.\d+|\d+|\.\d+)(?![\w.])", row)   # ".398": APA drops the leading zero
            if len(nums) < 4:
                continue
            ss, df, ms = _num(nums[0]), _num(nums[1]), _num(nums[2])
            if not (ss and df and ms) or df != int(df) or not 0 < df < 1000 or "." in nums[1] \
                    or "." not in nums[0] + nums[2]:
                continue
            if abs(ss / df - ms) / ms > 0.05:
                out.append({"check": "anova-row", "what": f"MS {ms} is not SS {ss} / df {int(df)} ({ss / df:.2f})",
                            "text": " ".join((h + " | " + row).split())[:300]})
            if eta_last:
                eta = _num(nums[-1])
                if eta is not None and eta > 1.0001 and "." in nums[-1]:
                    out.append({"check": "anova-row", "what": f"eta squared {eta} > 1",
                                "text": " ".join((h + " | " + row).split())[:300]})
    return out


_P = r"p\s*([<>=≤≥])\s*(\.\d+|0\.\d+|1\.0+)"
_TESTS = [
    ("t", rf"(?<![A-Za-z])t\s*\(\s*(\d+(?:\.\d+)?)\s*\)\s*=\s*(-?\d+\.?\d*)\s*,\s*{_P}"),
    ("F", rf"(?<![A-Za-z])F\s*\(\s*(\d+)\s*,\s*(\d+(?:\.\d+)?)\s*\)\s*=\s*(\d+\.?\d*)\s*,\s*{_P}"),
    ("chi2", rf"(?:χ|chi)\s*(?:2|²|-square[d]?)\s*\(\s*(\d+)(?:\s*,\s*N\s*=\s*\d+)?\s*\)\s*=\s*(\d+\.?\d*)\s*,\s*{_P}"),
    ("r", rf"(?<![A-Za-z])r\s*\(\s*(\d+)\s*\)\s*=\s*(-?\.\d+|-?0\.\d+)\s*,\s*{_P}"),
]


def p_decisions(text, alpha=0.05):
    out = []
    for test, pat in _TESTS:
        for m in re.finditer(pat, text, re.I if test == "chi2" else 0):
            g = m.groups()
            if test == "F":
                df1, df2, val, op, rp = float(g[0]), float(g[1]), float(g[2]), g[3], float(g[4])
            else:
                df1, val, op, rp, df2 = float(g[0]), float(g[1]), g[2], float(g[3]), None
            if df1 <= 0 or (df2 is not None and df2 <= 0):
                continue
            if re.search(r"(?:one|1)[- ]?(?:tailed|sided)|directional", text[max(0, m.start() - 150):m.end() + 80], re.I):
                continue
            p = p_value(test, abs(val), df1, df2)
            if p is None:
                continue
            sig_reported = (op in "<≤" and rp <= alpha) or (op == "=" and rp < alpha)
            if op in ">≥":
                sig_reported = False
            sig_computed = p < alpha
            if op == "=" and abs(p / 2 - rp) <= 0.0015 + 10 ** -len(g[-1].split(".")[-1]):
                continue                      # a one-tailed p, not labelled as one
            if test == "F" and df1 > df2:
                q = p_value(test, abs(val), df2, df1)
                if q is not None and (q < alpha) == sig_reported:
                    continue                  # degrees of freedom printed in reverse
            if op in ">≥" and rp <= 0.001 and p < 0.001:
                continue                      # "p > .001" printed for "p < .001"
            # the edge: p reported "= .05" or "< .05" for a computed .050-.051 is rounding
            if sig_reported != sig_computed and not (abs(p - alpha) < 0.002):
                out.append({"check": "p-decision", "what": f"{test} gives p = {p:.4f}, reported p {op} {g[-1]}",
                            "text": _ctx(text, m, 40)})
    return out


RELEASES = [("ChatGPT", r"chat\s*-?\s*gpt", 2022), ("GPT-3.5", r"gpt\s*-?\s*3\.5", 2022),
            ("GPT-4", r"gpt\s*-?\s*4", 2023), ("Bard", r"google\s+bard|\bbard\b(?=.{0,40}(?:ai|chatbot|google))", 2023),
            ("LLaMA", r"\bllama\s*(?:2|3)?\b(?=.{0,60}(?:large language|\bLLM|foundation model|meta ai))", 2023)]
# A preprint can name a tool the year before its public release (GPT-4 was described
# in 2022 coverage); a reference two or more years early cannot.
MARGIN = 1
_YEAR = r"(?<!\d)(19[5-9]\d|20[0-3]\d)(?!\d)"


def _strip_links(s):
    return re.sub(r"(?:https?://|doi:\s*|www\.)\S+", " ", s)


def anachronisms(refs):
    """A tool named in a reference dated before the tool existed. The date has to be
    that reference's own: in numbered (IEEE) lists, the year inside the same [n]
    entry; in author-year lists, the last "(YYYY" before the mention, with no later
    year at or after the tool's release between them (two entries run together in
    extracted text is the usual false alarm)."""
    out = []
    if not refs:
        return out
    refs = _strip_links(refs)
    lines = [" ".join(l.split()).lower() for l in refs.split("\n")]
    repeated = {l for l in lines if len(l) > 15 and lines.count(l) >= 2}    # running heads
    numbered = len(re.findall(r"\[\d+\]", refs)) >= 5
    for name, pat, rel in RELEASES:
        for m in re.finditer(pat, refs, re.I):
            ls, le = refs.rfind("\n", 0, m.start()) + 1, refs.find("\n", m.end())
            line = " ".join(refs[ls:le if le > 0 else None].split()).lower()
            if (m.group(0).isupper() and len(m.group(0)) > 4) or line in repeated \
                    or re.search(r"\d+\s*/\s*\d+\s*$|\bpage\s+\d+", line):
                continue                      # a running head or footer
            if numbered:
                a = refs.rfind("[", 0, m.start())
                if a < 0 or m.start() - a > 350 or not re.match(r"\[\d+\]", refs[a:]):
                    continue
                nxt = re.search(r"\[\d+\]", refs[m.end():])
                entry = refs[a:m.end() + (nxt.start() if nxt else 300)][:500]
                years = [int(y) for y in re.findall(_YEAR, entry)]
                if not years or max(years) > rel - 1 - MARGIN:
                    continue
                year = max(years)
            else:
                before = refs[max(0, m.start() - 300):m.start()]
                ys = list(re.finditer(r"\((19[5-9]\d|20[0-3]\d)[a-z]?(?:,[^)]*)?\)\.?", before))
                if not ys:
                    continue
                year = int(ys[-1].group(1))
                between = before[ys[-1].end():]
                # the mention must be in this entry's title: no sentence end between
                if year > rel - 1 - MARGIN or re.search(r"[.?!]\s", between) \
                        or any(int(y) >= rel for y in re.findall(_YEAR, between)):
                    continue
                entry = before[max(0, ys[-1].start() - 120):] + refs[m.start():m.end() + 120]
            out.append({"check": "anachronism", "what": f"{name} (released {rel}) in a reference dated {year}",
                        "text": " ".join(entry.split())[:300]})
    return out


def check_text(text):
    body, refs = body_and_refs(text)
    found = impossible_values(body) + anova_rows(body) + p_decisions(body) + anachronisms(refs)
    seen, uniq = set(), []
    for f in found:
        k = (f["check"], f["what"], f["text"][:80])
        if k not in seen:
            seen.add(k)
            uniq.append(f)
    return uniq


def severity(findings):
    """high: a reference that cannot exist, or a broken ANOVA row; review: an
    impossible value (most often a mislabelled statistic: t printed as r) or a
    p-decision inconsistency, high from three of those in one source."""
    kinds = {f["check"] for f in findings}
    if kinds & {"anova-row", "anachronism"}:
        return "high"
    if sum(f["check"] in ("p-decision", "impossible") for f in findings) >= 3:
        return "high"
    return "review" if findings else None


if __name__ == "__main__":
    import json
    import sys
    for path in sys.argv[1:]:
        f = check_text(open(path, encoding="utf-8", errors="replace").read())
        print(path, severity(f))
        for x in f:
            print("  ", json.dumps(x, ensure_ascii=False))
