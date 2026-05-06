#!/usr/bin/env python3
"""Comprehensive validation of paper claims against master CSV datasets."""

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

print("=" * 80)
print("FULL PAPER VALIDATION REPORT")
print("=" * 80)

# ====================================================================
# 1. PAPER 12 MARKOV - iCPursuitNeuralUCB wins (paper says 60/60)
# ====================================================================
print("\n--- 1. Paper 12 MARKOV wins ---")
p12m = p12[p12['scenario'] == 'markov']
icp_wins_markov = (p12m['winner'] == 'iCPursuitNeuralUCB').sum()
total_markov = len(p12m)
print(f"  iCPursuitNeuralUCB wins: {icp_wins_markov}/{total_markov}")
print(f"  Winner distribution:")
for model, count in p12m['winner'].value_counts().items():
    print(f"    {model}: {count}")
if icp_wins_markov != 60:
    discrepancies.append(f"Paper 12 MARKOV: paper says 60/60, CSV shows {icp_wins_markov}/{total_markov}")

# ====================================================================
# 2. PAPER 2 NONE scenario_winner
# ====================================================================
print("\n--- 2. Paper 2 NONE scenario_winner ---")
p2n = p2[p2['scenario'] == 'none']
scene_winners_none = p2n['scenario_winner'].unique()
print(f"  scenario_winner values: {scene_winners_none}")
# Paper 2 observation #2 says iCP wins 2/5 scenarios (none, markov)
# Check if that's correct
print("\n  Paper 2 scenario champions:")
p2_scenario_champs = {}
for scen in sorted(p2['scenario'].unique()):
    sub = p2[p2['scenario'] == scen]
    winners = sub['scenario_winner'].unique()
    p2_scenario_champs[scen] = winners
    print(f"    {scen}: {winners}")

# Paper says: iCP wins none + markov => 2/5
icp_scenarios = [s for s, w in p2_scenario_champs.items() 
                 if any('iCPursuitNeuralUCB' in str(x) for x in w)]
print(f"\n  Scenarios where iCP is scenario_winner: {icp_scenarios} ({len(icp_scenarios)}/5)")

# Paper says CP and G each win 3/5
cp_scenarios = [s for s, w in p2_scenario_champs.items() 
                if any('CPursuitNeuralUCB' in str(x) and 'iC' not in str(x) for x in w)]
g_scenarios = [s for s, w in p2_scenario_champs.items() 
               if any('GNeuralUCB' in str(x) for x in w)]
print(f"  Scenarios where CP is scenario_winner: {cp_scenarios} ({len(cp_scenarios)}/5)")
print(f"  Scenarios where G is scenario_winner: {g_scenarios} ({len(g_scenarios)}/5)")

# ====================================================================
# 3. PAPER 7 scenario champions
# ====================================================================
print("\n--- 3. Paper 7 scenario champions ---")
for scen in sorted(p7['scenario'].unique()):
    sub = p7[p7['scenario'] == scen]
    winners = sub['scenario_winner'].unique()
    print(f"  {scen}: {winners}")
# Paper says: iCP wins all 5, only G and EXP share markov

# ====================================================================
# 4. PAPER 12 scenario champions  
# ====================================================================
print("\n--- 4. Paper 12 scenario champions ---")
for scen in sorted(p12['scenario'].unique()):
    sub = p12[p12['scenario'] == scen]
    winners = sub['scenario_winner'].unique()
    print(f"  {scen}: {winners}")
# Paper says: all 4 models win in 4/5, markov uniquely favors iCP

# Check: does markov UNIQUELY favor iCP?
p12_markov_sw = p12[p12['scenario'] == 'markov']['scenario_winner'].unique()
if len(p12_markov_sw) > 1:
    discrepancies.append(f"Paper 12 MARKOV: paper says uniquely favors iCP, but scenario_winner = {p12_markov_sw}")

# ====================================================================
# 5. MODEL COUNTS
# ====================================================================
print("\n--- 5. Model counts ---")
all_dfs = {'P2': p2, 'P7': p7, 'P12': p12, 'CMABs': cmab, 'iCMABs': icmab, 'Hybrid': hybrid, 'EXP3': exp3}
all_models = set()
for name, df in all_dfs.items():
    models = set(df['model'].unique()) - {'Oracle'}
    all_models.update(models)
    print(f"  {name}: {len(models)} non-Oracle models")

