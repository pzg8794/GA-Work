# **Integration Plan: Sheeraja's UDRM into Quantum Path Optimization**

## 

## **High-Level Overview**

Sheeraja's **Uncertainty-Driven Replay Memory (UDRM)** optimizes RL agent learning through uncertainty-aware experience replay. We can adapt her **evidential deep learning** uncertainty quantification to improve EXPNeuralUCB's decision-making in quantum routing by prioritizing high-uncertainty transitions for better exploration.

## **1\. Core Concepts from Sheeraja's Work**

## **A. Uncertainty Types (Evidential Deep Learning)**

* **Aleatoric Uncertainty** \- Inherent quantum decoherence randomness (irreducible)  
* **Epistemic Uncertainty** \- Model confidence in path/qubit allocation predictions (reducible via learning)

## **B. Key Innovation: UDRM Mechanism**

1\. Initial Exploration (10% of timesteps)   
   → Collect uncertainty estimates for α, β calibration  
2\. Threshold Calculation    
   → threshold(t) \= α·e^(-β·t)  
   → α \= 99th percentile of initial uncertainties  
   → β \= log(k/2) / T\_total  (where k=2, threshold halves by T\_end)  
3\. Replay Buffer Prioritization  
   → Add transitions where epistemic\_unc \< threshold  
   → Re-add high-confidence transitions (reward \> 0\)  
   → Biases learning toward certain decisions  
4\. Alpha/Beta Recalibration  
   → Every τ timesteps (5000 recommended)  
   → Adjust α/β based on moving-average uncertainty

## **2\. Integration Architecture**

## **Phase 1: Uncertainty Estimation Layer**

**File: hybrid\_variable\_framework/uncertainty\_module.py**  
*\# Adapt Sheeraja's evidential DL approach*  
class QuantumUncertaintyEstimator:  
    """  
    Estimates aleatoric & epistemic uncertainty for:  
    \- Path selection decisions (EXP3 group)  
    \- Qubit allocation decisions (Neural UCB arm)  
    """  
    def estimate\_uncertainty(self, context, prediction):  
        *\# Use evidential regression (Sheeraja's approach)*  
        aleatoric \= estimate\_aleatoric(context)  *\# Decoherence noise*  
        epistemic \= estimate\_epistemic(prediction)  *\# Model uncertainty*  
        return aleatoric, epistemic

**Integration Point:**

* Feed EXPNeuralUCB's context → get uncertainty  
* Use to guide exploration-exploitation trade-off


## **Phase 2: Adaptive Replay Buffer**

**File: hybrid\_variable\_framework/adaptive\_replay\_buffer.py**  
class QuantumAdaptiveReplayBuffer:  
    """  
    UDRM applied to quantum routing:  
    \- Prioritize transitions with high epistemic uncertainty  
    \- Track uncertainty thresholds for path/qubit decisions  
    """  
    def store\_transition(self, path, qubit\_action, reward,   
                        epistemic\_unc, aleatoric\_unc):  
        threshold \= self.compute\_threshold(t)  
        
        *\# Sheeraja's logic: store if confident OR valuable*  
        if epistemic\_unc \< threshold:  
            self.buffer.append((path, qubit\_action, reward))  
              
            *\# Re-add high-confidence successful transitions*  
            if reward \> 0 and epistemic\_unc \< threshold \* 0.75:  
                self.buffer.append((path, qubit\_action, reward))

## **Phase 3: Enhanced EXPNeuralUCB**

**File: hybrid\_variable\_framework/exp\_neural\_ucb\_uncertain.py**  
**Modifications:**

* **Group Selection (EXP3)**: Weight by uncertainty-aware rewards  
* **Arm Selection (Neural UCB)**: Use epistemic uncertainty for UCB radius  
* **Learning**: Prioritize replay from the adaptive buffer

class UncertaintyAwareEXPNeuralUCB(EXPNeuralUCB):  
    """  
    EXPNeuralUCB \+ Sheeraja's UDRM uncertainty quantification  
    """  
      
    def select\_group(self, contexts):  
        *\# EXP3 path selection*  
        group\_probs \= self.exp3\_selector.select(  
            feedback\_rewards=self.uncertainty\_weighted\_rewards  
        )  
        return group\_probs  
      
    def select\_arm(self, context):  
        *\# Neural UCB with uncertainty-aware confidence bounds*  
        pred, a1, z1 \= self.neural\_network.forward(context)  
          
        *\# Epistemic uncertainty widens confidence interval*  
        epistemic \= self.uncertainty\_estimator.estimate\_epistemic(pred)  
        ucb\_radius \= self.beta \* epistemic \+ self.exploration\_bonus  
          
        arm \= np.argmax(pred \+ ucb\_radius)  
        return arm  
      
    def update(self, path, action, reward, uncertainty\_tuple):  
        *\# Store with uncertainty for adaptive replay*  
        self.adaptive\_buffer.store\_transition(  
            path, action, reward,  
            epistemic\_unc=uncertainty\_tuple\[1\],  
            aleatoric\_unc=uncertainty\_tuple\[0\]  
        )

## **3\. Quantitative Integration Points**

| Component | Sheeraja's UDRM | Quantum Routing | Integration Method |
| ----- | ----- | ----- | ----- |
| **Uncertainty Type** | Model confidence | Prediction reliability | Evidential DL (same) |
| **Threshold (t)** | α·e^(-β·t) | Path/qubit certainty | Adaptive decay |
| **Re-add Logic** | reward \> 0 \+ unc \< 0.75·τ | Entanglement success \> threshold | Quantum-specific thresholds |
| **Buffer Size** | Fixed (increases with re-adds) | Dynamic quantum state space | Bounded by |
| **Recalibration** | Every 5000 timesteps | Every 1000 frames (faster quantum drift) | Online α/β update |

