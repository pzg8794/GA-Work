# Piter Garcia & Dan Krutz
## Research & Development Task Tracker (Canonical)
### August 2025 - February 2026

**Document Type:** Formal Task Tracker (Task-Oriented)  
**Period Covered:** August 11, 2025 - March 1, 2026  
**Last Updated:** March 2, 2026  
**Owner:** Piter Garcia (GA) / Daniel Krutz (Faculty Advisor)  
**Primary Source Sync:** consolidated communications records + meeting transcript updates

---

## OVERVIEW & STATUS SUMMARY

**Role of this document:** This is the **single source of truth** for live tasks, priorities, ownership, and status.

| Metric | Value |
|---|---|
| **Total Tasks Logged** | 35 |
| **Completed** | 28 |
| **In Progress** | 5 |
| **Blocked/Waiting External** | 1 |
| **Scheduled** | 1 |
| **Completion Rate (Completed / Total)** | 80.0% |
| **Current Project Phase** | Paper Finalization & Publication Pipeline |

### Status Definitions
- ✅ **Completed** = closed and delivered
- 🔄 **In Progress** = actively being worked
- 🚧 **Blocked/Waiting External** = progress depends on external response/input
- 📅 **Scheduled** = upcoming date/time agreed (future checkpoint)
- ❌ **Not Answered (Timed-Out / N.A.)** = historical item no longer active

---

## CURRENT OPEN WORK (PRIORITIZED)

> This section is the single source of truth for active priorities.

### Priority 1 — Explicit Feb 11 Meeting Actions
1. **T-2026-007** — Address paper comments and compare manuscript claims against cited papers (in progress)
2. **T-2026-009** — Send Dan the updates/list as discussed in meeting follow-up (in progress)
3. **T-2026-010** — Next meeting checkpoint (Tue Feb 17, 11:35) (scheduled)

### Priority 2 — Continuing Paper Work
4. **T-2025-011** — Manuscript drafting + revisions (conference/journal paper) (in progress)
5. **T-2025-015** — Related works synthesis + structure alignment (in progress)

### Priority 3 — Ongoing Coordination / Admin
6. **T-2026-005** — Follow up and integrate Professor Travis feedback (blocked/waiting external)

### Priority 4 — External Testbed Expansion (Next Baseline)
7. **T-2026-012** — Integrate Paper 8 adaptive entanglement routing (DQN) as the next external baseline/testbed (in progress)

---

## TASK → DOCUMENTATION REFERENCE MAP

Use this section to jump from active tasks to the most relevant implementation/validation docs.

