#!/usr/bin/env python3
"""Render a `research/protocols/` configuration as BRANY's SBER protocol document.

BRANY's own template says: *"We prefer you use this template. However, you may
use a different format, order, outline, or template provided the necessary
information from this template is included."* This script answers the question
that sentence raises — **can our configuration supply the necessary
information?** — by attempting every section and reporting, per section, where
the answer came from or why there is none.

THE OUTPUT IS A COVERAGE REPORT FIRST AND A DOCUMENT SECOND. Any section this
schema cannot answer renders as a loud marker, never as plausible prose. That is
the same discipline the protocol fixtures use for `NOT ESTABLISHED`: a section
filled in by assumption reads as verified, which is worse than an absent one.

Four statuses, and the distinctions between them are the whole point:

  filled        rendered from configuration
  partial       rendered, but the template asks for more than the schema holds
  unspecified   the schema HAS the field; this protocol says nothing is
                established yet. A gap in the record, not in the schema.
  not-applicable  categorically inapplicable, by a rule stated in the output —
                some of these are decided by the record itself (BRANY requires
                a safety-monitoring plan only above minimal risk, so
                `risks.classification` decides section 16)
  no-field      THE SCHEMA HAS NOWHERE TO PUT THIS. The answer to "what could we
                not generate", and the only status that is a property of the
                schema rather than of a particular protocol.

Usage:
    python3 scripts/render_brany_protocol.py <protocol-id> [--version X.Y.Z]
                                             [--release <id>[@X.Y.Z]]
    python3 scripts/render_brany_protocol.py <protocol-id> --coverage
    python3 scripts/render_brany_protocol.py --gaps        # schema gaps alone
"""
from __future__ import annotations

import argparse
import sys
import textwrap

import research_lib as rl

FILLED = "filled"
PARTIAL = "partial"
UNSPEC = "unspecified"
NA = "not-applicable"
NO_FIELD = "no-field"

ORDER = [FILLED, PARTIAL, UNSPEC, NA, NO_FIELD]

# A section the schema cannot answer renders as this. Deliberately shouty and
# deliberately not prose: nobody should be able to paste the output into a
# submission without noticing.
def gap(what: str) -> str:
    return f"**NOT REPRESENTED IN PROTOCOL CONFIGURATION** — {what}"


def _md_list(items, empty="none recorded"):
    items = [i for i in (items or []) if str(i).strip()]
    if not items:
        return f"*{empty}*"
    return "\n".join(f"- {str(i).strip()}" for i in items)


def _para(value):
    return " ".join(str(value).split()) if value else None


def _scalar(value, absent="not recorded"):
    """YAML spelling, not Python's. `False` in a rendered governance document
    reads as a typo; `false` reads as the value it is."""
    if value is None:
        return f"*{absent}*"
    if isinstance(value, bool):
        return "`true`" if value else "`false`"
    return f"`{value}`"


# ---------------------------------------------------------------- sections
# Each renderer takes (protocol_record, release_record_or_None) and returns
# (status, body). Statuses are computed from the record wherever the record can
# decide them; NO_FIELD is structural and says so.


def s01_title(p, r):
    b = p.get("protocol", {})
    return FILLED, (f"{_para(b.get('title'))}\n\n"
                    f"Protocol identifier: `{b.get('id')}` version `{b.get('version')}`, "
                    f"effective {b.get('effective_from')}.\n\n"
                    f"*(BRANY asks for a unique study identifier and version date in the "
                    f"footer. Here they are the record's own identity: a version is a "
                    f"separate immutable file, so a modification cannot overwrite the "
                    f"version that was submitted.)*")


def s02_objectives(p, r):
    if r is None:
        return UNSPEC, ("*No research release named. The purpose and aims live on the "
                        "release (`release.question`), not the protocol — a protocol "
                        "governs a family of investigations.*")
    rel = r.get("release", {})
    design = r.get("research_design", {})
    out = [_para(rel.get("question")) or gap("release.question is empty")]
    if design.get("detail"):
        out.append(_para(design["detail"]))
    return FILLED, "\n\n".join(out)


