#!/usr/bin/env python3
import csv

files = {
    'paper7': 'Master_Dataset_paper7_50_50_5_ST.csv',
    'paper12': 'Master_Dataset_paper12_1500_500_5_ST.csv', 
    'paper2': 'Master_Dataset_paper2_4000_2000_5_ST.csv'
}

for paper, fname in files.items():
    print(f'\n{paper.upper()}:')
    with open(fname) as f:
        reader = csv.DictReader(f)
        model_best = {}
        
        for row in reader:
            model = row['model'].upper()
            if model == 'ORACLE':
                continue
            
            scenario = row['scenario']
            eff = float(row.get('eff_pct', row.get('efficiency_pct', 0)))
            
            if model not in model_best or eff > model_best[model][1]:
                model_best[model] = (scenario, eff)
        
        for model in ['CPURSUITNEURALUCB', 'GNEURALUCB', 'ICPURSUITNEURALUCB', 'EXPNEURALUCB']:
            if model in model_best:
                scenario, eff = model_best[model]
                print(f'  {model}: {scenario} ({eff:.2f}%)')
