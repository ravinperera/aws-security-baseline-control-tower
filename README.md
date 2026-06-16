# AWS Security Baseline With Control Tower

AWS multi-account security baseline using Control Tower, IAM Identity Center, central logging, guardrails, and Terraform.

This repository is a public reference pattern for designing a secure AWS landing zone. It is intentionally generic and does not include real account IDs, client data, internal policies, or company-specific configuration.

## What This Demonstrates

- AWS multi-account structure using Control Tower concepts
- Separation of security, logging, shared services, and workload accounts
- IAM Identity Center permission set design
- Centralized CloudTrail and AWS Config logging
- Guardrail-style preventive and detective controls
- Terraform examples for baseline security resources
- Governance model suitable for regulated SaaS environments

## Example Account Structure

| Account | Purpose |
| --- | --- |
| Management | AWS Organizations and Control Tower administration |
| Security | Security tooling, delegated admin, findings aggregation |
| Log Archive | Immutable audit and activity log storage |
| Infrastructure | Shared networking, DNS, CI/CD support, observability |
| Development | Non-production workload environment |
| Staging | Pre-production validation environment |
| Production | Production workloads and customer-facing services |

## Baseline Controls

- MFA enforced for privileged access
- IAM Identity Center used for human access
- Break-glass access documented and restricted
- CloudTrail enabled across all accounts and regions
- AWS Config enabled for resource compliance visibility
- S3 public access blocked by default
- Centralized log archive account for audit evidence
- Least-privilege permission sets for platform, engineering, and read-only access
- Workloads separated by account and environment

## Repository Structure

```text
.
├── terraform/
│   ├── iam-identity-center/
│   │   ├── permission-sets.tf
│   │   └── variables.tf
│   ├── logging-baseline/
│   │   ├── cloudtrail.tf
│   │   ├── config.tf
│   │   └── variables.tf
│   └── security-controls/
│       ├── s3-public-access-block.tf
│       └── variables.tf
├── docs/
│   ├── account-structure.md
│   ├── guardrails.md
│   └── access-model.md
└── README.md
```

## Design Principles

- Separate environments by AWS account where practical
- Centralize audit logs in a dedicated log archive account
- Use IAM Identity Center instead of long-lived IAM users
- Prefer role-based access with clear permission boundaries
- Apply security controls consistently across accounts
- Keep production access limited, approved, and auditable

## Status

This is a reference implementation for portfolio and architecture demonstration purposes. Replace placeholders and validate controls against your organisation's governance requirements before production use.