## **4\. Code Structure Overview**

hybrid\_variable\_framework/  
├── \_\_init\_\_.py  
├── uncertainty\_module.py          ← NEW: Evidential uncertainty estimation  
├── adaptive\_replay\_buffer.py       ← NEW: UDRM replay buffer (Sheeraja-adapted)  
├── exp\_neural\_ucb\_uncertain.py     ← MODIFIED: EXPNeuralUCB \+ uncertainties  
├── quantum\_environment.py          ← EXISTING (no changes needed)  
├── training\_loop.py                ← MODIFIED: Use new modules  
└── evaluation/  
    ├── metrics.py                  ← Add uncertainty-aware metrics  
    └── visualization.py            ← Plot uncertainty thresholds over time

## **5\. Experimental Validation Steps**

## **Step 1: Baseline Comparison**

* Run **standard EXPNeuralUCB** (current)  
* Run **EXPNeuralUCB \+ UDRM** (Sheeraja-adapted)  
* **Metric**: Reward convergence speed, final efficiency

## **Step 2: Uncertainty Calibration**

* Track α, β evolution over time  
* Verify threshold adapts correctly to quantum dynamics  
* **Metric**: Expected Calibration Error (ECE), threshold sharpness

## **Step 3: Replay Buffer Analysis**

* Compare standard vs. adaptive buffer composition  
* Count "re-added" high-confidence transitions  
* **Metric**: Buffer diversity, information gain per sample

## **Step 4: Ablation Study**

* UDRM without epistemic weighting → epistemic only  
* UDRM without recalibration → fixed threshold  
* **Metric**: Identify which components matter most

## **6\. Key Parameters to Tune**

From Sheeraja's paper (adapted to quantum):

| Parameter | Sheeraja's Default | Suggested Quantum Value | Rationale |
| ----- | ----- | ----- | ----- |
| α\_initial | 99th percentile of unc | 95th percentile | Quantum systems more uncertain |
| β | log(2)/T\_total | log(2)/15000 | Longer horizon (15k frames) |
| recal\_interval | 5000 | 1000 | Quantum decoherence is faster |
| moving\_avg\_window | 100 | 50 | Tighter feedback for routing |
| unc\_threshold\_margin | 0.75 | 0.5 | Stricter for quantum reliability |
| min\_reward\_to\_readd | 0 (any reward) | 0.8 (high threshold) | Quantum success rates low |

## 

## **7\. Deliverables Timeline**

| Phase | Files | Effort | Deadline |
| ----- | ----- | ----- | ----- |
| **Phase 1** | uncertainty\_module.py | 4-6 hours | Week 1 |
| **Phase 2** | adaptive\_replay\_buffer.py | 6-8 hours | Week 2 |
| **Phase 3** | exp\_neural\_ucb\_uncertain.py | 8-10 hours | Week 3 |
| **Integration** | training\_loop.py \+ tests | 4-6 hours | Week 4 |
| **Evaluation** | Experiments \+ metrics \+ plots | 8-10 hours | Week 4-5 |

## **8\. Code References from Your Files**

**Sheeraja's Key Functions to Adapt:**

* Algorithm 1 (UDRM pseudocode) → Translate to quantum context  
* compute\_threshold() → Quantum-aware decay function  
* Loss functions: INTSCOREloss, COMCALloss → Optional (deep learning)

**Your EXPNeuralUCB Functions to Modify:**

* EXPNeuralUCB.takeaction() → Add uncertainty weighting  
* QuantumEnvironment.generateattackpattern() → Pass uncertainty feedback  
* Replay buffer sampling → Prioritize high-uncertainty transitions

## **9\. Research Impact**

**Innovation:**

* **First application** of evidential uncertainty to quantum routing  
* Shows uncertainty-driven exploration \> adversarial robustness alone  
* Hybrid approach: EXP3 (robustness) \+ UDRM (learning efficiency)

**Results Expected:**

* 15-25% faster convergence (fewer timesteps to high reward)  
* Better calibration under stochastic (non-adversarial) conditions  
* Adaptive threshold validates quantum environment assumptions

# **UDRM Integration Architecture v2.0**

## **Stateful Object Pattern \- Hierarchical State Management with Tracking Plan**

**Date:** January 17, 2026  
**Status:** PLANNING COMPLETE \- Ready for Implementation  
**Context:** UDRM is a **STATEFUL OBJECT**, not a configuration. It tracks state at multiple hierarchy levels: per-run, per-experiment, per-evaluator, and per framework execution.

## **📊 Quick Status Dashboard**

| Phase | Component | Status | Est. Time | Blocker |
| :---- | :---- | :---- | :---- | :---- |
| **Setup** | P8: Config Integration | Planning | 30 min | None |
| **Setup** | P6: UDRM Class | Planning | 2-3 hrs | None |
| **Framework** | P1: Entry Point | Ready | 15 min | P8, P6 |
| **Hierarchy** | P2: Evaluator Loop | Ready | 20 min | P1 |
| **Hierarchy** | P3: Experiment Loop | Ready | 20 min | P2 |
| **Core** | P4: Run Loop | Ready | 30 min | P3, P7 |
| **Integration** | P7: Uncertainty Calc | Ready | 45 min | P1 |
| **Cleanup** | P5: Aggregation | Ready | 30 min | P4 |

