import pandas as pd
import numpy as np

files = [
    ('Paper 2', 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    ('Paper 7', 'Master_Dataset_paper7_50_50_5_ST.csv'),
    ('Paper 12', 'Master_Dataset_paper12_1500_500_5_ST.csv'),
    ('Internal Hybrid', 'Master_Dataset_Hybrid.csv'),
]

for name, f in files:
    df = pd.read_csv(f)
    print(f"=== {name} ===")
    print(f"  Columns: {list(df.columns)}")
    
    # Get Oracle stats
    oracle = df[(df['model']=='ORACLE') & (df['runs']==5)]
    if 'allocator' in df.columns:
        oracle_def = oracle[oracle['allocator']=='Default']
    else:
        oracle_def = oracle
    
    if len(oracle_def) > 0:
        print(f"  Oracle rows (Default, runs=5): {len(oracle_def)}")
        for col in ['avg_reward', 'eff_pct', 'regret', 'avg_fidelity', 'avg_throughput', 'total_reward']:
            if col in oracle_def.columns:
                vals = oracle_def[col].dropna()
                if len(vals) > 0:
                    print(f"    {col}: mean={vals.mean():.4f}, min={vals.min():.4f}, max={vals.max():.4f}")
    
    # Also check if there's a theoretical max column
    for col in df.columns:
        if 'max' in col.lower() or 'cap' in col.lower() or 'optimal' in col.lower() or 'bound' in col.lower():
            print(f"  Found column: {col} -> unique vals: {df[col].unique()[:10]}")
    
    # Show Oracle eff_pct (should always be ~100%)
    oracle_all = df[(df['model']=='ORACLE') & (df['runs']==5)]
    if 'eff_pct' in oracle_all.columns:
        print(f"  Oracle eff_pct: mean={oracle_all['eff_pct'].mean():.2f}%, min={oracle_all['eff_pct'].min():.2f}%, max={oracle_all['eff_pct'].max():.2f}%")
    
    # Non-oracle best
    non_oracle = df[(df['model']!='ORACLE') & (df['runs']==5) & (df['allocator']=='Default')]
    if 'cap_type' in non_oracle.columns:
        for cap in non_oracle['cap_type'].unique():
            sub = non_oracle[non_oracle['cap_type']==cap]
            print(f"  Best non-Oracle ({cap}, Default): max eff_pct={sub['eff_pct'].max():.2f}%, best avg_reward={sub['avg_reward'].max():.4f}")
    
    print()
