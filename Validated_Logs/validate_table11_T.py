#!/usr/bin/env python3
"""Validate Table 11 (T-only) values against paper."""
import pandas as pd

cmab = pd.read_csv('Master_Dataset_CMABs.csv')
icmab = pd.read_csv('Master_Dataset_iCMABs.csv')
hybrid = pd.read_csv('Master_Dataset_Hybrid.csv')
exp3 = pd.read_csv('Master_Dataset_EXP3.csv')

# Paper values (T-only)
paper = {
    ('CMABs', 'CPURSUIT'):           {'eff': 90.15, 'gap':  9.85, 'floor': 77.4, 'wins': 37, 'denom': 50},
    ('CMABs', 'CEPSILONGREEDY'):     {'eff': 87.78, 'gap': 12.22, 'floor': 79.2, 'wins': 13, 'denom': 50},
    ('CMABs', 'CEXP4'):              {'eff': 70.30, 'gap': 29.70, 'floor': 67.6, 'wins':  0, 'denom': 50},
    ('CMABs', 'CTHOMPSONSAMPLING'):  {'eff': 68.06, 'gap': 31.94, 'floor': 62.5, 'wins':  0, 'denom': 50},
    ('CMABs', 'CEPOCHGREEDY'):       {'eff': 37.63, 'gap': 62.37, 'floor': 36.0, 'wins':  0, 'denom': 50},
    ('iCMABs', 'ICEPSILONGREEDY'):   {'eff': 88.57, 'gap': 11.43, 'floor': 81.4, 'wins': 75, 'denom': 75},
    ('iCMABs', 'ICPURSUIT'):         {'eff': 69.33, 'gap': 30.67, 'floor': 61.6, 'wins':  0, 'denom': 75},
    ('iCMABs', 'ICTHOMPSONSAMPLING'):{'eff': 68.04, 'gap': 31.96, 'floor': 62.8, 'wins':  0, 'denom': 75},
    ('iCMABs', 'ICEXP4'):            {'eff': 37.43, 'gap': 62.57, 'floor': 36.1, 'wins':  0, 'denom': 75},
    ('iCMABs', 'ICEPOCHGREEDY'):     {'eff': 37.49, 'gap': 62.51, 'floor': 36.1, 'wins':  0, 'denom': 75},
    ('Hybrid', 'ICPURSUITNEURALUCB'):{'eff': 86.49, 'gap': 13.51, 'floor': 22.1, 'wins':118, 'denom':250},
    ('Hybrid', 'CPURSUITNEURALUCB'): {'eff': 85.77, 'gap': 14.23, 'floor': 22.8, 'wins': 60, 'denom':250},
    ('Hybrid', 'GNEURALUCB'):        {'eff': 83.89, 'gap': 16.11, 'floor': 22.5, 'wins': 37, 'denom':250},
    ('Hybrid', 'EXPNEURALUCB'):      {'eff': 83.31, 'gap': 16.69, 'floor': 14.1, 'wins': 35, 'denom':250},
    ('EXP3', 'GNEURALUCB'):          {'eff': 87.32, 'gap': 12.68, 'floor': 72.3, 'wins': 30, 'denom': 75},
    ('EXP3', 'EXPNEURALUCB'):        {'eff': 87.29, 'gap': 12.71, 'floor': 59.9, 'wins': 39, 'denom': 75},
    ('EXP3', 'EXPUCB'):              {'eff': 78.81, 'gap': 21.19, 'floor': 69.3, 'wins':  6, 'denom': 75},
}

datasets = {'CMABs': cmab, 'iCMABs': icmab, 'Hybrid': hybrid, 'EXP3': exp3}
errors = 0

for (fam, model), vals in paper.items():
    df = datasets[fam]
    sub = df[(df['runs'] == 5) & (df['cap_type'] == 'T') & (df['model'] == model)]
    
    csv_eff = sub['eff_pct'].mean()
    csv_floor = sub['eff_pct'].min()
    
    configs = df[(df['runs']==5) & (df['cap_type']=='T') & (df['model']!='ORACLE')].drop_duplicates(
        subset=['scenario','allocator','scale','experiment'])
    wc = configs['winner'].value_counts()
    csv_wins = 0
    for wname, cnt in wc.items():
        if str(wname).upper() == model:
            csv_wins = cnt
    csv_denom = len(configs)
    
    checks = []
    if abs(csv_eff - vals['eff']) > 0.02:
        checks.append(f"eff {vals['eff']} vs {csv_eff:.2f}")
    if abs(csv_floor - vals['floor']) > 0.15:
        checks.append(f"floor {vals['floor']} vs {csv_floor:.1f}")
    if csv_wins != vals['wins']:
        checks.append(f"wins {vals['wins']} vs {csv_wins}")
    if csv_denom != vals['denom']:
        checks.append(f"denom {vals['denom']} vs {csv_denom}")
    
    if checks:
        print(f"MISMATCH {fam}/{model}: {', '.join(checks)}")
        errors += 1
    else:
        print(f"  OK {fam}/{model}")

print(f"\n{'='*50}")
print(f"Result: {errors} mismatches out of {len(paper)} checks")
