# GA-Work Agent Notes

This file applies to the entire `Semester4/GA-Work/` tree unless a deeper `AGENTS.md` overrides it.

## Resume points

- For the quantum framework, start here:
  - `hybrid_variable_framework/AGENTS.md`
- For Drive migration details, read:
  - `hybrid_variable_framework/Dynamic_Routing_Eval_Framework/STATE-DRIVE-MIGRATION-PLAN.md`

## Quantum application-material rule

- While the ICNP submission is under anonymous review, do not use `GA Papers/QuantumFaultTolerant/ICNP_2026_venue_draft.tex`, `ICNP_2026_venue_draft.pdf`, or that draft's exact title in application packets, public-safe RESEARCH notes, or reusable filenames.
- If a manuscript-style sample is needed for a PhD or fellowship application, use an anonymous-safe technical report first.
- If a longer manuscript sample is still needed, derive a sanitized application copy from `GA Papers/QuantumFaultTolerant/main.tex` or a selected excerpt, and give it a different non-identifying title before sharing.
- Treat Overleaf as a working mirror; use the local manuscript/workspace files as the source of truth when preparing sanitized application material.

## Drive migration rules

- Stay on the existing Drive implementation.
- Only valid remote datalake roots are:
  - `quantum_data_lake/framework_state/`
  - `quantum_data_lake/model_state/`
- Do not rename state files.
- Use full saved filenames as keys during migration/status work.
- For risky changes, use:
  - task
  - before
  - after
  - reason
  - wait for approval

## Application artifact navigation rules

- For PhD/fellowship packet building, always start discovery from Overleaf before Drive or GitHub.
- Use `RESEARCH/APPLICATIONS/PhD/OVERLEAF_DISCOVERY_PLAYBOOK.md` as the canonical lookup workflow for course/topic keyword searches and known project mappings.
- Maintain `RESEARCH/APPLICATIONS/PhD/OVERLEAF_PAPER_INDEX.md` as the canonical repo-side index of application-grade Overleaf manuscript projects and their sanitized packet derivatives.
- Maintain `RESEARCH/APPLICATIONS/PhD/TRANSCRIPT_SOURCE_INDEX.md` whenever a transcript or degree document is intentionally mirrored into the repo for application work; record both the Drive/local source path and the repo mirror path.
- Keep retrieval order consistent:
  1. Overleaf (formal manuscript-style artifacts)
  2. Google Drive (broader archive/planning)
  3. GitHub (public-safe mirrors and packet trackers)
- Timing shortcut: if time is constrained, Google Drive and GitHub can be used interchangeably as fallback lookup layers.
- For Drive traversal, always enter from the DataScience root first:
  - [DataScience root Drive folder](https://drive.google.com/drive/folders/1pY_fQ54nHKvFABNRGYAr5bQ3su_tUDAi?usp=sharing)
  - Then drill down semester -> course (and UofR semester subdirectories when applicable).
- After any live submission update, record the new application record ID and attachment filenames in the corresponding packet-status file under `RESEARCH/APPLICATIONS/PhD/application-materials/`.
- Maintain non-destructive behavior for Overleaf sources: create application-specific copies before edits whenever practical.
- Writing-sample keyword lock for PhD packets:
  - Do not use generic retrieval keywords `Quantum` or `GA` when selecting sample papers.
  - Use exact keyword `QuantumPathOptimization` for the quantum/AI paper slot.
  - Canonical order for full sample bundles is:
    1. `BIO614-FinalProjectProposal`
    2. `ISTE780-Project_Phase4` (fallback `ISTE780-Project_Phase3`)
    3. `QuantumPathOptimization`
    4. `DSCI601-Project_Proposal` (latest)

## Application portal CV curation rules

- Do not blindly mirror LinkedIn or older CV entries into live application portal work-history sections.
- Exclude volunteer, pro bono, weak-fit, or user-disliked part-time roles unless the user explicitly asks to include them.
- Prefer recent research, teaching placement, tutoring, and directly relevant industry entries when curating a short portal CV.
- Normalize noisy employer branding when it weakens the presentation, for example prefer `Varsity Tutors` over `Varsity Tutors, a Nerdy Company` unless the full brand is explicitly required.
- For the University of Rochester placement, use the user-approved title `UofR Warner School Teaching Placement` (or an explicit replacement the user gives) and use `University of Rochester - Warner School of Education` as the employer; keep Pine Brook only in the description when the classroom site matters.
- After any portal CV edit, reopen the send/preview state and verify the retained entries before considering the application update complete.
