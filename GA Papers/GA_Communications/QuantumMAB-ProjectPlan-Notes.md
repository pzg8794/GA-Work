# QuantumMAB Project Plan & Work Log

**Last Updated:** February 12, 2026  
**Purpose:** Keep this document as a concise project-plan log with **date + one-line progress updates** and direct links to canonical task tracking.
**Classification:** Peer/Share-Friendly Summary (Concise)  
**Reports Notes Hub:** [../GA_Reports/NOTES-INDEX.md](../GA_Reports/NOTES-INDEX.md)

## Core References

- Baseline paper: [Quantum Entanglement Path Selection and Qubit Allocation via Adversarial Group Neural Bandits](https://arxiv.org/pdf/2411.00316)
- Comparative paper: [Informed Contextual Multi-Armed Bandits (iCMABs)](https://dl.acm.org/doi/pdf/10.1145/3638530.3664145)
- Canonical task tracker: [md_files/Task-Tracker-Formal.md](md_files/Task-Tracker-Formal.md)
- Communications navigation hub: [md_files/NAVIGATION-INDEX.md](md_files/NAVIGATION-INDEX.md)
- Detailed communication history: [md_files/Research-Communications.md](md_files/Research-Communications.md)
- Dynamic framework internal notes: [../GA_Reports/Dynamic_Routing_Allocation-GA-Notes.md](../GA_Reports/Dynamic_Routing_Allocation-GA-Notes.md)
- Testbeds internal notes: [../GA_Reports/Testbeds-GA-Notes.md](../GA_Reports/Testbeds-GA-Notes.md)

## Overall Objective

Apply stochastic methodology and informative contextual bandits (iCMAB) to EXP3-based quantum entanglement routing so the framework adapts under intelligent/adaptive adversaries. The target contribution is a predictive, context-aware adversarial routing pipeline integrating EXAMM-informed forecasting with robust bandit group selection.

## Finalized Research Questions

1. How does temporal attack correlation affect EXP3-based routing performance and regret?
2. Can EXAMM-evolved forecasting improve routing reward versus reactive-only policies?
3. How does the hybrid approach compare with strong neural/bandit baselines across scenarios?
4. What gains come from integrating predictive context into adversarial group selection?
5. How sensitive are reward/regret outcomes to forecast quality and horizon length?
6. Does stochastic reward updating model quantum uncertainty better than deterministic updates?
7. What convergence and stability changes appear under temporally correlated attacks?
8. How does the framework adapt to dynamic fidelity, capacity, and noise shifts?
9. How resilient is the hybrid model versus Byzantine-style and strategy-switching adversaries?
10. Which components transfer best to non-quantum adversarial routing domains?

## Current Work Status (Mapped to Canonical Tasks)

- **In Progress:** T-2025-020, T-2025-022, T-2025-023, T-2026-007, T-2026-008, T-2026-009
- **Blocked/Waiting External:** T-2026-005
- **Scheduled:** T-2026-010
- **Coordination:** T-2026-006

Source of truth for status changes remains [md_files/Task-Tracker-Formal.md](md_files/Task-Tracker-Formal.md).

## Date + One-Line Work Log

- **2025-08-26:** Overleaf structure and notes scaffold initialized.
- **2025-08-27:** Abstract/introduction drafted and initial RQ structure created.
- **2025-08-28:** Comparative analysis methodology and hybrid narrative refined.
- **2025-08-29:** Foundational methods section synthesized across stochastic/adversarial/contextual MABs.
- **2025-09-05:** Paper and RQs updated to match project objectives.
- **2025-09-08:** Development/test framework created and initial experiments executed.
- **2025-09-09:** EXPNeuralUCB refactored and baseline comparison improved.
- **2025-09-10:** Notebook organization improved readability and demo readiness.
- **2025-09-11:** EXPNeuralUCB modularized for faster iteration and transparency.
- **2025-09-12:** Migration into new experiment framework completed with integration checks.
- **2025-09-15:** Advisor sync completed; environment design and code structure aligned.
- **2025-09-17:** Variable adversarial environment development (0→n attacks) started.
- **2025-09-18:** Instability identified under variable environment and stabilization work initiated.
- **2025-10 to 2025-12:** Multi-paper testing/validation and comparative write-up expanded.
- **2026-01-07:** Project resumed after winter interruption; publication/paper finalization priorities reset.
- **2026-02-11:** Advisor meeting set publication-first direction and near-term venue/action items.
- **2026-02-12:** Documentation synchronized with dataset-verified current metrics and canonical tracker links.

## Active Next Steps (Execution Queue)

1. Close citation-level comparison gaps and unresolved paper comments (T-2026-007).
2. Complete remaining literature-based and testbed comparison items (T-2025-020, T-2025-022, T-2025-023).
3. Produce venue shortlist (2-3 options, B-or-better) with deadlines (T-2026-008).
4. Send consolidated progress + venue follow-up email (T-2026-009).
5. Attend Tuesday Feb 17 checkpoint and review completed updates/actions with Dan (T-2026-010).

Random Notes:

* For questions regarding iCMABs, you can contact PhD student Devroop Kar \< [dk7405@rit.edu](mailto:dk7405@rit.edu) \>  
* I reached out via email and Slack to create a channel of communication in the event I have questions.  
* **Strategic Research Framing (Brainstorm)**  
  * **Phase 1: EXPNeuralUCB \+ iCMAB (Baseline Integration)**  
    * **Focus Area:** Predictive hybrid feasibility under known adversarial settings  
    * **Goal:** Show performance gains from integrating EXAMM-evolved forecasts  
    * **Research Outcome:** Establish foundation for predictive-adversarial bandits; demonstrate baseline viability.  
  * **Phase 2: Intelligent / Adaptive Adversary**  
    * **Focus Area:** Stress-test hybrid under dynamic attacker behavior  
    * **Goal:** Evaluate adaptability beyond static attack models  
    * **Research Outcome:** Measure robustness under evolving threats; generate new benchmarks for strategic attackers.  
  * **Phase 3: Add Predictive Contender(s)**  
    * **Focus Area:** Compare iCMAB against other forecasting tools (e.g., RNNs, meta-learners)  
    * **Goal:** Identify stronger or more efficient predictive layers  
    * **Research Outcome:** Determine if iCMAB is optimal or replaceable; build a comparative performance landscape.  
  * **Phase 4: Expand Literature Toolset**  
    * **Focus Area:** Broaden survey of predictive bandit models  
    * **Goal:** Create a toolkit for modular forecasting integration  
    * **Research Outcome:** Curate and classify predictive modules for future research and plug-and-play experimentation.  
  * **Phase 5: Generalization Framework**  
    * **Focus Area:** Build pluggable hybrid architecture  
    * **Goal:** Abstract the forecasting layer → generalizable design  
    * **Research Outcome:** Deliver a reusable design pattern for predictive-adversarial MABs applicable across domains.  
* **Strategic Architecture Framing (Brainstorm)**  
  * **Unified Problem Reframing:** *Restructure* the comparative evaluation into a **universal decision-making problem**—not just about quantum routing, but about adaptive intelligence across adversarial, stochastic, and contextual systems.  
  * **Design Principle Emerged:** The idea of **"compositional intelligence"**—forecasting (iCMAB), robustness (EXPNeuralUCB), and structure adaptation (EXAMM)—was solidified as a *core architectural triad* for universal routing models.  
  * **Neural Waze for Everything → Operationalized:** It’s no longer metaphorical. Through the tables, diagrams, and hybrid UCB formulation, we laid out how Waze-like anticipatory adaptation becomes a functional system in quantum, healthcare, finance, and more.  
  * **Gap Map → Framework Generator:** The visual synthesis of five key research gaps now *drives* the implementation roadmap and framing—each gap maps to a specific feature of the hybrid.  
  * **Phase Readiness Locked:** Closing the loop between narrative (Comparative Analysis) and method (Advanced \+ Hybrid Approaches) to **dive into the implementation** plan.

**Literature Review Table with Download Links (Excluding Baseline Papers)**

|  | Citation Key | Authors | Title | Strategy | Relevance  | Status | Link |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **jie2024expneuralucb** | **Huang, Y.; Wang, L.; Xu, J.** | Quantum Entanglement Path Selection and Qubit Allocation via Adversarial Group Neural Bandits | Adversarial neural bandits (EXPNeuralUCB) | **Critical  (10/10)** | Available \- Primary Baseline | **[https://arxiv.org/abs/2411.00316](https://arxiv.org/abs/2411.00316)** |
| **2** | **chaudhary2023quantum** | **Chaudhary, V. et al.** | Learning-based Route Selection in Noisy Quantum Communication Networks | UCB multi-arm bandit for quantum route selection | **Critical  (9/10)** | Peer-specified \- PRIORITY  | **[https://genesys-lab.org/papers/Quantum\_Bandit\_ICC2023.pdf](https://genesys-lab.org/papers/Quantum_Bandit_ICC2023.pdf)** |
| **3** | **zhang2021icmab** | **Kar, Lyu, Ororbia, Desell, Krutz (GECCO ’24 Companion)** | Enabling An Informed Contextual Multi-Armed Bandit Framework for Stock Trading With Neuroevolution (EXAMM-evolved RNNs) | Informed Contextual MAB with EXAMM-evolved RNN forecasting | **Critical (9/10) Integration**  | Available \- Local Storage Reviewed | **[https://dl.acm.org/doi/pdf/10.1145/3638530.3664145](https://dl.acm.org/doi/pdf/10.1145/3638530.3664145)** |
| 4 | **dahlberg2021netsquid** | **Dahlberg, A., et al.** | NetSquid, a NETwork Simulator for QUantum Information using Discrete events | Discrete-event quantum network simulation framework | **High (8/10)** | Available \- Simulation Foundation | **[https://www.nature.com/articles/s42005-021-00647-8](https://www.nature.com/articles/s42005-021-00647-8)** |
| **5** | **wang2025learning** | **Xuchuang Wang, Maoli Liu, Xutong Liu, Zhuohua Li, Mohammad Hajiesmaili, John C.S. Lui, Don Towsley** | Learning Best Paths in Quantum Networks | Online learning for quantum network path selection | **High  (8/10)** | Peer-specified \- PRIORITY  | **[https://arxiv.org/abs/2506.12462](https://arxiv.org/abs/2506.12462)** |
| **6** | **zhou2020neuralucb** | **Zhou, D. et al.** | Neural Contextual Bandits with UCB-based Exploration | Neural UCB for contextual bandits | **High  (8/10)** | Available \- Core Baseline | **[https://arxiv.org/abs/1911.04462](https://arxiv.org/abs/1911.04462)** |
| **7** | **liu2024qbgp** | **Liu, Maoli; Duan, Yihan; Chen, Tianqi; et al. “Quantum BGP with Online Path Selection via Network Benchmarking,” IEEE INFOCOM 2024** | Quantum BGP with Online Path Selection via Network Benchmarking | Inter-domain quantum BGP routing | **High  (8/10)** | Available \- IEEE Xplore | **[https://ieeexplore.ieee.org/document/10621359](https://ieeexplore.ieee.org/document/10621359)** |
| **8** | **jallowkhan2025adaptive** | **Lamarana Jallow & Majid Iqbal Khan** | Adaptive Entanglement Routing with Deep Q-Networks | Deep reinforcement learning for entanglement routing | **High  (8/10)** | Available \- arXiv | **[https://arxiv.org/pdf/2503.02895.pdf](https://arxiv.org/pdf/2503.02895.pdf)** |
| **9** | **auer2002exp3** | **Auer, P., Cesa-Bianchi, N., Freund, Y., & Schapire, R. E.** | Gambling in a Rigged Casino: The Adversarial Multi-Armed Bandit Problem | EXP3 algorithm for adversarial (nonstochastic) bandit learning | **High  (8/10)** | Available Adversarial Foundation | **[https://ieeexplore-ieee-org.ezproxy.rit.edu/stamp/stamp.jsp?tp=\&arnumber=492488](https://ieeexplore-ieee-org.ezproxy.rit.edu/stamp/stamp.jsp?tp=&arnumber=492488)** |
| **10** | **pompili2021realization** | **Pompili, M., et al.** | Realization of a multinode quantum network of remote solid-state qubits | Multi-node quantum network with NV centers | **High  (7/10)** | Available \- Hardware Validation | **[https://www.science.org/doi/10.1126/science.abg1919](https://www.science.org/doi/10.1126/science.abg1919)** |
| **11** | **kumar2024routing** | **Kumar, V. et al.** | Routing in Quantum Repeater Networks with Mixed Efficiency | Heterogeneous quantum repeater routing | **High  (7/10)** | Available \- arXiv HTML | **[https://arxiv.org/html/2310.08990v4](https://arxiv.org/html/2310.08990v4)** |
| **12** | **wang2024quarc** | **Wang, L. et al.** | Efficient Routing on Quantum Networks using Adaptive Clustering | Clustering-based entanglement routing (QuARC) | **High  (7/10)** | Available \- arXiv | **[https://arxiv.org/pdf/2410.23007.pdf](https://arxiv.org/pdf/2410.23007.pdf)** |
| **13** | **qianetal2025cmabtts** | **Qian, M., Li, C., Ma, Y., Song, Y., Liu, C., & Yin, Z.** | A Contextual MAB-Based Two-Timescale Scheme for RIS-Assisted Systems | Contextual multi-armed bandits for reconfigurable intelligent surface (RIS) phase-shift optimization | **High  (7/10)** | Available – IEEE Wireless Communications Letters Vol. 14, No. 2, Feb 2025 | **[https://ieeexplore.ieee.org/document/10764718](https://ieeexplore.ieee.org/document/10764718)** |
| **14** | **thompson1933likelihood** | **Thompson, W. R.** | On the likelihood that one unknown probability exceeds another in view of the evidence of two samples | **Original Thompson Sampling Bayesian posterior sampling for exploration** | **High  (7/10)** | Available Historical Foundation | **[https://www-jstor-org.ezproxy.rit.edu/stable/2332286?seq=3](https://www-jstor-org.ezproxy.rit.edu/stable/2332286?seq=3)** |
| **15** | **gottesman2009qec** | **Daniel Gottesman (solo)** | An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation  | Stabilizer formalism and quantum error correction codes | Medium  (6/10) | Available \- QEC Foundation | **[https://arxiv.org/abs/0904.2557](https://arxiv.org/abs/0904.2557)** |
| **16** | **knill2005quantum** | **Knill, E.** | Quantum computing with realistically noisy devices | Fault-tolerant quantum computation thresholds | Medium (6/10) | Available \- Fault Tolerance Theory | **[https://www.nature.com/articles/nature03350](https://www.nature.com/articles/nature03350)** |
| **17** | **zhang2020neuralts** | **Zhang, W. et al.** | Neural Thompson Sampling | Neural Thompson Sampling for contextual bandits | **Medium  (6/10)** | Available \- Neural Baseline | **[https://arxiv.org/abs/2010.00827](https://arxiv.org/abs/2010.00827)** |
| **18** | **abbasi2011improved** | **Abbasi-yadkori, Y. et al.** | Improved Algorithms for Linear Stochastic Bandits | LinUCB for linear contextual bandits | **Medium  (6/10)** | Available \- Classical Baseline | **[https://papers.nips.cc/paper/2011/hash/e1d5be1c7f2f456670de3d53c7b54f4a-Abstract.html](https://papers.nips.cc/paper/2011/hash/e1d5be1c7f2f456670de3d53c7b54f4a-Abstract.html)** |
| **19** | **cicconetti2024scalable** | **Cicconetti, C. et al.** | Scalable Quantum Networks: Hierarchical Entanglement Routing | Hierarchical k-ary tree quantum network architecture | **Medium  (6/10)** | Available \- arXiv | **[https://arxiv.org/pdf/2306.09216.pdf](https://arxiv.org/pdf/2306.09216.pdf)** |
| **20** | **leone2021costvector** | **Leone, H., Miller, N. R., Singh, D., Langford, N. K., & Rohde, P. P.** | Cost vector analysis & multi-path entanglement routing in quantum networks | Cost-vector formalism for static quantum routing protocol analysis | **Medium  (6/10)** | Available | **[https://arxiv.org/abs/2105.00418v3](https://arxiv.org/abs/2105.00418v3)** |
| **21** | **coopmans2021benchmark** | **Helsen, J. & Wehner, S.** | A benchmarking procedure for quantum networks | Randomized benchmarking protocol for quantum network link quality | **Medium  (6/10)** | Available \- arXiv | **[https://arxiv.org/abs/2103.01165](https://arxiv.org/abs/2103.01165)** |
| **22** | **auer2002ucb1** | **Auer, P., Cesa-Bianchi, N., & Fischer, P.** | Finite-time analysis of the multiarmed bandit problem | **Upper confidence bound (UCB1) for bandit arm selection** | **Medium  (6/10)** | Available \- Classical Foundation | **[https://link.springer.com/article/10.1023/A:1013689704352](https://link.springer.com/article/10.1023/A:1013689704352)** |
| **23** | **agrawal2012thompson** | **Agrawal, S. & Goyal, N.** | Analysis of Thompson Sampling for the multi-armed bandit problem | **Thompson Sampling with theoretical regret analysis** | **Medium  (6/10)** | Available \- Bayesian Foundation | **[https://proceedings.mlr.press/v23/agrawal12.html](https://proceedings.mlr.press/v23/agrawal12.html)** |
| **24** | **sutton2018reinforcement** | **Sutton, R. S. & Barto, A. G.** | Reinforcement Learning: An Introduction (2nd ed.) | **ε-greedy exploration and reinforcement learning foundations** | **Medium  (6/10)** | Available RL Foundation | **[https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf)** |
| **25** | **brahmachari2023quantum** | **Brahmachari, S., Lumbreras, J., & Tomamichel, M.** | Quantum contextual bandits and recommender systems for quantum data | Linear contextual bandits for quantum measurement optimization | **Medium  (5/10)** | Available | **[https://arxiv.org/abs/2301.13524](https://arxiv.org/abs/2301.13524)** |
| **26** | **lee2022utility** | **Lee, Y., Dai, W., Towsley, D., & Englund, D.** | Quantum Network Utility: A Framework for Benchmarking Quantum Networks | Utility-based quantum network performance metrics | **Medium  (5/10)** | Available | **[https://arxiv.org/abs/2210.10752](https://arxiv.org/abs/2210.10752)** |
| **27** | **pereg2023quantum** | **Boche, H., Deppe, C., & Pereg, U.** | Quantum Broadcast Channels with Cooperating Decoders: An Information-Theoretic Perspective on Quantum Repeaters | Quantum broadcast network protocols with receiver cooperation | **Medium  (5/10)** | Available | **[https://arxiv.org/pdf/2011.09233](https://arxiv.org/pdf/2011.09233)** |
| **28** | **buchholz2023quantum** | **Buchholz, S. et al.** | Multi-Armed Bandits and Quantum Channel Oracles | Theoretical quantum MAB with oracle query complexity | **Low  (4/10)** | Available \- Quantum Theory | **[https://quantum-journal.org/papers/q-2025-03-25-1672/](https://quantum-journal.org/papers/q-2025-03-25-1672/)** |

**Literature Review Table**  
**Critical Finding: Both Missing Papers Were Found**

1. ***arxiv:2506.12462 \- Wang et al. (2025)​***  
   * *Title:* "Learning Best Paths in Quantum Networks"  
   * *Venue:* IEEE INFOCOM 2025  
   * *Found:* Available on arXiv and INFOCOM proceedings  
   * *Strategy:* Online learning for quantum network path selection with link-level and path-level feedback  
   * *Relevance:* High (8/10)  
2. ***genesys-lab.org/papers/QuantumBanditICC2023.pdf \- Chaudhary et al. (2023)​***  
   * *Title:* "Learning-based Route Selection in Noisy Quantum Communication Networks"  
   * *Venue:* IEEE ICC 2023  
   * *Found:* Available on Northeastern University's Genesys Lab website  
   * *Strategy:* UCB multi-arm bandit for quantum route selection with synchronized entanglement swapping analysis  
   * *Relevance:* Critical (9/10)

**Immediate Action Required for Piter**

1. ***Download both papers immediately:***  
   * Get Wang et al. (2025) from arXiv:2506.12462​  
   * Get Chaudhary et al. (2023) from the Genesys Lab website​  
2. ***Add to bibliography:*** Both papers are supervisor-specified and critical for your Related Work section  
3. ***Priority analysis:*** The Chaudhary paper (9/10 relevance) is a direct UCB bandit baseline comparison \- exactly what is needed for contrasting with our AQEM framework

**Note:**

- Dan mentioned these missing pieces of the literature for comparison in the quantum fault-tolerant routing paper.

## **Key Papers: Algorithms & Methods**

| Component | Paper/Source | Key Contribution | Implementation |
| :---- | :---- | :---- | :---- |
| **UCB1** | Auer et al., 2002 | Upper confidence bound for bandit arm selection | **UCB\_i(t)** \= μ\_i(t-1) \+ √(2ln(t)/N\_i(t)) |
| **Thompson Sampling** | Thompson, 1933;  Agrawal & Goyal, 2012 | Bayesian posterior sampling for exploration | **ThompsonSamplingAllocator** with  Beta(α\_i \+ s\_i, β\_i \+ f\_i) (uniform prior \= Beta(1,1)) |
| **ε-Greedy** | Sutton & Barto, 2018  (2nd ed.); Watkins, 1989  (Q-learning origins) | Epsilon-greedy exploration-exploitation  with decay schedule | ε\_t \= max(ε\_min, ε\_0 · λ^t)  (via **RandomQubitAllocator(epsilon, epsilon\_decay, min\_epsilon)**;  aliased as RandomQubitAllocator) |
| **EXP3** | Auer et al., 2002 | Adversarial multi-armed bandits | Weight-based exponential selection in the  **EXPNeuralUCB** group layer |
| **NeuralUCB** | Zhou et al., 2020 | Neural networks \+ UCB for contextual bandits | **GNeuralUCB** with  UCB μ\_{t-1}(x) \+ β\_t√(φ(x)^T V\_{t-1}^{-1} φ(x)) |
| **EXPNeuralUCB** | Huang et al., 2024 | Adversarial group bandits \+ neural UCB | **EXPNeuralUCB** combining **EXP3** group selection with neural **UCB** actions |
| **Pursuit Learning** | Leslie & Kohn, 2006 | Contextual pursuit with  probability-weighted updates | **CPursuitNeuralUCB** with learning rate 0.1 and action probability refinement |
| **iCMAB  (Informed CMAB)** | Your novel integration, building  on Kar et al., 2024 (EXAMM- evolved RNN forecasting) | Predictive CMAB via ARIMA forecasting | **iCPursuitNeuralUCB** with 50-frame ARIMA warmup, pursuit learning \+ time-series context |
| **Dynamic  Qubit Allocation** | Your implementation  (UCB-based) | Resource-aware qubit allocation  with fidelity/success-probability thresholds  and retry logic | **DynamicUCBAllocator** with dynamic Bell-pair fidelity thresholds (0.582–0.712) and backoff on sub-threshold links |
| **Random Allocation  (Baseline)** | Baseline (no paper) | Uniform random qubit selection for comparison | **RandomQubitAllocator** |

