# Baseline Control Exception Process

Security controls should be fixed or implemented as designed wherever practical. An exception is a temporary governance decision for a specific, documented case where the baseline cannot be met immediately without creating disproportionate operational or delivery risk.

An exception is not a permanent alternative to the baseline, a shortcut around review, or permission to weaken unrelated controls.

## When to Use an Exception

Consider an exception only when all of the following are true:

- the affected baseline control and scope are clearly identified;
- the reason the control cannot currently be met is documented;
- the resulting security risk is understood;
- compensating controls reduce the risk while the exception is active;
- an accountable owner and approver are named;
- the exception has an expiry date and review point;
- evidence can be retained without exposing secrets or sensitive production details.

Fix the control instead of requesting an exception when the gap is caused only by convenience, missing routine implementation work, or an avoidable configuration choice.

## Minimum Exception Record

Every exception should capture enough information for an independent reviewer to understand what is being accepted and for how long.

| Field | Required content |
| --- | --- |
| Exception ID | Internal ticket, risk, or change reference |
| Control | Exact baseline control or requirement affected |
| Scope | Accounts, organisational units, workloads, or environments covered |
| Justification | Why the control cannot currently be met |
| Risk | Security impact and plausible failure or abuse scenario |
| Compensating controls | Temporary measures that reduce likelihood or impact |
| Owner | Role accountable for remediation and review |
| Approver | Role authorised to accept the temporary risk |
| Start date | When the exception becomes effective |
| Expiry date | Date the exception automatically stops being valid |
| Review cadence | How often the exception is rechecked before expiry |
| Evidence | Sanitised references supporting the decision and controls |
| Remediation plan | Steps and target date for returning to the baseline |

Use placeholders in public examples. Do not publish real AWS account IDs, customer identifiers, credentials, private findings, or sensitive risk evidence.

## Review Flow

1. **Identify the control gap.** Record the exact control, affected scope, and current state.
2. **Challenge the need.** Confirm the baseline cannot reasonably be met now and that the exception is not being used for convenience.
3. **Assess the risk.** Describe likely abuse or failure scenarios and the expected impact.
4. **Define compensating controls.** Prefer controls that are measurable, monitored, and narrower than the original exposure.
5. **Set ownership and expiry.** Name an accountable role, a remediation owner, a review cadence, and a fixed expiry date.
6. **Obtain approval.** Route the decision through the organisation's normal security or risk-acceptance authority.
7. **Retain evidence.** Keep the approved record, supporting validation, and follow-up actions in the organisation's controlled system of record.
8. **Review until closure.** Remove the exception when the control is restored, the scope disappears, or the risk is no longer accepted.

For related evidence expectations, see [security baseline evidence collection](evidence-collection.md).

## Expiry, Renewal, and Revocation

Exceptions should expire automatically unless they are explicitly renewed before the expiry date. Renewal should require a fresh review of the risk, compensating controls, remaining scope, remediation progress, and continued business need.

Revoke an exception early when:

- the baseline control is restored;
- the compensating control fails or is removed;
- the affected scope changes materially;
- a security incident changes the risk assessment;
- the exception was based on incomplete or incorrect information.

Do not silently extend dates or copy old approvals into a new period without review.

## Emergency Handling

An urgent operational event may require a temporary deviation before the normal approval path is available. In that case:

- limit the scope and duration to the minimum necessary;
- retain monitoring and logging wherever possible;
- avoid disabling multiple independent controls to solve one problem;
- record who authorised the emergency action and why;
- complete retrospective risk review and formalise or revoke the exception as soon as the emergency ends.

Emergency privileged-access scenarios should also follow the [break-glass access drill guide](break-glass-drill.md) and the organisation's incident and change procedures.

## Example Exception Record

```text
Exception ID: EXAMPLE-001
Control: <baseline control>
Scope: <fictional workload or environment>
Justification: <temporary technical or operational constraint>
Risk: <plain-language security impact>
Compensating controls: <monitoring, restriction, manual review, or other temporary safeguards>
Owner: <accountable role>
Approver: <risk-acceptance role>
Start date: YYYY-MM-DD
Expiry date: YYYY-MM-DD
Review cadence: <for example, every 14 days>
Evidence: <sanitised ticket or test reference>
Remediation plan: <steps and target date to restore the baseline>
Status: Proposed / Approved / Revoked / Expired / Closed
```

## Relationship to the Baseline

The baseline remains the target state while an exception is active. Exceptions should be visible alongside the control inventory so reviewers can distinguish an intentionally accepted gap from an unknown or unmanaged one.

Use the [guardrails guide](guardrails.md) to identify the intended control outcome and keep exception evidence aligned with the [evidence collection guide](evidence-collection.md).
