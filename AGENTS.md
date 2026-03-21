# GA-Work Agent Notes

This file applies to the entire `Semester4/GA-Work/` tree unless a deeper `AGENTS.md` overrides it.

## Resume points

- For the quantum framework, start here:
  - `hybrid_variable_framework/AGENTS.md`
- For Drive migration details, read:
  - `hybrid_variable_framework/Dynamic_Routing_Eval_Framework/STATE-DRIVE-MIGRATION-PLAN.md`

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
