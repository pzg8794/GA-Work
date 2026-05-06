# Submodule Inventory

## Parent Superproject Submodules

| Path | Remote | Pinned branch at setup |
|---|---|---|
| `GA Papers/QuantumFaultTolerant` | `git@github.com:pzg8794/QuantumFaultTolerant.git` | `main` |
| `hybrid_variable_framework` | `https://github.com/pzg8794/quantum_project.git` | `gcp-main` |
| `quantum_project_hub` | `https://github.com/pzg8794/quantum_project_hub.git` | `main` |

## Nested Git Repositories Observed

The following Git repositories are physically nested under `quantum_project_hub/testbeds/` in the local checkout:

- `quantum_project_hub/testbeds/CMAB-CoMM`
- `quantum_project_hub/testbeds/EXPNeuralUCB`
- `quantum_project_hub/testbeds/Paper8-RL_Entanglement_Routing`

They are not registered as parent-level submodules because `quantum_project_hub` is itself a submodule. If those need recursive submodule behavior, refactor them inside `quantum_project_hub` in a separate dedicated change.
