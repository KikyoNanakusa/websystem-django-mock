resource "aws_security_group" "django" {
	name = var.security_group_name
	description = "Security group for Django"
	vpc_id = var.vpc_id
	tags = {
		Name = var.security_group_name
	}

	ingress {
		description = "Allow SSH traffic"
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = var.allowed_ssh_cidr_blocks
	}

	ingress {
		description = "Allow Django traffic"
		from_port = 8000
		to_port = 8000
		protocol = "tcp"
		cidr_blocks = var.allowed_django_cidr_blocks
	}

	egress {
		description = "Allow all traffic"
		from_port = 0
		to_port = 0
		protocol = "-1" # all protocols
		cidr_blocks = ["0.0.0.0/0"]
	}
}

resource "aws_security_group" "rds" {
	name = "${var.security_group_name}-rds"
	description = "Security group for RDS"
	vpc_id = var.vpc_id
	
	egress {
		description = "Allow all traffic"
		from_port = 0
		to_port = 0
		protocol = "-1" # all protocols
		cidr_blocks = ["0.0.0.0/0"]
	}
}

resource "aws_security_group_rule" "rds" {
	description = "Allow postgres traffic"
	security_group_id = aws_security_group.rds.id
	source_security_group_id = aws_security_group.django.id
	type = "ingress"
	from_port = 5432
	to_port = 5432
	protocol = "tcp"
}

resource "aws_security_group_rule" "django-rds-ingress" {
	description = "Allow postgres traffic"
	security_group_id = aws_security_group.django.id
	source_security_group_id = aws_security_group.rds.id
	type = "ingress"
	from_port = 5432
	to_port = 5432
	protocol = "tcp"
}

resource "aws_security_group" "alb" {
	name = "${var.security_group_name}-alb"
	description = "Security group for ALB"
	vpc_id = var.vpc_id

	ingress {
		description = "Allow HTTP traffic"
		from_port = 80
		to_port = 80
		protocol = "tcp"
		cidr_blocks = var.allowed_http_cidr_blocks
	}

	egress {
		description = "Allow all traffic"
		from_port = 0
		to_port = 0
		protocol = "-1" # all protocols
		cidr_blocks = ["0.0.0.0/0"]
	}
}

resource "aws_security_group_rule" "alb-ec2-ingress" {
	description = "Allow Django traffic"
	security_group_id = aws_security_group.django.id
	source_security_group_id = aws_security_group.alb.id
	type = "ingress"
	from_port = 8000
	to_port = 8000
	protocol = "tcp"
}