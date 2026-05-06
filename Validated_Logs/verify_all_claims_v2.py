#!/usr/bin/env python3
"""Comprehensive validation of paper claims against master CSV datasets (case-aware)."""

import pandas as pd
import numpy as np

# Load all datasets
p2 = pd.read_csv('Master_Dataset_paper2_4000_2000_5_ST.csv')
p7 = pd.read_csv('Master_Dataset_paper7_50_50_5_ST.csv')
p12 = pd.read_csv('Master_Dataset_paper12_1500_500_5_ST.csv')
cmab = pd.read_csv('Master_Dataset_CMABs.csv')
icmab = pd.read_csv('Master_Dataset_iCMABs.csv')
hybrid = pd.read_csv('Master_Dataset_Hybrid.csv')
exp3 = pd.read_csv('Master_Dataset_EXP3.csv')

discrepancies = []

# Helper: normalize model name for matching
def norm(s):
    return str(s).upper().strip()

print("=" * 80)
print("FULL PAPER VALIDATION REPORT")
print("=" * 80)

# ====================================================================
# 1. PAPER 12 MARKOV - iCPursuitNeuralUCB wins (paper says 60/60)
# ====================================================================
print("\n--- 1. Paper 12 MARKOV wins ---")
p12m = p12[p12['scenario'].str.upper() == 'MARKOV']
# winner col is mixed case, model col is upper
icp_wins = sum(1 for _, r in p12m.iterrows() if norm(r['winner']) == 'ICPURSUITNEURALUCB')
total_markov = len(p12m)
print(f"  Total markov rows: {total_markov}")
print(f"  iCPursuitNeuralUCB wins: {icp_wins}/{total_markov}")
winner_dist = p12m['winner'].apply(norm).value_counts()
print(f"  Winner distribution:")
for w, c in winner_dist.items():
    print(f"    {w}: {c}")
if icp_wins != 60:
    discrepancies.append(f"Paper 12 MARKOV: paper says 60/60, CSV shows {icp_wins}/{total_markov}")

# ====================================================================
# 2. PAPER 2 scenario champions
# ====================================================================
print("\n--- 2. Paper 2 scenario champions ---")
for scen in sorted(p2['scenario'].unique()):
    sub = p2[p2['scenario'] == scen]
    winners = sub['scenario_winner'].dropna().unique()
    print(f"  {scen}: scenario_winner = {winners}")

# Paper says Obs #2: iCP wins 2/5 (none, markov), CP and G each win 3/5
# Paper says Obs #3: P12 markov uniquely favors iCP (60/60)
# Check P2 NONE: paper text says iCP wins none+markov
p2_none_sw = p2[p2['scenario'].str.upper() == 'NONE']['scenario_winner'].dropna().unique()
if len(p2_none_sw) > 1:
    discrepancies.append(f"Paper 2 NONE: paper implies iCP sole winner, but scenario_winner = {p2_none_sw}")

# ====================================================================
# 3. PAPER 7 scenario champions
# ====================================================================
print("\n--- 3. Paper 7 scenario champions ---")
for scen in sorted(p7['scenario'].unique()):
    sub = p7[p7['scenario'] == scen]
    winners = sub['scenario_winner'].dropna().unique()
    print(f"  {scen}: scenario_winner = {winners}")

# ====================================================================
# 4. PAPER 12 scenario champions
# ====================================================================
print("\n--- 4. Paper 12 scenario champions ---")
for scen in sorted(p12['scenario'].unique()):
    sub = p12[p12['scenario'] == scen]
    winners = sub['scenario_winner'].dropna().unique()
    print(f"  {scen}: scenario_winner = {winners}")

# P12 markov uniquely favors iCP?
p12_markov_sw = p12[p12['scenario'].str.upper() == 'MARKOV']['scenario_winner'].dropna().unique()
print(f"\n  P12 MARKOV scenario_winner: {p12_markov_sw}")
if len(p12_markov_sw) != 1 or norm(p12_markov_sw[0]) != 'ICPURSUITNEURALUCB':
    discrepancies.append(f"Paper 12 MARKOV scenario_winner: expected only iCP, got {p12_markov_sw}")

# ====================================================================
# 5. MODEL COUNTS
# ====================================================================
print("\n--- 5. Model counts ---")
all_dfs = {'P2': p2, 'P7': p7, 'P12': p12, 'CMABs': cmab, 'iCMABs': icmab, 'Hybrid': hybrid, 'EXP3': exp3}
all_models = set()
for name, df in all_dfs.items():
    models = set(df['model'].apply(norm).unique()) - {'ORACLE'}
    all_models.update(models)
    print(f"  {name}: {len(models)} non-Oracle models")

print(f"\n  Total unique non-Oracle models: {len(all_models)}")
print(f"  Models: {sorted(all_models)}")

# ====================================================================
# 6. ABSTRACT CLAIMS
# ====================================================================
print("\n--- 6. Abstract claims ---")

