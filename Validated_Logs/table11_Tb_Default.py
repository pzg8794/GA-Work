#!/usr/bin/env python3
"""Compute Table 11 with runs=5, cap_type=Tb, Default allocator only for all families."""
import pandas as pd

display_names = {
    'CEPSILONGREEDY': 'CEpsilonGreedy', 'CPURSUIT': 'CPursuit', 'CEXP4': 'CEXP4',
    'CEPOCHGREEDY': 'CEpochGreedy', 'CTHOMPSONSAMPLING': 'CThompsonSampling',
    'ICEPSILONGREEDY': 'iCEpsilonGreedy', 'ICPURSUIT': 'iCPursuit', 'ICEXP4': 'iCEXP4',
    'ICEPOCHGREEDY': 'iCEpochGreedy', 'ICTHOMPSONSAMPLING': 'iCThompsonSampling',
    'ICPURSUITNEURALUCB': 'iCPursuitNeuralUCB', 'CPURSUITNEURALUCB': 'CPursuitNeuralUCB',
    'GNEURALUCB': 'GNeuralUCB', 'EXPNEURALUCB': 'EXPNeuralUCB', 'EXPUCB': 'EXPUCB',
}

families = [
    ('CMABs', 'Master_Dataset_CMABs.csv', ['CPURSUIT','CEPSILONGREEDY','CEXP4','CTHOMPSONSAMPLING','CEPOCHGREEDY']),
    ('iCMABs', 'Master_Dataset_iCMABs.csv', ['ICEPSILONGREEDY','ICPURSUIT','ICTHOMPSONSAMPLING','ICEXP4','ICEPOCHGREEDY']),
    ('Hybrid', 'Master_Dataset_Hybrid.csv', ['ICPURSUITNEURALUCB','CPURSUITNEURALUCB','GNEURALUCB','EXPNEURALUCB']),
    ('EXP3', 'Master_Dataset_EXP3.csv', ['GNEURALUCB','EXPNEURALUCB','EXPUCB']),
]

print("=" * 75)
print("TABLE 11: runs=5, cap_type=Tb, allocator=Default ONLY")
print("=" * 75)

for family, csvfile, model_order in families:
    df = pd.read_csv(csvfile)
    df = df[(df['runs'] == 5) & (df['cap_type'] == 'Tb') & (df['model'] != 'ORACLE') & (df['allocator'] == 'Default')]
    
    scales = sorted(df['scale'].unique())
    n_scenarios = df['scenario'].nunique()
    n_experiments = df['experiment'].nunique()
    
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
    actual_configs = len(configs)
    winner_counts = configs['winner'].value_counts()
    
    print(f"\n--- {family} (Tb, Default, scales {scales}, {actual_configs} configs) ---")
    print(f"    {n_scenarios} scen x 1 alloc x {len(scales)} scales x {n_experiments} exp = {actual_configs}")
    
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
        
        dn = display_names.get(m, m)
        print(f"  {dn:<25} Eff={avg_eff:.2f}%  Gap={gap:.2f}%  Floor={floor:.1f}%  Wins={w}/{actual_configs}")
    
    print(f"  Winner dist: { {str(k): int(v) for k, v in winner_counts.items()} }")
