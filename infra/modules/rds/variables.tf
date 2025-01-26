variable "db_username" {
  description 	= "Username for the database"
  type			= string
}

variable "db_password" {
  description 	= "Password for the database"
  type			= string
}

variable "db_instance_class" {
  description = "The instance class for the RDS database"
  type        = string
  default     = "db.t3.micro"
}

variable "subnet_ids" {
	description = "The subnet IDs for the RDS subnet group"
	type        = list(string)
}

variable "rds_security_group_ids" {
	description = "The security group ID for the RDS instance"
	type        = list(string)
}