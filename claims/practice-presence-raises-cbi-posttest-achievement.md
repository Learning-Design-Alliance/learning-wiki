---
type: claim
title: "In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice"
description: "In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice"
id: practice-presence-raises-cbi-posttest-achievement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: martin-2003
    resource: "https://eric.ed.gov/?id=ED484984"
    title: "Martin, F., Klein, J., & Sullivan, H. (2003). Effects of Instructional Events in Computer-Based Instruction. https://eric.ed.gov/?id=ED484984"
    author: "Martin, F., Klein, J., & Sullivan, H."
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
<!-- deprecated title (2026-10-05, overstated its evidence): Including practice with feedback in computer-based instruction significantly raises posttest achievement -->

## Subclaims
`q3 i?` The four treatment versions that included practice scored significantly higher on the posttest than the two versions without practice. [→ Martin 2003](#martin-2003)
`q3 i?` The omnibus one-way ANOVA on posttest scores showed a significant difference among the six treatment groups. [→ Martin 2003](#martin-2003)

## Evidence

### Martin 2003

Martin, F., Klein, J., & Sullivan, H. (2003). Effects of Instructional Events in Computer-Based Instruction. https://eric.ed.gov/?id=ED484984

`q3 · i?` · `causal · r2`

Experiment with 256 undergraduate computer literacy students randomly assigned within pretest blocks to six lesson versions. The ANOVA yielded "F (5, 250) = 11.689, p <.01"; Scheffe tests showed the four practice-including groups (means above 17) significantly outperformed the two without practice (below 15).

> "A one -way ANOVA conducted on the po sttest data yielded a significant difference between the treatment groups on the posttest, F (5, 250) = 11.689, p <.01. Follow -up Scheffe tests revealed that each of the four groups with means scores above 17, as listed above and shown in the table, scored  significantly higher than the two groups identified above that scored below 15."

## Studies bearing on this claim

<!-- synthesis:start -->
*After a model, does practice with support and feedback produce better unaided performance than no practice or unguided practice?* This table gathers the studies behind this claim and the 22 narrower claims that bear on it: **31 distinct studies** (12 causal, 7 review, 7 theoretical, 3 qualitative, 1 quant-synthesis, 1 kind not coded), `q1`–`q4`, 1 of 31 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| Martin 2003 | q3 · causal · r2 | i? | this claim; [Individually removing objectives, examples, or review from a well-designed computer-based ](single-event-removal-no-achievement-effect.md) (qualifies); [Students notice the absence of practice and examples: attitude items about those events ar](students-notice-missing-practice-and-examples.md) (supports) |
| [Sweller & Cooper 1985](https://doi.org/10.1207/s1532690xci0201_3) | q3 · causal · r? | i? | [Worked examples reduce unnecessary search for novices.](worked-examples-reduce-novice-search.md) (supports); [Studying worked examples improves novices' algebra performance on problems with the same s](worked-examples-improve-math-performance.md) (qualifies) |
| [Pratt and Savoy-Levine 1998](<https://doi.org/10.1016/s0193-3973(99)80041-0>) | q3 · causal · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Chi et al. 2001](https://doi.org/10.1207/s15516709cog2504_1) | q2 · causal · r1 | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Swanson and Lussier 2001](https://doi.org/10.3102/00346543071002321) | q4 · quant-synthesis · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [van de Pol et al. 2010](https://doi.org/10.1007/s10648-010-9127-6) | q3 · review · r2 | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports); [Fading support promotes the transfer of responsibility from instructor to learner.](fading-support-promotes-transfer-of-responsibility.md) (supports) |
| [Wood et al. 1976](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x) | q3 · qualitative · r? | i? | [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) (supports) |
| [Yibo Meng 2026](https://doi.org/10.48550/arxiv.2606.07765) | q3 · causal · r2 | i3 | [In a randomised study with 40 CPR-naive lay adults in Tibet, 10 minutes of TibetCPR traini](tibetcpr-rhythm-stabilisation-exceeds-unguided-practice.md) (supports); [TibetCPR training produced depth-accuracy gains that substantially exceeded unguided pract](tibetcpr-depth-accuracy-gains-exceed-control.md) (supports) |
| [Karpicke 2017](https://doi.org/10.1016/b978-0-12-809324-5.21055-9) | q2 · review · r3 | i? | [Taking initial multiple-choice tests without feedback can lead students to later produce t](multiple-choice-lures-can-be-learned-as-false-knowledge.md) (supports) |
| [Bastani Hamsa 2025](https://doi.org/10.1073/pnas.2422633122) | q3 · causal · r3 | i? | [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performan](gpt-tutor-improves-practice-more-than-gpt-base.md) (qualifies) |
| Mutlu Cukurova 2026 | q2 · theoretical · r3 | i? | [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 a](gpt4-access-harms-learning-after-withdrawal.md) (qualifies) |
| Reshaping Undergraduate Computer Science Education in the Generative AI Era 2026 | q2 · qualitative · r1 | i? | [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 a](gpt4-access-harms-learning-after-withdrawal.md) (qualifies) |
| [Zemin Guo 2026](https://doi.org/10.1016/j.caeai.2026.100679) | q1 · review · r2 | i? | [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 a](gpt4-access-harms-learning-after-withdrawal.md) (qualifies) |
| [Khosravi 2026](https://doi.org/10.48550/arxiv.2605.04816) | q2 · theoretical · r3 | i? | [Reviews citing one randomised trial (Bastani et al. 2025) report that unrestricted GPT-4 a](gpt4-access-harms-learning-after-withdrawal.md) (qualifies) |
| [van Gog et al. 2011](https://doi.org/10.1016/j.cedpsych.2010.10.004) | q3 · causal · r? | i? | [Example-first conditions outperformed problem-first conditions on an immediate circuit tes](worked-example-problem-sequences.md) (supports) |
| [Pollock et al. 2002](<https://doi.org/10.1016/s0959-4752(01)00016-0>) | q3 · causal · r? | i? | [Part-task practice reduces cognitive load for absolute novices during initial skill acquis](part-task-practice-reduces-load-for-novices.md) (supports) |
| [Renkl et al. 2002](https://doi.org/10.1080/00220970209599510) | q3 · causal · r? | i? | [Fading support promotes the transfer of responsibility from instructor to learner.](fading-support-promotes-transfer-of-responsibility.md) (supports) |
| [Barbieri & Booth 2016](https://doi.org/10.1016/j.lindif.2016.04.001) | q2 · causal · r? | i? | [Studying worked examples improves novices' algebra performance on problems with the same s](worked-examples-improve-math-performance.md) (qualifies) |
| [Kalyuga et al. 2003](https://doi.org/10.1207/s15326985ep3801_4) | q2 / q3 · review · r? | i? | [Worked-example guidance becomes less effective as learner expertise increases.](worked-examples-less-effective-with-expertise.md) (qualifies); [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| [Renkl & Atkinson 2003](https://doi.org/10.1207/s15326985ep3801_3) | q3 · theoretical · r? | i? | [Worked-example guidance becomes less effective as learner expertise increases.](worked-examples-less-effective-with-expertise.md) (qualifies) |
| [Kalyuga et al. 1998](https://doi.org/10.1518/001872098779480587) | q3 · causal · r? | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| Obikwelu 2013 | q1 · theoretical · r2 | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| [Slava Kalyuga 2010](https://doi.org/10.1007/s11251-009-9102-0) | q2 · review · r2 | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| [Leonard Tetzlaff 2021](https://doi.org/10.1007/s10648-020-09570-w) | q2 | i? | [Instructional guidance that helps novices can become redundant or counterproductive as exp](expertise-reversal-effect.md) (qualifies) |
| [van Merriënboer et al. 2006](https://doi.org/10.1002/acp.1250) | q2 · theoretical · r? | i? | [A training-design argument, not tested by any study recorded here, holds that practising w](whole-task-performance-improves-transfer.md) (qualifies) |
| [Aydinbek C 2022](https://doi.org/10.5897/err2022.4230) | q2 · review · r2 | i? | [Practice of grammar rules improves only the practiced skill, showing skill specificity of ](skill-specificity-l2-grammar-practice.md) (qualifies); [Automatization of L2 skills requires extensive practice in a consistent environment, not r](automatization-requires-practice-consistent-environment.md) (qualifies) |
| [Robert M. DeKeyser 1997](https://doi.org/10.1017/s0272263197002040) | q3 · causal · r? | i? | [Practice of grammar rules improves only the practiced skill, showing skill specificity of ](skill-specificity-l2-grammar-practice.md) (qualifies) |
| [Yingli Wang 2008](https://doi.org/10.5539/elt.v1n1p83) | q2 · review · r2 | i? | [Task rehearsal improves fluency and complexity on the repeated task but does not transfer ](task-repetition-fluency-complexity-same-task-only.md) (qualifies) |
| [Robert DeKeyser 2010](https://doi.org/10.6018/ijes/2010/1/114021) | q1 · theoretical · r2 | i? | [Purely mechanical drills are of limited use because they do not train learners to conceptu](mechanical-drills-limited-use-meaning-form.md) (qualifies) |
| [Won Ik Cho 2026](https://doi.org/10.48550/arxiv.2605.24688) | q1 · theoretical · r3 | i? | [AI assistance that substitutes for learning activities may improve immediate performance w](ai-substitution-impedes-long-term-skill-development.md) (supports) |
| [Rana Abou Khamis 2026](https://doi.org/10.48550/arxiv.2607.28650) | q2 · qualitative · r2 | i? | [GenAI compresses traditional sysadmin expertise pathways by shortcutting hands-on practice](genai-compresses-sysadmin-expertise-pathways.md) (qualifies) |
<!-- synthesis:end -->

## Discussion

The one study recorded here varied which instructional events a computer-based lesson included; its entry describes practice being present or absent and says nothing about the feedback given during practice, so it cannot separate practice from feedback. The size of the difference is not established: the entry prints an F test and group means but no effect size.

## Related Claims

- [Media comparison studies produce uninterpretable "no significant difference" findings.](media-comparison-studies-produce-uninterpretable-results.md) — the general claim this finding bears on, with the studies behind it
- [AI-mediated feedback in hands-on exhibits improves learning and engagement](ai-mediated-feedback-in-hands-on-exhibits-improves-learning-and-engagement.md) — a narrower finding that bears on this claim
- [Treatment version significantly affects student attitudes, with the lean program most negative and no-practice next](cbi-version-affects-attitudes-lean-most-negative.md) — related
- Ninth graders using the computer as a translation tool (utilities group) outperformed a computation group on applications problems — related
- [Students notice the absence of practice and examples: attitude items about those events are rated lower when the events are missing](students-notice-missing-practice-and-examples.md) — related
- [Short chunking study outlines produce higher test performance than long chunking study outlines](short-cso-improves-test-performance.md) — related
- [Individually removing objectives, examples, or review from a well-designed computer-based lesson did not significantly reduce achievement](single-event-removal-no-achievement-effect.md) — related
- [The review reports that students receiving situated instruction outperformed a lecture-based control group on a causality posttest](situated-instruction-outperformed-abstract-control-causality.md) — related
- [Offloading work to AI costs learning: students given answers did well in practice but scored lower on an unassisted exam](gpt4-access-harms-learning-after-withdrawal.md) — related
