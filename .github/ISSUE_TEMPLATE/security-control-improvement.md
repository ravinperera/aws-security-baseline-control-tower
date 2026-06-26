---
name: Security control improvement
description: Propose or improve an AWS baseline security control
title: "Control: "
labels: ["documentation"]
body:
  - type: markdown
    attributes:
      value: |
        Use this template for proposed improvements to AWS landing zone controls, guardrails, logging, access, or validation guidance.

  - type: textarea
    id: objective
    attributes:
      label: Control objective
      description: What risk does this control reduce?
      placeholder: Example: Ensure S3 public access is blocked by default across workload accounts.
    validations:
      required: true

  - type: textarea
    id: scope
    attributes:
      label: Scope
      description: Which account types, services, or environments does this apply to?
      placeholder: Example: Management, security, log archive, infrastructure, development, staging, and production accounts.
    validations:
      required: true

  - type: textarea
    id: implementation
    attributes:
      label: Proposed implementation
      description: Describe the documentation, Terraform example, or process change.
      placeholder: Example: Add a Terraform example using account-level S3 Public Access Block with safe placeholders.
    validations:
      required: true

  - type: textarea
    id: validation
    attributes:
      label: Validation approach
      description: How should the reader validate the control safely?
      placeholder: Example: Confirm the relevant AWS API returns block_public_acls, block_public_policy, ignore_public_acls, and restrict_public_buckets as true.
    validations:
      required: true

  - type: textarea
    id: safety
    attributes:
      label: Safety and privacy notes
      description: Confirm that the proposal avoids real account IDs, internal names, credentials, logs, and customer data.
      placeholder: Example: Uses only placeholder account IDs and generic account names.
    validations:
      required: true

  - type: textarea
    id: caveats
    attributes:
      label: Caveats
      description: Capture assumptions, service limitations, or organisation-specific decisions.
      placeholder: Example: Some controls may need exceptions for dedicated logging or delivery buckets.
