# Break-Glass Access Drill Guide

Break-glass access is emergency access for situations where normal privileged access paths are unavailable. This guide explains how to test the process safely without exposing credentials or production-sensitive details.

## Goals

- Confirm the emergency access path still works.
- Confirm ownership, MFA, monitoring, and escalation paths are documented.
- Confirm the access can be revoked, rotated, or returned to its normal locked state after the drill.
- Produce audit-ready evidence without publishing secrets or real account identifiers.

## Scope

A safe drill should normally validate process readiness rather than perform unnecessary production changes. Use a non-production or dedicated test path where possible.

Do not include real credentials, recovery codes, MFA seeds, named emergency users, production account IDs, or customer identifiers in public examples.

## Prerequisites

- Approved test window and named owner for the drill.
- Current break-glass procedure location is known.
- Emergency account ownership and MFA status are confirmed.
- Monitoring or alerting is enabled for emergency login activity.
- Rollback and credential rotation steps are documented.

## Drill Steps

1. Record the drill date, scope, owner, and expected outcome.
2. Confirm that the normal access route is documented and that break-glass use is justified only for emergency scenarios.
3. Validate the emergency login process using a safe test account or non-production path where possible.
4. Confirm MFA prompts, access boundaries, and alerting behaviour.
5. Confirm that no persistent access expansion was introduced.
6. Return access to its normal locked or restricted state.
7. Record evidence and follow-up actions.

## Evidence to Capture

| Evidence | Example format | Public-safe note |
| --- | --- | --- |
| Approval record | Ticket reference or review note | Use a placeholder in public docs. |
| Drill scope | Account category and control area | Avoid real account IDs. |
| MFA status | Confirmed / not confirmed | Do not publish MFA device details. |
| Alerting result | Alert received / alert missing | Do not include raw alert payloads. |
| Rollback result | Access returned to restricted state | Avoid screenshots containing identities. |
| Follow-up actions | Owner and due date | Use roles rather than real names in examples. |

## Follow-Up Actions

After the drill, record any gaps such as missing alerts, unclear ownership, outdated documentation, stale emergency users, or missing rotation evidence. Each gap should have an owner, due date, and severity.

## Example Drill Record

```text
Drill: Break-glass access readiness test
Date: YYYY-MM-DD
Scope: Example security account emergency access path
Outcome: Passed / Passed with actions / Failed
Evidence: Sanitized screenshot or command output reference
Follow-up: <action owner role> by <date>
Caveat: Public example only; no real credentials or account IDs included
```