# Pursuit-neural efficiency (hybrid, runs=5)
hybrid_r5 = hybrid[(hybrid['runs'] == 5) & (hybrid['model'].apply(norm) != 'ORACLE')]
pursuit_models_upper = ['ICPURSUITNEURALUCB', 'CPURSUITNEURALUCB']
pursuit_data = hybrid_r5[hybrid_r5['model'].apply(norm).isin(pursuit_models_upper)]
pursuit_eff = pursuit_data['eff_pct'].mean()
print(f"  Pursuit-neural avg eff (hybrid, runs=5): {pursuit_eff:.1f}%")
for m in pursuit_models_upper:
    e = hybrid_r5[hybrid_r5['model'].apply(norm) == m]['eff_pct'].mean()
    print(f"    {m}: {e:.1f}%")

# 18-24 pp vs non-contextual baselines
cmab_r5 = cmab[(cmab['runs'] == 5) & (cmab['model'].apply(norm) != 'ORACLE')]
for b in ['CEPOCHGREEDY', 'CTHOMPSONSAMPLING']:
    b_eff = cmab_r5[cmab_r5['model'].apply(norm) == b]['eff_pct'].mean()
    gap = pursuit_eff - b_eff
    print(f"  Gap: pursuit-neural ({pursuit_eff:.1f}%) - {b} ({b_eff:.1f}%) = {gap:.1f} pp")

# ====================================================================
# 7. CROSS-TESTBED EFFICIENCY RANGES
# ====================================================================
print("\n--- 7. Cross-testbed efficiency ranges (paper says 69.6-78.0% P2/P7, 42.5-44.1% P12) ---")
for name, df in [('P2', p2), ('P7', p7), ('P12', p12)]:
    non_oracle = df[df['model'].apply(norm) != 'ORACLE']
    by_model = non_oracle.groupby(non_oracle['model'].apply(norm))['eff_pct'].mean()
    print(f"  {name}: model avg range {by_model.min():.1f}% - {by_model.max():.1f}%")
    for m in sorted(by_model.index):
        print(f"    {m}: {by_model[m]:.1f}%")

# ====================================================================
# 8. EXPERIMENT WINNER COUNTS (Key Observations)
# ====================================================================
print("\n--- 8. Experiment winner counts ---")
print("  Paper 2 (paper says iCP:94, G:87, EXP:81, CP:38):")
for m_upper, m_winner in [('ICPURSUITNEURALUCB', 'iCPursuitNeuralUCB'), 
                           ('GNEURALUCB', 'GNeuralUCB'),
                           ('EXPNEURALUCB', 'EXPNeuralUCB'),
                           ('CPURSUITNEURALUCB', 'CPursuitNeuralUCB')]:
    rows = p2[p2['model'].apply(norm) == m_upper]
    wins = sum(1 for _, r in rows.iterrows() if norm(r['winner']) == m_upper)
    print(f"    {m_winner}: {wins}/300")

print("  Paper 7 (paper says iCP:245):")
for m_upper, m_winner in [('ICPURSUITNEURALUCB', 'iCPursuitNeuralUCB'),
                           ('GNEURALUCB', 'GNeuralUCB'),
                           ('EXPNEURALUCB', 'EXPNeuralUCB'),
                           ('CPURSUITNEURALUCB', 'CPursuitNeuralUCB')]:
    rows = p7[p7['model'].apply(norm) == m_upper]
    wins = sum(1 for _, r in rows.iterrows() if norm(r['winner']) == m_upper)
    print(f"    {m_winner}: {wins}/300")

print("  Paper 12 (paper says iCP:97, EXP:91):")
for m_upper, m_winner in [('ICPURSUITNEURALUCB', 'iCPursuitNeuralUCB'),
                           ('GNEURALUCB', 'GNeuralUCB'),
                           ('EXPNEURALUCB', 'EXPNeuralUCB'),
                           ('CPURSUITNEURALUCB', 'CPursuitNeuralUCB')]:
    rows = p12[p12['model'].apply(norm) == m_upper]
    wins = sum(1 for _, r in rows.iterrows() if norm(r['winner']) == m_upper)
    print(f"    {m_winner}: {wins}/300")

# ====================================================================
# 9. EVALUATION COUNTS
# ====================================================================
print("\n--- 9. Evaluation counts ---")
total_all = 0
total_non_oracle = 0
for name, df in all_dfs.items():
    total = len(df)
    no = len(df[df['model'].apply(norm) != 'ORACLE'])
    total_all += total
    total_non_oracle += no
    print(f"  {name}: {total} total, {no} non-Oracle")
print(f"  Total: {total_all} rows, {total_non_oracle} non-Oracle")
print(f"  Paper claims: 7,890 evaluations")

