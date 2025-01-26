variable "ami_id" {
	description = "ID of the AMI to use"
	type        = string
}

variable "instance_type" {
	description = "Type of EC2 instance"
	type        = string
	default     = "t2.micro"
}

variable "key_pair_name" {
	description = "Name of the key pair to use"
	type        = string
}

variable "subnet_ids" {
	description = "The subnet IDs for the EC2 instance"
	type        = list(string)
}

variable "security_group_ids" {
	description = "The security group IDs for the EC2 instance"
	type        = list(string)
}

variable "db_endpoint" {
	description = "The endpoint of the RDS instance"
	type        = string
}

variable "db_name" {
	description = "The name of the database"
	type        = string
}

variable "db_user" {
	description = "The username for the database"
	type        = string
}

variable "db_password" {
	description = "The password for the database"
	type        = string
}

variable "db_port" {
	description = "The port for the database"
	type        = string
	default     = 5432
}

variable "django_secret_key" {
	description = "The secret key for Django"
	type        = string
}
