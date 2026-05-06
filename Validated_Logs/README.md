# Validated Logs

This folder contains generated datasets and helper scripts for auditing/validating paper tables.

## Master-of-masters (standard runs)

To build a single combined dataset from the per-paper masters (e.g., `Master_Dataset_paper7-4000_2000.csv`), run:

```bash
cd /Users/pitergarcia/DataScience/Semester4/GA-Work
./.quantum/bin/python Validated_Logs/build_master_dataset_papers.py --key 4000_2000
```

Output:
- `Validated_Logs/Master_Dataset_papers-4000_2000.csv`

The combined output appends:
- `paper` (e.g., `paper7`)
- `config_key` (e.g., `4000_2000`)

## Standardized manuscript tables (4000\_2000)

To regenerate the LaTeX tables for the manuscript using the standardized dataset (`4000_2000`), run:

```bash
cd /Users/pitergarcia/DataScience/Semester4/GA-Work
./.quantum/bin/python Validated_Logs/build_standardized_manuscript_tables.py --runs 5
```

This prints two LaTeX `table*` environments to stdout:
- A standardized version of the cross-testbed comparison (Avg Reward / Regret / Eff / Gap / Exp Winner)
- A standardized version of the external-testbed Default-allocator slice (Avg Eff / Gap / Floor / Exp Winner)

These are designed to be pasted into:
- `GA Papers/QuantumFaultTolerant/main.tex`
