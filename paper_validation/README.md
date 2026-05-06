# Paper validation snapshots

CRITICAL / HIGH PRIORITY NOTE:

- The validated master currently has a provenance gap for RQ3b under $T$ anchoring at 6K with Default (=Fixed): the full $s{=}1.5$ grid is missing (including in the 3-run view). RQ3b is therefore reported using $T_b$ anchoring (3-run suite) until the master is repaired.

## Status dashboard (Pending vs Solved)

This dashboard is the human-readable companion to the notebook’s audit summaries.

- ✅ **Solved:** RQ3b is now reported under the source-backed $T_b$ / 6K / Default (=Fixed) / runs=3 branch, with an exported proof bundle (see below).
- 🔴 **Pending:** RQ3b under $T$ anchoring at 6K / Default (=Fixed) remains blocked by missing master rows for the full $s{=}1.5$ grid.

- ✅ **Solved (paper alignment + evidence):** RQ3c `tab:rq3c_allocators` is aligned in the notebook (`RQ3C_PAPER` matches the printed values) and a proof snapshot was exported for the approved branch: `paper_validation/snapshots/20260315_001835/`.

- ✅ **Solved (paper alignment):** RQ1 `tab:rq1masterstochastic` (`TABLE V`) high-priority mismatches were patched in `GA Papers/QuantumFaultTolerant/main.tex` to match the notebook’s approved “Before (Expected) vs After (Actual)” audit output (GNeuralUCB 3-run, EXPNeuralUCB 5-run, iCPursuit 3/5-run).

DONE (RQ3b Tb snapshot + manuscript update):

- Exported proof snapshot for RQ3b using $T_b$ anchoring at 6K with Default (=Fixed), 3-run suite (experiments 1--3), and updated the manuscript RQ3b table/caption/text to match the pandas-derived values: `paper_validation/snapshots/20260314_224936/`.

This folder holds reproducible snapshot exports from the verification notebook:

- Notebook: `hybrid_variable_framework/Dynamic_Routing_Eval_Framework/notebooks/H-MABs_MasterDataset_VerificationHub.ipynb`
- Snapshots: `paper_validation/snapshots/<timestamp>/`

Each snapshot directory is designed to be “evidence you can diff”:

- `audit_summary_counts.csv` — notebook-wide count of High/Medium/Low/None by audit label
- `audit__<label>.csv` — full audit table per label (includes **Expected vs Actual** and deltas)
- `audit__<label>__HIGH.csv` — High-priority subset per label (if any)
- `all_high_discrepancies.csv` — combined High rows across the notebook
- `audit_rollup_deltas.csv` — per-audit numeric rollup (counts + max/mean absolute delta)
- `filtered__*.csv` — exported provenance/branch DataFrames used to generate specific audits (guarded to avoid exporting huge master frames)
- `data__*.csv` — **raw row snapshots** from the master dataset(s) for specific evaluation slices (proves the slice exists and shows the underlying rows)
- `data_snapshot_manifest.csv` — row counts + key uniques per `data__*.csv` snapshot (quick existence check)
- `agg_used__*.csv` — **every pandas table used in the notebook** (derived/aggregation/report tables) exported directly from the notebook runtime
- `agg_used_snapshot_manifest.csv` — shape + column + dtype summaries for `agg_used__*.csv`
- `proof_snapshot_excluded.csv` — explicit list of pandas objects that were *not* exported (with a reason), to keep the bundle auditable
- `proof_snapshot_metadata.json` — timestamp + Python/pandas version + notebook path + export counts
- `agg__*.csv` — aggregations computed *from the corresponding raw slice* (groupby means/std/counts used as validation inputs)
- `agg__*__PIVOT_MEAN.csv` — pivoted mean table (e.g., scenario columns) derived from the slice
- `agg__*__PIVOT_COUNT.csv` — pivoted counts table derived from the slice
- `agg__*__MISSING_COMBOS.csv` — optional list of missing model/scale/scenario combos for that slice
- `agg_snapshot_manifest.csv` — aggregation row counts + missing-combo counts per slice

Notes on aggregation exports:

- `agg_used__*.csv` is “what the notebook actually used” (captured by walking the notebook globals after execution).
- `agg__*.csv` is “what you can recompute from exported raw slices” (derived mechanically from the `data__*.csv` files).

Interpretation:

- “Before” = `Expected` (paper/manuscript numbers encoded in the notebook)
- “After” = `Actual` (pandas-derived values from the master CSVs)
- The audits make provenance mismatches explicit instead of silently updating the paper values.

Data-slice snapshots (raw rows):

- These are **not** audits; they do not contain Expected/Actual columns.
- They are intended to prevent “missing data” disputes by exporting the exact row-level slice used for a given analysis (e.g., Hybrid master dataset, iCPN, `runs=3`, etc.).