## **Executive Summary**

UDRM **must be created as an object** at the **framework configuration layer**, then passed down through the execution hierarchy—exactly like allocators. This enables:

1. **Per-physics-model state** \- Alpha/beta recalibration  
2. **Per-experiment state** \- Uncertainty history, moving averages  
3. **Per-run state** \- Individual transition uncertainties  
4. **Cross-run aggregation** \- Model-level statistics across experiments  
   

## **✓ Planning Artifacts Created**

* **UDRM-Integration-Tracking-Plan.md** \- Full roadmap with all 8 points detailed  
* **UDRM-Quick-Reference.md** \- Quick guide for session execution  
* **Architecture Flowchart** \- Visual representation of hierarchy

## **8 Integration Points Overview**

## **Setup Phase (Do First \- Unblocks All Others)**

**P8: Configuration Integration**

* Add UDRM parameters to framework config  
* Parameters: alpha\_recal\_interval, beta\_recal\_interval, moving\_avg\_window  
* Time: 30 min | Blocker: None

**P6: UDRM Class Implementation**

* Implement full UDRMObject class (\~200 lines)  
* Implement Algorithm 1 from Sheeraja's paper  
* Time: 2-3 hrs | Blocker: None

## 

## **Framework Integration Phase (Sequential)**

**P1: Framework Entry Point (QuantumExperimentRunner.init)**

* Add self.udrm\_obj \= None alongside the allocator  
* Load UDRM config from framework  
* Time: 15 min | Depends: P8, P6

**P2: Evaluator Loop (run\_evaluator)**

* Initialize UDRM state container evaluator\_udrm\_states \= {}  
* Create UDRM per physics model: self.udrm\_obj \= self.create\_udrm(model)  
* Call initialize\_exploration\_phase() for each UDRM  
* Time: 20 min | Depends: P1

**P3: Experiment Loop (run\_experiments\_for\_model)**

* Pass UDRM through all experiments  
* Track alpha/beta history per experiment  
* Time: 20 min | Depends: P2

**P4: Run Loop (run\_single\_experiment)**

* Call udrm.process\_transition() at each timestep  
* Pass both aleatoric and epistemic uncertainties  
* Time: 30 min | Depends: P3, P7

## 

## **Integration Phase (Parallel)**

**P7: Uncertainty Calculation Integration**

* Extract uncertainties from the algorithm  
* Add get\_aleatoric\_uncertainty() method  
* Add get\_epistemic\_uncertainty() method  
* Time: 45 min | Depends: P1

## 

## **Cleanup Phase (Final)**

**P5: Cleanup Sequence (cleanup\_evaluator)**

* Aggregate UDRM statistics per model  
* Get final alpha, beta, replay buffer stats  
* Save aggregated statistics to persistent storage  
* Time: 30 min | Depends: P4

## **How to Use This Plan**

## **For First Session**

1. Open **UDRM-Integration-Tracking-Plan.md** for detailed info  
2. Start with **P8** (Config) \- 30 minutes, unblocks everything  
3. Then **P6** (UDRM Class) \- 2-3 hours, core implementation  
4. Mark complete in the tracking document

## **For Subsequent Sessions**

1. Check the tracking document for the current status  
2. Pick the next integration point from the ordered list  
3. Follow the exact code patterns provided  
4. Update progress in tracking document  
5. Move to the next point when ✓ Complete

## **During Implementation**

* Use **UDRM-Quick-Reference.md** as a bookmark/quick lookup  
* Refer to the exact code locations in the full tracking document  
* Each point has acceptance criteria to verify completion

## **Architecture Pattern: Stateful Object Lifecycle**

## 

## **Level 0: Framework Entry Point**

class QuantumPathOptimizationFramework:  
    def \_\_init\_\_(self, config: FrameworkConfig):  
        *\# ✓ Stateful Objects (created ONCE at framework level)*  
        self.allocator\_obj \= None      *\# Created per physics model*  
        self.udrm\_obj \= None           *\# ← NEW: Created per physics model*

## **Level 1: Evaluator Loop (Set of Experiments)**

def run\_evaluator(self, evaluator\_type: str):  
    *\# Initialize UDRM state container for this evaluator*  
    evaluator\_udrm\_states \= {}  *\# Stores all model states*  
      
    for physics\_model in self.physics\_models:  
        *\# ✓ CREATE UDRM OBJECT (NEW \- same pattern as allocator)*  
        self.udrm\_obj \= self.create\_udrm(physics\_model)  
        *\# ✓ INITIALIZE UDRM (NEW \- exploration phase)*  
        self.udrm\_obj.initialize\_exploration\_phase(num\_timesteps=self.framework\_config\['prod\_frames'\])  
        *\# Store UDRM state for this model within evaluator*  
        evaluator\_udrm\_states\[physics\_model\] \= {  
            'udrm\_obj': self.udrm\_obj,  
            'alpha\_history': \[\],  
            'beta\_history': \[\],  
            'uncertainty\_history': \[\]  
        }

## **Level 2: Experiment Loop (Set of Runs)**

def run\_experiments\_for\_model(self, physics\_model: str, physics\_params: dict, current\_frames: int, frame\_step: int, udrm, udrm\_state\_tracker: dict):  
    *\# ✓ UDRM remains active (stateful) across all experiments*  
    for scale in self.scales:  
        for exp\_num in self.runs:  
            success \= self.run\_single\_experiment(  
                ...,  
                udrm=udrm  *\# ← UDRM stays active and stateful*  
            )  
              
            *\# Track experiment-level UDRM state*  
            if success:  
                udrm\_state\_tracker\['alpha\_history'\].append(udrm.alpha)  
                udrm\_state\_tracker\['beta\_history'\].append(udrm.beta)

