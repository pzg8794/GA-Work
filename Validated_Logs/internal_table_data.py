import pandas as pd
import os

base = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'

print("="*70)
print("MODEL FAMILY TABLE DATA (scenario-aggregated, all scales)")
print("="*70)

# CMABs
df = pd.read_csv(os.path.join(base, 'Master_Dataset_CMABs.csv'))
df_m = df[df['model'] != 'ORACLE']
print("\nCMABs:")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    avg_rw = m['avg_reward'].mean()
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    retries = int(m['retries'].sum())
    failures = int(m['failures'].sum())
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}, retries={retries}, failures={failures}")

# Winner info
exp_detail = df_m.drop_duplicates(subset=['experiment', 'scenario', 'scale'])[['experiment', 'winner']]
winner_tally = exp_detail['winner'].value_counts()
print(f"  Overall winner: {winner_tally.to_dict()}")

# iCMABs
df = pd.read_csv(os.path.join(base, 'Master_Dataset_iCMABs.csv'))
df_m = df[df['model'] != 'ORACLE']
print("\niCMABs:")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    retries = int(m['retries'].sum())
    failures = int(m['failures'].sum())
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}, retries={retries}, failures={failures}")

exp_detail = df_m.drop_duplicates(subset=['experiment', 'scenario', 'scale'])[['experiment', 'winner']]
winner_tally = exp_detail['winner'].value_counts()
print(f"  Overall winner: {winner_tally.to_dict()}")

# Hybrid
df = pd.read_csv(os.path.join(base, 'Master_Dataset_Hybrid.csv'))
df_m = df[df['model'] != 'ORACLE']
print("\nHybrid:")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs_vals = m['runs'].unique()
    retries = int(m['retries'].sum())
    failures = int(m['failures'].sum())
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs_vals}, retries={retries}, failures={failures}")

exp_detail = df_m.drop_duplicates(subset=['experiment', 'scenario', 'scale', 'allocator'])[['experiment', 'winner']]
winner_tally = exp_detail['winner'].value_counts()
print(f"  Overall winner: {winner_tally.to_dict()}")

# EXP3
df = pd.read_csv(os.path.join(base, 'Master_Dataset_EXP3.csv'))
df_m = df[df['model'] != 'ORACLE']
print("\nEXP3:")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    retries = int(m['retries'].sum())
    failures = int(m['failures'].sum())
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}, retries={retries}, failures={failures}")

exp_detail = df_m.drop_duplicates(subset=['experiment', 'scenario', 'scale'])[['experiment', 'winner']]
winner_tally = exp_detail['winner'].value_counts()
print(f"  Overall winner: {winner_tally.to_dict()}")

# Now compare: what the table currently says vs what data says
print("\n\n" + "="*70)
print("COMPARISON: CURRENT TABLE vs ACTUAL DATA (Markov, Default only)")
print("="*70)

# CMABs - Markov, Default
df = pd.read_csv(os.path.join(base, 'Master_Dataset_CMABs.csv'))
df_m = df[(df['model'] != 'ORACLE') & (df['scenario'] == 'MARKOV') & (df['allocator'] == 'Default')]
print("\nCMABs (Markov, Default):")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}")

# iCMABs - Markov, Default
df = pd.read_csv(os.path.join(base, 'Master_Dataset_iCMABs.csv'))
df_m = df[(df['model'] != 'ORACLE') & (df['scenario'] == 'MARKOV') & (df['allocator'] == 'Default')]
print("\niCMABs (Markov, Default):")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}")

# Hybrid - Markov, Default
df = pd.read_csv(os.path.join(base, 'Master_Dataset_Hybrid.csv'))
df_m = df[(df['model'] != 'ORACLE') & (df['scenario'] == 'MARKOV') & (df['allocator'] == 'Default')]
print("\nHybrid (Markov, Default):")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs_vals = m['runs'].unique()
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs_vals}")

# EXP3 - Markov, Default
df = pd.read_csv(os.path.join(base, 'Master_Dataset_EXP3.csv'))
df_m = df[(df['model'] != 'ORACLE') & (df['scenario'] == 'MARKOV') & (df['allocator'] == 'Default')]
print("\nEXP3 (Markov, Default):")
for model in sorted(df_m['model'].unique()):
    m = df_m[df_m['model'] == model]
    avg_eff = m['eff_pct'].mean() if not m['eff_pct'].isna().all() else float('nan')
    gap = m['gap_pct'].mean() if not m['gap_pct'].isna().all() else float('nan')
    floor = m['eff_pct'].min() if not m['eff_pct'].isna().all() else float('nan')
    runs = int(m['runs'].iloc[0])
    print(f"  {model}: eff={avg_eff:.2f}%, gap={gap:.2f}%, floor={floor:.1f}%, runs={runs}")

# Compute overall winners for each family across ALL conditions
print("\n\n" + "="*70)
print("OVERALL WINNERS PER FAMILY (all conditions)")
print("="*70)

for name, filename in [('CMABs', 'Master_Dataset_CMABs.csv'), 
                        ('iCMABs', 'Master_Dataset_iCMABs.csv'),
                        ('Hybrid', 'Master_Dataset_Hybrid.csv'),
                        ('EXP3', 'Master_Dataset_EXP3.csv')]:
    df = pd.read_csv(os.path.join(base, filename))
    df_m = df[df['model'] != 'ORACLE']
    
    # Experiment-level winners
    if 'scale' in df.columns:
        exp_detail = df_m.drop_duplicates(subset=[c for c in ['experiment', 'scenario', 'scale', 'allocator'] if c in df.columns])
    else:
        exp_detail = df_m.drop_duplicates(subset=[c for c in ['experiment', 'scenario', 'allocator'] if c in df.columns])
    
    winner_tally = exp_detail['winner'].value_counts()
    total = winner_tally.sum()
    print(f"\n{name}:")
    for w, c in winner_tally.items():
        print(f"  {w}: {c}/{total} wins ({100*c/total:.1f}%)")
