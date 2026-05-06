import csv
from collections import defaultdict
import os

base_dir = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs/'

papers = {
    'Paper 7': os.path.join(base_dir, 'Master_Dataset_paper7_50_50_5_ST.csv'),
    'Paper 12': os.path.join(base_dir, 'Master_Dataset_paper12_1500_500_5_ST.csv'), 
    'Paper 2': os.path.join(base_dir, 'Master_Dataset_paper2_4000_2000_5_ST.csv')
}

for name, file in papers.items():
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Get unique models
    models = set()
    model_data = defaultdict(lambda: {'eff': [], 'gap': [], 'reward': [], 'regret': [], 'failures': 0})
    
    for row in rows:
        if row['scenario'] == 'NONE':  # Baseline only
            model = row['model']
            models.add(model)
            if model != 'ORACLE':
                try:
                    model_data[model]['eff'].append(float(row['eff_pct']))
                    model_data[model]['gap'].append(float(row['gap_pct']))
                    model_data[model]['reward'].append(float(row['avg_reward']))
                    model_data[model]['regret'].append(float(row['regret']))
                    model_data[model]['failures'] += int(row['failures'])
                except (ValueError, KeyError):
                    pass
    
    print(f"\n{'='*70}")
    print(f"{name}: {file}")
    print(f"{'='*70}")
    print(f"Models (baseline NONE scenario): {sorted(models)}")
    print(f"\nMetrics (averaged across baseline runs):")
    print(f"{'Model':<25} {'Efficiency%':>10} {'Gap%':>10} {'AvgReward':>12} {'Regret':>12} {'Failures':>10}")
    print('-' * 80)
    
    for model in sorted(models):
        if model == 'ORACLE':
            continue
        data = model_data[model]
        if data['eff']:
            avg_eff = sum(data['eff']) / len(data['eff'])
            avg_gap = sum(data['gap']) / len(data['gap'])
            avg_reward = sum(data['reward']) / len(data['reward'])
            avg_regret = sum(data['regret']) / len(data['regret'])
            failures = data['failures']
            print(f"{model:<25} {avg_eff:>10.2f} {avg_gap:>10.2f} {avg_reward:>12.4f} {avg_regret:>12.2f} {failures:>10}")
