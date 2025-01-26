resource "aws_db_subnet_group" "main" {
  name       = "web-system-db-subnet-group"
  subnet_ids = var.subnet_ids
  tags = {
	Name = "web-system-db-subnet-group"
  }
}

resource "aws_db_instance" "main" {
	identifier = "web-system-rds"
	allocated_storage = 20
	engine = "postgres"
	engine_version = "15"
	instance_class = var.db_instance_class
	username = var.db_username
	password = var.db_password
	db_subnet_group_name = aws_db_subnet_group.main.name
	vpc_security_group_ids = var.rds_security_group_ids
	multi_az = true
	publicly_accessible = false
	skip_final_snapshot = false

	tags = {
		Name = "web-system-rds"
	}
}