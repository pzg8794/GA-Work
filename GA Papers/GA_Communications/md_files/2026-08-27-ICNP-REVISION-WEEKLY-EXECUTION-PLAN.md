# ICNP Post-Review Revision — 10-Hour Weekly GA Execution Plan

**Created:** August 27, 2026  
**Owner:** Piter Garcia (Graduate Assistant)  
**Faculty lead:** Daniel Krutz  
**Primary working repository:** `pzg8794/GA-Work`  
**Active manuscript submodule:** `GA Papers/QuantumFaultTolerant` -> `pzg8794/QuantumFaultTolerant`  
**Strategic source of truth:** `pzg8794/RESEARCH`

---

## 1. Why This Plan Exists

The GA workspace contains the implementation, validated data, communication history, and the active quantum-paper submodule. However, several current strategic decisions about the ICNP 2026 reviews were documented in the separate `RESEARCH` repository after the GA task tracker was last comprehensively updated.

This plan reconnects those two workspaces so the local AI does **not** restart from the older March 2026 GA state or invent a new revision strategy.

The current paper-revision strategy is already documented. The job now is to:

1. synchronize `GA-Work` with the decisions documented in `RESEARCH`;
2. reconcile those decisions against the current active manuscript state in `QuantumFaultTolerant`;
3. work the remaining reviewer-feedback gaps in a controlled order;
4. spend and document **10 hours of GA work each week**;
5. communicate concrete weekly outputs to Dan.

---

## 2. Required Source Order for the Local AI

Before editing the paper, running experiments, or creating a new task plan, the local AI must read the following in order.

### A. Strategic decisions — `RESEARCH`

1. **ICNP review classification and revision roadmap**  
   `https://github.com/pzg8794/RESEARCH/blob/main/RESEARCH/2026-08-04-icnp-review-classification-and-revision-roadmap.md`

2. **DSCI 602 / quantum-paper consolidation advisor draft**  
   `https://github.com/pzg8794/RESEARCH/blob/main/ADMIN/2026-08-04-dsci602-quantum-paper-consolidation-advisor-draft.md`

3. **RESEARCH master index**, when broader project relationships or newer planning artifacts need to be resolved  
   `https://github.com/pzg8794/RESEARCH/blob/main/MASTER_RESEARCH_INDEX.md`

### B. Current manuscript implementation/status — `QuantumFaultTolerant`

4. `ICNP_VENUE_PREP/HIGH_PRIORITY_REVIEW_BACKLOG.md`
5. `ICNP_VENUE_PREP/ACTIVE_FEEDBACK_RESOLUTION_LOG.md`
6. `ICNP_VENUE_PREP/ICNP_DRAFT_AUDIT_TODO.md`
7. `ICNP_2026_venue_draft.tex`
8. relevant staging/source files referenced by the active draft

### C. GA implementation/evidence — `GA-Work`

9. `GA Papers/GA_Communications/md_files/Task-Tracker-Formal.md` for historical/current task IDs and prior commitments
10. `GA Papers/GA_Communications/QuantumFaultTolerant-Notes.md` for historical research notes
11. `Validated_Logs/` and documented master datasets for actual result values
12. framework/testbed submodules for code/configuration evidence

### Source-precedence rule

If sources disagree:

- **Strategic post-ICNP decisions:** the August 2026 `RESEARCH` roadmap wins over stale pre-review task wording.
- **What has actually been implemented in the manuscript:** current `QuantumFaultTolerant` source/logs win.
- **Actual performance values:** validated datasets/logs win over prose summaries.
- **Advisor/reviewer instructions:** direct documented feedback wins over inferred intent.

Do not duplicate entire RESEARCH documents into GA-Work. Link to them and record only the operational consequences needed for GA execution.

---

## 3. Locked Revision Strategy

The ICNP reviews are handled **A + C first, then B as a risk audit**.

### Reviewer A — accepted core

Preserve and foreground:

- matched policy–allocator–capacity evaluation;
- cross-testbed evidence;
- capacity-paradox result;
- controlled evaluation methodology as the primary contribution.

### Reviewer C — primary conversion checklist

Prioritize:

