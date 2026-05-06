import pandas as pd

# Deep dive: Paper 12 vs Internal Hybrid Oracle performance
# Question: What is the theoretical max, and what % does Oracle achieve?
files = {
    'Paper 2': ('Master_Dataset_paper2_4000_2000_5_ST.csv', 8),
    'Paper 7': ('Master_Dataset_paper7_50_50_5_ST.csv', 15),
    'Paper 12': ('Master_Dataset_paper12_1500_500_5_ST.csv', 4),
    'Internal Hybrid': ('Master_Dataset_Hybrid.csv', None),
}

for name, (f, n_paths) in files.items():
    df = pd.read_csv(f)
    oracle = df[(df['model']=='ORACLE') & (df['runs']==5) & (df['allocator']=='Default')]
    
    # For internal, check both T and Tb
    if name == 'Internal Hybrid':
        for cap in ['T', 'Tb']:
            o = oracle[oracle['cap_type']==cap]
            if len(o) == 0:
                continue
            models = df[(df['model']!='ORACLE') & (df['runs']==5) & (df['allocator']=='Default') & (df['cap_type']==cap)]
            print(f"--- {name} (cap={cap}) ---")
            print(f"  Oracle avg_reward: mean={o['avg_reward'].mean():.4f}, min={o['avg_reward'].min():.4f}, max={o['avg_reward'].max():.4f}")
            print(f"  Num paths: {df['num_paths'].iloc[0]}")
            print(f"  Best model eff_pct: {models['eff_pct'].max():.2f}%")
            print(f"  Models eff_pct range: {models['eff_pct'].min():.2f}% - {models['eff_pct'].max():.2f}%")
            # Per model average
            for m in sorted(models['model'].unique()):
                msub = models[models['model']==m]
                print(f"    {m}: avg_eff={msub['eff_pct'].mean():.2f}%, avg_reward={msub['avg_reward'].mean():.4f}")
    else:
        print(f"--- {name} ---")
        print(f"  Num paths: {oracle['num_paths'].iloc[0]}")
        print(f"  Oracle avg_reward: mean={oracle['avg_reward'].mean():.4f}, min={oracle['avg_reward'].min():.4f}, max={oracle['avg_reward'].max():.4f}")
        
        models = df[(df['model']!='ORACLE') & (df['runs']==5) & (df['allocator']=='Default')]
        print(f"  Best model eff_pct: {models['eff_pct'].max():.2f}%")
        print(f"  Models eff_pct range: {models['eff_pct'].min():.2f}% - {models['eff_pct'].max():.2f}%")
        
        # Per-scenario Oracle performance
        print(f"  Oracle per scenario:")
        for scen in sorted(oracle['scenario'].unique()):
            s = oracle[oracle['scenario']==scen]
            print(f"    {scen}: avg_reward={s['avg_reward'].mean():.4f}")
        
        # Per model average
        for m in sorted(models['model'].unique()):
            msub = models[models['model']==m]
            print(f"    {m}: avg_eff={msub['eff_pct'].mean():.2f}%, avg_reward={msub['avg_reward'].mean():.4f}")
    
    print()