def s03_background(p, r):
    return NO_FIELD, gap(
        "neither the protocol nor the release schema carries prior literature, gaps in "
        "current knowledge, or preliminary data. The wiki's claim pages hold exactly "
        "this material, but nothing links a protocol to them.")


def s04_inclusion_exclusion(p, r):
    part = p.get("participants", {})
    body = ["**Inclusion**", _md_list(part.get("inclusion")),
            "", "**Exclusion**", _md_list(part.get("exclusion")), "",
            gap("BRANY additionally requires an explicit include/exclude statement for "
                "each of four special populations — adults unable to consent, minors, "
                "pregnant women, prisoners — and warns that members of those populations "
                "may not be enrolled unless named in the inclusion criteria. The schema "
                "has free-text lists, so it cannot guarantee all four were addressed.")]
    return PARTIAL, "\n".join(body)


def s05_vulnerable(p, r):
    groups = p.get("participants", {}).get("vulnerable_populations") or []
    if not groups:
        return UNSPEC, "*No vulnerable populations recorded for this protocol.*"
    out = []
    for g in groups:
        out.append(f"**{_para(g.get('group'))}**")
        out.append("")
        out.append("Safeguards:")
        out.append(_md_list(g.get("safeguards")))
        out.append("")
    return FILLED, "\n".join(out).rstrip()


def s06_setting(p, r):
    return NO_FIELD, gap(
        "there is no field for where the research is conducted, where subjects are "
        "identified and recruited, or for site-specific regulation. `data.storage.location` "
        "says where DATA lives, which is a different question and must not be reused for it.")


def s07_resources(p, r):
    return NO_FIELD, gap(
        "no field for staff, their qualifications, investigator time, feasibility of the "
        "recruitment target, or available support resources.")


def s08_number_of_subjects(p, r):
    return NO_FIELD, gap(
        "no planned enrolment target. `observations/` records an achieved sample per "
        "result AFTER a study runs (`evidence_base.size`), which is a different fact "
        "from the number a protocol proposes to accrue.")


def s09_multisite(p, r):
    return NO_FIELD, gap(
        "no field for multi-site conduct, per-site approvals, or how modifications are "
        "communicated to sites. Relevant as soon as a study spans institutions.")


def s10_recruitment(p, r):
    part = p.get("participants", {})
    comp = part.get("compensation") or {}
    body = [_para(part.get("recruitment")) or gap("participants.recruitment is empty"), ""]
    body.append(f"**Population.** {_para(part.get('population')) or '*not recorded*'}")
    body.append("")
    kind = comp.get("kind")
    detail = _para(comp.get("detail"))
    body.append(f"**Payments to subjects.** {kind or '*not recorded*'}"
                + (f" — {detail}" if detail else ""))
    body.append("")
    body.append(gap("BRANY also asks for the recruitment MATERIALS themselves "
                    "(advertisements, scripts, screening procedure). The schema records "
                    "the method, not the artifacts."))
    return PARTIAL, "\n".join(body)


def s11_timelines(p, r):
    return NO_FIELD, gap(
        "no field for an individual subject's duration of participation, the enrolment "
        "period, or the estimated completion date. `protocol.effective_from` dates the "
        "governance, not the study.")


