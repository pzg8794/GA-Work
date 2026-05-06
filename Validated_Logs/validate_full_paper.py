#!/usr/bin/env python3
"""Validate ALL paper claims beyond Tables 10/11 against master CSVs."""
import pandas as pd
import numpy as np

BASE = '/Users/pitergarcia/DataScience/Semester4/GA-Work/Validated_Logs'
discrepancies = []

# Load all datasets
cmab = pd.read_csv(f"{BASE}/Master_Dataset_CMABs.csv")
icmab = pd.read_csv(f"{BASE}/Master_Dataset_iCMABs.csv")
hybrid = pd.read_csv(f"{BASE}/Master_Dataset_Hybrid.csv")
exp3 = pd.read_csv(f"{BASE}/Master_Dataset_EXP3.csv")
p2 = pd.read_csv(f"{BASE}/Master_Dataset_paper2_4000_2000_5_ST.csv")
p7 = pd.read_csv(f"{BASE}/Master_Dataset_paper7_50_50_5_ST.csv")
p12 = pd.read_csv(f"{BASE}/Master_Dataset_paper12_1500_500_5_ST.csv")

# Combine internal datasets for "corpus" analysis
all_internal = pd.concat([cmab, icmab, hybrid, exp3], ignore_index=True)

print("=" * 80)
print("1. MODEL COUNT VALIDATION")
print("=" * 80)
all_models_internal = set()
for df in [cmab, icmab, hybrid, exp3]:
    all_models_internal.update(df[df.model != 'ORACLE'].model.unique())
print(f"  Unique non-Oracle models across internal datasets: {len(all_models_internal)}")
print(f"  Models: {sorted(all_models_internal)}")
# Paper claims: Abstract says "13 algorithms", Intro says "16 models (15+Oracle)", 
# Algorithm portfolio says "14 algorithms + Oracle"
# Count: 5 CMAB + 5 iCMAB + 4 Hybrid + 3 EXP3 = 17, but some overlap (GNeuralUCB, EXPNeuralUCB)
unique = all_models_internal
print(f"  Unique model names: {len(unique)}")
if len(unique) != 13 and len(unique) != 15 and len(unique) != 14:
    discrepancies.append(f"  ❌ MODEL COUNT: Paper says 13/14/15/16 in different places, CSV has {len(unique)} unique non-Oracle models")

print("\n" + "=" * 80)
print("2. SCENARIO CHAMPION CLAIMS (Key Observations)")
print("=" * 80)

# Paper 2 claim: "iCP wins 2/5 scenarios (none, markov)"
# Paper 2 claim: "CP and G each win 3/5 (adaptive, onlineadaptive, stochastic)"
print("\n--- Paper 2 scenario winners ---")
p2_no = p2[p2.model != 'ORACLE']
for scen in sorted(p2_no.scenario.unique()):
    sw = p2_no[p2_no.scenario == scen].scenario_winner.dropna().unique()
    print(f"  {scen}: {sorted(sw)}")

# Check: does iCP win NONE alone? CSV shows NONE has both iCPursuitNeuralUCB AND EXPNeuralUCB
none_sw = sorted(p2_no[p2_no.scenario == 'NONE'].scenario_winner.dropna().unique())
if len(none_sw) > 1:
    discrepancies.append(f"  ⚠️  Paper 2 NONE scenario: paper says iCP wins alone, but CSV shows winners = {none_sw}")

# Paper 12 claim: "markov uniquely iCPursuitNeuralUCB (60/60 wins)"
print("\n--- Paper 12 MARKOV experiment winners ---")
p12_no = p12[p12.model != 'ORACLE']
markov_configs = p12_no[p12_no.scenario == 'MARKOV'].drop_duplicates(
    subset=['allocator','scale','experiment'])[['allocator','scale','experiment','winner']]
wc = markov_configs.winner.value_counts()
print(f"  Total markov configs: {len(markov_configs)}")
for w, c in wc.items():
    print(f"  {w}: {c}/{len(markov_configs)}")
icp_markov_wins = wc.get('iCPursuitNeuralUCB', 0)
if icp_markov_wins != 60:
    discrepancies.append(f"  ❌ Paper 12 MARKOV: paper says iCP wins 60/60, CSV shows {icp_markov_wins}/{len(markov_configs)}")

print("\n" + "=" * 80)
print("3. ABSTRACT / INTRO EFFICIENCY CLAIMS")
print("=" * 80)