print(f"\n  Total unique non-Oracle models: {len(all_models)}")
print(f"  Models: {sorted(all_models)}")
# Paper abstract says 13, intro says 16 (15+Oracle), portfolio might say 14+Oracle

# ====================================================================
# 6. ABSTRACT CLAIMS
# ====================================================================
print("\n--- 6. Abstract claims ---")

# "552 configurations"
print(f"  Abstract says: 552 configurations")
# What could 552 be? Let's check various combos

# "86-89% oracle-normalized efficiency"
# Check pursuit-neural family averages
hybrid_r5 = hybrid[hybrid['runs'] == 5]
pursuit_models = ['iCPursuitNeuralUCB', 'CPursuitNeuralUCB']
pursuit_eff = hybrid_r5[hybrid_r5['model'].isin(pursuit_models)]['eff_pct'].mean()
print(f"  Pursuit-neural avg eff (hybrid, runs=5): {pursuit_eff:.1f}%")

all_pursuit_neural = hybrid_r5[hybrid_r5['model'].isin(['iCPursuitNeuralUCB', 'CPursuitNeuralUCB'])]
for m in ['iCPursuitNeuralUCB', 'CPursuitNeuralUCB']:
    e = hybrid_r5[hybrid_r5['model'] == m]['eff_pct'].mean()
    print(f"    {m}: {e:.1f}%")

# "18-24 pp outperformance vs non-contextual baselines"
# This likely compares pursuit-neural vs CEpochGreedy/CThompsonSampling
cmab_r5 = cmab[cmab['runs'] == 5]
baselines = ['CEpochGreedy', 'CThompsonSampling']
for b in baselines:
    b_eff = cmab_r5[cmab_r5['model'] == b]['eff_pct'].mean()
    gap = pursuit_eff - b_eff
    print(f"  Pursuit-neural vs {b}: {pursuit_eff:.1f}% - {b_eff:.1f}% = {gap:.1f} pp")

# ====================================================================
# 7. CROSS-TESTBED EFFICIENCY RANGES
# ====================================================================
print("\n--- 7. Cross-testbed efficiency ranges ---")
# Paper says: "69.6-78.0% on Papers 2/7 and 42.5-44.1% on Paper 12"
for name, df in [('P2', p2), ('P7', p7), ('P12', p12)]:
    non_oracle = df[df['model'] != 'Oracle']
    by_model = non_oracle.groupby('model')['eff_pct'].mean()
    print(f"  {name}: range {by_model.min():.1f}% - {by_model.max():.1f}%")
    print(f"    Overall mean: {non_oracle['eff_pct'].mean():.1f}%")

# ====================================================================
# 8. EVALUATION COUNTS
# ====================================================================
print("\n--- 8. Evaluation counts ---")
# Paper claims: "7,890 model-scenario-configuration evaluations across 835 unique scenario-allocator-capacity-horizon settings"
total_non_oracle = 0
for name, df in all_dfs.items():
    n = len(df[df['model'] != 'Oracle'])
    total_non_oracle += n
    print(f"  {name}: {n} non-Oracle rows")
print(f"  Total non-Oracle rows: {total_non_oracle}")
print(f"  Paper claims: 7,890")

# What about 835 unique scenario-allocator-capacity-horizon settings?
# These are rows where you ignore the model
for name, df in all_dfs.items():
    cols_check = ['scenario', 'allocator', 'scale']
    if 'cap_type' in df.columns:
        cols_check.append('cap_type')
    unique_settings = df[cols_check].drop_duplicates()
    print(f"  {name}: {len(unique_settings)} unique settings (scenario x allocator x scale)")

# "552 configurations" from abstract
# Maybe 552 = unique model-scenario-allocator combos from internal datasets?
print("\n  Checking '552 configurations':")
# CMABs: 5 models * 5 scenarios * 1 alloc * 3 scales = 75
# iCMABs: 5 models * 5 scenarios * 1 alloc * 3 scales = 75 (but has 2 cap_types?)
# Hybrid: 4 models * 5 scenarios * 4 alloc * 3 scales = 240
# EXP3: 3 models * 5 scenarios * 1 alloc * 3 scales = 45
# Total: 435? Let's check with cap_type
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    r5 = df[df['runs'] == 5]
    no = r5[r5['model'] != 'Oracle']
    if 'cap_type' in no.columns:
        configs = no[['model', 'scenario', 'allocator', 'scale', 'cap_type']].drop_duplicates()
    else:
        configs = no[['model', 'scenario', 'allocator', 'scale']].drop_duplicates()
    print(f"  {name} (runs=5): {len(configs)} unique model-scenario-alloc-scale configs")

