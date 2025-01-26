resource "aws_instance" "django" {
	count = length(var.subnet_ids)
	ami = var.ami_id
	instance_type = var.instance_type
	key_name = "websystem-key-pair"
	subnet_id = element(var.subnet_ids, count.index)
	vpc_security_group_ids = var.security_group_ids
	tags = {
		Name = "web-system-django-${count.index}"
	}
	user_data = <<-EOF
            	#!/bin/bash
				sudo yum update -y
				sudo yum install -y git
				sudo yum install -y python3
				sudo yum install -y pip
				sudo yum install -y nginx
				git clone https://github.com/KikyoNanakusa/websystem-django-mock
				cd websystem-django-mock
				pip install -r requirements.txt
				echo "DATABASE_HOST=${var.db_endpoint}" >> startup.sh
				echo "DATABASE_PORT=${var.db_port}" >> startup.sh
				echo "POSTGRES_DB=${var.db_name}" >> startup.sh
				echo "POSTGRES_USER=${var.db_user}" >> startup.sh
				echo "POSTGRES_PASSWORD=${var.db_password}" >> startup.sh
				echo "DJANGO_SECRET_KEY=${var.django_secret_key}" >> startup.sh
            	EOF
}