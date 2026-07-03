# Security Baseline Evidence Collection

This guide lists practical evidence to collect when reviewing an AWS Control Tower security baseline. It is designed for portfolio, audit-readiness, and architecture review discussions.

Use placeholders in public examples. Do not include real account IDs, user names, ticket references, client names, log excerpts, screenshots with sensitive data, or production configuration values.

## Evidence Checklist

| Control area | Useful evidence | Notes |
| --- | --- | --- |
| AWS Organizations and Control Tower | Account structure, enabled regions, organisational unit layout, guardrail summary | Redact account IDs and business-sensitive account names. |
| CloudTrail | Organisation trail status, multi-region setting, log file validation setting, destination bucket policy summary | Avoid sharing raw event logs. Use sanitized screenshots or command output. |
| AWS Config | Recorder status, delivery channel status, aggregator status, representative managed rules | Confirm all intended regions are covered. |
| IAM Identity Center | Permission set names, assignment model, MFA requirement, access review process | Use role names and placeholders instead of individual user details. |
| S3 public access blocking | Account-level and bucket-level public access block status for baseline buckets | Include exceptions only with documented approval and risk acceptance. |
| Break-glass access | Procedure location, MFA status, owner list, last test date, rotation evidence | Never publish credentials, recovery codes, or emergency access details. |
| Logging retention | Retention policy, lifecycle rule summary, immutability or write-protection approach | Use retention categories rather than client-specific requirements. |

## Suggested Review Questions

- Are baseline controls applied consistently across the management, security, log archive, infrastructure, and workload accounts?
- Are any regions excluded from logging or configuration recording, and is that documented?
- Are privileged permission sets reviewed on a regular cadence?
- Is break-glass access tested, monitored, and restricted to named owners?
- Are exceptions tracked with an owner, expiry date, and compensating control?

## Example Evidence Record

```text
Control: CloudTrail organisation trail
Environment: Example landing zone
Evidence date: YYYY-MM-DD
Evidence source: AWS console screenshot / AWS CLI output / Terraform state summary
Status: Implemented / Partial / Not implemented
Caveats: Sanitized public example; no real account IDs included
Reviewer: <role or placeholder>
```

## Public Repository Safety

This repository should stay generic. When adding evidence examples, use synthetic names such as `example-security-account`, `example-log-archive`, and `123456789012`. Remove or redact anything that could identify a real customer, production account, or internal control process.
