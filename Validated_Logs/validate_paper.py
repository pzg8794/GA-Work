#!/usr/bin/env python3
"""Validate all numerical claims in main.tex against master CSVs."""
import pandas as pd
import numpy as np

BASE = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'

discrepancies = []

def check(label, paper_val, csv_val, tol=0.02):
    """Compare paper value to CSV value. tol is absolute tolerance."""
    if pd.isna(csv_val):
        discrepancies.append(f"  ⚠️  {label}: paper={paper_val}, CSV=NaN")
        return
    diff = abs(float(paper_val) - float(csv_val))
    if diff > tol:
        discrepancies.append(f"  ❌ {label}: paper={paper_val}, CSV={csv_val:.4f}, diff={diff:.4f}")
    else:
        print(f"  ✅ {label}: paper={paper_val}, CSV={csv_val:.4f}")

def check_int(label, paper_val, csv_val):
    if int(paper_val) != int(csv_val):
        discrepancies.append(f"  ❌ {label}: paper={paper_val}, CSV={csv_val}")
    else:
        print(f"  ✅ {label}: paper={paper_val}, CSV={csv_val}")

# ==============================================================================
# TABLE 10: Cross-Testbed Performance
# ==============================================================================
print("=" * 80)
print("TABLE 10: Cross-Testbed Validation")
print("=" * 80)

testbeds = [
    ('Paper 2', 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    ('Paper 7', 'Master_Dataset_paper7_50_50_5_ST.csv'),
    ('Paper 12', 'Master_Dataset_paper12_1500_500_5_ST.csv'),
]

# Paper claims for Table 10
table10_claims = {
    'Paper 2': {
        'topology': {'nodes': 15, 'edges': 51, 'paths': 8},
        'models': {
            'ORACLE':              {'avg_reward': 0.3927, 'regret': 0.0},
            'CPURSUITNEURALUCB':   {'avg_reward': 0.2888, 'regret': 508.7, 'eff': 73.24, 'gap': 26.76, 'wins': 38},
            'GNEURALUCB':          {'avg_reward': 0.2887, 'regret': 515.4, 'eff': 73.20, 'gap': 26.80, 'wins': 87},
            'ICPURSUITNEURALUCB':  {'avg_reward': 0.2934, 'regret': 494.4, 'eff': 74.45, 'gap': 25.55, 'wins': 94},
            'EXPNEURALUCB':        {'avg_reward': 0.2811, 'regret': 581.4, 'eff': 71.24, 'gap': 28.76, 'wins': 81},
        }
    },
    'Paper 7': {
        'topology': {'nodes': 50, 'edges': 141, 'paths': 15},
        'models': {
            'ORACLE':              {'avg_reward': 8.9237, 'regret': 0.0},
            'ICPURSUITNEURALUCB':  {'avg_reward': 6.9793, 'regret': 42.8,  'eff': 78.03, 'gap': 21.97, 'wins': 245},
            'EXPNEURALUCB':        {'avg_reward': 6.2227, 'regret': 272.3, 'eff': 69.57, 'gap': 30.43, 'wins': 16},
            'CPURSUITNEURALUCB':   {'avg_reward': 6.3314, 'regret': 269.1, 'eff': 70.82, 'gap': 29.18, 'wins': 0},
            'GNEURALUCB':          {'avg_reward': 6.3314, 'regret': 269.1, 'eff': 70.82, 'gap': 29.18, 'wins': 39},
        }
    },
    'Paper 12': {
        'topology': {'nodes': 100, 'edges': 426, 'paths': 4},
        'models': {
            'ORACLE':              {'avg_reward': 0.8724, 'regret': 0.0},
            'GNEURALUCB':          {'avg_reward': 0.3833, 'regret': 864.1, 'eff': 43.72, 'gap': 56.28, 'wins': 53},
            'EXPNEURALUCB':        {'avg_reward': 0.3730, 'regret': 892.2, 'eff': 42.54, 'gap': 57.46, 'wins': 91},
            'ICPURSUITNEURALUCB':  {'avg_reward': 0.3869, 'regret': 858.3, 'eff': 44.14, 'gap': 55.86, 'wins': 97},
            'CPURSUITNEURALUCB':   {'avg_reward': 0.3842, 'regret': 861.2, 'eff': 43.81, 'gap': 56.19, 'wins': 59},
        }
    }
}

for tb_name, csv_file in testbeds:
    print(f"\n--- {tb_name}: {csv_file} ---")
    df = pd.read_csv(f"{BASE}/{csv_file}")
    claims = table10_claims[tb_name]
    
    # Topology
    check_int(f"{tb_name} nodes", claims['topology']['nodes'], df.num_nodes.iloc[0])
    check_int(f"{tb_name} edges", claims['topology']['edges'], df.num_edges.iloc[0])
    check_int(f"{tb_name} paths", claims['topology']['paths'], df.num_paths.iloc[0])
    
    # Check allocators plus scales
    print(f"  Allocators in CSV: {sorted(df.allocator.unique())}")
    print(f"  Scales in CSV: {sorted(df.scale.unique())}")
    print(f"  Scenarios in CSV: {sorted(df.scenario.unique())}")
    print(f"  Experiments in CSV: {sorted(df.experiment.unique())}")
    
    # Per-model metrics (aggregated across all scenarios, allocators, scales, experiments)
    for model, vals in claims['models'].items():
        sub = df[df.model == model]
        if len(sub) == 0:
            discrepancies.append(f"  ❌ {tb_name}/{model}: NOT FOUND in CSV")
            continue
        
        csv_avg_reward = sub.avg_reward.mean()
        check(f"{tb_name}/{model} avg_reward", vals['avg_reward'], csv_avg_reward, tol=0.001)
        
        csv_regret = sub.regret.mean()
        check(f"{tb_name}/{model} regret", vals['regret'], csv_regret, tol=1.0)
        
        if 'eff' in vals:
            csv_eff = sub.eff_pct.mean()
            check(f"{tb_name}/{model} eff_pct", vals['eff'], csv_eff, tol=0.02)
        
        if 'gap' in vals:
            csv_gap = sub.gap_pct.mean()
            check(f"{tb_name}/{model} gap_pct", vals['gap'], csv_gap, tol=0.02)
        
        if 'wins' in vals:
            # Winner column has mixed-case model name
            # Count unique configs where this model is the winner
            configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])[['scenario','allocator','scale','experiment','winner']]
            w = sum(1 for _, row in configs.iterrows() if str(row['winner']).upper() == model)
            check_int(f"{tb_name}/{model} exp_wins", vals['wins'], w)

