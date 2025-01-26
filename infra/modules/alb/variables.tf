variable "security_group_ids" {
  description = "The security group IDs for the ALB"
  type        = list(string)
}

variable "subnet_ids" {
  description = "The subnet IDs for the ALB"
  type        = list(string)
}

variable "vpc_id" {
  description = "The VPC ID"
  type        = string
}

variable "target_ids" {
  description = "List of target instance IDs"
  type        = list(string)
}
