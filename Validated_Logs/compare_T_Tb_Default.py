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

for family, csvfile, model_order in families:
    df = pd.read_csv(csvfile)
    print(f"\n=== {family} ===")
    for cap in ['T', 'Tb']:
        sub = df[(df['runs']==5) & (df['cap_type']==cap) & (df['model']!='ORACLE') & (df['allocator']=='Default')]
        scales = sorted(sub['scale'].unique())
        configs = sub.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
        print(f"  {cap}: scales={scales}, configs={len(configs)}")

    print(f"  {'Algorithm':<25} {'T Eff%':>7} {'T Win':>7} {'T Flr':>6}  {'Tb Eff%':>8} {'Tb Win':>8} {'Tb Flr':>7}  {'Delta':>6}")
    print(f"  {'-'*72}")

    for m in model_order:
        dn = display_names.get(m, m)
        results = {}
        for cap in ['T', 'Tb']:
            data = df[(df['runs']==5) & (df['cap_type']==cap) & (df['model']==m) & (df['allocator']=='Default')]
            all_data = df[(df['runs']==5) & (df['cap_type']==cap) & (df['model']!='ORACLE') & (df['allocator']=='Default')]
            cfgs = all_data.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
            total = len(cfgs)
            winners = cfgs['winner'].value_counts()
            w = sum(int(v) for k, v in winners.items() if str(k).upper() == m)
            eff = round(data['eff_pct'].mean(), 2) if len(data) > 0 else 0
            flr = round(data['eff_pct'].min(), 1) if len(data) > 0 else 0
            results[cap] = (eff, w, total, flr)

        t_eff, t_w, t_tot, t_flr = results['T']
        tb_eff, tb_w, tb_tot, tb_flr = results['Tb']
        delta = round(tb_eff - t_eff, 2)
        sign = '+' if delta > 0 else ''
        print(f"  {dn:<25} {t_eff:>6.2f}% {t_w:>3}/{t_tot:<3} {t_flr:>5.1f}%  {tb_eff:>7.2f}% {tb_w:>3}/{tb_tot:<3} {tb_flr:>6.1f}%  {sign}{delta:>5.2f}")