# ==============================================================================
# TABLE 11: Model Family Comparison (runs=5 only)
# ==============================================================================
print("\n" + "=" * 80)
print("TABLE 11: Model Family Validation (runs=5 only)")
print("=" * 80)

family_files = [
    ('CMABs', 'Master_Dataset_CMABs.csv'),
    ('iCMABs', 'Master_Dataset_iCMABs.csv'),
    ('Hybrid', 'Master_Dataset_Hybrid.csv'),
    ('EXP3', 'Master_Dataset_EXP3.csv'),
]

table11_claims = {
    'CMABs': {
        'CPURSUIT':          {'eff': 90.00, 'gap': 10.00, 'floor': 77.4, 'wins': 57, 'total': 75},
        'CEPSILONGREEDY':    {'eff': 87.96, 'gap': 12.04, 'floor': 79.2, 'wins': 18, 'total': 75},
        'CEXP4':             {'eff': 70.16, 'gap': 29.84, 'floor': 67.4, 'wins': 0,  'total': 75},
        'CTHOMPSONSAMPLING': {'eff': 68.12, 'gap': 31.88, 'floor': 62.5, 'wins': 0,  'total': 75},
        'CEPOCHGREEDY':      {'eff': 37.64, 'gap': 62.36, 'floor': 36.0, 'wins': 0,  'total': 75},
    },
    'iCMABs': {
        'ICEPSILONGREEDY':    {'eff': 88.56, 'gap': 11.44, 'floor': 81.0, 'wins': 75, 'total': 75},
        'ICPURSUIT':          {'eff': 69.01, 'gap': 30.99, 'floor': 56.9, 'wins': 0,  'total': 75},
        'ICTHOMPSONSAMPLING': {'eff': 68.03, 'gap': 31.97, 'floor': 62.8, 'wins': 0,  'total': 75},
        'ICEXP4':             {'eff': 37.47, 'gap': 62.53, 'floor': 36.1, 'wins': 0,  'total': 75},
        'ICEPOCHGREEDY':      {'eff': 37.53, 'gap': 62.47, 'floor': 36.1, 'wins': 0,  'total': 75},
    },
    'Hybrid': {
        'ICPURSUITNEURALUCB': {'eff': 88.37, 'gap': 11.63, 'floor': 22.1, 'wins': 140, 'total': 300},
        'CPURSUITNEURALUCB':  {'eff': 86.88, 'gap': 13.12, 'floor': 22.8, 'wins': 75,  'total': 300},
        'GNEURALUCB':         {'eff': 85.36, 'gap': 14.64, 'floor': 19.7, 'wins': 42,  'total': 300},
        'EXPNEURALUCB':       {'eff': 84.11, 'gap': 15.89, 'floor': 14.1, 'wins': 43,  'total': 300},
    },
    'EXP3': {
        'GNEURALUCB':  {'eff': 86.34, 'gap': 13.66, 'floor': 61.6, 'wins': 30, 'total': 75},
        'EXPNEURALUCB':{'eff': 84.07, 'gap': 15.93, 'floor': 18.0, 'wins': 39, 'total': 75},
        'EXPUCB':      {'eff': 78.43, 'gap': 21.57, 'floor': 68.8, 'wins': 6,  'total': 75},
    },
}

