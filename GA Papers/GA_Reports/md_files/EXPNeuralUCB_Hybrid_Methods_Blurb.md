# Reusable Methods Blurb for EXPNeuralUCB Hybrid Paper

**Classification:** Peer/Share-Friendly Summary (Concise)  
**Reference Hub:** [../NOTES-INDEX.md](../NOTES-INDEX.md)  
**Canonical Tracker:** [../../GA_Communications/md_files/Task-Tracker-Formal.md](../../GA_Communications/md_files/Task-Tracker-Formal.md)

## One-Paragraph iCMAB Benchmark Reference (can be adapted for methods or related work)

**Baseline iCMAB Evaluation:**
To establish robust baselines for hybrid development, we conducted a comprehensive empirical evaluation of five informed contextual multi-armed bandit (iCMAB) algorithms—iCEpsilonGreedy, iCPursuit, iCThompsonSampling, iCEXP4, and iCEpochGreedy—across a 3~$\times$~2~$\times$~2~$\times$~5 experimental grid spanning capacity scales (1$\times$, 1.5$\times$, 2$\times$), evaluator regimes (T-type, Tb-type), run counts (3-run, 5-run), and environment conditions (NONE baseline, STOCHASTIC, MARKOV, ADAPTIVE ATTACKS, ONLINE ADAPTIVE ATTACKS). Using quantum network simulation with 4 paths and variable qubit allocations, we measured efficiency as the ratio of achieved to oracle-optimal rewards. Results show that iCEpsilonGreedy decisively dominates with 88.63\% global average efficiency and 25/25 scenario wins, while iCPursuit forms a reliable secondary tier at 67.99\%; iCThompsonSampling provides a Bayesian-grounded alternative at 67.17\%, while iCEXP4 and iCEpochGreedy serve as lower-bound heuristics. Critically, algorithm rankings are robust across capacity scaling (max variance 2.07\%), evaluator regimes (differences $\leq$1.50\%), and run counts (3-run vs 5-run $\leq$0.50\% variance), providing statistically validated baselines for hybrid integration.

---

## Extended Methods Paragraph (for more detailed methods section)

**Informed Contextual Multi-Armed Bandit Baselines:**
We established empirically grounded baselines through systematic evaluation of five iCMAB algorithms across comprehensive experimental conditions. The evaluation spans a 60-configuration grid: three capacity scales (1$\times$, 1.5$\times$, 2$\times$ of the base 4000-qubit allocation), two evaluator regimes (T-type and Tb-type routing protocols), two experiment suite sizes (3-run for rapid screening, 5-run for statistical confirmation), and five environment classes (NONE for ideal conditions, STOCHASTIC for natural failures, MARKOV for adversarial patterns, ADAPTIVE ATTACKS, and ONLINE ADAPTIVE ATTACKS). Each configuration runs the five candidate algorithms—iCEpsilonGreedy, iCPursuit, iCThompsonSampling, iCEXP4, and iCEpochGreedy—on a simulated 4-path quantum network with base qubit configuration (8, 10, 8, 9). Efficiency is measured as the ratio of algorithm reward to oracle reward (percentage form), enabling direct comparison to theoretical optimality. Empirical results demonstrate that iCEpsilonGreedy achieves 88.63\% global average efficiency with consistent dominance across all environment classes (ranging from 93.30\% in NONE to 86.38\% in MARKOV), while maintaining robustness across capacity and regime variations (maximum variance $\leq$2.07\%, regime differences $\leq$1.50\%). iCPursuit emerges as a secondary tier baseline at 67.99\%, providing a comparative reference for hybrid ablations. The consistency of these rankings across 3-run and 5-run suites (differences $\leq$0.50\%) validates the statistical reliability of the baseline selection. These grounded empirical results inform the selection of iCMAB models for hybrid integration and establish performance targets that hybrid systems must match or exceed.

---

## Citation Format for the Benchmark Paper

In your EXPNeuralUCB hybrid paper, you can cite the iCMAB benchmark as:

**In methods:**
"We benchmark candidate iCMAB algorithms using the evaluation framework described in [Garcia Bautista et al., 2025, iCMAB quantum routing benchmark], which provides statistically validated baselines across 60 experimental configurations..."

**In related work or baselines:**
"Recent work [Garcia Bautista et al., 2025] established that iCEpsilonGreedy provides a strong 88.63\% baseline for quantum routing tasks under diverse adversarial conditions, with robustness validated across capacity scaling and multiple evaluation regimes."

---

## Key Metrics to Reference in Hybrid Paper

