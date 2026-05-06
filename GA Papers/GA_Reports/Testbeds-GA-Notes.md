# Testbeds — GA Internal Notes

**Document Type:** Internal knowledge notes (content-heavy)  
**Audience:** Internal (research/implementation learning)  
**Last Updated:** February 12, 2026
**Classification:** Internal Knowledge Notes (Content-Heavy)  
**Reference Hub:** [NOTES-INDEX.md](NOTES-INDEX.md)  
**Canonical Tracker:** [../GA_Communications/md_files/Task-Tracker-Formal.md](../GA_Communications/md_files/Task-Tracker-Formal.md)

---

## Scope & Purpose

This file is intentionally dedicated to **testbeds work** so testbed learning is not mixed with dynamic-allocation notes or peer-facing communication summaries.

For live task status (owner/priority), use:
- [../GA_Communications/md_files/Task-Tracker-Formal.md](../GA_Communications/md_files/Task-Tracker-Formal.md)

For shared navigation, use:
- [../GA_Communications/md_files/NAVIGATION-INDEX.md](../GA_Communications/md_files/NAVIGATION-INDEX.md)

---

## Testbed Landscape (Integrated)

- **Paper 2:** MAB-based quantum routing with entanglement swapping focus.
- **Paper 7:** QBGP-style online path selection and routing dynamics.
- **Paper 12:** QuARC-style qubit allocation/fusion-centered evaluation.

Primary integration overview:
- [../../hybrid_variable_framework/docs/TESTBEDS_OVERVIEW.md](../../hybrid_variable_framework/docs/TESTBEDS_OVERVIEW.md)

Testbed docs are referenced from the shared `hybrid_variable_framework/docs` location.

---

## What We Learned from Testbed Integration

### 1) Parallel testbed support improves research credibility
Running multiple paper testbeds in one framework gives stronger cross-paper comparison and exposes hidden assumptions in single-paper narratives.

### 2) Unit-test-first workflow catches integration drift quickly
The Paper 7 / Paper 12 sanity-test pattern provides fast checks before expensive notebook runs and prevents “silent” parameter or format drift.

### 3) Parameter semantics must be explicit and versioned
Physics and reward assumptions can drift between experiments. Every testbed note should state active parameter assumptions and validation source date.

### 4) Validation logs are a gating layer, not optional reporting
Batch-level PASS status and data-quality checks are required before merging results into any narrative or tracker claim.

---

## Evidence Anchors Used for Testbed Learning

- [../../hybrid_variable_framework/docs/TESTBEDS_OVERVIEW.md](../../hybrid_variable_framework/docs/TESTBEDS_OVERVIEW.md)
- [../../hybrid_variable_framework/docs/testbeds/Paper7_vs_Paper12_Testing.md](../../hybrid_variable_framework/docs/testbeds/Paper7_vs_Paper12_Testing.md)
- [../../hybrid_variable_framework/docs/testbeds/PAPER12_TESTING_SUMMARY.md](../../hybrid_variable_framework/docs/testbeds/PAPER12_TESTING_SUMMARY.md)
- [../../hybrid_variable_framework/docs/validated_logs/validation_results.md](../../hybrid_variable_framework/docs/validated_logs/validation_results.md)
- [../GA_Communications/md_files/Task-Tracker-Formal.md](../GA_Communications/md_files/Task-Tracker-Formal.md)

---

## Internal Interpretation Notes

- Treat testbeds as complementary stress lenses, not interchangeable benchmarks.
- Scenario-dependent behavior means comparisons must always include scenario context.
- Distinguish clearly between:
  - historical snapshots,
  - current dataset-verified values,
  - in-progress rerun values not yet validated.

---

## Date + One-Line Work Log (Testbeds Track)

- **2025-12 (late):** Paper 2, 7, and 12 testbed integration moved into a unified evaluation direction.
- **2026-01-30:** Testbeds overview documented with integrated status across the three papers.
- **2026-02-11:** Active work prioritized around remaining testbed finalization and cross-testbed comparisons.
- **2026-02-12:** Dedicated internal testbeds notes file created to keep testbed knowledge separate from other notes.

---

## Next Internal Steps (Testbeds)

1. Maintain this file as the internal “what we learned” notebook for testbed behavior.
2. For each new testbed run batch, append one dated line with scenario + key takeaway.
3. Sync only finalized outcomes to shared tracker docs; keep exploratory details here.
4. Next external baseline/testbed to add: **Paper 8 (adaptive entanglement routing, DQN)** (`jallowkhan2025adaptive`). Rationale: repo available (lower integration friction) + adds an RL family complement to Papers 2/7/12. Paper 5 (`wang2025learning`) remains a strong candidate but code link is pending; NetSquid is deferred as a simulator/platform integration.
