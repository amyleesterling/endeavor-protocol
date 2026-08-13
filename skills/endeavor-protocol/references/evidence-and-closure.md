# Evidence and Closure

## Evidence classes

These classes describe the kind of support available. They are not universal rankings. A project should predeclare which class is required for each claim.

| Code | Evidence class | Example |
|---|---|---|
| **E0** | Assertion | A person or agent says the feature works |
| **E1** | Sourced | A primary document, dataset, specification, or direct record supports the claim |
| **E2** | Reproduced or inspected | A calculation is recomputed, a file is inspected, or an analysis is independently rerun |
| **E3** | Executed test | A defined test passes in a recorded environment |
| **E4** | Target-environment validation | The result works in production, with intended users, or on the physical system |
| **E5** | Independent verification | A meaningfully separate checker validates the underlying evidence without relying on the primary conclusion |

A claim may need several classes. A robot joint may require E1 specifications, E2 calculations, E3 bench tests, and E4 physical validation.

## Claim status

Use:

- unverified;
- supported;
- contradicted;
- partially supported;
- blocked;
- unknown;
- superseded.

## Closure states

| State | Meaning |
|---|---|
| **C0 Proposed** | Intended change or conclusion exists only as a proposal |
| **C1 Implemented** | Artifact or change exists |
| **C2 Checked** | Specified inspection, calculation, or test has been performed |
| **C3 Target-validated** | Result has been validated in the environment where it must work |
| **C4 Independently verified** | A separate checker confirms the required underlying evidence |
| **CX Deferred** | Explicitly not closing now, with rationale and owner |
| **CB Blocked** | Closure cannot proceed because a dependency or evidence requirement is missing |

Do not assume every project needs C4. Predeclare the required state.

## Evidence ledger fields

```text
Claim ID:
Claim:
Materiality:
Source or method:
Evidence class:
Environment:
Checker:
Status:
Confidence:
Limitations:
Required next validation:
Last updated:
```

## Closure matrix fields

```text
Item:
Owner:
Required closure:
Current closure:
Evidence:
Contradictions:
Blocker:
Next action:
Approval:
```

## Confidence

Confidence is a judgment about uncertainty. It is not evidence. Record it only after recording the evidence and limitations.

## Contradictions

When sources or checks disagree:

1. preserve both results;
2. compare scope, assumptions, versions, dates, units, and environments;
3. identify whether both can be true under different conditions;
4. design the smallest discriminating check;
5. mark the claim unresolved until the contradiction is addressed.

## Independent verification test

Call a check independent only when the verifier:

- did not merely inherit the primary conclusion;
- can inspect the underlying evidence;
- uses a meaningfully separate attempt, method, context, or qualified reviewer;
- reports its own limitations.

Multiple agents reading the same summary and agreeing do not satisfy this test.
