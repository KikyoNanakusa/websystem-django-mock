variable "security_group_name" {
	description = "Name of the security group"
	type 		= string
}

variable "vpc_id" {
	description = "ID of the VPC"
	type 		= string
}

variable "allowed_ssh_cidr_blocks" {
	description = "CIDR blocks to allow SSH traffic"
	type 		= list(string)
	default 	= ["133.70.0.0/16"]
}

variable "allowed_django_cidr_blocks" {
	description = "CIDR blocks to allow Django traffic"
	type 		= list(string)
	default 	= ["133.70.0.0/16"]
}

variable "allowed_http_cidr_blocks" {
	description = "CIDR blocks to allow HTTP traffic"
	type 		= list(string)
	default 	= ["133.70.0.0/16"]
}
