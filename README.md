# AWS Security Baseline With Control Tower

AWS multi-account security baseline using Control Tower, IAM Identity Center, central logging, guardrails, and Terraform.

This repository is a public reference pattern for designing a secure AWS landing zone. It is intentionally generic and does not include real account IDs, client data, internal policies, or company-specific configuration.

## 30-Second Adoption Path

Use the repository in this order:

1. **Define the account layout.** Start with [account structure](docs/account-structure.md) and decide which management, security, log archive, shared-services, and workload accounts your organisation requires.
2. **Define human access.** Review the [access model](docs/access-model.md), map job roles to IAM Identity Center permission sets, and document break-glass ownership before granting access.
3. **Establish central logging.** Review the Terraform under `terraform/logging-baseline/` and confirm the destination, retention, encryption, access, and monitoring requirements for CloudTrail and AWS Config data.
4. **Select baseline controls.** Use the [guardrails guide](docs/guardrails.md) and the examples under `terraform/security-controls/` to choose preventive and detective controls appropriate to each organisational unit and workload tier.
5. **Validate before adoption.** Replace every placeholder, run the local validation commands below, review the plan in a non-production environment, and retain the evidence listed in [security baseline evidence collection](docs/evidence-collection.md).

This is a reference architecture, not a production-ready landing-zone installer. Account IDs, regions, organisation units, log destinations, retention periods, permission scopes, control selections, and approval processes must be adapted and independently reviewed before deployment.

## What This Demonstrates

- AWS multi-account structure using Control Tower concepts
- Separation of security, logging, shared services, and workload accounts
- IAM Identity Center permission set design
- Centralized CloudTrail and AWS Config logging
- Guardrail-style preventive and detective controls
- Terraform examples for baseline security resources
- Governance model suitable for regulated SaaS environments

## Architecture

The reference architecture separates organisation governance, central audit storage, security findings, shared services, and workload environments into dedicated accounts. IAM Identity Center provides reviewed workforce access, while CloudTrail, AWS Config, and security findings flow to central accounts with restricted access.

See the [governance baseline architecture diagram](docs/architecture.md) for the account layout, logging flow, access relationships, responsibilities, and scope limitations.

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
├── .github/workflows/
│   └── validate.yml
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
│   ├── architecture.md
│   ├── guardrails.md
│   ├── access-model.md
│   ├── evidence-collection.md
│   ├── break-glass-drill.md
│   └── account-provisioning-checklist.md
├── scripts/
│   └── validate_examples.py
├── CONTRIBUTING.md
└── README.md
```

## Documentation

- [Account structure](docs/account-structure.md)
- [Governance baseline architecture](docs/architecture.md)
- [Access model](docs/access-model.md)
- [Guardrails](docs/guardrails.md)
- [Security baseline evidence collection](docs/evidence-collection.md)
- [Break-glass access drill guide](docs/break-glass-drill.md)
- [Account provisioning checklist](docs/account-provisioning-checklist.md)

## Design Principles

- Separate environments by AWS account where practical
- Centralize audit logs in a dedicated log archive account
- Use IAM Identity Center instead of long-lived IAM users
- Prefer role-based access with clear permission boundaries
- Apply security controls consistently across accounts
- Keep production access limited, approved, and auditable

## Validate Locally

Terraform 1.6 or later is required. These checks do not deploy resources, call AWS APIs, or require AWS credentials.

```bash
python3 scripts/validate_examples.py
terraform fmt -check -recursive terraform

for directory in terraform/*; do
  if [ -d "$directory" ]; then
    terraform -chdir="$directory" init -backend=false -input=false
    terraform -chdir="$directory" validate
  fi
done
```

The Python script checks JSON syntax, local Markdown links, and YAML tab indentation. GitHub Actions repeats the repository and Terraform checks in [`.github/workflows/validate.yml`](.github/workflows/validate.yml) using only read access to repository contents.

The examples intentionally contain placeholder account IDs, regions, names, retention values, organisation structures, and policy choices. Successful validation confirms formatting, provider initialisation, configuration structure, and local documentation links. It does not prove that a plan is safe for a particular AWS organisation, that controls meet a specific regulatory framework, or that the examples are production ready. Review a Terraform plan and the resulting security responsibilities independently before adoption.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on safe examples, placeholder values, review expectations, and useful contribution types.

## Status

This is a reference implementation for portfolio and architecture demonstration purposes. Replace placeholders and validate controls against your organisation's governance requirements before production use.
