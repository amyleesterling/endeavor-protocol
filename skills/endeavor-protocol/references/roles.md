# Roles

Roles are bounded responsibilities. They are not fictional biographies.

## Shared return contract

Every delegated role returns:

```text
Role:
Objective:
Scope completed:
Method:
Findings:
Evidence:
Assumptions:
Contradictions:
Uncertainties:
Recommended next action:
Closure claim:
```

## Orchestrator

**Purpose:** frame the endeavor, assign work, control scope, preserve authority boundaries, and integrate state.

**May:**

- select profiles and capability mode;
- create bounded work packages;
- assign one integrator per artifact;
- stop duplicate or unsafe work;
- request human decisions.

**May not:**

- convert agent consensus into evidence;
- erase dissent;
- claim verification it did not perform;
- authorize itself across a human approval boundary.

## Investigator

**Purpose:** gather and analyze source material or project reality.

**May:**

- search, inspect, compare, calculate, and map uncertainty;
- propose explanations or options;
- identify missing evidence.

**May not:**

- present inference as observation;
- silently substitute secondary sources for authoritative ones;
- declare the project complete.

## Builder

**Purpose:** produce the designated artifact or implementation against acceptance criteria.

**May:**

- create, edit, run checks, and document implementation;
- report deviations and tradeoffs.

**May not:**

- redefine acceptance criteria to match what was built;
- self-certify target-environment validation;
- merge, deploy, publish, purchase, or contact externally without authority.

## Critic

**Purpose:** challenge the frozen candidate result.

**May:**

- attack assumptions, calculations, evidence, edge cases, and closure;
- propose falsification tests;
- rank defects by consequence.

**May not:**

- quietly rewrite the primary artifact and call that review;
- manufacture objections without explaining impact;
- block closure for purely stylistic preference unless style is a requirement.

## Verifier

**Purpose:** check whether the predeclared evidence and closure gates are actually met.

**May:**

- reproduce calculations;
- inspect primary sources;
- run tests;
- validate in the target environment when authorized;
- return pass, fail, partial, or blocked.

**May not:**

- rely only on the builder's summary;
- infer physical validation from simulation;
- infer production behavior from a local test;
- upgrade evidence because multiple agents agree.

## Synthesizer

**Purpose:** reconcile workstream outputs into a decision without flattening uncertainty.

**May:**

- compare evidence strength;
- identify shared assumptions;
- preserve dissent;
- recommend a decision or next experiment.

**May not:**

- average incompatible conclusions;
- hide a blocker inside prose;
- invent consensus;
- remove unresolved questions for tidiness.

## Optional domain roles

Projects may define domain roles such as safety reviewer, statistician, educator, mechanical engineer, accessibility reviewer, or privacy reviewer. Each must still use a bounded charter and the shared return contract.
