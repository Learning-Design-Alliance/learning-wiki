---
type: claim
title: "Operational resolution records require workflow-semantic checks before interpretation: one administrator accounts for 72.7% of attributed human resolutions, most administrative closures occur in synchronous bulk events, and the accepted_derived field encodes resolver identity rather than acceptance"
description: "Operational resolution records require workflow-semantic checks before interpretation: one administrator accounts for 72.7% of attributed human resolutions, most administrative closures occur in synchronous bulk event..."
id: resolution-record-semantics-attribution-and-coding-caveats
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: gupta-2026
    resource: "https://doi.org/10.48550/arxiv.2609.38967"
    title: "Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967 [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)"
    author: Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S.
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: gupta-2026-2
    resource: "https://doi.org/10.48550/arxiv.2609.38967"
    title: "Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967. [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)"
    author: Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Operational resolution records require workflow-semantic checks before interpretation: one administrator accounts for 72.7% of attributed human resolutions, most administrative closures occur in synchronous bulk events, and the accepted_derived field encodes resolver identity rather than acceptance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Among 1,408 resolutions with an identifiable human responder, one administrator accounts for 1,024 (72.7%), with no other individual exceeding 4.5%; 99.7% of that administrator's records carry the direct-answer path. [→ Gupta 2026](#gupta-2026)
`q2 i?` The accepted_derived field is true for every resolution path except self-resolution, constituting a perfect partition on whether the resolver differed from the asker rather than on acceptance quality. [→ Gupta 2026 (2)](#gupta-2026-2)

## Evidence

### Gupta 2026

Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967 [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)

`q2 · i?` · `design · r2`

Attribution and outcome-coding analysis of the deployment record (RQ3). The administrator accounts for 91.0% of all 1,122 human_admin_direct records; the full distribution is shown in Fig. 2 with identities anonymised.

> "Among the 1,408 resolutions with an identifiable human responder,oneadministratoraccountsfor1,024,or72.7%,withnootherindividualexceeding4.5%. Ofthatadministrator's1,024records,1,021,or99.7%,carrythehuman_admin_directpath"

### Gupta 2026 (2)

Gupta, J., Ayinampudi, P., Aditya B.M.V., Hegade, P., Sharma, R., Sharma, S., Meenakshi, V., Iyengar, S.R.S. (2026). What Students Actually Ask: Demand Structure and Automation Potential in a Hybrid Support System. arXiv:2609.38967. https://arxiv.org/abs/2609.38967. [doi:10.48550/arxiv.2609.38967](https://doi.org/10.48550/arxiv.2609.38967)

`q2 · i?` · `design · r2`

Field-level audit of the record export across all resolution paths. The article also reports that the resolver email field denotes the author on administrative paths but the approver on peer paths, and that 118 of 119 records lacking a resolver email carry a peer identifier without a recorded approver.

> "Theaccepted_derivedfieldistrueforeveryresolutionpathexceptselfresolutionandoneunresolved record,bothofwhichareuniformlyfalse. Thisconstitutesaperfectpartitiononwhethertheresolverdiffered from the asker."

## Discussion


## Related Claims
- [Peer answering in the hybrid support system was fast where it occurred: 70.3% of peer-answered queries closed within one hour, against 1.9% of administrator-answered and 14.8% of script-closed queries](peer-answering-fast-70-percent-within-one-hour.md) — related
- [Corpus reuse in the deployed support system is concentrated on a single process step: three certificate/offer-letter entries account for 56.8% of 871 resolutions, with a Gini of 0.586 across entries](corpus-reuse-concentrated-single-process-step-gini-0-586.md) — related
