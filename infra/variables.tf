variable "db_username" {
  description = "Username for the RDS database"
  type        = string
}

variable "db_password" {
  description = "Password for the RDS database"
  type        = string
}

variable "db_name" {
	description = "value of the database name"
	type = string
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-1"
}

variable "azs" {
	description = "Availability zones"
	type = list(string)
	default = ["ap-northeast-1a", "ap-northeast-1c"]
}

variable "key_pair_name" {
  description = "The key pair name for SSH access"
  type        = string
}

variable  "db_port" {
	description = "The port for the database"
  	type        = string
  	default     = "5432"
}

variable "django_secret_key" {
  description = "The secret key for Django"
  type        = string
}

# variable "web_system_public_key_path" {
#   description = "Path to the public key"
#   type        = string
# }