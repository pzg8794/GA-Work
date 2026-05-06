# GA-Work Superproject

Private superproject for `/Users/pitergarcia/DataScience/Semester4/GA-Work`.

This repository tracks top-level GA-Work notes, validated logs, paper-support files, and Git submodule pointers for the major project repositories.

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