def s12_procedures(p, r):
    data = p.get("data", {})
    collected = data.get("collected") or []
    parts = []
    if r is not None:
        d = r.get("research_design", {})
        parts.append(f"**Design.** {d.get('family', '*not recorded*')}"
                     + (f" — {_para(d.get('detail'))}" if d.get("detail") else ""))
        pre = d.get("preregistration") or {}
        if pre:
            parts.append(f"**Preregistration.** registered: {pre.get('registered')}"
                         + (f" — {_para(pre.get('note'))}" if pre.get("note") else ""))
    else:
        parts.append("*No release named; the study design lives on the release.*")
    parts.append("")
    parts.append("**Data collected** (BRANY: \"the source records that will be used to "
                 "collect data about subjects\" and \"what data will be collected\")")
    if collected:
        rows = []
        for c in collected:
            rows.append(f"- `{c.get('item')}` — {_para(c.get('purpose')) or 'purpose not recorded'}")
        parts.append("\n".join(rows))
    else:
        parts.append("*none recorded*")
    if data.get("prohibited"):
        parts.append("")
        parts.append("**Explicitly not collected**")
        parts.append(_md_list(data.get("prohibited")))
    parts.append("")
    parts.append(gap("the step-by-step procedure a subject undergoes, and the instruments "
                     "themselves (surveys, scripts, data-collection forms), which BRANY "
                     "asks to be attached."))
    return PARTIAL, "\n".join(parts)


def s13_specimens(p, r):
    return NA, ("Not applicable. No biospecimens are collected or banked: this protocol "
                "governs data recorded by a software platform. "
                "*(Rule: applies whenever the protocol declares no biospecimen items. "
                "The schema has no biospecimen concept at all, which is itself the "
                "assertion — there is no way to express one.)*")


def s14_1_analysis(p, r):
    if r is None:
        return UNSPEC, "*No release named; the analysis plan lives on the release.*"
    analyses = r.get("analyses") or []
    if not analyses:
        return UNSPEC, "*The release records no analyses.*"
    out = []
    for a in analyses:
        out.append(f"**{_para(a.get('title'))}**")
        if a.get("code"):
            out.append(f"Code: `{a['code']}`")
        if a.get("ai_processing") is not None:
            out.append(f"AI processing: {a['ai_processing']}")
        out.append("")
    return FILLED, "\n".join(out).rstrip()


def s14_2_endpoints(p, r):
    return NO_FIELD, gap(
        "no pre-declared endpoint or outcome variable. `observations/` records outcomes "
        "as MEASURED; a protocol needs them as DECLARED, and the difference between the "
        "two is what preregistration exists to police.")


def s14_3_data_quality(p, r):
    return NO_FIELD, gap("no field for quality-control procedures on collected data.")


def s14_4_confidentiality(p, r):
    d = p.get("data", {})
    ident = d.get("identifiability") or {}
    deid = d.get("deidentification") or {}
    store = d.get("storage") or {}
    ret = d.get("retention") or {}
    access = d.get("access") or {}
    lines = [
        f"**Identifiability.** as collected: {_scalar(ident.get('collected'))}; "
        f"as published: {_scalar(ident.get('published'))}.",
        "",
        "*(BRANY asks whether data are ANONYMOUS — no identifiers ever linked — or "
        "DE-IDENTIFIED — identifiers removed but a link retained. This schema's scale is "
        "finer and the mapping is not one-to-one: `pseudonymised` is BRANY's "
        "de-identified, `anonymous` is their anonymous, and `deidentified` here asserts "
        "the link is gone. Worth confirming the reading with the IRB rather than assuming "
        "it.)*",
        "",
        "**De-identification.**",
        f"- method: {_para(deid.get('method')) or '*not recorded*'}",
        f"- applied at: {_scalar(deid.get('applied_at'))}",
        f"- reversible: {_scalar(deid.get('reversible'))}",
        f"- key holder: {_para(deid.get('key_holder')) or '*not recorded*'}",
        "",
        "**Storage controls.**",
        f"- location: {_para(store.get('location')) or '*not recorded*'}",
        f"- encryption at rest: {_scalar(store.get('encryption_at_rest'))}",
        f"- encryption in transit: {_scalar(store.get('encryption_in_transit'))}",
        f"- access logging: {_scalar(store.get('access_logging'))}",
        "",
        "**Retention.**",
        f"- raw: {_para(ret.get('raw')) or '*not recorded*'}",
        f"- derived: {_para(ret.get('derived')) or '*not recorded*'}",
        f"- basis: {_para(ret.get('basis')) or '*not recorded*'}",
        "",
        "**Who has access**, by class:",
    ]
    for cls in ("raw", "derived", "published"):
        lines.append(f"- {cls}: " + (", ".join(access.get(cls) or []) or "*not recorded*"))

    # The tri-states are the honest-gap case: the schema HAS the field and this
    # protocol has not established it. That is exactly why they are tri-state
    # rather than boolean.
    unset = [k for k in ("encryption_at_rest", "encryption_in_transit", "access_logging")
             if store.get(k) == "unspecified"]
    status = UNSPEC if unset else FILLED
    if unset:
        lines += ["", f"*{len(unset)} storage control(s) are `unspecified` — nobody has "
                      f"checked the hosting configuration. BRANY asks these directly, so "
                      f"they must be established before a submission, not filled in by "
                      f"assumption.*"]
    return status, "\n".join(lines)


