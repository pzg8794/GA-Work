#!/usr/bin/env python3
"""
Comprehensive cross-testbed analysis extracting rich findings from master datasets.
"""
import csv
from collections import defaultdict

def analyze_testbed(filename, testbed_name):
    """Extract comprehensive findings from a testbed dataset."""
    
    # Data structures for analysis
    model_scenario_perf = defaultdict(lambda: defaultdict(list))
    model_allocator_perf = defaultdict(lambda: defaultdict(list))
    scenario_winners = defaultdict(int)
    
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row['model'].upper()
            if model == 'ORACLE':
                continue
                
            scenario = row['scenario']
            allocator = row['allocator']
            eff = float(row['eff_pct'])
            gap = float(row['gap_pct'])
            regret = float(row['regret'])
            winner = row['winner']
            scenario_winner = row['scenario_winner']
            
            # Track performance by scenario
            model_scenario_perf[model][scenario].append(eff)
            
            # Track performance by allocator
            model_allocator_perf[model][allocator].append(eff)
            
            # Track scenario winners
            if scenario_winner:
                scenario_winners[scenario_winner] += 1
    
    print(f"\n{'='*70}")
    print(f"{testbed_name} COMPREHENSIVE ANALYSIS")
    print(f"{'='*70}")
    
    # Finding 1: Performance across scenarios (robustness)
    print(f"\n1. ROBUSTNESS: Performance Across All Scenarios")
    print(f"{'-'*70}")
    for model in sorted(model_scenario_perf.keys()):
        perfs = []
        for scenario in ['NONE', 'STOCHASTIC', 'MARKOV', 'ADAPTIVE', 'ONLINEADAPTIVE']:
            if scenario in model_scenario_perf[model]:
                avg_eff = sum(model_scenario_perf[model][scenario]) / len(model_scenario_perf[model][scenario])
                perfs.append((scenario.lower(), avg_eff))
        
        if perfs:
            print(f"\n{model}:")
            best = max(perfs, key=lambda x: x[1])
            worst = min(perfs, key=lambda x: x[1])
            robustness = best[1] - worst[1]
            
            for scen, eff in perfs:
                marker = "★" if scen == best[0] else "✗" if scen == worst[0] else " "
                print(f"  {marker} {scen:15s}: {eff:6.2f}%")
            print(f"  → Robustness gap: {robustness:.2f}pp (best-worst)")
    
    # Finding 2: Scenario difficulty ranking
    print(f"\n2. SCENARIO DIFFICULTY RANKING")
    print(f"{'-'*70}")
    scenario_avg = {}
    for scenario in ['NONE', 'STOCHASTIC', 'MARKOV', 'ADAPTIVE', 'ONLINEADAPTIVE']:
        all_effs = []
        for model_perfs in model_scenario_perf.values():
            if scenario in model_perfs:
                all_effs.extend(model_perfs[scenario])
        if all_effs:
            scenario_avg[scenario] = sum(all_effs) / len(all_effs)
    
    sorted_scenarios = sorted(scenario_avg.items(), key=lambda x: x[1], reverse=True)
    for rank, (scenario, avg_eff) in enumerate(sorted_scenarios, 1):
        difficulty = "EASIEST" if rank == 1 else "HARDEST" if rank == len(sorted_scenarios) else ""
        print(f"{rank}. {scenario.lower():15s}: {avg_eff:6.2f}% avg  {difficulty}")
    
    # Finding 3: Most dominant model
    print(f"\n3. DOMINANCE ANALYSIS")
    print(f"{'-'*70}")
    print(f"Most winning model: {max(scenario_winners.items(), key=lambda x: x[1])}")
    
    # Finding 4: Allocator effects (if multiple allocators present)
    print(f"\n4. ALLOCATOR IMPACT (if applicable)")
    print(f"{'-'*70}")
    allocators = set()
    for model_allocs in model_allocator_perf.values():
        allocators.update(model_allocs.keys())
    
    if len(allocators) > 1:
        for model in sorted(model_allocator_perf.keys()):
            if len(model_allocator_perf[model]) > 1:
                print(f"\n{model}:")
                for alloc, effs in sorted(model_allocator_perf[model].items()):
                    avg_eff = sum(effs) / len(effs)
                    print(f"  {alloc:20s}: {avg_eff:6.2f}%")
    else:
        print(f"Single allocator: {list(allocators)[0]}")
    
    return {
        'model_scenario_perf': model_scenario_perf,
        'scenario_avg': scenario_avg,
        'scenario_winners': scenario_winners
    }


if __name__ == '__main__':
    testbeds = {
        'PAPER 2 (Large-Scale: 15N/51E/4P, ThompsonSampling, 4K/2K/5R)': 
            'Master_Dataset_paper2_4000_2000_5_ST.csv',
        'PAPER 7 (Small-Scale: 50N/141E/15P, Default, 50/50/5R)': 
            'Master_Dataset_paper7_50_50_5_ST.csv',
        'PAPER 12 (Mid-Scale: 100N/426E/4P, Default, 1.5K/500/5R)': 
            'Master_Dataset_paper12_1500_500_5_ST.csv',
    }
    
    results = {}
    for name, filename in testbeds.items():
        results[name] = analyze_testbed(filename, name)
    
    # Cross-testbed comparison
    print(f"\n\n{'='*70}")
    print(f"CROSS-TESTBED META-ANALYSIS")
    print(f"{'='*70}")
    
    print(f"\nScenario difficulty consistency across testbeds:")
    for testbed, data in results.items():
        print(f"\n{testbed}:")
        sorted_scens = sorted(data['scenario_avg'].items(), key=lambda x: x[1], reverse=True)
        print(f"  Easiest → Hardest: {' > '.join([s[0].lower() for s in sorted_scens])}")