# Check runs=5 only for internal
internal_r5_total = 0
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    r5 = df[(df['runs'] == 5) & (df['model'].apply(norm) != 'ORACLE')]
    internal_r5_total += len(r5)
    print(f"  {name} (runs=5, non-Oracle): {len(r5)}")
ext_total = sum(len(df[df['model'].apply(norm) != 'ORACLE']) for df in [p2, p7, p12])
print(f"  External (non-Oracle): {ext_total}")
print(f"  Internal runs=5 + External: {internal_r5_total + ext_total}")

# Also just internal all runs
internal_all_total = 0
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    no = len(df[df['model'].apply(norm) != 'ORACLE'])
    internal_all_total += no
print(f"  Internal all runs: {internal_all_total}")
print(f"  Internal all + External: {internal_all_total + ext_total}")

# ====================================================================
# 10. CAPACITY PARADOX CLAIMS
# ====================================================================
print("\n--- 10. Capacity paradox (22-31 pp collapse under Adaptive) ---")
hybrid_r5_no = hybrid_r5.copy()
for m in ['ICPURSUITNEURALUCB', 'CPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB']:
    for alloc in ['Default', 'Dynamic', 'Random', 'ThompsonSampling']:
        sub_adapt = hybrid_r5_no[(hybrid_r5_no['model'].apply(norm) == m) & 
                                 (hybrid_r5_no['scenario'].str.upper() == 'ADAPTIVE') &
                                 (hybrid_r5_no['allocator'] == alloc)]
        s1 = sub_adapt[sub_adapt['scale'] == 1.0]['eff_pct'].mean()
        s2 = sub_adapt[sub_adapt['scale'] == 2.0]['eff_pct'].mean()
        if not np.isnan(s1) and not np.isnan(s2):
            diff = s1 - s2
            if abs(diff) > 15:
                print(f"  {m}/{alloc} Adaptive: scale=1 {s1:.1f}% -> scale=2 {s2:.1f}%, collapse={diff:.1f} pp")

# Allocator swings
print("\n  Allocator swings (max - min across allocators):")
for m in ['ICPURSUITNEURALUCB', 'CPURSUITNEURALUCB']:
    by_alloc = hybrid_r5_no[hybrid_r5_no['model'].apply(norm) == m].groupby('allocator')['eff_pct'].mean()
    swing = by_alloc.max() - by_alloc.min()
    print(f"  {m}: {by_alloc.to_dict()}")
    print(f"    range = {by_alloc.min():.1f}% - {by_alloc.max():.1f}%, swing = {swing:.1f} pp")

# ====================================================================
# 11. TABLE 11 VERIFICATION (already validated, but double-check)
# ====================================================================
print("\n--- 11. Table 11 spot-check (runs=5 only) ---")
# CMABs CPursuit 
cpursuit = cmab[(cmab['runs'] == 5) & (cmab['model'].apply(norm) == 'CPURSUIT')]
print(f"  CPursuit eff: {cpursuit['eff_pct'].mean():.2f}% (paper: 90.00%)")
print(f"  CPursuit wins: {sum(1 for _, r in cpursuit.iterrows() if norm(r['winner']) == 'CPURSUIT')}/75 (paper: 57/75)")

# iCEpsilonGreedy
iceg = icmab[(icmab['runs'] == 5) & (icmab['model'].apply(norm) == 'ICEPSILONGREEDY')]
print(f"  iCEpsilonGreedy eff: {iceg['eff_pct'].mean():.2f}% (paper: 88.56%)")
print(f"  iCEpsilonGreedy wins: {sum(1 for _, r in iceg.iterrows() if norm(r['winner']) == 'ICEPSILONGREEDY')}/75 (paper: 75/75)")

# Hybrid iCPursuitNeuralUCB
icp_h = hybrid[(hybrid['runs'] == 5) & (hybrid['model'].apply(norm) == 'ICPURSUITNEURALUCB')]
print(f"  iCPursuitNeuralUCB eff: {icp_h['eff_pct'].mean():.2f}% (paper: 88.37%)")
print(f"  iCPursuitNeuralUCB wins: {sum(1 for _, r in icp_h.iterrows() if norm(r['winner']) == 'ICPURSUITNEURALUCB')}/300 (paper: 140/300)")

# EXP3 EXPNeuralUCB
exp_n = exp3[(exp3['runs'] == 5) & (exp3['model'].apply(norm) == 'EXPNEURALUCB')]
print(f"  EXPNeuralUCB eff: {exp_n['eff_pct'].mean():.2f}% (paper: 84.07%)")
print(f"  EXPNeuralUCB wins: {sum(1 for _, r in exp_n.iterrows() if norm(r['winner']) == 'EXPNEURALUCB')}/75 (paper: 39/75)")

# ====================================================================
# SUMMARY
# ====================================================================
print("\n" + "=" * 80)
print("CONFIRMED DISCREPANCIES:")
print("=" * 80)
for i, d in enumerate(discrepancies, 1):
    print(f"  {i}. {d}")
