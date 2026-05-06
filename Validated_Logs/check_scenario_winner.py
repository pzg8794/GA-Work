import pandas as pd

# Check what's actually in scenario_winner column
datasets = {
    'paper2': 'Master_Dataset_paper2_4000_2000_5_ST.csv',
    'paper7': 'Master_Dataset_paper7_50_50_5_ST.csv', 
    'paper12': 'Master_Dataset_paper12_1500_500_5_ST.csv'
}

for paper, filename in datasets.items():
    df = pd.read_csv(filename)
    
    print(f"\n{'='*60}")
    print(f"{paper.upper()}: Sample data")
    print('='*60)
    
    # Show first few rows with relevant columns
    cols = ['model', 'scenario', 'scenario_winner', 'scen_winner_eff']
    if all(col in df.columns for col in cols):
        print(df[cols].head(20).to_string())
    
    print(f"\nUnique values in scenario_winner:")
    print(df['scenario_winner'].unique()[:20])
    
    print(f"\nUnique models:")
    print(df['model'].unique())
