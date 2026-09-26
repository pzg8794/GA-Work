# GA-Work Superproject

Public superproject for the GA research workspace.

This repository tracks top-level GA-Work notes, validated logs, paper-support files, and Git submodule pointers for the major project repositories.

## Medium-scale preparation — September 26, 2026

F-08 engineering preparation is documented in the [Quantum execution preparation record](https://github.com/pzg8794/quantum_project/blob/gcp-main/Dynamic_Routing_Eval_Framework/docs/guides/MEDIUM_SCALE_EXECUTION_PREPARATION.md) and the manuscript's [current preparation status](https://github.com/pzg8794/QuantumFaultTolerant/blob/main/updates/MEDIUM_SCALE_PREPARATION_2026-09-26.md). The required anchor is 15–20 nodes with at least ten distinct candidate routes under comparable primary-style semantics. Scientific configuration and execution approval remain open; F-09 execution and F-10 diagnostics have not begun in this preparation pass.

The execution owner is `quantum_project` (`hybrid_variable_framework` locally). `quantum_project_hub` supplies supporting testbeds and navigation. Existing dirty checkouts and submodule pointers are preserved; current manuscript planning must be read from its latest remote record when an older local checkout disagrees. This status records research preparation, not paid-hour or submission evidence.

## Submodules

- `GA Papers/QuantumFaultTolerant` -> `git@github.com:pzg8794/QuantumFaultTolerant.git`
- `hybrid_variable_framework` -> `https://github.com/pzg8794/quantum_project.git`
- `quantum_project_hub` -> `https://github.com/pzg8794/quantum_project_hub.git`

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/pzg8794/GA-Work.git
```

Refresh submodules after pulling:

```bash
git submodule update --init --recursive
```

## Local-only material

The superproject intentionally ignores local environments, scratch worktrees, temporary files, and credentials such as `.quantum/`, `_worktrees/`, `tmp/`, `.vscode/`, and `quantum-gd-credentials.json`.

Submodules are configured with `ignore = dirty` so local in-progress work inside each nested repository does not make the parent superproject appear dirty unless the pinned submodule commit changes.