## **Level 3: Run Loop (Individual Timesteps)**

def run\_single\_experiment(self, ..., allocator, udrm):  
    for timestep in range(current\_frames):  
        action \= runner.select\_action(state, timestep, udrm=udrm)  
        next\_state, reward, done \= environment.step(action)  
        *\# ✓ UDRM processes this transition (Algorithm 1\)*  
        udrm.process\_transition(  
            state=environment.state,  
            action=action,  
            reward=reward,  
            next\_state=next\_state,  
            timestep=timestep,  
            aleatoric\_unc=runner.get\_aleatoric\_uncertainty(),  
            epistemic\_unc=runner.get\_epistemic\_uncertainty()  
        )

## **Level 4: Cleanup Sequence**

def cleanup\_evaluator(self, udrm\_states: dict):  
    evaluation\_summary \= {'models': {}}  
    for physics\_model, state\_info in udrm\_states.items():  
        udrm\_obj \= state\_info\['udrm\_obj'\]  
        summary \= udrm\_obj.get\_state\_summary()  
        evaluation\_summary\['models'\]\[physics\_model\] \= {  
            'final\_alpha': summary\['alpha'\],  
            'final\_beta': summary\['beta'\],  
            'total\_replay\_buffer\_size': summary\['replay\_buffer\_size'\],  
            'transitions\_doubled': summary\['transitions\_added\_twice'\],  
        }  
    self.save\_udrm\_statistics(evaluation\_summary)

## **State Persistence Pattern**

| Level | Object | State Scope | Cleanup |
| :---- | :---- | :---- | :---- |
| **Evaluator** | UDRMObject | Aggregates across all models | After all models are complete |
| **Model** | UDRMObject | Per physics model (alpha/beta) | After experiments complete |
| **Experiment** | UDRMObject | Per experiment run (uncertainties) | Persists for next run |
| **Run** | UDRMObject | Per timestep (transitions) | Accumulates in the moving avg |

## **Implementation Roadmap**

## **Phase 1: Setup (Complete Planning)**

* Analyze existing code structure  
* Identify 8 integration points  
* Create tracking documents  
* Design state persistence pattern  
* **NEXT: Start P8 (Config Integration)**

## 

## **Phase 2: Implementation (Follows This Plan)**

* P8: Config (30 min)  
* P6: UDRM Class (2-3 hrs)  
* P1-P5, P7: Framework integration (2-3 hrs)  
* Testing & validation (1-2 hrs)

## 

## **Phase 3: Validation**

* Unit tests for the UDRM class  
* Integration tests with the framework  
* Validate against Sheeraja's Algorithm 1

## **Session Tracking**

## **Session 1: Planning & Architecture (Jan 17, 2026\)**

**Status:** ✓ COMPLETE

**Completed:**

* Analyzed your QuantumExperimentRunner codebase  
* Identified exact integration points (8 total)  
* Created dependency graph  
* Designed state tracking architecture  
* Created tracking documents

**Artifacts:**

* ✓ UDRM-Integration-Tracking-Plan.md (full roadmap)  
* ✓ UDRM-Quick-Reference.md (quick guide)  
* ✓ Architecture Flowchart (visual)  
* ✓ This updated canvas document

**Key Decisions:**

1. Follow the allocator pattern exactly  
2. P8 & P6 are blockers for all others  
3. Implement in strict order for minimal rework

## 

## **Key Insights**

## **Why UDRM is Stateful (Not Configuration)**

1. **Alpha Recalibration Across Experiments**  
   * Alpha depends on the percentile of exploration uncertainties  
   * Must persist across multiple runs to maintain consistency  
2. **Beta Decay Across Entire Training**  
   * Beta exponentially decays over timesteps  
   * The state must persist from timestep 0 to the final timestep  
3. **Moving Average Window**  
   * A 100-timestep window tracks the recent uncertainty trend  
   * Used for beta recalibration decisions  
   * Persists across experiment boundaries  
4. **Replay Buffer Statistics**  
   * Counts transitions added twice  
   * Tracks buffer size  
   * Aggregated per model and per evaluator  
5. **Uncertainty History**  
   * Stored uncertainties from the exploration phase  
   * Used for alpha initialization  
   * Cleaned up only after model experiments are complete

## **Documentation**

All details available in tracking documents:

**UDRM-Integration-Tracking-Plan.md:**

* Detailed description of each integration point  
* Exact code patterns for each point  
* Acceptance criteria for verification  
* Task checklists and dependencies


**UDRM-Quick-Reference.md:**

* Quick lookup guide  
* Key patterns at a glance  
* Status tracking template  
* Decision tree for common questions

## **✓ Ready for Implementation**

**When you're ready to code:**

1. Open UDRM-Integration-Tracking-Plan.md  
2. Follow Point P8 (Config Integration) exactly  
3. I'll provide precise code with before/after  
4. Mark complete and move to P6  
5. Continue through all 8 points in order

**Current Status:** Planning Complete \- Ready to Start Coding  
Let me know which point you want to tackle first\!

# **UDRM Integration Points Tracking Plan**

Status: Planning & Scoping  
Date Created: January 17, 2026  
Last Updated: January 17, 2026  
Owner: GA \- AI/Quantum Computing

## **Overview**

