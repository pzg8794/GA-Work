#!/usr/bin/env python3
"""Precise verification of key discrepancies."""
import pandas as pd

p12 = pd.read_csv('Master_Dataset_paper12_1500_500_5_ST.csv')
p2 = pd.read_csv('Master_Dataset_paper2_4000_2000_5_ST.csv')
cmab = pd.read_csv('Master_Dataset_CMABs.csv')
hybrid = pd.read_csv('Master_Dataset_Hybrid.csv')

# 1. Paper 12 MARKOV - filter to iCP rows only (1 row per experiment)
p12m_icp = p12[(p12['scenario'] == 'MARKOV') & (p12['model'] == 'ICPURSUITNEURALUCB')]
icp_wins = (p12m_icp['winner'].str.upper() == 'ICPURSUITNEURALUCB').sum()
total = len(p12m_icp)
print(f"1. P12 MARKOV: iCP rows={total}, iCP wins={icp_wins}/{total}")
print(f"   Winner dist: {p12m_icp['winner'].value_counts().to_dict()}")

# 2. Paper 2 NONE scenario_winner
p2_none = p2[p2['scenario'] == 'NONE']
sw = p2_none['scenario_winner'].dropna().unique()
print(f"\n2. P2 NONE scenario_winner: {sw}")

# P2 all scenario champions
print("\n   P2 all scenario champions:")
for scen in sorted(p2['scenario'].unique()):
    sub = p2[p2['scenario'] == scen]
    winners = sub['scenario_winner'].dropna().unique()
    print(f"   {scen}: {winners}")

# 3. cap_type in CMABs
print(f"\n3. CMABs cap_type values: {cmab['cap_type'].unique()}")
print(f"   Hybrid cap_type values: {hybrid['cap_type'].unique()}")

# 4. CPursuit wins with cap_type=T filter
cp_t = cmab[(cmab['runs'] == 5) & (cmab['model'] == 'CPURSUIT') & (cmab['cap_type'] == 'T')]
cp_wins_t = (cp_t['winner'].str.upper() == 'CPURSUIT').sum()
print(f"\n4. CPursuit (runs=5, cap_type=T): {len(cp_t)} rows, {cp_wins_t} wins (paper: 57/75)")

cp_all = cmab[(cmab['runs'] == 5) & (cmab['model'] == 'CPURSUIT')]
cp_wins_all = (cp_all['winner'].str.upper() == 'CPURSUIT').sum()
print(f"   CPursuit (runs=5, all cap): {len(cp_all)} rows, {cp_wins_all} wins")

# 5. Table 11 caption says cap_type=T. Verify eff matches.
cp_eff_t = cp_t['eff_pct'].mean()
cp_eff_all = cp_all['eff_pct'].mean()
print(f"\n5. CPursuit eff_pct: cap_type=T -> {cp_eff_t:.2f}%, all cap -> {cp_eff_all:.2f}% (paper: 90.00%)")

# 6. Verify iCEpsilonGreedy (iCMABs)
icmab = pd.read_csv('Master_Dataset_iCMABs.csv')
print(f"\n6. iCMABs cap_type: {icmab['cap_type'].unique()}")
iceg_t = icmab[(icmab['runs'] == 5) & (icmab['model'] == 'ICEPSILONGREEDY') & (icmab['cap_type'] == 'T')]
iceg_wins_t = (iceg_t['winner'].str.upper() == 'ICEPSILONGREEDY').sum()
print(f"   iCEpsilonGreedy (runs=5, T): {len(iceg_t)} rows, {iceg_wins_t} wins (paper: 75/75)")

# 7. Hybrid iCP (cap_type=T)
icp_h_t = hybrid[(hybrid['runs'] == 5) & (hybrid['model'] == 'ICPURSUITNEURALUCB') & (hybrid['cap_type'] == 'T')]
icp_h_wins = (icp_h_t['winner'].str.upper() == 'ICPURSUITNEURALUCB').sum()
print(f"\n7. Hybrid iCP (runs=5, T): {len(icp_h_t)} rows, {icp_h_wins} wins (paper: 140/300)")

# Check with all cap_types
icp_h_all = hybrid[(hybrid['runs'] == 5) & (hybrid['model'] == 'ICPURSUITNEURALUCB')]
icp_h_wins_all = (icp_h_all['winner'].str.upper() == 'ICPURSUITNEURALUCB').sum()
print(f"   Hybrid iCP (runs=5, all cap): {len(icp_h_all)} rows, {icp_h_wins_all} wins")

# 8. EXP3
exp3 = pd.read_csv('Master_Dataset_EXP3.csv')
print(f"\n8. EXP3 cap_type: {exp3['cap_type'].unique()}")
expn_t = exp3[(exp3['runs'] == 5) & (exp3['model'] == 'EXPNEURALUCB') & (exp3['cap_type'] == 'T')]
expn_wins = (expn_t['winner'].str.upper() == 'EXPNEURALUCB').sum()
print(f"   EXPNeuralUCB (runs=5, T): {len(expn_t)} rows, {expn_wins} wins (paper: 39/75)")

# 9. How many configs in P12 MARKOV per model?
for m in p12[p12['scenario'] == 'MARKOV']['model'].unique():
    count = len(p12[(p12['scenario'] == 'MARKOV') & (p12['model'] == m)])
    print(f"\n9. P12 MARKOV {m}: {count} rows")

# 10. Abstract "552 configurations"  
# Maybe 552 is just the Hybrid rows? 4 models x 5 scen x 4 alloc x 3 scales x ? 
# Or unique model-scenario-allocator combos
print(f"\n10. Checking what '552' could be:")
print(f"    Hybrid unique configs (runs=5, T, non-Oracle):")
h_r5_t = hybrid[(hybrid['runs'] == 5) & (hybrid['cap_type'] == 'T') & (hybrid['model'] != 'ORACLE')]
configs = h_r5_t[['model', 'scenario', 'allocator', 'scale']].drop_duplicates()
print(f"    {len(configs)} unique model-scenario-allocator-scale")

# Try: all internal datasets, runs=5, cap_type=T
total_configs = 0
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    r5t = df[(df['runs'] == 5) & (df['cap_type'] == 'T') & (df['model'] != 'ORACLE')]
    c = r5t[['model', 'scenario', 'allocator', 'scale']].drop_duplicates()
    total_configs += len(c)
    print(f"    {name}: {len(c)}")
print(f"    Total (internal, runs=5, T): {total_configs}")

# All internal, all runs, cap_type=T
total_configs2 = 0
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    t = df[(df['cap_type'] == 'T') & (df['model'] != 'ORACLE')]
    c = t[['model', 'scenario', 'allocator', 'scale']].drop_duplicates()
    total_configs2 += len(c)
    print(f"    {name} (all runs, T): {len(c)}")
print(f"    Total (internal, all runs, T): {total_configs2}")
