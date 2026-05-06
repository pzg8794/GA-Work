# Research Communications Reference Log
**Piter Garcia & Dan Krutz**  
Period: December 25, 2025 - January 7, 2026

---

## Purpose
This document serves as a comprehensive record of all research discussions, requests, and responses between Piter and Dan to ensure continuity, avoid redundant conversations, and maintain a single source of truth for research collaboration.

---

## SECTION 1: CHRONOLOGICAL COMMUNICATION TIMELINE

### Communication #1
**Date:** December 25, 2025 (3:26 AM)  
**From:** Piter Garcia  
**To:** Dan Krutz (and Devroop)

**Subject:** Paper 2 & Paper 7 Testing Complete + Progress Update

**Piter's Communication:**
- Paper 2 Testing Results (Default vs Dynamic Allocators):
  - Default allocator: Stochastic avg efficiency 92.8% (CPursuit/iCPursuit lead at 93.0-93.4%)
  - Dynamic allocator: Stochastic avg efficiency 92.7% (similar winners)
  - Markov adversarial results: efficiency drop to ~60% (59-62% range)
  - Key finding: Dynamic allocator provides marginal improvement in Markov scenarios (59-62% vs lower with Fixed)

- Paper 7 Testing Results (Baseline with 100 frames, Dynamic with 50 frames):
  - Default (100 frames): EXPNeuralUCB leads across scenarios (54.7% Stochastic, 41.7% Markov, 42.3% Adaptive)
  - Dynamic (50 frames): Mixed results - GNeuralUCB and iCPursuit alternating wins; iCPursuit leads Markov (63-65%)
  - Note: Smaller frame sizes indicate K (arms per path) may be limiting exploration
  - Performance lower (40-55% range) vs Paper 2 (92-93%), suggesting frame/capacity dependency

- Dynamic Physics Implementation:
  - Generalized get_physics_params_paper12() ready for arbitrary num_paths/arms_per_path
  - Successfully removes hardcoded '4' constraint - now supports 50+ paths scalably
  - Implementation tested in test pipeline; no shape inconsistencies reported

- Next Steps & Timeline:
  - Paper 2 results solid → running baseline with new testbed
  - Paper 7 results solid → running baseline with new testbed
  - Paper 12 integration done, tests running
  - README contribution guide in progress
  - Master datasets notebook being updated as new tests run

**Attachments Provided:**
- quantum_exps-Dynamic(paper2)_alloc-all_envs-5_attacks-1400_100-5_runs-S2T_20251224_log.txt
- quantum_exps-Dynamic(paper7)_alloc-all_envs-5_attacks-50_50-4_runs-S2T_20251225_log.txt
- quantum_exps-Default(paper2)_alloc-all_envs-5_attacks-1400_100-5_runs-S2T_20251224_log.txt
- quantum_exps-Default(paper7)_alloc-all_envs-5_attacks-100_100-1_runs-S2T_20251224_log.txt

---

