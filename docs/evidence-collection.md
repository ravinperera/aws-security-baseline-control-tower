# Security Baseline Evidence Collection

This guide provides a practical evidence checklist for reviewing an AWS Control Tower security baseline. It is designed for portfolio, audit-readiness, internal control, and architecture review discussions.

Use placeholders in public examples. Do not include real account IDs, user names, ticket references, client names, log excerpts, screenshots with sensitive data, or production configuration values.

## How to Use This Checklist

For each control, record the implementation status, evidence date, evidence owner, reviewer, and any exception or remediation action. Evidence should be recent enough to represent the current environment and retained according to the organisation's audit and records-management requirements.

Suggested statuses:

- **Implemented** — the control is operating as intended and current evidence is available.
- **Partial** — the control exists but has a coverage, ownership, or evidence gap.
- **Not implemented** — the control is absent or cannot be demonstrated.
- **Not applicable** — the control does not apply and the rationale is documented.

## Review Evidence Checklist

### Access controls

- [ ] IAM Identity Center is used for workforce access instead of long-lived IAM users.
- [ ] Privileged permission sets are limited, approved, and reviewed regularly.
- [ ] MFA requirements are documented and enforced for privileged access.
- [ ] Production access assignments have named owners and an approval trail.
- [ ] Break-glass access is restricted, monitored, rotated, and tested.
- [ ] Dormant assignments and unnecessary permissions are removed.

Useful artefacts to retain:

- Sanitized permission-set inventory
- Redacted assignment or access-review report
- MFA policy or configuration summary
- Approved production-access request example
- Break-glass drill record showing the date, outcome, and remediation actions

### Logging and monitoring

- [ ] An organisation-wide, multi-region CloudTrail trail is enabled.
- [ ] CloudTrail log file validation is enabled where required.
- [ ] AWS Config recorders and delivery channels cover all intended accounts and regions.
- [ ] Security findings are aggregated in the designated security account.
- [ ] Logging failures, disabled controls, and configuration drift generate alerts.
- [ ] Log retention and archive lifecycle settings match the agreed policy.

Useful artefacts to retain:

- Sanitized CloudTrail configuration output
- AWS Config recorder and aggregator status
- Security Hub, GuardDuty, or equivalent delegated-administrator summary
- Example alert with sensitive values removed
- Retention policy and S3 lifecycle configuration summary

### Configuration and governance

- [ ] The account and organisational-unit structure matches the approved design.
- [ ] Preventive and detective guardrails are recorded with owners and rationale.
- [ ] Required controls are applied consistently to workload accounts.
- [ ] Exceptions include an owner, business justification, expiry date, and compensating control.
- [ ] New-account provisioning includes baseline security checks.
- [ ] Terraform or other infrastructure-as-code changes receive review before deployment.

Useful artefacts to retain:

- Sanitized organisation and OU diagram
- Enabled-control or guardrail summary
- Completed account-provisioning checklist
- Redacted exception register entry
- Pull-request review showing infrastructure change approval
- Periodic control-review minutes or sign-off record

### Storage and data protection

- [ ] S3 Block Public Access is enabled at account level unless an approved exception exists.
- [ ] Baseline logging buckets prevent unintended public access.
- [ ] Encryption is enabled for audit logs and other security evidence.
- [ ] Access to the log archive is restricted and independently monitored.
- [ ] Versioning, retention, lifecycle, and deletion protections are documented.
- [ ] Backup or recovery expectations for security configuration are defined.

Useful artefacts to retain:

- Account-level and bucket-level public-access-block status
- Sanitized bucket policy and encryption configuration
- Object Lock, retention, or write-protection configuration summary where used
- Access-analyzer or equivalent findings summary
- Lifecycle and versioning configuration
- Documented recovery or restoration test result

## Evidence Register Template

| Control | Scope | Status | Evidence source | Evidence date | Owner | Reviewer | Exception or action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CloudTrail organisation trail | All accounts and enabled regions | Implemented | Sanitized CLI output | YYYY-MM-DD | Platform Security | Internal reviewer | None |
| Privileged permission-set review | Production accounts | Partial | Redacted access-review export | YYYY-MM-DD | IAM owner | Security lead | Remove two stale assignments by YYYY-MM-DD |
| S3 Block Public Access | Log archive account | Implemented | Configuration screenshot | YYYY-MM-DD | Cloud Platform | Internal reviewer | None |

## Suggested Review Questions

- Are baseline controls applied consistently across the management, security, log archive, infrastructure, and workload accounts?
- Are any accounts or regions excluded from logging or configuration recording, and is the rationale documented?
- Are privileged permission sets and production assignments reviewed on a regular cadence?
- Is break-glass access tested, monitored, and restricted to named owners?
- Are exceptions tracked with an owner, expiry date, compensating control, and closure evidence?
- Can each claimed control be supported by a current, independently reviewable artefact?

## Public Repository Safety

This repository should stay generic. When adding evidence examples, use synthetic names such as `example-security-account`, `example-log-archive`, and `123456789012`. Remove or redact anything that could identify a real customer, production account, employee, internal ticket, or control process.

Do not publish credentials, recovery codes, session details, raw event logs, real account identifiers, internal screenshots, or Terraform state files.