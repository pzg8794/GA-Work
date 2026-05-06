import pandas as pd

cmab = pd.read_csv('Master_Dataset_CMABs.csv')
icmab = pd.read_csv('Master_Dataset_iCMABs.csv')
hybrid = pd.read_csv('Master_Dataset_Hybrid.csv')
exp3 = pd.read_csv('Master_Dataset_EXP3.csv')

# Test different source datasets for Table 5 models
tests = [
    ('GNeuralUCB', 'Hybrid', hybrid, 'GNEURALUCB'),
    ('GNeuralUCB', 'EXP3', exp3, 'GNEURALUCB'),
    ('EXPNeuralUCB', 'Hybrid', hybrid, 'EXPNEURALUCB'),
    ('EXPNeuralUCB', 'EXP3', exp3, 'EXPNEURALUCB'),
    ('iCEpsilonGreedy', 'iCMABs', icmab, 'ICEPSILONGREEDY'),
    ('iCPursuit', 'iCMABs', icmab, 'ICPURSUIT'),
    ('CThompsonSampling', 'CMABs', cmab, 'CTHOMPSONSAMPLING'),
    ('iCThompsonSampling', 'iCMABs', icmab, 'ICTHOMPSONSAMPLING'),
]

print("=== Table 5 Stochastic values with different filters ===\n")
for name, ds_name, ds, upper in tests:
    print(f"--- {name} from {ds_name} ---")
    for runs_val in [5, 3, None]:
        for alloc_filter in ['Default', None]:
            sub = ds[(ds.model == upper) & (ds.scenario == 'STOCHASTIC')]
            if runs_val:
                sub = sub[sub.runs == runs_val]
            if alloc_filter:
                sub = sub[sub.allocator == alloc_filter]
            if len(sub) > 0:
                avg = sub.eff_pct.mean()
                runs_label = f"runs={runs_val}" if runs_val else "all runs"
                alloc_label = alloc_filter if alloc_filter else "all allocs"
                print(f"  {runs_label}, {alloc_label}: {avg:.2f}% (n={len(sub)})")
    print()