### Communication #2
**Date:** December 26, 2025 (2:39 PM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Request:**

1. **Overleaf Document Clarification**
   - Question: "Is there an updated Overleaf document that is currently being updated that I should/can look at?"
   - Context: "I'm wondering as there are a bunch of projects and I want to make sure that I am looking at the correct one."

2. **Comparative Analysis Writeup**
   - Request: "Do you have a short writeup comparing your work to existing works that use MABs to address stochastic scenarios?"
   - Specific need: "What makes your work better/different?"
   - Length requirement: "At most, 1 page at most. Just keep it short/to the point."

3. **Primary Research Thrusts Description**
   - Request: "Briefly mention the primary thrusts of your work."
   - Example clarification: "For example, do you *just* utilize a special kind of MABs for path planning?"
   - Format: "I'd envision the above writeup to be 1 page at most."

**Status at request:** Awaiting response

---

### Communication #3
**Date:** December 28, 2025 (8:34 AM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Questions:**
1. "Did you ever touch base with Sheeraja?"
2. "What is your slack username (if you use Slack)?"

**Context:** Dan planning to coordinate with Sheeraja, needs Piter's Slack contact information.

**Status at request:** Awaiting response

---

### Communication #4
**Date:** December 28, 2025 (2:12 PM)  
**From:** Piter Garcia  
**To:** Dan Krutz

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Piter's Response:**
1. **Sheeraja Contact:** "I haven't had the chance to connect with Sheeraja yet, but I can reach out once I have his contact information."
   
2. **Slack Username:** "My Slack username is Piter Garcia"
   - Alternative contact: "I'm also easily reachable at pzg8794@g.rit.edu if that's more convenient."

3. **Regarding Earlier Request:** "Regarding your previous email, I'll provide a comprehensive response once I've finished validating the testbed integration and reviewed the findings."
   - Timeline: "Based on the preliminary results, I believe the allocator comparison and performance insights will be valuable additions to the paper, so I'll include relevant findings in my follow-up."

4. **Request for Sheeraja's Email:** "Do you have Sheeraja's email? I can send him a message directly via Slack once I have it."

**Status:** Waiting for Sheeraja's email and readiness to provide comprehensive response to Dan's earlier requests.

---

### Communication #5
**Date:** December 29, 2025 (9:10 AM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Statements & Information:**
1. **Slack Issue:** "I am doing something really dumb and cannot find you on slack. Could you send me a message: dxkvse@g.rit.edu on slack."
   - Note: Dan prefers to be contacted via Slack at dxkvse@g.rit.edu

2. **Response Expectations:** "I am not looking for a super comprehensive response. A high level 1-3 paragraph overview would be suffice."
   - Clarification: "To be clear, this is a writeup for proposed work; not something that you would have needed to have accomplished."

3. **Sheeraja Contact Information Provided:** "Sheeraja email is: sheeraja@mail.rit.edu"

4. **Dan's Schedule Note:** "I have a roadtrip coming up..." (message truncated)

**Status:** Dan expects brief 1-3 paragraph response on proposed work overview.

---

### Communication #6
**Date:** December 31, 2025 (3:28 AM)  
**From:** Piter Garcia  
**To:** Dan Krutz

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**MAJOR RESPONSE - Comprehensive Framework & Research Writeup**

#### Part A: Overleaf Document Link Clarification
- **Current Working Document:** https://www.overleaf.com/project/68ea344896594f27b427ca8f
- **Gray-Out Review View:** https://www.overleaf.com/read/ttmrwxyfqjfy#38bfea (abstract, research questions, results only) - prepared for Professor Travis feedback
- **Status:** One primary Overleaf project; the second link is a review/read view of prepared content for feedback, not a separate active project source

#### Part B: Framework Evolution & Research Contributions (5-Paper Progression)

**Paper 1 - Baseline Replication (EXPNeuralUCB Framework)**
- Replicated quantum routing paper's setup
- Extended beyond hardcoded 10K capacity to scaled regimes (SC = 1T, 1.5T, 2T)
- Exposed allocation overfitting in original design

**Paper 2 - Predictive Enhancement (iCMAB Framework)**
- Incorporated context-aware Pursuit variants (CPursuit, iCPursuit)
- Added topology awareness, neural feature extraction, world modeling
- Went beyond simple reward history

**Paper 3 - Multi-Model Comparative Framework (Convergence Point)**
- Benchmarked 4 algorithms × 5 attack scenarios × 4 allocators = 60 conditions
- CPursuit dominance: 89% efficiency, 60% win rate vs. EXPNeuralUCB's 78%, 5%
- Thompson Sampling: 88.2% efficiency with 3× speedup (3.52h vs 11.62h)
- Fixed Allocator Trap: 6.4% generalization penalty under dynamic allocation

**Paper 4a - Stochastic vs Adversarial Evaluation**
- Introduced 5 adversarial regimes (Baseline, Stochastic, Markov, Adaptive, OnlineAdaptive)
- Quantify variance and vulnerability across conditions

**Paper 4b - Hybrid MABs Evaluation Framework**
- Focused on hybrid combinations (CPursuit+Thompson)
- Consistent dominance in high-variance environments
- Discovered attack-allocator synergies (+2.7% to -26.5%) that inform deployment strategies

**Paper 5 - Dynamic Routing Synthesis (CURRENT)**
- Integrated findings from Papers 1-4 into full-stack routing
- Scenario-aware strategy pairing (CPursuit+Thompson for OnlineAdaptive)
- Resource-bound variants (1T, 1.5T, 2T capacity scaling)
- Attack-allocator interaction rules for threat-based deployment

#### Part C: How This Differs from Existing Stochastic MAB Work

1. **Multi-scenario stress testing:** Five adversarial models reveal brittleness invisible in single-environment evaluation
2. **Cross-allocator generalization:** EXPNeuralUCB succeeds under Fixed+Markov (original paper's exact conditions) but wins only 1/20 scenario-allocator combinations overall
3. **Allocator-algorithm synergies:** Markov+Dynamic UCB improves +2.7%; Adaptive+Random collapses -26.5%, creating pairing rules
4. **Efficiency under constraint:** Thompson Sampling achieves Fixed-level efficiency while cutting runtime by 3×—not captured in single-allocator benchmarks

#### Part D: Primary Research Thrusts

Beyond specialized MAB path planning:
- **Evaluation methodology:** Exposes systematic bias in fixed-allocation testing (standard practice including the quantum paper), quantified via 6.4% generalization penalty metric
- **Co-design principles:** Allocators and algorithms must be tuned jointly—optimal pairs (CPursuit+Thompson) achieve 97-98% peak efficiency
- **Deployment taxonomy:** Four winner types (scenario-specific, gap-reduction, efficiency, overall robustness) distinguish production contexts

#### Part E: One-Page Summary
"Context-aware Pursuit algorithms with probabilistic allocation achieve superior generalization (89% efficiency, 7.9% CV, 72.9% floor) vs. exponential weighting with fixed allocation (78%, 10.9% CV, 54% floor). Single-allocator evaluations mask critical failure modes—our framework quantifies this bias and provides deployment-ready guidelines for robust quantum routing and general MAB systems under realistic threat conditions."

#### Part F: Questions for Dan

1. **Hour Logging:** "I stopped logging hours when the semester ended last week. Should I continue tracking hours, or pause until Spring semester begins?"
2. **Spring Continuation:** "As I finalize my Spring schedule, can you confirm whether the GA position continues through Spring semester?"

**Status:** Comprehensive response provided; awaiting feedback on questions.

---

### Communication #7
**Date:** January 2, 2026 (6:48 AM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Requests:**

1. **Overleaf Access**
   - Request: "Could you give me access to this page: https://www.overleaf.com/project/6945bfa58266e8759ad66f24"
   - Note: This is the CONDENSED version (abstract, research questions, results only)

2. **Slack Contact**
   - Request: "Could you send me a message on Slack. My username is dxkvse@g.rit.edu"

3. **Process Overview Expansion**
   - Request: "Could you send me a 2-3 sentence overview of how our proposed process works?"
   - Scope: "You don't need to mention results, just give an overview of the process."
   - Context: "I'd also add this overview of your process to the abstract of your working version."
   - Current state assessment: "I think that it just jumps from the proposed problem to your findings?"
   - Suggestion: "You kind of touch base on your process in I.b of the introduction, but I would double or triple the length of this description as it is pretty high level."

4. **Meeting Request**
   - "We will touch base next week. How does your Monday morning work, say around 10?"

**Status:** Three-part action items awaiting response; meeting proposed for Monday 10 AM.

---

### Communication #8
**Date:** January 2, 2026 (10:37 AM)  
**From:** Piter Garcia  
**To:** Dan Krutz

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Piter's Status Update:**
- "I will get back to you as soon as I am out of bed, I have been ill in bed for about three days now."

**Status:** Delayed response due to illness; recovery in progress.

---

### Communication #9
**Date:** January 2, 2026 (9:11 PM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Response to Illness:**
- "I am sorry to hear this. Feel better soon"

**Status:** Supportive acknowledgment; awaiting Piter's recovery.

---

### Communication #10
**Date:** January 5, 2026 (8:50 PM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Check-in & Request:**
1. **Wellness Check:** "Hi Piter, I am just checking in to see how you are doing."
2. **Overleaf Access (Second Request):** "Also, could you give me access (dan7800@yahoo.com) access to https://www.overleaf.com/project/6945bfa58266e8759ad66f24"

**Status:** Follow-up on wellness and Overleaf access; awaiting response.

---

### Communication #11
**Date:** January 7, 2026 (1:29 AM)  
**From:** Piter Garcia  
**To:** Dan Krutz

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Piter's Recovery & Clarifications:**

1. **Health Status:** "I've been recovering slowly—it's taken longer than expected, but I've finally been able to get out of bed and am now catching up on emails and resuming my work on finalizing my schedule for the semester."

2. **Overleaf Link Clarification (IMPORTANT):**
   - "I wanted to clarify something regarding the Overleaf link you sent (https://www.overleaf.com/project/6945bfa58266e8759ad66f24)."
   - "I'm not sure where that link came from, but it doesn't seem connected to any of my projects."
    - **Clarification:** "As far as I know, there is one primary source project and one review view:
     - The project you originally created: https://www.overleaf.com/project/68ea344896594f27b427ca8f
       - The gray-out review view prepared for Professor Travis (also shared with you): https://www.overleaf.com/read/ttmrwxyfqjfy#38bfea
       - The review view is for feedback convenience, not a separate active source project."

3. **Schedule & GA Questions:** "Also, I've resumed putting together my schedule—especially around GA responsibilities—and wanted to circle back since some of my earlier questions may have been missed during the end-of-semester rush. Let me know if you'd like me to resend anything."

4. **Slack Account Clarification:** "Lastly, I did send you a message on Slack. I was able to find your account in the main RIT workspace under @Daniel Krutz (dxkvse / dxkvse@rit.edu), but not in the MS Data Science channel."

5. **Future Coordination:** "I'll be meeting with Devroop and Sheeraja soon to discuss next steps—let me know if you'd like to be added to those meetings."

**Status:** Recovering; clarified single-source Overleaf setup with review view for Travis; ready to resend earlier questions; awaiting Dan's Slack confirmation.

---

### Communication #12
**Date:** January 7, 2026 (5:59 AM)  
**From:** Dan Krutz  
**To:** Piter Garcia

**Subject:** Re: Paper 2 & Paper 7 Testing Complete + Progress Update

**Dan's Response & Questions:**

1. **Wellness:** "Hi Piter, glad to hear that you're feeling better."

2. **Slack Clarification:** "I actually don't use that account on slack that you found me on."
   - Note: This suggests Dan may have preferred contact method different from dxkvse@g.rit.edu

3. **Schedule/Meeting Request:** "What times would work well for you to zoom this week to circle back with a few things. I am sure that I've forgotten/missed a bunch of your questions over break."

4. **Overleaf Project Concern:** 
   - "If I understand things correctly, we currently have 2 overleaf projects with updated content? If so, would it make more sense to have 1 version?"
   - This is asking whether consolidation is needed

**Status:** Meeting scheduled for this week (specific time TBD); Dan acknowledges possibly missing questions during break; requesting Overleaf project consolidation guidance.

---

## SECTION 2: CATEGORICAL REQUEST TRACKER

### CATEGORY A: Paper Content & Structure

| Topic | Request/Discussion | Date | Status | Details |
|-------|------------------|------|--------|---------|
| **Overleaf Document** | Which Overleaf project should be the working document? | Dec 26 | ✅ ANSWERED | Working source: https://www.overleaf.com/project/68ea344896594f27b427ca8f. Travis feedback used a gray-out/review view: https://www.overleaf.com/read/ttmrwxyfqjfy#38bfea. |
| **Overleaf Access** | Grant Dan access to condensed Overleaf | Jan 2 | ⏳ PENDING | Requested at dan7800@yahoo.com. Second request Jan 5. |
| **Overleaf Clarification** | Is consolidation needed? | Jan 7 | ✅ ANSWERED | No consolidation required if one source project is maintained and review content is handled as an in-project gray-out/review section or read-view for feedback. |
| **Process Overview** | Expand 2-3 sentence overview of proposed process for abstract | Jan 2 | ⏳ PENDING | Dan notes: currently jumps from problem to findings; should double/triple length in Introduction I.b; should be high-level proposed work description |
| **Process Overview Length** | How detailed should process description be? | Jan 2 | ✅ ANSWERED | Dan: "1-3 paragraph overview would suffice"; "for proposed work; not something accomplished" |
| **Comparison to Existing MAB Work** | Provide short writeup comparing your work to existing MAB literature | Dec 26 | ✅ ANSWERED | Provided Dec 31: 4-point differentiation (multi-scenario testing, cross-allocator generalization, synergies, efficiency under constraint) |
| **Primary Research Thrusts** | Identify primary research thrusts beyond just MAB path planning | Dec 26 | ✅ ANSWERED | Provided Dec 31: Evaluation methodology, Co-design principles, Deployment taxonomy |
| **Writeup Length** | How long should comparison/thrusts writeup be? | Dec 26 | ✅ ANSWERED | 1 page maximum; short and to-the-point |

---

### CATEGORY B: Research Questions & Findings

| Topic | Request/Discussion | Date | Status | Details |
|-------|------------------|------|--------|---------|
| **Framework Evolution** | Explain the 5-paper progression and how each adds to the research | Dec 26 | ✅ ANSWERED | Provided Dec 31: Papers 1-5 evolution with quantified findings (CPursuit 89%, Thompson 3x speedup, Fixed Allocator Trap 6.4%) |
| **Testing Progress** | Update on Paper 2 & Paper 7 testbed integration | Dec 25 | ✅ PROVIDED | Historical snapshot from Dec 25 thread (not current baseline). Current dataset-verified values are listed in "Current Dataset-Verified Snapshot (as of 2026-02-12)" below. |
| **Allocator Comparison** | How do different allocators compare across scenarios? | Dec 31 | ✅ ANSWERED | Attack-allocator synergies: +2.7% to -26.5%; deployment rules provided |
| **Key Metrics** | What are the benchmark figures for the research? | Dec 31 | ✅ ANSWERED | CPursuit: 89% efficiency, 60% win rate; Thompson: 88.2%, 3× speedup; Fixed Allocator: 6.4% penalty |
| **Paper 1 Replication** | How does baseline replication differ from original? | Dec 31 | ✅ ANSWERED | Extended from 10K to 1T/1.5T/2T capacity; exposed allocation overfitting |
| **Paper 2 iCMAB** | What enhancements does context-aware approach provide? | Dec 31 | ✅ ANSWERED | Topology awareness, neural feature extraction, world modeling beyond reward history |

---

### CATEGORY C: Administrative & Logistics

| Topic | Request/Discussion | Date | Status | Details |
|-------|------------------|------|--------|---------|
| **Slack Contact** | Provide Slack username for communication | Jan 2 | ✅ ANSWERED | Piter's username: "Piter Garcia"; Piter's email: pzg8794@g.rit.edu. Dan's note: doesn't use found account; prefers different contact |
| **Slack Message** | Send Dan a message on Slack | Jan 2 | ✅ COMPLETED | Piter found Dan at @Daniel Krutz (dxkvse / dxkvse@rit.edu) in main RIT workspace |
| **Hour Logging** | Should Piter continue logging GA hours after semester ended? | Dec 31 | ❌ NOT ANSWERED (TIMED-OUT / N.A.) | Time-sensitive admin question from prior semester; no recorded response in this thread; no longer an active blocker |
| **Spring GA Continuation** | Will GA position continue through Spring semester? | Dec 31 | ❌ NOT ANSWERED (TIMED-OUT / N.A.) | Time-sensitive semester transition question; no recorded confirmation in this thread; treated as historical/unresolved |
| **Monday 10 AM Meeting** | Proposed meeting time for week of Jan 2-6 | Jan 2 | ✅ PROPOSED | Meeting proposed; awaiting Piter's confirmation (was ill) |
| **Zoom This Week** | Schedule Zoom call this week (Jan 6+) | Jan 7 | ⏳ PENDING | Dan asking: "What times would work well for you to zoom this week?" |
| **Sheeraja Contact** | Coordinate with Sheeraja on research | Dec 28 | ✅ IN PROGRESS | Sheeraja's email: sheeraja@mail.rit.edu; Piter planning to contact |
| **Meeting Addition** | Should Dan join Devroop/Sheeraja meetings? | Jan 7 | ⏳ PENDING | Piter asking if Dan wants to be added to upcoming meetings |

---

## SECTION 3: KEY RESEARCH FINDINGS & METRICS

### Quantified Results (Historical Snapshot from Piter's responses)

**Snapshot Timestamp:** Primarily Dec 25-31, 2025 communications  
**Important Context:** These values are historical checkpoints captured at that time. They are **not guaranteed current** and may have changed with newer runs, parameter updates, or additional experiments.

| Metric | Value | Source/Context |
|--------|-------|-----------------|
| **CPursuit Efficiency** | 89% | Paper 3 Multi-Model Framework benchmark |
| **CPursuit Win Rate** | 60% (12/20) | Paper 3 Multi-Model Framework |
| **EXPNeuralUCB Efficiency** | 78% | Paper 3 baseline comparison |
| **EXPNeuralUCB Win Rate** | 5% (1/20) | Paper 3 benchmark |
| **Thompson Sampling Efficiency** | 88.2% | Paper 3 Bayesian approach |
| **Thompson Sampling Speedup** | 3× | 3.52h vs 11.62h; Paper 3 |
| **Fixed Allocator Penalty** | 6.4% | Generalization penalty under dynamic allocation; Paper 3 |
| **Paper 2 Stochastic Performance** | 92.8% (default), 92.7% (dynamic) | Dec 25 testing update |
| **Paper 2 Markov Performance** | 59-62% | Dec 25 testing; adversarial scenario |
| **Paper 7 Performance** | 40-55% | Dec 25 testing; frame/capacity dependent |
| **CPursuit Floor Efficiency** | 72.9% | One-page summary |
| **CPursuit Coefficient of Variation** | 7.9% | One-page summary |
| **EXPNeuralUCB CV** | 10.9% | One-page summary |
| **EXPNeuralUCB Floor** | 54% | One-page summary |
| **Attack-Allocator Synergy Range** | +2.7% to -26.5% | Paper 4b finding |
| **CPursuit+Thompson Peak** | 97-98% | Optimal pairing efficiency |

### Current Dataset-Verified Snapshot (as of 2026-02-12)

**Source of truth for current values:**
- `Validated_Logs/Master_Dataset_paper2_4000_2000_5_ST.csv`
- `Validated_Logs/Master_Dataset_paper7_50_50_5_ST.csv`
- `Validated_Logs/Master_Dataset_paper12_1500_500_5_ST.csv`

**Method note:** grouped by scenario (`NONE` and `STOCHASTIC`) and model, excluding Oracle rows.

| Paper | Scenario NONE (No Attack) - Top Model | Scenario STOCHASTIC - Top Model | EXPNeuralUCB Retention (Stochastic / None) |
|---|---|---|---|
| Paper 2 | iCPursuitNeuralUCB: reward 2973.44, eff 90.92% | GNeuralUCB: reward 2751.70, eff 86.18% | 92.3% (2667.50 / 2891.35) |
| Paper 7 | iCPursuitNeuralUCB: reward 1350.00, eff 100.00% | iCPursuitNeuralUCB: reward 1268.10, eff 93.97% | 93.2% (1112.05 / 1192.93) |
| Paper 12 | iCPursuitNeuralUCB: reward 1245.21, eff 55.98% | iCPursuitNeuralUCB: reward 1156.60, eff 51.99% | 92.6% (1110.29 / 1199.62) |

### Supporting Documents Referenced

- **GA Dynamic Qubit Allocation Report** - 60-condition analysis with 4 allocators
- **GA iCMAB Evaluation Report** - iCPursuit at 90-92% Oracle efficiency
- **GA EXPNeuralUCB Tests Report** - 58.5% Oracle efficiency under Markov attacks
- **GA CMAB Models Evaluation** - CPursuit at 96% Oracle efficiency
- **Capacity Paradox Reports** - 22-30% efficiency collapse under adaptive quantum attacks
- **Master Datasets** - Updated as new tests run; comprehensive empirical foundation

---

## SECTION 4: STATUS & ACTION ITEMS

### ✅ ANSWERED/COMPLETED

- ✅ Framework evolution explanation (5 papers, Dec 31)
- ✅ Comparison to existing MAB work (4 differentiators, Dec 31)
- ✅ Primary research thrusts (3 main areas, Dec 31)
- ✅ Testing progress updates (Papers 2, 7, Dec 25)
- ✅ Slack username provided (Piter Garcia, Dec 28)
- ✅ Slack contact established (found Dan in main workspace, Jan 7)
- ✅ Key metrics provided (historical quantified snapshot captured Dec 31)
- ✅ Overleaf project clarification (2 projects identified, Dec 31 & Jan 7)

### ⏳ PENDING (Awaiting Response)

**From Piter (awaiting Dan's answer):**
1. Overleaf project consolidation: Should we merge into 1 document?
2. Zoom scheduling: What times work this week?

**Timed-Out / N.A. (Historical, not active):**
1. Hour logging: Continue or pause until Spring? (asked Dec 31; not answered in-thread)
2. Spring GA continuation: Position continues through Spring semester? (asked Dec 31; not answered in-thread)

**From Dan (awaiting Piter's action):**
1. Overleaf access: Grant dan7800@yahoo.com access to condensed project
2. Process overview: Expand abstract process description (double/triple length)
3. Meeting attendance: Confirm times for Zoom call this week

### 🔄 IN PROGRESS

- Testbed integration with Papers 2, 7, 12
- README contribution guide development
- Master datasets notebook updates
- Epsilon + NeuralUCB integration and testing
- Devroop/Sheeraja coordination on next steps

---

## SECTION 5: COMMUNICATION NOTES & CONTEXT

### Dan's Apparent Concerns/Questions
1. **Multiple Overleaf projects** - Unsure which to review; needs clarity
2. **Process description** - Currently too high-level; needs expansion
3. **Work differentiation** - Wants clear statement of how this differs from existing MAB research
4. **Meeting coordination** - Important to catch up; Dan acknowledges "forgotten/missed" items during break
5. **Document consolidation** - Wondering if 2 Overleaf projects should be 1

### Piter's Apparent Status
1. **Health recovery** - Recovering from illness lasting 3+ days; now functional as of Jan 7
2. **Schedule management** - Working on Spring semester planning and GA responsibilities
3. **Research progress** - Testing progressing well; results are "solid"
4. **Coordination** - Reaching out to Devroop and Sheeraja for next steps
5. **Documentation** - Keeping detailed records; comprehensive responses provided

### Critical Clarifications Made
- One **primary Overleaf source project** is used for active work
- A **gray-out/review view** was prepared for Professor Travis feedback
- Review view is for feedback convenience, not a separate active source project
- Dan's Slack account issue: **doesn't use found account**; prefers alternative contact method
- **Framework evolution** spans 5 papers with clear progression and quantified results

---

## SECTION 6: REFERENCES & RESOURCES

### Key Files/Links
- **Primary Overleaf:** https://www.overleaf.com/project/68ea344896594f27b427ca8f
- **Condensed Overleaf:** https://www.overleaf.com/read/ttmrwxyfqjfy#38bfea
- **Master Datasets:** Being continuously updated
- **GA Reports:** iCMAB Evaluation, EXPNeuralUCB Tests, CMAB Models Evaluation, Capacity Paradox

### Contact Information
- **Piter:** pzg8794@rit.edu / pzg8794@g.rit.edu / Slack: "Piter Garcia"
- **Dan:** dxkvse@rit.edu (primary) / Slack: varies (clarification needed)
- **Sheeraja:** sheeraja@mail.rit.edu
- **Devroop:** (contact through Piter)

---

## NOTES & SUGGESTIONS

1. **For Dan**: This log captures all communications, requests, and responses. Anytime a question arises, you can reference this document to see if it's been discussed.

2. **For Future Use**: This document should be updated after each significant communication or decision point to maintain accuracy and accessibility.

3. **Discussion Points for Upcoming Zoom**: 
   - Overleaf project consolidation strategy
   - Process description expansion for abstract
   - Meeting schedule with Devroop/Sheeraja
   - Next steps on Papers 4b and 5 integration

4. **Items Repeated/Clarified**:
   - Overleaf access requested twice (Jan 2, Jan 5) - still pending
   - Process overview requested once, clarified as 1-3 paragraphs
   - Slack contact clarified (Dan doesn't use found account)
   - Overleaf workflow clarified (1 source project + review view for feedback)

---

**Last Updated:** February 12, 2026  
**Document Status:** Active - Living Document (Updated after each communication)  
**Shared With:** Daniel Krutz (dxkvse@rit.edu)
