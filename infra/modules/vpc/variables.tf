
variable "vpc_cidr" {
	description = "VPC CIDR block"
	type = string
	default = "10.0.0.0/16"
}

variable "azs" {
	description = "Availability zones"
	type = list(string)
}