This document tracks the UDRM Integration Roadmap — a comprehensive plan to integrate Sheeraja's Uncertainty-Driven Replay Memory (UDRM) into the existing quantum path optimization framework.

## **Purpose**

* Track Integration Points \- Know exactly where UDRM fits in your code  
* Manage Dependencies \- Understand what needs to be done before what  
* Monitor Progress \- Update status as we implement each piece  
* Share Context \- Quick reference for returning to work

## **Success Criteria**

UDRM object created alongside the allocator at the framework level  
UDRM flows through all hierarchy levels (evaluator → experiment → run → timestep)  
Transition processing integrated with uncertainty calculations  
State aggregation works across runs, experiments, and models  
The cleanup sequence properly releases resources

## **Integration Points Summary**

| Point | Location | Status | Owner | Notes |
| :---- | :---- | :---- | :---- | :---- |
| P1 | Framework Entry | Planning | GA | Add UDRM obj to \_\_init\_\_ |
| P2 | Evaluator Loop | Planning | GA | Create UDRM per model |
| P3 | Experiment Loop | Planning | GA | Pass UDRM through runs |
| P4 | Run Loop | Planning | GA | Call process\_transition() |
| P5 | Cleanup Sequence | Planning | GA | Aggregate & release state |
| P6 | UDRM Class | Planning | GA | Implement a full class |
| P7 | Uncertainty Calc | Planning | GA | Integrate with algorithms |
| P8 | Config Integration | Planning | GA | Add UDRM params to config |

## **Detailed Integration Points**

## **Point 1: Framework Entry Point (QuantumExperimentRunner.init)**

File: Your experiment runner class  
Current Code Section:  
def \_\_init\_\_(self, id=0, config=ExperimentConfiguration(None, None), ...):  
    self.configs \= config if config is not None else ExperimentConfiguration()  
    self.allocator\_obj \= None  
    *\# ADD UDRM HERE*  
Tasks:

*  Add self.udrm\_obj \= None alongside the allocator  
*  Add self.udrm\_config dictionary for UDRM parameters  
*  Load UDRM config from framework config file  
*  Document the initialization pattern

Expected Code:  
self.allocator\_obj \= None      *\# Existing*  
self.udrm\_obj \= None           *\# NEW*  
self.udrm\_config \= {  
    'alpha\_recal\_interval': self.configs.get('udrm\_alpha\_recal\_interval', 50),  
    'beta\_recal\_interval': self.configs.get('udrm\_beta\_recal\_interval', 5000),  
    'moving\_avg\_window': self.configs.get('udrm\_moving\_avg\_window', 100),  
    'exploration\_phase\_fraction': 0.1,  
}  
Acceptance Criteria:

* ✓ UDRM object initialized to None  
* ✓ Config parameters loaded from framework config  
* ✓ Pattern mirrors allocator initialization

## **Point 2: Evaluator Loop (run\_evaluator Method)**

File: Your evaluator/runner orchestrator  
Current Pattern: Creates an allocator per physics model  
Tasks:

*  Initialize evaluator\_udrm\_states \= {} container  
*  Create a new UDRM object per physics model  
*  Call initialize\_exploration\_phase() after creation  
*  Store UDRM reference and tracking state  
*  Pass UDRM to the experiment loop

Expected Structure:  
def run\_evaluator(self, evaluator\_type: str):  
    evaluator\_udrm\_states \= {}  *\# NEW*  
      
    for physics\_model in self.physics\_models:  
        self.allocator\_obj \= self.create\_allocator(physics\_model)  
        self.udrm\_obj \= self.create\_udrm(physics\_model)  *\# NEW*  
        self.udrm\_obj.initialize\_exploration\_phase(  
            num\_timesteps=self.configs\['prod\_frames'\]  
        )  
    
        evaluator\_udrm\_states\[physics\_model\] \= {  
            'udrm\_obj': self.udrm\_obj,  
            'alpha\_history': \[\],  
            'beta\_history': \[\],  
            'uncertainty\_history': \[\]  
        }  
          
        self.run\_experiments\_for\_model(  
            ...,  
            udrm=self.udrm\_obj,  
            udrm\_state\_tracker=evaluator\_udrm\_states\[physics\_model\]  
        )

Acceptance Criteria:

* ✓ UDRM object created per physics model  
* ✓ Exploration phase initialized correctly  
* ✓ State tracking container properly structured  
* ✓ UDRM passed to experiment loop

## **Point 3: Experiment Loop (run\_experiments\_for\_model Method)**

File: Same file as Point 2  
Current Pattern: Loops through experiments with allocator  
Tasks:

*  Add the udrm parameter to the method signature  
*  Add the udrm\_state\_tracker parameter for history tracking  
*  Pass UDRM to each experiment run  
*  Track alpha/beta history after each run  
*  Track uncertainty history

Expected Structure:  
def run\_experiments\_for\_model(self, physics\_model, physics\_params,   
                              current\_frames, frame\_step, udrm, udrm\_state\_tracker):  *\# NEW params*  
    for scale in self.scales:  
        for exp\_num in self.runs:  
            success \= self.run\_single\_experiment(  
                ...,  
                udrm=udrm  *\# NEW*  
            )  
            if success:  
                udrm\_state\_tracker\['alpha\_history'\].append(udrm.alpha)  
                udrm\_state\_tracker\['beta\_history'\].append(udrm.beta)  
                udrm\_state\_tracker\['uncertainty\_history'\].extend(  
                    udrm.stored\_uncertainties\[-100:\]  
                )  