def s14_5_future_use(p, r):
    c = p.get("consent", {})
    uses = c.get("permitted_uses") or {}
    lines = ["**Permitted uses**, as closed classes:"]
    for cls in sorted(uses):
        lines.append(f"- `{cls}`: **{uses[cls]}**")
    if not uses:
        lines.append("*none recorded*")
    if c.get("permitted_uses_note"):
        lines += ["", _para(c["permitted_uses_note"])]
    lines += ["", "*(This is the section with the cleanest correspondence to BRANY's own "
                  "documents: their SBER consent form offers exactly two authorised "
                  "future-use paragraphs, and `secondary-research-by-others: permitted | "
                  "prohibited` selects between them. A release that names a use this "
                  "mapping prohibits fails validation.)*"]
    return FILLED, "\n".join(lines)


def s15_privacy(p, r):
    return NO_FIELD, gap(
        "BRANY is explicit that this is NOT data confidentiality — it is intrusiveness: "
        "how subjects are approached, how they are put at ease, and how the team is "
        "permitted to reach any source of information about them. The schema covers the "
        "data half thoroughly and has nothing for the interaction half.")


def s16_safety(p, r):
    cls = (p.get("risks") or {}).get("classification")
    if cls == "minimal":
        return NA, ("Not applicable — BRANY requires a safety-monitoring plan only where "
                    "research involves more than minimal risk, and `risks.classification` "
                    "is `minimal`.\n\n*(This determination is made by the record, not by "
                    "the author of this document: change the classification and the "
                    "section becomes required.)*")
    if cls == "more-than-minimal":
        return NO_FIELD, gap(
            "`risks.classification` is `more-than-minimal`, so BRANY requires a monitoring "
            "plan — review body, data reviewed, frequency, suspension triggers — and the "
            "schema has no field for any of it.")
    return UNSPEC, (f"`risks.classification` is `{cls}`, so whether this section is "
                    f"required cannot be decided. BRANY's trigger is 'more than minimal "
                    f"risk'; an undetermined classification decides nothing.")


def s17_withdrawal(p, r):
    c = p.get("consent", {})
    if c.get("required") is not True:
        return NA, (f"Consent is not obtained under this protocol "
                    f"(`consent.required` is {_scalar(c.get('required'))}, mechanism "
                    f"{_scalar(c.get('mechanism'))}), so there is no withdrawal from "
                    f"participation to describe.\n\n"
                    + gap("BRANY also asks about withdrawal WITHOUT the subject's "
                          "consent — investigator-initiated termination — which the "
                          "schema does not represent under any consent arrangement."))
    w = c.get("withdrawal") or {}
    lines = [f"**Withdrawal permitted:** {_scalar(w.get('allowed'))}"]
    if w.get("mechanism"):
        lines += ["", f"**How.** {_para(w['mechanism'])}"]
    if w.get("effect_on_collected_data"):
        lines += ["", f"**Effect on data already collected.** "
                      f"{_para(w['effect_on_collected_data'])}"]
    lines += ["", "*(The schema requires the second of these separately from the first, "
                  "because 'you may withdraw' and 'here is what happens to what you "
                  "already gave us' are two promises and only the second is operational.)*",
              "", gap("investigator-initiated withdrawal and orderly-termination "
                      "procedures have no field.")]
    return PARTIAL, "\n".join(lines)


