import pandas as pd
import os

base = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'
datasets = {
    'PAPER2': os.path.join(base, 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    'PAPER7': os.path.join(base, 'Master_Dataset_paper7_50_50_5_ST.csv'),
    'PAPER12': os.path.join(base, 'Master_Dataset_paper12_1500_500_5_ST.csv'),
}

non_oracle = lambda df: df[df['model'] != 'ORACLE']

for paper, path in datasets.items():
    df = pd.read_csv(path)
    df_m = non_oracle(df)
    
    print(f"\n{'#'*70}")
    print(f"  {paper}")
    print(f"{'#'*70}")

    # ========== 1. EXPERIMENT LEVEL ==========
    print(f"\n--- EXPERIMENT LEVEL (winner per experiment) ---")
    # The 'winner' column already has the experiment-level winner
    exp_winners = df_m.groupby('experiment')['winner'].first().reset_index()
    print(exp_winners.to_string(index=False))
    
    # Overall experiment winner: who wins the most experiments?
    exp_winner_counts = df_m.drop_duplicates(subset=['experiment', 'scenario', 'allocator', 'scale'])[['experiment','winner']]
    exp_tally = exp_winner_counts['winner'].value_counts()
    print(f"\nExperiment win tally:")
    print(exp_tally.to_string())
    overall_exp_winner = exp_tally.index[0]
    print(f">> OVERALL EXPERIMENT WINNER: {overall_exp_winner} ({exp_tally.iloc[0]} wins)")

    # ========== 2. SCENARIO LEVEL ==========
    print(f"\n--- SCENARIO LEVEL (winner per scenario) ---")
    # scenario_winner column: who won each scenario
    scen_winners = df_m.groupby('scenario')['scenario_winner'].first().reset_index()
    # But scenario_winner is per (scenario, allocator, scale, experiment) combo
    # Let's count wins per scenario
    scen_detail = df_m.drop_duplicates(subset=['scenario', 'allocator', 'scale', 'experiment'])[['scenario', 'scenario_winner']]
    for scenario in sorted(df['scenario'].unique()):
        subset = scen_detail[scen_detail['scenario'] == scenario]
        tally = subset['scenario_winner'].value_counts()
        print(f"\n  {scenario}:")
        print(f"  {tally.to_string()}")
        print(f"  >> SCENARIO WINNER: {tally.index[0]} ({tally.iloc[0]} wins)")

    # Overall scenario winner
    overall_scen_tally = scen_detail['scenario_winner'].value_counts()
    print(f"\nOverall scenario win tally:")
    print(overall_scen_tally.to_string())
    print(f">> OVERALL SCENARIO WINNER: {overall_scen_tally.index[0]} ({overall_scen_tally.iloc[0]} wins)")

    # ========== 3. ALLOCATOR LEVEL ==========
    print(f"\n--- ALLOCATOR LEVEL (winner per allocator) ---")
    alloc_detail = df_m.drop_duplicates(subset=['allocator', 'scenario', 'scale', 'experiment'])[['allocator', 'winner']]
    for alloc in sorted(df['allocator'].unique()):
        subset = alloc_detail[alloc_detail['allocator'] == alloc]
        tally = subset['winner'].value_counts()
        print(f"\n  {alloc}:")
        print(f"  {tally.to_string()}")
        print(f"  >> ALLOCATOR WINNER: {tally.index[0]} ({tally.iloc[0]} wins)")
    
    overall_alloc_tally = alloc_detail['winner'].value_counts()
    print(f"\nOverall allocator win tally:")
    print(overall_alloc_tally.to_string())
    print(f">> OVERALL ALLOCATOR WINNER: {overall_alloc_tally.index[0]} ({overall_alloc_tally.iloc[0]} wins)")

    # ========== 4. CAPACITY (SCALE) LEVEL ==========
    print(f"\n--- CAPACITY (SCALE) LEVEL (winner per scale) ---")
    scale_detail = df_m.drop_duplicates(subset=['scale', 'scenario', 'allocator', 'experiment'])[['scale', 'winner']]
    for scale in sorted(df['scale'].unique()):
        subset = scale_detail[scale_detail['scale'] == scale]
        tally = subset['winner'].value_counts()
        print(f"\n  Scale={scale}:")
        print(f"  {tally.to_string()}")
        print(f"  >> SCALE WINNER: {tally.index[0]} ({tally.iloc[0]} wins)")
    
    overall_scale_tally = scale_detail['winner'].value_counts()
    print(f"\nOverall scale win tally:")
    print(overall_scale_tally.to_string())
    print(f">> OVERALL SCALE WINNER: {overall_scale_tally.index[0]} ({overall_scale_tally.iloc[0]} wins)")

    # ========== GRAND OVERALL WINNER ==========
    all_wins = df_m.drop_duplicates(subset=['experiment', 'scenario', 'allocator', 'scale'])['winner'].value_counts()
    print(f"\n{'='*50}")
    print(f"GRAND OVERALL WINNER for {paper}:")
    print(all_wins.to_string())
    print(f">> {all_wins.index[0]} ({all_wins.iloc[0]} total wins)")
    print(f"{'='*50}")

# ========== ALSO: Best scenario per model (champion) ==========
print(f"\n\n{'#'*70}")
print(f"  BEST SCENARIO PER MODEL (where each model was champion)")
print(f"{'#'*70}")

for paper, path in datasets.items():
    df = pd.read_csv(path)
    df_m = non_oracle(df)
    
    print(f"\n{paper}:")
    models_map = {
        'CPURSUITNEURALUCB': 'CPursuitNeuralUCB',
        'GNEURALUCB': 'GNeuralUCB', 
        'EXPNEURALUCB': 'EXPNeuralUCB',
        'ICPURSUITNEURALUCB': 'iCPursuitNeuralUCB'
    }
    
    scen_detail = df_m.drop_duplicates(subset=['scenario', 'allocator', 'scale', 'experiment'])[['scenario', 'scenario_winner']]
    
    for model_upper, model_mixed in models_map.items():
        won = scen_detail[scen_detail['scenario_winner'] == model_mixed]
        if len(won) > 0:
            best_scen = won['scenario'].value_counts()
            print(f"  {model_upper}: champion in {', '.join(best_scen.index)} (total {len(won)} wins)")
        else:
            print(f"  {model_upper}: never won any scenario")

# ========== TABLE DATA: Baseline metrics + Best Scenario + Overall Winner ==========
print(f"\n\n{'#'*70}")
print(f"  TABLE DATA FOR LATEX")
print(f"{'#'*70}")

for paper, path in datasets.items():
    df = pd.read_csv(path)
    df_m = non_oracle(df)
    
    print(f"\n{paper}:")
    
    # Find the allocator used in the table
    # Paper 2: ThompsonSampling, scale=1.5
    # Paper 7: Default, scale=2.0  
    # Paper 12: Default, scale=1.0
    if paper == 'PAPER2':
        baseline = df[(df['scenario'] == 'NONE') & (df['allocator'] == 'ThompsonSampling') & (df['scale'] == 1.5)]
    elif paper == 'PAPER7':
        baseline = df[(df['scenario'] == 'NONE') & (df['allocator'] == 'Default') & (df['scale'] == 2.0)]
    else:  # PAPER12
        baseline = df[(df['scenario'] == 'NONE') & (df['allocator'] == 'Default') & (df['scale'] == 1.0)]
    
    models = ['ORACLE', 'CPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB', 'ICPURSUITNEURALUCB']
    for model in models:
        m = baseline[baseline['model'] == model]
        if len(m) > 0:
            avg_rw = m['avg_reward'].mean()
            regret = m['regret'].mean()
            eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
            gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
            print(f"  {model}: avg_reward={avg_rw:.4f}, regret={regret:.1f}, eff={eff:.2f}%, gap={gap:.2f}%")
    
    # Overall winner for this testbed
    all_wins = df_m.drop_duplicates(subset=['experiment', 'scenario', 'allocator', 'scale'])['winner'].value_counts()
    print(f"  Overall Winner: {all_wins.index[0]} ({all_wins.iloc[0]}/{all_wins.sum()} wins)")
