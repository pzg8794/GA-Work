import pandas as pd
import os

base = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'

datasets = {
    'paper2': os.path.join(base, 'Master_Dataset_paper2_4000_2000_5_ST.csv'),
    'paper7': os.path.join(base, 'Master_Dataset_paper7_50_50_5_ST.csv'),
    'paper12': os.path.join(base, 'Master_Dataset_paper12_1500_500_5_ST.csv'),
}

for name, path in datasets.items():
    df = pd.read_csv(path)
    print(f"\n{'='*70}")
    print(f"{name.upper()} — shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nUnique models: {sorted(df['model'].unique())}")
    print(f"Unique scenarios: {sorted(df['scenario'].unique())}")
    print(f"Unique allocators: {sorted(df['allocator'].unique()) if 'allocator' in df.columns else 'N/A'}")
    print(f"Unique scales: {sorted(df['scale'].unique()) if 'scale' in df.columns else 'N/A'}")
    print(f"Unique experiments: {sorted(df['experiment'].unique()) if 'experiment' in df.columns else 'N/A'}")
    
    # Check scenario_winner
    print(f"\nscenario_winner unique: {sorted(df['scenario_winner'].unique()) if 'scenario_winner' in df.columns else 'N/A'}")
    
    # First 3 rows
    print(f"\nSample row:\n{df.iloc[0].to_dict()}")
