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

SPECIAL_POPULATION_CLASSES = rl.SPECIAL_POPULATIONS

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


def s01_title(p, st, r):
    b = p.get("protocol", {})
    return FILLED, (f"{_para(b.get('title'))}\n\n"
                    f"Protocol identifier: `{b.get('id')}` version `{b.get('version')}`, "
                    f"effective {b.get('effective_from')}.\n\n"
                    f"*(BRANY asks for a unique study identifier and version date in the "
                    f"footer. Here they are the record's own identity: a version is a "
                    f"separate immutable file, so a modification cannot overwrite the "
                    f"version that was submitted.)*")


def s02_objectives(p, st, r):
    """The purpose lives on the STUDY: a protocol governs a family of
    investigations and has no single question to state."""
    if st is None:
        return UNSPEC, ("*No study plan named. The question lives on the study "
                        "(`study.question`), not the protocol.*")
    out = [_para(st.get("study", {}).get("question")) or gap("study.question is empty")]
    d = st.get("design", {})
    if d.get("detail"):
        out.append(_para(d["detail"]))
    return FILLED, "\n\n".join(out)


def s03_background(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; the background lives on the study.*"
    return FILLED, (_para(st.get("study", {}).get("background"))
                    or gap("study.background is empty"))


def s04_inclusion_exclusion(p, st, r):
    part = p.get("participants", {})
    body = ["**Inclusion**", _md_list(part.get("inclusion")),
            "", "**Exclusion**", _md_list(part.get("exclusion")), ""]
    special = part.get("special_populations")
    if not isinstance(special, dict):
        body.append(gap("the four special populations BRANY requires an explicit "
                        "position on are not addressed: `participants."
                        "special_populations` is absent from this protocol."))
        return PARTIAL, "\n".join(body)
    body.append("**Special populations**, as the template requires — a position on "
                "each of the four:")
    unaddressed = []
    for cls in sorted(SPECIAL_POPULATION_CLASSES):
        stance = special.get(cls)
        if stance is None or stance == "not-addressed":
            unaddressed.append(cls)
            stance = stance or "ABSENT"
        body.append(f"- `{cls}`: **{stance}**")
    if st is not None:
        enrolled = (st.get("enrolment") or {}).get("special_populations") or {}
        if enrolled:
            body += ["", "This study enrols: "
                     + ", ".join(f"`{k}`" for k, v in sorted(enrolled.items())
                                 if v == "included") or "*none of the four*"]
    if unaddressed:
        body += ["", gap("no position is recorded for " + ", ".join(unaddressed)
                         + ". BRANY warns that members of these populations may not be "
                           "enrolled unless named in the inclusion criteria, so silence "
                           "here is a defect rather than a default.")]
        return PARTIAL, "\n".join(body)
    return FILLED, "\n".join(body)


def s05_vulnerable(p, st, r):
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



def s06_setting(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; the setting lives on the study.*"
    setting = st.get("setting") or {}
    lines = [f"**Where the research is conducted.** {_para(setting.get('conducted_where'))}",
             "",
             f"**Where subjects are identified and recruited.** "
             f"{_para(setting.get('recruitment_sites'))}"]
    reqs = setting.get("site_specific_requirements")
    if reqs:
        lines += ["", "**Site-specific requirements**", _md_list(reqs)]
    sites = p.get("sites")
    if sites:
        lines += ["", "**Sites** (from the protocol — the governance applies per site)"]
        for site in sites:
            lines.append(f"- **{_para(site.get('name'))}** — {_para(site.get('role'))}")
            for a in site.get("approvals") or []:
                lines.append(f"  - approval: {a}")
    return FILLED, "\n".join(lines)



def s07_resources(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; resources live on the study.*"
    res = (st.get("setting") or {}).get("resources") or {}
    lines = ["**Staff**", _md_list(res.get("staff"))]
    if res.get("investigator_time"):
        lines += ["", f"**Investigator time.** {_para(res['investigator_time'])}"]
    if res.get("participant_support"):
        lines += ["", f"**Support available to participants.** "
                      f"{_para(res['participant_support'])}"]
    return FILLED, "\n".join(lines)



def s08_number_of_subjects(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; the enrolment target lives on the study.*"
    enr = st.get("enrolment") or {}
    lines = []
    for label, k in (("Planned", "planned"), ("Screened", "screened"),
                     ("Analysed", "analysed")):
        c = enr.get(k)
        if isinstance(c, dict):
            lines.append(f"- **{label}:** {c.get('value')} {c.get('unit')}")
    lines += ["", f"**Justification.** {_para(enr.get('justification'))}",
              "", "*(A count carries its unit, because the same field otherwise reports "
                  "students, classes and studies interchangeably and nothing can read "
                  "it. In a cluster design the two differ and the difference is the "
                  "whole power calculation.)*"]
    return FILLED, "\n".join(lines)



def s09_multisite(p, st, r):
    sites = p.get("sites")
    if not sites:
        return NA, ("Single-site: the protocol records no `sites`. *(Decided by the "
                    "record — adding a second site makes this section required.)*")
    lines = [f"{len(sites)} sites, recorded on the protocol because the governance "
             f"applies per site:"]
    for site in sites:
        lines.append(f"- **{_para(site.get('name'))}** — {_para(site.get('role'))}")
        for a in site.get("approvals") or []:
            lines.append(f"  - approval: {a}")
    setting = (st or {}).get("setting") or {}
    if setting.get("site_specific_requirements"):
        lines += ["", "**Per-site requirements**",
                  _md_list(setting["site_specific_requirements"])]
    coord = setting.get("multi_site_coordination")
    if coord:
        lines += ["", "**How sites are kept in step** (problems, interim results, "
                      "closure)", _md_list(coord)]
        return FILLED, "\n".join(lines)
    lines += ["", gap("`setting.multi_site_coordination` is absent: how problems, "
                      "interim results and study closure are communicated between "
                      "sites. BRANY asks it of a lead investigator coordinating "
                      f"others, and this protocol names {len(sites)} sites.")]
    return PARTIAL, "\n".join(lines)


def s10_recruitment(p, st, r):
    part = p.get("participants", {})
    comp = part.get("compensation") or {}
    body = [_para(part.get("recruitment")) or gap("participants.recruitment is empty"), ""]
    body.append(f"**Population.** {_para(part.get('population')) or '*not recorded*'}")
    body.append("")
    kind = comp.get("kind")
    detail = _para(comp.get("detail"))
    body.append(f"**Payments to subjects.** {kind or '*not recorded*'}"
                + (f" — {detail}" if detail else ""))
    proc = (st or {}).get("procedures") or {}
    if proc.get("recruitment_materials"):
        body += ["", "**Recruitment materials** (BRANY asks for these as attachments)",
                 _md_list(proc["recruitment_materials"])]
    if proc.get("screening"):
        body += ["", f"**Screening.** {_para(proc['screening'])}"]
    if st is None:
        body += ["", "*No study plan named; the materials and screening live on the "
                     "study.*"]
        return PARTIAL, "\n".join(body)
    return FILLED, "\n".join(body)


def s11_timelines(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; timelines live on the study.*"
    t = st.get("timelines") or {}
    return FILLED, "\n".join([
        f"- **An individual subject's participation:** {_para(t.get('participation_duration'))}",
        f"- **Enrolment period:** {_para(t.get('enrolment_period'))}",
        f"- **Estimated completion of the primary analysis:** "
        f"{_para(t.get('estimated_completion'))}",
    ])


def s12_procedures(p, st, r):
    data = p.get("data", {})
    collected = data.get("collected") or []
    parts = []
    if st is not None:
        d = st.get("design", {})
        parts.append(f"**Design.** `{d.get('family')}` — {_para(d.get('detail'))}")
        if d.get("allocation"):
            parts.append(f"**Allocation.** {_para(d['allocation'])}")
        pre = d.get("preregistration") or {}
        parts.append(f"**Preregistration.** registered: {_scalar(pre.get('registered'))}"
                     + (f", {pre.get('registry')} — `{pre.get('identifier')}`"
                        if pre.get("registered") else ""))
        proc = st.get("procedures") or {}
        parts += ["", "**Procedures, in order**", _md_list(proc.get("steps"))]
        parts += ["", "**Instruments** (BRANY asks for these as attachments)",
                  _md_list(proc.get("instruments"))]
    else:
        parts.append("*No study plan named; the design and procedures live on the study.*")
    parts += ["", "**Data collected** (BRANY: \"what data will be collected\")"]
    if collected:
        parts.append("\n".join(
            f"- `{c.get('item')}` — {_para(c.get('purpose')) or 'purpose not recorded'}"
            for c in collected))
    else:
        parts.append("*none recorded*")
    if data.get("prohibited"):
        parts += ["", "**Explicitly not collected**", _md_list(data.get("prohibited"))]
    return (FILLED if st is not None else PARTIAL), "\n".join(parts)


def s13_specimens(p, st, r):
    return NA, ("Not applicable. No biospecimens are collected or banked: this protocol "
                "governs data recorded by a software platform. "
                "*(Rule: applies whenever the protocol declares no biospecimen items. "
                "The schema has no biospecimen concept at all, which is itself the "
                "assertion — there is no way to express one.)*")


def s14_1_analysis(p, st, r):
    """The PLANNED analysis, from the study; what was actually run, from the
    release when there is one. Keeping them apart is the point."""
    if st is None and r is None:
        return UNSPEC, "*No study plan and no release named.*"
    lines = []
    if st is not None:
        plan = st.get("analysis_plan") or {}
        lines += [f"**Planned approach.** {_para(plan.get('approach'))}", "",
                  "**Proposed statistical tests**", _md_list(plan.get("tests"))]
        for label, k in (("Missing data", "missing_data"),
                         ("Multiplicity", "multiplicity")):
            if plan.get(k):
                lines += ["", f"**{label}.** {_para(plan[k])}"]
    if r is not None:
        analyses = r.get("analyses") or []
        if analyses:
            lines += ["", "**Analyses actually run** (from the release)"]
            for a in analyses:
                lines.append(f"- {_para(a.get('title'))}"
                             + (f" — code: `{a['code']}`" if a.get("code") else ""))
    return FILLED, "\n".join(lines)


def s14_2_endpoints(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; endpoints live on the study.*"
    lines = []
    for e in st.get("endpoints") or []:
        lines.append(f"- **{_para(e.get('name'))}** (`{e.get('role')}`) — "
                     f"{_para(e.get('measure'))}, at {_para(e.get('timepoint'))}")
    lines += ["", "*(Declared before anything runs. `observations/` records outcomes as "
                  "MEASURED; the difference between the two lists is what "
                  "preregistration exists to police, and it is only visible because "
                  "they are separate records.)*"]
    return FILLED, "\n".join(lines)



def s14_3_data_quality(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; quality control lives on the study.*"
    q = (st.get("procedures") or {}).get("data_quality") or {}
    return FILLED, _md_list(q.get("procedures"))


def s14_4_confidentiality(p, st, r):
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


def s14_5_future_use(p, st, r):
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



def s15_privacy(p, st, r):
    sp = (p.get("data") or {}).get("subject_privacy")
    if not isinstance(sp, dict):
        return UNSPEC, ("*`data.subject_privacy` is absent from this protocol.* BRANY "
                        "is explicit that this section is NOT data confidentiality: it "
                        "is intrusiveness — how subjects are approached, and how the "
                        "team is entitled to reach information about them. The field "
                        "exists; this protocol has not filled it in.")
    lines = [f"**How subjects are approached.** {_para(sp.get('approach'))}"]
    if sp.get("intrusiveness_measures"):
        lines += ["", "**Putting subjects at ease**", _md_list(sp["intrusiveness_measures"])]
    if sp.get("information_sources"):
        lines += ["", "**How the team is permitted to reach each source of information**",
                  _md_list(sp["information_sources"])]
    return FILLED, "\n".join(lines)


def s16_safety(p, st, r):
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


def s17_withdrawal(p, st, r):
    c = p.get("consent", {})
    w = c.get("withdrawal") or {}
    inv = w.get("investigator_initiated") or {}
    if c.get("required") is not True:
        body = (f"Consent is not obtained under this protocol (`consent.required` is "
                f"{_scalar(c.get('required'))}, mechanism {_scalar(c.get('mechanism'))}), "
                f"so there is no withdrawal from participation to describe.")
        if not inv:
            return NA, body + "\n\n" + gap(
                "investigator-initiated withdrawal — withdrawal WITHOUT the subject's "
                "consent — is a separate question the template asks, and this protocol "
                "records no position on it.")
        return NA, body
    lines = [f"**Withdrawal permitted:** {_scalar(w.get('allowed'))}"]
    if w.get("mechanism"):
        lines += ["", f"**How.** {_para(w['mechanism'])}"]
    if w.get("effect_on_collected_data"):
        lines += ["", f"**Effect on data already collected.** "
                      f"{_para(w['effect_on_collected_data'])}"]
    lines += ["", "*(The schema requires the second of these separately from the first, "
                  "because 'you may withdraw' and 'here is what happens to what you "
                  "already gave us' are two promises and only the second is "
                  "operational.)*"]
    if inv:
        lines += ["", f"**Withdrawal by the investigator, without the subject's "
                      f"consent:** {_scalar(inv.get('allowed'))}"]
        if inv.get("circumstances"):
            lines.append(_md_list(inv["circumstances"]))
        return FILLED, "\n".join(lines)
    lines += ["", gap("investigator-initiated withdrawal has no position recorded on "
                      "this protocol.")]
    return PARTIAL, "\n".join(lines)


def s18_risks(p, st, r):
    risks = p.get("risks") or {}
    identified = risks.get("identified") or []
    lines = [f"**Risk classification:** {_scalar(risks.get('classification'))}", ""]
    dims = ("probability", "magnitude", "duration", "reversibility")
    complete = bool(identified)
    for item in identified:
        lines.append(f"**{_para(item.get('risk'))}**")
        lines.append("")
        for d in dims:
            if item.get(d):
                lines.append(f"- {d}: {_para(item[d])}")
            else:
                complete = False
        lines.append(f"- mitigation: {_para(item.get('mitigation')) or '*none recorded*'}")
        lines.append("")
    if not identified:
        lines.append("*No specific risks recorded (an empty list means somebody looked "
                     "and found none).*")
    if not complete and identified:
        lines.append(gap("BRANY asks for probability, magnitude, duration and "
                         "reversibility on every risk; at least one is missing above."))
        return PARTIAL, "\n".join(lines)
    return FILLED, "\n".join(lines).rstrip()


def s19_benefits(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; benefits live on the study.*"
    b = st.get("benefits") or {}
    return FILLED, (f"**Direct benefit to participants:** `{b.get('to_participants')}`"
                    f"\n\n{_para(b.get('detail'))}")



def s20_cbpr(p, st, r):
    if st is None:
        return UNSPEC, ("*No study plan named.* This cannot be answered "
                        "'not applicable' by default: nothing outside the study record "
                        "says whether it was co-designed.")
    c = st.get("community_involvement") or {}
    return FILLED, (f"**Community involved in design or conduct:** "
                    f"{_scalar(c.get('involved'))}\n\n{_para(c.get('detail'))}")



def s21_sharing_results(p, st, r):
    if st is None:
        return UNSPEC, "*No study plan named; the results-sharing policy lives on the study.*"
    sh = st.get("results_sharing") or {}
    return FILLED, f"**Policy:** `{sh.get('policy')}`\n\n{_para(sh.get('detail'))}"


def s22_prior_approvals(p, st, r):
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


def s23_injury_compensation(p, st, r):
    cls = (p.get("risks") or {}).get("classification")
    if cls == "minimal":
        return NA, ("Not applicable — BRANY requires this only where the research involves "
                    "more than minimal risk, and `risks.classification` is `minimal`. "
                    "*(Decided by the record, as with section 16.)*")
    return NO_FIELD, gap(
        f"`risks.classification` is `{cls}`, so this may be required, and there is no "
        f"field for injury-compensation arrangements.")



def s24_economic_burden(p, st, r):
    if st is None:
        return UNSPEC, ("*No study plan named; participant burden lives on the study.* "
                        "The protocol's `participants.compensation` is the opposite "
                        "direction — payment TO the subject — and does not answer it.")
    b = st.get("participant_burden") or {}
    return FILLED, (f"**Costs borne by the subject:** `{b.get('costs')}`"
                    f"\n\n{_para(b.get('detail'))}")


def s25_consent(p, st, r):
    c = p.get("consent", {})
    proc = c.get("process") or {}
    waiver = c.get("waiver") or {}
    minors = c.get("minors") or {}
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
    lines += ["", "**What the participant was actually shown**",
              _md_list(c.get("information_provided"), empty="not recorded")]

    missing = []
    if proc:
        lines += ["", "**The consent process**",
                  f"- documented as: `{proc.get('documentation')}`"]
        for label, k in (("where", "location"), ("when", "timing"),
                         ("obtained by", "obtained_by"),
                         ("waiting period", "waiting_period")):
            if proc.get(k):
                lines.append(f"- {label}: {_para(proc[k])}")
        if proc.get("languages"):
            lines.append(f"- languages: {', '.join(proc['languages'])}")
        for label, k in (("Ensuring understanding", "comprehension_measures"),
                         ("Minimising coercion", "coercion_safeguards")):
            if proc.get(k):
                lines += ["", f"**{label}**", _md_list(proc[k])]
    else:
        missing.append("`consent.process` — where and when consent is obtained, by "
                       "whom, after what waiting period, in which languages, and "
                       "whether it is documented in writing")

    kind = waiver.get("kind")
    if kind and kind != "none":
        lines += ["", f"**Waiver:** `{kind}`, justified against each regulatory "
                      f"criterion:"]
        for crit, entry in (waiver.get("justification") or {}).items():
            if isinstance(entry, dict):
                lines.append(f"- `{crit}`: {_scalar(entry.get('met'))} — "
                             f"{_para(entry.get('rationale'))}")
    elif kind == "none":
        lines += ["", "**Waiver:** none claimed — consent is obtained and documented."]
    else:
        missing.append("`consent.waiver` — whether a waiver of consent, of "
                       "documentation, or an alteration applies, and its justification "
                       "against each of the five regulatory criteria")

    if minors:
        lines += ["", "**Subjects who are not yet adults**",
                  f"- age of majority: {minors.get('age_of_majority')} "
                  f"({_para(minors.get('jurisdiction'))})",
                  f"- parental permission: `{minors.get('parental_permission')}`",
                  f"- assent obtained from: `{minors.get('assent')}`",
                  f"- assent documented as: `{minors.get('assent_documentation')}`",
                  f"- re-consent on attaining majority mid-study: "
                  f"{_scalar(minors.get('reconsent_on_majority'))}"]
        if minors.get("assent_scope_detail"):
            lines.append(f"- which children assent: "
                         f"{_para(minors['assent_scope_detail'])}")
        lines += ["", "*(BRANY's teen-parent form carries a section for subjects who "
                      "turn 18 during a study. `reconsent_on_majority` is the field "
                      "that makes it actionable: a running system knows when that date "
                      "passes for a given participant, and a filed document does not.)*"]
    else:
        enrols_minors = ((st or {}).get("enrolment") or {}).get(
            "special_populations", {}).get("minors") == "included"
        note = ("`consent.minors` — age of majority and its jurisdiction, whose "
                "permission, whose assent, how documented, and re-consent on turning "
                "18 mid-study")
        missing.append(note + (" **— and this study enrols minors**"
                               if enrols_minors else ""))

    # Record-driven, like sections 16 and 23: when the protocol excludes the
    # population, the template's questions about it are genuinely inapplicable
    # rather than unanswered.
    stance = (p.get("participants") or {}).get("special_populations", {}) \
        .get("adults-unable-to-consent")
    if stance == "excluded":
        lines += ["", "*Adults unable to consent are `excluded` by this protocol, so "
                      "the legally-authorised-representative hierarchy and the capacity "
                      "assessment do not apply. Including them would make both "
                      "required, and neither has a field yet.*"]
    else:
        missing.append("adults unable to consent: the ordered list of legally "
                       "authorised representatives, and the capacity assessment — no "
                       f"field, and this protocol records `{stance}` for that class")
    if missing:
        lines += ["", "**Not recorded on this protocol:**"] + [f"- {m}" for m in missing]
        return PARTIAL, "\n".join(lines)
    return FILLED, "\n".join(lines)


def s26_drugs_devices(p, st, r):
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


def render(protocol, study=None, release=None):
    """[(number, title, status, body)] for every template section."""
    return [(num, title, *fn(protocol, study, release)) for num, title, fn in SECTIONS]


def document(protocol, study, release, rows):
    p = protocol.get("protocol", {})
    head = [
        f"# BRANY SBER Protocol — {p.get('title', '')}".rstrip(),
        "",
        f"> Rendered from `research/protocols/{p.get('id')}/{p.get('version')}.yaml`"
        + (f", `research/studies/{study['study']['id']}/"
           f"{study['study']['version']}.yaml`" if study else "")
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
    ap.add_argument("--study", help="study id, optionally id@version — the plan, "
                                    "which is what an IRB actually reviews")
    ap.add_argument("--release", help="release id, optionally id@version, for the "
                                      "analysis section")
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

    def _pick(loader, spec, label):
        recs, errs = loader()
        for e in errs:
            print(f"error: {e}", file=sys.stderr)
        oid, _, over = spec.partition("@")
        vs = sorted((v for i, v in recs if i == oid), key=rl.semver)
        if not vs:
            print(f"error: no {label} {oid!r}", file=sys.stderr)
            return None, 1
        return recs[(oid, over or vs[-1])], 0

    study = None
    if args.study:
        study, rc = _pick(rl.load_studies, args.study, "study")
        if rc:
            return rc

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

    rows = render(protocol, study, release)
    if args.coverage or args.gaps:
        print(coverage(rows, gaps_only=args.gaps))
    else:
        print(document(protocol, study, release, rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