Acceptance Criteria:

* ✓ UDRM parameter properly threaded through  
* ✓ State tracking captures alpha/beta history  
* ✓ Uncertainty history captured per experiment

## **Point 4: Run Loop (run\_single\_experiment Method)**

File: Same file as Points 2-3  
Current Pattern: Timestep loop with allocator updates  
Tasks:

*  Add the udrm parameter to the method signature  
*  Pass UDRM to action selection  
*  Call udrm.process\_transition() per timestep  
*  Extract/compute uncertainties from the algorithm  
*  Handle both aleatoric and epistemic uncertainty

Expected Structure:  
def run\_single\_experiment(self, physics\_model, scale, experiment\_num,  
                         physics\_params, current\_frames, frame\_step, allocator, udrm):  *\# NEW param*  
    for timestep in range(current\_frames):  
        action \= runner.select\_action(  
            state=environment.state, timestep=timestep, udrm=udrm  *\# Pass to action selection*  
        )  
        next\_state, reward, done \= environment.step(action)  
          
        *\# NEW: UDRM processes transition*  
        udrm.process\_transition(  
            state=environment.state,  
            action=action,  
            reward=reward,  
            next\_state=next\_state,  
            timestep=timestep,  
            aleatoric\_unc=runner.get\_aleatoric\_uncertainty(),  
            epistemic\_unc=runner.get\_epistemic\_uncertainty()  
        )  
Acceptance Criteria:

* ✓ UDRM.process\_transition called at each timestep  
* ✓ Uncertainties properly extracted/computed  
* ✓ Transition state recorded in UDRM

## **Point 5: Cleanup Sequence (cleanup\_evaluator Method)**

File: Same file as Points 2-4  
Current Pattern: Post-experiment cleanup  
Tasks:

*  Create cleanup\_evaluator() method  
*  Iterate through the udrm\_states dictionary  
*  Call get\_state\_summary() on each UDRM object  
*  Aggregate statistics per model  
*  Save aggregated statistics to a file  
*  Clean up and release UDRM objects

Expected Structure:  
def cleanup\_evaluator(self, udrm\_states: dict):  
    """Clean up after evaluator completes."""  
    print("🧹 CLEANUP: Evaluator-level UDRM aggregation")  
    evaluation\_summary \= {'models': {}}  
    for physics\_model, state\_info in udrm\_states.items():  
        udrm\_obj \= state\_info\['udrm\_obj'\]  
        summary \= udrm\_obj.get\_state\_summary()  
        evaluation\_summary\['models'\]\[physics\_model\] \= {  
            'final\_alpha': summary\['alpha'\],  
            'final\_beta': summary\['beta'\],  
            'total\_replay\_buffer\_size': summary\['replay\_buffer\_size'\],  
            'transitions\_doubled': summary\['transitions\_added\_twice'\],  
            'avg\_uncertainty': summary\['avg\_uncertainty'\]  
        }  
    self.save\_udrm\_statistics(evaluation\_summary)  
    for state\_info in udrm\_states.values():  
        state\_info\['udrm\_obj'\] \= None  
    gc.collect()  
Acceptance Criteria:

* ✓ UDRM state properly summarized  
* ✓ Statistics aggregated per model  
* ✓ Statistics saved to persistent storage  
* ✓ Resources properly released

## **Point 6: UDRM Class Implementation**

File: New file udrm\_object.py or in the existing algorithm file  
Status: Designed (in canvas), not yet implemented  
Tasks:

*  Create the UDRMObject class with full implementation  
*  Implement \_\_init\_\_() with state initialization  
*  Implement initialize\_exploration\_phase()  
*  Implement process\_transition() (Algorithm 1 from paper)  
*  Implement alpha/beta recalibration logic  
*  Implement threshold calculation  
*  Implement get\_state\_summary() for monitoring

Key Methods:  
class UDRMObject:  
    def \_\_init\_\_(self, physics\_model: str, config: dict)  
    def initialize\_exploration\_phase(self, num\_timesteps: int)  
    def process\_transition(self, state, action, reward, next\_state, timestep, ...)  
    def \_initialize\_alpha\_beta(self)  
    def \_calculate\_threshold(self, timestep: int) \-\> float  
    def get\_state\_summary(self) \-\> dict  
Acceptance Criteria:

* ✓ All state variables properly initialized  
* ✓ Process\_transition follows Algorithm 1 exactly  
* ✓ Alpha/beta recalibration is working correctly  
* ✓ State summary provides comprehensive monitoring

## **Point 7: Uncertainty Calculation Integration**

File: Your algorithm classes (EXPNeuralUCB, GNeuralUCB, etc.)  
Current Pattern: Algorithms compute internal uncertainties  
Tasks:

*  Identify where aleatoric uncertainty is computed  
*  Identify where epistemic uncertainty is computed  
*  Add get\_aleatoric\_uncertainty() method to runner  
*  Add get\_epistemic\_uncertainty() method to runner  
*  Ensure uncertainties are in \[0, 1\] or a normalized range  
*  Document uncertainty computation source

Expected Integration:  
class QuantumExperimentRunner:  
    def get\_aleatoric\_uncertainty(self) \-\> float:  
        """Extract aleatoric (data) uncertainty from algorithm."""  
        *\# Get from neural network confidence bounds*  
        return self.algorithm.get\_aleatoric\_unc()  
    def get\_epistemic\_uncertainty(self) \-\> float:  
        """Extract epistemic (model) uncertainty from algorithm."""  
        *\# Get from exploration parameter or network variance*  
        return self.algorithm.get\_epistemic\_unc()  
