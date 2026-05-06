import pandas as pd
import os

base = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'

# The current table says Markov + Default + scale=1.0?
# Let's try to match the current values to find the filter

# CMABs: table says CEpsilonGreedy=85.05, CPursuit=83.27, CEXP4=67.61, CEpochGreedy=36.93, CThompsonSampling=62.99
df = pd.read_csv(os.path.join(base, 'Master_Dataset_CMABs.csv'))
df_m = df[df['model'] != 'ORACLE']

# Try Markov only, scale=1.0
print("CMABs Markov, Default, scale=1.0:")
subset = df_m[(df_m['scenario'] == 'MARKOV') & (df_m['allocator'] == 'Default') & (df_m['scale'] == 1.0)]
for model in sorted(subset['model'].unique()):
    m = subset[subset['model'] == model]
    print(f"  {model}: eff={m['eff_pct'].mean():.2f}%, runs={int(m['runs'].iloc[0])}")

print("\nCMABs all scenarios, Default, scale=1.0:")
subset = df_m[(df_m['allocator'] == 'Default') & (df_m['scale'] == 1.0)]
for model in sorted(subset['model'].unique()):
    m = subset[subset['model'] == model]
    print(f"  {model}: eff={m['eff_pct'].mean():.2f}%")

# The table says runs=5 for CMABs but data has runs=3
# Maybe there's an older 5-run dataset?
print("\nCMABs all runs values:", df['runs'].unique())

# For Hybrid, table says iCPursuitNeuralUCB=92.60, CPursuitNeuralUCB=92.47, GNeuralUCB=87.82
# Try Markov, Default, 3 runs only
df = pd.read_csv(os.path.join(base, 'Master_Dataset_Hybrid.csv'))
df_m = df[df['model'] != 'ORACLE']
print("\nHybrid Markov, Default, scale=1.0:")
subset = df_m[(df_m['scenario'] == 'MARKOV') & (df_m['allocator'] == 'Default') & (df_m['scale'] == 1.0)]
for model in sorted(subset['model'].unique()):
    m = subset[subset['model'] == model]
    print(f"  {model}: eff={m['eff_pct'].mean():.2f}%, runs={m['runs'].unique()}")

# EXP3
df = pd.read_csv(os.path.join(base, 'Master_Dataset_EXP3.csv'))
df_m = df[df['model'] != 'ORACLE'] 
print("\nEXP3 Markov, Default, scale=1.0:")
subset = df_m[(df_m['scenario'] == 'MARKOV') & (df_m['allocator'] == 'Default') & (df_m['scale'] == 1.0)]
for model in sorted(subset['model'].unique()):
    m = subset[subset['model'] == model]
    print(f"  {model}: eff={m['eff_pct'].mean():.2f}%, runs={int(m['runs'].iloc[0])}")

# Try scale=1.0 for CMABs Markov Default - maybe with specific experiment?
df = pd.read_csv(os.path.join(base, 'Master_Dataset_CMABs.csv'))
df_m = df[(df['model'] != 'ORACLE') & (df['scenario'] == 'MARKOV') & (df['allocator'] == 'Default') & (df['scale'] == 1.0)]
print("\n\nCMABs Markov, Default, scale=1.0 per experiment:")
for exp in sorted(df_m['experiment'].unique()):
    e = df_m[df_m['experiment'] == exp]
    print(f"\n  Experiment {exp}:")
    for model in sorted(e['model'].unique()):
        m = e[e['model'] == model]
        print(f"    {model}: eff={m['eff_pct'].values[0]:.2f}%, runs={int(m['runs'].iloc[0])}")

# Check: table has CEpsilonGreedy 85.05% - is that experiment 1 only?
ceg = df_m[df_m['model'] == 'CEPSILONGREEDY']
for exp in sorted(ceg['experiment'].unique()):
    e = ceg[ceg['experiment'] == exp]
    print(f"\n  CEpsilonGreedy exp {exp}: eff={e['eff_pct'].values[0]:.2f}%")
