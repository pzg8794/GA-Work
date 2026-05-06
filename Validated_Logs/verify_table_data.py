import pandas as pd
import os

base = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'
datasets = {
    'PAPER2': os.path.join(base, 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    'PAPER7': os.path.join(base, 'Master_Dataset_paper7_50_50_5_ST.csv'),
    'PAPER12': os.path.join(base, 'Master_Dataset_paper12_1500_500_5_ST.csv'),
}

non_oracle = lambda df: df[df['model'] != 'ORACLE']

print("="*70)
print("SCENARIO-AGGREGATED METRICS FOR TABLE 10")
print("="*70)

for paper, path in datasets.items():
    df = pd.read_csv(path)
    df_m = non_oracle(df)
    
    print(f"\n{paper}:")
    
    # Scenario-aggregated metrics (means across ALL scenarios, ALL allocators, ALL scales)
    models = ['ORACLE', 'CPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB', 'ICPURSUITNEURALUCB']
    for model in models:
        m = df[df['model'] == model]
        avg_rw = m['avg_reward'].mean()
        regret = m['regret'].mean()
        eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
        gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
        print(f"  {model}: avg_reward={avg_rw:.4f}, regret={regret:.1f}, eff={eff:.2f}%, gap={gap:.2f}%")
    
    print()
    
    # SCENARIO WINNER COUNTS (how many of 5 scenarios each model won)
    # Count: for each scenario, who won the most times?
    scen_detail = df_m.drop_duplicates(subset=['scenario', 'allocator', 'scale', 'experiment'])[['scenario', 'scenario_winner']]
    
    models_mixed = {
        'CPURSUITNEURALUCB': 'CPursuitNeuralUCB',
        'GNEURALUCB': 'GNeuralUCB',
        'EXPNEURALUCB': 'EXPNeuralUCB',
        'ICPURSUITNEURALUCB': 'iCPursuitNeuralUCB'
    }
    
    # Which scenarios does each model win (majority)?
    print(f"  SCENARIO WINNERS (majority per scenario):")
    scenarios = ['NONE', 'STOCHASTIC', 'MARKOV', 'ADAPTIVE', 'ONLINEADAPTIVE']
    for scenario in scenarios:
        subset = scen_detail[scen_detail['scenario'] == scenario]
        tally = subset['scenario_winner'].value_counts()
        winner = tally.index[0]
        # Find all models that appear as winner in this scenario
        participating = tally.index.tolist()
        print(f"    {scenario}: majority={winner} ({tally.iloc[0]}), all participants: {dict(tally)}")
    
    # Count: in how many scenarios does each model appear as winner AT ALL
    print(f"\n  SCENARIO PRESENCE (appears as winner in x/5 scenarios):")
    for model_upper, model_mixed in models_mixed.items():
        won_scenarios = scen_detail[scen_detail['scenario_winner'] == model_mixed]['scenario'].unique()
        print(f"    {model_upper}: {len(won_scenarios)}/5 ({', '.join(sorted(won_scenarios))})")
    
    # Who is the majority winner across all scenarios?
    overall_tally = scen_detail['scenario_winner'].value_counts()
    print(f"\n  OVERALL SCENARIO WINNER: {overall_tally.index[0]} ({overall_tally.iloc[0]} total wins)")
    
    # Experiment-level overall winner
    exp_detail = df_m.drop_duplicates(subset=['experiment', 'scenario', 'allocator', 'scale'])['winner']
    exp_tally = exp_detail.value_counts()
    print(f"  OVERALL EXPERIMENT WINNER: {exp_tally.index[0]} ({exp_tally.iloc[0]}/{exp_tally.sum()} wins)")

print("\n\n" + "="*70)
print("INTERNAL DATASETS (CMABs, iCMABs, Hybrid, EXP3)")
print("="*70)

internal_datasets = {
    'CMABs': os.path.join(base, 'Master_Dataset_CMABs.csv'),
    'iCMABs': os.path.join(base, 'Master_Dataset_iCMABs.csv'),
    'Hybrid': os.path.join(base, 'Master_Dataset_Hybrid.csv'),
    'EXP3': os.path.join(base, 'Master_Dataset_EXP3.csv'),
}

for name, path in internal_datasets.items():
    if not os.path.exists(path):
        print(f"\n{name}: FILE NOT FOUND")
        continue
    df = pd.read_csv(path)
    print(f"\n{name} — shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    print(f"  Unique models: {sorted(df['model'].unique())}")
    if 'scenario' in df.columns:
        print(f"  Unique scenarios: {sorted(df['scenario'].unique())}")
    if 'allocator' in df.columns:
        print(f"  Unique allocators: {sorted(df['allocator'].unique())}")
    if 'scale' in df.columns:
        print(f"  Unique scales: {sorted(df['scale'].unique())}")
    
    # Check for winner column
    for col in ['winner', 'scenario_winner', 'retries', 'failures']:
        if col in df.columns:
            print(f"  {col}: {df[col].unique()[:10]}")
    
    # Show first row
    print(f"  Sample:\n{df.iloc[0].to_dict()}")