def s18_risks(p, r):
    risks = p.get("risks") or {}
    identified = risks.get("identified") or []
    lines = [f"**Risk classification:** {_scalar(risks.get('classification'))}", ""]
    if identified:
        for item in identified:
            lines.append(f"- **{_para(item.get('risk'))}** — "
                         f"mitigation: {_para(item.get('mitigation')) or '*none recorded*'}")
    else:
        lines.append("*No specific risks recorded.*")
    lines += ["", gap("BRANY asks for probability, magnitude, duration and reversibility "
                      "per risk; the schema records the risk and its mitigation as prose.")]
    return PARTIAL, "\n".join(lines)


def s19_benefits(p, r):
    return NO_FIELD, gap(
        "no field for direct benefit to subjects, or for the statement that there is none. "
        "BRANY requires one or the other explicitly.")


def s20_cbpr(p, r):
    return NO_FIELD, gap(
        "no field for community involvement in the design and conduct of the research. "
        "This cannot be auto-answered 'not applicable': a co-designed study would need it, "
        "and nothing in the record says whether this is one.")


def s21_sharing_results(p, r):
    return NO_FIELD, gap(
        "no field for whether study results or individual results are returned to "
        "subjects, or how.")


def s22_prior_approvals(p, r):
    er = p.get("external_review") or {}
    lines = [f"**Status:** {_scalar(er.get('status'))}"]
    for label, k in (("Authority", "authority"), ("Approval id", "approval_id"),
                     ("Reviewed at", "reviewed_at")):
        if er.get(k):
            lines.append(f"**{label}:** {er[k]}")
    if er.get("determination"):
        lines += ["", _para(er["determination"])]
    status = UNSPEC if er.get("status") == "not-determined" else FILLED
    if status is UNSPEC:
        lines += ["", "*`not-determined` means nobody has established whether external "
                      "review applies — which is a different statement from "
                      "`not-required`, and the reason the vocabulary has five values "
                      "rather than being a boolean.*"]
    return status, "\n".join(lines)


def s23_injury_compensation(p, r):
    cls = (p.get("risks") or {}).get("classification")
    if cls == "minimal":
        return NA, ("Not applicable — BRANY requires this only where the research involves "
                    "more than minimal risk, and `risks.classification` is `minimal`. "
                    "*(Decided by the record, as with section 16.)*")
    return NO_FIELD, gap(
        f"`risks.classification` is `{cls}`, so this may be required, and there is no "
        f"field for injury-compensation arrangements.")


def s24_economic_burden(p, r):
    comp = (p.get("participants") or {}).get("compensation") or {}
    return NO_FIELD, gap(
        "no field for costs a subject bears by participating. "
        f"`participants.compensation` records the opposite direction — payment TO the "
        f"subject, here `{comp.get('kind', 'not recorded')}` — and must not be reused for it.")


