# Architecture

Endeavor Protocol separates four things that are commonly blurred together:

1. **purpose**: what outcome matters and why;
2. **organization**: how work is divided and coordinated;
3. **evidence**: what supports each claim;
4. **closure**: what validation is required before a state changes.

This separation is the core architecture.

## Layers

### 1. Entrance layer

`BOOTSTRAP.md` and `SKILL.md` let a fresh instance reconstruct the protocol without access to the conversation that created it.

### 2. Profile layer

Profiles adapt the same lifecycle to different endeavor shapes. Profiles are composable but must remain behaviorally meaningful.

### 3. Capability layer

The capability ladder selects Solo, Delegated, or Orchestrated execution. The protocol optimizes for the smallest mode that satisfies the evidence and coordination requirements.

### 4. Role layer

Roles provide bounded epistemic and operational responsibilities. They are not personalities. A role's value comes from its charter, scope, and return contract.

### 5. State layer

The `.endeavor/` directory preserves project truth across instances. It is deliberately separate from source code and deliverables.

### 6. Evidence layer

Claims are recorded with source, method, status, confidence, limitations, and checker. Closure depends on project-specific evidence, not model confidence.

### 7. Governance layer

Human approval boundaries remain explicit. The protocol does not convert agent capability into authority.

## Core invariants

### Inspect reality, not just plans

A document saying a test passed is weaker than the test result. A disposition saying an issue is closed is weaker than the calculation or physical evidence required to close it.

### One writer per shared artifact

Parallel agents may investigate, calculate, test, or critique. One designated integrator owns each shared artifact at a time. This reduces edit conflict and synthesis mush.

### Dissent is data

The synthesizer records unresolved disagreement and the evidence that would distinguish competing positions. Consensus is not a required output.

### No counterfeit independence

A single model adopting six roles may improve coverage, but it is not six independent replications. Independence requires meaningfully separated attempts, context, methods, or checkers.

### Append, supersede, preserve

Material decisions and run history are not silently rewritten. A later entry may supersede an earlier one while keeping the earlier state visible.

### Closure is typed

“Implemented,” “checked,” “target-validated,” and “independently verified” are different project states.

## Data flow

```text
Project reality
    ↓
Intake and framing
    ↓
Profile + capability selection
    ↓
Bounded work packages
    ↓
Role outputs with evidence
    ↓
Adversarial review
    ↓
Closure matrix
    ↓
Decision / delivery / next experiment
    ↓
Persistent handoff
```

Contradictory evidence loops back to framing. It does not get sanded away during synthesis.

## Platform independence

The core is Markdown, JSON, and standard-library Python. An environment may add native subagents, browser tools, repositories, schedulers, or connectors, but the protocol does not require a specific vendor.

## Future adapters

Potential adapters may add:

- Work and Codex orchestration;
- GitHub issue and pull request state;
- Slack, email, and calendar operations;
- research database ingestion;
- scheduled operations;
- dashboards and provenance graphs;
- evaluation harnesses.

Adapters should remain outside the core protocol unless their behavior is platform-neutral.
