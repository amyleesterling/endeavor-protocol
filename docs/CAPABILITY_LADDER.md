# Capability Ladder

More agents are not automatically more intelligence. They can add breadth, independent attempts, tool concurrency, and verification. They can also add duplicated work, context loss, edit conflict, and false consensus.

Endeavor Protocol chooses the smallest sufficient capability mode.

## Auto

`auto` is a selection policy, not a fourth execution architecture.

Choose based on:

- number of separable workstreams;
- need for independent attempts;
- coupling between tasks;
- shared-file contention;
- latency and resource budget;
- tool availability;
- consequence of error;
- validation requirements.

## Solo mode

Use Solo when:

- the problem is one tightly coupled conceptual knot;
- a single coherent thread is valuable;
- the task is small;
- subagents are unavailable;
- parallel overhead would exceed benefit.

A Solo agent may execute roles sequentially:

```text
investigate → build → criticize → verify → synthesize
```

Label outputs as **sequential perspectives**, not independent findings.

## Delegated mode

Use Delegated when:

- workstreams can be bounded;
- agents can receive enough context without receiving everything;
- outputs can use a common return schema;
- separate attempts materially improve confidence;
- agents are unlikely to edit the same artifact concurrently.

Good delegation:

- separate literature domains;
- independent calculations;
- subsystem audits;
- test design versus implementation;
- audience analysis versus scientific fact checking;
- red-team review after a draft is frozen.

Poor delegation:

- five agents editing the same paragraph;
- tightly coupled architecture decisions with no integrator;
- vague assignments such as “look into everything”;
- duplicate agents whose results cannot be compared;
- agents whose output is accepted without evidence.

## Orchestrated mode

Use Orchestrated when the project needs durable coordination:

- recurring monitoring or triage;
- long-running experiments;
- persistent role ownership;
- scheduled checks;
- multiple repositories or systems;
- formal review queues;
- traceable automation.

Orchestration introduces operational risk. Define permissions, budgets, stop conditions, and review boundaries before activation.

## Independence labels

Use these exact distinctions when relevant:

- **Perspective:** same agent or shared context, different role or method.
- **Separate attempt:** distinct run or subagent, but substantial shared framing.
- **Independent verification:** checker did not rely on the primary conclusion and had access to the underlying evidence.
- **External validation:** evidence from the target environment, physical system, production system, or qualified outside reviewer.

## Delegation contract

Every delegated work package includes:

- objective;
- in-scope and out-of-scope boundaries;
- authoritative inputs;
- expected method;
- output schema;
- evidence standard;
- stop conditions;
- prohibited actions;
- deadline or budget when relevant.

## Synthesis rule

The orchestrator does not average conclusions. It compares evidence, methods, assumptions, and failure modes. Unresolved disagreements remain visible.