def s25_consent(p, r):
    c = p.get("consent", {})
    lines = [
        f"**Consent required:** {_scalar(c.get('required'))}  ",
        f"**Mechanism:** {_scalar(c.get('mechanism'))}  ",
        f"**Processing basis:** {_scalar(c.get('basis'))}",
        "",
        "**AI processing disclosed to participants:** "
        f"{_scalar(c.get('ai_processing_disclosed'))}",
    ]
    if c.get("ai_processing_detail"):
        lines.append(f"\n{_para(c['ai_processing_detail'])}")
    info = c.get("information_provided")
    lines += ["", "**What the participant was actually shown**"]
    lines.append(_md_list(info, empty="not recorded"))
    lines += [
        "",
        gap("the template's consent MECHANICS have no fields: where and when consent is "
            "obtained; the waiting period; who obtains it and their role; steps to "
            "minimise coercion; how understanding is ensured; whether consent is "
            "documented in writing."),
        "",
        gap("waiver of consent, and waiver of DOCUMENTATION of consent, each require a "
            "justification against the regulatory criteria BRANY lists. `mechanism: "
            "waived` records that a waiver applies and nothing about why it qualifies."),
        "",
        gap("non-English-speaking subjects: which languages, and how materials and the "
            "consent discussion are provided in them."),
        "",
        gap("MINORS — the largest cluster. Nothing represents: the age of consent in the "
            "applicable jurisdiction; whether permission is sought from one parent or "
            "both; who other than a parent may give permission; whether assent is "
            "obtained, from which children, and how it is documented; or re-consent when "
            "a subject turns 18 mid-study, which BRANY's teen-parent form has a section "
            "for. `participants.age_assurance` records how age is ESTABLISHED, which is "
            "a prerequisite for these questions and not an answer to any of them."),
        "",
        gap("adults unable to consent: the ordered list of legally authorised "
            "representatives, and the capacity assessment."),
    ]
    return PARTIAL, "\n".join(lines)


def s26_drugs_devices(p, r):
    return NA, ("Not applicable. No drug or device is administered. *(As with section 13, "
                "the schema has no concept of one, which is what makes the answer "
                "structural rather than an assertion by the author.)*")


SECTIONS = [
    ("1", "STUDY (PROTOCOL) TITLE", s01_title),
    ("2", "OBJECTIVES", s02_objectives),
    ("3", "BACKGROUND", s03_background),
    ("4", "INCLUSION AND EXCLUSION CRITERIA", s04_inclusion_exclusion),
    ("5", "VULNERABLE POPULATIONS", s05_vulnerable),
    ("6", "SETTING", s06_setting),
    ("7", "RESOURCES", s07_resources),
    ("8", "NUMBER OF SUBJECTS", s08_number_of_subjects),
    ("9", "MULTI-SITE RESEARCH", s09_multisite),
    ("10", "RECRUITMENT METHODS", s10_recruitment),
    ("11", "STUDY TIMELINES", s11_timelines),
    ("12", "PROCEDURES INVOLVED", s12_procedures),
    ("13", "SPECIMEN BANKING", s13_specimens),
    ("14.1", "DATA MANAGEMENT — Data Analysis", s14_1_analysis),
    ("14.2", "DATA MANAGEMENT — Study Endpoints", s14_2_endpoints),
    ("14.3", "DATA MANAGEMENT — Data Quality", s14_3_data_quality),
    ("14.4", "DATA MANAGEMENT — Confidentiality", s14_4_confidentiality),
    ("14.5", "DATA MANAGEMENT — Future Use of Data", s14_5_future_use),
    ("15", "PROTECTING THE PRIVACY OF SUBJECTS", s15_privacy),
    ("16", "ENSURING THE SAFETY OF SUBJECTS", s16_safety),
    ("17", "WITHDRAWAL OF SUBJECTS", s17_withdrawal),
    ("18", "RISKS TO SUBJECTS", s18_risks),
    ("19", "POTENTIAL BENEFITS TO SUBJECTS", s19_benefits),
    ("20", "COMMUNITY-BASED PARTICIPATORY RESEARCH", s20_cbpr),
    ("21", "SHARING OF RESULTS WITH SUBJECTS", s21_sharing_results),
    ("22", "PRIOR APPROVALS", s22_prior_approvals),
    ("23", "COMPENSATION FOR RESEARCH-RELATED INJURY", s23_injury_compensation),
    ("24", "ECONOMIC BURDEN TO SUBJECTS", s24_economic_burden),
    ("25", "CONSENT PROCESS AND DOCUMENTATION", s25_consent),
    ("26", "DRUGS OR DEVICES", s26_drugs_devices),
]


