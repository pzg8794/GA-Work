#!/usr/bin/env python3
"""Recompute Table 11 with runs=5 AND cap_type=T. Use actual row counts."""
import pandas as pd

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
    
    allocs = sorted(df['allocator'].unique())
    scales = sorted(df['scale'].unique())
    scenarios = sorted(df['scenario'].unique())
    experiments = sorted(df['experiment'].unique())
    
    # Actual unique configs (experiment = one run for a specific setting)
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
    actual_configs = len(configs)
    winner_counts = configs['winner'].value_counts()
    
    print(f"\n{'='*70}")
    print(f"{family} (runs=5, cap_type=T)")
    print(f"  Rows: {len(df)} non-Oracle, Models: {df['model'].nunique()}")
    print(f"  Allocators ({len(allocs)}): {allocs}")
    print(f"  Scales ({len(scales)}): {scales}")
    print(f"  Scenarios ({len(scenarios)}): {scenarios}")
    print(f"  Experiments: {experiments}")
    print(f"  Actual unique configs: {actual_configs}")
    print(f"  Rows per model:")
    for m in model_order:
        n = len(df[df['model'] == m])
        print(f"    {display_names[m]}: {n}")
    print(f"  Winner counts sum: {winner_counts.sum()}")
    print(f"{'='*70}")
    
    for m in model_order:
        sub = df[df['model'] == m]
        if len(sub) == 0:
            continue
        avg_eff = sub['eff_pct'].mean()
        gap = 100 - avg_eff
        floor = sub['eff_pct'].min()
        
        w = 0
        for wname, cnt in winner_counts.items():
            if str(wname).upper() == m:
                w = cnt
                break
        
        dn = display_names.get(m, m)
        print(f"  {dn:30s}  Eff={avg_eff:.2f}%  Gap={gap:.2f}%  Floor={floor:.1f}%  Wins={w}/{actual_configs}")
    
    print(f"\n  Winner total check: {winner_counts.to_dict()}")
