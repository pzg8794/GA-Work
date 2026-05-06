# R-11 Figure Caption Pass Review for QuantumFaultTolerant

## Executive summary

Your R-11 “caption pass” is **substantively complete**: the current `main.tex` has moved from long, number-heavy, manually down-sized captions (the old pattern) to **short, takeaway-first figure captions** that largely avoid methodological clutter and no longer embed `\tiny` inside `\caption{...}`. This directly matches Dan’s stated intent for R-11 (“Shorten captions and state the main takeaway” for figures). fileciteturn70file0

The **one meaningful remaining gap** is consistency: at least one figure caption (notably `fig:heatmap`) still **opens with “what it is” (setup) rather than “what it means” (takeaway)** and carries residual provenance/detail that your own plan says to avoid in this pass. This is a simple, low-effort fix.

A secondary (optional but safety-improving) refinement is to ensure your `\scriptsize`/`\tiny` directives used to scale *plot/tikz content* do **not** accidentally scope over captions. While IEEEtran typically controls caption sizing, scoping the font changes inside braces makes compliance with “don’t change caption size” robust and reviewer-proof without changing results or layout.

## Dan’s R-11 requirement and what “done” means

In your tracker, R-11 is explicitly: **“Figure captions — Shorten captions and state the main takeaway.”** fileciteturn70file0 The same tracker thread (C-048 through C-060 / C-057, C-058, C-059) records the recurring constraint Dan emphasized while requesting shortening: **avoid manual caption sizing like `\tiny`** and keep captions focused on the primary message. fileciteturn70file0

Your plan’s interpretation is correct and aligns with the tracker’s meaning: captions should (i) lead with the takeaway, (ii) include only minimal context, and (iii) avoid methodology/provenance and dense numeric blocks that belong in the text/tables. fileciteturn70file0

## Evidence that the repo changes implement the intent

The “before” baseline in `archive/main_old.tex` contains the exact anti-pattern Dan was flagging: long captions with explicit `\caption{\tiny ...}` and embedded multi-statistic explanations. For example, multiple figures include long, number-led captions and explicitly set caption text to `\tiny` inside the `\caption` command. fileciteturn67file0

In the current `main.tex`, the corresponding captions have been rewritten into substantially shorter, takeaway-first statements, and the manual `\tiny` inside `\caption{...}` is removed across the main figure set (e.g., `fig:framework`, `fig:context_exp3_capacity`, `fig:floor`, `fig:global_win_share`, `fig:context_capacity_effects`, `fig:scenario_penalties`, `fig:capacity_all`, `fig:threat_rules`, `fig:convergence_hybrid`, `fig:context_hybrid`). fileciteturn63file0 This matches the tracker’s claimed resolution for the R-11 caption sweep applied on **2026-03-30**. fileciteturn70file0

In short: the diff direction is correct, and the “caption-only” nature of the improvements is visible in exactly the areas Dan called out earlier (wordiness + manual caption sizing). fileciteturn70file0turn63file0turn67file0

## Caption audit against your plan

Your plan’s standard is: **takeaway first**, then minimal disambiguating context; “no process-heavy phrasing,” and keep captions to one short sentence (or two short clauses). fileciteturn70file0

Most of the key figures now comply well (and are a clear improvement over `archive/main_old.tex`). fileciteturn63file0turn67file0 The main inconsistency is a caption that still starts “Efficiency heatmap for…” (setup-first) rather than the implication, and includes extra provenance text that your plan explicitly wants out of captions. This is consistent with the tracker’s earlier note that the heatmap caption was a specific Dan pain point (C-057). fileciteturn70file0

### Minimal compliance table