# Also check with both runs
for name, df in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    no = df[df['model'] != 'Oracle']
    if 'cap_type' in no.columns:
        configs = no[['model', 'scenario', 'allocator', 'scale', 'cap_type', 'runs']].drop_duplicates()
    else:
        configs = no[['model', 'scenario', 'allocator', 'scale', 'runs']].drop_duplicates()
    print(f"  {name} (all runs): {len(configs)} unique configs")

# ====================================================================
# 9. KEY OBSERVATIONS TABLE 10 CLAIMS (already validated but recheck)
# ====================================================================
print("\n--- 9. Table 10 Key Observation details ---")
# Paper says Paper 2 is a 4-way race: iCP: 94, G: 87, EXP: 81, CP: 38
p2_winners = p2[p2['model'] != 'Oracle'].groupby('model').apply(lambda x: (x['winner'] == x['model'].iloc[0]).sum())
print(f"  Paper 2 experiment winner counts:")
for m in ['iCPursuitNeuralUCB', 'GNeuralUCB', 'EXPNeuralUCB', 'CPursuitNeuralUCB']:
    count = (p2[p2['model'] == m]['winner'] == m).sum()
    print(f"    {m}: {count}")

# Paper 12 is a 2-way race: iCP: 97, EXP: 91
print(f"  Paper 12 experiment winner counts:")
for m in ['iCPursuitNeuralUCB', 'GNeuralUCB', 'EXPNeuralUCB', 'CPursuitNeuralUCB']:
    count = (p12[p12['model'] == m]['winner'] == m).sum()
    print(f"    {m}: {count}")

# ====================================================================
# 10. INTRO CLAIMS ON TOPOLOGY
# ====================================================================
print("\n--- 10. Topology claims ---")
# Paper says: Paper 2: 15N, 51E, 8P  Paper 7: 50N, 141E, 15P  Paper 12: 100N, 426E, 4P
for name, df in [('P2', p2), ('P7', p7), ('P12', p12)]:
    if 'num_nodes' in df.columns:
        print(f"  {name}: nodes={df['num_nodes'].unique()}, edges={df.get('num_edges', pd.Series()).unique()}")
    unique_paths = df['num_paths'].unique() if 'num_paths' in df.columns else 'N/A'
    print(f"  {name}: num_paths={unique_paths}")

# ====================================================================
# 11. CAPACITY PARADOX CLAIMS
# ====================================================================
print("\n--- 11. Capacity paradox claims ---")
# "22-31 pp efficiency collapse under Adaptive attacks"
# Compare T scale 1 vs T scale 2 under adaptive scenario
hybrid_r5_adaptive = hybrid_r5[hybrid_r5['scenario'] == 'adaptive']
for m in ['iCPursuitNeuralUCB', 'CPursuitNeuralUCB']:
    s1 = hybrid_r5_adaptive[(hybrid_r5_adaptive['model'] == m) & (hybrid_r5_adaptive['scale'] == 1.0)]['eff_pct'].mean()
    s2 = hybrid_r5_adaptive[(hybrid_r5_adaptive['model'] == m) & (hybrid_r5_adaptive['scale'] == 2.0)]['eff_pct'].mean()
    print(f"  {m} Adaptive: scale=1 {s1:.1f}% -> scale=2 {s2:.1f}%, diff={s1-s2:.1f} pp")

# "10-15 pp allocator swings"
print("\n  Allocator swings (hybrid, runs=5):")
for m in ['iCPursuitNeuralUCB', 'CPursuitNeuralUCB']:
    by_alloc = hybrid_r5[hybrid_r5['model'] == m].groupby('allocator')['eff_pct'].mean()
    swing = by_alloc.max() - by_alloc.min()
    print(f"  {m}: alloc range {by_alloc.min():.1f}% - {by_alloc.max():.1f}% (swing={swing:.1f} pp)")

# ====================================================================
# SUMMARY
# ====================================================================
print("\n" + "=" * 80)
print("DISCREPANCIES FOUND:")
print("=" * 80)
for i, d in enumerate(discrepancies, 1):
    print(f"  {i}. {d}")
if not discrepancies:
    print("  None detected (but see detailed notes above)")
