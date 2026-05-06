#!/usr/bin/env python3
"""
Analyze which scenario each model performs best in for each testbed.
"""
import csv
import os
from collections import defaultdict

# Keep actual scenario codes from CSV (no renaming)
SCENARIO_NAMES = {
    'NONE': 'none',
    'STOCHASTIC': 'stochastic',
    'MARKOV': 'markov',
    'ADAPTIVE': 'adaptive',
    'ONLINEADAPTIVE': 'onlineadaptive'
}

def analyze_best_scenarios():
    """Find which scenario each model performs best in."""
    
    testbeds = {
        'paper7': 'Master_Dataset_paper7_50_50_5_ST.csv',
        'paper12': 'Master_Dataset_paper12_1500_500_5_ST.csv',
        'paper2': 'Master_Dataset_paper2_4000_2000_5_ST.csv'
    }
    
    results = {}
    
    for paper, filename in testbeds.items():
        filepath = os.path.join(os.path.dirname(__file__), filename)
        
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found")
            continue
            
        print(f"\n{'='*70}")
        print(f"Analyzing {paper.upper()}: {filename}")
        print(f"{'='*70}")
        
        # Store performance by model and scenario
        # Structure: model_performance[model][scenario] = list of efficiency values
        model_performance = defaultdict(lambda: defaultdict(list))
        
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                model = row['model'].strip().upper()
                scenario = row['scenario'].strip().upper()
                
                # Skip ORACLE
                if model == 'ORACLE':
                    continue
                
                try:
                    avg_reward = float(row['avg_reward'])
                    efficiency = float(row.get('eff_pct', row.get('efficiency_pct', 0)))
                    regret = float(row['regret'])
                    
                    model_performance[model][scenario].append({
                        'avg_reward': avg_reward,
                        'efficiency': efficiency,
                        'regret': regret
                    })
                except (ValueError, KeyError) as e:
                    continue
        
        # Find best scenario for each model
        paper_results = {}
        for model, scenarios in sorted(model_performance.items()):
            # Average the metrics for each scenario
            scenario_averages = {}
            for scenario_name, metrics_list in scenarios.items():
                if metrics_list:
                    avg_efficiency = sum(m['efficiency'] for m in metrics_list) / len(metrics_list)
                    avg_reward = sum(m['avg_reward'] for m in metrics_list) / len(metrics_list)
                    avg_regret = sum(m['regret'] for m in metrics_list) / len(metrics_list)
                    scenario_averages[scenario_name] = {
                        'efficiency': avg_efficiency,
                        'avg_reward': avg_reward,
                        'regret': avg_regret,
                        'count': len(metrics_list)
                    }
            
            if not scenario_averages:
                continue
            
            # Find scenario with highest efficiency
            best_scenario_name = max(scenario_averages.keys(), key=lambda x: scenario_averages[x]['efficiency'])
            best_metrics = scenario_averages[best_scenario_name]
            
            paper_results[model] = {
                'best_scenario': SCENARIO_NAMES.get(best_scenario_name, best_scenario_name),
                'best_scenario_code': best_scenario_name,
                'efficiency': best_metrics['efficiency'],
                'avg_reward': best_metrics['avg_reward'],
                'regret': best_metrics['regret']
            }
            
            print(f"\n{model}:")
            print(f"  Best Scenario: {SCENARIO_NAMES.get(best_scenario_name, best_scenario_name)}")
            print(f"  Efficiency: {best_metrics['efficiency']:.2f}%")
            print(f"  Avg Reward: {best_metrics['avg_reward']:.4f}")
            print(f"  Regret: {best_metrics['regret']:.2f}")
            
            # Show all scenarios for comparison
            print(f"  All Scenarios:")
            for scen in sorted(scenario_averages.keys(), key=lambda x: scenario_averages[x]['efficiency'], reverse=True):
                metrics = scenario_averages[scen]
                print(f"    {SCENARIO_NAMES.get(scen, scen):20s}: {metrics['efficiency']:6.2f}% efficiency (n={metrics['count']})")
        
        results[paper] = paper_results
    
    return results

if __name__ == '__main__':
    results = analyze_best_scenarios()
    
    print(f"\n\n{'='*70}")
    print("SUMMARY: BEST SCENARIOS BY MODEL AND TESTBED")
    print(f"{'='*70}\n")
    
    for paper in ['paper7', 'paper12', 'paper2']:
        if paper not in results:
            continue
            
        print(f"\n{paper.upper()}:")
        for model in ['CPURSUITNEURALUCB', 'GNEURALUCB', 'ICPURSUITNEURALUCB', 'EXPNEURALUCB']:
            if model in results[paper]:
                info = results[paper][model]
                print(f"  {model:25s}: {info['best_scenario']:20s} ({info['efficiency']:.2f}%)")
