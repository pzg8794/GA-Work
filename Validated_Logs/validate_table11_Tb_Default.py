import pandas as pd

expected = {
    'CMABs': {'file': 'Master_Dataset_CMABs.csv', 'entries': [
        ('CPURSUIT', 89.90, 54, 75), ('CEPSILONGREEDY', 88.08, 21, 75),
        ('CEXP4', 70.06, 0, 75), ('CTHOMPSONSAMPLING', 68.16, 0, 75), ('CEPOCHGREEDY', 37.65, 0, 75)]},
    'iCMABs': {'file': 'Master_Dataset_iCMABs.csv', 'entries': [
        ('ICEPSILONGREEDY', 88.56, 75, 75), ('ICPURSUIT', 68.69, 0, 75),
        ('ICTHOMPSONSAMPLING', 68.01, 0, 75), ('ICEXP4', 37.50, 0, 75), ('ICEPOCHGREEDY', 37.57, 0, 75)]},
    'Hybrid': {'file': 'Master_Dataset_Hybrid.csv', 'entries': [
        ('ICPURSUITNEURALUCB', 90.86, 23, 75), ('CPURSUITNEURALUCB', 89.00, 17, 75),
        ('GNEURALUCB', 88.99, 21, 75), ('EXPNEURALUCB', 88.37, 14, 75)]},
    'EXP3': {'file': 'Master_Dataset_EXP3.csv', 'entries': [
        ('GNEURALUCB', 85.37, 41, 75), ('EXPNEURALUCB', 80.86, 28, 75), ('EXPUCB', 78.06, 6, 75)]},
}

mismatches = 0
for fam, info in expected.items():
    df = pd.read_csv(info['file'])
    df = df[(df['runs']==5) & (df['cap_type']=='Tb') & (df['model']!='ORACLE') & (df['allocator']=='Default')]
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
    winners = configs['winner'].value_counts()
    total = len(configs)

    for model, exp_eff, exp_wins, exp_total in info['entries']:
        sub = df[df['model'] == model]
        actual_eff = round(sub['eff_pct'].mean(), 2)
        w = 0
        for wname, cnt in winners.items():
            if str(wname).upper() == model:
                w = cnt
        ok_eff = abs(actual_eff - exp_eff) < 0.015
        ok_wins = (w == exp_wins)
        ok_total = (total == exp_total)
        if not (ok_eff and ok_wins and ok_total):
            print(f'MISMATCH {fam}/{model}: eff={actual_eff} vs {exp_eff}, wins={w} vs {exp_wins}, total={total} vs {exp_total}')
            mismatches += 1

print(f'Validation complete: {mismatches} mismatches out of 17 entries')
