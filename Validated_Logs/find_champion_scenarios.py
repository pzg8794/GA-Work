import pandas as pd

# Read the master datasets
datasets = {
    'PAPER2': 'Master_Dataset_paper2_4000_2000_5_ST.csv',
    'PAPER7': 'Master_Dataset_paper7_50_50_5_ST.csv', 
    'PAPER12': 'Master_Dataset_paper12_1500_500_5_ST.csv'
}

print("Finding which scenario each model WON in (was the champion):\n")

# Store best scenario per model per paper
best_scenarios = {}

for paper, filename in datasets.items():
    df = pd.read_csv(filename)
    best_scenarios[paper] = {}
    
    print(f"\n{'='*60}")
    print(f"{paper}")
    print('='*60)
    
    # Get unique scenarios
    scenarios = [s for s in df['scenario'].unique() if s.upper() != 'NONE']
    scenarios.append('NONE')  # Add NONE at the end
    
    # For each model, find which scenario they won
    models = ['CPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB', 'ICPURSUITNEURALUCB']
    
    for model in models:
        # Normalize model name to match scenario_winner format
        model_variants = [
            model,
            'CPursuitNeuralUCB' if model == 'CPURSUITNEURALUCB' else None,
            'GNeuralUCB' if model == 'GNEURALUCB' else None,
            'EXPNeuralUCB' if model == 'EXPNEURALUCB' else None,
            'iCPursuitNeuralUCB' if model == 'ICPURSUITNEURALUCB' else None
        ]
        model_variants = [m for m in model_variants if m is not None]
        
        # Find scenarios where this model was the winner
        winning_scenarios = []
        for scenario in scenarios:
            scenario_df = df[df['scenario'] == scenario]
            # Check if this model was the winner in this scenario
            for variant in model_variants:
                if variant in scenario_df['scenario_winner'].values:
                    winning_scenarios.append(scenario)
                    break
        
        if winning_scenarios:
            # Get the most common winning scenario, or prefer non-NONE
            best_scenario = winning_scenarios[0]
            for ws in winning_scenarios:
                if ws.upper() != 'NONE':
                    best_scenario = ws
                    break
            
            best_scenarios[paper][model] = best_scenario.upper()
            print(f"{model}: {best_scenario.upper()}")
        else:
            best_scenarios[paper][model] = "NEVER WON"
            print(f"{model}: NEVER WON")

print("\n" + "="*60)
print("SUMMARY FOR TABLE:")
print("="*60)

for paper in ['PAPER2', 'PAPER7', 'PAPER12']:
    print(f"\n{paper}:")
    for model in ['CPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB', 'ICPURSUITNEURALUCB']:
        best = best_scenarios.get(paper, {}).get(model, "UNKNOWN")
        print(f"  {model}: {best}")
