import pandas as pd
import os

# Read the master datasets
datasets = {
    'paper2': 'Master_Dataset_paper2_4000_2000_5_ST.csv',
    'paper7': 'Master_Dataset_paper7_50_50_5_ST.csv', 
    'paper12': 'Master_Dataset_paper12_1500_500_5_ST.csv'
}

print("Finding which scenario each model WON in (was the champion):\n")

for paper, filename in datasets.items():
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
    
    df = pd.read_csv(filename)
    print(f"\n{'='*60}")
    print(f"{paper.upper()}: {filename}")
    print('='*60)
    
    # Get unique models
    models = df['model'].unique()
    
    for model in sorted(models):
        # Find rows where this model was the scenario_winner
        winner_rows = df[df['scenario_winner'] == model]
        
        if len(winner_rows) == 0:
            print(f"{model}: NO WINS")
            continue
        
        # Get unique scenarios where this model won
        winning_scenarios = winner_rows['scenario'].unique()
        
        print(f"\n{model}:")
        for scenario in winning_scenarios:
            scenario_wins = winner_rows[winner_rows['scenario'] == scenario]
            print(f"  Won in scenario: {scenario.upper()} ({len(scenario_wins)} times)")
            # Show example efficiency when they won
            avg_eff = scenario_wins['eff_pct'].mean()
            print(f"    Average efficiency when winning: {avg_eff:.2f}%")

print("\n" + "="*60)
print("SUMMARY: Best Scenario per Model (where they were champion)")
print("="*60)

for paper, filename in datasets.items():
    if not os.path.exists(filename):
        continue
    
    df = pd.read_csv(filename)
    models = df['model'].unique()
    
    print(f"\n{paper.upper()}:")
    for model in sorted(models):
        winner_rows = df[df['scenario_winner'] == model]
        
        if len(winner_rows) == 0:
            print(f"  {model}: NEVER WON")
            continue
        
        # Get the scenario where they won most often or had best performance
        scenario_counts = winner_rows['scenario'].value_counts()
        primary_scenario = scenario_counts.index[0]
        
        print(f"  {model}: {primary_scenario.upper()}")