# "pursuit-neural hybrids achieve 86-89% oracle-normalized efficiency on average"
hybrid5 = hybrid[hybrid.runs == 5]
hybrid5_no = hybrid5[hybrid5.model != 'ORACLE']
pursuit_models = hybrid5_no[hybrid5_no.model.isin(['ICPURSUITNEURALUCB','CPURSUITNEURALUCB'])]
pursuit_avg = pursuit_models.eff_pct.mean()
all_hybrid_avg = hybrid5_no.eff_pct.mean()
print(f"  Pursuit-neural avg (iCP+CP, runs=5): {pursuit_avg:.1f}%")
print(f"  All hybrid avg (runs=5): {all_hybrid_avg:.1f}%")
if not (86 <= pursuit_avg <= 89):
    discrepancies.append(f"  ⚠️  Abstract: 'pursuit-neural hybrids achieve 86-89%' — CSV pursuit avg = {pursuit_avg:.1f}%")

# "outperform non-contextual baselines by 18-24 pp"
# non-contextual = EXP3 family
exp3_5 = exp3[exp3.runs == 5]
exp3_no = exp3_5[exp3_5.model != 'ORACLE']
exp3_avg = exp3_no.eff_pct.mean()
gap_pursuit_exp3 = pursuit_avg - exp3_avg
print(f"  EXP3 avg (runs=5): {exp3_avg:.1f}%")
print(f"  Pursuit - EXP3 gap: {gap_pursuit_exp3:.1f} pp")
# Actually the 18-24pp might refer to all internal data, not just runs=5
pursuit_all = hybrid[hybrid.model.isin(['ICPURSUITNEURALUCB','CPURSUITNEURALUCB']) & (hybrid.model != 'ORACLE')]
exp3_all = exp3[exp3.model != 'ORACLE']
gap_all = pursuit_all.eff_pct.mean() - exp3_all.eff_pct.mean()
print(f"  Pursuit - EXP3 gap (all runs): {gap_all:.1f} pp")

# Cross-testbed: "69.6-78.0% on Papers 2/7"
p2_eff_range = (p2_no.groupby('model').eff_pct.mean().min(), p2_no.groupby('model').eff_pct.mean().max())
p7_no = p7[p7.model != 'ORACLE']
p7_eff_range = (p7_no.groupby('model').eff_pct.mean().min(), p7_no.groupby('model').eff_pct.mean().max())
print(f"  Paper 2 eff range: {p2_eff_range[0]:.1f}% - {p2_eff_range[1]:.1f}%")
print(f"  Paper 7 eff range: {p7_eff_range[0]:.1f}% - {p7_eff_range[1]:.1f}%")
combined_min = min(p2_eff_range[0], p7_eff_range[0])
combined_max = max(p2_eff_range[1], p7_eff_range[1])
print(f"  Combined P2+P7 range: {combined_min:.1f}% - {combined_max:.1f}%")
# Paper says "69.6-78.0%"
if abs(combined_min - 69.6) > 0.5 or abs(combined_max - 78.0) > 0.5:
    discrepancies.append(f"  ⚠️  Abstract: 'cross-testbed 69.6-78.0% on Papers 2/7' — CSV range = {combined_min:.1f}-{combined_max:.1f}%")

# "42.5-44.1% on Paper 12"
p12_eff_range = (p12_no.groupby('model').eff_pct.mean().min(), p12_no.groupby('model').eff_pct.mean().max())
print(f"  Paper 12 eff range: {p12_eff_range[0]:.1f}% - {p12_eff_range[1]:.1f}%")

print("\n" + "=" * 80)
print("4. TABLE 5 (RQ1 Stochastic) - 5-run column")
print("=" * 80)
# Table 5 shows per-model stochastic efficiency at 3-run and 5-run
# Let's validate 5-run stochastic efficiency from internal datasets
table5_claims_5run = {
    'CPursuit': ('CMABs', 90.1),
    'iCEpsilonGreedy': ('iCMABs', 88.6),
    'CEpsilonGreedy': ('CMABs', 87.9),
    'GNeuralUCB': ('Hybrid', 86.3),  # or EXP3?
    'EXPNeuralUCB': ('Hybrid', 83.8),
    'EXPUCB': ('EXP3', 78.4),
    'CEXP4': ('CMABs', 70.2),
    'iCPursuit': ('iCMABs', 69.0),
    'CThompsonSampling': ('CMABs', 68.1),
    'iCThompsonSampling': ('iCMABs', 68.0),
    'CEpochGreedy': ('CMABs', 37.6),
    'iCEpochGreedy': ('iCMABs', 37.5),
    'iCEXP4': ('iCMABs', 37.4),
}

dataset_map = {'CMABs': cmab, 'iCMABs': icmab, 'Hybrid': hybrid, 'EXP3': exp3}
model_upper = {
    'CPursuit': 'CPURSUIT', 'iCEpsilonGreedy': 'ICEPSILONGREEDY', 'CEpsilonGreedy': 'CEPSILONGREEDY',
    'GNeuralUCB': 'GNEURALUCB', 'EXPNeuralUCB': 'EXPNEURALUCB', 'EXPUCB': 'EXPUCB',
    'CEXP4': 'CEXP4', 'iCPursuit': 'ICPURSUIT', 'CThompsonSampling': 'CTHOMPSONSAMPLING',
    'iCThompsonSampling': 'ICTHOMPSONSAMPLING', 'CEpochGreedy': 'CEPOCHGREEDY',
    'iCEpochGreedy': 'ICEPOCHGREEDY', 'iCEXP4': 'ICEXP4',
}

