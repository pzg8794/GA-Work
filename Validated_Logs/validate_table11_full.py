import pandas as pd

# Validate ALL Table 11 entries: internal (Tb, Default) + external (T, Default)
expected = {
    'CMABs': {'file': 'Master_Dataset_CMABs.csv', 'cap': 'Tb', 'entries': [
        ('CPURSUIT', 89.90, 54, 75), ('CEPSILONGREEDY', 88.08, 21, 75),
        ('CEXP4', 70.06, 0, 75), ('CTHOMPSONSAMPLING', 68.16, 0, 75), ('CEPOCHGREEDY', 37.65, 0, 75)]},
    'iCMABs': {'file': 'Master_Dataset_iCMABs.csv', 'cap': 'Tb', 'entries': [
        ('ICEPSILONGREEDY', 88.56, 75, 75), ('ICPURSUIT', 68.69, 0, 75),
        ('ICTHOMPSONSAMPLING', 68.01, 0, 75), ('ICEXP4', 37.50, 0, 75), ('ICEPOCHGREEDY', 37.57, 0, 75)]},
    'EXP3': {'file': 'Master_Dataset_EXP3.csv', 'cap': 'Tb', 'entries': [
        ('GNEURALUCB', 85.37, 41, 75), ('EXPNEURALUCB', 80.86, 28, 75), ('EXPUCB', 78.06, 6, 75)]},
    'Hybrid': {'file': 'Master_Dataset_Hybrid.csv', 'cap': 'Tb', 'entries': [
        ('ICPURSUITNEURALUCB', 90.86, 23, 75), ('CPURSUITNEURALUCB', 89.00, 17, 75),
        ('GNEURALUCB', 88.99, 21, 75), ('EXPNEURALUCB', 88.37, 14, 75)]},
    'Paper2': {'file': 'Master_Dataset_paper2_4000_2000_5_ST.csv', 'cap': 'T', 'entries': [
        ('ICPURSUITNEURALUCB', 74.43, 24, 75), ('CPURSUITNEURALUCB', 73.22, 8, 75),
        ('GNEURALUCB', 73.21, 23, 75), ('EXPNEURALUCB', 71.28, 20, 75)]},
    'Paper7': {'file': 'Master_Dataset_paper7_50_50_5_ST.csv', 'cap': 'T', 'entries': [
        ('ICPURSUITNEURALUCB', 77.50, 58, 75), ('GNEURALUCB', 70.89, 10, 75),
        ('CPURSUITNEURALUCB', 70.89, 0, 75), ('EXPNEURALUCB', 69.54, 7, 75)]},
    'Paper12': {'file': 'Master_Dataset_paper12_1500_500_5_ST.csv', 'cap': 'T', 'entries': [
        ('ICPURSUITNEURALUCB', 41.55, 26, 75), ('CPURSUITNEURALUCB', 41.19, 13, 75),
        ('GNEURALUCB', 41.13, 14, 75), ('EXPNEURALUCB', 40.18, 22, 75)]},
}

mismatches = 0
total_entries = 0
for fam, info in expected.items():
    df = pd.read_csv(info['file'])
    cap = info['cap']
    df = df[(df['runs']==5) & (df['cap_type']==cap) & (df['model']!='ORACLE') & (df['allocator']=='Default')]
    configs = df.drop_duplicates(subset=['scenario','allocator','scale','experiment'])
    winners = configs['winner'].value_counts()
    total = len(configs)

    for model, exp_eff, exp_wins, exp_total in info['entries']:
        total_entries += 1
        sub = df[df['model'] == model]
        actual_eff = round(sub['eff_pct'].mean(), 2)
        w = sum(int(v) for k, v in winners.items() if str(k).upper() == model.upper())
        ok_eff = abs(actual_eff - exp_eff) < 0.015
        ok_wins = (w == exp_wins)
        ok_total = (total == exp_total)
        if not (ok_eff and ok_wins and ok_total):
            print(f'MISMATCH {fam}/{model}: eff={actual_eff} vs {exp_eff}, wins={w} vs {exp_wins}, total={total} vs {exp_total}')
            mismatches += 1

print(f'Validation complete: {mismatches} mismatches out of {total_entries} entries')