for fam_name, csv_file in family_files:
    print(f"\n--- {fam_name}: {csv_file} (runs=5) ---")
    df = pd.read_csv(f"{BASE}/{csv_file}")
    df = df[df.runs == 5]
    df_no = df[df.model != 'ORACLE']
    
    print(f"  Allocators: {sorted(df_no.allocator.unique())}")
    n_alloc = df_no.allocator.nunique()
    n_scen = df_no.scenario.nunique()
    n_scale = df_no.scale.nunique()
    n_exp = df_no.experiment.nunique()
    total = n_scen * n_alloc * n_scale * n_exp
    print(f"  Total configs: {n_scen}s x {n_alloc}a x {n_scale}sc x {n_exp}e = {total}")
    
    claims = table11_claims[fam_name]
    
    # Get winner counts
    configs = df_no.drop_duplicates(subset=['scenario','allocator','scale','experiment'])[['scenario','allocator','scale','experiment','winner']]
    winner_counts = {}
    for _, row in configs.iterrows():
        w = str(row['winner']).upper()
        winner_counts[w] = winner_counts.get(w, 0) + 1
    
    for model, vals in claims.items():
        sub = df_no[df_no.model == model]
        if len(sub) == 0:
            discrepancies.append(f"  ❌ {fam_name}/{model}: NOT FOUND in CSV (runs=5)")
            continue
        
        csv_eff = sub.eff_pct.mean()
        check(f"{fam_name}/{model} eff", vals['eff'], csv_eff, tol=0.02)
        
        csv_gap = 100 - csv_eff
        check(f"{fam_name}/{model} gap", vals['gap'], csv_gap, tol=0.02)
        
        csv_floor = sub.eff_pct.min()
        check(f"{fam_name}/{model} floor", vals['floor'], csv_floor, tol=0.15)
        
        w = winner_counts.get(model, 0)
        check_int(f"{fam_name}/{model} wins", vals['wins'], w)
        
        check_int(f"{fam_name}/{model} total_configs", vals['total'], total)

# ==============================================================================
# SCENARIO CHAMPION CLAIMS (Key Observations)
# ==============================================================================
print("\n" + "=" * 80)
print("KEY OBSERVATIONS: Scenario Champion Claims")
print("=" * 80)

# Paper 2 claims: iCP wins 2/5 scenarios (none, markov), CP and G each win 3/5
print("\n--- Paper 2 scenario champions ---")
df2 = pd.read_csv(f"{BASE}/Master_Dataset_paper2_4000_2000_5_ST.csv")
df2_no = df2[df2.model != 'ORACLE']
for scen in sorted(df2_no.scenario.unique()):
    sub = df2_no[df2_no.scenario == scen]
    sw = sub.scenario_winner.dropna().unique()
    print(f"  {scen}: scenario_winner = {sw}")

# Paper 7 claims: iCP wins all 5 scenarios
print("\n--- Paper 7 scenario champions ---")
df7 = pd.read_csv(f"{BASE}/Master_Dataset_paper7_50_50_5_ST.csv")
df7_no = df7[df7.model != 'ORACLE']
for scen in sorted(df7_no.scenario.unique()):
    sub = df7_no[df7_no.scenario == scen]
    sw = sub.scenario_winner.dropna().unique()
    print(f"  {scen}: scenario_winner = {sw}")

# Paper 12 claims: all 4 win 4/5 scenarios, markov uniquely iCP (60/60)
print("\n--- Paper 12 scenario champions ---")
df12 = pd.read_csv(f"{BASE}/Master_Dataset_paper12_1500_500_5_ST.csv")
df12_no = df12[df12.model != 'ORACLE']
for scen in sorted(df12_no.scenario.unique()):
    sub = df12_no[df12_no.scenario == scen]
    sw = sub.scenario_winner.dropna().unique()
    # Also count per-model wins in this scenario
    scen_configs = sub.drop_duplicates(subset=['allocator','scale','experiment'])[['allocator','scale','experiment','winner']]
    wc = {}
    for _, row in scen_configs.iterrows():
        w = str(row['winner'])
        wc[w] = wc.get(w, 0) + 1
    print(f"  {scen}: scenario_winner = {sw}, exp winners = {wc}")

# Paper 12 claim: markov iCPursuitNeuralUCB 60/60 wins
print("\n--- Paper 12 markov detail ---")
markov12 = df12_no[df12_no.scenario == 'MARKOV']
markov_configs = markov12.drop_duplicates(subset=['allocator','scale','experiment'])[['allocator','scale','experiment','winner']]
print(f"  Total markov configs: {len(markov_configs)}")
for w in sorted(markov_configs.winner.unique()):
    cnt = (markov_configs.winner == w).sum()
    print(f"  {w}: {cnt}/{len(markov_configs)}")

# ==============================================================================
# SUMMARY
# ==============================================================================
print("\n" + "=" * 80)
print(f"DISCREPANCY SUMMARY: {len(discrepancies)} issues found")
print("=" * 80)
for d in discrepancies:
    print(d)