for name, (ds_name, claimed_val) in table5_claims_5run.items():
    ds = dataset_map[ds_name]
    upper = model_upper[name]
    sub = ds[(ds.runs == 5) & (ds.model == upper) & (ds.scenario == 'STOCHASTIC')]
    if len(sub) == 0:
        discrepancies.append(f"  ❌ Table 5/{name}: No data for {upper} in {ds_name}, runs=5, STOCHASTIC")
        continue
    csv_val = sub.eff_pct.mean()
    diff = abs(claimed_val - csv_val)
    if diff > 0.15:
        discrepancies.append(f"  ❌ Table 5/{name} (5-run stochastic): paper={claimed_val}, CSV={csv_val:.1f}, diff={diff:.1f}")
    else:
        print(f"  ✅ {name}: paper={claimed_val}, CSV={csv_val:.2f}")

print("\n" + "=" * 80)
print("5. TABLE 6 (RQ2 Adversarial) - Selected models")
print("=" * 80)
# Table 6: CPursuit adversarial avg 88.1%, iCEpsGreedy 86.9%, EXPNeuralUCB 82.4%, EXPUCB 76.3%
# "Adversarial" likely = all non-baseline scenarios (Stochastic, Markov, Adaptive, OA)
# Let's check averages for runs=5 across adversarial scenarios
adversarial_scenarios = ['STOCHASTIC', 'MARKOV', 'ADAPTIVE', 'ONLINEADAPTIVE']

table6_claims = {
    'CPursuit': ('CMABs', 'CPURSUIT', 88.1, 5.3, 77.4, 31.5),
    'iCEpsilonGreedy': ('iCMABs', 'ICEPSILONGREEDY', 86.9, 3.6, 81.0, 25.0),
    'EXPNeuralUCB': ('EXP3', 'EXPNEURALUCB', 82.4, 16.5, 18.0, 11.1),
    'EXPUCB': ('EXP3', 'EXPUCB', 76.3, 6.0, 68.8, 0.0),
}

for name, (ds_name, upper, avg_claim, cv_claim, floor_claim, ws_claim) in table6_claims.items():
    ds = dataset_map[ds_name]
    # Try both all runs and runs=5
    for run_filter, run_label in [(None, 'all'), (5, 'runs=5'), (3, 'runs=3')]:
        sub = ds[(ds.model == upper) & (ds.scenario.isin(adversarial_scenarios))]
        if run_filter:
            sub = sub[sub.runs == run_filter]
        if len(sub) == 0:
            continue
        csv_avg = sub.eff_pct.mean()
        csv_floor = sub.eff_pct.min()
        csv_cv = (sub.eff_pct.std() / sub.eff_pct.mean()) * 100
        diff = abs(avg_claim - csv_avg)
        label = f"Table6/{name} ({run_label} adv)"
        if diff < 0.5:
            print(f"  ✅ {label}: avg paper={avg_claim}, CSV={csv_avg:.1f}, floor paper={floor_claim}, CSV={csv_floor:.1f}")
            break
    else:
        discrepancies.append(f"  ⚠️  Table6/{name}: avg paper={avg_claim}, CSV best match not found within 0.5")

print("\n" + "=" * 80)
print("6. FIGURE 7 WIN SHARE VALIDATION")
print("=" * 80)
# Paper claims: CPursuit 27.8%, iCEpsGreedy 37.5%, GNeuralUCB 11.9%, EXPNeuralUCB 11.6%
# Win share likely from Default allocator across all families
# Let's compute global win share

# Combine all internal data, Default allocator
all_default = all_internal[(all_internal.allocator == 'Default') & (all_internal.model != 'ORACLE')]
configs = all_default.drop_duplicates(subset=['scenario','scale','experiment','runs','model'])[['scenario','scale','experiment','runs','winner']]
# Actually, winner is per experiment config (scenario, allocator, scale, experiment, runs)
# Need unique configs = (scenario, allocator, scale, experiment, runs) — one winner per config
unique_configs = all_default.drop_duplicates(subset=['scenario','allocator','scale','experiment','runs'])
total_unique = len(unique_configs)
wc = {}
for _, row in unique_configs.iterrows():
    w = str(row['winner'])
    wc[w] = wc.get(w, 0) + 1