Acceptance Criteria:

* ✓ Both uncertainty types were properly extracted  
* ✓ Uncertainties in the correct value range  
* ✓ Computation matches algorithm implementation

## **Point 8: Configuration Integration**

File: Your config file (YAML, dict, or ExperimentConfiguration)  
Tasks:

*  Add UDRM configuration section  
*  Define alpha recalibration interval (default: 50\)  
*  Define beta recalibration interval (default: 5000\)  
*  Define moving average window size (default: 100\)  
*  Define exploration phase fraction (default: 0.1)  
*  Document each parameter

Expected Config Structure:  
udrm\_config:  
  alpha\_recal\_interval: 50  
  beta\_recal\_interval: 5000  
  moving\_avg\_window: 100  
  exploration\_phase\_fraction: 0.1  
  threshold\_comparison\_tolerance: 0.75  
  reward\_threshold: 0  
Acceptance Criteria:

* ✓ All parameters present in the config  
* ✓ Default values are reasonable for the quantum domain  
* ✓ Parameters properly documented

## **Dependencies & Order**

┌─────────────────────────────────────────┐  
│ P8: Config Integration                  │  
│ (Must happen first \- all points read)   │  
└────────────┬────────────────────────────┘  
             ▼  
┌─────────────────────────────────────────┐  
│ P6: UDRM Class Implementation           │  
│ (Core logic \- needed by all points)     │  
└────────────┬────────────────────────────┘  
             ▼  
┌─────────────────────────────────────────┐  
│ P1: Framework Entry Point               │  
│ (Initialize UDRM obj creation)          │  
└────────────┬────────────────────────────┘  
             ▼  
┌─────────────────────────────────────────┐  
│ P2: Evaluator Loop                      │  
│ (Create UDRM per model)                 │  
└────────────┬────────────────────────────┘  
             ▼  
┌─────────────────────────────────────────┐  
│ P3: Experiment Loop                     │  
│ (Pass UDRM through experiments)         │  
└────────────┬────────────────────────────┘  
             ▼  
┌───────────────────────────────────────────┐  
│ P4: Run Loop \+ P7: Uncertainty Calc       │  
│ (Call process\_transition w/ uncertainties)│  
└────────────┬──────────────────────────────┘  
             ▼  
┌─────────────────────────────────────────┐  
│ P5: Cleanup Sequence                    │  
│ (Aggregate stats, release resources)    │  
└─────────────────────────────────────────┘  
Critical Path: P8 → P6 → P1 → P2 → P3 → (P4 \+ P7) → P5

## **Progress Tracker**

## **Phase 1: Planning & Setup**

*  P8 \- Configuration Integration (DEPENDENCY FOR ALL)  
  * Status: Not Started  
  * Est. Time: 30 min  
  * Owner: GA  
*  P6 \- UDRM Class Implementation (DEPENDENCY FOR P1-5)  
  * Status: Not Started  
  * Est. Time: 2-3 hours  
  * Owner: GA

## **Phase 2: Framework Integration**

*  P1 \- Framework Entry Point  
  * Status: Not Started  
  * Est. Time: 15 min  
  * Owner: GA  
  * Depends On: P8, P6  
*  P2 \- Evaluator Loop  
  * Status: Not Started  
  * Est. Time: 20 min  
  * Owner: GA  
  * Depends On: P1  
*  P3 \- Experiment Loop  
  * Status: Not Started  
  * Est. Time: 20 min  
  * Owner: GA  
  * Depends On: P2

## **Phase 3: Core Integration**

*  P4 \- Run Loop (Transition Processing)  
  * Status: Not Started  
  * Est. Time: 30 min  
  * Owner: GA  
  * Depends On: P3, P7  
*  P7 \- Uncertainty Calculation Integration  
  * Status: Not Started  
  * Est. Time: 45 min  
  * Owner: GA  
  * Depends On: P1

## **Phase 4: Finalization**

*  P5 \- Cleanup Sequence  
  * Status: Not Started  
  * Est. Time: 30 min  
  * Owner: GA  
  * Depends On: P4  
*  Testing \- Validate all integration points  
  * Status: Not Started  
  * Est. Time: 1-2 hours  
  * Owner: GA

## **Session Log**

## **Session 1: Planning & Scoping (Jan 17, 2026\)**

Duration: \~1 hour  
Attendees: GA  
Tasks Completed:

* Analyzed existing QuantumExperimentRunner code  
* Identified 8 integration points  
* Mapped dependency graph  
* Created this tracking document

Decisions Made:

1. UDRM follows the allocator pattern exactly  
2. P8 (config) and P6 (class) are blockers for all others  
3. Will implement in phases: Setup → Framework → Core → Finalization

Open Questions:

* Where exactly are uncertainties computed in your neural algorithms?  
* Are you already tracking uncertainty in your bandit implementations?

Next Session: Start with P8 (Config Integration)

## **Artifact Locations**

When we start coding, here are the exact locations:  
Your Code Structure:  
├── quantumexperimentrunner.py     ← P1, P2, P3, P4, P5  
├── udrm\_object.py                 ← P6 (NEW FILE)  
├── quantumalgorithms.py           ← P7 (update existing)  
├── framework\_config.yml           ← P8 (update existing)  
└── quantummodel.py                ← May need updates for uncertainty

## **Lessons & Patterns**

## **Pattern 1: Stateful Objects**

UDRM is a stateful object (like an allocator), not a configuration:

