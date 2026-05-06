<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# I used this plan to update the paper according to Dan's feedback, can you check it out (the recent changes pushed to the repo "QuantumFaultTolerant" linked here) and let me know of any improvements/changes needed to make sure we fully capture Dan's feedback/comment/task?

## Plan — Dan `R-11` Caption Pass (Figures Only)

### Summary

Apply Dan’s March 13 `R-11` comment as a **figure-caption-only** pass in `Semester4/GA-Work/GA Papers/QuantumFaultTolerant/main.tex`. The goal is to make every **figure** caption shorter and takeaway-first, while leaving **table captions** for the separate `R-13` pass.

### Task

Shorten the figure captions and make the main takeaway explicit.

### Meaning

Each figure caption should do two things, in this order:

1. State the result readers should remember.
2. Add only the minimum context needed to read the figure.

This is a style pass, not a results change. We keep the same figures, labels, and claims; we only tighten the wording.

### Implementation Changes

- **Scope**
- Touch **figure captions only** in `main.tex`.
- Do **not** edit table captions in this pass.
- Do **not** change labels, figure placement, figure size, or caption font sizing.
- **Caption rule to apply consistently**
- Start with the takeaway, not the setup.
- Keep each caption to **1 short sentence**, or **2 very short clauses** if context is necessary.
- Prefer this pattern:
- **Takeaway.** Minimal context in parentheses or a trailing phrase.
- Remove process-heavy phrasing like:
- “computed from…”
- “aggregated across…”
- long metric definitions that belong in text/tables
- Keep only the context needed to avoid ambiguity:
- corpus/slice if needed
- allocator if needed
- threat/capacity framing if needed
- Preserve technical terms that are central to interpretation:
- `Oracle-normalized efficiency`
- `default allocator` / `Fixed allocator` when the figure depends on that choice
- `T` vs `T_b` only when the figure is explicitly about capacity semantics
- **Figures to normalize in this pass**
- `fig:framework`
- `fig:context_exp3_capacity`
- `fig:floor`
- the unlabeled topology/network figure
- `fig:global_win_share`
- `fig:context_capacity_effects`
- `fig:scenario_penalties`
- `fig:capacity_all`
- `fig:threat_rules`
- the unlabeled predictive-context figure
- `fig:convergence_hybrid`
- `fig:context_hybrid`
- **Per-caption rewrite standard**
- For already-short captions, only tighten if they still lead with setup instead of takeaway.
- For longer captions, remove secondary explanation and keep the one main implication.
- If a caption currently contains both a finding and an interpretation, keep the finding and compress the interpretation into 3–6 words max.


### Before / After Standard

- **Before**
- Caption opens with setup or experimental slice.
- Takeaway appears late or is split across multiple clauses.
- Caption carries more methodological detail than needed.
- **After**
- Caption opens with the main result.
- Context is compressed and secondary.
- Reader can understand the figure’s point in one quick read.


### Reasoning

This matches Dan’s tracked review intent for `R-11` and avoids blending it with `R-13` table-caption work. It also keeps the paper stylistically consistent: figure captions become quick-result anchors, while methodological detail stays in the body, tables, and study-design sections.

### Test Plan

- Read every figure caption top-to-bottom and confirm:
- it starts with the takeaway
- it is shorter than the current version
- it does not change the scientific claim
- it does not introduce new numbers unless the number is the takeaway
- Compile the LaTeX document and verify:
- no label/reference breakage
- no caption-size changes
- no overfull/ugly caption wrapping introduced by the rewrites


### Assumptions / Defaults

- We are handling **`R-11` only**, not the separate table-caption task.
- We will preserve IEEE default caption sizing and not reintroduce manual `\tiny`.
- We will keep unlabeled figure captions in scope if they appear in `main.tex`, because Dan’s note was about the caption style across figures, not only labeled figures.

Now I have everything I need. Let me deliver the full audit:

***

## R-11 Caption Pass — Audit Results