| Figure | Current state vs R-11 | What to adjust (if anything) | Effort | Priority |
|---|---|---|---|---|
| `fig:framework` | Short + takeaway-first; manual caption sizing removed (matches Dan + tracker notes). fileciteturn63file0turn70file0 | No change needed unless you want to add 2–4 words of context (“evaluation pipeline” vs “pipeline”). | Low | Low |
| `fig:context_exp3_capacity` / `fig:floor` / “family separation” figures | Now short and takeaway-led (strong improvement over old multi-number caption blocks). fileciteturn63file0turn67file0 | No change needed. | Low | Low |
| `fig:global_win_share`, `fig:context_capacity_effects`, `fig:scenario_penalties`, `fig:capacity_all`, `fig:threat_rules`, `fig:convergence_hybrid`, `fig:context_hybrid` | Generally compliant: takeaway-first and minimal context; consistent with your “After” standard. fileciteturn63file0turn70file0 | Optional: ensure each caption has enough context to stand alone (usually already provided by axes/legend). | Low | Low |
| `fig:heatmap` | Improved vs old, but still partly “setup-first” and heavier than your stated target; it is also explicitly tracked as a caption issue in the tracker. fileciteturn70file0turn63file0 | Rewrite to lead with the takeaway and delete provenance/exclusion detail that belongs in text or appendix. | Low | High |

## Recommended edits to fully close R-11

### Make `fig:heatmap` strictly takeaway-first

This change stays within the spirit of your plan (“caption pass only”), preserves the claim, and removes residual process/provenance. It also aligns with Dan’s repeated request pattern captured in C-057 (“Too wordy… don’t change caption size”) while being even more consistent with your “takeaway first” template. fileciteturn70file0

Suggested patch (diff-style):

```diff
-\caption[Efficiency heatmap for CPursuitNeuralUCB]{Efficiency heatmap for \texttt{CPursuitNeuralUCB} across allocator strategies and threat scenarios. In this setting, the Fixed allocator yields the highest efficiency across scenarios, reinforcing allocator choice as a first-class robustness factor.}
+\caption[CPursuitNeuralUCB heatmap]{Allocator choice dominates \texttt{CPursuitNeuralUCB}: Fixed is highest across threat scenarios (efficiency heatmap over allocator $\times$ scenario).}
```

Why this addresses Dan’s concern: the reader’s “remember this” message (“allocator choice dominates; Fixed highest”) appears first; the remainder is just enough context to interpret the plot. This removes the preamble (“Efficiency heatmap… across…”) that doesn’t add meaning and is exactly the kind of setup-led phrasing your plan says to avoid. fileciteturn70file0

### Optional safety tweak: scope plot font size so it cannot affect caption sizing

Even though IEEEtran usually renders captions in a consistent size, this is a **low-risk defensive edit** if you want to be absolutely sure a reviewer cannot claim captions were “shrunk” indirectly. The idea: keep `\scriptsize`/`\tiny` limited to the `tikzpicture` content and restore normal scope before `\caption`.

Pattern:

```tex
\begin{figure}[ht!]
\centering
{\scriptsize
  \begin{tikzpicture}
    ...
  \end{tikzpicture}
}
\caption{...}
\label{...}
\end{figure}
```

This does not change results, labels, or placement; it only guarantees the caption is rendered with the class’s caption font policy, regardless of what precedes it. This directly supports Dan’s “don’t change caption size” constraint documented throughout the caption-related tracker items. fileciteturn70file0

## Tracker-level improvements for “fully captured” closure

Your tracker indicates: “2026-03-30 — R-11 figure-caption pass applied in `main.tex`,” but the plan (and reviewer closure) becomes stronger if you also record **the commit hash that introduced the caption sweep**, since your tracker’s own conventions ask for it. fileciteturn70file0

A minimal addition would be:

- Add the commit short hash to the R-11 progress note line (and/or add a Change Log entry “Figure caption pass (R-11): takeaway-first captions; removed `\caption{\tiny...}`”). This makes it easy for Dan (and future you) to audit “what changed” without rereading the file.

## Final closure checklist for R-11

If you apply the one remaining `fig:heatmap` tightening, you’ll meet both Dan’s literal R-11 ask and your own “After” standard:

Confirm across **all** figures that (a) the takeaway is first, (b) no caption contains manual size directives like `\tiny` inside `\caption`, and (c) captions do not smuggle in table-level methodology/provenance. The old version showed exactly these problems; the current version has largely corrected them. fileciteturn67file0turn63file0turn70file0