* Created once per physics model  
* Persists across the entire set of experiments  
* Accumulates state (not reset between runs)  
* Provides a final summary at cleanup

## 

## **Pattern 2: Hierarchical Passing**

Objects flow down the hierarchy:

* Framework creates an object  
* Evaluator passes to experiments  
* Experiments pass to runs  
* Runs are used at the timestep level  
* Cleanup aggregates state upward

## 

## **Pattern 3: State Tracking Containers**

Use dict to track state per model:  
state\_tracker \= {  
    'model\_1': {  
        'udrm\_obj': \<object\>,  
        'alpha\_history': \[\],  
        'beta\_history': \[\],  
        'uncertainty\_history': \[\]  
    }  
}

# **UDRM Integration Quick Reference**

Quick Guide for Tracking & Executing UDRM Integration  
Status: Active Planning Phase  
Print/Bookmark This

## **At a Glance**

UDRM Integration \= 8 Integration Points  
START HERE ↓  
┌─────────────────────────────────────┐  
│ P8: Config (30 min)                 │ ← Do FIRST (unblocks everything)  
│ P6: UDRM Class (2-3 hrs)            │ ← Do SECOND (needed by all)  
└─────────────┬───────────────────────┘  
              ↓  
    ┌─────────────────────┐  
    │ Framework Level     │  
    │ P1: Entry (15 min)  │  
    └──────────┬──────────┘  
               ↓  
    ┌─────────────────────┐  
    │ Hierarchy Flow      │  
    │ P2: Eval (20 min)   │  
    │ P3: Exp (20 min)    │  
    │ P4: Run (30 min)    │  
    └──────────┬──────────┘  
               ↓  
    ┌─────────────────────┐  
    │ Integration         │  
    │ P7: Unc (45 min)    │  
    └──────────┬──────────┘  
               ↓  
    ┌─────────────────────┐  
    │ Cleanup             │  
    │ P5: Cleanup (30 min)│  
    └─────────────────────┘

## **Integration Points Checklist**

## **Setup Phase (Do First)**

*  P8 \- Add UDRM config parameters  
*  P6 \- Implement the UDRMObject class

## **Integration Phase (Do After Setup)**

*  P1 \- Add UDRM to framework init  
*  P2 \- Create UDRM in evaluator loop  
*  P3 \- Pass UDRM through experiment loop  
*  P4 \- Call process\_transition in run loop  
*  P7 \- Integrate uncertainty extraction  
*  P5 \- Add cleanup aggregation

## **Testing Phase**

*  Unit test UDRM class  
*  Integration test full flow  
*  Validate against paper Algorithm 1

## 

## **Key Code Patterns**

## 

## **Pattern 1: Creating & Initializing**

*\# P1: Framework init*  
self.udrm\_obj \= None  
self.udrm\_config \= {...}  
*\# P2: Evaluator loop*  
self.udrm\_obj \= self.create\_udrm(physics\_model)  
self.udrm\_obj.initialize\_exploration\_phase(num\_timesteps)

## **Pattern 2: Passing Through Hierarchy**

*\# P3: Experiment loop*  
self.run\_experiments\_for\_model(..., udrm=self.udrm\_obj, ...)  
*\# P4: Run loop*  
udrm.process\_transition(state, action, reward, next\_state, timestep, ...)

## **Pattern 3: Tracking State**

*\# P2: Store tracking dict*  
evaluator\_udrm\_states \= {model: {'udrm\_obj': obj, 'alpha\_history': \[\], ...}}  
*\# P3: Update history after each run*  
udrm\_state\_tracker\['alpha\_history'\].append(udrm.alpha)  
*\# P5: Aggregate at cleanup*  
summary \= udrm\_obj.get\_state\_summary()

## **File Locations**

| Point | File | Method | Action |
| :---- | :---- | :---- | :---- |
| P1 | runner.py | \_\_init\_\_ | Add 2 lines |
| P2 | runner.py | run\_evaluator | Add 10 lines |
| P3 | runner.py | run\_experiments | Add 5 lines |
| P4 | runner.py | run\_single\_experiment | Add 1 call |
| P5 | runner.py | cleanup\_evaluator | New method |
| P6 | udrm.py | (new file) | \~200 lines |
| P7 | algorithms | methods | Extract uncertainty |
| P8 | config | YAML/dict | Add 6 params |

## **Remember**

1. Order Matters \- Start with P8 & P6, they unblock others  
2. Follow Allocator Pattern \- UDRM mirrors allocator creation/passing  
3. State is King \- UDRM isn't a configuration, it's a stateful object  
4. Persist Through Experiments \- Alpha/beta DON'T reset between runs  
5. Pass Down, Aggregate Up \- Created at top, flows down, aggregates at cleanup

## **Quick Status Check**

Update this when you start each point:  
Session Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
P8 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P6 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P1 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P2 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P3 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P4 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P7 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
P5 ☐ Not Started  ☐ In Progress  ☐ Complete  (Time: \_\_)  
Overall: \_\_\_% Complete  
Blockers: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Next: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## 

## **Decision Tree**

**Q: Where do I start?**  
A: Start with P8 (config) \+ P6 (class)  
**Q: What if I don't know uncertainties?**  
A: Document where they should come from in P7, implement later  
**Q: Can I do P4 without P7?**  
A: No \- P4 needs uncertainties from P7  
**Q: What if something's not clear?**  
A: Check the full tracking document, section by section  
**Q: How do I know it's working?**  
A: UDRM state changes (alpha/beta values), tracked in udrm\_states dict