The commit [`d60e2ea`](https://github.com/pzg8794/QuantumFaultTolerant/commit/d60e2eaaa3e9a1d43b8257db7c24f457af73186c) ("paper: shorten figure captions for Dan R-11") touched 12 deletions and 12 additions in `main.tex`. Overall the pass is in good shape — 10 of the 12 in-scope figures are fully compliant with Dan's intent. Here's the complete picture:

***

## ✅ What's Done Well (10/12 figures)

| Figure | Current Caption | Status |
| :-- | :-- | :-- |
| `fig:framework` | "A unified evaluation pipeline enables apples-to-apples routing comparisons across threats, capacity semantics, allocators, and model families." | ✅ Takeaway-first, 1 sentence |
| `fig:context_exp3_capacity` | "Contextual (CMAB/iCMAB) methods are more scale-robust than EXP3 baselines, with the clearest Oracle-normalized efficiency gap under $T_b$ settings." | ✅ |
| `fig:floor` | "Worst-case robustness separates the model families: context-aware methods retain higher floors than adversarial-first baselines at the default $2T$–$2T_b$ budget." | ✅ |
| `fig:network_topology` (unlabeled topology figure) | "The testbed exposes four alternative entanglement paths whose qubit splits vary by allocator strategy." | ✅ Short, point-first |
| `fig:global_win_share` | "`iCEpsilonGreedy` wins most often under the default allocator, with `CPursuit` second." | ✅ Perfect — named winner first |
| `fig:context_capacity_effects` | "Contextual (CMAB/iCMAB) models maintain higher Oracle-normalized efficiency than non-context EXP3 baselines across threats under both $T$ and $T_b$." | ✅ |
| `fig:scenario_penalties` | "Context-aware methods absorb smaller, more stable threat penalties, while EXP3-family baselines are most exposed under adaptive threats." | ✅ |
| `fig:capacity_all` | "More capacity helps in Baseline and Markov settings but can hurt under Adaptive threats, revealing the capacity paradox." | ✅ Excellent — paradox named upfront |
| `fig:threat_rules` | "Allocator choice is threat-dependent: Thompson leads in Adaptive regimes, DynamicUCB stays competitive, and Random underperforms." | ✅ |
| `fig:convergence_hybrid` | "Pursuit-based hybrids converge higher, while neural baselines plateau lower under sparse reward feedback." | ✅ |
| `fig:context_hybrid` | "Pursuit-based hybrids maintain higher efficiency than neural and EXP3 baselines across all five threat regimes." | ✅ |

Table captions (`tab:rq3a_informative`, `tab:rq2_adversarial`, `tab:rq3c_allocators`, etc.) were correctly left untouched — scope respected. ✅

***

## ⚠️ Issues / Gaps to Address

### 1. `fig:heatmap` — Still Setup-First (the one carry-over from C-057)

**Current caption (L849–852):**

```
\caption[Efficiency heatmap for CPursuitNeuralUCB]{Efficiency heatmap for \texttt{CPursuitNeuralUCB}
across allocator strategies and threat scenarios. In this setting, the Fixed allocator yields
the highest efficiency across scenarios, reinforcing allocator choice as a first-class robustness factor.}
```

**Problem:** Opens with a label/"what this is" (`Efficiency heatmap for…`) rather than the finding. This violates the R-11 rule "start with the takeaway, not the setup," and the caption was already approved under C-057 using this pattern — meaning the C-057 fix was incomplete and R-11 should now clean it up.

**Suggested fix:**

```latex
\caption[Fixed allocator tops CPursuitNeuralUCB heatmap]{Fixed allocator yields the highest
Oracle-normalized efficiency for \texttt{CPursuitNeuralUCB} across threat scenarios,
making allocator choice a first-class robustness factor.}
```

This also fixes the optional short caption `[...]` to be takeaway-first for List-of-Figures consistency.

***

### 2. "Unlabeled Predictive-Context Figure" — Doesn't Exist; Plan Item Is Moot

The plan's scope listed "the unlabeled predictive-context figure" as a target. In the current `main.tex`, there is **no such figure** — the only predictive-context element near that section is `tab:rq3a_informative`, which is a **table** (and correctly left untouched). The figure either never existed or was converted to a table in an earlier pass.

**Action needed:** Add a note in `PAPER-CHANGES-TRACKER.md` under the R-11 entry clarifying that this item was resolved as N/A (no matching figure exists — the predictive-context data lives in a table). This prevents future confusion if someone tries to locate "the unlabeled predictive-context figure" during review.

***

### 3. Tracker Not Formally Closed for R-11

The progress note in `PAPER-CHANGES-TRACKER.md` (added 2026-03-30) records that the R-11 pass was applied, but there is **no formal `C-###` entry** added to the main "Current Queue" section the way C-057, C-058, C-059, C-060 were each tracked individually. The active review queue still shows R-11 open without a corresponding "Done" C-entry.

**Action needed:** Add a `C-063` (or next available ID) entry to the Current Queue table marking R-11 as Done, listing the 11 figures touched in this pass, and noting the `fig:heatmap` carry-over and the N/A predictive-context item.

***

## Summary Checklist

| Item | Status | Fix needed? |
| :-- | :-- | :-- |
| 10 in-scope figures rewritten (takeaway-first, no `\tiny`) | ✅ Done | — |
| Table captions untouched | ✅ Correct scope | — |
| `fig:heatmap` still setup-first | ⚠️ Gap | Yes — 1-line rewrite |
| "Unlabeled predictive-context figure" | ⚠️ N/A — it's a table | Add tracker note clarifying N/A |
| R-11 tracker entry formally closed | ⚠️ Missing | Add C-063 entry as Done |

The pass is 90% complete. The only actual `main.tex` change needed is the `fig:heatmap` rewrite above. The other two items are tracker hygiene.
<span style="display:none">[^1][^10][^11][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: repo_structure.txt

[^2]: QuantumPathOptimization.pdf

[^3]: Sheeraja_IJCNN_2026.pdf

[^4]: LinkSelFiE_Link_Selection_and_Fidelity_Estimation_in_Quantum_Networks.pdf

[^5]: Multipath_Inter-Domain_Routing_Protocols_for_Quantum_Networks_With_Online_Path_Selection.pdf

[^6]: Learning_Best_Paths_in_Quantum_Networks.pdf

[^7]: paper7_liu2024qbgp.pdf

[^8]: GA-Paper--iCMABs.pdf

[^9]: paper12_wang2024quarc.pdf

[^10]: GA-Paper-EXPNeuralUCB.pdf

[^11]: paper2_chaudhary2023quantum.pdf

