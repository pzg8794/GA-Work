#!/usr/bin/env python3
"""Verify Table 11 caption claim re cap_type and confirm final numbers."""
import pandas as pd

cmab = pd.read_csv('Master_Dataset_CMABs.csv')
icmab = pd.read_csv('Master_Dataset_iCMABs.csv')
hybrid = pd.read_csv('Master_Dataset_Hybrid.csv')
exp3 = pd.read_csv('Master_Dataset_EXP3.csv')

print("TABLE 11 DATA SOURCE VERIFICATION")
print("=" * 70)

# Table 11 values that we validated:
# CPursuit: 90.00%, 57/75
# iCEpsilonGreedy: 88.56%, 75/75
# iCPursuitNeuralUCB: 88.37%, 140/300
# EXPNeuralUCB: 84.07%, 39/75

# Check each with different cap_type filters
for dataset_name, df, model_upper, paper_eff, paper_wins, paper_denom in [
    ('CMABs', cmab, 'CPURSUIT', 90.00, 57, 75),
    ('iCMABs', icmab, 'ICEPSILONGREEDY', 88.56, 75, 75),
    ('Hybrid', hybrid, 'ICPURSUITNEURALUCB', 88.37, 140, 300),
    ('EXP3', exp3, 'EXPNEURALUCB', 84.07, 39, 75),
]:
    print(f"\n--- {dataset_name}: {model_upper} ---")
    r5 = df[(df['runs'] == 5) & (df['model'] == model_upper)]
    
    for cap in ['ALL', 'T', 'Tb']:
        if cap == 'ALL':
            subset = r5
        else:
            subset = r5[r5['cap_type'] == cap]
        
        eff = subset['eff_pct'].mean()
        wins = (subset['winner'].str.upper() == model_upper).sum()
        total = len(subset)
        
        match_eff = "MATCH" if abs(eff - paper_eff) < 0.02 else f"DIFF ({eff:.2f})"
        match_wins = "MATCH" if wins == paper_wins else f"DIFF ({wins})"
        
        print(f"  cap={cap:3s}: rows={total:4d}, eff={eff:.2f}% [{match_eff}], "
              f"wins={wins}/{total} [{match_wins}]")

# Also check the cap_type distribution per dataset
print("\n\nCAP_TYPE DISTRIBUTION (runs=5, non-Oracle):")
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    r5_no = df[(df['runs'] == 5) & (df['model'] != 'ORACLE')]
    for ct in r5_no['cap_type'].unique():
        n = len(r5_no[r5_no['cap_type'] == ct])
        models = r5_no[r5_no['cap_type'] == ct]['model'].nunique()
        print(f"  {name} cap={ct}: {n} rows, {models} models")

# What filter produces the exact paper denominators?
print("\n\nFINDING THE RIGHT FILTER FOR PAPER DENOMINATORS:")
# CMABs: 75 per model means 75 rows when we pick one model
# 5 scenarios × 1 allocator × ? = 75 → need 15. 3 scales × 5 experiments = 15. But that gives 75.
# With cap_type=T: only 50 rows for CPursuit. With Tb: 75 rows.
# So maybe the paper uses cap_type=Tb for CMABs?
for name, df, model in [('CMABs', cmab, 'CPURSUIT'), ('iCMABs', icmab, 'ICEPSILONGREEDY'),
                         ('EXP3', exp3, 'EXPNEURALUCB')]:
    r5m = df[(df['runs'] == 5) & (df['model'] == model)]
    for ct in ['T', 'Tb']:
        n = len(r5m[r5m['cap_type'] == ct])
        print(f"  {name} {model} cap={ct}: {n} rows")
    
    # What about unique experiments?
    print(f"  {name} unique experiments: {r5m['experiment'].nunique()}")
    print(f"  {name} unique scales: {r5m['scale'].unique()}")
    print(f"  {name} unique allocators: {r5m['allocator'].unique()}")
    print(f"  {name} unique scenarios: {r5m['scenario'].unique()}")

# For Hybrid (paper says 300 per model)
r5h = hybrid[(hybrid['runs'] == 5) & (hybrid['model'] == 'ICPURSUITNEURALUCB')]
print(f"\n  Hybrid ICPURSUITNEURALUCB all: {len(r5h)} rows")
for ct in ['T', 'Tb']:
    n = len(r5h[r5h['cap_type'] == ct])
    print(f"  Hybrid iCP cap={ct}: {n} rows")
