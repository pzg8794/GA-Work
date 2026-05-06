#!/usr/bin/env python3
"""Recompute Table 11 with runs=5 AND cap_type=T only."""
import pandas as pd
import numpy as np

display_names = {
    'CEPSILONGREEDY': 'CEpsilonGreedy', 'CPURSUIT': 'CPursuit', 'CEXP4': 'CEXP4',
    'CEPOCHGREEDY': 'CEpochGreedy', 'CTHOMPSONSAMPLING': 'CThompsonSampling',
    'ICEPSILONGREEDY': 'iCEpsilonGreedy', 'ICPURSUIT': 'iCPursuit', 'ICEXP4': 'iCEXP4',
    'ICEPOCHGREEDY': 'iCEpochGreedy', 'ICTHOMPSONSAMPLING': 'iCThompsonSampling',
    'ICPURSUITNEURALUCB': 'iCPursuitNeuralUCB', 'CPURSUITNEURALUCB': 'CPursuitNeuralUCB',
    'GNEURALUCB': 'GNeuralUCB', 'EXPNEURALUCB': 'EXPNeuralUCB', 'EXPUCB': 'EXPUCB',
}

families = {
    'CMABs': ('Master_Dataset_CMABs.csv', ['CPURSUIT','CEPSILONGREEDY','CEXP4','CTHOMPSONSAMPLING','CEPOCHGREEDY']),
    'iCMABs': ('Master_Dataset_iCMABs.csv', ['ICEPSILONGREEDY','ICPURSUIT','ICTHOMPSONSAMPLING','ICEXP4','ICEPOCHGREEDY']),
    'Hybrid': ('Master_Dataset_Hybrid.csv', ['ICPURSUITNEURALUCB','CPURSUITNEURALUCB','GNEURALUCB','EXPNEURALUCB']),
    'EXP3': ('Master_Dataset_EXP3.csv', ['GNEURALUCB','EXPNEURALUCB','EXPUCB']),
}

for family, (csvfile, model_order) in families.items():
    df = pd.read_csv(csvfile)
    df = df[(df['runs'] == 5) & (df['cap_type'] == 'T') & (df['model'] != 'ORACLE')]
    
    n_allocs = df['allocator'].nunique()
    n_scenarios = df['scenario'].nunique()
    n_scales = df['scale'].nunique()
    n_experiments = df['experiment'].nunique()
    total_configs = n_scenarios * n_allocs * n_scales * n_experiments
    
    allocs = sorted(df['allocator'].unique())
    
    print(f"\n{'='*70}")
    print(f"{family} (runs=5, cap_type=T, {len(df)} non-Oracle rows)")
    print(f"  Allocators ({n_allocs}): {allocs}")
    print(f"  Configs per model: {n_scenarios}scen x {n_allocs}alloc x {n_scales}scales x {n_experiments}exp = {total_configs}")
    print(f"{'='*70}")
    
    # Get unique experiment configs and their winners
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])[['scenario','allocator','scale','experiment','winner']]
    winner_counts = configs['winner'].value_counts()
    
    for m in model_order:
        sub = df[df['model'] == m]
        if len(sub) == 0:
            continue
        avg_eff = sub['eff_pct'].mean()
        gap = 100 - avg_eff
        floor = sub['eff_pct'].min()
        
        # Winner count
        w = 0
        for wname, cnt in winner_counts.items():
            if str(wname).upper() == m:
                w = cnt
                break
        
        dn = display_names.get(m, m)
        print(f"  {dn:30s}  Eff={avg_eff:.2f}%  Gap={gap:.2f}%  Floor={floor:.1f}%  Wins={w}/{total_configs}")
    
    # Find best model
    best_eff_model = max(model_order, key=lambda m: df[df['model']==m]['eff_pct'].mean() if len(df[df['model']==m]) > 0 else 0)
    best_wins = max(model_order, key=lambda m: sum(1 for wname, cnt in winner_counts.items() if str(wname).upper() == m) if len(df[df['model']==m]) > 0 else 0)
    
    best_eff_val = df[df['model']==best_eff_model]['eff_pct'].mean()
    best_wins_count = 0
    for wname, cnt in winner_counts.items():
        if str(wname).upper() == best_wins:
            best_wins_count = cnt
    
    print(f"\n  BEST EFF: {display_names[best_eff_model]} ({best_eff_val:.2f}%)")
    print(f"  BEST WINS: {display_names[best_wins]} ({best_wins_count}/{total_configs} = {100*best_wins_count/total_configs:.0f}%)")
