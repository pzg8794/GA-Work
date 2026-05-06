#!/usr/bin/env python3
"""Compute Table 11 with runs=5 AND cap_type=Tb only."""
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

print(f"{'Family':<12} {'Algorithm':<25} {'Eff%':>7} {'Gap%':>7} {'Floor%':>7} {'Wins':>10}")
print("=" * 75)

for family, csvfile, model_order in families:
    df = pd.read_csv(csvfile)
    df = df[(df['runs'] == 5) & (df['cap_type'] == 'Tb') & (df['model'] != 'ORACLE')]
    
    scales = sorted(df['scale'].unique())
    allocs = sorted(df['allocator'].unique())
    
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
    actual_configs = len(configs)
    winner_counts = configs['winner'].value_counts()
    
    print(f"\n--- {family} (Tb, {len(allocs)} alloc, scales {scales}, {actual_configs} configs) ---")
    
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
        print(f"  {dn:<25} {avg_eff:>7.2f} {gap:>7.2f} {floor:>7.1f} {w:>4}/{actual_configs}")

# Now print side-by-side comparison T vs Tb
print("\n\n" + "=" * 90)
print("SIDE-BY-SIDE: T vs Tb")
print("=" * 90)
print(f"{'Family':<10} {'Algorithm':<22} {'T Eff%':>7} {'Tb Eff%':>8} {'Diff':>6} {'T Wins':>8} {'Tb Wins':>9}")
print("-" * 90)

for family, csvfile, model_order in families:
    df = pd.read_csv(csvfile)
    df_r5 = df[(df['runs'] == 5) & (df['model'] != 'ORACLE')]
    
    for cap in ['T', 'Tb']:
        sub_cap = df_r5[df_r5['cap_type'] == cap]
        configs = sub_cap.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
        globals()[f'wc_{cap}'] = configs['winner'].value_counts()
        globals()[f'denom_{cap}'] = len(configs)
    
    for m in model_order:
        dn = display_names.get(m, m)
        
        t_sub = df_r5[(df_r5['cap_type'] == 'T') & (df_r5['model'] == m)]
        tb_sub = df_r5[(df_r5['cap_type'] == 'Tb') & (df_r5['model'] == m)]
        
        t_eff = t_sub['eff_pct'].mean() if len(t_sub) > 0 else 0
        tb_eff = tb_sub['eff_pct'].mean() if len(tb_sub) > 0 else 0
        diff = tb_eff - t_eff
        
        t_w = sum(cnt for wname, cnt in wc_T.items() if str(wname).upper() == m)
        tb_w = sum(cnt for wname, cnt in wc_Tb.items() if str(wname).upper() == m)
        
        print(f"  {dn:<22} {t_eff:>7.2f} {tb_eff:>8.2f} {diff:>+6.1f} {t_w:>3}/{denom_T:<4} {tb_w:>3}/{denom_Tb}")
    print()