def render(protocol, release=None):
    """[(number, title, status, body)] for every template section."""
    return [(num, title, *fn(protocol, release)) for num, title, fn in SECTIONS]


def document(protocol, release, rows):
    p = protocol.get("protocol", {})
    head = [
        f"# BRANY SBER Protocol — {p.get('title', '')}".rstrip(),
        "",
        f"> Rendered from `research/protocols/{p.get('id')}/{p.get('version')}.yaml`"
        + (f" and `research/releases/{release['release']['id']}/"
           f"{release['release']['version']}.yaml`" if release else "")
        + " by `scripts/render_brany_protocol.py`.",
        ">",
        "> **This is a generated mapping, not a submission.** Every section below was "
        "either filled from configuration or marked as a gap. No section was written by "
        "hand, and nothing absent from the configuration has been supplied by inference.",
        "",
        "---",
        "",
    ]
    body = []
    for num, title, status, text in rows:
        body += [f"## {num}) {title}", "", f"`status: {status}`", "", text, ""]
    return "\n".join(head + body)


def coverage(rows, *, gaps_only=False):
    counts = {s: 0 for s in ORDER}
    for _, _, status, _ in rows:
        counts[status] += 1
    out = []
    if not gaps_only:
        width = max(len(t) for _, t, _, _ in rows)
        for num, title, status, _ in rows:
            out.append(f"  {num:<5} {title:<{width}}  {status}")
        out.append("")
        out.append("  " + " · ".join(f"{counts[s]} {s}" for s in ORDER if counts[s]))
        out.append("")
    unanswerable = [(n, t) for n, t, s, _ in rows if s == NO_FIELD]
    out.append(f"  {len(unanswerable)} of {len(rows)} sections CANNOT be answered from the "
               f"protocol schema at all:")
    for n, t in unanswerable:
        out.append(f"    {n:<5} {t}")
    soft = [(n, t) for n, t, s, _ in rows if s in (PARTIAL, UNSPEC)]
    out.append("")
    out.append(f"  {len(soft)} more are answered only in part:")
    for n, t in soft:
        out.append(f"    {n:<5} {t}")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("protocol", nargs="?", help="protocol id under research/protocols/")
    ap.add_argument("--version", help="protocol version (default: highest present)")
    ap.add_argument("--release", help="release id, optionally id@version, for the "
                                      "design and analysis sections")
    ap.add_argument("--coverage", action="store_true", help="per-section status table")
    ap.add_argument("--gaps", action="store_true",
                    help="only the sections the schema cannot answer")
    args = ap.parse_args(argv)

    protocols, errs = rl.load_protocols()
    for e in errs:
        print(f"error: {e}", file=sys.stderr)
    if not args.protocol:
        ids = sorted({pid for pid, _ in protocols})
        print("protocols:\n" + "\n".join(f"  {i}" for i in ids))
        return 0

    versions = sorted((v for pid, v in protocols if pid == args.protocol), key=rl.semver)
    if not versions:
        print(f"error: no protocol {args.protocol!r}", file=sys.stderr)
        return 1
    version = args.version or versions[-1]
    protocol = protocols.get((args.protocol, version))
    if protocol is None:
        print(f"error: {args.protocol} has no version {version}", file=sys.stderr)
        return 1

    release = None
    if args.release:
        releases, rerrs = rl.load_releases()
        for e in rerrs:
            print(f"error: {e}", file=sys.stderr)
        rid, _, rver = args.release.partition("@")
        rvs = sorted((v for i, v in releases if i == rid), key=rl.semver)
        if not rvs:
            print(f"error: no release {rid!r}", file=sys.stderr)
            return 1
        release = releases[(rid, rver or rvs[-1])]

    rows = render(protocol, release)
    if args.coverage or args.gaps:
        print(coverage(rows, gaps_only=args.gaps))
    else:
        print(document(protocol, release, rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