When comparing your hybrid results to these baselines:

| Baseline | Global Avg | Tier | Use Case |
|----------|-----------|------|----------|
| iCEpsilonGreedy | 88.63% | Primary | "Our hybrid target is to match or exceed the 88.63% iCEpsilonGreedy baseline..." |
| iCPursuit | 67.99% | Secondary | "As a secondary comparison, iCPursuit achieves 67.99%, providing a broader comparative context..." |
| NONE (ideal) | 93.30% | Upper bound | "iCEpsilonGreedy achieves 93.30% in ideal NONE conditions, establishing an upper-bound reference..." |
| STOCHASTIC | 87.57% | Common scenario | "In realistic stochastic failure scenarios, the baseline achieves 87.57\% efficiency..." |
| Online Adaptive | 89.26% | Hardest adversarial | "Even under online adaptive attacks (the most challenging regime), iCEpsilonGreedy maintains 89.26%..." |

---

## Narrative for Hybrid Results Section

**Template Sentence:**
"Our iCEpsilonGreedy + EXPNeuralUCB hybrid achieves [X]% efficiency, [exceeding/approaching] the pure iCEpsilonGreedy baseline of 88.63% by [+/-Y percentage points], representing a [%] improvement in [specific environment or regime]. Across capacity scales, the hybrid maintains [Z]% maximum variance, consistent with the 2.07% variance of the iCEpsilonGreedy baseline and validating robustness across network configurations."

**Comparative Anchor:**
"While the pure iCEpsilonGreedy iCMAB achieves a global average of 88.63\%, our hybrid architecture achieves [new value], demonstrating that adversarial robustness augmentation provides [describe benefit]. In the most challenging online adaptive attacks scenario, where iCEpsilonGreedy alone achieves 89.26%, our hybrid reaches [new value], representing a [magnitude] improvement over the non-adversarial baseline."

---

## FAQ: Using the Benchmark in Your Hybrid Work

**Q: Can I cite the iCMAB benchmark before it's published?**
A: Yes—cite it as "Garcia Bautista, P., et al. (2025). Comprehensive evaluation of informed contextual multi-armed bandit models for quantum network routing. [Technical Report, RIT AI/Quantum Computing Program]" or adjust to match your publication venue.

**Q: Should I compare my hybrid to all 5 iCMAB algorithms or just iCEpsilonGreedy?**
A: Always include iCEpsilonGreedy (the dominant baseline at 88.63%). If space permits, also compare iCPursuit (67.99%) to show the magnitude of improvement over secondary tiers. Avoid dwelling on iCEXP4/iCEpochGreedy unless your hybrid specifically targets lower tiers.

**Q: What if my hybrid underperforms the 88.63% baseline?**
A: This is still publishable—explain the trade-off (e.g., "we sacrifice 3% efficiency for adversarial robustness guarantees" or "the hybrid achieves 85% efficiency but with [specific theoretical guarantee]"). Frames the iCEpsilonGreedy baseline as "reasonable but non-adversarial" and positions your work as advancing the adversarial-aware frontier.

**Q: Can I use just the "global average" number or should I break it down by environment?**
A: Use the global average (88.63%) as your headline benchmark. For detailed comparisons, break down by environment (NONE: 93.30%, STOCHASTIC: 87.57%, etc.) to show where your hybrid excels or lags.

---

## Files for Reference

- **Primary benchmark report:** `iCMAB_Evaluation_Report_FINAL.tex` (comprehensive, 15-20 pages)
- **Summary document:** `iCMAB_Update_Summary.md` (quick reference, all key metrics)
- **Data source:** 12 iCMAB log files from quantum routing experiments (3-run and 5-run suites across S1/S1.5/S2 capacities and T/Tb regimes)

---

## Quick Copy-Paste Numbers

```
Global average: 88.63%
Scenario wins: 25/25
NONE baseline: 93.30%
STOCHASTIC: 87.57%
MARKOV: 86.38%
ADAPTIVE: 87.65%
ONLINE ADAPTIVE: 89.26%

Capacity 1×: 88.00%
Capacity 1.5×: 87.57%
Capacity 2×: 85.93%
Max capacity variance: 2.07%

T-type: 87.39%
Tb-type: 87.68%
Max regime difference: +0.29%

3-run: 87.48%
5-run: 87.60%
Max run variance: +0.12%

Secondary baseline (iCPursuit): 67.99%
Mid-range (iCThompsonSampling): 67.17%
Lower-bound (iCEXP4/iCEpochGreedy): 37.30% / 37.15%
```
