# Baseline Control Ownership And Evidence Matrix

This matrix turns the reference architecture into an operational control register. It is deliberately role-based and generic: adopters should map the example roles to their own accountable teams and retain evidence according to their governance and records-management requirements.

Use this together with the [evidence collection guide](evidence-collection.md), [guardrails guide](guardrails.md), and [control exception process](control-exceptions.md). A control should not be treated as complete merely because a Terraform example exists; ownership, operating evidence, scope, and review triggers also need to be defined.

## Reference Matrix

| Control | Type | Accountable role | Enforcement or implementation point | Minimum evidence | Review trigger |
| --- | --- | --- | --- | --- | --- |
| Privileged MFA | Preventive | IAM / Security owner | IAM Identity Center and identity-provider policy | Sanitized MFA policy/configuration summary and privileged-access review | Identity-provider change, privileged-role change, authentication incident |
| Workforce access through IAM Identity Center | Preventive | IAM owner | IAM Identity Center permission sets and assignments | Permission-set inventory and redacted assignment review | New role, permission-set change, new production account |
| Break-glass access | Recovery / detective | Security owner | Restricted emergency identities, monitoring, and recovery process | Drill record, ownership record, rotation/test evidence | Drill failure, owner change, credential recovery event, major incident |
| Organisation-wide CloudTrail | Detective | Cloud Platform / Security | Organisation trail, log destination, encryption, monitoring | Sanitized trail configuration and delivery/alert evidence | New region/account, trail or destination change, logging incident |
| AWS Config coverage | Detective | Cloud Platform / Security | Recorders, delivery channels, aggregators, conformance rules where used | Recorder/aggregator status and coverage review | New region/account, service expansion, recorder/config change |
| Central log archive | Preventive / detective | Security / Platform owner | Dedicated log archive account and protected storage | Bucket policy, encryption, retention/lifecycle, access-review evidence | Retention change, access-policy change, storage migration, audit finding |
| S3 Block Public Access | Preventive | Cloud Platform owner | Account-level and bucket-level public-access controls | Sanitized public-access-block status and approved exceptions | New account, storage pattern change, exception request |
| Least-privilege permission sets | Preventive | IAM owner | Permission-set definitions, approval process, periodic access review | Permission-set diff/review and stale-assignment removal evidence | Role change, new service access, production access change, access incident |
| Environment/account separation | Preventive | Cloud Platform / Architecture | AWS Organizations, OUs, account vending and provisioning controls | Approved account/OU diagram and completed provisioning checklist | New workload tier, account move, OU/control-policy change |
| Baseline control exceptions | Governance | Security risk owner | Exception register and compensating controls | Approved exception with owner, rationale, expiry, compensating control and closure evidence | Expiry, scope change, control restoration, incident involving exception |

## Minimum Record Per Control

For each adopted control, record at least:

- a stable control name or internal identifier;
- the accounts, OUs, regions, workloads, or identities in scope;
- an accountable owner and an operational owner if different;
- whether the control is preventive, detective, recovery, or governance-oriented;
- the implementation or enforcement point;
- the evidence source and most recent evidence date;
- the reviewer and review cadence;
- any active exception, compensating control, or remediation action; and
- the events that require reassessment before the next scheduled review.

## Review Rules

A useful ownership matrix should make gaps visible rather than hide them. Mark a control as partial when its technical configuration exists but ownership, coverage, evidence, or review responsibility is missing. Do not assign a generic team such as "Security" as both owner and reviewer for every control when independent review is expected by the organisation.

When a control changes materially, refresh the related evidence rather than carrying forward an old screenshot or configuration export. If the control cannot be restored promptly, use the documented [control exception process](control-exceptions.md) and retain the decision with the control record.

## Public Repository Safety

Do not commit real account IDs, employee names, ticket numbers, client names, screenshots, internal control identifiers, or production configuration exports to this repository. Use synthetic examples only; operational evidence belongs in the adopting organisation's approved evidence store.
