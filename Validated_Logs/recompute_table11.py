import pandas as pd
import numpy as np

# Model name mapping: UPPERCASE -> display name
display_names = {
    'CEPSILONGREEDY': 'CEpsilonGreedy', 'CPURSUIT': 'CPursuit', 'CEXP4': 'CEXP4',
    'CEPOCHGREEDY': 'CEpochGreedy', 'CTHOMPSONSAMPLING': 'CThompsonSampling',
    'ICEPSILONGREEDY': 'iCEpsilonGreedy', 'ICPURSUIT': 'iCPursuit', 'ICEXP4': 'iCEXP4',
    'ICEPOCHGREEDY': 'iCEpochGreedy', 'ICTHOMPSONSAMPLING': 'iCThompsonSampling',
    'ICPURSUITNEURALUCB': 'iCPursuitNeuralUCB', 'CPURSUITNEURALUCB': 'CPursuitNeuralUCB',
    'GNEURALUCB': 'GNeuralUCB', 'EXPNEURALUCB': 'EXPNeuralUCB', 'EXPUCB': 'EXPUCB',
}

for name, f in [('CMABs','Master_Dataset_CMABs.csv'), ('iCMABs','Master_Dataset_iCMABs.csv'), ('Hybrid','Master_Dataset_Hybrid.csv'), ('EXP3','Master_Dataset_EXP3.csv')]:
    df = pd.read_csv(f)
    df = df[df.runs == 5]  # FILTER to runs=5 only
    df_no_oracle = df[df.model != 'ORACLE']
    
    allocs = sorted(df_no_oracle.allocator.unique())
    n_allocs = len(allocs)
    n_scenarios = df_no_oracle.scenario.nunique()
    n_scales = df_no_oracle.scale.nunique()
    n_experiments = df_no_oracle.experiment.nunique()
    n_models = df_no_oracle.model.nunique()
    
    print(f'\n========== {name} (runs=5, {len(df_no_oracle)} non-oracle rows) ==========')
    print(f'  Allocators ({n_allocs}): {allocs}')
    print(f'  Scales: {sorted(df_no_oracle.scale.unique())}')
    print(f'  Configs per model: {n_scenarios} scen x {n_allocs} alloc x {n_scales} scales x {n_experiments} exp = {n_scenarios*n_allocs*n_scales*n_experiments}')
    
    total_configs = n_scenarios * n_allocs * n_scales * n_experiments
    
    # Per-model: avg eff, gap, floor
    print(f'\n  Per-model metrics:')
    for m in sorted(df_no_oracle.model.unique()):
        sub = df_no_oracle[df_no_oracle.model == m]
        avg_eff = sub.eff_pct.mean()
        gap = 100 - avg_eff
        floor = sub.eff_pct.min()
        dn = display_names.get(m, m)
        print(f'  {dn:30s}  Avg Eff={avg_eff:.2f}%  Gap={gap:.2f}%  Floor={floor:.1f}%')
    
    # Experiment winner counts - winner column has model name strings
    print(f'\n  Exp. Winner counts:')
    # Each row has a winner field with the winning model name for that config
    # Count how many configs each model won
    winner_counts = df_no_oracle.groupby('model')['winner'].apply(
        lambda x: (x.str.upper() == x.name).sum()
    )
    # Alternative: just count unique winner values per config
    configs = df_no_oracle.drop_duplicates(subset=['scenario','allocator','scale','experiment'])[['scenario','allocator','scale','experiment','winner']]
    winner_counts2 = configs.winner.value_counts()
    
    for m in sorted(df_no_oracle.model.unique()):
        dn = display_names.get(m, m)
        # Match winner string (mixed case) to model (uppercase)
        # winner column has mixed case names like 'CPursuit', model column has 'CPURSUIT'
        w = 0
        for wname, cnt in winner_counts2.items():
            if str(wname).upper() == m:
                w = cnt
                break
        print(f'    {dn:30s}  {w}/{total_configs}')
    print(f'  Total configs: {total_configs}')