- contribution positioning and narrative clarity;
- end-to-end decision-loop algorithm/pseudocode;
- complete context and hyperparameter specification;
- allocator-policy interface and execution order;
- threat-to-physics mapping;
- claim calibration;
- medium-scale topology evidence;
- diagnosis of the 100-node efficiency compression.

### Reviewer B — secondary risk audit

After A and C are addressed, map B's concerns onto completed artifacts and identify only the genuinely unresolved B-only risks.

Do **not** rebuild the paper around Reviewer B before completing the A+C plan.

---

## 4. Non-Negotiable First Step: Reconciliation Before Editing

At the beginning of the restart, create or update a working matrix with these columns:

| Reviewer request / roadmap item | Planned response | Current manuscript status | Evidence/file | Gap remaining | Next action | Hours used |
|---|---|---|---|---|---|---:|

Every planned edit or experiment must originate from an unresolved row in this matrix.

If an item is already implemented, mark it complete and move on. Do not redo it because it appears in an older checklist.

---

## 5. Weekly GA Time Contract

**Required effort: 10 hours per week.**

The ten hours are measured by actual research work and artifacts, not by keeping a timer running while blocked.

Default weekly allocation:

| Work category | Weekly target |
|---|---:|
| Technical manuscript / algorithm / experiment work | 7.0 h |
| Validation, evidence tracing, reproducibility, build/PDF checks | 2.0 h |
| Documentation + weekly update to Dan | 1.0 h |
| **Total** | **10.0 h** |

The distribution can change when experiments dominate, but the weekly total remains 10 hours and the outputs must be documented.

### Weekly completion rule

At the end of every week, record:

- hours worked;
- artifacts changed/created;
- reviewer items completed;
- evidence/validation performed;
- blockers requiring Dan/Travis/coauthor input;
- next week's expected deliverables.

Avoid vague updates such as "worked on paper." Report concrete outputs.

---

## 6. Restart Session — August 27, 2026

The user intends to restart work in approximately 10 hours from the time this plan was created. Because this conversation occurred shortly after midnight, the practical restart is **Thursday, August 27, 2026**, not August 28.

### First 10-hour weekly block

The first week is primarily **Phase 0 + Phase 1 reconciliation and execution**.

#### Block 1 — Repository and review-state reconciliation — 2.0 h

- pull/update `RESEARCH`, `GA-Work`, and the `QuantumFaultTolerant` submodule;
- read the August 4 RESEARCH roadmap;
- compare it against the current active feedback log/backlog and manuscript;
- build the reviewer-request -> current-status matrix;
- identify which roadmap items are already complete and which are genuinely open.

**Deliverable:** one current-state feedback matrix with no unresolved ambiguity about duplicate/stale tasks.

#### Block 2 — Accepted-core / contribution pass — 2.0 h

- verify the abstract, introduction, contribution bullets, and conclusion consistently frame the primary contribution as the controlled threat-aware evaluation methodology;
- preserve the cross-testbed evidence and capacity-paradox result;
- make only evidence-supported edits;
- do not reopen already-completed sections unless reconciliation shows a current gap.

**Deliverable:** synchronized two-sentence contribution statement plus a list/diff of any necessary manuscript changes.

#### Block 3 — Decision-loop algorithm + interface check — 2.0 h

- determine whether the current manuscript already contains a complete end-to-end decision loop;
- if incomplete, produce/repair pseudocode covering context construction, route/path selection, qubit allocation, feedback, replay, and policy update;
- verify allocator-policy execution order.

**Deliverable:** reviewer-traceable algorithm/interface artifact or a documented finding that the existing artifact already satisfies the request.

#### Block 4 — Context + hyperparameter reproducibility inventory — 2.0 h

- enumerate context features, dimensions, normalization, missing-value behavior, update/training cadence, policy settings, allocator settings, replay semantics, and major hyperparameters;
- trace every value to code/config/log sources rather than memory.

**Deliverable:** complete or substantially completed context/configuration inventory with source pointers.

#### Block 5 — Validation + weekly report — 2.0 h

- compile/review the active paper if changes were made;
- check references, figure/table placement, warnings, and claim/evidence consistency for the changed scope;
- update the feedback matrix;
- write the weekly Dan update with completed work, blockers, and next week's target.

