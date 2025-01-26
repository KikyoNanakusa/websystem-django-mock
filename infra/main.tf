provider "aws" {
	region  = var.region
	profile = "default"
}

module "vpc" {
	source = "./modules/vpc"
	azs = var.azs
}

module "security_group" {
	source 				= "./modules/security_group"
	security_group_name = "web-system-sg"
	vpc_id 				= module.vpc.vpc_id
}

module "rds" {
	source 		= "./modules/rds"
	db_instance_class = "db.t3.micro"
	subnet_ids = module.vpc.public_subnet_ids
	rds_security_group_ids = [module.security_group.rds_security_group_id]
	db_username = var.db_username
	db_password = var.db_password
}

module "ec2" {
	source = "./modules/ec2"
	 ami_id = "ami-0b28346b270c7b165"
	instance_type = "t2.micro"
	key_pair_name = var.key_pair_name
	subnet_ids = module.vpc.public_subnet_ids
	security_group_ids = [module.security_group.django_security_group_id]
	db_endpoint = module.rds.db_endpoint
	db_name = var.db_name
	db_user = var.db_username
	db_password = var.db_password
	db_port = var.db_port
	django_secret_key = var.django_secret_key
}

module "alb" {
	source = "./modules/alb"
	subnet_ids = module.vpc.public_subnet_ids
	security_group_ids = [module.security_group.alb_security_group_id]
	vpc_id = module.vpc.vpc_id
	target_ids = module.ec2.ec2_instance_ids
}