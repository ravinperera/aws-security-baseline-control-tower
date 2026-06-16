variable "cloudtrail_bucket_name" {
  description = "S3 bucket used for CloudTrail logs."
  type        = string
}

variable "config_bucket_name" {
  description = "S3 bucket used for AWS Config delivery."
  type        = string
}

variable "trail_name" {
  description = "CloudTrail name."
  type        = string
  default     = "organization-trail"
}

variable "is_organization_trail" {
  description = "Whether the trail is an AWS Organizations trail."
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags applied to supported resources."
  type        = map(string)
  default     = {}
}