**Deliverable:** Week 1 GA report and Dan-ready status summary.

### Reallocation rule

If reconciliation shows that one of Blocks 2-4 is already fully satisfied, immediately reassign that time to the next open A+C item. Do not spend GA hours recreating existing work.

---

## 7. Expected Weekly Progression After Week 1

The weekly sequence is a planning baseline, not a promise to force incomplete science into a calendar slot. If a task requires more evidence, carry it forward and report the reason.

### Week 1 — Reconcile + close lowest-cost A/C gaps

Expected outputs:

- authoritative feedback/status matrix;
- contribution statement aligned across paper sections;
- joint decision-loop algorithm/interface status resolved;
- context/hyperparameter inventory materially complete;
- Week 1 report to Dan.

### Week 2 — Finish reproducibility/interface layer

Expected outputs:

- all remaining non-scale Reviewer C interface/reproducibility items closed;
- allocator-policy contract finalized;
- context/configuration tables ready for the manuscript/appendix;
- paper build/visual validation;
- explicit list of items requiring quantum-physics/coauthor validation.

### Week 3 — Threat grounding and claim calibration

Expected outputs:

- threat-regime -> plausible quantum failure/adversary mapping;
- literature/source support for each physical analogue;
- explicit distinction between physical model and controlled stress test;
- calibrated deployment/realism claims;
- questions for Dan/Travis/quantum collaborators where physical interpretation requires confirmation.

### Week 4 — Scale experiment design and readiness

Expected outputs:

- reproducible 15-20 node / >=10 candidate-path experiment specification;
- baseline/control selection;
- metrics and stopping criteria;
- compute/configuration readiness check;
- 100-node diagnostic ablation plan.

### Week 5+ — Scale execution, diagnosis, and B risk audit

Expected outputs as evidence becomes available:

- medium-scale experiment runs and validated plots/tables;
- targeted diagnosis of the ~44.1% 100-node efficiency result;
- documented transfer/non-transfer across scales;
- Reviewer B residual-risk matrix;
- revised manuscript claims tied to the new evidence.

---

## 8. What Not To Do

- Do not invent a new review strategy before reading the RESEARCH roadmap.
- Do not treat the old March 2026 GA task tracker as sufficient for post-ICNP decisions.
- Do not rerun expensive experiments before reconciling what the reviewers actually requested and what is already complete.
- Do not delete validated evidence simply to simplify the narrative; relocate/compress with traceability.
- Do not overstate physical realism; label controlled stress tests honestly.
- Do not conflate the existing GA manuscript contribution with the new DSCI601/602 fairness extension.
- Do not spend GA hours on clinical fairness work unless Dan explicitly shifts the GA scope there.

---

## 9. Weekly Update Template for Dan

Use this structure each week:

**GA hours:** X / 10

**Completed this week**
- concrete artifact / reviewer item
- concrete artifact / reviewer item
- validation performed

**What changed in the manuscript/framework**
- concise technical summary

**Open/blocking questions**
- only items requiring advisor/coauthor input

**Next week's 10-hour target**
- 2-4 concrete deliverables tied to the revision roadmap

---

## 10. Current Definition of Done

The ICNP-feedback revision phase is ready for retargeting/submission review when:

1. Reviewer A's accepted core is preserved and clearly visible;
2. all non-scale Reviewer C reproducibility/interface requests are resolved;
3. threat regimes have defensible mappings or explicit stress-test boundaries;
4. claims are calibrated to evidence;
5. medium-scale evidence is reproducible;
6. the 100-node result is explained or bounded as a documented limitation;
7. Reviewer B has been fully audited for residual issues;
8. the manuscript passes build, visual, blind-review/metadata, and venue-specific final checks;
9. Dan/coauthors approve the revision and target venue.

---

## 11. Venue Note

The technical A+C-first strategy remains current. The **venue/deadline subsection of the August 4 RESEARCH roadmap must be refreshed before submission decisions**, because the August 15 and August 20 options referenced there have passed as of August 27, 2026.

Do not change technical priorities merely because an old venue deadline expired.
