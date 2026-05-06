import pandas as pd

# Check external testbed CSVs for cap_type and allocator availability
files = [
    ('Paper 2', 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    ('Paper 7', 'Master_Dataset_paper7_50_50_5_ST.csv'),
    ('Paper 12', 'Master_Dataset_paper12_1500_500_5_ST.csv'),
]

for name, f in files:
    df = pd.read_csv(f)
    print(f"=== {name} ({f}) ===")
    print(f"  cap_types: {sorted(df['cap_type'].unique())}")
    print(f"  allocators: {sorted(df['allocator'].unique())}")
    print(f"  runs: {sorted(df['runs'].unique())}")
    print(f"  scales: {sorted(df['scale'].unique())}")
    models = [m for m in df['model'].unique() if m != 'ORACLE']
    print(f"  models (non-ORACLE): {models}")
    
    # Check Default + T (what Table 10 currently uses, but with Default only)
    for cap in ['T', 'Tb']:
        sub = df[(df['runs']==5) & (df['cap_type']==cap) & (df['model']!='ORACLE') & (df['allocator']=='Default')]
        if len(sub) == 0:
            print(f"  {cap} + Default: NO DATA")
            continue
        scales = sorted(sub['scale'].unique())
        configs = sub.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
        total = len(configs)
        winners = configs['winner'].value_counts()
        print(f"\n  {cap} + Default: scales={scales}, configs={total}")
        for m in models:
            msub = sub[sub['model'] == m]
            if len(msub) == 0:
                continue
            eff = round(msub['eff_pct'].mean(), 2)
            flr = round(msub['eff_pct'].min(), 1)
            w = sum(int(v) for k, v in winners.items() if str(k).upper() == m.upper())
            print(f"    {m:<25} Eff={eff:.2f}%  Floor={flr:.1f}%  Wins={w}/{total}")
    print()