print(f"  Total unique configs (Default alloc, all internal): {total_unique}")
for model in sorted(wc.keys(), key=lambda x: wc[x], reverse=True):
    share = wc[model] / total_unique * 100
    print(f"  {model:30s}  {wc[model]}/{total_unique} = {share:.1f}%")

print("\n" + "=" * 80)
print("7. PHYSICAL PARAMETERS VALIDATION")
print("=" * 80)
# Paper 2: p_BSM=0.2, p_depol=0.1, p_gate=0.2, p_init=1e-5, att=0.05
# Check what columns we have
phys_cols = [c for c in p2.columns if 'phys' in c.lower() or 'prob' in c.lower() or 'bsm' in c.lower() or 'depol' in c.lower() or 'gate' in c.lower() or 'att' in c.lower() or 'init' in c.lower() or 'fusion' in c.lower()]
print(f"  Paper 2 physics columns: {phys_cols}")
for c in phys_cols:
    vals = p2[c].unique()
    print(f"    {c}: {vals}")

phys_cols_12 = [c for c in p12.columns if 'phys' in c.lower() or 'fusion' in c.lower() or 'q_' in c.lower()]
print(f"  Paper 12 physics columns: {phys_cols_12}")
for c in phys_cols_12:
    vals = p12[c].unique()
    print(f"    {c}: {vals}")

print("\n" + "=" * 80)
print("8. CAPACITY PARADOX CLAIMS")
print("=" * 80)
# "22-31 pp efficiency collapse under Adaptive attacks (T->2T)" i.e. scale 1 vs scale 2
# Check in internal datasets
for ds_name, ds in [('CMABs', cmab), ('iCMABs', icmab), ('Hybrid', hybrid), ('EXP3', exp3)]:
    ds5 = ds[(ds.runs == 5) & (ds.model != 'ORACLE') & (ds.scenario == 'ADAPTIVE')]
    if len(ds5) == 0:
        continue
    for m in ds5.model.unique():
        s1 = ds5[(ds5.model == m) & (ds5.scale == 1.0)].eff_pct.mean()
        s2 = ds5[(ds5.model == m) & (ds5.scale == 2.0)].eff_pct.mean()
        diff = s1 - s2
        if abs(diff) > 10:  # significant capacity effect
            print(f"  {ds_name}/{m}: scale=1 {s1:.1f}%, scale=2 {s2:.1f}%, diff={diff:.1f} pp")

print("\n" + "=" * 80)
print("9. DISCUSSION CLAIMS (Fig 14 data)")  
print("=" * 80)
# Hybrid corpus by scenario for pursuit models
# "CPursuit: Stochastic 89.9, Markov 85.8, Adaptive 89.4, OA 89.1, Baseline 95.3"
scen_map = {'STOCHASTIC': 'Sh', 'MARKOV': 'Mk', 'ADAPTIVE': 'Ag', 'ONLINEADAPTIVE': 'OA', 'NONE': 'Bl'}
for m in ['CPURSUITNEURALUCB', 'ICPURSUITNEURALUCB', 'GNEURALUCB', 'EXPNEURALUCB']:
    h = hybrid[(hybrid.model == m)]
    print(f"  {m}:")
    for scen in ['NONE', 'STOCHASTIC', 'MARKOV', 'ADAPTIVE', 'ONLINEADAPTIVE']:
        sub = h[h.scenario == scen]
        avg = sub.eff_pct.mean()
        print(f"    {scen_map[scen]}: {avg:.1f}%")

print("\n" + "=" * 80)
print("10. 7890 EVALUATIONS / 835 SETTINGS / 552 CONFIGS")
print("=" * 80)
# Count total rows (each row = one model-scenario-config evaluation)
total_rows = sum(len(df[df.model != 'ORACLE']) for df in [cmab, icmab, hybrid, exp3])
print(f"  Total non-Oracle rows across internal datasets: {total_rows}")
total_with_oracle = sum(len(df) for df in [cmab, icmab, hybrid, exp3])
print(f"  Total rows including Oracle: {total_with_oracle}")

# Unique settings = unique (scenario, allocator, scale, runs) combos
all_int = pd.concat([cmab, icmab, hybrid, exp3], ignore_index=True)
all_int_no = all_int[all_int.model != 'ORACLE']
unique_settings = all_int_no.drop_duplicates(subset=['scenario','allocator','scale','runs','experiment']).shape[0]
print(f"  Unique (scenario, allocator, scale, runs, experiment) combos: {unique_settings}")
unique_no_exp = all_int_no.drop_duplicates(subset=['scenario','allocator','scale','runs']).shape[0]
print(f"  Unique (scenario, allocator, scale, runs) combos: {unique_no_exp}")

print("\n" + "=" * 80)
print(f"DISCREPANCY SUMMARY: {len(discrepancies)} issues found")
print("=" * 80)
for d in discrepancies:
    print(d)