| Task ID | Documentation References | Why These Docs |
|---|---|---|
| T-2026-005 | [../../hybrid_variable_framework/docs/paper12/PAPER12_DOCUMENTATION_UPDATE_COMPLETE.md](../../hybrid_variable_framework/docs/paper12/PAPER12_DOCUMENTATION_UPDATE_COMPLETE.md) | Reference context to apply only when external feedback is actually available |
| T-2025-011 | [../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md](../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md), [../../hybrid_variable_framework/docs/INDEX.md](../../hybrid_variable_framework/docs/INDEX.md), [../../hybrid_variable_framework/docs/updates/UPDATE_SUMMARY.md](../../hybrid_variable_framework/docs/updates/UPDATE_SUMMARY.md), [../../hybrid_variable_framework/docs/guides/STATE_ANALYSIS_EVALUATOR_CONTRACT.md](../../hybrid_variable_framework/docs/guides/STATE_ANALYSIS_EVALUATOR_CONTRACT.md) | Paper-specific checklist + pointers into the documentation set supporting manuscript edits; include evaluator-state contract when validated logs/master datasets are part of the workflow |
| T-2025-015 | [../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md](../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md), [../../hybrid_variable_framework/docs/INDEX.md](../../hybrid_variable_framework/docs/INDEX.md) | Paper-specific checklist + starting point for related-works alignment |
| T-2026-007 | [../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md](../../QuantumFaultTolerant/tracking/PAPER-CHANGES-TRACKER.md), [../2026-02-11 10.25.40 Daniel Krutz's Personal Meeting Room/meeting_saved_closed_caption.txt](../2026-02-11%2010.25.40%20Daniel%20Krutz%27s%20Personal%20Meeting%20Room/meeting_saved_closed_caption.txt) | Paper change checklist + direct meeting action: address comments and compare against cited work |
| T-2026-009 | [B-Rated-Venues-Reference.md](B-Rated-Venues-Reference.md) | Source doc for venue update email (email itself not archived here) |
| T-2026-012 | [../QuantumFaultTolerant-Notes.md](../QuantumFaultTolerant-Notes.md), [../emails/Rochester Institute of Technology Mail - Meeting assets for Piter Garcia (RIT Student)'s Zoom Meeting are ready!5.pdf](../emails/Rochester%20Institute%20of%20Technology%20Mail%20-%20Meeting%20assets%20for%20Piter%20Garcia%20%28RIT%20Student%29%27s%20Zoom%20Meeting%20are%20ready%215.pdf), [../../quantum_project_hub/notebooks/H-MABs_Eval-T_XQubit_Alloc_XQRuns.ipynb](../../quantum_project_hub/notebooks/H-MABs_Eval-T_XQubit_Alloc_XQRuns.ipynb), [../../quantum_project_hub/daqr/core/topology_generator.py](../../quantum_project_hub/daqr/core/topology_generator.py), [../../quantum_project_hub/daqr/core/quantum_physics.py](../../quantum_project_hub/daqr/core/quantum_physics.py), [../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/daqr/core/topology_generator.py](../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/daqr/core/topology_generator.py), [../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/daqr/core/quantum_physics.py](../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/daqr/core/quantum_physics.py), [../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper8-PaperRunConfig.ipynb](../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper8-PaperRunConfig.ipynb), [../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper8-StandardizedRunConfig.ipynb](../../hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_Eval-Testbed-Paper8-StandardizedRunConfig.ipynb), [../../hybrid_variable_framework/docs/guides/STATE_ANALYSIS_EVALUATOR_CONTRACT.md](../../hybrid_variable_framework/docs/guides/STATE_ANALYSIS_EVALUATOR_CONTRACT.md) | Candidate comparison + decision record (Paper 8 chosen); Paper8 components mirrored into core modules (topology + physics) so the testbed stays reusable/mix-and-match; paper-config notebook comes first, standardized sweep comes after; include evaluator-state contract because validated-log extraction is part of the regression path |

---

## ACTIVE TASK VERIFICATION LOG

Use this as a lightweight audit line so active items stay synchronized with source docs.

| Task ID | Last Verified | Verified Against |
|---|---|---|
| T-2026-005 | 2026-02-12 | `hybrid_variable_framework/docs/paper12/PAPER12_DOCUMENTATION_UPDATE_COMPLETE.md` |
| T-2025-011 | 2026-02-14 | `hybrid_variable_framework/docs/INDEX.md`, `hybrid_variable_framework/docs/updates/UPDATE_SUMMARY.md` |
| T-2025-015 | 2026-02-14 | `hybrid_variable_framework/docs/INDEX.md` |
| T-2026-007 | 2026-02-12 | `GA_Communications/2026-02-11 10.25.40 Daniel Krutz's Personal Meeting Room/meeting_saved_closed_caption.txt` |
| T-2026-009 | 2026-02-14 | `B-Rated-Venues-Reference.md` |
| T-2026-010 | 2026-02-12 | `GA_Communications/2026-02-11 10.25.40 Daniel Krutz's Personal Meeting Room/meeting_saved_closed_caption.txt` |
| T-2026-012 | 2026-03-02 | `quantum_project_hub/notebooks/H-MABs_Eval-T_XQubit_Alloc_XQRuns.ipynb`, `quantum_project_hub/daqr/core/topology_generator.py`, `quantum_project_hub/daqr/core/quantum_physics.py`, `GA_Communications/QuantumFaultTolerant-Notes.md` |

---

## PRIMARY EVIDENCE SOURCES (FOR TASK VALIDATION)

Technical docs referenced below use the shared `hybrid_variable_framework/docs` location.

- Meeting decisions (latest): [../2026-02-11 10.25.40 Daniel Krutz's Personal Meeting Room/meeting_saved_closed_caption.txt](../2026-02-11%2010.25.40%20Daniel%20Krutz%27s%20Personal%20Meeting%20Room/meeting_saved_closed_caption.txt)
- Multi-testbed docs index: [../../hybrid_variable_framework/docs/INDEX.md](../../hybrid_variable_framework/docs/INDEX.md)
- Integration status summary: [../../hybrid_variable_framework/docs/INTEGRATION_COMPLETE.md](../../hybrid_variable_framework/docs/INTEGRATION_COMPLETE.md)
- Update chronology: [../../hybrid_variable_framework/docs/updates/UPDATE_SUMMARY.md](../../hybrid_variable_framework/docs/updates/UPDATE_SUMMARY.md)
- Paper12 correction & baseline validation: [../../hybrid_variable_framework/docs/paper12/PAPER12_DOCUMENTATION_UPDATE_COMPLETE.md](../../hybrid_variable_framework/docs/paper12/PAPER12_DOCUMENTATION_UPDATE_COMPLETE.md)
- Validation batches: [../../hybrid_variable_framework/docs/validated_logs/validation_results.md](../../hybrid_variable_framework/docs/validated_logs/validation_results.md)

---

## TASK LEDGER (NORMALIZED)

> Full task detail is intentionally maintained here to avoid duplication in the communications summary.

| Task ID | Assigned Date / Window | Assigned By | Assigned To | Status | Summary | Source |
|---|---|---|---|---|---|---|
| T-2025-001 | 2025-08-11 | Daniel Krutz | Piter Garcia | ✅ Completed | GA position initiation and orientation | Communications logs |
| T-2025-002 | 2025-08-20 → 2025-08-25 | Daniel Krutz | Piter Garcia | ✅ Completed | Jie Xu paper review + AGNB method analysis | Communications logs |
| T-2025-003 | 2025-09-03 → 2025-09-08 | Piter Garcia | Piter Garcia / Devroop Kar | ✅ Completed | iCMAB communication channel setup | Communications logs |
| T-2025-004 | 2025-09-15 | Devroop Kar | Piter Garcia | ✅ Completed | iCMAB GitHub access/setup | Communications logs |
| T-2025-005 | 2025-09-18 → 2025-09-22 | Piter Garcia | Piter Garcia + Dan Krutz | ✅ Completed | Environment + health scheduling coordination | Communications logs |
| T-2025-006 | 2025-09-26 | Piter Garcia | Piter Garcia + Dan Krutz | ✅ Completed | Meeting confirmation process with calendar invites | Communications logs |
| T-2025-007 | 2025-10-03 → 2025-10-04 | Research Plan | Piter Garcia | ✅ Completed | CMAB baseline testing phase 1 | Communications logs |
| T-2025-008 | 2025-10-03 → 2025-10-16 | Research Plan | Piter Garcia | ✅ Completed | iCMAB algorithm evaluation phase 2 | Communications logs |
| T-2025-009 | 2025-10-10 → 2025-10-21 | Research Requirements | Piter Garcia | ✅ Completed | Production-ready framework architecture | Communications logs |
| T-2025-010 | 2025-10-21 | Framework Validation | Piter Garcia | ✅ Completed | Dynamic qubit allocation strategy comparison | Communications logs |
| T-2025-011 | 2025-10-15 → Ongoing | Daniel Krutz | Piter Garcia | 🔄 In Progress | Manuscript drafting + revisions (conference/journal paper) | Communications logs |
| T-2025-012 | 2025-10-16 → 2025-10-21 | Circumstance | Piter Garcia | ✅ Completed | Family emergency management with work continuity | Communications logs |
| T-2025-013 | 2025-10-28 → 2025-11-03 | Daniel Krutz | Piter Garcia | ✅ Completed | Image modification for stochastic framing | Communications logs |
| T-2025-014 | 2025-11-12 | Daniel Krutz | Piter Garcia | ✅ Completed | EXA-GP direction assessment and approval | Communications logs |
| T-2025-015 | 2025-11-15 → Ongoing | Daniel Krutz | Piter Garcia | 🔄 In Progress | Related works synthesis + structure alignment | Communications logs |
| T-2025-016 | 2025-11-25 | Daniel Krutz (implicit) | Piter Garcia | ✅ Completed | Top-5 paper identification and strategic mapping | Communications logs |
| T-2025-017 | 2025-11-25 → 2025-12-01 | Daniel Krutz | Piter Garcia | ✅ Completed | Concise problem/solution statements | Communications logs |
| T-2025-018 | 2025-11-17 → 2025-11-18 | Devroop Kar | Piter Garcia | ✅ Completed | Progress sync and collaboration checkpoint | Communications logs |
| T-2025-019 | 2025-12-05 | Devroop Kar (implied) | Piter Garcia | ✅ Completed | Documentation suite (Colab/Local/GCP) | Communications logs |
| T-2025-020 | 2025-12-10 → 2026-02-14 | Daniel Krutz | Piter Garcia | ✅ Completed | Literature comparison tests completed; per-paper results recorded (confirmed 2026-02-14) | Communications logs |
| T-2025-021 | 2025-12-20 → 2025-12-22 | Daniel Krutz | Piter Garcia | ✅ Completed | Evaluation validation corpus + figures | Communications logs |
| T-2025-022 | 2025-12-10 → 2026-02-14 | Research Plan | Piter Garcia | ✅ Completed | Testbed runs finalized; result batches validated (confirmed 2026-02-14) | Communications logs |
| T-2025-023 | 2025-12-20 → 2026-02-14 | Daniel Krutz | Piter Garcia | ✅ Completed | IEEE baseline comparison table built for manuscript integration (confirmed 2026-02-14) | Communications logs |
| T-2026-001 | 2025-12-31 → 2026-01-07 | Circumstance | Piter Garcia | ✅ Completed | Recovery and return-to-work status | Communications logs |
| T-2026-002 | 2026-01-07 → 2026-02-14 | Self-assigned | Piter Garcia | ✅ Completed | GA schedule/work-hours structuring (no longer tracked as active task; confirmed 2026-02-14) | Communications logs |
| T-2026-003 | 2026-01-07 | Daniel Krutz | Piter Garcia | ✅ Completed | Overleaf source clarification: one primary source project + Travis review view workflow | Communications logs |
| T-2026-004 | 2026-01-07 | Piter Garcia | Team | ✅ Completed | Team alignment meeting scheduling action executed (historical) | Communications logs |
| T-2026-005 | 2026-01-07 → Ongoing | Daniel Krutz (implicit) | Piter Garcia | 🚧 Blocked/Waiting External | Follow-up for Travis feedback | Communications logs |
| T-2026-006 | 2026-01-07 → 2026-02-14 | Piter Garcia | Piter Garcia | ✅ Completed | Communication tracking maintenance completed via canonical md docs (confirmed 2026-02-14) | Communications logs |
| T-2026-007 | 2026-02-11 10:10–10:12 | Daniel Krutz | Piter Garcia | 🔄 In Progress | Address paper comments and compare against cited papers in the manuscript | Feb 11 transcript |
| T-2026-008 | 2026-02-11 10:11–10:13 | Daniel Krutz | Piter Garcia | ✅ Completed | Build shortlist of 2-3 B-or-better venues with deadlines in next 1-2 months | Feb 11 transcript |
| T-2026-009 | 2026-02-11 10:22–10:25 | Piter Garcia (commitment) | Piter Garcia | 🔄 In Progress | Send follow-up note with updates/list to Dan as agreed | Feb 11 transcript |
| T-2026-010 | 2026-02-11 10:22–10:24 | Daniel Krutz + Piter Garcia | Piter Garcia + Dan Krutz | 📅 Scheduled | Next meeting set for Tuesday Feb 17 at 11:35 | Feb 11 transcript |
| T-2026-011 | 2026-02-11 10:13–10:18 | Daniel Krutz | Piter Garcia | ✅ Completed | Contacted Devroop and Shiraja; provided high-level feedback back to Dan (confirmed 2026-02-14) | Feb 11 transcript |
| T-2026-012 | 2026-03-01 → Ongoing | Devroop Kar (Dec 23 comms) + Research Plan | Piter Garcia | 🔄 In Progress | Add the next external baseline/testbed: Paper 8 adaptive entanglement routing (RL/Q-learning). Implementation constraint: follow existing testbed flow (Paper2/7/12) by adding components into core modules (no standalone per-paper “testbed object” file), then validate via small dry-run tools | Zoom meeting assets summary (Dec 23, 2025) + internal ranking notes |


---

## TIMED-OUT / N.A. ADMIN ITEMS (HISTORICAL)

These are retained for audit trail only and are **not active blockers**.

| Item | Original Date | Status | Note |
|---|---|---|---|
| Hour Logging continuation question | 2025-12-31 | ❌ Not Answered (Timed-Out / N.A.) | Time-sensitive semester transition item; no in-thread answer captured |
| Spring GA continuation confirmation | 2025-12-31 | ❌ Not Answered (Timed-Out / N.A.) | Historical unresolved item in-thread; no longer tracked as active queue item |

---

## OVERLEAF WORKFLOW (CLARIFIED)

- **Primary source project (active):** (remote Overleaf link removed)
- **Travis review view (feedback-oriented):** (remote Overleaf link removed)
- This is treated as **one active source workflow**, not two independent active project streams.

---

## METRICS NOTE (FOR RESULTS DISCUSSIONS)

Quantified performance values previously logged in communication threads are **historical snapshots** (primarily Dec 25-31, 2025). They may have changed with additional experiments and should be refreshed before final reporting.

### CURRENT DATASET-VERIFIED SNAPSHOT (AS OF 2026-02-12)

Method: values below are computed from master datasets in `Validated_Logs`, grouped by scenario (`NONE` and `STOCHASTIC`) and model, excluding Oracle rows.

| Paper | Scenario NONE (No Attack) - Top Model | Scenario STOCHASTIC - Top Model | EXPNeuralUCB Retention (Stochastic / None) |
|---|---|---|---|
| Paper 2 | iCPursuitNeuralUCB: reward 2973.44, eff 90.92% | GNeuralUCB: reward 2751.70, eff 86.18% | 92.3% (2667.50 / 2891.35) |
| Paper 7 | iCPursuitNeuralUCB: reward 1350.00, eff 100.00% | iCPursuitNeuralUCB: reward 1268.10, eff 93.97% | 93.2% (1112.05 / 1192.93) |
| Paper 12 | iCPursuitNeuralUCB: reward 1245.21, eff 55.98% | iCPursuitNeuralUCB: reward 1156.60, eff 51.99% | 92.6% (1110.29 / 1199.62) |

### Paper 7 follow-up validation

- Verify upstream Paper 7 traffic/event distributions exercised in our integration:
  - `Poisson`
  - `Exponential`
  - `Uniform`
  - `Pareto`
  - `Log-Normal`
- Confirm whether current Paper 7 master dataset and saved evaluator states were generated under all supported upstream distributions or only a subset.
- Keep this separate from the current Paper 7/Paper 12 resume-capacity audit.
- Run a small cross-allocator verification pass against the Paper 7 master dataset:
  - same model set as the master dataset
  - one threat scenario only
  - compare fresh results vs `Validated_Logs/Master_Dataset_paper7_50_50_5_ST.csv`
  - use that comparison to decide between state repair vs full Paper 7 / Paper 12 reruns
  - status update (2026-03-07): completed as a 3-experiment stochastic verification on the corrected 4-path branch; results were structurally different but numerically close, so rerun vs repair remains open
- Make the Google Drive `GA-Work` replica usable as a direct filesystem fallback for state loading:
  - detect the mirrored Drive workspace automatically,
  - read missing state files from the Drive mirror before invoking Drive API recovery,
  - keep shared-drive cleanup opt-in only (`DAQR_RESET_SHARED_DRIVE_STATE_CACHE=1`),
  - use this as the base for multi-PC and low-local-disk workflows.

---

## MAINTENANCE RULES

1. Add/update tasks only from dated communications or meeting records.
2. Keep status values within normalized set above.
3. Move old unresolved, time-sensitive items to **Timed-Out / N.A.**
4. Reorder **Current Open Work** after each major sync or meeting.

---

**Document Status:** Active Canonical Task Tracker  
**Next Review Checkpoint:** Post Feb 17 meeting updates
